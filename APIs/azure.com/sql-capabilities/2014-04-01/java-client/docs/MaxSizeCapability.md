

# MaxSizeCapability

The maximum size limits for a database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limit** | **Long** | The maximum size of the database (see &#39;unit&#39; for the units). |  [optional] [readonly] |
|**status** | **CapabilityStatus** |  |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The units that the limit is expressed in. |  [optional] [readonly] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| MEGABYTES | &quot;Megabytes&quot; |
| GIGABYTES | &quot;Gigabytes&quot; |
| TERABYTES | &quot;Terabytes&quot; |
| PETABYTES | &quot;Petabytes&quot; |



