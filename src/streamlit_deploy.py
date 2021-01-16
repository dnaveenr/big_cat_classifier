from fastai.learner import load_learner
from fastai.vision.core import PILImage

import streamlit as st
from PIL import Image

def load_image(image):
    '''
    Pass    BytesIO image
    Return  PILImage object
    '''
    return Image.open(image)

def predict_img(img):
    '''
    Pass    PILImage object
    Return  prediction[str], prediction_idx[int], probability[tensor]
    '''
    if img is not None:
        return learner_inf.predict(pil_img)

'## Big Cats Classifier'
"Here's the [GitHub](https://github.com/dnaveenr/big_cat_classifier) repo"
'Upload a picture of a Big Cat and determine which category it belongs to.'

learner_inf = load_learner("./big_cat_classifier.pkl")

# Upload
pic = st.file_uploader("Upload Image File")

'Click Classify'

probs = []
pred_idx = 1
pred = 'n/a'

# Display image
if pic is not None:
    img = load_image(pic)
    st.image(img, use_column_width=True)

    # Parse image
    pil_img = PILImage.create(pic)

    # Predict category
    pred, pred_idx, probs = predict_img(pil_img)

# Classify
if st.button('Classify'):
    'Predicted as ', pred
    'Probability of ', str(round(probs[pred_idx].item(), 3))

"Note : Probability greater than 90% indicates a confident guess whereas a lower probability indicates the model is not very sure of the guess. :)"