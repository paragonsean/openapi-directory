# BillingManagementClient.RecipientTransfersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipientTransfersAccept**](RecipientTransfersApi.md#recipientTransfersAccept) | **POST** /providers/Microsoft.Billing/transfers/{transferName}/acceptTransfer | Accepts the transfer with given transfer Id.
[**recipientTransfersDecline**](RecipientTransfersApi.md#recipientTransfersDecline) | **POST** /providers/Microsoft.Billing/transfers/{transferName}/declineTransfer | Declines the transfer with given transfer Id.
[**recipientTransfersGet**](RecipientTransfersApi.md#recipientTransfersGet) | **GET** /providers/Microsoft.Billing/transfers/{transferName} | Gets the transfer with given transfer Id.
[**recipientTransfersList**](RecipientTransfersApi.md#recipientTransfersList) | **GET** /providers/Microsoft.Billing/transfers | Lists the transfers received by caller.
[**recipientTransfersValidate**](RecipientTransfersApi.md#recipientTransfersValidate) | **POST** /providers/Microsoft.Billing/transfers/{transferName}/validateTransfer | Validates if the products can be transferred in the context of the given transfer name.



## recipientTransfersAccept

> RecipientTransferDetails recipientTransfersAccept(transferName, parameters)

Accepts the transfer with given transfer Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.RecipientTransfersApi();
let transferName = "transferName_example"; // String | Transfer Name.
let parameters = new BillingManagementClient.AcceptTransferRequest(); // AcceptTransferRequest | Parameters supplied to accept the transfer.
apiInstance.recipientTransfersAccept(transferName, parameters, (error, data, response) => {
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
 **transferName** | **String**| Transfer Name. | 
 **parameters** | [**AcceptTransferRequest**](AcceptTransferRequest.md)| Parameters supplied to accept the transfer. | 

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recipientTransfersDecline

> RecipientTransferDetails recipientTransfersDecline(transferName)

Declines the transfer with given transfer Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.RecipientTransfersApi();
let transferName = "transferName_example"; // String | Transfer Name.
apiInstance.recipientTransfersDecline(transferName, (error, data, response) => {
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
 **transferName** | **String**| Transfer Name. | 

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recipientTransfersGet

> RecipientTransferDetails recipientTransfersGet(transferName)

Gets the transfer with given transfer Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.RecipientTransfersApi();
let transferName = "transferName_example"; // String | Transfer Name.
apiInstance.recipientTransfersGet(transferName, (error, data, response) => {
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
 **transferName** | **String**| Transfer Name. | 

### Return type

[**RecipientTransferDetails**](RecipientTransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recipientTransfersList

> RecipientTransferDetailsListResult recipientTransfersList()

Lists the transfers received by caller.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.RecipientTransfersApi();
apiInstance.recipientTransfersList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**RecipientTransferDetailsListResult**](RecipientTransferDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recipientTransfersValidate

> ValidateTransferListResponse recipientTransfersValidate(transferName, parameters)

Validates if the products can be transferred in the context of the given transfer name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.RecipientTransfersApi();
let transferName = "transferName_example"; // String | Transfer Name.
let parameters = new BillingManagementClient.AcceptTransferRequest(); // AcceptTransferRequest | Parameters supplied to validate the transfer.
apiInstance.recipientTransfersValidate(transferName, parameters, (error, data, response) => {
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
 **transferName** | **String**| Transfer Name. | 
 **parameters** | [**AcceptTransferRequest**](AcceptTransferRequest.md)| Parameters supplied to validate the transfer. | 

### Return type

[**ValidateTransferListResponse**](ValidateTransferListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

