

# ManagedInstanceVersionCapability

The managed instance capability

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The server version name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedEditions** | [**List&lt;ManagedInstanceEditionCapability&gt;**](ManagedInstanceEditionCapability.md) | The list of supported managed instance editions. |  [optional] [readonly] |
|**supportedInstancePoolEditions** | [**List&lt;InstancePoolEditionCapability&gt;**](InstancePoolEditionCapability.md) | The list of supported instance pool editions. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



