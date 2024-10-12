# SquareConnectApi.BusinessBookingProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowUserCancel** | **Boolean** | Indicates whether customers can cancel or reschedule their own bookings (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
**bookingEnabled** | **Boolean** | Indicates whether the seller is open for booking. | [optional] 
**bookingPolicy** | **String** | The policy for the seller to automatically accept booking requests (&#x60;ACCEPT_ALL&#x60;) or not (&#x60;REQUIRES_ACCEPTANCE&#x60;). | [optional] 
**businessAppointmentSettings** | [**BusinessAppointmentSettings**](BusinessAppointmentSettings.md) |  | [optional] 
**createdAt** | **String** | The RFC 3339 timestamp specifying the booking&#39;s creation time. | [optional] 
**customerTimezoneChoice** | **String** | The choice of customer&#39;s time zone information of a booking. The Square online booking site and all notifications to customers uses either the seller location’s time zone or the time zone the customer chooses at booking. | [optional] 
**sellerId** | **String** | The ID of the seller, obtainable using the Merchants API. | [optional] 


