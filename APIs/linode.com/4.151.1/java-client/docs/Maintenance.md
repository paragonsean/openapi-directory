

# Maintenance

Information about maintenance affecting an entity. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**MaintenanceEntity**](MaintenanceEntity.md) |  |  [optional] |
|**reason** | **String** | The reason maintenance is being performed.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The maintenance status.  Maintenance progresses in the following sequence: pending, started, then completed.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of maintenance.  |  [optional] |
|**when** | **OffsetDateTime** | When the maintenance will begin.  [Filterable](/docs/api/#filtering-and-sorting) with the following parameters:  * A single value in date-time string format (\&quot;%Y-%m-%dT%H:%M:%S\&quot;), which returns only matches to that value.  * A dictionary containing pairs of inequality operator string keys (\&quot;+or\&quot;, \&quot;+gt\&quot;, \&quot;+gte\&quot;, \&quot;+lt\&quot;, \&quot;+lte\&quot;, or \&quot;+neq\&quot;) and single date-time string format values (\&quot;%Y-%m-%dT%H:%M:%S\&quot;). \&quot;+or\&quot; accepts an array of values that may consist of single date-time strings or dictionaries of inequality operator pairs.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| PENDING | &quot;pending&quot; |
| STARTED | &quot;started&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REBOOT | &quot;reboot&quot; |
| COLD_MIGRATION | &quot;cold_migration&quot; |
| LIVE_MIGRATION | &quot;live_migration&quot; |



