import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

def predicted(focused_features, focused_features_data ,saved_model):
    combined_data = list(zip(focused_features, focused_features_data.flatten()))
    convert_df = pd.DataFrame(combined_data, columns=['Feature', 'Value'])
    convert_df = convert_df.T
    convert_df.columns = convert_df.iloc[0]
    convert_df = convert_df[1:]
    predicted_value = saved_model.predict(convert_df)[0]  
    return predicted_value

def plot_predicted(focused_features, focused_features_data ,saved_model,df):
    input_features = {}
    for data, feature in zip(focused_features_data, focused_features):
        if data == '':
            input_features[feature] = None
        else:
            input_features[feature] = float(data)

    input_df = pd.DataFrame([input_features])
    missing_features = input_df.columns[input_df.isnull().any()].tolist()
    all_graph = []
    for missing_feature in missing_features:
            imputed_values = df[missing_feature].mean()
            if missing_feature == '%N':
                feature_range = np.linspace(0, 15, num=100)
            elif missing_feature == '%O':
                feature_range = np.linspace(0, 30, num=100)
            elif missing_feature == '%S':
                feature_range = np.linspace(0, 15, num=100)
            elif missing_feature == 'ID/IG':
                feature_range = np.linspace(0, 3, num=100)
            elif missing_feature == 'Current density (A/g)':
                feature_range = np.linspace(0, 15, num=100)
            else:
                feature_range = np.linspace(imputed_values - 10, imputed_values + 10, num=100)

            varying_feature_df = pd.DataFrame({missing_feature: feature_range})
            for col in input_df.columns:
                if col != missing_feature:
                    varying_feature_df[col] = input_df[col][0]

            predicted_capacitance_varying = saved_model.predict(varying_feature_df)

            fig = go.Figure()

            fig.add_trace(go.Scatter(x=feature_range, y=predicted_capacitance_varying,
                                     mode='lines', name='Predicted Capacitance (Imputed Feature)'))

            fig.update_layout(
                xaxis_title=missing_feature,
                yaxis_title='Predicted Specific capacitance (F/g)',
                title=f'Relationship between {missing_feature} and Predicted Capacitance',
                showlegend=True,
                autosize=True,
                width=1200,  
                height=500,
                 
            )

            div_plot = plot(fig, output_type="div")

            all_graph.append({'div_plot': div_plot, 'missing_feature': missing_feature})

    return all_graph