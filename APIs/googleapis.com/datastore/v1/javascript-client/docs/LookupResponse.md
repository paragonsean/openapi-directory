# CloudDatastoreApi.LookupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred** | [**[Key]**](Key.md) | A list of keys that were not looked up due to resource constraints. The order of results in this field is undefined and has no relation to the order of the keys in the input. | [optional] 
**found** | [**[EntityResult]**](EntityResult.md) | Entities found as &#x60;ResultType.FULL&#x60; entities. The order of results in this field is undefined and has no relation to the order of the keys in the input. | [optional] 
**missing** | [**[EntityResult]**](EntityResult.md) | Entities not found as &#x60;ResultType.KEY_ONLY&#x60; entities. The order of results in this field is undefined and has no relation to the order of the keys in the input. | [optional] 
**readTime** | **String** | The time at which these entities were read or found missing. | [optional] 
**transaction** | **Blob** | The identifier of the transaction that was started as part of this Lookup request. Set only when ReadOptions.new_transaction was set in LookupRequest.read_options. | [optional] 


