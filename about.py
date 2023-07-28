import streamlit as st
from PIL import Image

image1 = Image.open('OvO.jpg')
image2 = Image.open('genimage.jpg')

def about_section():
    st.markdown('## Welcome')
    st.image(image1, use_column_width="auto", output_format="auto")
    st.markdown(r'''
    ### About This Application

    This application serves as a tool to stay updated and informed about the state of ransomware. Its purpose is to shed light on the rapidly evolving landscape of ransomware, which poses an increasing threat to individuals, businesses, and governments around the globe. 

    By providing a comprehensive overview of ransomware incidents, the application allows users to better understand the nature of these threats, which in turn could help in strategizing defenses against them. 

    The data presented here is collected and maintained by the [RansomWatch project](https://github.com/joshhighet/ransomwatch), a dedicated initiative that tracks and compiles information on various ransomware families and incidents. We would like to express our gratitude to them for their incredible work and for making this data publicly accessible. 

    The RansomWatch project is licensed under [Unlicense.org](http://unlicense.org/), which allows for the free use of its software, with or without modification, for any purpose. 

    Remember, knowledge is power, and staying informed is the first step in defending against ransomware threats.
    ''')

    st.image(image2, use_column_width="auto", output_format="auto")
    
    st.markdown(r'''
    ### [Overt Operator](https://www.overtoperator.com/):

    Overt Operator, an organization committed to providing a nuanced understanding of global affairs, has been a key inspiration for the development of this application. Their mission resonates with ours, as they strive to empower individuals by demystifying complex geopolitical dynamics.

    The ethos of Overt Operator is reflected in the way this application functions. By shedding light on the rapidly evolving landscape of ransomware, we aim to empower you, just as Overt Operator does through their insightful analysis of global affairs. 

    Whether it's the shadowy corridors of power in Washington or the intricacies of cybersecurity, the common thread is the democratization of knowledge. Overt Operator does this by bringing nuanced geopolitical narratives to your doorstep, and we strive to do the same for the realm of cybersecurity.

    So, as you navigate through this application, remember that it's not just about understanding the world of ransomware—it's also a testament to the power of open knowledge and the incredible work organizations like Overt Operator are doing to make the world a more informed place.
    ''')