

# EvaluateUserConsentsRequest

Evaluate a user's Consents for all matching User data mappings. Note: User data mappings are indexed asynchronously, causing slight delays between the time mappings are created or updated and when they are included in EvaluateUserConsents results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consentList** | [**ConsentList**](ConsentList.md) |  |  [optional] |
|**pageSize** | **Integer** | Optional. Limit on the number of User data mappings to return in a single response. If not specified, 100 is used. May not be larger than 1000. |  [optional] |
|**pageToken** | **String** | Optional. Token to retrieve the next page of results, or empty to get the first page. |  [optional] |
|**requestAttributes** | **Map&lt;String, String&gt;** | Required. The values of request attributes associated with this access request. |  [optional] |
|**resourceAttributes** | **Map&lt;String, String&gt;** | Optional. The values of resource attributes associated with the resources being requested. If no values are specified, then all resources are queried. |  [optional] |
|**responseView** | [**ResponseViewEnum**](#ResponseViewEnum) | Optional. The view for EvaluateUserConsentsResponse. If unspecified, defaults to &#x60;BASIC&#x60; and returns &#x60;consented&#x60; as &#x60;TRUE&#x60; or &#x60;FALSE&#x60;. |  [optional] |
|**userId** | **String** | Required. User ID to evaluate consents for. |  [optional] |



## Enum: ResponseViewEnum

| Name | Value |
|---- | -----|
| RESPONSE_VIEW_UNSPECIFIED | &quot;RESPONSE_VIEW_UNSPECIFIED&quot; |
| BASIC | &quot;BASIC&quot; |
| FULL | &quot;FULL&quot; |



