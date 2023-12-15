document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form[name='calculate_form']");
    const inputFields = form.querySelectorAll("input[type='text']");
    const submitButton = form.querySelector("button[type='submit']");

    function isNumeric(value) {
        return !isNaN(value.trim());
    }


    function isFormValid() {
        let allNumeric = true;
        inputFields.forEach(function(input) {
            input.setCustomValidity('');
            const inputValue = input.value.trim();
            if(inputValue == '-'){inputValue=''}
            if (!isNumeric(inputValue)) {
                allNumeric = false;
                input.setCustomValidity('Please fill in as a number or decimal only');
            } 
            else if(input.name=='ssa'){
                if (input.value.trim()==''){
                    input.setCustomValidity('This field can not be empty!');
                    allNumeric = false;
                }
                else if(input.value <0 || input.value > 2650){
                    input.setCustomValidity('Input value must be between 0 and 2650');
                    allNumeric = false;
                }

            }
            else if(input.name=='ph'){
                console.log(input.value);
                if (input.value.trim()==''){
                    input.setCustomValidity('This field can not be empty!');
                    allNumeric = false;
                }
                else if(input.value <0 || input.value > 15){
                    input.setCustomValidity('Input value must be between 0 and 15');
                    allNumeric = false;
                }

            }
            else if (input.name == 'nitrogen' || input.name == 'sulphur' || input.name == 'ag') {
                if (input.value < 0 || input.value > 15){
                    input.setCustomValidity('Input value must be in between 0 and 15');
                    allNumeric = false;
                }
            }
            else if (input.name == 'oxygen' ) {
                if (input.value < 0 || input.value > 30){
                    input.setCustomValidity('Input value must be in between 0 and 30');
                    allNumeric = false;
                }
            }
            else if (input.name == 'idig' ) {
                if (input.value < 0 || input.value > 3){
                    input.setCustomValidity('Input value must be in between 0 and 3');
                    allNumeric = false;
                }
            }
            else {
                input.setCustomValidity('');
            }
        });
        return allNumeric;
    }

    submitButton.disabled = !isFormValid();

    inputFields.forEach(function(input) {
        input.addEventListener("input", function() {
            isFormValid();
            submitButton.disabled = !isFormValid();
        });

        input.addEventListener("change", function() {
            input.reportValidity();
        });
    });

    form.addEventListener('submit', function(event) {
        if (!isFormValid()) {
            event.preventDefault();
        }
    });

    const clearButton = document.querySelector("button[type='reset']");
    clearButton.addEventListener('click', function(event) {
        event.preventDefault(); 
        clearForm();
    });

    // Clear function
    function clearForm() {
        inputFields.forEach(input => {
            input.value = '';
        });
        inputFields.forEach(input => {
            input.setCustomValidity('');
        });
        submitButton.disabled = !isFormValid();
    }

});



function displayGraph() {
    const featureSelect = document.getElementById('feature-option');   
    const selectedFeature = featureSelect.value;

    const showGraphDivs = document.querySelectorAll('.show_graph');

    showGraphDivs.forEach(graphDiv => {
        const graphFeature = graphDiv.getAttribute('data-missing-value');

        if (graphFeature === selectedFeature) {
            graphDiv.style.display = '';  
        } else {
            graphDiv.style.display = 'none';  
        }
        

    });
  
}

function calculate(){
    document.getElementById('loading').style.display = 'block';
}
