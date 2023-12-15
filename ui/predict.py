import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

# Function to predict capacitance based on focused features and a saved model
def predicted(focused_features, focused_features_data, saved_model):
    # Combine features and their corresponding data into a DataFrame
    combined_data = list(zip(focused_features, focused_features_data.flatten()))
    convert_df = pd.DataFrame(combined_data, columns=['Feature', 'Value'])
    
    # Transpose the DataFrame for prediction
    convert_df = convert_df.T
    convert_df.columns = convert_df.iloc[0]
    convert_df = convert_df[1:]
    
    # Predict capacitance using the saved model
    predicted_value = saved_model.predict(convert_df)[0]
    return predicted_value

# Function to plot the relationship between missing features and predicted capacitance
def plot_predicted(focused_features, focused_features_data, saved_model, df):
    input_features = {}

    # Create a dictionary of input features and their values
    for data, feature in zip(focused_features_data, focused_features):
        if data == '':
            input_features[feature] = None
        else:
            input_features[feature] = float(data)

    # Create a DataFrame from the input features
    input_df = pd.DataFrame([input_features])

    # Identify missing features in the input
    missing_features = input_df.columns[input_df.isnull().any()].tolist()
    all_graph = []

    # Loop through missing features and create plots
    for missing_feature in missing_features:
        imputed_values = df[missing_feature].mean()

        # Define feature ranges based on the missing feature
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

        # Create a DataFrame with varying values for the missing feature
        varying_feature_df = pd.DataFrame({missing_feature: feature_range})
        for col in input_df.columns:
            if col != missing_feature:
                varying_feature_df[col] = input_df[col][0]

        # Predict capacitance for varying feature values
        predicted_capacitance_varying = saved_model.predict(varying_feature_df)

        # Create a Plotly figure
        fig = go.Figure()

        # Add a scatter plot for predicted capacitance
        fig.add_trace(go.Scatter(x=feature_range, y=predicted_capacitance_varying,
                                 mode='lines', name='Predicted Capacitance (Imputed Feature)'))

        # Configure layout of the figure
        fig.update_layout(
            xaxis_title=missing_feature,
            yaxis_title='Predicted Specific capacitance (F/g)',
            title=f'Relationship between {missing_feature} and Predicted Capacitance',
            showlegend=True,
            autosize=True,
            width=1200,
            height=500,
        )

        # Generate HTML div for the plot
        div_plot = plot(fig, output_type="div")

        # Append plot information to the result list
        all_graph.append({'div_plot': div_plot, 'missing_feature': missing_feature})

    return all_graph
