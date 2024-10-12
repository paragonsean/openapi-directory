# AwsIoTWireless.CreateWirelessGatewayRequestLoRaWAN

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatewayEui** | **String** |  | [optional] 
**rfRegion** | **String** |  | [optional] 
**joinEuiFilters** | **[Array]** | A list of JoinEuiRange used by LoRa gateways to filter LoRa frames. | [optional] 
**netIdFilters** | **[String]** | A list of NetId values that are used by LoRa gateways to filter the uplink frames. | [optional] 
**subBands** | **[Number]** | A list of integer indicating which sub bands are supported by LoRa gateway. | [optional] 
**beaconing** | [**CreateWirelessGatewayRequestLoRaWANBeaconing**](CreateWirelessGatewayRequestLoRaWANBeaconing.md) |  | [optional] 
**maxEirp** | **Number** |  | [optional] 


