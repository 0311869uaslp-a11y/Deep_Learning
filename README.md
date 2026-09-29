# Deep Learning

Repositorio académico con ejercicios, prácticas y experimentos desarrollados durante mi formación en **Deep Learning** como parte del programa de **Data Science & Artificial Intelligence de la Universidad Autónoma de San Luis Potosí (UASLP)**.

El repositorio documenta una progresión desde los fundamentos de redes neuronales y perceptrones hasta **Multilayer Perceptrons (MLP)** y **Convolutional Neural Networks (CNN)** aplicadas a problemas de regresión, clasificación y procesamiento de imágenes.

Los ejercicios incluyen experimentación con datasets reales, construcción y entrenamiento de modelos, análisis de overfitting y underfitting, preprocesamiento de datos e imágenes, y evaluación del comportamiento de diferentes arquitecturas neuronales.

---

## Contents

The repository covers topics including:

- Artificial Neural Networks
- Perceptrons
- Multilayer Perceptrons (MLP)
- Regression with neural networks
- Classification with neural networks
- Activation functions
- Neural-network architecture
- Training and optimization
- Overfitting and underfitting
- Model generalization
- Image preprocessing
- Convolutional Neural Networks (CNN)
- Image classification
- CIFAR experiments
- Practical applications with real datasets

---

# Neural Network Fundamentals

## Perceptron

The course begins with the **perceptron**, one of the fundamental building blocks of artificial neural networks.

A simplified neuron can be represented as:

```text
x1 ----\
x2 -----\                 +----------+
x3 ------> Weighted Sum ->| Activation |----> Output
... -----/                +----------+
xn ----/
```

Mathematically:

```text
z = w1*x1 + w2*x2 + ... + wn*xn + b
```

followed by an activation function:

```text
y = f(z)
```

These exercises provide the foundations for understanding how neural networks transform input variables into predictions.

---

# Multilayer Perceptrons

The repository includes exercises using **Multilayer Perceptrons (MLP)**.

Unlike a single perceptron, an MLP contains one or more hidden layers:

```text
Input Layer
     |
     v
Hidden Layer
     |
     v
Hidden Layer
     |
     v
Output Layer
```

The hidden layers allow the network to learn nonlinear relationships between input variables and the target.

The practical exercises explore MLPs for both **regression and prediction problems**.

---

# Regression with Neural Networks

Several exercises apply neural networks to regression problems.

The general workflow is:

```text
Dataset
   |
   v
Data Preprocessing
   |
   v
Feature Selection
   |
   v
Neural Network
   |
   v
Training
   |
   v
Prediction
   |
   v
Model Evaluation
```

These exercises demonstrate how neural networks can approximate nonlinear relationships in structured datasets.

---

## Brooklyn Property Dataset

One of the practical exercises applies an **MLP regression model to property data from Brooklyn**.

The objective is to use structured real-estate variables to learn relationships between property characteristics and a continuous target.

The exercise demonstrates:

- Data preprocessing
- Selection of predictor variables
- Neural-network regression
- Model training
- Prediction of continuous values
- Evaluation of regression behavior

This example provides experience applying neural networks beyond image classification to **tabular regression problems**.

---

## SaratogaHouses Dataset

Another exercise uses the **SaratogaHouses** dataset for regression.

The workflow explores how housing characteristics can be processed and supplied to a neural network for prediction.

```text
Housing Features
       |
       v
Data Preparation
       |
       v
      MLP
       |
       v
Predicted Value
```

This exercise reinforces the application of multilayer neural networks to structured numerical data.

---

# Classification with Neural Networks

The repository also contains classification exercises where a neural network learns to assign observations to predefined categories.

The general process is:

```text
Input Features
      |
      v
Neural Network
      |
      v
Class Probabilities
      |
      v
Predicted Class
```

These exercises complement regression examples by demonstrating how neural networks can solve different types of supervised-learning problems.

---

## Wine Dataset

The **Wine dataset** is used in exercises related to perceptrons and neural-network classification.

The exercise provides experience with:

- Numerical input features
- Class labels
- Data preparation
- Neural-network training
- Classification
- Model evaluation

This dataset provides a compact example for understanding how neural networks separate observations belonging to different classes.

---

# Neural Network Architecture

The course explores the basic structure of Artificial Neural Networks.

A typical feed-forward network can be represented as:

```text
             Hidden Layer
            /     |      \
           /      |       \
Input ----> O ---- O ---- O ----> Output
           \      |       /
            \     |      /
```

Important architectural concepts include:

- Input neurons
- Hidden layers
- Output neurons
- Weights
- Bias terms
- Activation functions
- Number of neurons per layer
- Network depth

Changing these parameters affects model complexity, training behavior and generalization.

---

# Training Process

Neural-network training consists of iteratively adjusting model parameters to minimize a loss function.

Conceptually:

```text
Input Data
    |
    v
Forward Pass
    |
    v
Prediction
    |
    v
Calculate Loss
    |
    v
Backpropagation
    |
    v
Update Weights
    |
    +----------------+
                     |
                     v
               Next Iteration
```

This iterative process allows the model to learn patterns from training data.

---

# Overfitting and Underfitting

The repository includes material and exercises related to **overfitting and underfitting**, two fundamental concepts in Machine Learning and Deep Learning.

## Underfitting

A model underfits when it is too simple to capture the underlying structure of the data.

```text
Training Error   -> High
Validation Error -> High
```

## Good Generalization

A well-trained model captures useful patterns while maintaining performance on unseen data.

```text
Training Error   -> Low
Validation Error -> Low
```

## Overfitting

A model overfits when it learns the training data too closely and fails to generalize.

```text
Training Error   -> Very Low
Validation Error -> Higher
```

Understanding this trade-off is fundamental when designing and evaluating neural networks.

---

# Computer Vision

The course progresses from structured datasets to **image-processing and computer-vision problems**.

Images introduce additional complexity because spatial relationships between pixels contain important information.

```text
Image
  |
  v
Pixel Representation
  |
  v
Preprocessing
  |
  v
Neural Network
  |
  v
Classification
```

---

# Image Preprocessing

The repository contains exercises related to preparing image data for neural-network models.

Image preprocessing is an important stage because neural networks require numerical tensors with consistent dimensions and representations.

The workflow can be summarized as:

```text
Raw Images
    |
    v
Image Loading
    |
    v
Preprocessing
    |
    v
Numerical Tensors
    |
    v
Neural Network
```

These exercises provide the foundation for later work with convolutional neural networks.

---

# Convolutional Neural Networks

The repository includes practical work with **Convolutional Neural Networks (CNNs)**.

CNNs are specifically designed to learn spatial patterns from image data.

A simplified architecture can be represented as:

```text
Input Image
     |
     v
Convolution
     |
     v
Activation
     |
     v
Pooling
     |
     v
Convolution
     |
     v
Pooling
     |
     v
Flatten
     |
     v
Dense Layers
     |
     v
Classification
```

Convolutional layers learn local visual patterns, while deeper layers can progressively learn more complex representations.

---

# Image Classification

CNN exercises explore the complete image-classification workflow:

```text
Image Dataset
      |
      v
Preprocessing
      |
      v
Train / Validation Data
      |
      v
CNN Architecture
      |
      v
Model Training
      |
      v
Evaluation
      |
      v
Image Classification
```

This provides practical experience moving from raw image data to trained classification models.

---

# CIFAR Experiments

The repository includes exercises involving **CIFAR image data**.

CIFAR provides a multi-class image-classification problem useful for experimenting with convolutional neural networks.

These exercises explore:

- Image datasets
- Input tensor preparation
- CNN architectures
- Model training
- Multi-class classification
- Evaluation of predictions
- Generalization to unseen images

The experiments demonstrate the difference between working with conventional tabular datasets and high-dimensional image data.

---

# Animal Image Classification

The repository also contains material related to **animal image classification using convolutional neural networks**.

The general pipeline is:

```text
Animal Images
      |
      v
Image Preprocessing
      |
      v
Training Dataset
      |
      v
Convolutional Neural Network
      |
      v
Feature Learning
      |
      v
Classification
```

This exercise provides a practical example of applying CNNs to visual recognition.

---

# From Traditional Neural Networks to CNNs

The exercises in the repository illustrate a natural progression:

```text
Perceptron
    |
    v
Artificial Neural Network
    |
    v
Multilayer Perceptron
    |
    +------------------+
    |                  |
    v                  v
Regression        Classification
    |                  |
    +---------+--------+
              |
              v
        Deep Networks
              |
              v
       Image Processing
              |
              v
             CNN
              |
              v
     Image Classification
```

This progression demonstrates how the same fundamental concepts of weighted connections, activation functions and optimization evolve into architectures capable of learning complex representations from images.

---

# Skills Developed

Through the exercises in this repository, the course develops practical knowledge in:

- Neural networks
- Perceptrons
- Multilayer Perceptrons
- Supervised learning
- Regression
- Classification
- Neural-network architecture
- Model training
- Model evaluation
- Overfitting and underfitting
- Model generalization
- Image preprocessing
- Convolutional Neural Networks
- Computer vision
- Image classification
- Python-based Machine Learning
- TensorFlow/Keras

---

# Relationship with Data Science

Deep Learning forms part of a broader Data Science workflow.

```text
Raw Data
   |
   v
Data Processing
   |
   v
Exploratory Analysis
   |
   v
Feature Preparation
   |
   v
Machine Learning / Deep Learning
   |
   v
Model Evaluation
   |
   v
Prediction
```

The exercises in this repository complement other areas of my Data Science training, including:

- Machine Learning
- Data Mining
- Statistical analysis
- Graph Theory
- NoSQL databases
- Data preprocessing
- Artificial Intelligence

Together, these areas provide a foundation for developing data-driven models for structured data, images and engineering applications.

---

# Academic Context

This repository contains coursework developed as part of my specialized training in:

**Data Science & Artificial Intelligence**  
**Universidad Autónoma de San Luis Potosí (UASLP)**  
San Luis Potosí, Mexico

The complete training program comprised **195 hours** and covered Machine Learning, Data Mining, Deep Learning, Artificial Intelligence, Graph Theory and related computational methods.

---

# Repository Purpose

The purpose of this repository is to preserve and document the practical exercises completed during the Deep Learning course while demonstrating the progression from basic neural-network concepts to more advanced image-classification architectures.

The repository serves as evidence of practical academic training in:

```text
Neural Networks
      ↓
MLP
      ↓
Regression & Classification
      ↓
Model Generalization
      ↓
Image Processing
      ↓
CNN
      ↓
Computer Vision
```

---

# Author

**José Luis Romero Vázquez**

Electronics Engineer and Data Scientist with international graduate education in Electronic Engineering, Telecommunications and Computer Networks, with applied experience in Machine Learning, time-series forecasting, IoT analytics, research and software development.

**LinkedIn:**  
https://www.linkedin.com/in/jose-luis-romero-vazquez-486569209

**GitHub:**  
https://github.com/0311869uaslp-a11y
