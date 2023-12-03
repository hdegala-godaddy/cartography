import json
import csv

def jsonl_to_tsv(jsonl_file, tsv_file):
    with open(jsonl_file, 'r') as json_file, open(tsv_file, 'w', newline='') as tsv_file:
        # Create a CSV writer with tab delimiter
        tsv_writer = csv.writer(tsv_file, delimiter='\t')

        # Write header if needed
        # tsv_writer.writerow(["field1", "field2", ...])

        # Iterate over JSONL lines
        for line in json_file:
            # Load JSON from each line
            json_data = json.loads(line)

            # Extract fields and write to TSV
            tsv_writer.writerow([json_data.get("premise", ""), json_data.get("hypothesis", ""),json_data.get("label", "")])

# Example usage:
jsonl_file_path = 'train_2.jsonl'
tsv_file_path = 'train.tsv'

jsonl_to_tsv(jsonl_file_path, tsv_file_path)

