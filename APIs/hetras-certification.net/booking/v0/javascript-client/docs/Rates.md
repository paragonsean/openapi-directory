# HetrasBookingApiVersion0.Rates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrivalDate** | **Date** | The arrival date of the guest for this rate offer | [optional] 
**departureDate** | **Date** | The departure date of the guest for this rate offer | [optional] 
**hotelId** | **Number** | The id of the hotel the rate offers will be valid for | [optional] 
**hotelName** | **String** | The name of the hotel the rate offers will be valid for | [optional] 
**ratePlans** | [**[RatePlan]**](RatePlan.md) | List of rate plans details for rates you can find offers in the room_offers | [optional] 
**roomOffers** | [**[RoomOffer]**](RoomOffer.md) | List of room types with available rate offers ordered from ascending | [optional] 
**rooms** | [**[ReservationRoom]**](ReservationRoom.md) | List of room type details for room types you can find offers in the room_offers | [optional] 
**services** | [**[Service]**](Service.md) | List of service details for included services in offers you can find in the room_offers | [optional] 


