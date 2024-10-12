

# ListBoundMembershipsResponse

List of Memberships bound to a Scope.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**memberships** | [**List&lt;Membership&gt;**](Membership.md) | The list of Memberships bound to the given Scope. |  [optional] |
|**nextPageToken** | **String** | A token to request the next page of resources from the &#x60;ListBoundMemberships&#x60; method. The value of an empty string means that there are no more resources to return. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | List of locations that could not be reached while fetching this list. |  [optional] |



