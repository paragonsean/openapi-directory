

# HotelOffer

Hotel Offer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boardType** | **BoardType** |  |  [optional] |
|**category** | **String** | Special Rate Category Examples:   ASSOCIATION   FAMILY_PLAN |  [optional] |
|**checkInDate** | **LocalDate** | check-in date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is today date (no dates in the past). |  [optional] |
|**checkOutDate** | **LocalDate** | check-out date of the stay (hotel local date). Format YYYY-MM-DD The lowest accepted value is &#x60;checkInDate&#x60;+1. |  [optional] |
|**commission** | [**HotelProductCommission**](HotelProductCommission.md) |  |  [optional] |
|**description** | [**QualifiedFreeText**](QualifiedFreeText.md) |  |  [optional] |
|**guests** | [**HotelProductGuests**](HotelProductGuests.md) |  |  [optional] |
|**id** | **String** | Unique identifier of this offer. Might be valid for a temporary period only. |  |
|**policies** | [**HotelProductPolicyDetails**](HotelProductPolicyDetails.md) |  |  [optional] |
|**price** | [**HotelProductHotelPrice**](HotelProductHotelPrice.md) |  |  |
|**rateCode** | **String** | Special Rate - Provider Response Code (3 chars) Examples    * RAC - Rack    * BAR - Best Available Rate    * PRO - Promotional    * COR - Corporate    * GOV - Government (qualified)    * AAA - AAA (qualified)    * BNB - Bed and Breakfast    * PKG - Package    * TVL - Travel Industry    * SPC - Special Promo Rate    * WKD - Weekend    * CON - Convention    * SNR - Senior (Europe) (qualified)    * ARP - AARP - American Association of Retired People (50+) (qualified)    * SRS - Senior (qualified)    * ROR - Room Only Rate (no breakfast)    * FAM - Family    * DAY - Day rate |  |
|**rateFamilyEstimated** | [**HotelProductRateFamily**](HotelProductRateFamily.md) |  |  [optional] |
|**room** | [**HotelProductRoomDetails**](HotelProductRoomDetails.md) |  |  |
|**roomQuantity** | **String** | number of rooms (1-9) |  [optional] |
|**self** | **String** | A self link to the object. Use this to refresh the Offer price |  [optional] |
|**type** | **Type** |  |  [optional] |



