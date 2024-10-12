# ServiceFabricClientApis.MeshServicesApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meshServiceGet**](MeshServicesApi.md#meshServiceGet) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName} | Gets the Service resource with the given name.
[**meshServiceList**](MeshServicesApi.md#meshServiceList) | **GET** /Resources/Applications/{applicationResourceName}/Services | Lists all the service resources.



## meshServiceGet

> ServiceResourceDescription meshServiceGet(apiVersion, applicationResourceName, serviceResourceName)

Gets the Service resource with the given name.

Gets the information about the Service resource with the given name. The information include the description and other properties of the Service.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshServicesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
apiInstance.meshServiceGet(apiVersion, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meshServiceList

> PagedServiceResourceDescriptionList meshServiceList(apiVersion, applicationResourceName)

Lists all the service resources.

Gets the information about all services of an application resource. The information include the description and other properties of the Service.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.MeshServicesApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
apiInstance.meshServiceList(apiVersion, applicationResourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **applicationResourceName** | **String**| The identity of the application. | 

### Return type

[**PagedServiceResourceDescriptionList**](PagedServiceResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

