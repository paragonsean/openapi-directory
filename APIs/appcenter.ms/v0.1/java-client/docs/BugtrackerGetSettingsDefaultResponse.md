

# BugtrackerGetSettingsDefaultResponse

Alerting service error

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requestId** | **String** | Unique request identifier for tracking |  |
|**code** | [**CodeEnum**](#CodeEnum) | The status code return by the API. It can be 400 or 404 or 409 or 500. |  |
|**message** | **String** | The reason for the request failed |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| NUMBER_400 | 400 |
| NUMBER_404 | 404 |
| NUMBER_409 | 409 |
| NUMBER_500 | 500 |



