# Pims.EventsEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakEven** | **Number** | Value of the break-even for the event. | [optional] 
**cancellationDate** | **Date** | Date the event was canceled. | [optional] 
**contract** | [**EventsEntityContract**](EventsEntityContract.md) |  | 
**costingCapacity** | **Number** | Costing capacity of the event. | [optional] 
**creationTimestamp** | **Number** | Timestamp for when the venue was created in the customer&#39;s database. | 
**currency** | **String** | Currency of the prices. | [optional] 
**datetime** | **String** | Datetime of the event (relative to the timezone of the venue). | 
**free** | **Boolean** | Whether this event is free or not. | 
**generalSalesDate** | **Date** | Date the event went on general sales (relative to the timezone of the venue). | [optional] 
**id** | **Number** | Unique ID of the event. | 
**inputType** | [**EventsEntityInputType**](EventsEntityInputType.md) |  | 
**label** | **String** | Label of the event. | 
**lastUpdateTimestamp** | **Number** | Timestamp for when the venue was last updated in the customer&#39;s database. | 
**maxCapacity** | **Number** | Maximum capacity for the venue in which the event occurs. | [optional] 
**presalesDate** | **Date** | Date the event went on presales (relative to the timezone of the venue). | [optional] 
**seriesId** | **Number** | ID of the series the event belongs to. | 
**soldOutDate** | **Date** | Date the event was sold out. | [optional] 
**venue** | [**VenuesEntity**](VenuesEntity.md) |  | 


