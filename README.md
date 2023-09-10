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

2. Install the required packages:
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
- `--slides`: (Optional) Number of slides in the presentation. Default is 10.
- `--output`: (Optional) Name of the output PowerPoint file. Default is presentation.pptx.