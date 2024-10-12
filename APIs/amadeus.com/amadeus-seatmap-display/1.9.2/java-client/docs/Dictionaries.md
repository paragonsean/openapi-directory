

# Dictionaries


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**facilities** | **Map&lt;String, String&gt;** | on board facilities map. E.g: bulkhead, closet, exit door, galley, lavatory |  [optional] |
|**locations** | [**Map&lt;String, LocationValue&gt;**](LocationValue.md) |  |  [optional] |
|**seatCharacteristics** | **Map&lt;String, String&gt;** | seat characteristics dictionary allows mapping a service characteristic to its name. Possible values are part of:   IATA code: Most of the codes are defined by IATA Standard/IATA Code list 9825, Example: CH &#x3D; Chargeable Seat, W &#x3D; Window Seat, A &#x3D; Aisle              Seat, Q &#x3D; Seat in a quiet zone, E &#x3D; Exit Row Seat   Amadeus Code: defined as extension, example MV&#x3D;row with movie screen   Seat map display Code: API specific codes, example 1A_AQC_PREMIUM_SEAT&#x3D;premium seat |  [optional] |



