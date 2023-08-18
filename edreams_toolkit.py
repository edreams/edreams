from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List
from edreams_tool import InstagramSendTool

class EdreamsToolkit(BaseToolkit):
    name = "Edreams Toolkit"
    description = "Toolkit for interacting with Instagram"

    def get_tools(self) -> List[BaseTool]:
        return [InstagramSendTool()]

