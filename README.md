# Personality Prediction Using Facial Images  

## Project Overview  
This project explores personality prediction using a single portrait image. The system leverages **Deep Neural Networks (DNN)**, specifically **Convolutional Neural Networks (CNNs)**, to classify personality traits based on the **Five-Factor Model (Big Five)**:  
- **Openness (O)**  
- **Conscientiousness (C)**  
- **Extraversion (E)**  
- **Agreeableness (A)**  
- **Neuroticism (N)**  

By analyzing facial features, the model predicts binary traits for each factor, achieving an accuracy of **87.50%** during testing.  

## Features  
- **Automated Feature Learning**: Extracts relevant features from input images.  
- **Personality Trait Prediction**: Classifies personality traits based on a single grayscale portrait.  
- **Efficient Performance**: Processes images with minimal user input and computational overhead.  

## Objectives  
- To design an efficient personality prediction system using facial images.  
- To reduce the time required for traditional personality assessments.  
- To ensure privacy by predicting personality traits without sensitive personal data.  

## Technologies and Tools  
- **Programming Language**: Python  
- **Libraries**:  
  - TensorFlow: For building and training neural networks.  
  - Keras: For simplified neural network modeling.  
  - NumPy: For numerical operations and image preprocessing.  
  - Pillow: For basic image processing tasks.  
- **IDE and GUI Tools**:  
  - PyCharm: For development and debugging.  
  - Qt Designer: For designing the graphical user interface (GUI).  

## System Workflow  
1. **Preprocessing**:  
   - Images are read and normalized into a dataset (208x208 grayscale).  
   - The dataset is split into 80% training and 20% testing.  

2. **Model Training**:  
   - A CNN model is trained on 30,935 labeled portrait images.  
   - The model architecture includes Convolution2D and MaxPooling2D layers.  
   - The trained model is saved in JSON format, with weights stored in an `.h5` file.  

3. **Prediction and Testing**:  
   - The trained model predicts personality traits for input images.  
   - Outputs are evaluated for accuracy and reliability.  

## Installation  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/personality-prediction.git  
   cd personality-prediction  
   ```  
2. **Install Dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. **Prepare the Dataset**:
   - Extract the datasset in the main folder "Model".
   - Ensure images are formatted as 208x208 grayscale portraits.  

## Results  
- **Model Accuracy**: 87.50%  

## Limitations and Future Work  
- **Current Limitations**:  
  - Cannot predict intelligence, IQ, mood, or future behavior.  
  - Requires a single facial image with specific conditions (grayscale, 208x208).  

- **Future Enhancements**:  
  - Expand the dataset for improved performance.  
  - Adapt the system into a web or mobile application.  

## Contributing  
Contributions are welcome! Fork the repository, create a branch, and submit a pull request for review.  
