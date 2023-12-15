from django.shortcuts import render, redirect
from django.http import FileResponse
import ui.models as model
import matplotlib.pyplot as plt
from io import BytesIO
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import joblib
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from .predict import predicted,plot_predicted
import numpy as np

plt.switch_backend('Agg')

df = pd.read_csv('data/final_supercapacitor.csv')
model_ensemble = joblib.load('saved_ensemble_model/saved_ensemble_model.pkl')
df.to_pickle('data/df.pkl')
loaded_df = pd.read_pickle('data/df.pkl')

with open('data/df.pkl', 'rb') as file:
    X_train = pickle.load(file)

cv = CountVectorizer()
cv.fit(X_train)

# Create your views here.
def login(request):
    login = True
    check_login = request.session.get('login')
    if check_login == 'incorrect_login':
        del request.session['login']
        return render(request, "login.html",{"login":login,'incorrect_login':True})
    
    elif check_login == 'email_already_existed':
        del request.session['login']
        return render(request, "login.html",{"login":login,'email_already_existed':True})
    
    elif check_login == 'username_already_existed':
        del request.session['login']
        return render(request, "login.html",{"login":login,'username_already_existed':True})
    
    elif check_login == 'password_not_match':
        del request.session['login']
        return render(request, "login.html",{"login":login,'password_not_match':True})
    
    elif check_login == 'not_login':
        del request.session['login']
        return render(request, "login.html",{"login":login,'not_login':True})
    
    else:
        return render(request, "login.html",{"login":login})

def home(request):
    username = request.session.get('user')
    if username is not None:
        if request.method == "POST":
            ph          = request.POST.get("ph").strip()
            ssa         = request.POST.get("ssa").strip()
            idig        = request.POST.get("idig").strip()
            nitrogen    = request.POST.get("nitrogen").strip()
            oxygen      = request.POST.get("oxygen").strip()
            sulphur     = request.POST.get("sulphur").strip()
            ag          = request.POST.get("ag").strip()
            predicted_value =   '-'
            all_graph       =   None

            focused_features = ['SSA (m2/g)', 'ID/IG', '%N', '%O', '%S', 'Current density (A/g)', 'Calculated pH']
            focused_features_data = [ssa, idig, nitrogen, oxygen, sulphur, ag, ph]

            has_none_value = False
            for value in focused_features_data:
                if value == '':
                    has_none_value = True

            focused_features_data = np.array(focused_features_data)

            if has_none_value:
                all_graph = plot_predicted(focused_features, focused_features_data ,model_ensemble,df)
            else:
                for i in range(len(focused_features_data)):
                    focused_features_data[i] = float(focused_features_data[i])
                predicted_value = predicted(focused_features, focused_features_data ,model_ensemble)
            

            if predicted_value != '-' :
                predicted_value = round(predicted_value, 2)


            context = {'predict_num': predicted_value,
                        'ssa':ssa,
                         'idig':idig,
                         'nitrogen':nitrogen,
                         'o2':oxygen,
                         'sulphur':sulphur, 
                         'ag':ag,
                         'ph':ph,
                         'predicted_value':predicted_value,
                         'all_graph':all_graph,
                         'predicted' : True,
                         'home':True
                         }
            create_model = model.Calculate_Data.objects.create(
                username = request.session.get('user'),
                ph              = str(ph),
                ssa             = str(ssa),
                id_ig_ratio     = str(idig),
                nitrogen        = str(nitrogen),
                oxygen          = str(oxygen),
                sulphur         = str(sulphur),
                density         = str(ag),
                predicted_value = str(predicted_value)
            )

            create_model.save()
                    
                        
            return render(request, "home.html",context)
        else:
            return render(request, "home.html",{'predict_num': '-','home':True})
    else:
        return redirect('/')
    

def about(request):
    return render(request, "about.html")

def help(request):
    pdf_path = 'pdf/UserManual.pdf'
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    return response

def log(request):
    username = request.session.get('user')
    if(username is None):
        return redirect('/')

    test_data = list(reversed(model.Calculate_Data.objects.filter(username = username)))
    items_per_page = 20
    paginator = Paginator(test_data, items_per_page)
    page = request.GET.get('page')

    try:
        test_data_page = paginator.page(page)

    except PageNotAnInteger:
        test_data_page = paginator.page(1)

    except EmptyPage:
        test_data_page = paginator.page(paginator.num_pages)

    return render(request, 'log.html', {'test_data_page': test_data_page,'username':username,'log':True})
    
def handle_login(request):
    incorrect_login = False
    login_page = True
    if request.method == 'POST':
        if 'login_form' in request.POST:
            username_post = request.POST.get('username_login')
            password_post = request.POST.get('password_login')

            user = model.User.objects.filter(username = username_post).first()
            email = model.User.objects.filter(email = username_post).first()

            if user is not None:
                print(user.password)
                if user.password == password_post:
                    request.session['user'] = user.username
                    return redirect("ui:home")
                else:    
                    incorrect_login = True  
                    request.session['login'] = 'incorrect_login'
                    return redirect('ui:login')
            elif email is not None:
                if email.password == password_post:
                    request.session['user'] = email.username
                    return redirect("ui:home")
                else:    
                    incorrect_login = True  
                    request.session['login'] = 'incorrect_login'
                    return redirect('ui:login')
            else:
                incorrect_login = True  
                request.session['login'] = 'incorrect_login'
                return redirect('ui:login')
          
        elif 'signup_form' in request.POST:
            username = request.POST.get('username_signup')
            email = request.POST.get('email_signup')
            password = request.POST.get('password_signup')
            con_pass = request.POST.get('confirm_password_signup')

            if model.User.objects.filter(email=email).exists():
                request.session['login'] = 'email_already_existed'
                return redirect('ui:login')

            if model.User.objects.filter(username=username).exists():
                request.session['login'] = 'username_already_existed'
                return redirect('ui:login')
            if password == con_pass:
                user = model.User.objects.create(
                    username = username,
                    email = email,
                    password = password,
                )
                user.save()

                request.session['user'] = user.username
                return render(request, "home.html", {"username": username})
            else:
                request.session['login'] = 'password_not_match'
                return redirect('ui:login')

def logout(request):
    del request.session['user']
    return redirect('ui:login')




