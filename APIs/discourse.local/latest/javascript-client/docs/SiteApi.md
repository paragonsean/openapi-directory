# DiscourseApiDocumentation.SiteApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSite**](SiteApi.md#getSite) | **GET** /site.json | Get site info



## getSite

> GetSite200Response getSite()

Get site info

Can be used to fetch all categories and subcategories

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.SiteApi();
apiInstance.getSite((error, data, response) => {
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

[**GetSite200Response**](GetSite200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

