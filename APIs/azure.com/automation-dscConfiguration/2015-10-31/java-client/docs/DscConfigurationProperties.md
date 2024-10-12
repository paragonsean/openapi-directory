

# DscConfigurationProperties

Definition of the configuration property type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time. |  [optional] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**jobCount** | **Integer** | Gets or sets the job count of the configuration. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time. |  [optional] |
|**logVerbose** | **Boolean** | Gets or sets verbose log option. |  [optional] |
|**nodeConfigurationCount** | **Integer** | Gets the number of compiled node configurations. |  [optional] |
|**parameters** | [**Map&lt;String, DscConfigurationParameter&gt;**](DscConfigurationParameter.md) | Gets or sets the configuration parameters. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the provisioning state of the configuration. |  [optional] |
|**source** | [**ContentSource**](ContentSource.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the state of the configuration. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| EDIT | &quot;Edit&quot; |
| PUBLISHED | &quot;Published&quot; |



