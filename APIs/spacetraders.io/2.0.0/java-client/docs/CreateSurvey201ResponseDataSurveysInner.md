

# CreateSurvey201ResponseDataSurveysInner

A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deposits** | [**List&lt;CreateSurvey201ResponseDataSurveysInnerDepositsInner&gt;**](CreateSurvey201ResponseDataSurveysInnerDepositsInner.md) | A list of deposits that can be found at this location. |  |
|**expiration** | **OffsetDateTime** | The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction. |  |
|**signature** | **String** | A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey. |  |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted. |  |
|**symbol** | **String** | The symbol of the waypoint that this survey is for. |  |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| SMALL | &quot;SMALL&quot; |
| MODERATE | &quot;MODERATE&quot; |
| LARGE | &quot;LARGE&quot; |



