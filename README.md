# Autonomous R&D Strategic Intelligence Orchestrator
## 📌 Project Overview
This project is an **Agentic AI System** designed to simulate a **Principal R&D Systems Architect**. It evaluates the strategic impact of moving from static automation to autonomous agentic workflows within high-tech engineering firms. 

The goal is to demonstrate how AI agents can accelerate product development lifecycles, reduce technical debt, and optimize innovation velocity in complex fields like medical robotics and industrial IoT.

## 🛠️ Technical Stack
* **Orchestration:** [CrewAI](https://www.crewai.com/) (Multi-agent framework)
* **LLM:** Llama 3.3 70B Versatile
* **Inference Engine:** [Groq Cloud](https://groq.com/) (LPU-powered for ultra-low latency)
* **Language:** Python 3.12+
* **Security:** Environment-based secret management (`python-dotenv`)



## 🚀 Key Features
* **Agentic Reasoning:** Unlike standard chatbots, this system uses a "Role-Goal-Backstory" framework to ensure technical domain expertise.
* **High-Speed Inference:** Leverages Groq's LPU architecture to produce complex technical reports in seconds.
* **Production-Ready Code:** Built using Object-Oriented Programming (OOP) principles for scalability and modularity.

## 📁 Repository Structure
* `main.py`: The core orchestration logic and agent definitions.
* `requirements.txt`: Project dependencies for reproducible environments.
* `.env.example`: A template for required environment variables.
* `.gitignore`: Ensures sensitive API credentials remain local and secure.

## 🔧 Installation & Usage
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/lijinvv/AI-Agent-Project.git](https://github.com/lijinvv/AI-Agent-Project.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup Environment:**
    Create a `.env` file and add your `GROQ_API_KEY`.
4.  **Run the System:**
    ```bash
    python main.py
    ```