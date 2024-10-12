# ServiceQuotas.DefaultApi

All URIs are relative to *http://servicequotas.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateServiceQuotaTemplate**](DefaultApi.md#associateServiceQuotaTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.AssociateServiceQuotaTemplate | 
[**deleteServiceQuotaIncreaseRequestFromTemplate**](DefaultApi.md#deleteServiceQuotaIncreaseRequestFromTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.DeleteServiceQuotaIncreaseRequestFromTemplate | 
[**disassociateServiceQuotaTemplate**](DefaultApi.md#disassociateServiceQuotaTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.DisassociateServiceQuotaTemplate | 
[**getAWSDefaultServiceQuota**](DefaultApi.md#getAWSDefaultServiceQuota) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.GetAWSDefaultServiceQuota | 
[**getAssociationForServiceQuotaTemplate**](DefaultApi.md#getAssociationForServiceQuotaTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.GetAssociationForServiceQuotaTemplate | 
[**getRequestedServiceQuotaChange**](DefaultApi.md#getRequestedServiceQuotaChange) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.GetRequestedServiceQuotaChange | 
[**getServiceQuota**](DefaultApi.md#getServiceQuota) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.GetServiceQuota | 
[**getServiceQuotaIncreaseRequestFromTemplate**](DefaultApi.md#getServiceQuotaIncreaseRequestFromTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.GetServiceQuotaIncreaseRequestFromTemplate | 
[**listAWSDefaultServiceQuotas**](DefaultApi.md#listAWSDefaultServiceQuotas) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListAWSDefaultServiceQuotas | 
[**listRequestedServiceQuotaChangeHistory**](DefaultApi.md#listRequestedServiceQuotaChangeHistory) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListRequestedServiceQuotaChangeHistory | 
[**listRequestedServiceQuotaChangeHistoryByQuota**](DefaultApi.md#listRequestedServiceQuotaChangeHistoryByQuota) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListRequestedServiceQuotaChangeHistoryByQuota | 
[**listServiceQuotaIncreaseRequestsInTemplate**](DefaultApi.md#listServiceQuotaIncreaseRequestsInTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListServiceQuotaIncreaseRequestsInTemplate | 
[**listServiceQuotas**](DefaultApi.md#listServiceQuotas) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListServiceQuotas | 
[**listServices**](DefaultApi.md#listServices) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListServices | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.ListTagsForResource | 
[**putServiceQuotaIncreaseRequestIntoTemplate**](DefaultApi.md#putServiceQuotaIncreaseRequestIntoTemplate) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.PutServiceQuotaIncreaseRequestIntoTemplate | 
[**requestServiceQuotaIncrease**](DefaultApi.md#requestServiceQuotaIncrease) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.RequestServiceQuotaIncrease | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;ServiceQuotasV20190624.UntagResource | 



## associateServiceQuotaTemplate

> Object associateServiceQuotaTemplate(xAmzTarget, body, opts)



Associates your quota request template with your organization. When a new account is created in your organization, the quota increase requests in the template are automatically applied to the account. You can add a quota increase request for any adjustable quota to your template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateServiceQuotaTemplate(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteServiceQuotaIncreaseRequestFromTemplate

> Object deleteServiceQuotaIncreaseRequestFromTemplate(xAmzTarget, deleteServiceQuotaIncreaseRequestFromTemplateRequest, opts)



Deletes the quota increase request for the specified quota from your quota request template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteServiceQuotaIncreaseRequestFromTemplateRequest = new ServiceQuotas.DeleteServiceQuotaIncreaseRequestFromTemplateRequest(); // DeleteServiceQuotaIncreaseRequestFromTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteServiceQuotaIncreaseRequestFromTemplate(xAmzTarget, deleteServiceQuotaIncreaseRequestFromTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **deleteServiceQuotaIncreaseRequestFromTemplateRequest** | [**DeleteServiceQuotaIncreaseRequestFromTemplateRequest**](DeleteServiceQuotaIncreaseRequestFromTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateServiceQuotaTemplate

> Object disassociateServiceQuotaTemplate(xAmzTarget, body, opts)



Disables your quota request template. After a template is disabled, the quota increase requests in the template are not applied to new accounts in your organization. Disabling a quota request template does not apply its quota increase requests.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateServiceQuotaTemplate(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAWSDefaultServiceQuota

> GetAWSDefaultServiceQuotaResponse getAWSDefaultServiceQuota(xAmzTarget, getAWSDefaultServiceQuotaRequest, opts)



Retrieves the default value for the specified quota. The default value does not reflect any quota increases.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getAWSDefaultServiceQuotaRequest = new ServiceQuotas.GetAWSDefaultServiceQuotaRequest(); // GetAWSDefaultServiceQuotaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAWSDefaultServiceQuota(xAmzTarget, getAWSDefaultServiceQuotaRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getAWSDefaultServiceQuotaRequest** | [**GetAWSDefaultServiceQuotaRequest**](GetAWSDefaultServiceQuotaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAWSDefaultServiceQuotaResponse**](GetAWSDefaultServiceQuotaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAssociationForServiceQuotaTemplate

> GetAssociationForServiceQuotaTemplateResponse getAssociationForServiceQuotaTemplate(xAmzTarget, body, opts)



Retrieves the status of the association for the quota request template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAssociationForServiceQuotaTemplate(xAmzTarget, body, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAssociationForServiceQuotaTemplateResponse**](GetAssociationForServiceQuotaTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRequestedServiceQuotaChange

> GetRequestedServiceQuotaChangeResponse getRequestedServiceQuotaChange(xAmzTarget, getRequestedServiceQuotaChangeRequest, opts)



Retrieves information about the specified quota increase request.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRequestedServiceQuotaChangeRequest = new ServiceQuotas.GetRequestedServiceQuotaChangeRequest(); // GetRequestedServiceQuotaChangeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRequestedServiceQuotaChange(xAmzTarget, getRequestedServiceQuotaChangeRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getRequestedServiceQuotaChangeRequest** | [**GetRequestedServiceQuotaChangeRequest**](GetRequestedServiceQuotaChangeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRequestedServiceQuotaChangeResponse**](GetRequestedServiceQuotaChangeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getServiceQuota

> GetServiceQuotaResponse getServiceQuota(xAmzTarget, getServiceQuotaRequest, opts)



Retrieves the applied quota value for the specified quota. For some quotas, only the default values are available. If the applied quota value is not available for a quota, the quota is not retrieved.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getServiceQuotaRequest = new ServiceQuotas.GetServiceQuotaRequest(); // GetServiceQuotaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceQuota(xAmzTarget, getServiceQuotaRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getServiceQuotaRequest** | [**GetServiceQuotaRequest**](GetServiceQuotaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceQuotaResponse**](GetServiceQuotaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getServiceQuotaIncreaseRequestFromTemplate

> GetServiceQuotaIncreaseRequestFromTemplateResponse getServiceQuotaIncreaseRequestFromTemplate(xAmzTarget, getServiceQuotaIncreaseRequestFromTemplateRequest, opts)



Retrieves information about the specified quota increase request in your quota request template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getServiceQuotaIncreaseRequestFromTemplateRequest = new ServiceQuotas.GetServiceQuotaIncreaseRequestFromTemplateRequest(); // GetServiceQuotaIncreaseRequestFromTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceQuotaIncreaseRequestFromTemplate(xAmzTarget, getServiceQuotaIncreaseRequestFromTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getServiceQuotaIncreaseRequestFromTemplateRequest** | [**GetServiceQuotaIncreaseRequestFromTemplateRequest**](GetServiceQuotaIncreaseRequestFromTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceQuotaIncreaseRequestFromTemplateResponse**](GetServiceQuotaIncreaseRequestFromTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAWSDefaultServiceQuotas

> ListAWSDefaultServiceQuotasResponse listAWSDefaultServiceQuotas(xAmzTarget, listAWSDefaultServiceQuotasRequest, opts)



Lists the default values for the quotas for the specified AWS service. A default value does not reflect any quota increases.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listAWSDefaultServiceQuotasRequest = new ServiceQuotas.ListAWSDefaultServiceQuotasRequest(); // ListAWSDefaultServiceQuotasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listAWSDefaultServiceQuotas(xAmzTarget, listAWSDefaultServiceQuotasRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listAWSDefaultServiceQuotasRequest** | [**ListAWSDefaultServiceQuotasRequest**](ListAWSDefaultServiceQuotasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListAWSDefaultServiceQuotasResponse**](ListAWSDefaultServiceQuotasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRequestedServiceQuotaChangeHistory

> ListRequestedServiceQuotaChangeHistoryResponse listRequestedServiceQuotaChangeHistory(xAmzTarget, listRequestedServiceQuotaChangeHistoryRequest, opts)



Retrieves the quota increase requests for the specified service.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRequestedServiceQuotaChangeHistoryRequest = new ServiceQuotas.ListRequestedServiceQuotaChangeHistoryRequest(); // ListRequestedServiceQuotaChangeHistoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listRequestedServiceQuotaChangeHistory(xAmzTarget, listRequestedServiceQuotaChangeHistoryRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listRequestedServiceQuotaChangeHistoryRequest** | [**ListRequestedServiceQuotaChangeHistoryRequest**](ListRequestedServiceQuotaChangeHistoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListRequestedServiceQuotaChangeHistoryResponse**](ListRequestedServiceQuotaChangeHistoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRequestedServiceQuotaChangeHistoryByQuota

> ListRequestedServiceQuotaChangeHistoryByQuotaResponse listRequestedServiceQuotaChangeHistoryByQuota(xAmzTarget, listRequestedServiceQuotaChangeHistoryByQuotaRequest, opts)



Retrieves the quota increase requests for the specified quota.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRequestedServiceQuotaChangeHistoryByQuotaRequest = new ServiceQuotas.ListRequestedServiceQuotaChangeHistoryByQuotaRequest(); // ListRequestedServiceQuotaChangeHistoryByQuotaRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listRequestedServiceQuotaChangeHistoryByQuota(xAmzTarget, listRequestedServiceQuotaChangeHistoryByQuotaRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listRequestedServiceQuotaChangeHistoryByQuotaRequest** | [**ListRequestedServiceQuotaChangeHistoryByQuotaRequest**](ListRequestedServiceQuotaChangeHistoryByQuotaRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListRequestedServiceQuotaChangeHistoryByQuotaResponse**](ListRequestedServiceQuotaChangeHistoryByQuotaResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServiceQuotaIncreaseRequestsInTemplate

> ListServiceQuotaIncreaseRequestsInTemplateResponse listServiceQuotaIncreaseRequestsInTemplate(xAmzTarget, listServiceQuotaIncreaseRequestsInTemplateRequest, opts)



Lists the quota increase requests in the specified quota request template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServiceQuotaIncreaseRequestsInTemplateRequest = new ServiceQuotas.ListServiceQuotaIncreaseRequestsInTemplateRequest(); // ListServiceQuotaIncreaseRequestsInTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listServiceQuotaIncreaseRequestsInTemplate(xAmzTarget, listServiceQuotaIncreaseRequestsInTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listServiceQuotaIncreaseRequestsInTemplateRequest** | [**ListServiceQuotaIncreaseRequestsInTemplateRequest**](ListServiceQuotaIncreaseRequestsInTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListServiceQuotaIncreaseRequestsInTemplateResponse**](ListServiceQuotaIncreaseRequestsInTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServiceQuotas

> ListServiceQuotasResponse listServiceQuotas(xAmzTarget, listServiceQuotasRequest, opts)



Lists the applied quota values for the specified AWS service. For some quotas, only the default values are available. If the applied quota value is not available for a quota, the quota is not retrieved.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServiceQuotasRequest = new ServiceQuotas.ListServiceQuotasRequest(); // ListServiceQuotasRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listServiceQuotas(xAmzTarget, listServiceQuotasRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listServiceQuotasRequest** | [**ListServiceQuotasRequest**](ListServiceQuotasRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListServiceQuotasResponse**](ListServiceQuotasResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServices

> ListServicesResponse listServices(xAmzTarget, listServicesRequest, opts)



Lists the names and codes for the services integrated with Service Quotas.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServicesRequest = new ServiceQuotas.ListServicesRequest(); // ListServicesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listServices(xAmzTarget, listServicesRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listServicesRequest** | [**ListServicesRequest**](ListServicesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Returns a list of the tags assigned to the specified applied quota.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new ServiceQuotas.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putServiceQuotaIncreaseRequestIntoTemplate

> PutServiceQuotaIncreaseRequestIntoTemplateResponse putServiceQuotaIncreaseRequestIntoTemplate(xAmzTarget, putServiceQuotaIncreaseRequestIntoTemplateRequest, opts)



Adds a quota increase request to your quota request template.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putServiceQuotaIncreaseRequestIntoTemplateRequest = new ServiceQuotas.PutServiceQuotaIncreaseRequestIntoTemplateRequest(); // PutServiceQuotaIncreaseRequestIntoTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putServiceQuotaIncreaseRequestIntoTemplate(xAmzTarget, putServiceQuotaIncreaseRequestIntoTemplateRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **putServiceQuotaIncreaseRequestIntoTemplateRequest** | [**PutServiceQuotaIncreaseRequestIntoTemplateRequest**](PutServiceQuotaIncreaseRequestIntoTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutServiceQuotaIncreaseRequestIntoTemplateResponse**](PutServiceQuotaIncreaseRequestIntoTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## requestServiceQuotaIncrease

> RequestServiceQuotaIncreaseResponse requestServiceQuotaIncrease(xAmzTarget, requestServiceQuotaIncreaseRequest, opts)



Submits a quota increase request for the specified quota.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let requestServiceQuotaIncreaseRequest = new ServiceQuotas.RequestServiceQuotaIncreaseRequest(); // RequestServiceQuotaIncreaseRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.requestServiceQuotaIncrease(xAmzTarget, requestServiceQuotaIncreaseRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **requestServiceQuotaIncreaseRequest** | [**RequestServiceQuotaIncreaseRequest**](RequestServiceQuotaIncreaseRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RequestServiceQuotaIncreaseResponse**](RequestServiceQuotaIncreaseResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Adds tags to the specified applied quota. You can include one or more tags to add to the quota.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new ServiceQuotas.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Removes tags from the specified applied quota. You can specify one or more tags to remove.

### Example

```javascript
import ServiceQuotas from 'service_quotas';
let defaultClient = ServiceQuotas.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new ServiceQuotas.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new ServiceQuotas.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

