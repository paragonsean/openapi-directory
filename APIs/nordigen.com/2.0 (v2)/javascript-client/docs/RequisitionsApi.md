# NordigenAccountInformationServicesApi.RequisitionsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRequisitionByIdV2**](RequisitionsApi.md#deleteRequisitionByIdV2) | **DELETE** /api/v2/requisitions/{id}/ | 
[**requisitionById**](RequisitionsApi.md#requisitionById) | **GET** /api/v2/requisitions/{id}/ | 
[**requisitionCreated**](RequisitionsApi.md#requisitionCreated) | **POST** /api/v2/requisitions/ | 
[**retrieveAllRequisitions**](RequisitionsApi.md#retrieveAllRequisitions) | **GET** /api/v2/requisitions/ | 



## deleteRequisitionByIdV2

> deleteRequisitionByIdV2(id)



Delete requisition and its end user agreement

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.RequisitionsApi();
let id = "id_example"; // String | A UUID string identifying this requisition.
apiInstance.deleteRequisitionByIdV2(id, (error, data, response) => {
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
 **id** | **String**| A UUID string identifying this requisition. | 

### Return type

null (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requisitionById

> Requisition requisitionById(id)



Retrieve a requisition by ID

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.RequisitionsApi();
let id = "id_example"; // String | A UUID string identifying this requisition.
apiInstance.requisitionById(id, (error, data, response) => {
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
 **id** | **String**| A UUID string identifying this requisition. | 

### Return type

[**Requisition**](Requisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requisitionCreated

> SpectacularRequisition requisitionCreated(requisitionRequest)



Create a new requisition

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.RequisitionsApi();
let requisitionRequest = new NordigenAccountInformationServicesApi.RequisitionRequest(); // RequisitionRequest | 
apiInstance.requisitionCreated(requisitionRequest, (error, data, response) => {
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
 **requisitionRequest** | [**RequisitionRequest**](RequisitionRequest.md)|  | 

### Return type

[**SpectacularRequisition**](SpectacularRequisition.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## retrieveAllRequisitions

> PaginatedRequisitionList retrieveAllRequisitions(opts)



Retrieve all requisitions belonging to the company

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.RequisitionsApi();
let opts = {
  'limit': 100, // Number | Number of results to return per page.
  'offset': 1 // Number | The initial index from which to return the results.
};
apiInstance.retrieveAllRequisitions(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] [default to 100]
 **offset** | **Number**| The initial index from which to return the results. | [optional] [default to 1]

### Return type

[**PaginatedRequisitionList**](PaginatedRequisitionList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

