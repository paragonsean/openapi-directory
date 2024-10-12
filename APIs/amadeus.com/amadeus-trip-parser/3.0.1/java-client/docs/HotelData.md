

# HotelData

  Hotel product

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**amenities** | **List&lt;String&gt;** | amenities (list) |  [optional] |
|**checkInDate** | **String** | heck-in date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is today date (no dates in the past). |  [optional] |
|**checkOutDate** | **String** | check-out date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is checkInDate+1. |  [optional] |
|**confirmationNumber** | **String** | Confirmation number |  [optional] |
|**contact** | [**ContactHotel**](ContactHotel.md) |  |  [optional] |
|**description** | [**Description**](Description.md) |  |  [optional] |
|**guests** | [**Guests**](Guests.md) |  |  [optional] |
|**name** | **String** | Hotel Name |  [optional] |
|**policies** | [**Policies**](Policies.md) |  |  [optional] |
|**room** | [**Room**](Room.md) |  |  [optional] |
|**roomQuantity** | **Integer** | number of rooms (1-9) |  [optional] |



