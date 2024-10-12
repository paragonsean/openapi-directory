

# ForecastProperties

The properties of the forecast charge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**charge** | **BigDecimal** | The amount of charge |  [optional] [readonly] |
|**chargeType** | [**ChargeTypeEnum**](#ChargeTypeEnum) | The type of the charge. Could be actual or forecast |  [optional] |
|**confidenceLevels** | [**List&lt;ForecastPropertiesConfidenceLevelsInner&gt;**](ForecastPropertiesConfidenceLevelsInner.md) | The details about the forecast confidence levels. This is populated only when chargeType is Forecast. |  [optional] [readonly] |
|**currency** | **String** | The ISO currency in which the meter is charged, for example, USD. |  [optional] [readonly] |
|**grain** | [**GrainEnum**](#GrainEnum) | The granularity of forecast. |  [optional] |
|**usageDate** | **String** | The usage date of the forecast. |  [optional] [readonly] |



## Enum: ChargeTypeEnum

| Name | Value |
|---- | -----|
| ACTUAL | &quot;Actual&quot; |
| FORECAST | &quot;Forecast&quot; |



## Enum: GrainEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |
| MONTHLY | &quot;Monthly&quot; |
| YEARLY | &quot;Yearly&quot; |



