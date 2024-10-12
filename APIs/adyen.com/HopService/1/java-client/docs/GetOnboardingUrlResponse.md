

# GetOnboardingUrlResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invalidFields** | [**List&lt;ErrorFieldTypeWrapper&gt;**](ErrorFieldTypeWrapper.md) | Information about any invalid fields. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**redirectUrl** | **String** | The URL to the Hosted Onboarding Page where you should redirect your sub-merchant. This URL must be used within 30 seconds and can only be used once. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**submittedAsync** | **Boolean** | Indicates whether the request is processed asynchronously. Depending on the request&#39;s platform settings, the following scenarios may be applied: * **true**: The request is queued and will be executed when the providing service is available in the order in which the requests are received. * **false**: The processing of the request is immediately attempted; it may result in an error if the providing service is unavailable. |  [optional] |



