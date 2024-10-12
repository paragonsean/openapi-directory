

# EventsEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakEven** | **Integer** | Value of the break-even for the event. |  [optional] |
|**cancellationDate** | **LocalDate** | Date the event was canceled. |  [optional] |
|**contract** | [**EventsEntityContract**](EventsEntityContract.md) |  |  |
|**costingCapacity** | **Integer** | Costing capacity of the event. |  [optional] |
|**creationTimestamp** | **Long** | Timestamp for when the venue was created in the customer&#39;s database. |  |
|**currency** | **String** | Currency of the prices. |  [optional] |
|**datetime** | **String** | Datetime of the event (relative to the timezone of the venue). |  |
|**free** | **Boolean** | Whether this event is free or not. |  |
|**generalSalesDate** | **LocalDate** | Date the event went on general sales (relative to the timezone of the venue). |  [optional] |
|**id** | **Integer** | Unique ID of the event. |  |
|**inputType** | [**EventsEntityInputType**](EventsEntityInputType.md) |  |  |
|**label** | **String** | Label of the event. |  |
|**lastUpdateTimestamp** | **Long** | Timestamp for when the venue was last updated in the customer&#39;s database. |  |
|**maxCapacity** | **Integer** | Maximum capacity for the venue in which the event occurs. |  [optional] |
|**presalesDate** | **LocalDate** | Date the event went on presales (relative to the timezone of the venue). |  [optional] |
|**seriesId** | **Integer** | ID of the series the event belongs to. |  |
|**soldOutDate** | **LocalDate** | Date the event was sold out. |  [optional] |
|**venue** | [**VenuesEntity**](VenuesEntity.md) |  |  |



