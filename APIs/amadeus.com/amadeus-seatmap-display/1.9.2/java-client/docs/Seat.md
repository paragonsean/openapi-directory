

# Seat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cabin** | **String** | Cabin of the seat. |  [optional] |
|**characteristicsCodes** | **List&lt;String&gt;** | List of seat characteristics (the characteristic&#39;s names can be retrieved in the seat characteristic dictionary) Possible values are part of:    IATA code: Most of the codes are defined by IATA Standard/IATA Code list 9825    Amadeus Code: defined as extension, example MV&#x3D;row with movie screen    Seat map display Code: API specific codes, example 1A_AQC_PREMIUM_SEAT&#x3D;premium seat |  [optional] |
|**coordinates** | [**Coordinates**](Coordinates.md) |  |  [optional] |
|**number** | **String** | Concatenation of the row id and the column id, for example 12B |  [optional] |
|**travelerPricing** | [**List&lt;SeatmapTravelerPricing&gt;**](SeatmapTravelerPricing.md) | Traveler&#39;s information and price |  [optional] |



