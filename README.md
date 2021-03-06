## The Big Cats Classifier

![Big Cats](./images/big_cats_classifier.jpg)

The term "big cat" is typically used to refer to any of the five living members of the genus Panthera, namely the tiger, lion, jaguar, leopard, and snow leopard, as well as the non-pantherine cheetah and cougar.

Upload an image of one of the Big Cat and determine which category the big cat belongs to. The model is trained using FastAI with backbone of Resnet18 architecture.
Image data is retrieved using the Bing Image Search API.

#### Side Note
*I have always had a problem in recognizing big cats, so I thought of building a classifier using FastAI as part of my learning from the FastAI book.*

### Categories the Classifier can predict :
1. Cheetah
1. Cougar
1. Jaguar
1. Leopard
1. Lion
1. Snow leopard
1. Tiger

### Results

The model gets an accuracy of 91% on the validation set, the model does get confused between the leopard and jaguar categories.

### Live Demo

The model is deployed using StreamLit Sharing.  You can try it out here :  
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dnaveenr/big_cat_classifier/main/src/streamlit_deploy.py)

### References 

1. FastAI [Book](https://course.fast.ai/).
2. Streamlit deployment is inspired from [here](https://github.com/jacKlinc/covid_mask_classifier).