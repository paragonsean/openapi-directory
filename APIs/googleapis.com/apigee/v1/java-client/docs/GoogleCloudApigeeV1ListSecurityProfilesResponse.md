

# GoogleCloudApigeeV1ListSecurityProfilesResponse

Response for ListSecurityProfiles.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token that can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**securityProfiles** | [**List&lt;GoogleCloudApigeeV1SecurityProfile&gt;**](GoogleCloudApigeeV1SecurityProfile.md) | List of security profiles in the organization. The profiles may be attached or unattached to any environment. This will return latest revision of each profile. |  [optional] |



