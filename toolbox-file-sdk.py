# Simple run with sending a file over using Toolbox SDK
# Tool: https://toolbox.nextgis.com/t/kmldae2footprints
# More SDK examples: https://gitlab.com/nextgis/toolbox/toolbox_sdk/-/blob/master/README.md?ref_type=heads

from toolbox_sdk import ToolboxClient

##############SET THESE#######################
token = "YOUR API TOKEN"
tool_name = "kmldae2footprints"
input_data = "sampledata.zip"
##############################################

toolbox = ToolboxClient(token=token)
tool = toolbox.tool(tool_name)

# Run and wait for the result
result = tool({
    "zip_with_kmls": toolbox.upload_file(input_data)
})

# Download all results into the current directory
toolbox.download_results(result, ".")
