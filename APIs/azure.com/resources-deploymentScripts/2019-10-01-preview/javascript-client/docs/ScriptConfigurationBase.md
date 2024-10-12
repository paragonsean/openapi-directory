# DeploymentScriptsClient.ScriptConfigurationBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | **String** | Command line arguments to pass to the script. Arguments are separated by spaces. ex: -Name blue* -Location &#39;West US 2&#39;  | [optional] 
**environmentVariables** | [**[EnvironmentVariable]**](EnvironmentVariable.md) | The environment variables to pass over to the script. | [optional] 
**forceUpdateTag** | **String** | Gets or sets how the deployment script should be forced to execute even if the script resource has not changed. Can be current time stamp or a GUID. | [optional] 
**primaryScriptUri** | **String** | Uri for the script. This is the entry point for the external script. | [optional] 
**retentionInterval** | **String** | Interval for which the service retains the script resource after it reaches a terminal state. Resource will be deleted when this duration expires. Duration is based on ISO 8601 pattern (for example P7D means one week). | 
**scriptContent** | **String** | Script body. | [optional] 
**supportingScriptUris** | **[String]** | Supporting files for the external script. | [optional] 
**timeout** | **String** | Maximum allowed script execution time specified in ISO 8601 format. Default value is PT1H | [optional] 


