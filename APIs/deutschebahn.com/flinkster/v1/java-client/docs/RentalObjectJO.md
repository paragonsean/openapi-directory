

# RentalObjectJO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;LinkJO&gt;**](LinkJO.md) |  |  [optional] |
|**attributes** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**category** | [**CategoryJO**](CategoryJO.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**expand** | **String** |  |  [optional] |
|**href** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**provider** | [**ProviderJO**](ProviderJO.md) |  |  [optional] |
|**providerNetworkIds** | **List&lt;Integer&gt;** |  |  [optional] |
|**providerRentalObjectId** | **String** |  |  [optional] |
|**rentalModel** | [**RentalModelEnum**](#RentalModelEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**uid** | **String** |  |  [optional] |



## Enum: RentalModelEnum

| Name | Value |
|---- | -----|
| FREEFLOATING | &quot;FREEFLOATING&quot; |
| FREEFLOATINGWITHSTATION | &quot;FREEFLOATINGWITHSTATION&quot; |
| STATIONBASED | &quot;STATIONBASED&quot; |
| PARKINGAREA | &quot;PARKINGAREA&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VEHICLE | &quot;VEHICLE&quot; |
| VEHICLEPOOL | &quot;VEHICLEPOOL&quot; |
| BIKE | &quot;BIKE&quot; |
| PEDELEC | &quot;PEDELEC&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



