# RadioMusicServices.PersonalisedCategoriesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**myCategoriesFollowsDelete**](PersonalisedCategoriesApi.md#myCategoriesFollowsDelete) | **DELETE** /my/categories/follows | Unfollow category
[**myCategoriesFollowsGet**](PersonalisedCategoriesApi.md#myCategoriesFollowsGet) | **GET** /my/categories/follows | List of followed categories
[**myCategoriesFollowsPost**](PersonalisedCategoriesApi.md#myCategoriesFollowsPost) | **POST** /my/categories/follows | Follow category



## myCategoriesFollowsDelete

> myCategoriesFollowsDelete(authorization, xAPIKey, body)

Unfollow category

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedCategoriesApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.Body1(); // Body1 | 
apiInstance.myCategoriesFollowsDelete(authorization, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**Body1**](Body1.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## myCategoriesFollowsGet

> PersonalisedCategoriesResponse myCategoriesFollowsGet(authorization, xAPIKey, opts)

List of followed categories

List of followed categories for a given user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedCategoriesApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.myCategoriesFollowsGet(authorization, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedCategoriesResponse**](PersonalisedCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## myCategoriesFollowsPost

> myCategoriesFollowsPost(authorization, xAPIKey, body)

Follow category

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedCategoriesApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.Body(); // Body | 
apiInstance.myCategoriesFollowsPost(authorization, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**Body**](Body.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

