

# KpiProperties

Each KPI must contain a 'type' and 'enabled' key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | show the KPI in the UI? |  [optional] |
|**id** | **String** | ID of resource related to metric (budget). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | KPI type (Forecast, Budget). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FORECAST | &quot;Forecast&quot; |
| BUDGET | &quot;Budget&quot; |



