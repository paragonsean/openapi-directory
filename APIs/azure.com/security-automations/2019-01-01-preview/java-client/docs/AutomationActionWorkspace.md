

# AutomationActionWorkspace

The Log Analytics Workspace to which event data will be exported. Security alerts data will reside in the 'SecurityAlert' table and the assessments data will reside in the 'SecurityRecommendation' table (under the 'Security'/'SecurityCenterFree' solutions). Note that in order to view the data in the workspace, the Security Center Log Analytics free/standard solution needs to be enabled on that workspace. To learn more about Security Center continuous export capabilities, visit https://aka.ms/ASCExportLearnMore

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workspaceResourceId** | **String** | The fully qualified Log Analytics Workspace Azure Resource ID. |  [optional] |



