

# StartTestSetGenerationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**testSetName** | **String** | The test set name for the test set generation request. |  |
|**description** | **String** | The test set description for the test set generation request. |  [optional] |
|**storageLocation** | [**StartTestSetGenerationRequestStorageLocation**](StartTestSetGenerationRequestStorageLocation.md) |  |  |
|**generationDataSource** | [**StartTestSetGenerationRequestGenerationDataSource**](StartTestSetGenerationRequestGenerationDataSource.md) |  |  |
|**roleArn** | **String** | The roleARN used for any operation in the test set to access resources in the Amazon Web Services account. |  |
|**testSetTags** | **Map&lt;String, String&gt;** | A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can&#39;t use the &lt;code&gt;UpdateTestSet&lt;/code&gt; operation to update tags. To update tags, use the &lt;code&gt;TagResource&lt;/code&gt; operation. |  [optional] |



