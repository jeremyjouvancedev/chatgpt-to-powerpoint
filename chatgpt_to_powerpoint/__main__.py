import json
import argparse

# Env variable
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from chatgpt_to_powerpoint.powerpointGenerator import PowerPointGenerator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate PowerPoint presentation using ChatGPT."
    )
    parser.add_argument(
        "topic", type=str, help="Topic for the PowerPoint presentation."
    )
    parser.add_argument(
        "--modelType",
        type=str,
        default="ChatOpenAI",
        help="Model type to use for generating the presentation. Default is ChatOpenAI.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-3.5-turbo",
        help="Model to use for generating the presentation. Default is gpt-3.5-turbo.",
    )
    parser.add_argument(
        "--slides",
        type=int,
        default=10,
        help="Number of slides in the presentation. Default is 10.",
    )
    parser.add_argument(
        "--outputFolder",
        type=str,
        default=".",
        help="Output Folder. Default is '.'.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="presentation.pptx",
        help="Output PowerPoint file name. Default is presentation.pptx.",
    )
    
    parser.add_argument(
        "--json",
        type=str,
        default=None,
        help="Reload from a json file.",
    )

    parser.add_argument(
        "--openaiApiKey",
        type=str,
        default=None,
        help="OpenAi Api key.",
    )

    args = parser.parse_args()

    generator = PowerPointGenerator(args.modelType, args.model)
    generator.generate_slides(args.slides, args.topic, args.outputFolder, args.output, load_json=args.json)
