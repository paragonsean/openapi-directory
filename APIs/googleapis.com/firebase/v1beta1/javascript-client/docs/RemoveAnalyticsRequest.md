# FirebaseManagementApi.RemoveAnalyticsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyticsPropertyId** | **String** | Optional. The ID of the Google Analytics property associated with the specified &#x60;FirebaseProject&#x60;. - If not set, then the Google Analytics property that is currently associated with the specified &#x60;FirebaseProject&#x60; is removed. - If set, and the specified &#x60;FirebaseProject&#x60; is currently associated with a *different* Google Analytics property, then the response is a &#x60;412 Precondition Failed&#x60; error.  | [optional] 


