# OsfApiv2Documentation.AddonsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addonsList**](AddonsApi.md#addonsList) | **GET** /addons/ | List all addons



## addonsList

> [Addon] addonsList()

List all addons

 A paginated list of addons configurable with the OSF, for read purposes only. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 addons. Each resource in the array is a separate addon object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.AddonsApi();
apiInstance.addonsList((error, data, response) => {
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

[**[Addon]**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

