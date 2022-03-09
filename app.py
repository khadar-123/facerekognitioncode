import boto3
import streamlit as stl
from PIL import Image
import os

def load_image(image_file):
    img=Image.open(image_file)
    return img

st.header("Face matching project using aws")
col1,col2=st.columns(2)

col1.subheader('Enter source Image')
src_image_file=col1.file_uploader("Upload Image",type=["png","jpg","jpeg"],key=1)

col2.subheader('Enter target Image')
target_image_file=col2.file_uploader("Upload Image",type=["png","jpg","jpeg"],key=2)

  if src_image_fil1 is not None:
      file_details={"filename":src_img_file,"filetype":src_img_file.type,"filesize":src_img_file.size}
      col1.write(file_details)
      col1.image(load_image(src_image_file),width=250)

      with open(os.path.join("uploads","src.jpg"),"wb") as f:
           f.write(src_image_file.getbuffer())
           col1.success('file saved')

  if src_image_fil1 is not None:
      file_details={"filename":target_img_file,"filetype":target_img_file.type,"filesize":target_img_file.size}
      col2.write(file_details)
      col2.image(load_image(target_image_file),width=250)

      with open(os.path.join("uploads","target.jpg"),"wb") as f:
           f.write(target_image_file.getbuffer())
           col2.success('file saved')
if st.button("Compare faces"):
    st.warning("Faces comparison called")
    imagesource=open("uploads/src.jpg","rb")
    imagetarget=open("uploads/target.jpg","rb")
    client=boto3.client('rekognition')
    responses=client.compare_faces(SimilaityThreshold=70,SourceImage={'Bytes':imagesource.read()},TargetImage={'Bytes':imagetarget.read()})
    try:
        print(response['FaceMatches'][0])
        st.success('Faces Matched')
    except:
        st.error('Faces are not Matched')