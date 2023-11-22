import streamlit as st

st.sidebar.image('https://clipartcraft.com/images/deloitte-logo-transparent-4.png', use_column_width=True)
st.header("Details on the process")
st.markdown("""<hr style="height:2px;border:none;color:#9ACD66;background-color:#9ACD66;" /> """, unsafe_allow_html=True)

file = "./assets/BaseReport.docx"

file2 = "./assets/EnhancedReport.docx"

col1, col2, col3 = st.columns([5,5,5])

with col1:
    with open(file,'rb') as file:
        btn = st.download_button(
            label = 'Download Base Report',
            data = file,
            file_name = 'BaseReport.docx'
        )

with col3:
    with open(file2,'rb') as file2:
        btn2 = st.download_button(
            label = 'Download Enhanced Report',
            data = file2,
            file_name = 'EnhancedReport.docx'
        )

with st.expander("See AI breakdown preview"):

    st.subheader("Question 1")
    st.write("""
    1. What are the latest advancements in the field of software engineering, specifically in the development and enhancement of virtual reality tools and applications 

The main pillars of modern software development are cloud computing, microservices, blockchain, IoT, AI, augmented reality, the LCNC approach, and 5G connectivity. Among the leading programming tools are Python, TensorFlow, and React Native. Advancements in VR hardware include brain-computer interfaces (BCIs) and AI-driven facial recognition and natural language processing. 

Thought Process:  

Sub-Question: What are the current trends in software engineering? 
 
Intermediate thought: The main pillars of modern software development are cloud computing, microservices, blockchain, IoT, AI, augmented reality, the LCNC approach, and 5G connectivity. Among the leading programming tools are Python, TensorFlow, and React Native. 

Sub-Question: What are the latest advancements in virtual reality technology? 
 
Intermediate thought: Advancements in Hardware One promising advancement in VR hardware is the development of brain-computer interfaces (BCIs). BCIs allow users to control VR experiences with their thoughts. In turn, this eliminates the need for controllers or other input devices. BCIs may still be in the early stages of development. 
        """)
    st.subheader("Question 2")
    st.write("""2. What are the current capabilities of the Unreal Gaming Engine and 3DS Max in terms of creating detailed models of construction sites and architectural specifications 

3Ds Max can be used to create detailed models of construction sites and architectural specifications, and can be used to create realistic visualizations of construction sites and architectural specifications. 

Thought Process:  

Sub-Question: What is the Unreal Gaming Engine? 
 
Intermediate thought: Unreal Engine, also known as UE, is a video game development tool from the video game and software development company Epic Games. With this tool, developers have the ability to build a simulation, edit videos or sound, and render animations. 

Sub-Question: What are the capabilities of the Unreal Gaming Engine? 
 
Intermediate thought: Features  * Pipeline integration. FBX, USD, and Alembic support. ...  * World building. The Unreal Editor. ...  * Characters and animation. Animation Blueprints. ...  * Rendering, lighting, and materials. Nanite & Virtual Shadow Maps. ...  * Simulation and effects. ...  * Gameplay and interactivity authoring. ...  * Integrated media support. ...  * Virtual production. 

Sub-Question: What is 3DS Max? 
 
Intermediate thought: Autodesk 3ds Max: Computer program. Autodesk 3ds Max, formerly 3D Studio and 3D Studio Max, is a professional 3D computer graphics program for making 3D animations, models, games and images. It is developed and produced by Autodesk Media and Entertainment. Autodesk 3ds Max Initial release date: April 1996. Autodesk 3ds Max Developer: Autodesk and Autodesk Media and Entertainment. Autodesk 3ds Max Programming languages: Python, C, and C++. Autodesk 3ds Max Frames per second: 30 frames per second. Autodesk 3ds Max Available in: English, German, French, Brazilian Portuguese, Japanese, Chinese, Korean. Autodesk 3ds Max License: Software as a service, Trialware. Autodesk 3ds Max Stable release: 2024.1 / May 17, 2023; 4 months ago. Autodesk 3ds Max® professional 3D modeling, rendering, and animation software enables you to create expansive worlds and premium designs. Breathe life into ... Autodesk 3ds Max, formerly 3D Studio and 3D Studio Max, is a professional 3D computer graphics program for making 3D animations, models, games and images. 3ds Max is a professional 3D modeling and rendering program for design visualization, games, and animation. But before it became Autodesk's 3ds ... 3ds Max is one most known software for 3d work, today we ... Duration: 10:34. Posted: Jan 9, 2020. Formerly known as a 3D studio and 3D studio Max, 3ds Max is a 3D professional modeling, animation, and rendering application build for ... The highly popular and professional 3D graphics software for 3D animation, models, games, and images, Autodesk 3ds Max is used by television commercial ... 

Sub-Question: What are the current capabilities of 3DS Max in terms of creating detailed models of construction sites and architectural specifications? 
 
Intermediate thought: Best Planning: Using 3Ds Max, architects and builders can create 3D models of buildings to better plan and coordinate construction activities. Using the software, precise plans for HVAC, plumbing, and other building systems can be made. """)

    st.subheader("Question 3")
    st.write("""3. What are the challenges in dealing with dense geometries and polygons in the context of software engineering and virtual reality 

Arbitrarily increasing the geometry density to resolve shape inaccuracies (without addressing the fundamental topology issues) tends to cause problems with rendering and editing. 

Thought Process:  

Sub-Question: What is the main challenge in dealing with dense geometries and polygons? 
 
Intermediate thought: Arbitrarily increasing the geometry density to resolve shape inaccuracies (without addressing the fundamental topology issues) tends to ... It's especially true if the polygons in that area have been stretched/enlarged by previous brush action. Btw, smoothing the blocky area, even at the lowest ... Blender 2.8 Viewport Performance heavy geometries, it becomes difficult to edit vertices (I am not referring only to subdiivided surfaces) yet ... Idea so far: Compute all the distances between each object in the polygon. Compute the standard deviation between the distances. The basic idea is to read through all the feature geometry and then write out some new features where all the vertices have a shift in their ... The goal of The Art and. Craft of Problem Solving is to develop strong problem solving skills, which it achieves by encouraging students to do math rather ... Basic area formulas are reviewed for parallelograms and ... Duration: 24:57. Posted: Jan 18, 2018. The problem is handling the corner joins, miters, caps etc. The resulting polygon needs to be "perfect" in the sense of no overdraw, clean ... In this post, we'll show you how you can quickly and easily decrease the complexity and density of geometry in TouchDesigner! We will attemp to run a processing algorithm on the input layer to demonstrate how invalid geometries can cause problems during geoprocessing ... """)

with st.expander('See code example'):
    st.code("""llm = OpenAI(temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
        Tool(
            name="Intermediate Answer",
            func=search.results,
            description="useful for when you need to ask with search"
        )
]

self_ask_with_search_result = initialize_agent(tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True, return_intermediate_steps = True)""",language='python')