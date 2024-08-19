# SquareConnectApi.Booking

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointmentSegments** | [**[AppointmentSegment]**](AppointmentSegment.md) | A list of appointment segments for this booking. | [optional] 
**createdAt** | **String** | The timestamp specifying the creation time of this booking, in RFC 3339 format. | [optional] 
**customerId** | **String** | The ID of the [Customer](https://developer.squareup.com/reference/square_2021-08-18/objects/Customer) object representing the customer attending this booking | [optional] 
**customerNote** | **String** | The free-text field for the customer to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a relevant [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance. | [optional] 
**id** | **String** | A unique ID of this object representing a booking. | [optional] 
**locationId** | **String** | The ID of the [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) object representing the location where the booked service is provided. | [optional] 
**sellerNote** | **String** | The free-text field for the seller to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a specific [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) instance. This field should not be visible to customers. | [optional] 
**startAt** | **String** | The timestamp specifying the starting time of this booking, in RFC 3339 format. | [optional] 
**status** | **String** | The status of the booking, describing where the booking stands with respect to the booking state machine. | [optional] 
**updatedAt** | **String** | The timestamp specifying the most recent update time of this booking, in RFC 3339 format. | [optional] 
**version** | **Number** | The revision number for the booking used for optimistic concurrency. | [optional] 


