# SecurityCenter.AssessmentsMetadataApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assessmentsMetadataGet**](AssessmentsMetadataApi.md#assessmentsMetadataGet) | **GET** /providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} | 
[**assessmentsMetadataList**](AssessmentsMetadataApi.md#assessmentsMetadataList) | **GET** /providers/Microsoft.Security/assessmentMetadata | 
[**assessmentsMetadataSubscriptionCreate**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} | 
[**assessmentsMetadataSubscriptionDelete**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} | 
[**assessmentsMetadataSubscriptionGet**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName} | 
[**assessmentsMetadataSubscriptionList**](AssessmentsMetadataApi.md#assessmentsMetadataSubscriptionList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata | 



## assessmentsMetadataGet

> SecurityAssessmentMetadata assessmentsMetadataGet(apiVersion, assessmentMetadataName)



Get metadata information on an assessment type

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
apiInstance.assessmentsMetadataGet(apiVersion, assessmentMetadataName, (error, data, response) => {
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
 **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | 

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsMetadataList

> SecurityAssessmentMetadataList assessmentsMetadataList(apiVersion)



Get metadata information on all assessment types

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.assessmentsMetadataList(apiVersion, (error, data, response) => {
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

### Return type

[**SecurityAssessmentMetadataList**](SecurityAssessmentMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsMetadataSubscriptionCreate

> SecurityAssessmentMetadata assessmentsMetadataSubscriptionCreate(apiVersion, assessmentMetadataName, subscriptionId, assessmentMetadata)



Create metadata information on an assessment type in a specific subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let assessmentMetadata = new SecurityCenter.SecurityAssessmentMetadata(); // SecurityAssessmentMetadata | AssessmentMetadata object
apiInstance.assessmentsMetadataSubscriptionCreate(apiVersion, assessmentMetadataName, subscriptionId, assessmentMetadata, (error, data, response) => {
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
 **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **assessmentMetadata** | [**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)| AssessmentMetadata object | 

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## assessmentsMetadataSubscriptionDelete

> assessmentsMetadataSubscriptionDelete(apiVersion, assessmentMetadataName, subscriptionId)



Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.assessmentsMetadataSubscriptionDelete(apiVersion, assessmentMetadataName, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | 
 **subscriptionId** | **String**| Azure subscription ID | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsMetadataSubscriptionGet

> SecurityAssessmentMetadata assessmentsMetadataSubscriptionGet(apiVersion, assessmentMetadataName, subscriptionId)



Get metadata information on an assessment type in a specific subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let assessmentMetadataName = "assessmentMetadataName_example"; // String | The Assessment Key - Unique key for the assessment type
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.assessmentsMetadataSubscriptionGet(apiVersion, assessmentMetadataName, subscriptionId, (error, data, response) => {
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
 **assessmentMetadataName** | **String**| The Assessment Key - Unique key for the assessment type | 
 **subscriptionId** | **String**| Azure subscription ID | 

### Return type

[**SecurityAssessmentMetadata**](SecurityAssessmentMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assessmentsMetadataSubscriptionList

> SecurityAssessmentMetadataList assessmentsMetadataSubscriptionList(apiVersion, subscriptionId)



Get metadata information on all assessment types in a specific subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AssessmentsMetadataApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
apiInstance.assessmentsMetadataSubscriptionList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**SecurityAssessmentMetadataList**](SecurityAssessmentMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

