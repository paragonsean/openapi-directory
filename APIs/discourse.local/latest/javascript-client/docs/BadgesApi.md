# DiscourseApiDocumentation.BadgesApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminListBadges**](BadgesApi.md#adminListBadges) | **GET** /admin/badges.json | List badges
[**createBadge**](BadgesApi.md#createBadge) | **POST** /admin/badges.json | Create badge
[**deleteBadge**](BadgesApi.md#deleteBadge) | **DELETE** /admin/badges/{id}.json | Delete badge
[**listUserBadges**](BadgesApi.md#listUserBadges) | **GET** /user-badges/{username}.json | List badges for a user
[**updateBadge**](BadgesApi.md#updateBadge) | **PUT** /admin/badges/{id}.json | Update badge



## adminListBadges

> AdminListBadges200Response adminListBadges()

List badges

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BadgesApi();
apiInstance.adminListBadges((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AdminListBadges200Response**](AdminListBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBadge

> CreateBadge200Response createBadge(opts)

Create badge

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BadgesApi();
let opts = {
  'createBadgeRequest': new DiscourseApiDocumentation.CreateBadgeRequest() // CreateBadgeRequest | 
};
apiInstance.createBadge(opts, (error, data, response) => {
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
 **createBadgeRequest** | [**CreateBadgeRequest**](CreateBadgeRequest.md)|  | [optional] 

### Return type

[**CreateBadge200Response**](CreateBadge200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteBadge

> deleteBadge(id)

Delete badge

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BadgesApi();
let id = 56; // Number | 
apiInstance.deleteBadge(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listUserBadges

> ListUserBadges200Response listUserBadges(username)

List badges for a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BadgesApi();
let username = "username_example"; // String | 
apiInstance.listUserBadges(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**ListUserBadges200Response**](ListUserBadges200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBadge

> CreateBadge200Response updateBadge(id, opts)

Update badge

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.BadgesApi();
let id = 56; // Number | 
let opts = {
  'createBadgeRequest': new DiscourseApiDocumentation.CreateBadgeRequest() // CreateBadgeRequest | 
};
apiInstance.updateBadge(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **createBadgeRequest** | [**CreateBadgeRequest**](CreateBadgeRequest.md)|  | [optional] 

### Return type

[**CreateBadge200Response**](CreateBadge200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

