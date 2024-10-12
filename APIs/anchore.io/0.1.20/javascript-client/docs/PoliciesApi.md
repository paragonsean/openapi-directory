# AnchoreEngineApiServer.PoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPolicy**](PoliciesApi.md#addPolicy) | **POST** /policies | Add a new policy
[**deletePolicy**](PoliciesApi.md#deletePolicy) | **DELETE** /policies/{policyId} | Delete policy
[**getPolicy**](PoliciesApi.md#getPolicy) | **GET** /policies/{policyId} | Get specific policy
[**listPolicies**](PoliciesApi.md#listPolicies) | **GET** /policies | List policies
[**updatePolicy**](PoliciesApi.md#updatePolicy) | **PUT** /policies/{policyId} | Update policy



## addPolicy

> PolicyBundleRecord addPolicy(policyBundle, opts)

Add a new policy

Adds a new policy bundle to the system

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.PoliciesApi();
let policyBundle = new AnchoreEngineApiServer.PolicyBundle(); // PolicyBundle | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.addPolicy(policyBundle, opts, (error, data, response) => {
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
 **policyBundle** | [**PolicyBundle**](PolicyBundle.md)|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**PolicyBundleRecord**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePolicy

> deletePolicy(policyId, opts)

Delete policy

Delete the specified policy

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.PoliciesApi();
let policyId = "policyId_example"; // String | 
let opts = {
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.deletePolicy(policyId, opts, (error, data, response) => {
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
 **policyId** | **String**|  | 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolicy

> [PolicyBundleRecord] getPolicy(policyId, opts)

Get specific policy

Get the policy bundle content

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.PoliciesApi();
let policyId = "policyId_example"; // String | 
let opts = {
  'detail': true, // Boolean | Include policy bundle detail in the form of the full bundle content for each entry
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.getPolicy(policyId, opts, (error, data, response) => {
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
 **policyId** | **String**|  | 
 **detail** | **Boolean**| Include policy bundle detail in the form of the full bundle content for each entry | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[PolicyBundleRecord]**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPolicies

> [PolicyBundleRecord] listPolicies(opts)

List policies

List all saved policy bundles

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.PoliciesApi();
let opts = {
  'detail': true, // Boolean | Include policy bundle detail in the form of the full bundle content for each entry
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.listPolicies(opts, (error, data, response) => {
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
 **detail** | **Boolean**| Include policy bundle detail in the form of the full bundle content for each entry | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[PolicyBundleRecord]**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePolicy

> [PolicyBundleRecord] updatePolicy(policyId, policyBundleRecord, opts)

Update policy

Update/replace and existing policy

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.PoliciesApi();
let policyId = "policyId_example"; // String | 
let policyBundleRecord = new AnchoreEngineApiServer.PolicyBundleRecord(); // PolicyBundleRecord | 
let opts = {
  'active': true, // Boolean | Mark policy as active
  'xAnchoreAccount': "xAnchoreAccount_example" // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
};
apiInstance.updatePolicy(policyId, policyBundleRecord, opts, (error, data, response) => {
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
 **policyId** | **String**|  | 
 **policyBundleRecord** | [**PolicyBundleRecord**](PolicyBundleRecord.md)|  | 
 **active** | **Boolean**| Mark policy as active | [optional] 
 **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] 

### Return type

[**[PolicyBundleRecord]**](PolicyBundleRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

