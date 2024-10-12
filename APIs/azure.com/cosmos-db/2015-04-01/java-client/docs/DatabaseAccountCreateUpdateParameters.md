

# DatabaseAccountCreateUpdateParameters

Parameters to create and update Cosmos DB database accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | Indicates the type of database account. This can only be set at database account creation. |  [optional] |
|**properties** | [**DatabaseAccountCreateUpdateProperties**](DatabaseAccountCreateUpdateProperties.md) |  |  |
|**id** | **String** | The unique resource identifier of the database account. |  [optional] [readonly] |
|**location** | **String** | The location of the resource group to which the resource belongs. |  [optional] |
|**name** | **String** | The name of the database account. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with \&quot;defaultExperience\&quot;: \&quot;Cassandra\&quot;. Current \&quot;defaultExperience\&quot; values also include \&quot;Table\&quot;, \&quot;Graph\&quot;, \&quot;DocumentDB\&quot;, and \&quot;MongoDB\&quot;. |  [optional] |
|**type** | **String** | The type of Azure resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| GLOBAL_DOCUMENT_DB | &quot;GlobalDocumentDB&quot; |
| MONGO_DB | &quot;MongoDB&quot; |
| PARSE | &quot;Parse&quot; |



