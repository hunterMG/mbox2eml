import sys
from email import policy
from email.parser import BytesParser
from email.generator import BytesGenerator

def read_and_modify_eml(input_eml, output_eml):
    # Parse the input EML file
    with open(input_eml, 'rb') as eml_data:
        msg = BytesParser(policy=policy.default).parse(eml_data)

    # Modify the "From" section (replace with "user@example.com")
    msg.replace_header('To', 'user@example.com')

    # Write the modified content to the new EML file
    with open(output_eml, 'wb') as new_eml:
        generator = BytesGenerator(new_eml)
        generator.flatten(msg)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python3 modify_eml.py <input_eml_path> <output_eml_path>")
        sys.exit(1)

    input_eml_file = sys.argv[1]
    output_eml_file = sys.argv[2]

    read_and_modify_eml(input_eml_file, output_eml_file)
    print(f"Modified content written to {output_eml_file}")