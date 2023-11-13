import xml.etree.ElementTree as ET

def check_step_existence(kjb_file_path, step_name):
    tree = ET.parse(kjb_file_path)
    root = tree.getroot()

    # Print the XML structure
    ET.dump(root)

    # Find the steps section and check for the desired step
    steps_section = root.find(".//steps")
    if steps_section is not None:
        for step in steps_section.findall("step"):
            name = step.get("name")
            if name == step_name:
                return True
    return False

# Usage:
kjb_file_path = "C:\\Users\\hogsettm\\OneDrive - Reed Elsevier Group ICO Reed Elsevier Inc\\Desktop\\pythonProject\\MIKD_CivilCommon\\MIKD-MainJob.kjb"
step_name = "Delete unzipped folder if exists"

exists = check_step_existence(kjb_file_path, step_name)
print(exists)
