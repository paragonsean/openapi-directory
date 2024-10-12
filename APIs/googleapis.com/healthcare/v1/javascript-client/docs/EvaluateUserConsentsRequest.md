# CloudHealthcareApi.EvaluateUserConsentsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentList** | [**ConsentList**](ConsentList.md) |  | [optional] 
**pageSize** | **Number** | Optional. Limit on the number of User data mappings to return in a single response. If not specified, 100 is used. May not be larger than 1000. | [optional] 
**pageToken** | **String** | Optional. Token to retrieve the next page of results, or empty to get the first page. | [optional] 
**requestAttributes** | **{String: String}** | Required. The values of request attributes associated with this access request. | [optional] 
**resourceAttributes** | **{String: String}** | Optional. The values of resource attributes associated with the resources being requested. If no values are specified, then all resources are queried. | [optional] 
**responseView** | **String** | Optional. The view for EvaluateUserConsentsResponse. If unspecified, defaults to &#x60;BASIC&#x60; and returns &#x60;consented&#x60; as &#x60;TRUE&#x60; or &#x60;FALSE&#x60;. | [optional] 
**userId** | **String** | Required. User ID to evaluate consents for. | [optional] 



## Enum: ResponseViewEnum


* `RESPONSE_VIEW_UNSPECIFIED` (value: `"RESPONSE_VIEW_UNSPECIFIED"`)

* `BASIC` (value: `"BASIC"`)

* `FULL` (value: `"FULL"`)




