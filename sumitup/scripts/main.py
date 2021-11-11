import argparse

import sumitup.nlp.model as model
import sumitup.source.bbc as bbc
import sumitup.source.cnn as cnn
from sumitup.exporter.notion import NotionExporter
from sumitup.exporter.tts import TtsExporter


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("source", action="store")
    parser.add_argument("exporter", action="store")

    source_map = {
        "cnn_business": cnn.CnnBusinessSource(),
        "cnn_entertainment": cnn.CnnEntertainmentSource(),
        "cnn_politics": cnn.CnnPoliticsSource(),
        "bbc": bbc.BbcNewsSource(),
    }

    args = parser.parse_args()

    # Define exporter
    if args.exporter == "notion":
        exporter = NotionExporter(audio_version=False)
    elif args.exporter == "tts":
        exporter = TtsExporter()
    else:
        raise Exception

    # Define NLP model
    model_ = model.FrequencySummarizer()

    # Define the data source
    source = source_map[args.source]
    page_urls = source.get_page_urls()
    page_gen = source.parse_pages(page_urls)

    # Run the model
    summed_up = [model_.run(article=page) for page in page_gen]

    # Export
    exporter.export_list(items=summed_up)


if __name__ == "__main__":
    raise SystemExit(main())
