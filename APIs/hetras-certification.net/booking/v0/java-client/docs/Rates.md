

# Rates


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrivalDate** | **OffsetDateTime** | The arrival date of the guest for this rate offer |  [optional] |
|**departureDate** | **OffsetDateTime** | The departure date of the guest for this rate offer |  [optional] |
|**hotelId** | **Integer** | The id of the hotel the rate offers will be valid for |  [optional] |
|**hotelName** | **String** | The name of the hotel the rate offers will be valid for |  [optional] |
|**ratePlans** | [**List&lt;RatePlan&gt;**](RatePlan.md) | List of rate plans details for rates you can find offers in the room_offers |  [optional] |
|**roomOffers** | [**List&lt;RoomOffer&gt;**](RoomOffer.md) | List of room types with available rate offers ordered from ascending |  [optional] |
|**rooms** | [**List&lt;ReservationRoom&gt;**](ReservationRoom.md) | List of room type details for room types you can find offers in the room_offers |  [optional] |
|**services** | [**List&lt;Service&gt;**](Service.md) | List of service details for included services in offers you can find in the room_offers |  [optional] |



