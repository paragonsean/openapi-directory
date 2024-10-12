# ConsumptionManagementClient.ForecastProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge** | **Number** | The amount of charge | [optional] [readonly] 
**chargeType** | **String** | The type of the charge. Could be actual or forecast | [optional] 
**confidenceLevels** | [**[ForecastPropertiesConfidenceLevelsInner]**](ForecastPropertiesConfidenceLevelsInner.md) | The details about the forecast confidence levels. This is populated only when chargeType is Forecast. | [optional] [readonly] 
**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. | [optional] [readonly] 
**grain** | **String** | The granularity of forecast. | [optional] 
**usageDate** | **String** | The usage date of the forecast. | [optional] [readonly] 



## Enum: ChargeTypeEnum


* `Actual` (value: `"Actual"`)

* `Forecast` (value: `"Forecast"`)





## Enum: GrainEnum


* `Daily` (value: `"Daily"`)

* `Monthly` (value: `"Monthly"`)

* `Yearly` (value: `"Yearly"`)




