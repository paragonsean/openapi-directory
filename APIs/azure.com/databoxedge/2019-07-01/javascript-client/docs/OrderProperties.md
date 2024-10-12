# DataBoxEdgeManagementClient.OrderProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactInformation** | [**ContactDetails**](ContactDetails.md) |  | 
**currentStatus** | [**OrderStatus**](OrderStatus.md) |  | [optional] 
**deliveryTrackingInfo** | [**[TrackingInfo]**](TrackingInfo.md) | Tracking information for the package delivered to the customer whether it has an original or a replacement device. | [optional] [readonly] 
**orderHistory** | [**[OrderStatus]**](OrderStatus.md) | List of status changes in the order. | [optional] [readonly] 
**returnTrackingInfo** | [**[TrackingInfo]**](TrackingInfo.md) | Tracking information for the package returned from the customer whether it has an original or a replacement device. | [optional] [readonly] 
**serialNumber** | **String** | Serial number of the device. | [optional] [readonly] 
**shippingAddress** | [**Address**](Address.md) |  | 


