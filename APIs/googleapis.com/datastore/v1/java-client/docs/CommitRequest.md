

# CommitRequest

The request for Datastore.Commit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseId** | **String** | The ID of the database against which to make the request. &#39;(default)&#39; is not allowed; please use empty string &#39;&#39; to refer the default database. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The type of commit to perform. Defaults to &#x60;TRANSACTIONAL&#x60;. |  [optional] |
|**mutations** | [**List&lt;Mutation&gt;**](Mutation.md) | The mutations to perform. When mode is &#x60;TRANSACTIONAL&#x60;, mutations affecting a single entity are applied in order. The following sequences of mutations affecting a single entity are not permitted in a single &#x60;Commit&#x60; request: - &#x60;insert&#x60; followed by &#x60;insert&#x60; - &#x60;update&#x60; followed by &#x60;insert&#x60; - &#x60;upsert&#x60; followed by &#x60;insert&#x60; - &#x60;delete&#x60; followed by &#x60;update&#x60; When mode is &#x60;NON_TRANSACTIONAL&#x60;, no two mutations may affect a single entity. |  [optional] |
|**singleUseTransaction** | [**TransactionOptions**](TransactionOptions.md) |  |  [optional] |
|**transaction** | **byte[]** | The identifier of the transaction associated with the commit. A transaction identifier is returned by a call to Datastore.BeginTransaction. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| TRANSACTIONAL | &quot;TRANSACTIONAL&quot; |
| NON_TRANSACTIONAL | &quot;NON_TRANSACTIONAL&quot; |



