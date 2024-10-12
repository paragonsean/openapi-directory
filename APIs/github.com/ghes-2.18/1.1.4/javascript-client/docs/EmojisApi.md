# GitHubV3RestApi.EmojisApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emojisGet**](EmojisApi.md#emojisGet) | **GET** /emojis | Get emojis



## emojisGet

> {String: String} emojisGet()

Get emojis

Lists all the emojis available to use on GitHub Enterprise Server.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.EmojisApi();
apiInstance.emojisGet((error, data, response) => {
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

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

