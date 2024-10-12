# AwsIoTWireless.GetPositionEstimateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wiFiAccessPoints** | [**[WiFiAccessPoint]**](WiFiAccessPoint.md) | Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HERE&#39;s Wi-Fi based solver. | [optional] 
**cellTowers** | [**GetPositionEstimateRequestCellTowers**](GetPositionEstimateRequestCellTowers.md) |  | [optional] 
**ip** | [**GetPositionEstimateRequestIp**](GetPositionEstimateRequestIp.md) |  | [optional] 
**gnss** | [**GetPositionEstimateRequestGnss**](GetPositionEstimateRequestGnss.md) |  | [optional] 
**timestamp** | **Date** | Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used. | [optional] 


