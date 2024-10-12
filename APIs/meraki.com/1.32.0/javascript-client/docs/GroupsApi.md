# MerakiDashboardApi.GroupsApi

All URIs are relative to *https://api.meraki.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkFirmwareUpgradesStagedGroup_3**](GroupsApi.md#createNetworkFirmwareUpgradesStagedGroup_3) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network
[**createOrganizationAdaptivePolicyGroup_2**](GroupsApi.md#createOrganizationAdaptivePolicyGroup_2) | **POST** /organizations/{organizationId}/adaptivePolicy/groups | Creates a new adaptive policy group
[**createOrganizationPolicyObjectsGroup_2**](GroupsApi.md#createOrganizationPolicyObjectsGroup_2) | **POST** /organizations/{organizationId}/policyObjects/groups | Creates a new Policy Object Group.
[**deleteNetworkFirmwareUpgradesStagedGroup_3**](GroupsApi.md#deleteNetworkFirmwareUpgradesStagedGroup_3) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group
[**deleteOrganizationAdaptivePolicyGroup_2**](GroupsApi.md#deleteOrganizationAdaptivePolicyGroup_2) | **DELETE** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Deletes the specified adaptive policy group and any associated policies and references
[**deleteOrganizationPolicyObjectsGroup_2**](GroupsApi.md#deleteOrganizationPolicyObjectsGroup_2) | **DELETE** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Deletes a Policy Object Group.
[**getNetworkFirmwareUpgradesStagedGroup_3**](GroupsApi.md#getNetworkFirmwareUpgradesStagedGroup_3) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network
[**getNetworkFirmwareUpgradesStagedGroups_3**](GroupsApi.md#getNetworkFirmwareUpgradesStagedGroups_3) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network
[**getOrganizationAdaptivePolicyGroup_2**](GroupsApi.md#getOrganizationAdaptivePolicyGroup_2) | **GET** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Returns an adaptive policy group
[**getOrganizationAdaptivePolicyGroups_2**](GroupsApi.md#getOrganizationAdaptivePolicyGroups_2) | **GET** /organizations/{organizationId}/adaptivePolicy/groups | List adaptive policy groups in a organization
[**getOrganizationPolicyObjectsGroup_2**](GroupsApi.md#getOrganizationPolicyObjectsGroup_2) | **GET** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Shows details of a Policy Object Group.
[**getOrganizationPolicyObjectsGroups_2**](GroupsApi.md#getOrganizationPolicyObjectsGroups_2) | **GET** /organizations/{organizationId}/policyObjects/groups | Lists Policy Object Groups belonging to the organization.
[**updateNetworkFirmwareUpgradesStagedGroup_3**](GroupsApi.md#updateNetworkFirmwareUpgradesStagedGroup_3) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network
[**updateOrganizationAdaptivePolicyGroup_2**](GroupsApi.md#updateOrganizationAdaptivePolicyGroup_2) | **PUT** /organizations/{organizationId}/adaptivePolicy/groups/{id} | Updates an adaptive policy group
[**updateOrganizationPolicyObjectsGroup_2**](GroupsApi.md#updateOrganizationPolicyObjectsGroup_2) | **PUT** /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId} | Updates a Policy Object Group.



## createNetworkFirmwareUpgradesStagedGroup_3

> Object createNetworkFirmwareUpgradesStagedGroup_3(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

Create a Staged Upgrade Group for a network

Create a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let networkId = "networkId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.createNetworkFirmwareUpgradesStagedGroup_3(networkId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationAdaptivePolicyGroup_2

> Object createOrganizationAdaptivePolicyGroup_2(organizationId, createOrganizationAdaptivePolicyGroupRequest)

Creates a new adaptive policy group

Creates a new adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationAdaptivePolicyGroupRequest = new MerakiDashboardApi.CreateOrganizationAdaptivePolicyGroupRequest(); // CreateOrganizationAdaptivePolicyGroupRequest | 
apiInstance.createOrganizationAdaptivePolicyGroup_2(organizationId, createOrganizationAdaptivePolicyGroupRequest, (error, data, response) => {
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
 **createOrganizationAdaptivePolicyGroupRequest** | [**CreateOrganizationAdaptivePolicyGroupRequest**](CreateOrganizationAdaptivePolicyGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOrganizationPolicyObjectsGroup_2

> Object createOrganizationPolicyObjectsGroup_2(organizationId, createOrganizationPolicyObjectsGroupRequest)

Creates a new Policy Object Group.

Creates a new Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let createOrganizationPolicyObjectsGroupRequest = new MerakiDashboardApi.CreateOrganizationPolicyObjectsGroupRequest(); // CreateOrganizationPolicyObjectsGroupRequest | 
apiInstance.createOrganizationPolicyObjectsGroup_2(organizationId, createOrganizationPolicyObjectsGroupRequest, (error, data, response) => {
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
 **createOrganizationPolicyObjectsGroupRequest** | [**CreateOrganizationPolicyObjectsGroupRequest**](CreateOrganizationPolicyObjectsGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNetworkFirmwareUpgradesStagedGroup_3

> deleteNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId)

Delete a Staged Upgrade Group

Delete a Staged Upgrade Group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, (error, data, response) => {
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
 **networkId** | **String**|  | 
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationAdaptivePolicyGroup_2

> deleteOrganizationAdaptivePolicyGroup_2(organizationId, id)

Deletes the specified adaptive policy group and any associated policies and references

Deletes the specified adaptive policy group and any associated policies and references

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.deleteOrganizationAdaptivePolicyGroup_2(organizationId, id, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteOrganizationPolicyObjectsGroup_2

> deleteOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId)

Deletes a Policy Object Group.

Deletes a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
apiInstance.deleteOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, (error, data, response) => {
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
 **organizationId** | **String**|  | 
 **policyObjectGroupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkFirmwareUpgradesStagedGroup_3

> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId)

Get a Staged Upgrade Group from a network

Get a Staged Upgrade Group from a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

[**GetNetworkFirmwareUpgradesStagedGroups200ResponseInner**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkFirmwareUpgradesStagedGroups_3

> [GetNetworkFirmwareUpgradesStagedGroups200ResponseInner] getNetworkFirmwareUpgradesStagedGroups_3(networkId)

List of Staged Upgrade Groups in a network

List of Staged Upgrade Groups in a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let networkId = "networkId_example"; // String | 
apiInstance.getNetworkFirmwareUpgradesStagedGroups_3(networkId, (error, data, response) => {
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

### Return type

[**[GetNetworkFirmwareUpgradesStagedGroups200ResponseInner]**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroup_2

> Object getOrganizationAdaptivePolicyGroup_2(organizationId, id)

Returns an adaptive policy group

Returns an adaptive policy group

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroup_2(organizationId, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationAdaptivePolicyGroups_2

> [Object] getOrganizationAdaptivePolicyGroups_2(organizationId)

List adaptive policy groups in a organization

List adaptive policy groups in a organization

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
apiInstance.getOrganizationAdaptivePolicyGroups_2(organizationId, (error, data, response) => {
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

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObjectsGroup_2

> Object getOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId)

Shows details of a Policy Object Group.

Shows details of a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
apiInstance.getOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, (error, data, response) => {
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
 **policyObjectGroupId** | **String**|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrganizationPolicyObjectsGroups_2

> [Object] getOrganizationPolicyObjectsGroups_2(organizationId, opts)

Lists Policy Object Groups belonging to the organization.

Lists Policy Object Groups belonging to the organization.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let opts = {
  'perPage': 56, // Number | The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
  'startingAfter': "startingAfter_example", // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
  'endingBefore': "endingBefore_example" // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
};
apiInstance.getOrganizationPolicyObjectsGroups_2(organizationId, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000. | [optional] 
 **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 
 **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] 

### Return type

**[Object]**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNetworkFirmwareUpgradesStagedGroup_3

> Object updateNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

Update a Staged Upgrade Group for a network

Update a Staged Upgrade Group for a network

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let networkId = "networkId_example"; // String | 
let groupId = "groupId_example"; // String | 
let createNetworkFirmwareUpgradesStagedGroupRequest = new MerakiDashboardApi.CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
apiInstance.updateNetworkFirmwareUpgradesStagedGroup_3(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationAdaptivePolicyGroup_2

> Object updateOrganizationAdaptivePolicyGroup_2(organizationId, id, opts)

Updates an adaptive policy group

Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'updateOrganizationAdaptivePolicyGroupRequest': new MerakiDashboardApi.UpdateOrganizationAdaptivePolicyGroupRequest() // UpdateOrganizationAdaptivePolicyGroupRequest | 
};
apiInstance.updateOrganizationAdaptivePolicyGroup_2(organizationId, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **updateOrganizationAdaptivePolicyGroupRequest** | [**UpdateOrganizationAdaptivePolicyGroupRequest**](UpdateOrganizationAdaptivePolicyGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOrganizationPolicyObjectsGroup_2

> Object updateOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, opts)

Updates a Policy Object Group.

Updates a Policy Object Group.

### Example

```javascript
import MerakiDashboardApi from 'meraki_dashboard_api';
let defaultClient = MerakiDashboardApi.ApiClient.instance;
// Configure API key authorization: meraki_api_key
let meraki_api_key = defaultClient.authentications['meraki_api_key'];
meraki_api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//meraki_api_key.apiKeyPrefix = 'Token';

let apiInstance = new MerakiDashboardApi.GroupsApi();
let organizationId = "organizationId_example"; // String | 
let policyObjectGroupId = "policyObjectGroupId_example"; // String | 
let opts = {
  'updateOrganizationPolicyObjectsGroupRequest': new MerakiDashboardApi.UpdateOrganizationPolicyObjectsGroupRequest() // UpdateOrganizationPolicyObjectsGroupRequest | 
};
apiInstance.updateOrganizationPolicyObjectsGroup_2(organizationId, policyObjectGroupId, opts, (error, data, response) => {
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
 **policyObjectGroupId** | **String**|  | 
 **updateOrganizationPolicyObjectsGroupRequest** | [**UpdateOrganizationPolicyObjectsGroupRequest**](UpdateOrganizationPolicyObjectsGroupRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

