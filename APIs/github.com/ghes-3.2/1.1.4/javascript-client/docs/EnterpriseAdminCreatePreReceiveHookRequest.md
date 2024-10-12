# GitHubV3RestApi.EnterpriseAdminCreatePreReceiveHookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowDownstreamConfiguration** | **Boolean** | Whether enforcement can be overridden at the org or repo level. default: &#x60;false&#x60; | [optional] 
**enforcement** | **String** | The state of enforcement for this hook. default: &#x60;disabled&#x60; | [optional] 
**environment** | **{String: Object}** | The pre-receive environment where the script is executed. | 
**name** | **String** | The name of the hook. | 
**script** | **String** | The script that the hook runs. | 
**scriptRepository** | **{String: Object}** | The GitHub repository where the script is kept. | 


