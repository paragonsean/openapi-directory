# GkeHubApi.ListMembershipsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token to request the next page of resources from the &#x60;ListMemberships&#x60; method. The value of an empty string means that there are no more resources to return. | [optional] 
**resources** | [**[Membership]**](Membership.md) | The list of matching Memberships. | [optional] 
**unreachable** | **[String]** | List of locations that could not be reached while fetching this list. | [optional] 


