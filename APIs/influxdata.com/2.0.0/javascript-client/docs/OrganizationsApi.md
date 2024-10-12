# InfluxOssApiService.OrganizationsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteOrgsID**](OrganizationsApi.md#deleteOrgsID) | **DELETE** /orgs/{orgID} | Delete an organization
[**deleteOrgsIDMembersID**](OrganizationsApi.md#deleteOrgsIDMembersID) | **DELETE** /orgs/{orgID}/members/{userID} | Remove a member from an organization
[**deleteOrgsIDOwnersID**](OrganizationsApi.md#deleteOrgsIDOwnersID) | **DELETE** /orgs/{orgID}/owners/{userID} | Remove an owner from an organization
[**getOrgs**](OrganizationsApi.md#getOrgs) | **GET** /orgs | List all organizations
[**getOrgsID**](OrganizationsApi.md#getOrgsID) | **GET** /orgs/{orgID} | Retrieve an organization
[**getOrgsIDMembers**](OrganizationsApi.md#getOrgsIDMembers) | **GET** /orgs/{orgID}/members | List all members of an organization
[**getOrgsIDOwners**](OrganizationsApi.md#getOrgsIDOwners) | **GET** /orgs/{orgID}/owners | List all owners of an organization
[**getOrgsIDSecrets_0**](OrganizationsApi.md#getOrgsIDSecrets_0) | **GET** /orgs/{orgID}/secrets | List all secret keys for an organization
[**patchOrgsID**](OrganizationsApi.md#patchOrgsID) | **PATCH** /orgs/{orgID} | Update an organization
[**patchOrgsIDSecrets_0**](OrganizationsApi.md#patchOrgsIDSecrets_0) | **PATCH** /orgs/{orgID}/secrets | Update secrets in an organization
[**postOrgs**](OrganizationsApi.md#postOrgs) | **POST** /orgs | Create an organization
[**postOrgsIDMembers**](OrganizationsApi.md#postOrgsIDMembers) | **POST** /orgs/{orgID}/members | Add a member to an organization
[**postOrgsIDOwners**](OrganizationsApi.md#postOrgsIDOwners) | **POST** /orgs/{orgID}/owners | Add an owner to an organization
[**postOrgsIDSecrets_0**](OrganizationsApi.md#postOrgsIDSecrets_0) | **POST** /orgs/{orgID}/secrets/delete | Delete secrets from an organization



## deleteOrgsID

> deleteOrgsID(orgID, opts)

Delete an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The ID of the organization to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteOrgsID(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The ID of the organization to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteOrgsIDMembersID

> deleteOrgsIDMembersID(userID, orgID, opts)

Remove a member from an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let userID = "userID_example"; // String | The ID of the member to remove.
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteOrgsIDMembersID(userID, orgID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the member to remove. | 
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteOrgsIDOwnersID

> deleteOrgsIDOwnersID(userID, orgID, opts)

Remove an owner from an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let userID = "userID_example"; // String | The ID of the owner to remove.
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteOrgsIDOwnersID(userID, orgID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the owner to remove. | 
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgs

> Organizations getOrgs(opts)

List all organizations

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20, // Number | 
  'descending': false, // Boolean | 
  'org': "org_example", // String | Filter organizations to a specific organization name.
  'orgID': "orgID_example", // String | Filter organizations to a specific organization ID.
  'userID': "userID_example" // String | Filter organizations to a specific user ID.
};
apiInstance.getOrgs(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **descending** | **Boolean**|  | [optional] [default to false]
 **org** | **String**| Filter organizations to a specific organization name. | [optional] 
 **orgID** | **String**| Filter organizations to a specific organization ID. | [optional] 
 **userID** | **String**| Filter organizations to a specific user ID. | [optional] 

### Return type

[**Organizations**](Organizations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgsID

> Organization getOrgsID(orgID, opts)

Retrieve an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The ID of the organization to get.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getOrgsID(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The ID of the organization to get. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgsIDMembers

> ResourceMembers getOrgsIDMembers(orgID, opts)

List all members of an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getOrgsIDMembers(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgsIDOwners

> ResourceOwners getOrgsIDOwners(orgID, opts)

List all owners of an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getOrgsIDOwners(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOrgsIDSecrets_0

> SecretKeysResponse getOrgsIDSecrets_0(orgID, opts)

List all secret keys for an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getOrgsIDSecrets_0(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**SecretKeysResponse**](SecretKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchOrgsID

> Organization patchOrgsID(orgID, patchOrganizationRequest, opts)

Update an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The ID of the organization to get.
let patchOrganizationRequest = new InfluxOssApiService.PatchOrganizationRequest(); // PatchOrganizationRequest | Organization update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchOrgsID(orgID, patchOrganizationRequest, opts, (error, data, response) => {
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
 **orgID** | **String**| The ID of the organization to get. | 
 **patchOrganizationRequest** | [**PatchOrganizationRequest**](PatchOrganizationRequest.md)| Organization update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchOrgsIDSecrets_0

> patchOrgsIDSecrets_0(orgID, requestBody, opts)

Update secrets in an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let requestBody = {key: "null"}; // {String: String} | Secret key value pairs to update/add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchOrgsIDSecrets_0(orgID, requestBody, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **requestBody** | [**{String: String}**](String.md)| Secret key value pairs to update/add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrgs

> Organization postOrgs(postOrganizationRequest, opts)

Create an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let postOrganizationRequest = new InfluxOssApiService.PostOrganizationRequest(); // PostOrganizationRequest | Organization to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postOrgs(postOrganizationRequest, opts, (error, data, response) => {
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
 **postOrganizationRequest** | [**PostOrganizationRequest**](PostOrganizationRequest.md)| Organization to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrgsIDMembers

> ResourceMember postOrgsIDMembers(orgID, addResourceMemberRequestBody, opts)

Add a member to an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postOrgsIDMembers(orgID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrgsIDOwners

> ResourceOwner postOrgsIDOwners(orgID, addResourceMemberRequestBody, opts)

Add an owner to an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postOrgsIDOwners(orgID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postOrgsIDSecrets_0

> postOrgsIDSecrets_0(orgID, secretKeys, opts)

Delete secrets from an organization

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.OrganizationsApi();
let orgID = "orgID_example"; // String | The organization ID.
let secretKeys = new InfluxOssApiService.SecretKeys(); // SecretKeys | Secret key to delete
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postOrgsIDSecrets_0(orgID, secretKeys, opts, (error, data, response) => {
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
 **orgID** | **String**| The organization ID. | 
 **secretKeys** | [**SecretKeys**](SecretKeys.md)| Secret key to delete | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

