# RandommerApi.SocialNumberApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSocialNumberGet**](SocialNumberApi.md#apiSocialNumberGet) | **GET** /api/SocialNumber | Generate a social security number
[**apiSocialNumberPost**](SocialNumberApi.md#apiSocialNumberPost) | **POST** /api/SocialNumber | Validate VAT/identity numbers



## apiSocialNumberGet

> apiSocialNumberGet(opts)

Generate a social security number

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.SocialNumberApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiSocialNumberGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiSocialNumberPost

> apiSocialNumberPost(idType, numberValidation, opts)

Validate VAT/identity numbers

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.SocialNumberApi();
let idType = new RandommerApi.IdType(); // IdType | 
let numberValidation = new RandommerApi.NumberValidation(); // NumberValidation | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiSocialNumberPost(idType, numberValidation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idType** | [**IdType**](.md)|  | 
 **numberValidation** | [**NumberValidation**](NumberValidation.md)|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined

