import ssl 
#configuring ssl to ignore certification errors
#means the script can download datasets from the internet without encountering SSL errors
ssl._create_default_https_context = ssl._create_unverified_context

#tensorflow is a library for building and training the machine learning model
import tensorflow as tf 


#the MNSIT dataset contains images of handwritten digits
from tensorflow.keras.datasets import mnist


#a plotting library used to display images
import matplotlib.pyplot as plt


# Sequential,Dense,Flatten are the components from tensor flow used to build and structure the network
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten


#these are the libraries used for image processing
from PIL import Image, ImageOps

#a numpy library for numerical operations
import numpy as np



# Load the dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()



# Normalize the data
# this makes the data easier for model to process
x_train, x_test = x_train / 255.0, x_test / 255.0



# Display the first image in the training dataset
# show the first picture in our training set in shadses of gray
plt.imshow(x_train[0], cmap='gray')
# displsy picture on screen
plt.show()


# Build the model
# sequential component which tells our computer to do things in sequential manner
model = Sequential([
    #tourn our 2D picture into a 1D list of numbers so the computer can process it
Flatten(input_shape=(28, 28)),
    # dense is a like of layer of neuron cells
Dense(128, activation='relu'),
Dense(10, activation='softmax')
])
# Compile the model
# adam is like a smart coach that helps computer learn and improve the model's performance
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])

# train thr model
model.fit(x_train, y_train, epochs=30) #epochs are iterations

# Evaluate the model
# testing the model using testing data
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Function to preprocess the image
def preprocess_image(image_path):  # convert the image to grayscale
    img = Image.open(image_path).convert('L')
    img = ImageOps.invert(img)
    img = img.resize((28, 28)) #resizing it to 28*28 pixels
    img = np.array(img) / 255.0 #normalizing 
    img = img.reshape(1, 28, 28) #reshaping the model
    return img 


# Path to the handwritten digit image
image_path = 'digit.png'
new_image = preprocess_image(image_path) 

# Predict the digit
prediction = model.predict(new_image) #preprocessed image is passed to model for prediction
predicted_digit = np.argmax(prediction) 
print(f"Predicted Digit: {predicted_digit}")

plt.imshow(new_image.reshape(28, 28), cmap='gray')
plt.title(f"Predicted Digit: {predicted_digit}")
plt.show()



