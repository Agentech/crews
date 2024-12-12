from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DocumentTypeClassificationForInsuranceOcrDataCrew():
    """DocumentTypeClassificationForInsuranceOcrData crew"""

    @agent
    def document_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['document_analyzer']
        )

    @agent
    def insurance_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['insurance_classifier']
        )

    @agent
    def confidence_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['confidence_evaluator']
        )


    @task
    def analyze_document_features(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_document_features'],
            tools=[],
        )

    @task
    def classify_document_type(self) -> Task:
        return Task(
            config=self.tasks_config['classify_document_type'],
            tools=[],
        )

    @task
    def calculate_confidence_score(self) -> Task:
        return Task(
            config=self.tasks_config['calculate_confidence_score'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the DocumentTypeClassificationForInsuranceOcrData crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
