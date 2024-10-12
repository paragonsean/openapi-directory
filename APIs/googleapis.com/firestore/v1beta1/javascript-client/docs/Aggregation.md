# CloudFirestoreApi.Aggregation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | Optional. Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format &#x60;field_&#x60;. For example: &#x60;&#x60;&#x60; AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2), COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) OVER ( ... ); &#x60;&#x60;&#x60; becomes: &#x60;&#x60;&#x60; AGGREGATE COUNT_UP_TO(1) AS count_up_to_1, COUNT_UP_TO(2) AS field_1, COUNT_UP_TO(3) AS count_up_to_3, COUNT(*) AS field_2 OVER ( ... ); &#x60;&#x60;&#x60; Requires: * Must be unique across all aggregation aliases. * Conform to document field name limitations. | [optional] 
**avg** | [**Avg**](Avg.md) |  | [optional] 
**count** | [**Count**](Count.md) |  | [optional] 
**sum** | [**Sum**](Sum.md) |  | [optional] 


