# MerakiDashboardApi.LicensingApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationLicensingCotermLicenses**](LicensingApi.md#getOrganizationLicensingCotermLicenses) | **GET** /organizations/{organizationId}/licensing/coterm/licenses | List the licenses in a coterm organization
[**moveOrganizationLicensingCotermLicenses**](LicensingApi.md#moveOrganizationLicensingCotermLicenses) | **POST** /organizations/{organizationId}/licensing/coterm/licenses/move | Moves a license to a different organization (coterm only)



## getOrganizationLicensingCotermLicenses

> [GetOrganizationLicensingCotermLicenses200ResponseInner] getOrganizationLicensingCotermLicenses(organizationId, opts)

List the licenses in a coterm organization

List the licenses in a coterm organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LicensingApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'invalidated': true, // Boolean | Filter for licenses that are invalidated
  'expired': true // Boolean | Filter for licenses that are expired
};
apiInstance.getOrganizationLicensingCotermLicenses(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **invalidated** | **Boolean**| Filter for licenses that are invalidated | [optional] 
 **expired** | **Boolean**| Filter for licenses that are expired | [optional] 

### Return type

[**[GetOrganizationLicensingCotermLicenses200ResponseInner]**](GetOrganizationLicensingCotermLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## moveOrganizationLicensingCotermLicenses

> MoveOrganizationLicensingCotermLicenses200Response moveOrganizationLicensingCotermLicenses(organizationId, moveOrganizationLicensingCotermLicensesRequest)

Moves a license to a different organization (coterm only)

Moves a license to a different organization (coterm only)

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.LicensingApi();
let organizationId = "organizationId_example"; // String | 
let moveOrganizationLicensingCotermLicensesRequest = new MerakiDashboardApi.MoveOrganizationLicensingCotermLicensesRequest(); // MoveOrganizationLicensingCotermLicensesRequest | 
apiInstance.moveOrganizationLicensingCotermLicenses(organizationId, moveOrganizationLicensingCotermLicensesRequest, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **moveOrganizationLicensingCotermLicensesRequest** | [**MoveOrganizationLicensingCotermLicensesRequest**](MoveOrganizationLicensingCotermLicensesRequest.md)|  | 

### Return type

[**MoveOrganizationLicensingCotermLicenses200Response**](MoveOrganizationLicensingCotermLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

