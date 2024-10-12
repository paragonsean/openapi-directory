

# ScoreDetail

Represents score detail of a background check

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**result** | [**ResultEnum**](#ResultEnum) | Overall result of the data collected. If at least one collected data status is found, the result will be found, otherwise, it will be the most frecuent status |  |
|**score** | **Float** | Dataset score. Number between 0 and 1 where 1 is the best score. |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none |  |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| FOUND | &quot;found&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| ERROR | &quot;error&quot; |
| DELAYED | &quot;delayed&quot; |
| IGNORED | &quot;ignored&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| NONE | &quot;none&quot; |
| VERY_LOW | &quot;very_low&quot; |
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| HIGH | &quot;high&quot; |
| VERY_HIGH | &quot;very_high&quot; |



