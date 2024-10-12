# HotelBooking.HotelBookingQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guests** | [**[Stakeholder]**](Stakeholder.md) | minimum one guest is mandatory | 
**offerId** | **String** | offerId to book | 
**payments** | [**[Payment]**](Payment.md) | payments (often mandatory) | [optional] 
**rooms** | [**[Room]**](Room.md) | rooms repartition (when used the &#x60;rooms&#x60; array items must match the shopping offer &#x60;roomQuantity&#x60;) | [optional] 


