# TheNounProject.OauthApi

All URIs are relative to *http://api.thenounproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiQuotaStatus**](OauthApi.md#getApiQuotaStatus) | **GET** /oauth/usage | Get api quota status



## getApiQuotaStatus

> getApiQuotaStatus()

Get api quota status

Returns current oauth usage and limits

### Example

```javascript
import TheNounProject from 'the_noun_project';

let apiInstance = new TheNounProject.OauthApi();
apiInstance.getApiQuotaStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

