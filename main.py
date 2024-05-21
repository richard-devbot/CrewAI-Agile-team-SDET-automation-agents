import time
from crewai import Crew
from agents import AutomationAgents
from tasks import WebsiteScrapingTask
import streamlit as st
from crewai import Process
from dotenv import load_dotenv
load_dotenv()

agents = AutomationAgents()

manualwritter = agents.Test_Case_Writer()
SDETwritter = agents.SDET_Test_Engineer()
Reviewer = agents.Quality_Assurance_Reviewer()

tasks = WebsiteScrapingTask()

testcaseweriter_task = []
sdettestengineer_tasks = []
qareviewer_tasks = []

testcaseweriter_task = tasks.testcaseweriter(
            agent=manualwritter,
        )

sdettestengineer_tasks = tasks.sdettestengineer(
            agent=manualwritter,
        )

qareviewer_tasks = tasks.qareviewer(
            agent=manualwritter,
        )

# Add the task to the crew
testcaseweriter_task.append(testcaseweriter_task)
sdettestengineer_tasks.append(sdettestengineer_tasks)
qareviewer_tasks.append(qareviewer_tasks)

st.subheader(":green[Still Hiring Automation Test Enginner's...!!!, I was using AI to write test cases, Feature Files, Step Defintions files for my team to automate the testing process in selenium and Cucumber.]")
st.sidebar.title(":green[## Designed By Richardson Gunde 🎨]")
st.sidebar.markdown("""
    🚀 Excited to share a breakthrough in Automated Testing with AI! 💻������Introducing our AI-powered Testing Assistant - your go-to solution for automating the testing process in Selenium and Cucumber. 🌟

With this innovative system, we're streamlining the process of drafting user stories, writing manual test cases, creating feature files, and implementing step definitions.

Try it out now and experience the future of automated testing! 💡💼

---

🔗 Simply input the requirements, and watch as our AI-powered system creates thorough and detailed:
- Manual test cases
- Feature files
- Step definitions

---

🤝 **Contributions Welcome**

If you want this tool, please let us know. We are open-source developers!

---

🔗 Linkedin : [Richardson Gunde](Linkedin URL)
📧 Gmail : [gunderichardson@gmail.com](mailto:gunderichardson@gmail.com)
    """)

# Setup Crew
crew = Crew(
    agents=[
        manualwritter,
        SDETwritter,
        Reviewer
    ],
    tasks=[
        *testcaseweriter_task,
        *sdettestengineer_tasks,
        *qareviewer_tasks
    ],
    max_rpm=29,
    verbose=2,
    process=Process.sequential
)

start_time = time.time()

if st.button("Start Process"):
    result = crew.kickoff()
    st.write("Process completed!")
    st.write(result)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Crew kickoff took {elapsed_time} seconds.")
print("Crew usage", crew.usage_metrics)