import json
from typing import Any, Type

def generate_sample_data_from_json_ld_with_type(json_ld: Any, type_: Type) -> Any:
  """Generates sample data from JSON-LD based on the defined type.

  Args:
    json_ld: A JSON-LD object.
    type_: The type of the sample data.

  Returns:
    A sample data object of the defined type.
  """

  if isinstance(type_, dict):
    sample_data = {}
    for key, value in type_.items():
      if key in json_ld:
        sample_data[key] = generate_sample_data_from_json_ld_with_type(json_ld[key], value)
      elif type_[key]["@type"] == "xsd:string":
        sample_data[key] = ""
  elif isinstance(type_, list):
    sample_data = []
    for element_type in type_:
      sample_data.append(generate_sample_data_from_json_ld_with_type(json_ld, element_type))
  else:
    sample_data = json_ld

  return sample_data

def main():
  # Load the JSON-LD from the sample URI.
  with open("https://raw.githubusercontent.com/magnetar-io/strange_matter/main/Component_Definition/Header/component_definition.json") as f:
    json_ld = json.load(f)

  # Generate sample data of the type `ComponentDefinition`.
  component_definition = generate_sample_data_from_json_ld_with_type(json_ld, ComponentDefinition)

  print(component_definition)

if __name__ == "__main__":
  main()
