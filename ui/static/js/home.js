document.addEventListener("DOMContentLoaded", function() {
    // Selecting elements
    const form = document.querySelector("form[name='calculate_form']");
    const inputFields = form.querySelectorAll("input[type='text']");
    const submitButton = form.querySelector("button[type='submit']");

    // Function to check if a value is numeric
    function isNumeric(value) {
        return !isNaN(value.trim());
    }

    // Function to check if all input fields are numeric
    function isFormValid() {
        let allNumeric = true;
        inputFields.forEach(function(input) {
            // Reset custom validity
            input.setCustomValidity('');

            // Validate numeric inputs
            const inputValue = input.value.trim();
            if(inputValue == '-'){inputValue=''}
            if (!isNumeric(inputValue)) {
                allNumeric = false;
                input.setCustomValidity('Please fill in as a number or decimal only');
            } 
            else if(input.name=='ssa'){
                if (input.value.trim()==''){
                    // Add custom validation logic for 'ssa' input
                    input.setCustomValidity('This field can not be empty!');
                    allNumeric = false;
                }
                else if(input.value <0 || input.value > 2650){
                    // Validate specific input ranges
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
                // Validate specific input ranges
                else if(input.value <0 || input.value > 15){
                    input.setCustomValidity('Input value must be between 0 and 15');
                    allNumeric = false;
                }

            }
            else if (input.name == 'nitrogen' || input.name == 'sulphur' || input.name == 'ag') {
                // Validate specific input ranges
                if (input.value < 0 || input.value > 15){
                    input.setCustomValidity('Input value must be in between 0 and 15');
                    allNumeric = false;
                }
            }
            else if (input.name == 'oxygen' ) {
                // Validate specific input ranges
                if (input.value < 0 || input.value > 30){
                    input.setCustomValidity('Input value must be in between 0 and 30');
                    allNumeric = false;
                }
            }
            else if (input.name == 'idig' ) {
                // Validate specific input ranges
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

    // Initial state
    submitButton.disabled = !isFormValid();

    // Event listener for input fields
    inputFields.forEach(function(input) {
        input.addEventListener("input", function() {
            // Check validity in real-time
            isFormValid();
            submitButton.disabled = !isFormValid();
        });

        input.addEventListener("change", function() {
            // Trigger custom validity check on change
            input.reportValidity();
        });
    });

    // Event listener for form submission
    form.addEventListener('submit', function(event) {
        // Check validity before submitting
        if (!isFormValid()) {
            // Prevent form submission if not valid
            event.preventDefault();
        }
    });

    const clearButton = document.querySelector("button[type='reset']");
    clearButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the default behavior (form submission)
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

// Function to display/hide graphs based on selected feature
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

// Function to show loading indicator when calculating
function calculate() {
    document.getElementById('loading').style.display = 'block';
}
