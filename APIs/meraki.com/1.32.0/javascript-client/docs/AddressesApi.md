# MerakiDashboardApi.AddressesApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationDevicesUplinksAddressesByDevice_3**](AddressesApi.md#getOrganizationDevicesUplinksAddressesByDevice_3) | **GET** /organizations/{organizationId}/devices/uplinks/addresses/byDevice | List the current uplink addresses for devices in an organization.



## getOrganizationDevicesUplinksAddressesByDevice_3

> [GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner] getOrganizationDevicesUplinksAddressesByDevice_3(organizationId, opts)

List the current uplink addresses for devices in an organization.

List the current uplink addresses for devices in an organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.AddressesApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
  'productTypes': ["null"], // [String] | Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
  'serials': ["null"], // [String] | Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
  'tags': ["null"], // [String] | An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
  'tagsFilterType': "tagsFilterType_example" // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
};
apiInstance.getOrganizationDevicesUplinksAddressesByDevice_3(organizationId, opts, (error, data, response) => {
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
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches. | [optional] 
 **productTypes** | [**[String]**](String.md)| Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches. | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. | [optional] 
 **tags** | [**[String]**](String.md)| An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches. | [optional] 
 **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] 

### Return type

[**[GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner]**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

