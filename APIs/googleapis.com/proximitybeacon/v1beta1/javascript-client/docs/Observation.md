# ProximityBeaconApi.Observation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertisedId** | [**AdvertisedId**](AdvertisedId.md) |  | [optional] 
**telemetry** | **Blob** | The array of telemetry bytes received from the beacon. The server is responsible for parsing it. This field may frequently be empty, as with a beacon that transmits telemetry only occasionally. | [optional] 
**timestampMs** | **String** | Time when the beacon was observed. | [optional] 


