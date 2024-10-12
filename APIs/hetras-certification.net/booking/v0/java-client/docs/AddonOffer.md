

# AddonOffer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakdown** | [**List&lt;AddonOfferBreakdown&gt;**](AddonOfferBreakdown.md) | In this collection you will get an entry with price information for every day the addon service will be charged              to the folio of the reservation if the addon service is booked. |  [optional] |
|**code** | **String** | The code of the addon service |  [optional] |
|**description** | **String** | The description of the addon service |  [optional] |
|**frequency** | **String** | The frequency this addon service will be charged to the reservation. This field is a string that can be displayed,              but is not supposed to be used for computation |  [optional] |
|**name** | **String** | The name of the addon service |  [optional] |
|**rateMode** | [**RateModeEnum**](#RateModeEnum) | The price for an addon service can be per person or per room. All the prices in an offer are already calculated              for all rooms and number of persons per room. Based on this attribute you will be able to know how to calculate              the price per person and room, per room or per person depending on your needs. |  [optional] |
|**totalStay** | [**AddonOfferRate**](AddonOfferRate.md) |  |  [optional] |



## Enum: RateModeEnum

| Name | Value |
|---- | -----|
| PER_ROOM | &quot;PerRoom&quot; |
| PER_PERSON | &quot;PerPerson&quot; |



