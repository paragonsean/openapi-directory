# DialogflowApi.GoogleCloudDialogflowCxV3ExportAgentResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentContent** | **Blob** | Uncompressed raw byte content for agent. This field is populated if none of &#x60;agent_uri&#x60; and &#x60;git_destination&#x60; are specified in ExportAgentRequest. | [optional] 
**agentUri** | **String** | The URI to a file containing the exported agent. This field is populated if &#x60;agent_uri&#x60; is specified in ExportAgentRequest. | [optional] 
**commitSha** | **String** | Commit SHA of the git push. This field is populated if &#x60;git_destination&#x60; is specified in ExportAgentRequest. | [optional] 


