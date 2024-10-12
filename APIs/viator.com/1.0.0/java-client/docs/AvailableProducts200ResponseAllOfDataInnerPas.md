

# AvailableProducts200ResponseAllOfDataInnerPas

**object** detailing product availability - `pas` stands for Product Availability Schema 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**incompleteQuote** | **Boolean** | ignore (Viator only) |  [optional] |
|**productCode** | **String** | **unique alphanumeric identifier** of *this* product |  [optional] |
|**removedChildAges** | **List&lt;String&gt;** | ignore (Viator only) |  [optional] |
|**tourGrades** | [**Map&lt;String, AvailableProducts200ResponseAllOfDataInnerPasTourGradesValue&gt;**](AvailableProducts200ResponseAllOfDataInnerPasTourGradesValue.md) | **dictionary** of tour grade alphanumeric codes to tour grade objects |  [optional] |
|**travellerMix** | **String** | **alphanumeric code** indicating the combination of adults and children being enquired about |  [optional] |



