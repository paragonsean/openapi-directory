# ProfileSystem.Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Schema&#39;s human readable description. | 
**documentTTL** | **Number** | Document time to live, in days. After this many days from its creation or update, any document cerated from this schema will be deleted. | [optional] 
**properties** | [**SchemaProperties**](SchemaProperties.md) |  | 
**required** | **[String]** | Schema required fields. | 
**title** | **String** | Schema title. | 
**type** | **String** | Schema type. | 
**vIndexed** | **[Object]** |  | [optional] 
**vUnique** | **[Object]** |  | [optional] 
**version** | **Number** | Schema version. | [optional] 


