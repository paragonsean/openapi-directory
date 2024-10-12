# FirebaseManagementApi.AnalyticsProperty

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyticsAccountId** | **String** | Output only. The ID of the [Google Analytics account](https://www.google.com/analytics/) for the Google Analytics property associated with the specified FirebaseProject. | [optional] [readonly] 
**displayName** | **String** | The display name of the Google Analytics property associated with the specified &#x60;FirebaseProject&#x60;. | [optional] 
**id** | **String** | The globally unique, Google-assigned identifier of the Google Analytics property associated with the specified &#x60;FirebaseProject&#x60;. If you called [&#x60;AddGoogleAnalytics&#x60;](../../v1beta1/projects/addGoogleAnalytics) to link the &#x60;FirebaseProject&#x60; with a Google Analytics account, the value in this &#x60;id&#x60; field is the same as the ID of the property either specified or provisioned with that call to &#x60;AddGoogleAnalytics&#x60;. | [optional] 


