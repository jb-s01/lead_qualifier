from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class LeadQualifier():
	"""LeadQualifier crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def web_search_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['web_search_agent'],
			verbose=True,
			tools=[SerperDevTool()]
		)

	@agent
	def linkedin_query_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['linkedin_query_agent'],
			verbose=True
		)

	@agent
	def crm_query_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['crm_query_agent'],
			verbose=True
		)
	
	@agent
	def data_synthesis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_synthesis_agent'],
			verbose=True
		)
	

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def fetch_web_data(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_web_data'],
		)

	@task
	def fetch_linkedin_data(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_linkedin_data'],
		)
	
	@task
	def fetch_crm_data(self) -> Task:
		return Task(
			config=self.tasks_config['fetch_crm_data'],
		)
	
	@task
	def synthesize_data(self) -> Task:
		return Task(
			config=self.tasks_config['synthesize_data'],
			output_file='report.md'
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the LeadQualifier crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
