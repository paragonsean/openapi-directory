

# EditionCapability

The edition capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The database edition name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedServiceLevelObjectives** | [**List&lt;ServiceObjectiveCapability&gt;**](ServiceObjectiveCapability.md) | The list of supported service objectives for the edition. |  [optional] [readonly] |
|**zoneRedundant** | **Boolean** | Whether or not zone redundancy is supported for the edition. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



