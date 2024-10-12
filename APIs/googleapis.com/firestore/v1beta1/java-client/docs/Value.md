

# Value

A message that can hold any of the supported value types.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrayValue** | [**ArrayValue**](ArrayValue.md) |  |  [optional] |
|**booleanValue** | **Boolean** | A boolean value. |  [optional] |
|**bytesValue** | **byte[]** | A bytes value. Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries. |  [optional] |
|**doubleValue** | **Double** | A double value. |  [optional] |
|**geoPointValue** | [**LatLng**](LatLng.md) |  |  [optional] |
|**integerValue** | **String** | An integer value. |  [optional] |
|**mapValue** | [**MapValue**](MapValue.md) |  |  [optional] |
|**nullValue** | [**NullValueEnum**](#NullValueEnum) | A null value. |  [optional] |
|**referenceValue** | **String** | A reference to a document. For example: &#x60;projects/{project_id}/databases/{database_id}/documents/{document_path}&#x60;. |  [optional] |
|**stringValue** | **String** | A string value. The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries. |  [optional] |
|**timestampValue** | **String** | A timestamp value. Precise only to microseconds. When stored, any additional precision is rounded down. |  [optional] |



## Enum: NullValueEnum

| Name | Value |
|---- | -----|
| NULL_VALUE | &quot;NULL_VALUE&quot; |



