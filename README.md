# PowerPoint Generator with ChatGPT
This script allows you to generate PowerPoint presentations using ChatGPT. It takes a topic as input and creates a presentation with the specified number of slides.

# Features
- Automatically generate slides based on a given topic.
- Save the generated content as a JSON file.
- Load content from a previously saved JSON file.
- Supports various slide layouts including "Title Slide", "Title and Content", "Two Content", "Comparison", and "Content with Caption".

# Prerequisites
- Python 3.x
- Required Python packages: python-pptx, dotenv, langchain
- A .env file with necessary environment variables for langchain.

# Installation

1. Clone this repository:

    ```bash    
    git clone https://github.com/jeremyjouvancedev/chatgpt-to-powerpoint.git
    cd chatgpt-to-powerpoint
    ```

2. Create a .env file
    ```bash
    touch .env
    ```
    Add `OPENAI_API_KEY` with your key to the `.env` file

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
# Usage

To generate a PowerPoint presentation:

```bash
python <script_name>.py "Your Topic Here" --slides 5 --output output_filename.pptx
```

Arguments:
- `topic`: The topic for which you want to generate the presentation.
- `--openaiApiKey`: (Optional) OpenAi Api Key.
- `--slides`: (Optional) Number of slides in the presentation. Default is 10.
- `--output`: (Optional) Name of the output PowerPoint file. Default is presentation.pptx.
- `--modelType`: (Optional) Model type to use for generating the presentation. Default is ChatOpenAI.
- `--model`: (Optional) Model to use for generating the presentation. Default is gpt-3.5-turbo.
- `--json`: (Optional) Reload json slides representation.


# Next Improvements

- Get data from Web instead of chatgpt base knowledge
- Insert royalty free images for Caption Slides
- Automatique Image Generation for Caption Slides
- Can Have mutliple Agent Prompt profiles (AKA persona)
- Can specify a Design template
- Add the ability to insert Hyperlinks / videos
- Multilingual Support
- Analytics on slides (Estamed time, engagement)
- Fine Tuned model for presentation generation
