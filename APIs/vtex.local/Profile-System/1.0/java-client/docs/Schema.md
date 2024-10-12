

# Schema


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Schema&#39;s human readable description. |  |
|**documentTTL** | **Integer** | Document time to live, in days. After this many days from its creation or update, any document cerated from this schema will be deleted. |  [optional] |
|**properties** | [**SchemaProperties**](SchemaProperties.md) |  |  |
|**required** | **List&lt;String&gt;** | Schema required fields. |  |
|**title** | **String** | Schema title. |  |
|**type** | **String** | Schema type. |  |
|**vIndexed** | **List&lt;Object&gt;** |  |  [optional] |
|**vUnique** | **List&lt;Object&gt;** |  |  [optional] |
|**version** | **Integer** | Schema version. |  [optional] |



