# IxApi.NetworkServicesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkServiceCancellationPolicyRead**](NetworkServicesApi.md#networkServiceCancellationPolicyRead) | **GET** /network-services/{id}/cancellation-policy | 
[**networkServiceChangeRequestCreate**](NetworkServicesApi.md#networkServiceChangeRequestCreate) | **POST** /network-services/{id}/change-request | 
[**networkServiceChangeRequestDestroy**](NetworkServicesApi.md#networkServiceChangeRequestDestroy) | **DELETE** /network-services/{id}/change-request | 
[**networkServiceChangeRequestRead**](NetworkServicesApi.md#networkServiceChangeRequestRead) | **GET** /network-services/{id}/change-request | 
[**networkServicesCreate**](NetworkServicesApi.md#networkServicesCreate) | **POST** /network-services | 
[**networkServicesDestroy**](NetworkServicesApi.md#networkServicesDestroy) | **DELETE** /network-services/{id} | 
[**networkServicesList**](NetworkServicesApi.md#networkServicesList) | **GET** /network-services | 
[**networkServicesPartialUpdate**](NetworkServicesApi.md#networkServicesPartialUpdate) | **PATCH** /network-services/{id} | 
[**networkServicesRead**](NetworkServicesApi.md#networkServicesRead) | **GET** /network-services/{id} | 
[**networkServicesUpdate**](NetworkServicesApi.md#networkServicesUpdate) | **PUT** /network-services/{id} | 



## networkServiceCancellationPolicyRead

> CancellationPolicy networkServiceCancellationPolicyRead(id, opts)



The cancellation-policy can be queried to answer the questions:  If I cancel my service, *when will it be technically decommissioned*? If I cancel my service, *until what date will I be charged*?  When the query parameter &#x60;decommision_at&#x60; is not provided it will provide the first possible cancellation date and charge period if cancelled at above date.  The granularity of the date field is a day, the start and end of which are to be interpreted by the IXP (some may use UTC, some may use their local time zone).

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'decommissionAt': "decommissionAt_example" // String | By providing a date in the format `YYYY-MM-DD` you can query the policy what would happen if you request a decommissioning on this date.
};
apiInstance.networkServiceCancellationPolicyRead(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **decommissionAt** | **String**| By providing a date in the format &#x60;YYYY-MM-DD&#x60; you can query the policy what would happen if you request a decommissioning on this date. | [optional] 

### Return type

[**CancellationPolicy**](CancellationPolicy.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServiceChangeRequestCreate

> NetworkServiceChangeRequest networkServiceChangeRequestCreate(id, opts)



Request a change to the network service.  A participant in a network service of type &#x60;p2p_vc&#x60; can issue a change request, expressing a desired change in the capacity. The change is accepted when all sides have configured the network service configs with the new bandwidth. These changes can sometimes require a change of the product offering. The product offering may only differ in regards to bandwidth.  The network service will change it&#39;s state from &#x60;production&#x60; into &#x60;production_change_pending&#x60;.  Only one change request may be issued at a time.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkServiceChangeRequest': new IxApi.NetworkServiceChangeRequest() // NetworkServiceChangeRequest | NetworkServiceChangeRequest
};
apiInstance.networkServiceChangeRequestCreate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **networkServiceChangeRequest** | [**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)| NetworkServiceChangeRequest | [optional] 

### Return type

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkServiceChangeRequestDestroy

> NetworkServiceChangeRequest networkServiceChangeRequestDestroy(id)



Retract or reject a change to the network service.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
apiInstance.networkServiceChangeRequestDestroy(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServiceChangeRequestRead

> NetworkServiceChangeRequest networkServiceChangeRequestRead(id)



Get the change request.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
apiInstance.networkServiceChangeRequestRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**NetworkServiceChangeRequest**](NetworkServiceChangeRequest.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServicesCreate

> NetworkService networkServicesCreate(opts)



Create a new network service

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let opts = {
  'networkServiceRequest': new IxApi.NetworkServiceRequest() // NetworkServiceRequest | Polymorphic Network Service Request
};
apiInstance.networkServicesCreate(opts, (error, data, response) => {
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
 **networkServiceRequest** | [**NetworkServiceRequest**](NetworkServiceRequest.md)| Polymorphic Network Service Request | [optional] 

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkServicesDestroy

> NetworkService networkServicesDestroy(id, opts)



Request decomissioning of the network service.  The network service will enter the state of &#x60;decommission_requested&#x60;. The request will cascade to related network service and feature configs.  An *optional request body* can be provided to request a specific service termination date.  If no date is given in the request body, it is assumed to be the earliest possible date.  Possible values for &#x60;decommission_at&#x60; can be queried through the &#x60;network_service_cancellation_policy_read&#x60; operation.  The response will contain the dates on which the changes will be effected.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'cancellationRequest': new IxApi.CancellationRequest() // CancellationRequest | Service Cancellation Request
};
apiInstance.networkServicesDestroy(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **cancellationRequest** | [**CancellationRequest**](CancellationRequest.md)| Service Cancellation Request | [optional] 

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkServicesList

> [NetworkService] networkServicesList(opts)



List available &#x60;NetworkService&#x60;s.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'state': "state_example", // String | Filter by state
  'stateIsNot': "stateIsNot_example", // String | Filter by state__is_not
  'managingAccount': "managingAccount_example", // String | Filter by managing_account
  'consumingAccount': "consumingAccount_example", // String | Filter by consuming_account
  'externalRef': "externalRef_example", // String | Filter by external_ref
  'type': "type_example", // String | Filter by type
  'pop': "pop_example", // String | Filter by pop
  'productOffering': "productOffering_example" // String | Filter by product_offering
};
apiInstance.networkServicesList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **state** | **String**| Filter by state | [optional] 
 **stateIsNot** | **String**| Filter by state__is_not | [optional] 
 **managingAccount** | **String**| Filter by managing_account | [optional] 
 **consumingAccount** | **String**| Filter by consuming_account | [optional] 
 **externalRef** | **String**| Filter by external_ref | [optional] 
 **type** | **String**| Filter by type | [optional] 
 **pop** | **String**| Filter by pop | [optional] 
 **productOffering** | **String**| Filter by product_offering | [optional] 

### Return type

[**[NetworkService]**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServicesPartialUpdate

> NetworkService networkServicesPartialUpdate(id, opts)



Partially update a network service

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkServiceRequestPartial': new IxApi.NetworkServiceRequestPartial() // NetworkServiceRequestPartial | Polymorphic Network Service Request
};
apiInstance.networkServicesPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **networkServiceRequestPartial** | [**NetworkServiceRequestPartial**](NetworkServiceRequestPartial.md)| Polymorphic Network Service Request | [optional] 

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## networkServicesRead

> NetworkService networkServicesRead(id)



Get a specific &#x60;network-service&#x60; by id.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
apiInstance.networkServicesRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkServicesUpdate

> NetworkService networkServicesUpdate(id, opts)



Update a network service

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.NetworkServicesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'networkServiceRequest': new IxApi.NetworkServiceRequest() // NetworkServiceRequest | Polymorphic Network Service Request
};
apiInstance.networkServicesUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **networkServiceRequest** | [**NetworkServiceRequest**](NetworkServiceRequest.md)| Polymorphic Network Service Request | [optional] 

### Return type

[**NetworkService**](NetworkService.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

