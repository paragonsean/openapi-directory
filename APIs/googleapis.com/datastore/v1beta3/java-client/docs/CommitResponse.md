

# CommitResponse

The response for Datastore.Commit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitTime** | **String** | The transaction commit timestamp. Not set for non-transactional commits. |  [optional] |
|**indexUpdates** | **Integer** | The number of index entries updated during the commit, or zero if none were updated. |  [optional] |
|**mutationResults** | [**List&lt;MutationResult&gt;**](MutationResult.md) | The result of performing the mutations. The i-th mutation result corresponds to the i-th mutation in the request. |  [optional] |



