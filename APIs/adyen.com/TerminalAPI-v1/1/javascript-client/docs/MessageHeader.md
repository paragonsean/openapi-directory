# AdyenTerminalApi.MessageHeader

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceID** | **String** | If Device MessageClass. | [optional] 
**messageCategory** | [**MessageCategory**](MessageCategory.md) |  | 
**messageClass** | [**MessageClass**](MessageClass.md) |  | 
**messageType** | [**MessageType**](MessageType.md) |  | 
**POIID** | **String** | Identification of a POI System or a POI Terminal for the Sale to POI protocol. | 
**protocolVersion** | **String** | If MessageCategory is Login or Diagnosis. | [optional] 
**saleID** | **String** | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. | 
**serviceID** | **String** | Required if Service or Event MessageClass message or if Device MessageClass and request from POI or response from Sale. | [optional] 


