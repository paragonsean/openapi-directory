

# ListAvailableOrgPolicyConstraintsResponse

The response returned from the `ListAvailableOrgPolicyConstraints` method. Returns all `Constraints` that could be set at this level of the hierarchy (contrast with the response from `ListPolicies`, which returns all policies which are set).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraints** | [**List&lt;Constraint&gt;**](Constraint.md) | The collection of constraints that are settable on the request resource. |  [optional] |
|**nextPageToken** | **String** | Page token used to retrieve the next page. This is currently not used. |  [optional] |



