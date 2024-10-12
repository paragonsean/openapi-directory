# MerakiDashboardApi.UplinksApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeviceApplianceUplinksSettings_1**](UplinksApi.md#getDeviceApplianceUplinksSettings_1) | **GET** /devices/{serial}/appliance/uplinks/settings | Return the uplink settings for an MX appliance
[**getDeviceLossAndLatencyHistory_1**](UplinksApi.md#getDeviceLossAndLatencyHistory_1) | **GET** /devices/{serial}/lossAndLatencyHistory | Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
[**getNetworkApplianceUplinksUsageHistory_1**](UplinksApi.md#getNetworkApplianceUplinksUsageHistory_1) | **GET** /networks/{networkId}/appliance/uplinks/usageHistory | Get the sent and received bytes for each uplink of a network.
[**getOrganizationApplianceUplinkStatuses_1**](UplinksApi.md#getOrganizationApplianceUplinkStatuses_1) | **GET** /organizations/{organizationId}/appliance/uplink/statuses | List the uplink status of every Meraki MX and Z series appliances in the organization
[**getOrganizationDevicesUplinksAddressesByDevice_2**](UplinksApi.md#getOrganizationDevicesUplinksAddressesByDevice_2) | **GET** /organizations/{organizationId}/devices/uplinks/addresses/byDevice | List the current uplink addresses for devices in an organization.
[**getOrganizationDevicesUplinksLossAndLatency_2**](UplinksApi.md#getOrganizationDevicesUplinksLossAndLatency_2) | **GET** /organizations/{organizationId}/devices/uplinksLossAndLatency | Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
[**getOrganizationUplinksStatuses_1**](UplinksApi.md#getOrganizationUplinksStatuses_1) | **GET** /organizations/{organizationId}/uplinks/statuses | List the uplink status of every Meraki MX, MG and Z series devices in the organization
[**updateDeviceApplianceUplinksSettings_1**](UplinksApi.md#updateDeviceApplianceUplinksSettings_1) | **PUT** /devices/{serial}/appliance/uplinks/settings | Update the uplink settings for an MX appliance



## getDeviceApplianceUplinksSettings_1

> GetDeviceApplianceUplinksSettings200Response getDeviceApplianceUplinksSettings_1(serial)

Return the uplink settings for an MX appliance

Return the uplink settings for an MX appliance

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let serial = "serial_example"; // String | 
apiInstance.getDeviceApplianceUplinksSettings_1(serial, (error, data, response) => {
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
 **serial** | **String**|  | 

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeviceLossAndLatencyHistory_1

> [Object] getDeviceLossAndLatencyHistory_1(serial, ip, opts)

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let serial = "serial_example"; // String | 
let ip = "ip_example"; // String | The destination IP used to obtain the requested stats. This is required.
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
  'resolution': 56, // Number | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
  'uplink': "uplink_example" // String | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
};
apiInstance.getDeviceLossAndLatencyHistory_1(serial, ip, opts, (error, data, response) => {
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
 **serial** | **String**|  | 
 **ip** | **String**| The destination IP used to obtain the requested stats. This is required. | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 60 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. | [optional] 
 **uplink** | **String**| The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkApplianceUplinksUsageHistory_1

> [Object] getNetworkApplianceUplinksUsageHistory_1(networkId, opts)

Get the sent and received bytes for each uplink of a network.

Get the sent and received bytes for each uplink of a network.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let networkId = "networkId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
  'resolution': 56 // Number | The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
};
apiInstance.getNetworkApplianceUplinksUsageHistory_1(networkId, opts, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes. | [optional] 
 **resolution** | **Number**| The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationApplianceUplinkStatuses_1

> [Object] getOrganizationApplianceUplinkStatuses_1(organizationId, opts)

List the uplink status of every Meraki MX and Z series appliances in the organization

List the uplink status of every Meraki MX and Z series appliances in the organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | A list of network IDs. The returned devices will be filtered to only include these networks.
  'serials': ["null"], // [String] | A list of serial numbers. The returned devices will be filtered to only include these serials.
  'iccids': ["null"] // [String] | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
};
apiInstance.getOrganizationApplianceUplinkStatuses_1(organizationId, opts, (error, data, response) => {
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
 **networkIds** | [**[String]**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] 
 **serials** | [**[String]**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] 
 **iccids** | [**[String]**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationDevicesUplinksAddressesByDevice_2

> [GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner] getOrganizationDevicesUplinksAddressesByDevice_2(organizationId, opts)

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

let apiInstance = new MerakiDashboardApi.UplinksApi();
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
apiInstance.getOrganizationDevicesUplinksAddressesByDevice_2(organizationId, opts, (error, data, response) => {
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


## getOrganizationDevicesUplinksLossAndLatency_2

> [GetOrganizationDevicesUplinksLossAndLatency200ResponseInner] getOrganizationDevicesUplinksLossAndLatency_2(organizationId, opts)

Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  't0': "t0_example", // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
  't1': "t1_example", // String | The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
  'timespan': 3.4, // Number | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
  'uplink': "uplink_example", // String | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
  'ip': "ip_example" // String | Optional filter for a specific destination IP. Default will return all destination IPs.
};
apiInstance.getOrganizationDevicesUplinksLossAndLatency_2(organizationId, opts, (error, data, response) => {
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
 **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 60 days from today. | [optional] 
 **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past. | [optional] 
 **timespan** | **Number**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes. | [optional] 
 **uplink** | **String**| Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks. | [optional] 
 **ip** | **String**| Optional filter for a specific destination IP. Default will return all destination IPs. | [optional] 

### Return type

[**[GetOrganizationDevicesUplinksLossAndLatency200ResponseInner]**](GetOrganizationDevicesUplinksLossAndLatency200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationUplinksStatuses_1

> [GetOrganizationUplinksStatuses200ResponseInner] getOrganizationUplinksStatuses_1(organizationId, opts)

List the uplink status of every Meraki MX, MG and Z series devices in the organization

List the uplink status of every Meraki MX, MG and Z series devices in the organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example", // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'networkIds': ["null"], // [String] | A list of network IDs. The returned devices will be filtered to only include these networks.
  'serials': ["null"], // [String] | A list of serial numbers. The returned devices will be filtered to only include these serials.
  'iccids': ["null"] // [String] | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
};
apiInstance.getOrganizationUplinksStatuses_1(organizationId, opts, (error, data, response) => {
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
 **networkIds** | [**[String]**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] 
 **serials** | [**[String]**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] 
 **iccids** | [**[String]**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] 

### Return type

[**[GetOrganizationUplinksStatuses200ResponseInner]**](GetOrganizationUplinksStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDeviceApplianceUplinksSettings_1

> GetDeviceApplianceUplinksSettings200Response updateDeviceApplianceUplinksSettings_1(serial, updateDeviceApplianceUplinksSettingsRequest)

Update the uplink settings for an MX appliance

Update the uplink settings for an MX appliance

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.UplinksApi();
let serial = "serial_example"; // String | 
let updateDeviceApplianceUplinksSettingsRequest = new MerakiDashboardApi.UpdateDeviceApplianceUplinksSettingsRequest(); // UpdateDeviceApplianceUplinksSettingsRequest | 
apiInstance.updateDeviceApplianceUplinksSettings_1(serial, updateDeviceApplianceUplinksSettingsRequest, (error, data, response) => {
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
 **serial** | **String**|  | 
 **updateDeviceApplianceUplinksSettingsRequest** | [**UpdateDeviceApplianceUplinksSettingsRequest**](UpdateDeviceApplianceUplinksSettingsRequest.md)|  | 

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

