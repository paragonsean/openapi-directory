

# RatesPerDate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**closed** | **Boolean** | Determines whether the rate is available for a stay including this date. |  |
|**closedToArrival** | **Boolean** | Determines whether the rate is available if the arrival falls on this date. |  [optional] |
|**closedToDeparture** | **Boolean** | Determines whether the rate is available if the departure falls on this date. |  [optional] |
|**date** | **String** |  |  |
|**rates** | [**Set&lt;RatePlanRate&gt;**](RatePlanRate.md) | Rate prices for each occupancy the room can accommodate. |  |
|**staythrough** | [**RatesPerDateStaythrough**](RatesPerDateStaythrough.md) |  |  [optional] |



