from crewai import Agent, Task, Process, Crew
import streamlit as st
from crewai import Agent, Task, Crew, Process
# from langchain.agents import load_tools
# from langchain.agents import Tool
# from langchain.tools import tool
import os
from crewai_tools import SeleniumScrapingTool
from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
from agentops.agent import track_agent
import agentops
from dotenv import load_dotenv
load_dotenv()

# agentops.init()
agentops.init(api_key='492a0623-9037-4c03-bb76-800bd791c234', tags=['BBD generator'])

st.title("Website Scraping and Testing Automation")

website_url = st.text_input("Enter Website URL:")

llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )
tool1 = SeleniumScrapingTool(website_url=website_url)
tool2 = SeleniumScrapingTool(website_url=website_url, css_element='.main-content')

os.environ["SERPER_API_KEY"] = "586dd44d3544a918ea21aa60b2a99741bed6f97d"
search_tool = SerperDevTool()

def callback_function(output):
    # Display output in Streamlit UI
    st.write(f"""
        Task completed!
        Task: {output.description}
        Output: {output.result}
    """)

@track_agent(name="create_test_case_writer")
def create_test_case_writer():
    return Agent(
        role="Manual Test Case Writer",
        goal="Create detailed manual test cases for all the elements identified using the SeleniumScrapingTool.",
        backstory="As a skilled Test Case Writer, You are responsible for creating detailed manual test cases that cover all the elements identified on a website using the SeleniumScrapingTool.",
        verbose=True,
        allow_delegation=True,
        tools=[tool1],
        llm=llm
    )

@track_agent(name="create_sdet_test_engineer")
def create_sdet_test_engineer():
    return Agent(
        role="SDET Test Engineer",
        goal="Create clear and concise BDD-style Gherkin feature files and translate them into corresponding Java step definitions using CSS selectors or XPath.",
        backstory="As a certified SDET with a background in writing feature files and step definitions, excel in translating requirements and specifications into user-centric scenarios using CSS selectors or XPath for element identification.",
        verbose=True,
        allow_delegation=True,
        llm=llm,
        tools=[tool2]
    )

@track_agent(name="create_reviewer")
def create_reviewer():
    return Agent(
        role="Quality Assurance Reviewer",
        goal="Ensure the overall quality and alignment of the output provided by Test_Case_Writer and SDET Test Engineer with BDD principles of the final artifacts.",
        backstory="As an experienced Quality Assurance Reviewer with a keen eye for detail and understanding of BDD principles, review the final outputs for clarity, consistency, and effectiveness.",
        verbose=True,
        allow_delegation=True,
        llm=llm,
        callback=callback_function,
        tools=[search_tool]
    )

def create_task1():
    agent = create_test_case_writer()
    return Task(
        description="Create detailed manual test cases by covering all possible scenarios for the elements identified using the SeleniumScrapingTool.",
        agent=agent,
        expected_output="Detailed manual test cases for the identified elements.",
    )

def create_task2():
    agent = create_sdet_test_engineer()
    return Task(
        description="Generate all possible BDD-style feature file scenarios, and step definitions in java, capturing all potential user behaviors and edge cases.",
        agent=agent,
        expected_output="All the BDD-style feature files, and step definitions.",
    )

def create_task3():
    agent = create_reviewer()
    return Task(
        description="Integrate the BDD-style feature files and step definitions and ensure their alignment with BDD principles.",
        agent=agent,
        expected_output="The final artifacts, ensuring the overall quality and alignment with BDD principles.",
    )

def create_crew():
    task1 = create_task1()
    task2 = create_task2()
    task3 = create_task3()
    agent1 = create_test_case_writer()
    agent2 = create_sdet_test_engineer()
    agent3 = create_reviewer()
    return Crew(
        agents=[agent1, agent2, agent3],
        tasks=[task1, task2, task3],
        verbose=2,
        process=Process.sequential,
        memory=False,
        max_rpm=2
    )

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

# Add Streamlit button to start the process
if st.button("Start Process"):
    crew = create_crew()  
    result = crew.kickoff()
    st.write("Process completed!")
    st.write(result)



# automated_test_executor = Agent(
#     role="Automated Test Executor",
#     goal="Execute automated test scripts to validate the functionality of the software application.",
#     backstory="As an expert in automated testing, your role is to execute automated test scripts to ensure the functionality and reliability of the software application.",
#     verbose=True,
#     allow_delegation=True,
#     llm=llm,
#     tools=[tool3]
# )

# report_generator = Agent(
#     role="Report Generator",
#     goal="Generate comprehensive test reports summarizing the test results and findings.",
#     backstory="As a skilled Report Generator, your responsibility is to create comprehensive test reports summarizing the test results and findings for further analysis and decision-making.",
#     verbose=True,
#     allow_delegation=True,
#     llm=llm,
#     tools=[tool4]
# )



# task4 = Task(
#     description="Execute automated test scripts to validate the functionality of the software application.",
#     agent=automated_test_executor,
#     expected_output="Test execution completed."
# )

# task5 = Task(
#     description="Generate comprehensive test reports summarizing the test results and findings.",
#     agent=report_generator,
#     context=[task3],
#     expected_output="Comprehensive test reports generated."
# )