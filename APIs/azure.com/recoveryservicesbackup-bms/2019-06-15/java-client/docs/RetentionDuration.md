

# RetentionDuration

Retention duration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Count of duration types. Retention duration is obtained by the counting the duration type Count times.  For example, when Count &#x3D; 3 and DurationType &#x3D; Weeks, retention duration will be three weeks. |  [optional] |
|**durationType** | [**DurationTypeEnum**](#DurationTypeEnum) | Retention duration type of retention policy. |  [optional] |



## Enum: DurationTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DAYS | &quot;Days&quot; |
| WEEKS | &quot;Weeks&quot; |
| MONTHS | &quot;Months&quot; |
| YEARS | &quot;Years&quot; |



