

# ListOrgPoliciesResponse

The response returned from the `ListOrgPolicies` method. It will be empty if no `Policies` are set on the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token. |  [optional] |
|**policies** | [**List&lt;OrgPolicy&gt;**](OrgPolicy.md) | The &#x60;Policies&#x60; that are set on the resource. It will be empty if no &#x60;Policies&#x60; are set. |  [optional] |



