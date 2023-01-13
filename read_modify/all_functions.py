import subprocess




# Create a constructor:
class DocumentModifier:

  def __init__(self, filename):
    self.filename = filename

  def change_content(self, my_dict):
    # Open the file in read mode
    with open(self.filename, 'r') as file:
      # Read the contents of the file
      content = file.read()

    # Modify the content of the file
    for old_text in my_dict.keys():
      # Replace the old text with the new text if it is present in the "text" variable
      if isinstance(my_dict[old_text],int):
        my_dict[old_text]=str(my_dict[old_text])
      elif isinstance(my_dict[old_text],str):
        my_dict[old_text] = my_dict[old_text]

      content = content.replace(old_text, my_dict[old_text])

    # Open the file in write mode
    with open(self.filename, 'w') as file:
      # Write the modified content to the file
      file.write(content)


#other funbctions:

# Single latex
# Single Dict
def single_latex_single_dict(file, Dict):
  modifier = DocumentModifier(file)  # read file
  modifier.change_content(Dict)  # modify content
  # run the external Latex file in Python:
  # the -interaction=batchmode option to run the compiler in batch mode,
  # which will suppress most prompts and error messages and make the output more predictable:
  return subprocess.run(["pdflatex", "-interaction=batchmode", file])


# Multi Latex: we have a list of latex files and we want to make a nest dictionary with keys are the latex file names
# Multi Dict: That are the values of dictionary and we
def multi_latex_nest_dict(multi_file, nest_dict):
  for k in multi_file:
    modifier = DocumentModifier(k)  # read file
    modifier.change_content(nest_dict[k])  # modify content
    # run the external Latex file in Python:
    # the -interaction=batchmode option to run the compiler in batch mode,
    # which will suppress most prompts and error messages and make the output more predictable:
    return subprocess.run(["pdflatex", "-interaction=batchmode", k])


# Single Latex
# Multi Dict
def single_latex_nest_dict(single_latex, nest_dict):
  modifier = DocumentModifier(single_latex)  # read file
  for k in nest_dict.keys():
    modifier.change_content(nest_dict[k])  # modify content
    # run the external Latex file in Python:
    # the -interaction=batchmode option to run the compiler in batch mode,
    # which will suppress most prompts and error messages and make the output more predictable:
    return subprocess.run(["pdflatex", "-interaction=batchmode", single_latex])


