# CloudDatastoreApi.MutationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflictDetected** | **Boolean** | Whether a conflict was detected for this mutation. Always false when a conflict detection strategy field is not set in the mutation. | [optional] 
**createTime** | **String** | The create time of the entity. This field will not be set after a &#39;delete&#39;. | [optional] 
**key** | [**Key**](Key.md) |  | [optional] 
**updateTime** | **String** | The update time of the entity on the server after processing the mutation. If the mutation doesn&#39;t change anything on the server, then the timestamp will be the update timestamp of the current entity. This field will not be set after a &#39;delete&#39;. | [optional] 
**version** | **String** | The version of the entity on the server after processing the mutation. If the mutation doesn&#39;t change anything on the server, then the version will be the version of the current entity or, if no entity is present, a version that is strictly greater than the version of any previous entity and less than the version of any possible future entity. | [optional] 


