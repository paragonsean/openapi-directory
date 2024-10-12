# CloudFirestoreApi.Value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arrayValue** | [**ArrayValue**](ArrayValue.md) |  | [optional] 
**booleanValue** | **Boolean** | A boolean value. | [optional] 
**bytesValue** | **Blob** | A bytes value. Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries. | [optional] 
**doubleValue** | **Number** | A double value. | [optional] 
**geoPointValue** | [**LatLng**](LatLng.md) |  | [optional] 
**integerValue** | **String** | An integer value. | [optional] 
**mapValue** | [**MapValue**](MapValue.md) |  | [optional] 
**nullValue** | **String** | A null value. | [optional] 
**referenceValue** | **String** | A reference to a document. For example: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. | [optional] 
**stringValue** | **String** | A string value. The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries. | [optional] 
**timestampValue** | **String** | A timestamp value. Precise only to microseconds. When stored, any additional precision is rounded down. | [optional] 



## Enum: NullValueEnum


* `NULL_VALUE` (value: `"NULL_VALUE"`)




