import openai


api_key = "I have removed my API key"


project_title = "Project Title"
project_description = "Project Description"
project_requirements = "Project Requirements"
your_experience = "Your Experience Relevant to the Project"
budget = "Your Proposed Budget"
proposal_deadline = "Proposal Submission Deadline"


def generate_project_proposal():
    prompt = f"Write a project proposal for the project titled '{project_title}'.\n\nProject Description: {project_description}\n\nProject Requirements: {project_requirements}\n\nYour Experience: {your_experience}\n\nBudget: {budget}\n\nProposal Deadline: {proposal_deadline}\n\nProposal:"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )

    proposal = response.choices[0].text.strip()
    return proposal


if __name__ == "__main__":
    openai.api_key = api_key
    proposal = generate_project_proposal()

    print(f"Project Proposal for '{project_title}':")
    print(proposal)
