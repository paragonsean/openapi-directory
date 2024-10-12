

# MaxSizeCapability

The maximum size capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Integer** | The maximum size limit (see &#39;unit&#39; for the units). |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | The units that the limit is expressed in. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MEGABYTES | &quot;Megabytes&quot; |
| GIGABYTES | &quot;Gigabytes&quot; |
| TERABYTES | &quot;Terabytes&quot; |
| PETABYTES | &quot;Petabytes&quot; |



