

# LocationCapabilities

The location capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The location name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedManagedInstanceVersions** | [**List&lt;ManagedInstanceVersionCapability&gt;**](ManagedInstanceVersionCapability.md) | The list of supported managed instance versions. |  [optional] [readonly] |
|**supportedServerVersions** | [**List&lt;ServerVersionCapability&gt;**](ServerVersionCapability.md) | The list of supported server versions. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



