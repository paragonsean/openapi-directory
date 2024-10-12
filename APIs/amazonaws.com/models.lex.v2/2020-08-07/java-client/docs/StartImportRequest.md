

# StartImportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**importId** | **String** | The unique identifier for the import. It is included in the response from the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html\&quot;&gt;CreateUploadUrl&lt;/a&gt; operation. |  |
|**resourceSpecification** | [**StartImportRequestResourceSpecification**](StartImportRequestResourceSpecification.md) |  |  |
|**mergeStrategy** | [**MergeStrategyEnum**](#MergeStrategyEnum) | The strategy to use when there is a name conflict between the imported resource and an existing resource. When the merge strategy is &lt;code&gt;FailOnConflict&lt;/code&gt; existing resources are not overwritten and the import fails. |  |
|**filePassword** | **String** | The password used to encrypt the zip archive that contains the resource definition. You should always encrypt the zip archive to protect it during transit between your site and Amazon Lex. |  [optional] |



## Enum: MergeStrategyEnum

| Name | Value |
|---- | -----|
| OVERWRITE | &quot;Overwrite&quot; |
| FAIL_ON_CONFLICT | &quot;FailOnConflict&quot; |
| APPEND | &quot;Append&quot; |



