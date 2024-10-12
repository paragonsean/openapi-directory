# RubrikRestApi.EventCsvDownloadResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterDate** | **Date** | The requested after date filter, if applicable. | [optional] 
**afterIdResponse** | **String** | The serialized AfterId of the response, if any. | [optional] 
**beforeDate** | **Date** | The requested before date filter, if applicable. | [optional] 
**downloadLink** | **String** | The download link for the CSV file. | 
**eventSeriesStatus** | [**EventSeriesStatusV1**](EventSeriesStatusV1.md) |  | [optional] 
**eventSeverity** | [**EventSeverityV1**](EventSeverityV1.md) |  | [optional] 
**eventStatus** | [**EventStatusV1**](EventStatusV1.md) |  | [optional] 
**eventType** | [**EventTypeV1**](EventTypeV1.md) |  | [optional] 
**objectIds** | **[String]** | The requested list of object ID to filter events, if applicable. | [optional] 
**objectName** | **String** | The requested object name filter, if applicable. | [optional] 
**objectType** | [**ObjectTypeV1**](ObjectTypeV1.md) |  | [optional] 


