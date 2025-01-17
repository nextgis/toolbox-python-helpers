# Simplest Toolbox SDK run for https://toolbox.nextgis.com/t/hello

from toolbox_sdk import ToolboxClient

##############SET THESE#######################
token = '425e6a88-8e83-49ec-b178-4d9ca6d518ff'
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