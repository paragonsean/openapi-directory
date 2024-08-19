

# GoogleCloudAiplatformV1Index

A representation of a collection of database items organized in a way that allows for approximate nearest neighbor (a.k.a ANN) algorithms search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this Index was created. |  [optional] [readonly] |
|**deployedIndexes** | [**List&lt;GoogleCloudAiplatformV1DeployedIndexRef&gt;**](GoogleCloudAiplatformV1DeployedIndexRef.md) | Output only. The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first. |  [optional] [readonly] |
|**description** | **String** | The description of the Index. |  [optional] |
|**displayName** | **String** | Required. The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  |  [optional] |
|**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**indexStats** | [**GoogleCloudAiplatformV1IndexStats**](GoogleCloudAiplatformV1IndexStats.md) |  |  [optional] |
|**indexUpdateMethod** | [**IndexUpdateMethodEnum**](#IndexUpdateMethodEnum) | Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**metadata** | **Object** | An additional information about the Index; the schema of the metadata can be found in metadata_schema. |  [optional] |
|**metadataSchemaUri** | **String** | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |  [optional] |
|**name** | **String** | Output only. The resource name of the Index. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it. |  [optional] [readonly] |



## Enum: IndexUpdateMethodEnum

| Name | Value |
|---- | -----|
| INDEX_UPDATE_METHOD_UNSPECIFIED | &quot;INDEX_UPDATE_METHOD_UNSPECIFIED&quot; |
| BATCH_UPDATE | &quot;BATCH_UPDATE&quot; |
| STREAM_UPDATE | &quot;STREAM_UPDATE&quot; |



