

# WirelessGatewayStatisticsLoRaWAN


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewayEui** | [**String**](String.md) |  |  [optional] |
|**rfRegion** | [**String**](String.md) |  |  [optional] |
|**joinEuiFilters** | **List&lt;List&lt;String&gt;&gt;** | A list of JoinEuiRange used by LoRa gateways to filter LoRa frames. |  [optional] |
|**netIdFilters** | **List&lt;String&gt;** | A list of NetId values that are used by LoRa gateways to filter the uplink frames. |  [optional] |
|**subBands** | **List&lt;Integer&gt;** | A list of integer indicating which sub bands are supported by LoRa gateway. |  [optional] |
|**beaconing** | [**CreateWirelessGatewayRequestLoRaWANBeaconing**](CreateWirelessGatewayRequestLoRaWANBeaconing.md) |  |  [optional] |
|**maxEirp** | [**Float**](Float.md) |  |  [optional] |



