# SecurityCenter.RegulatoryComplianceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regulatoryComplianceAssessmentsGet**](RegulatoryComplianceApi.md#regulatoryComplianceAssessmentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName}/regulatoryComplianceAssessments/{regulatoryComplianceAssessmentName} | 
[**regulatoryComplianceAssessmentsList**](RegulatoryComplianceApi.md#regulatoryComplianceAssessmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName}/regulatoryComplianceAssessments | 
[**regulatoryComplianceControlsGet**](RegulatoryComplianceApi.md#regulatoryComplianceControlsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName} | 
[**regulatoryComplianceControlsList**](RegulatoryComplianceApi.md#regulatoryComplianceControlsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls | 
[**regulatoryComplianceStandardsGet**](RegulatoryComplianceApi.md#regulatoryComplianceStandardsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName} | 
[**regulatoryComplianceStandardsList**](RegulatoryComplianceApi.md#regulatoryComplianceStandardsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards | 



## regulatoryComplianceAssessmentsGet

> RegulatoryComplianceAssessment regulatoryComplianceAssessmentsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, regulatoryComplianceAssessmentName)



Supported regulatory compliance details and state for selected assessment

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
let regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
let regulatoryComplianceAssessmentName = "regulatoryComplianceAssessmentName_example"; // String | Name of the regulatory compliance assessment object
apiInstance.regulatoryComplianceAssessmentsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, regulatoryComplianceAssessmentName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | 
 **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | 
 **regulatoryComplianceAssessmentName** | **String**| Name of the regulatory compliance assessment object | 

### Return type

[**RegulatoryComplianceAssessment**](RegulatoryComplianceAssessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulatoryComplianceAssessmentsList

> RegulatoryComplianceAssessmentList regulatoryComplianceAssessmentsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, opts)



Details and state of assessments mapped to selected regulatory compliance control

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
let regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.regulatoryComplianceAssessmentsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | 
 **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**RegulatoryComplianceAssessmentList**](RegulatoryComplianceAssessmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulatoryComplianceControlsGet

> RegulatoryComplianceControl regulatoryComplianceControlsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName)



Selected regulatory compliance control details and state

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
let regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
apiInstance.regulatoryComplianceControlsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | 
 **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | 

### Return type

[**RegulatoryComplianceControl**](RegulatoryComplianceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulatoryComplianceControlsList

> RegulatoryComplianceControlList regulatoryComplianceControlsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, opts)



All supported regulatory compliance controls details and state for selected standard

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.regulatoryComplianceControlsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**RegulatoryComplianceControlList**](RegulatoryComplianceControlList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulatoryComplianceStandardsGet

> RegulatoryComplianceStandard regulatoryComplianceStandardsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName)



Supported regulatory compliance details state for selected standard

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
apiInstance.regulatoryComplianceStandardsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | 

### Return type

[**RegulatoryComplianceStandard**](RegulatoryComplianceStandard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regulatoryComplianceStandardsList

> RegulatoryComplianceStandardList regulatoryComplianceStandardsList(apiVersion, subscriptionId, opts)



Supported regulatory compliance standards details and state

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.RegulatoryComplianceApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.regulatoryComplianceStandardsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**RegulatoryComplianceStandardList**](RegulatoryComplianceStandardList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

