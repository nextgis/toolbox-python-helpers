# Simplest tool run using Toolbox SDK
# Tool: https://toolbox.nextgis.com/t/hello
# More SDK examples: https://gitlab.com/nextgis/toolbox/toolbox_sdk/-/blob/master/README.md?ref_type=heads

from toolbox_sdk import ToolboxClient

##############SET THESE#######################
token = 'YOUR API TOKEN'
tool_name = 'hello'
name = 'John' #5 symbols max here
##############################################

toolbox = ToolboxClient(token=token)
tool = toolbox.tool(tool_name)

# Run and wait for the result
result = tool({
    "name": name
})

print(result.outputs[0]['value'])