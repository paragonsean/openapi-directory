# PeopleApi.PersonResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**httpStatusCode** | **Number** | **DEPRECATED** (Please use status instead) [HTTP 1.1 status code] (http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html). | [optional] 
**person** | [**Person**](Person.md) |  | [optional] 
**requestedResourceName** | **String** | The original requested resource name. May be different than the resource name on the returned person. The resource name can change when adding or removing fields that link a contact and profile such as a verified email, verified phone number, or a profile URL. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 


