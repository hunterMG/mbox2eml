import mailbox
import os
import argparse

def mbox_to_eml(mbox_file, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the mbox file
    mbox = mailbox.mbox(mbox_file)

    # Iterate through each message in the mbox file
    for i, message in enumerate(mbox):
        # Create a new eml file for each message
        eml_filename = f"{i + 1}.eml"
        eml_path = os.path.join(output_dir, eml_filename)

        # Write the eml content to the file
        with open(eml_path, 'w') as eml_file:
            eml_file.write(message.as_string())

        print(f"Message {i + 1} converted to {eml_filename}")

if __name__ == "__main__":
    # mbox_file = "path/to/your/input.mbox"
    # output_dir = "./output"
    
    # Read input and output path from CLI arguments.
    parser = argparse.ArgumentParser(description='Convert mbox to eml')
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the input mbox file, eg. 1.mbox')
    parser.add_argument('--output_dir', '-o', type=str, required=True, help='Path to the output directory, eg. output')

    args = parser.parse_args()

    mbox_to_eml(args.file, args.output_dir)
