

# RetentionDuration

Retention duration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Count of the duration types. Retention duration is determined by the combining the Count times and durationType.      For example, if Count &#x3D; 3 and durationType &#x3D; Weeks, then the retention duration is three weeks. |  [optional] |
|**durationType** | [**DurationTypeEnum**](#DurationTypeEnum) | The retention duration type of the retention policy. |  [optional] |



## Enum: DurationTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DAYS | &quot;Days&quot; |
| WEEKS | &quot;Weeks&quot; |
| MONTHS | &quot;Months&quot; |
| YEARS | &quot;Years&quot; |



