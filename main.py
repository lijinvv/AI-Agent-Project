"""
SYSTEM: R&D Intelligence Orchestrator
GOAL: Strategic analysis of Agentic AI integration in high-tech engineering.
ENGINE: Llama-3.3-70b-versatile

"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# 1. ENVIRONMENT CONFIGURATION
# Loading environment variables ensures security of API credentials
load_dotenv()

class EngineeringIntelligenceSystem:
    """
    A professional class to manage the orchestration of autonomous 
    AI agents for R&D strategic reporting.
    
    """
    
    def __init__(self):
        # Initialize the high-performance inference engine
        # temperature=0.1 ensures technical consistency and precision
        self.llm = ChatGroq(
            temperature=0.1,
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.environ.get("GROQ_API_KEY")
        )

    def get_agent(self):
        """Defines the Principal R&D Architect with domain-specific expertise."""
        return Agent(
            role='Principal R&D Systems Architect',
            goal='Synthesize the technical value proposition of Agentic AI for Tier-1 engineering consultancies.',
            backstory="""You are a veteran systems architect specializing in digital 
            transformation. Your expertise lies in reducing design-cycle latency 
            and optimizing R&D workflows for medical robotics and industrial IoT.""",
            allow_delegation=False,
            llm=self.llm,
            verbose=True
        )

    def get_task(self, architect_agent):
        """Defines the technical deliverables and strategic constraints."""
        return Task(
            description="""Analyze the shift from static automation to autonomous agentic 
            workflows in high-tech R&D. Focus on two core pillars: 
            1) Accelerated prototyping cycles.
            2) Technical debt reduction through autonomous optimization.""",
            agent=architect_agent,
            expected_output="A high-level 2-paragraph Strategic Impact Briefing."
        )

    def execute_workflow(self):
        """Orchestrates the agentic workflow and returns the final technical report."""
        # Instantiate agent and task
        agent = self.get_agent()
        task = self.get_task(agent)

        # Initialize the CrewAI orchestrator
        crew = Crew(
            agents=[agent],
            tasks=[task]
        )
        
        return crew.kickoff()

# 2. SYSTEM ENTRY POINT
if __name__ == "__main__":
    print("\n" + "="*50)
    print("INITIALIZING AUTONOMOUS R&D INTELLIGENCE SYSTEM")
    print("="*50 + "\n")
    
    # Initialize the system
    system = EngineeringIntelligenceSystem()
    
    # Run the technical analysis
    technical_report = system.execute_workflow()
    
    print("\n" + "="*50)
    print("SUCCESS: STRATEGIC R&D IMPACT REPORT GENERATED")
    print("="*50 + "\n")
    print(technical_report)
