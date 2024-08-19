# ImpalaHotelBookingApi.CancellationPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **String** | The time (in the hotel&#39;s local timezone) at which the policy takes effect, in ISO 8601 format. If omitted, the policy applies open-ended until the guests&#39; stay. | [optional] 
**fee** | [**CancellationFee**](CancellationFee.md) |  | 
**formatted** | **String** | Human-readable plain English cancellation policy information, ready to be shown to your guests. | 
**start** | **String** | The time (in the hotel&#39;s local timezone) at which the policy takes effect, in ISO 8601 format. If omitted, the policy is already in effect. | 


