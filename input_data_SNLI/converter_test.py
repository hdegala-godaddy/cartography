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

        ## 'annotator_labels', 'captionID', 'gold_label', 'pairID', 
        ## 'sentence1', 'sentence1_binary_parse', 'sentence1_parse', 
        ## 'sentence2', 'sentence2_binary_parse', 'sentence2_parse'
            # Extract fields and write to TSV
            tsv_writer.writerow([ json_data.get("captionID", ""),json_data.get("gold_label", "") ,json_data.get("sentence1", ""),json_data.get("sentence2", "")])

# Example usage:
jsonl_file_path = 'snli_1.0_test.jsonl'
tsv_file_path = 'test.tsv'

jsonl_to_tsv(jsonl_file_path, tsv_file_path)

