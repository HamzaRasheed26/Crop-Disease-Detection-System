import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("model_VGG16.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(224,224))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Detection", "Diseases Info"])

#Main Page
if(app_mode=="Home"):
    st.header("CROP DISEASE DETECTION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
    Welcome to the Crop Disease Detection System! 🌿🔍
    
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Detection** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Detection** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
                #### VGG-16 Model
                To resolve the detection diseases of in plants. CNN deep-learning models are popular for image processing. However, deep CNN layers are difficult to train as this process is computationally expensive. 
                To solve such issues, transfer learning based models have been proposed by various researchers. Popular transfer learning models include VGG-16, ResNet, DenseNet, and Inception. 
                Among these models, we choose **VGG-16**. Making it suitable for plant disease detection tasks. 
                By using the capabilities of VGG-16 we can develop an efficient system for plant disease detection.

                #### About Dataset
                The dataset utilized for this project is taken from Kaggle repository: https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset. 
                This dataset consists of about **87K rgb images** of healthy and diseased crop leaves which is categorized into **38 different classes**. 
                The total dataset is divided into **80/20 ratio of training and validation** set preserving the directory structure. 
                A new directory containing **33 test images** is created later for prediction purpose.

                #### Content
                1. train (70295 images)
                2. validation (17572  images)
                3. test (33 images)

                #### About the Developer
                Hi, I'm Hamza Rasheed, a 3rd year Computer Science student at UET Lahore. I developed this Crop Disease Detection System under the supervision of Sir Samyan Qayyum Wahla and Chairman Usman Ghani. 
                You can contact me via [GitHub](https://github.com/HamzaRasheed26) or [LinkedIn](https://www.linkedin.com/in/hamza-rasheed-9666b3237/).
                If you have any questions, feedback, or suggestions, feel free to reach out to me at hamzarasheed19961@gmail.com.
                """)

#Prediction Page
elif(app_mode=="Disease Detection"):
    st.header("Disease Detection")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))

elif app_mode == "Diseases Info":
    st.header("Diseases Info")

    # Define a dictionary containing information about each disease
    diseases_info = {
        "Apple Diseases": ["Apple Scab", "Black Rot", "Cedar Apple Rust", "Healthy"],
        "Blueberry Diseases": ["Healthy"],
        "Cherry Diseases": ["Powdery Mildew", "Healthy"],
        "Corn Diseases": ["Cercospora Leaf Spot", "Common Rust", "Northern Leaf Blight", "Healthy"],
        "Grape Diseases": ["Black Rot", "Esca (Black Measles)", "Leaf Blight (Isariopsis Leaf Spot)", "Healthy"],
        "Orange Diseases": ["Haunglongbing (Citrus greening)"],
        "Peach Diseases": ["Bacterial Spot", "Healthy"],
        "Pepper Bell Diseases": ["Bacterial Spot", "Healthy"],
        "Potato Diseases": ["Early Blight", "Late Blight", "Healthy"],
        "Raspberry Diseases": ["Healthy"],
        "Soybean Diseases": ["Healthy"],
        "Squash Diseases": ["Powdery Mildew"],
        "Strawberry Diseases": ["Leaf Scorch", "Healthy"],
        "Tomato Diseases": ["Bacterial Spot", "Early Blight", "Late Blight", "Leaf Mold", 
                            "Septoria Leaf Spot", "Spider Mites", "Target Spot", 
                            "Yellow Leaf Curl Virus", "Tomato Mosaic Virus", "Healthy"]
    }

    # Display disease information using interactive widgets
    selected_disease = st.selectbox("Select a Disease", list(diseases_info.keys()))

    if selected_disease:
        st.subheader(selected_disease)
        # Display symptoms of the selected disease
        if selected_disease in diseases_info:
            for symptom in diseases_info[selected_disease]:
                st.write(f"- {symptom}")