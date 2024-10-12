# AutomationManagement.DscConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | Gets or sets the creation time. | [optional] 
**description** | **String** | Gets or sets the description. | [optional] 
**jobCount** | **Number** | Gets or sets the job count of the configuration. | [optional] 
**lastModifiedTime** | **Date** | Gets or sets the last modified time. | [optional] 
**logVerbose** | **Boolean** | Gets or sets verbose log option. | [optional] 
**nodeConfigurationCount** | **Number** | Gets the number of compiled node configurations. | [optional] 
**parameters** | [**{String: DscConfigurationParameter}**](DscConfigurationParameter.md) | Gets or sets the configuration parameters. | [optional] 
**provisioningState** | **String** | Gets or sets the provisioning state of the configuration. | [optional] 
**source** | [**ContentSource**](ContentSource.md) |  | [optional] 
**state** | **String** | Gets or sets the state of the configuration. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)





## Enum: StateEnum


* `New` (value: `"New"`)

* `Edit` (value: `"Edit"`)

* `Published` (value: `"Published"`)




