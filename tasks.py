from crewai import Task

class WebsiteScrapingTask():
    def testcaseweriter(self, agent):
        return Task(
            description="Create detailed manual test cases for all the elements identified using the SeleniumScrapingTool.",
            agent=agent,
            expected_output="Detailed manual test cases for the identified elements.",
        )
    
    def sdettestengineer(self, agent):
        return Task(
            description="Create clear and concise BDD-style Gherkin feature files and translate them into corresponding Java step definitions using CSS selectors or XPath.",
            agent=agent,
            expected_output="Clear and concise BDD-style Gherkin feature files and corresponding Java step definitions.",
        )
    
    def qareviewer(self, agent):
        return Task(
            description="Integrate the BDD-style feature files and step definitions and ensure their alignment with BDD principles.",
            agent=agent,
            expected_output="Feedback on the quality of the manual test cases,feature file, and step definitions.",
        )
    
    # def qaapprover(self, agent):
    #     return Task(
    #         description="Approve the test cases and the test reports.",
    #         agent=agent,
    #         expected_output="Approved test cases and test reports.",
    #     )
    
    # def developer(self, agent):
    #     return Task(
    #         description="Develop the test cases and the test reports.",
    #         agent=agent,
    #         expected_output="Developed test cases and test reports.",
    #     )
    
    # def testexecuter(self, agent):
    #     return Task(
    #         description="Execute the test cases and the test reports.",
    #         agent=agent,
    #         expected_output="Executed test cases and test reports.",
    #     )
    
    # def testreportwriter(self, agent):
    #     return Task(
    #         description="Write the test reports.",
    #         agent=agent,
    #         expected_output="Written test reports.",
    #     )
    
    