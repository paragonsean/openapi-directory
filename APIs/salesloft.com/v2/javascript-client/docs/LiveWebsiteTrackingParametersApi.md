# SalesLoftPlatform.LiveWebsiteTrackingParametersApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2LiveWebsiteTrackingParametersJsonPost**](LiveWebsiteTrackingParametersApi.md#v2LiveWebsiteTrackingParametersJsonPost) | **POST** /v2/live_website_tracking_parameters.json | Create an Live Website Tracking Parameter



## v2LiveWebsiteTrackingParametersJsonPost

> LiveWebsiteTrackingParameter v2LiveWebsiteTrackingParametersJsonPost(personId)

Create an Live Website Tracking Parameter

Creates a Live Website Tracking parameter to identify a person 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.LiveWebsiteTrackingParametersApi();
let personId = 56; // Number | The person to create the LiveWebsiteTrackingParameter for
apiInstance.v2LiveWebsiteTrackingParametersJsonPost(personId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **personId** | **Number**| The person to create the LiveWebsiteTrackingParameter for | 

### Return type

[**LiveWebsiteTrackingParameter**](LiveWebsiteTrackingParameter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

