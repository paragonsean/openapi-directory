

# ListAdminClusterMembershipsResponse

Response message for the `GkeHub.ListAdminClusterMemberships` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminClusterMemberships** | [**List&lt;Membership&gt;**](Membership.md) | The list of matching Memberships of admin clusters. |  [optional] |
|**nextPageToken** | **String** | A token to request the next page of resources from the &#x60;ListAdminClusterMemberships&#x60; method. The value of an empty string means that there are no more resources to return. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | List of locations that could not be reached while fetching this list. |  [optional] |



