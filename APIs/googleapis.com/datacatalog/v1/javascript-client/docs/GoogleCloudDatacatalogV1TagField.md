# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1TagField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolValue** | **Boolean** | The value of a tag field with a boolean type. | [optional] 
**displayName** | **String** | Output only. The display name of this field. | [optional] [readonly] 
**doubleValue** | **Number** | The value of a tag field with a double type. | [optional] 
**enumValue** | [**GoogleCloudDatacatalogV1TagFieldEnumValue**](GoogleCloudDatacatalogV1TagFieldEnumValue.md) |  | [optional] 
**order** | **Number** | Output only. The order of this field with respect to other fields in this tag. Can be set by Tag. For example, a higher value can indicate a more important field. The value can be negative. Multiple fields can have the same order, and field orders within a tag don&#39;t have to be sequential. | [optional] [readonly] 
**richtextValue** | **String** | The value of a tag field with a rich text type. The maximum length is 10 MiB as this value holds HTML descriptions including encoded images. The maximum length of the text without images is 100 KiB. | [optional] 
**stringValue** | **String** | The value of a tag field with a string type. The maximum length is 2000 UTF-8 characters. | [optional] 
**timestampValue** | **String** | The value of a tag field with a timestamp type. | [optional] 


