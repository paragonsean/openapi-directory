

# ListProfilesResponse

ListProfileResponse contains the list of collected profiles for deployments in projects which the user has permissions to view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Token to receive the next page of results. This field maybe empty if there are no more profiles to fetch. |  [optional] |
|**profiles** | [**List&lt;Profile&gt;**](Profile.md) | List of profiles fetched. |  [optional] |
|**skippedProfiles** | **Integer** | Number of profiles that were skipped in the current page since they were not able to be fetched successfully. This should typically be zero. A non-zero value may indicate a transient failure, in which case if the number is too high for your use case, the call may be retried. |  [optional] |



