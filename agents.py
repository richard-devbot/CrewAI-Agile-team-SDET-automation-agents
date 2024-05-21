import os
from crewai import Agent
from langchain_groq import ChatGroq
import streamlit as st
from crewai_tools import SeleniumScrapingTool
from langchain.agents import load_tools
from crewai_tools import SerperDevTool

st.title("Website Scraping and Testing Automation")

website_url = st.text_input("Enter Website URL:")

tool1 = SeleniumScrapingTool(website_url=website_url)
tool2 = SeleniumScrapingTool(website_url=website_url, css_element='.main-content')
#human_tools = load_tools(["human"])
os.environ["SERPER_API_KEY"] = "586dd44d3544a918ea21aa60b2a99741bed6f97d"
search_tool = SerperDevTool()

class AutomationAgents():
    def __init__(self):
        self.llm = ChatGroq(
            #api_key=os.getenv("GROQ_API_KEY"),
            api_key="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",
            model="mixtral-8x7b-32768"
        )

    def Test_Case_Writer(self):
        return Agent(
            role="Manual Test Case Writer",
            goal="Create detailed manual test cases for all the elements identified using the SeleniumScrapingTool.",
            backstory="""As a skilled Test Case Writer, You are responsible for creating detailed manual test cases 
                        that cover all the elements identified on a website using the SeleniumScrapingTool.""",
            verbose=True,
            allow_delegation=True,
            #tools=[SeleniumScrapingTool()],
            llm=self.llm,
            tools = [tool1]
        )
    
    def SDET_Test_Engineer(self):
        return Agent(
            role="SDET Test Engineer",
            goal="""Create clear and concise BDD-style Gherkin feature files and translate them into 
                    corresponding Java step definitions using CSS selectors or XPath.""",
            backstory="""As a certified SDET with a background in writing feature files and step definitions, 
                    excel in translating requirements and specifications into user-centric scenarios using CSS selectors 
                    or XPath for element identification.""",
            verbose=True,
            allow_delegation=True,
            # delegatees=["Manual Test Case Writer"],
            #tools=[JiraIntegration()], # TODO: Add actual integration here
            llm=self.llm,
            tools = [tool2]
        )
    
    def Quality_Assurance_Reviewer(self):
        return Agent(
           role="Quality Assurance Reviewer",
            goal="""Ensure the overall quality and alignment of the output provided by Test_Case_Writer and 
                    SDET Test Engineer with BDD principles of the final artifacts.""",
            backstory="""As an experienced Quality Assurance Reviewer with a keen eye for detail and understanding 
                    of BDD principles, review the final outputs for clarity, consistency, and effectiveness.""",
            verbose=True,
            allow_delegation=True,
            delegatees=["SDET Test Engineer"],
            #tools=[JiraIntegration()]
            tools = [search_tool]
        )
    
    # def Developer(self):
    #     return Agent(
    #         role="Developer",
    #         goal="Develop the software application.",
    #         backstory="""As a Developer, you are responsible for developing the software application.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Quality Assurance Reviewer"],
    #         tools=[JiraIntegration()]
    #     )
    # def QA_Engineer(self):
    #     return Agent(
    #         role="QA Engineer",
    #         goal="Perform quality assurance on the software application.",
    #         backstory="""As a QA Engineer, you are responsible for performing quality assurance on the software application.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Quality Assurance Reviewer"],
    #         tools=[JiraIntegration()]
    #     )
    # def DevOps_Engineer(self):
    #     return Agent(
    #         role="DevOps Engineer",
    #         goal="Perform DevOps on the software application.",
    #         backstory="""As a DevOps Engineer, you are responsible for performing DevOps on the software application.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["QA Engineer", "Developer"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def Automation_Team(self):
    #     return Agent(
    #         role="Automation Team",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Team, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["DevOps Engineer"],
    #         tools=[JiraIntegration()]
    #     )
    # def Automation_Lead(self):
    #     return Agent(
    #         role="Automation Lead",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Lead, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Team"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def Automation_Manager(self):
    #     return Agent(
    #         role="Automation Manager",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Manager, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Lead"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def Automation_Architect(self):
    #     return Agent(
    #         role="Automation Architect",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Architect, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Manager"],
    #         tools=[JiraIntegration()]
    #     )
    # def Automation_Tester(self):
    #     return Agent(
    #         role="Automation Tester",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Tester, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Architect"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def Automation_Developer(self):
    #     return Agent(
    #         role="Automation Developer",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation Developer, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Tester"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def Automation_SDET(self):
    #     return Agent(
    #         role="Automation SDET",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an Automation SDET, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation Developer"],
    #         tools=[JiraIntegration()]
    #     )
    # def SDET_Test_Engineer(self):
    #     return Agent(
    #         role="SDET Test Engineer",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an SDET Test Engineer, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["Automation SDET"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def SDET_QA_Engineer(self):
    #     return Agent(
    #         role="SDET QA Engineer",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an SDET QA Engineer, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["SDET Test Engineer"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def SDET_DevOps_Engineer(self):
    #     return Agent(
    #         role="SDET DevOps Engineer",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an SDET DevOps Engineer, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["SDET QA Engineer"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def SDET_Automation_Team(self):
    #     return Agent(
    #         role="SDET Automation Team",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an SDET Automation Team, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["SDET DevOps Engineer"],
    #         tools=[JiraIntegration()]
    #     )
    
    # def SDET_Automation_Lead(self):
    #     return Agent(
    #         role="SDET Automation Lead",
    #         goal="Perform all the automation tasks.",
    #         backstory="""As an SDET Automation Lead, you are responsible for performing all the automation tasks.""",
    #         verbose=True,
    #         allow_delegation=True,
    #         delegatees=["SDET Automation Team"],
    #         tools=[JiraIntegration()]
    #     )
    


  
