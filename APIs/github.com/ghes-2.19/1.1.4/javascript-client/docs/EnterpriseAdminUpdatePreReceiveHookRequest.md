# GitHubV3RestApi.EnterpriseAdminUpdatePreReceiveHookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowDownstreamConfiguration** | **Boolean** | Whether enforcement can be overridden at the org or repo level. | [optional] 
**enforcement** | **String** | The state of enforcement for this hook. | [optional] 
**environment** | **{String: Object}** | The pre-receive environment where the script is executed. | [optional] 
**name** | **String** | The name of the hook. | [optional] 
**script** | **String** | The script that the hook runs. | [optional] 
**scriptRepository** | **{String: Object}** | The GitHub repository where the script is kept. | [optional] 


