# AmazonCloudDirectory.CreateIndexRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orderedIndexedAttributeList** | [**[AttributeKey]**](AttributeKey.md) | Specifies the attributes that should be indexed on. Currently only a single attribute is supported. | 
**isUnique** | **Boolean** | Indicates whether the attribute that is being indexed has unique values or not. | 
**parentReference** | [**AddFacetToObjectRequestObjectReference**](AddFacetToObjectRequestObjectReference.md) |  | [optional] 
**linkName** | **String** | The name of the link between the parent object and the index object. | [optional] 


