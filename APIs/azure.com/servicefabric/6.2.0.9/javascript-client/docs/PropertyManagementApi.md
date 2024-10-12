# ServiceFabricClientApis.PropertyManagementApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createName**](PropertyManagementApi.md#createName) | **POST** /Names/$/Create | Creates a Service Fabric name.
[**deleteName**](PropertyManagementApi.md#deleteName) | **DELETE** /Names/{nameId} | Deletes a Service Fabric name.
[**deleteProperty**](PropertyManagementApi.md#deleteProperty) | **DELETE** /Names/{nameId}/$/GetProperty | Deletes the specified Service Fabric property.
[**getNameExistsInfo**](PropertyManagementApi.md#getNameExistsInfo) | **GET** /Names/{nameId} | Returns whether the Service Fabric name exists.
[**getPropertyInfo**](PropertyManagementApi.md#getPropertyInfo) | **GET** /Names/{nameId}/$/GetProperty | Gets the specified Service Fabric property.
[**getPropertyInfoList**](PropertyManagementApi.md#getPropertyInfoList) | **GET** /Names/{nameId}/$/GetProperties | Gets information on all Service Fabric properties under a given name.
[**getSubNameInfoList**](PropertyManagementApi.md#getSubNameInfoList) | **GET** /Names/{nameId}/$/GetSubNames | Enumerates all the Service Fabric names under a given name.
[**putProperty**](PropertyManagementApi.md#putProperty) | **PUT** /Names/{nameId}/$/GetProperty | Creates or updates a Service Fabric property.
[**submitPropertyBatch**](PropertyManagementApi.md#submitPropertyBatch) | **POST** /Names/{nameId}/$/GetProperties/$/SubmitBatch | Submits a property batch.



## createName

> createName(apiVersion, nameDescription, opts)

Creates a Service Fabric name.

Creates the specified Service Fabric name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameDescription = new ServiceFabricClientApis.NameDescription(); // NameDescription | Describes the Service Fabric name to be created.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.createName(apiVersion, nameDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameDescription** | [**NameDescription**](NameDescription.md)| Describes the Service Fabric name to be created. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteName

> deleteName(apiVersion, nameId, opts)

Deletes a Service Fabric name.

Deletes the specified Service Fabric name. A name must be created before it can be deleted. Deleting a name with child properties will fail.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.deleteName(apiVersion, nameId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProperty

> deleteProperty(apiVersion, nameId, propertyName, opts)

Deletes the specified Service Fabric property.

Deletes the specified Service Fabric property under a given name. A property must be created before it can be deleted.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let propertyName = "propertyName_example"; // String | Specifies the name of the property to get.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.deleteProperty(apiVersion, nameId, propertyName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **propertyName** | **String**| Specifies the name of the property to get. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNameExistsInfo

> getNameExistsInfo(apiVersion, nameId, opts)

Returns whether the Service Fabric name exists.

Returns whether the specified Service Fabric name exists.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getNameExistsInfo(apiVersion, nameId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPropertyInfo

> PropertyInfo getPropertyInfo(apiVersion, nameId, propertyName, opts)

Gets the specified Service Fabric property.

Gets the specified Service Fabric property under a given name. This will always return both value and metadata.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let propertyName = "propertyName_example"; // String | Specifies the name of the property to get.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPropertyInfo(apiVersion, nameId, propertyName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **propertyName** | **String**| Specifies the name of the property to get. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PropertyInfo**](PropertyInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPropertyInfoList

> PagedPropertyInfoList getPropertyInfoList(apiVersion, nameId, opts)

Gets information on all Service Fabric properties under a given name.

A Service Fabric name can have one or more named properties that stores custom information. This operation gets the information about these properties in a paged list. The information include name, value and metadata about each of the properties.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let opts = {
  'includeValues': false, // Boolean | Allows specifying whether to include the values of the properties returned. True if values should be returned with the metadata; False to return only property metadata.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPropertyInfoList(apiVersion, nameId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **includeValues** | **Boolean**| Allows specifying whether to include the values of the properties returned. True if values should be returned with the metadata; False to return only property metadata. | [optional] [default to false]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedPropertyInfoList**](PagedPropertyInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubNameInfoList

> PagedSubNameInfoList getSubNameInfoList(apiVersion, nameId, opts)

Enumerates all the Service Fabric names under a given name.

Enumerates all the Service Fabric names under a given name. If the subnames do not fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. Querying a name that doesn&#39;t exist will fail.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let opts = {
  'recursive': false, // Boolean | Allows specifying that the search performed should be recursive.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getSubNameInfoList(apiVersion, nameId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **recursive** | **Boolean**| Allows specifying that the search performed should be recursive. | [optional] [default to false]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedSubNameInfoList**](PagedSubNameInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putProperty

> putProperty(apiVersion, nameId, propertyDescription, opts)

Creates or updates a Service Fabric property.

Creates or updates the specified Service Fabric property under a given name.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let propertyDescription = new ServiceFabricClientApis.PropertyDescription(); // PropertyDescription | Describes the Service Fabric property to be created.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.putProperty(apiVersion, nameId, propertyDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **propertyDescription** | [**PropertyDescription**](PropertyDescription.md)| Describes the Service Fabric property to be created. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitPropertyBatch

> SuccessfulPropertyBatchInfo submitPropertyBatch(apiVersion, nameId, propertyBatchDescriptionList, opts)

Submits a property batch.

Submits a batch of property operations. Either all or none of the operations will be committed.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.PropertyManagementApi();
let apiVersion = "'6.0'"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
let nameId = "nameId_example"; // String | The Service Fabric name, without the 'fabric:' URI scheme.
let propertyBatchDescriptionList = new ServiceFabricClientApis.PropertyBatchDescriptionList(); // PropertyBatchDescriptionList | Describes the property batch operations to be submitted.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.submitPropertyBatch(apiVersion, nameId, propertyBatchDescriptionList, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to &#39;6.0&#39;]
 **nameId** | **String**| The Service Fabric name, without the &#39;fabric:&#39; URI scheme. | 
 **propertyBatchDescriptionList** | [**PropertyBatchDescriptionList**](PropertyBatchDescriptionList.md)| Describes the property batch operations to be submitted. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**SuccessfulPropertyBatchInfo**](SuccessfulPropertyBatchInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

