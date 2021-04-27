import numpy as np
from PyES import ES
from tensorflow.keras.datasets import mnist

def relu(x):
    return np.maximum(x, 0)

def softmax(x):
    r = np.exp(x - np.max(x))
    return r / r.sum()

def predict(dna, x):
    mat_1 = dna[:input_size*hidden_size].reshape(-1, input_size)
    mat_2 = dna[input_size*hidden_size:].reshape(10, -1)
    return np.argmax(softmax(np.dot(mat_2, relu(np.dot(mat_1, x)))))



input_size = 784
hidden_size = 32
output_size = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = (x_train.astype("float32")/255).reshape(-1, input_size)
x_test = (x_test.astype("float32")/255).reshape(-1,input_size)




dna = np.random.randn(input_size*hidden_size+hidden_size*output_size)

optimizer = ES("acc", predict, 50, 0.1, 0.05, 10)
optimizer.fit(dna, x_train[:2000], y_train[:2000])