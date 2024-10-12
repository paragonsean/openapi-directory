

# UpdateStudioComponentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_configuration** | [**CreateStudioComponentRequestConfiguration**](CreateStudioComponentRequestConfiguration.md) |  |  [optional] |
|**description** | **String** | The description. |  [optional] |
|**ec2SecurityGroupIds** | **List&lt;String&gt;** | The EC2 security groups that control access to the studio component. |  [optional] |
|**initializationScripts** | [**List&lt;StudioComponentInitializationScript&gt;**](StudioComponentInitializationScript.md) | Initialization scripts for studio components. |  [optional] |
|**name** | **String** | The name for the studio component. |  [optional] |
|**runtimeRoleArn** | **String** | An IAM role attached to a Studio Component that gives the studio component access to Amazon Web Services resources at anytime while the instance is running.  |  [optional] |
|**scriptParameters** | [**List&lt;ScriptParameterKeyValue&gt;**](ScriptParameterKeyValue.md) | Parameters for the studio component scripts. |  [optional] |
|**secureInitializationRoleArn** | **String** | An IAM role attached to Studio Component when the system initialization script runs which give the studio component access to Amazon Web Services resources when the system initialization script runs. |  [optional] |
|**subtype** | [**SubtypeEnum**](#SubtypeEnum) | The specific subtype of a studio component. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the studio component. |  [optional] |



## Enum: SubtypeEnum

| Name | Value |
|---- | -----|
| AWS_MANAGED_MICROSOFT_AD | &quot;AWS_MANAGED_MICROSOFT_AD&quot; |
| AMAZON_FSX_FOR_WINDOWS | &quot;AMAZON_FSX_FOR_WINDOWS&quot; |
| AMAZON_FSX_FOR_LUSTRE | &quot;AMAZON_FSX_FOR_LUSTRE&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACTIVE_DIRECTORY | &quot;ACTIVE_DIRECTORY&quot; |
| SHARED_FILE_SYSTEM | &quot;SHARED_FILE_SYSTEM&quot; |
| COMPUTE_FARM | &quot;COMPUTE_FARM&quot; |
| LICENSE_SERVICE | &quot;LICENSE_SERVICE&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



