# CloudHealthcareApi.CheckDataAccessRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentList** | [**ConsentList**](ConsentList.md) |  | [optional] 
**dataId** | **String** | Required. The unique identifier of the resource to check access for. This identifier must correspond to a User data mapping in the given consent store. | [optional] 
**requestAttributes** | **{String: String}** | The values of request attributes associated with this access request. | [optional] 
**responseView** | **String** | Optional. The view for CheckDataAccessResponse. If unspecified, defaults to &#x60;BASIC&#x60; and returns &#x60;consented&#x60; as &#x60;TRUE&#x60; or &#x60;FALSE&#x60;. | [optional] 



## Enum: ResponseViewEnum


* `RESPONSE_VIEW_UNSPECIFIED` (value: `"RESPONSE_VIEW_UNSPECIFIED"`)

* `BASIC` (value: `"BASIC"`)

* `FULL` (value: `"FULL"`)




