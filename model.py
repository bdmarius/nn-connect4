import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical


class ConnectFourModel:

    def __init__(self, numberOfInputs, numberOfOutputs, batchSize, epochs):
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.batchSize = batchSize
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Dense(42, activation='relu', input_shape=(numberOfInputs,)))
        self.model.add(Dense(42, activation='relu'))
        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer="rmsprop", metrics=['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, num_classes=3)
        limit = int(0.8 * len(X))
        X_train = X[:limit]
        X_test = X[limit:]
        y_train = y[:limit]
        y_test = y[limit:]
        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]