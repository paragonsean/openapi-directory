# ManagedLabsClient.GlobalUsersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalUsersGetEnvironment**](GlobalUsersApi.md#globalUsersGetEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/getEnvironment | 
[**globalUsersGetOperationBatchStatus**](GlobalUsersApi.md#globalUsersGetOperationBatchStatus) | **POST** /providers/Microsoft.LabServices/users/{userName}/getOperationBatchStatus | 
[**globalUsersGetOperationStatus**](GlobalUsersApi.md#globalUsersGetOperationStatus) | **POST** /providers/Microsoft.LabServices/users/{userName}/getOperationStatus | 
[**globalUsersGetPersonalPreferences**](GlobalUsersApi.md#globalUsersGetPersonalPreferences) | **POST** /providers/Microsoft.LabServices/users/{userName}/getPersonalPreferences | 
[**globalUsersListEnvironments**](GlobalUsersApi.md#globalUsersListEnvironments) | **POST** /providers/Microsoft.LabServices/users/{userName}/listEnvironments | 
[**globalUsersListLabs**](GlobalUsersApi.md#globalUsersListLabs) | **POST** /providers/Microsoft.LabServices/users/{userName}/listLabs | 
[**globalUsersRegister**](GlobalUsersApi.md#globalUsersRegister) | **POST** /providers/Microsoft.LabServices/users/{userName}/register | 
[**globalUsersResetPassword**](GlobalUsersApi.md#globalUsersResetPassword) | **POST** /providers/Microsoft.LabServices/users/{userName}/resetPassword | 
[**globalUsersStartEnvironment**](GlobalUsersApi.md#globalUsersStartEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/startEnvironment | 
[**globalUsersStopEnvironment**](GlobalUsersApi.md#globalUsersStopEnvironment) | **POST** /providers/Microsoft.LabServices/users/{userName}/stopEnvironment | 



## globalUsersGetEnvironment

> GetEnvironmentResponse globalUsersGetEnvironment(userName, apiVersion, environmentOperationsPayload, opts)



Gets the virtual machine details

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environmentOperationsPayload = new ManagedLabsClient.EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($expand=environment)'
};
apiInstance.globalUsersGetEnvironment(userName, apiVersion, environmentOperationsPayload, opts, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | 
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;environment)&#39; | [optional] 

### Return type

[**GetEnvironmentResponse**](GetEnvironmentResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersGetOperationBatchStatus

> OperationBatchStatusResponse globalUsersGetOperationBatchStatus(userName, apiVersion, operationBatchStatusPayload)



Get batch operation status

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let operationBatchStatusPayload = new ManagedLabsClient.OperationBatchStatusPayload(); // OperationBatchStatusPayload | Payload to get the status of an operation
apiInstance.globalUsersGetOperationBatchStatus(userName, apiVersion, operationBatchStatusPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **operationBatchStatusPayload** | [**OperationBatchStatusPayload**](OperationBatchStatusPayload.md)| Payload to get the status of an operation | 

### Return type

[**OperationBatchStatusResponse**](OperationBatchStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersGetOperationStatus

> OperationStatusResponse globalUsersGetOperationStatus(userName, apiVersion, operationStatusPayload)



Gets the status of long running operation

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let operationStatusPayload = new ManagedLabsClient.OperationStatusPayload(); // OperationStatusPayload | Payload to get the status of an operation
apiInstance.globalUsersGetOperationStatus(userName, apiVersion, operationStatusPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **operationStatusPayload** | [**OperationStatusPayload**](OperationStatusPayload.md)| Payload to get the status of an operation | 

### Return type

[**OperationStatusResponse**](OperationStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersGetPersonalPreferences

> GetPersonalPreferencesResponse globalUsersGetPersonalPreferences(userName, apiVersion, personalPreferencesOperationsPayload)



Get personal preferences for a user

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let personalPreferencesOperationsPayload = new ManagedLabsClient.PersonalPreferencesOperationsPayload(); // PersonalPreferencesOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
apiInstance.globalUsersGetPersonalPreferences(userName, apiVersion, personalPreferencesOperationsPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **personalPreferencesOperationsPayload** | [**PersonalPreferencesOperationsPayload**](PersonalPreferencesOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | 

### Return type

[**GetPersonalPreferencesResponse**](GetPersonalPreferencesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersListEnvironments

> ListEnvironmentsResponse globalUsersListEnvironments(userName, apiVersion, listEnvironmentsPayload)



List Environments for the user

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let listEnvironmentsPayload = new ManagedLabsClient.ListEnvironmentsPayload(); // ListEnvironmentsPayload | Represents the payload to list environments owned by a user
apiInstance.globalUsersListEnvironments(userName, apiVersion, listEnvironmentsPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **listEnvironmentsPayload** | [**ListEnvironmentsPayload**](ListEnvironmentsPayload.md)| Represents the payload to list environments owned by a user | 

### Return type

[**ListEnvironmentsResponse**](ListEnvironmentsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersListLabs

> ListLabsResponse globalUsersListLabs(userName, apiVersion)



List labs for the user.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.globalUsersListLabs(userName, apiVersion, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

[**ListLabsResponse**](ListLabsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## globalUsersRegister

> globalUsersRegister(userName, apiVersion, registerPayload)



Register a user to a managed lab

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let registerPayload = new ManagedLabsClient.RegisterPayload(); // RegisterPayload | Represents payload for Register action.
apiInstance.globalUsersRegister(userName, apiVersion, registerPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **registerPayload** | [**RegisterPayload**](RegisterPayload.md)| Represents payload for Register action. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersResetPassword

> globalUsersResetPassword(userName, apiVersion, resetPasswordPayload)



Resets the user password on an environment This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let resetPasswordPayload = new ManagedLabsClient.ResetPasswordPayload(); // ResetPasswordPayload | Represents the payload for resetting passwords.
apiInstance.globalUsersResetPassword(userName, apiVersion, resetPasswordPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **resetPasswordPayload** | [**ResetPasswordPayload**](ResetPasswordPayload.md)| Represents the payload for resetting passwords. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersStartEnvironment

> globalUsersStartEnvironment(userName, apiVersion, environmentOperationsPayload)



Starts an environment by starting all resources inside the environment. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environmentOperationsPayload = new ManagedLabsClient.EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
apiInstance.globalUsersStartEnvironment(userName, apiVersion, environmentOperationsPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## globalUsersStopEnvironment

> globalUsersStopEnvironment(userName, apiVersion, environmentOperationsPayload)



Stops an environment by stopping all resources inside the environment This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.GlobalUsersApi();
let userName = "userName_example"; // String | The name of the user.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environmentOperationsPayload = new ManagedLabsClient.EnvironmentOperationsPayload(); // EnvironmentOperationsPayload | Represents payload for any Environment operations like get, start, stop, connect
apiInstance.globalUsersStopEnvironment(userName, apiVersion, environmentOperationsPayload, (error, data, response) => {
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
 **userName** | **String**| The name of the user. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **environmentOperationsPayload** | [**EnvironmentOperationsPayload**](EnvironmentOperationsPayload.md)| Represents payload for any Environment operations like get, start, stop, connect | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

