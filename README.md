# LeadQualifier Crew

Welcome to the LeadQualifier Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/lead_qualifier/config/agents.yaml` to define your agents
- Modify `src/lead_qualifier/config/tasks.yaml` to define your tasks
- Modify `src/lead_qualifier/crew.py` to add your own logic, tools and specific args
- Modify `src/lead_qualifier/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the lead_qualifier Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The lead_qualifier Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the LeadQualifier Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## Project Specifics

# CrewAI Lead Qualification Workflow

## Overview
The **Lead Qualification Workflow** automates the process of gathering and synthesizing data about a prospective lead. This CrewAI-powered system leverages multiple agents to pull data from web searches, LinkedIn profiles, and internal CRM systems, then synthesizes this information into a professional one-page summary.

This workflow is particularly useful for sales teams, account managers, and business development professionals looking to engage with leads efficiently and effectively.

---

## Agents

### 1. **Web Search Agent**
- **Role:** Web Data Specialist
- **Description:**
   Retrieves publicly available data about a lead using the **Serper Dev Tool**.
- **Responsibilities:**
   - Execute targeted web searches.
   - Summarize relevant articles, company information, and mentions.
- **Tools:** Serper Dev Tool
- **Outputs:** JSON data containing lead-related web information.

### 2. **LinkedIn Query Agent**
- **Role:** LinkedIn Profile Specialist
- **Description:**
   Fetches professional profile information for a lead using the **LinkedIn API**.
- **Responsibilities:**
   - Identify career history, education, and professional networks.
   - Return structured LinkedIn data.
- **Tools:** LinkedIn API
- **Outputs:** JSON data with LinkedIn profile details.

### 3. **CRM Query Agent**
- **Role:** Internal CRM Specialist
- **Description:**
   Queries the organization's internal CRM to retrieve historical lead interactions and data.
- **Responsibilities:**
   - Provide lead history, sales notes, and pipeline status.
- **Tools:** Internal CRM API
- **Outputs:** JSON data with CRM-specific lead information.

### 4. **Data Synthesis Agent**
- **Role:** Lead Data Synthesizer
- **Description:**
   Combines data from multiple sources to generate a tailored, professional summary for the lead.
- **Responsibilities:**
   - Synthesize all gathered data into actionable insights.
   - Create a formatted one-pager with bio, conversation starters, potential services, and next steps.
- **Tools:** OpenAI GPT-4o
- **Outputs:** Formatted text summary (one-pager).

---

## Tasks

### 1. **Fetch Web Data**
- **Agent:** Web Search Agent
- **Description:** Executes a web search using Bing Search API to gather lead-related public information.
- **Inputs:** Lead Name
- **Outputs:** `web_data` (JSON)

### 2. **Fetch LinkedIn Data**
- **Agent:** LinkedIn Query Agent
- **Description:** Retrieves professional profile details for the lead from LinkedIn.
- **Inputs:** Lead Name
- **Outputs:** `linkedin_data` (JSON)

### 3. **Fetch CRM Data**
- **Agent:** CRM Query Agent
- **Description:** Pulls existing lead data from the internal CRM system.
- **Inputs:** Lead Name
- **Outputs:** `crm_data` (JSON)

### 4. **Synthesize Data**
- **Agent:** Data Synthesis Agent
- **Description:** Combines web, LinkedIn, and CRM data into a one-pager summary.
- **Inputs:**
   - Lead Name
   - Interested Services
   - `web_data` (from Fetch Web Data)
   - `linkedin_data` (from Fetch LinkedIn Data)
   - `crm_data` (from Fetch CRM Data)
- **Outputs:** `lead_summary` (Formatted text)

---

## Workflow Diagram

1. **Fetch Web Data** → JSON (web_data)
2. **Fetch LinkedIn Data** → JSON (linkedin_data)
3. **Fetch CRM Data** → JSON (crm_data)
4. **Synthesize Data** → Formatted One-Pager (lead_summary)

---

## How to Run the Workflow
1. Configure API Keys for Serper Dev Tool, LinkedIn, and OpenAI in your environment.
2. Deploy the CrewAI agents and tasks as defined.
3. Run the workflow with the desired **Lead Name** and optional **Interested Services**.
4. The system will output a one-page summary containing:
   - Bio
   - Conversation Starters
   - Potential Services
   - Next Steps

---

## Output Example
```
## Lead Summary

**Bio**
John Doe is a Senior Vice President at Acme Corp with over 15 years of experience in technology leadership. His focus includes cloud infrastructure and enterprise digital transformation.

**Conversation Starters**
- "I noticed Acme Corp recently expanded its cloud offerings. How is your team adapting to this growth?"
- "Given your strong leadership background, what trends do you see emerging in digital transformation?"

**Potential Services**
- Cloud Migration Strategy
- AI-Driven Business Analytics
- Enterprise Data Governance Framework

**Next Steps**
- Schedule an introductory call to align on business priorities.
- Share relevant case studies highlighting similar transformations.
```

---

## Use Cases
- Sales Lead Preparation
- Account Research for Relationship Managers
- Business Development Insights

---

## Dependencies
- **APIs:** Serper Dev Tool, LinkedIn, Internal CRM
- **LLM Model:** OpenAI GPT-4o
- **Framework:** CrewAI

---

## License
This project is licensed under the MIT License.

---



