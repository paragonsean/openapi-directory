# ThePlaidApi.ProductStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdown** | [**ProductStatusBreakdown**](ProductStatusBreakdown.md) |  | 
**lastStatusChange** | **Date** | [ISO 8601](https://wikipedia.org/wiki/ISO_8601) formatted timestamp of the last status change for the institution.  | 
**status** | **String** | This field is deprecated in favor of the &#x60;breakdown&#x60; object, which provides more granular institution health data.  &#x60;HEALTHY&#x60;: the majority of requests are successful &#x60;DEGRADED&#x60;: only some requests are successful &#x60;DOWN&#x60;: all requests are failing | 



## Enum: StatusEnum


* `HEALTHY` (value: `"HEALTHY"`)

* `DEGRADED` (value: `"DEGRADED"`)

* `DOWN` (value: `"DOWN"`)




