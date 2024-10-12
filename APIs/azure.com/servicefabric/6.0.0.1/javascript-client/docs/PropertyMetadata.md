# ServiceFabricClientApis.PropertyMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customTypeId** | **String** | The property&#39;s custom type id. Using this property, the user is able to tag the type of the value of the property. | [optional] 
**lastModifiedUtcTimestamp** | **Date** | Represents when the Property was last modified. Only write operations will cause this field to be updated. | [optional] 
**parent** | **String** | The Service Fabric name, including the &#39;fabric:&#39; URI scheme. | [optional] 
**sequenceNumber** | **String** | The version of the property. Every time a property is modified, its sequence number is increased. | [optional] 
**sizeInBytes** | **Number** | The length of the serialized property value. | [optional] 
**typeId** | [**PropertyValueKind**](PropertyValueKind.md) |  | [optional] 


