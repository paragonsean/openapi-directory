# HotelSearchApi.Hotel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandCode** | **String** | Brand (RT...) (Amadeus 2 chars Code). Small Properties distributed by Merchants may not have a Brand. Example - AD (Value Hotels) is the Provider/Merchant, and RT (Accor) is the Brand of the Property | [optional] 
**chainCode** | **String** | Brand (RT...) or Merchant (AD...) (Amadeus 2 chars Code) | [optional] 
**cityCode** | **String** | Warning: The IATA city code associated to the hotel (not necessary the real Hotel City) | [optional] 
**dupeId** | **String** | Unique Property identifier of the physical hotel. One physical hotel can be represented by different Providers, each one having its own &#x60;hotelID&#x60;. This attribute allows a client application to group together hotels that are actually the same. | [optional] 
**hotelId** | **String** | Amadeus Property Code (8 chars) | [optional] 
**name** | **String** | Hotel Name | [optional] 


