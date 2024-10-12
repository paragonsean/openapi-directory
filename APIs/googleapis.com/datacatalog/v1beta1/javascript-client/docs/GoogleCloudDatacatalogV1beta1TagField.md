# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1TagField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolValue** | **Boolean** | Holds the value for a tag field with boolean type. | [optional] 
**displayName** | **String** | Output only. The display name of this field. | [optional] [readonly] 
**doubleValue** | **Number** | Holds the value for a tag field with double type. | [optional] 
**enumValue** | [**GoogleCloudDatacatalogV1beta1TagFieldEnumValue**](GoogleCloudDatacatalogV1beta1TagFieldEnumValue.md) |  | [optional] 
**order** | **Number** | Output only. The order of this field with respect to other fields in this tag. It can be set in Tag. For example, a higher value can indicate a more important field. The value can be negative. Multiple fields can have the same order, and field orders within a tag do not have to be sequential. | [optional] [readonly] 
**stringValue** | **String** | Holds the value for a tag field with string type. | [optional] 
**timestampValue** | **String** | Holds the value for a tag field with timestamp type. | [optional] 


