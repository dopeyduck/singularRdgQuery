import re
import csv
from lxml import etree

# Define the namespace
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# Get the witnesses from the user
witnesses_input = input("Please enter witnesses: ")

# Split the input strings by commas, tabs, and spaces, strip any leading or trailing whitespace from each witness, and convert the list of witnesses to a set
witnesses = set(witness.strip() for witness in re.split('[, \t]+', witnesses_input))

# Get the path of the XML file from the user
xml_file_path = input("Please enter the path of the XML file: ")

# Open and parse the XML file
with open(xml_file_path, 'r') as file:
    tree = etree.parse(file)

# Initialize a counter
counter = 0

# Open the CSV file
with open('singularRdgs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')

    # Write the header row
    writer.writerow(['n', 'from', 'to', 'rdg_n', 'witness', 'type', 'text', 'A_text'])

    # Iterate over all 'app' elements
    for app in tree.xpath('//tei:app', namespaces=ns):
        rdgs = app.xpath('.//tei:rdg', namespaces=ns)

        # Initialize the 'A' text
        a_text = None

        # Check if any wit attribute contains 'A'
        for rdg in rdgs:
            if 'A' in rdg.get('wit', '').split():
                a_text = rdg.text
                break

        # Check if any wit attribute contains exactly one witness from the set and no other witnesses from the set
        for rdg in rdgs:
            wit = set(rdg.get('wit', '').split())
            intersection = wit & witnesses
            if len(intersection) == 1 and not (wit - intersection):
                # If so, write the 'n', 'from', 'to' attributes of the 'app', the 'n' attribute of the 'rdg', the name of the witness, the 'type' attribute, the text of the 'rdg', and the 'A' text to the CSV file
                writer.writerow([app.get('n'), app.get('from'), app.get('to'), rdg.get('n'), list(intersection)[0], rdg.get('type'), rdg.text, a_text])
                counter += 1
                break

# Print the total number of instances
print(f"Total instances: {counter}")