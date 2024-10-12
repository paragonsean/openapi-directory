

# RoutingPreference

Routing preference defines the type of network, either microsoft or internet routing to be used to deliver the user data, the default option is microsoft routing

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publishInternetEndpoints** | **Boolean** | A boolean flag which indicates whether internet routing storage endpoints are to be published |  [optional] |
|**publishMicrosoftEndpoints** | **Boolean** | A boolean flag which indicates whether microsoft routing storage endpoints are to be published |  [optional] |
|**routingChoice** | [**RoutingChoiceEnum**](#RoutingChoiceEnum) | Routing Choice defines the kind of network routing opted by the user. |  [optional] |



## Enum: RoutingChoiceEnum

| Name | Value |
|---- | -----|
| MICROSOFT_ROUTING | &quot;MicrosoftRouting&quot; |
| INTERNET_ROUTING | &quot;InternetRouting&quot; |



