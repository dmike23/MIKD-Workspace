import xml.etree.ElementTree as ET


def check_step_existence(kjb_file_path, attribute_name, attribute_value):
    tree = ET.parse(kjb_file_path)
    root = tree.getroot()

    for step in root.iter("step"):
        if attribute_name in step.attrib and step.attrib[attribute_name] == attribute_value:
            return True

    return False


# Usage example
kjb_file_path = "MIKD_CivilCommon/MIKD-MainJob.kjb"
attribute_name = "type"
attribute_value = "EXECUTE_PROCESS"

exists = check_step_existence(kjb_file_path, attribute_name, attribute_value)
print(exists)
