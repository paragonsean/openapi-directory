# AmazonNimbleStudio.UpdateStudioComponentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**CreateStudioComponentRequestConfiguration**](CreateStudioComponentRequestConfiguration.md) |  | [optional] 
**description** | **String** | The description. | [optional] 
**ec2SecurityGroupIds** | **[String]** | The EC2 security groups that control access to the studio component. | [optional] 
**initializationScripts** | [**[StudioComponentInitializationScript]**](StudioComponentInitializationScript.md) | Initialization scripts for studio components. | [optional] 
**name** | **String** | The name for the studio component. | [optional] 
**runtimeRoleArn** | **String** | An IAM role attached to a Studio Component that gives the studio component access to Amazon Web Services resources at anytime while the instance is running.  | [optional] 
**scriptParameters** | [**[ScriptParameterKeyValue]**](ScriptParameterKeyValue.md) | Parameters for the studio component scripts. | [optional] 
**secureInitializationRoleArn** | **String** | An IAM role attached to Studio Component when the system initialization script runs which give the studio component access to Amazon Web Services resources when the system initialization script runs. | [optional] 
**subtype** | **String** | The specific subtype of a studio component. | [optional] 
**type** | **String** | The type of the studio component. | [optional] 



## Enum: SubtypeEnum


* `AWS_MANAGED_MICROSOFT_AD` (value: `"AWS_MANAGED_MICROSOFT_AD"`)

* `AMAZON_FSX_FOR_WINDOWS` (value: `"AMAZON_FSX_FOR_WINDOWS"`)

* `AMAZON_FSX_FOR_LUSTRE` (value: `"AMAZON_FSX_FOR_LUSTRE"`)

* `CUSTOM` (value: `"CUSTOM"`)





## Enum: TypeEnum


* `ACTIVE_DIRECTORY` (value: `"ACTIVE_DIRECTORY"`)

* `SHARED_FILE_SYSTEM` (value: `"SHARED_FILE_SYSTEM"`)

* `COMPUTE_FARM` (value: `"COMPUTE_FARM"`)

* `LICENSE_SERVICE` (value: `"LICENSE_SERVICE"`)

* `CUSTOM` (value: `"CUSTOM"`)




