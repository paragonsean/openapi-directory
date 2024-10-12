# MerakiDashboardApi.FirmwareApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganizationFirmwareUpgradesByDevice_1**](FirmwareApi.md#getOrganizationFirmwareUpgradesByDevice_1) | **GET** /organizations/{organizationId}/firmware/upgrades/byDevice | Get firmware upgrade status for the filtered devices
[**getOrganizationFirmwareUpgrades_1**](FirmwareApi.md#getOrganizationFirmwareUpgrades_1) | **GET** /organizations/{organizationId}/firmware/upgrades | Get firmware upgrade information for an organization



## getOrganizationFirmwareUpgradesByDevice_1

> [GetOrganizationFirmwareUpgradesByDevice200ResponseInner] getOrganizationFirmwareUpgradesByDevice_1(organizationId, opts)

Get firmware upgrade status for the filtered devices

Get firmware upgrade status for the filtered devices

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirmwareApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | Optional parameter to filter by network
  'serials': ["null"], // [String] | Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
  'macs': ["null"], // [String] | Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
  'firmwareUpgradeIds': ["null"], // [String] | Optional parameter to filter by firmware upgrade ids.
  'firmwareUpgradeBatchIds': ["null"] // [String] | Optional parameter to filter by firmware upgrade batch ids.
};
apiInstance.getOrganizationFirmwareUpgradesByDevice_1(organizationId, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **networkIds** | [**[String]**](String.md)| Optional parameter to filter by network | [optional] 
 **serials** | [**[String]**](String.md)| Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match. | [optional] 
 **macs** | [**[String]**](String.md)| Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match. | [optional] 
 **firmwareUpgradeIds** | [**[String]**](String.md)| Optional parameter to filter by firmware upgrade ids. | [optional] 
 **firmwareUpgradeBatchIds** | [**[String]**](String.md)| Optional parameter to filter by firmware upgrade batch ids. | [optional] 

### Return type

[**[GetOrganizationFirmwareUpgradesByDevice200ResponseInner]**](GetOrganizationFirmwareUpgradesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationFirmwareUpgrades_1

> [GetOrganizationFirmwareUpgrades200ResponseInner] getOrganizationFirmwareUpgrades_1(organizationId, opts)

Get firmware upgrade information for an organization

Get firmware upgrade information for an organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.FirmwareApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'status': ["null"], // [String] | The status of an upgrade 
  'productType': ["null"] // [String] | The product type in a given upgrade ID
};
apiInstance.getOrganizationFirmwareUpgrades_1(organizationId, opts, (error, data, response) => {
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
 **status** | [**[String]**](String.md)| The status of an upgrade  | [optional] 
 **productType** | [**[String]**](String.md)| The product type in a given upgrade ID | [optional] 

### Return type

[**[GetOrganizationFirmwareUpgrades200ResponseInner]**](GetOrganizationFirmwareUpgrades200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

