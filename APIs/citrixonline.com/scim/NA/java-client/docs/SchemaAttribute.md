

# SchemaAttribute

Describes a resource attribute

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseExact** | **Boolean** | Indicates whether the attribute is case sensitive |  |
|**description** | **String** | The attribute&#39;s description |  |
|**multiValued** | **Boolean** | Indicates whether the attribute can have multiple values |  |
|**name** | **String** | The attribute&#39;s name |  |
|**readOnly** | **Boolean** | Indicates whether the attribute is mutable |  |
|**required** | **Boolean** | Indicates whether the attribute is required |  |
|**schema** | **String** | The attribute&#39;s associated scheme, e.g. urn:scim:schemas:core:1.0 |  |
|**subAttributes** | [**List&lt;SchemaSubAttribute&gt;**](SchemaSubAttribute.md) | The attribute&#39;s potential sub-attributes |  [optional] |
|**type** | **String** | The attribute&#39;s data type, e.g. String |  |



