# LinodeApi.Maintenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**MaintenanceEntity**](MaintenanceEntity.md) |  | [optional] 
**reason** | **String** | The reason maintenance is being performed.  | [optional] 
**status** | **String** | The maintenance status.  Maintenance progresses in the following sequence: pending, started, then completed.  | [optional] 
**type** | **String** | The type of maintenance.  | [optional] 
**when** | **Date** | When the maintenance will begin.  [Filterable](/docs/api/#filtering-and-sorting) with the following parameters:  * A single value in date-time string format (\&quot;%Y-%m-%dT%H:%M:%S\&quot;), which returns only matches to that value.  * A dictionary containing pairs of inequality operator string keys (\&quot;+or\&quot;, \&quot;+gt\&quot;, \&quot;+gte\&quot;, \&quot;+lt\&quot;, \&quot;+lte\&quot;, or \&quot;+neq\&quot;) and single date-time string format values (\&quot;%Y-%m-%dT%H:%M:%S\&quot;). \&quot;+or\&quot; accepts an array of values that may consist of single date-time strings or dictionaries of inequality operator pairs.  | [optional] 



## Enum: StatusEnum


* `completed` (value: `"completed"`)

* `pending` (value: `"pending"`)

* `started` (value: `"started"`)





## Enum: TypeEnum


* `reboot` (value: `"reboot"`)

* `cold_migration` (value: `"cold_migration"`)

* `live_migration` (value: `"live_migration"`)




