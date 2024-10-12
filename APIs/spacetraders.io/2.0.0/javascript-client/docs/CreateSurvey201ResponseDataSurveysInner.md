# SpaceTradersApi.CreateSurvey201ResponseDataSurveysInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposits** | [**[CreateSurvey201ResponseDataSurveysInnerDepositsInner]**](CreateSurvey201ResponseDataSurveysInnerDepositsInner.md) | A list of deposits that can be found at this location. | 
**expiration** | **Date** | The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction. | 
**signature** | **String** | A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey. | 
**size** | **String** | The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted. | 
**symbol** | **String** | The symbol of the waypoint that this survey is for. | 



## Enum: SizeEnum


* `SMALL` (value: `"SMALL"`)

* `MODERATE` (value: `"MODERATE"`)

* `LARGE` (value: `"LARGE"`)




