import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a simple feedforward neural network
def create_feedforward_nn(input_dim, hidden_units, output_dim):
    model = Sequential()
    model.add(Dense(hidden_units, input_dim=input_dim, activation='relu'))
    model.add(Dense(output_dim, activation='softmax'))
    return model

# Example usage
input_dim = 10  # Number of input features
hidden_units = 20  # Number of units in the hidden layer
output_dim = 2  # Number of output classes

# Create the feedforward neural network
model = create_feedforward_nn(input_dim, hidden_units, output_dim)

# Display the network architecture
model.summary()
