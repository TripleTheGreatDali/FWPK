import os

# Base folder name
base_folder = "0_Python_Learning_Journey"

# Syllabus stages with subfolders for topics (numbered)
stages = {
    "0_Foundations": [
        "0_Introduction_to_Programming",
        "1_Setup_Python_IDE",
        "2_Running_Scripts",
        "3_Basic_Syntax",
        "4_Data_Types",
        "5_Input_Output",
        "6_Arithmetic_Operations",
        "7_Type_Casting"
    ],
    "1_Core_Python": [
        "0_Strings",
        "1_Lists",
        "2_Tuples",
        "3_Sets",
        "4_Dictionaries",
        "5_Conditionals",
        "6_Loops",
        "7_Functions",
        "8_Modules_and_Imports"
    ],
    "2_Intermediate_Python": [
        "0_List_Comprehensions",
        "1_Dict_Set_Comprehensions",
        "2_Lambda_Functions",
        "3_Map_Filter_Reduce",
        "4_Exception_Handling",
        "5_File_Handling",
        "6_Regular_Expressions",
        "7_Built_in_Modules"
    ],
    "3_Object_Oriented_Python": [
        "0_Classes_and_Objects",
        "1_Instance_Variables_Methods",
        "2_Class_Variables_Methods",
        "3_Inheritance_Polymorphism",
        "4_Encapsulation_Private_Attributes",
        "5_Special_Methods"
    ],
    "4_Advanced_Python": [
        "0_Iterators_Generators",
        "1_Decorators",
        "2_Context_Managers",
        "3_Advanced_File_Handling",
        "4_Logging",
        "5_Functional_Programming",
        "6_Memory_Management"
    ],
    "5_Data_Handling_Libraries": [
        "0_Numpy",
        "1_Pandas",
        "2_Matplotlib_Seaborn",
        "3_APIs_Requests_JSON",
        "4_Web_Scraping"
    ],
    "6_Testing_Packaging_Deployment": [
        "0_Unit_Testing",
        "1_Debugging",
        "2_Virtual_Environments",
        "3_Packaging_Projects",
        "4_Scripts",
        "5_Git_Version_Control"
    ],
    "7_Advanced_Projects_Specialization": [
        "0_Object_Serialization",
        "1_MultiThreading_Multiprocessing",
        "2_Async_Programming",
        "3_Database_Connectivity",
        "4_Mini_Projects",
        "5_Specializations_DataScience",
        "6_Specializations_WebDev",
        "7_Specializations_Automation",
        "8_Specializations_GameDev"
    ],
    "8_Expert_Level": [
        "0_Design_Patterns",
        "1_Performance_Optimization",
        "2_Memory_Profiling",
        "3_Advanced_OOP_Metaclasses",
        "4_Custom_Decorators_ContextManagers",
        "5_Open_Source_Contribution",
        "6_Large_Scale_Projects",
        "7_Code_Quality_PEP8"
    ]
}

# Create folders
for stage, topics in stages.items():
    stage_path = os.path.join(base_folder, stage)
    os.makedirs(stage_path, exist_ok=True)
    for topic in topics:
        topic_path = os.path.join(stage_path, topic)
        os.makedirs(topic_path, exist_ok=True)

print(f"Python learning journey folders created under '{base_folder}'")
