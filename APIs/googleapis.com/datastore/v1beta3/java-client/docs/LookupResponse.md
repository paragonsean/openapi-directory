

# LookupResponse

The response for Datastore.Lookup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deferred** | [**List&lt;Key&gt;**](Key.md) | A list of keys that were not looked up due to resource constraints. The order of results in this field is undefined and has no relation to the order of the keys in the input. |  [optional] |
|**found** | [**List&lt;EntityResult&gt;**](EntityResult.md) | Entities found as &#x60;ResultType.FULL&#x60; entities. The order of results in this field is undefined and has no relation to the order of the keys in the input. |  [optional] |
|**missing** | [**List&lt;EntityResult&gt;**](EntityResult.md) | Entities not found as &#x60;ResultType.KEY_ONLY&#x60; entities. The order of results in this field is undefined and has no relation to the order of the keys in the input. |  [optional] |
|**readTime** | **String** | The time at which these entities were read or found missing. |  [optional] |



