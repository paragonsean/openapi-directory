# LinodeApi.ManagedApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createManagedContact**](ManagedApi.md#createManagedContact) | **POST** /managed/contacts | Managed Contact Create
[**createManagedCredential**](ManagedApi.md#createManagedCredential) | **POST** /managed/credentials | Managed Credential Create
[**createManagedService**](ManagedApi.md#createManagedService) | **POST** /managed/services | Managed Service Create
[**deleteManagedContact**](ManagedApi.md#deleteManagedContact) | **DELETE** /managed/contacts/{contactId} | Managed Contact Delete
[**deleteManagedCredential**](ManagedApi.md#deleteManagedCredential) | **POST** /managed/credentials/{credentialId}/revoke | Managed Credential Delete
[**deleteManagedService**](ManagedApi.md#deleteManagedService) | **DELETE** /managed/services/{serviceId} | Managed Service Delete
[**disableManagedService**](ManagedApi.md#disableManagedService) | **POST** /managed/services/{serviceId}/disable | Managed Service Disable
[**enableManagedService**](ManagedApi.md#enableManagedService) | **POST** /managed/services/{serviceId}/enable | Managed Service Enable
[**getManagedContact**](ManagedApi.md#getManagedContact) | **GET** /managed/contacts/{contactId} | Managed Contact View
[**getManagedContacts**](ManagedApi.md#getManagedContacts) | **GET** /managed/contacts | Managed Contacts List
[**getManagedCredential**](ManagedApi.md#getManagedCredential) | **GET** /managed/credentials/{credentialId} | Managed Credential View
[**getManagedCredentials**](ManagedApi.md#getManagedCredentials) | **GET** /managed/credentials | Managed Credentials List
[**getManagedIssue**](ManagedApi.md#getManagedIssue) | **GET** /managed/issues/{issueId} | Managed Issue View
[**getManagedIssues**](ManagedApi.md#getManagedIssues) | **GET** /managed/issues | Managed Issues List
[**getManagedLinodeSetting**](ManagedApi.md#getManagedLinodeSetting) | **GET** /managed/linode-settings/{linodeId} | Linode&#39;s Managed Settings View
[**getManagedLinodeSettings**](ManagedApi.md#getManagedLinodeSettings) | **GET** /managed/linode-settings | Managed Linode Settings List
[**getManagedService**](ManagedApi.md#getManagedService) | **GET** /managed/services/{serviceId} | Managed Service View
[**getManagedServices**](ManagedApi.md#getManagedServices) | **GET** /managed/services | Managed Services List
[**getManagedStats**](ManagedApi.md#getManagedStats) | **GET** /managed/stats | Managed Stats List
[**updateManagedContact**](ManagedApi.md#updateManagedContact) | **PUT** /managed/contacts/{contactId} | Managed Contact Update
[**updateManagedCredential**](ManagedApi.md#updateManagedCredential) | **PUT** /managed/credentials/{credentialId} | Managed Credential Update
[**updateManagedCredentialUsernamePassword**](ManagedApi.md#updateManagedCredentialUsernamePassword) | **POST** /managed/credentials/{credentialId}/update | Managed Credential Username and Password Update
[**updateManagedLinodeSetting**](ManagedApi.md#updateManagedLinodeSetting) | **PUT** /managed/linode-settings/{linodeId} | Linode&#39;s Managed Settings Update
[**updateManagedService**](ManagedApi.md#updateManagedService) | **PUT** /managed/services/{serviceId} | Managed Service Update
[**viewManagedSSHKey**](ManagedApi.md#viewManagedSSHKey) | **GET** /managed/credentials/sshkey | Managed SSH Key View



## createManagedContact

> ManagedContact createManagedContact(opts)

Managed Contact Create

Creates a Managed Contact.  A Managed Contact is someone Linode special forces can contact in the course of attempting to resolve an issue with a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'managedContact': new LinodeApi.ManagedContact() // ManagedContact | Information about the contact to create.
};
apiInstance.createManagedContact(opts, (error, data, response) => {
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
 **managedContact** | [**ManagedContact**](ManagedContact.md)| Information about the contact to create. | [optional] 

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createManagedCredential

> ManagedCredential createManagedCredential(opts)

Managed Credential Create

Creates a Managed Credential. A Managed Credential is stored securely to allow Linode special forces to access your Managed Services and resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'createManagedCredentialRequest': new LinodeApi.CreateManagedCredentialRequest() // CreateManagedCredentialRequest | Information about the Credential to create.
};
apiInstance.createManagedCredential(opts, (error, data, response) => {
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
 **createManagedCredentialRequest** | [**CreateManagedCredentialRequest**](CreateManagedCredentialRequest.md)| Information about the Credential to create. | [optional] 

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createManagedService

> ManagedService createManagedService(opts)

Managed Service Create

Creates a Managed Service. Linode Managed will begin monitoring this service and reporting and attempting to resolve any Issues.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'managedService': new LinodeApi.ManagedService() // ManagedService | Information about the service to monitor.
};
apiInstance.createManagedService(opts, (error, data, response) => {
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
 **managedService** | [**ManagedService**](ManagedService.md)| Information about the service to monitor. | [optional] 

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteManagedContact

> Object deleteManagedContact(contactId)

Managed Contact Delete

Deletes a Managed Contact.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let contactId = 56; // Number | The ID of the contact to access.
apiInstance.deleteManagedContact(contactId, (error, data, response) => {
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
 **contactId** | **Number**| The ID of the contact to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteManagedCredential

> Object deleteManagedCredential(credentialId)

Managed Credential Delete

Deletes a Managed Credential.  Linode special forces will no longer have access to this Credential when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let credentialId = 56; // Number | The ID of the Credential to access.
apiInstance.deleteManagedCredential(credentialId, (error, data, response) => {
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
 **credentialId** | **Number**| The ID of the Credential to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteManagedService

> Object deleteManagedService(serviceId)

Managed Service Delete

Deletes a Managed Service.  This service will no longer be monitored by Linode Managed.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let serviceId = 56; // Number | The ID of the Managed Service to access.
apiInstance.deleteManagedService(serviceId, (error, data, response) => {
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
 **serviceId** | **Number**| The ID of the Managed Service to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableManagedService

> ManagedService disableManagedService(serviceId)

Managed Service Disable

Temporarily disables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let serviceId = 56; // Number | The ID of the Managed Service to disable.
apiInstance.disableManagedService(serviceId, (error, data, response) => {
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
 **serviceId** | **Number**| The ID of the Managed Service to disable. | 

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableManagedService

> ManagedService enableManagedService(serviceId)

Managed Service Enable

Enables monitoring of a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let serviceId = 56; // Number | The ID of the Managed Service to enable.
apiInstance.enableManagedService(serviceId, (error, data, response) => {
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
 **serviceId** | **Number**| The ID of the Managed Service to enable. | 

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedContact

> ManagedContact getManagedContact(contactId)

Managed Contact View

Returns a single Managed Contact.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let contactId = 56; // Number | The ID of the contact to access.
apiInstance.getManagedContact(contactId, (error, data, response) => {
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
 **contactId** | **Number**| The ID of the contact to access. | 

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedContacts

> GetManagedContacts200Response getManagedContacts(opts)

Managed Contacts List

Returns a paginated list of Managed Contacts on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getManagedContacts(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedContacts200Response**](GetManagedContacts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedCredential

> ManagedCredential getManagedCredential(credentialId)

Managed Credential View

Returns a single Managed Credential.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let credentialId = 56; // Number | The ID of the Credential to access.
apiInstance.getManagedCredential(credentialId, (error, data, response) => {
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
 **credentialId** | **Number**| The ID of the Credential to access. | 

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedCredentials

> GetManagedCredentials200Response getManagedCredentials(opts)

Managed Credentials List

Returns a paginated list of Managed Credentials on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getManagedCredentials(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedCredentials200Response**](GetManagedCredentials200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedIssue

> ManagedIssue getManagedIssue(issueId)

Managed Issue View

Returns a single Issue that is impacting or did impact one of your Managed Services.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let issueId = 56; // Number | The Issue to look up.
apiInstance.getManagedIssue(issueId, (error, data, response) => {
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
 **issueId** | **Number**| The Issue to look up. | 

### Return type

[**ManagedIssue**](ManagedIssue.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedIssues

> GetManagedIssues200Response getManagedIssues(opts)

Managed Issues List

Returns a paginated list of recent and ongoing issues detected on your Managed Services.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getManagedIssues(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedIssues200Response**](GetManagedIssues200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedLinodeSetting

> ManagedLinodeSettings getManagedLinodeSetting(linodeId)

Linode&#39;s Managed Settings View

Returns a single Linode&#39;s Managed settings.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let linodeId = 56; // Number | The Linode ID whose settings we are accessing.
apiInstance.getManagedLinodeSetting(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| The Linode ID whose settings we are accessing. | 

### Return type

[**ManagedLinodeSettings**](ManagedLinodeSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedLinodeSettings

> GetManagedLinodeSettings200Response getManagedLinodeSettings(opts)

Managed Linode Settings List

Returns a paginated list of Managed Settings for your Linodes. There will be one entry per Linode on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getManagedLinodeSettings(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetManagedLinodeSettings200Response**](GetManagedLinodeSettings200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedService

> ManagedService getManagedService(serviceId)

Managed Service View

Returns information about a single Managed Service on your Account.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let serviceId = 56; // Number | The ID of the Managed Service to access.
apiInstance.getManagedService(serviceId, (error, data, response) => {
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
 **serviceId** | **Number**| The ID of the Managed Service to access. | 

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedServices

> GetManagedServices200Response getManagedServices()

Managed Services List

Returns a paginated list of Managed Services on your Account. These are the services Linode Managed is monitoring and will report and attempt to resolve issues with.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
apiInstance.getManagedServices((error, data, response) => {
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

[**GetManagedServices200Response**](GetManagedServices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedStats

> GetManagedStats200Response getManagedStats()

Managed Stats List

Returns a list of Managed Stats on your Account in the form of x and y data points. You can use these data points to plot your own graph visualizations. These stats reflect the last 24 hours of combined usage across all managed Linodes on your account giving you a high-level snapshot of data for the following:   * cpu * disk * swap * network in * network out  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
apiInstance.getManagedStats((error, data, response) => {
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

[**GetManagedStats200Response**](GetManagedStats200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateManagedContact

> ManagedContact updateManagedContact(contactId, managedContact)

Managed Contact Update

Updates information about a Managed Contact. This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let contactId = 56; // Number | The ID of the contact to access.
let managedContact = new LinodeApi.ManagedContact(); // ManagedContact | The fields to update.
apiInstance.updateManagedContact(contactId, managedContact, (error, data, response) => {
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
 **contactId** | **Number**| The ID of the contact to access. | 
 **managedContact** | [**ManagedContact**](ManagedContact.md)| The fields to update. | 

### Return type

[**ManagedContact**](ManagedContact.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManagedCredential

> ManagedCredential updateManagedCredential(credentialId, managedCredential)

Managed Credential Update

Updates the label of a Managed Credential. This endpoint does not update the username and password for a Managed Credential. To do this, use the Managed Credential Username and Password Update ([POST /managed/credentials/{credentialId}/update](/docs/api/managed/#managed-credential-username-and-password-update)) endpoint instead. This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let credentialId = 56; // Number | The ID of the Credential to access.
let managedCredential = new LinodeApi.ManagedCredential(); // ManagedCredential | The fields to update.
apiInstance.updateManagedCredential(credentialId, managedCredential, (error, data, response) => {
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
 **credentialId** | **Number**| The ID of the Credential to access. | 
 **managedCredential** | [**ManagedCredential**](ManagedCredential.md)| The fields to update. | 

### Return type

[**ManagedCredential**](ManagedCredential.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManagedCredentialUsernamePassword

> Object updateManagedCredentialUsernamePassword(credentialId, opts)

Managed Credential Username and Password Update

Updates the username and password for a Managed Credential.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let credentialId = 56; // Number | The ID of the Credential to update.
let opts = {
  'updateManagedCredentialUsernamePasswordRequest': new LinodeApi.UpdateManagedCredentialUsernamePasswordRequest() // UpdateManagedCredentialUsernamePasswordRequest | The new username and password to assign to the Managed Credential. 
};
apiInstance.updateManagedCredentialUsernamePassword(credentialId, opts, (error, data, response) => {
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
 **credentialId** | **Number**| The ID of the Credential to update. | 
 **updateManagedCredentialUsernamePasswordRequest** | [**UpdateManagedCredentialUsernamePasswordRequest**](UpdateManagedCredentialUsernamePasswordRequest.md)| The new username and password to assign to the Managed Credential.  | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManagedLinodeSetting

> ManagedLinodeSettings updateManagedLinodeSetting(linodeId, managedLinodeSettings)

Linode&#39;s Managed Settings Update

Updates a single Linode&#39;s Managed settings. This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let linodeId = 56; // Number | The Linode ID whose settings we are accessing.
let managedLinodeSettings = new LinodeApi.ManagedLinodeSettings(); // ManagedLinodeSettings | The settings to update.
apiInstance.updateManagedLinodeSetting(linodeId, managedLinodeSettings, (error, data, response) => {
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
 **linodeId** | **Number**| The Linode ID whose settings we are accessing. | 
 **managedLinodeSettings** | [**ManagedLinodeSettings**](ManagedLinodeSettings.md)| The settings to update. | 

### Return type

[**ManagedLinodeSettings**](ManagedLinodeSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateManagedService

> ManagedService updateManagedService(serviceId, managedService)

Managed Service Update

Updates information about a Managed Service.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
let serviceId = 56; // Number | The ID of the Managed Service to access.
let managedService = new LinodeApi.ManagedService(); // ManagedService | The fields to update.
apiInstance.updateManagedService(serviceId, managedService, (error, data, response) => {
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
 **serviceId** | **Number**| The ID of the Managed Service to access. | 
 **managedService** | [**ManagedService**](ManagedService.md)| The fields to update. | 

### Return type

[**ManagedService**](ManagedService.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## viewManagedSSHKey

> ViewManagedSSHKey200Response viewManagedSSHKey()

Managed SSH Key View

Returns the unique SSH public key assigned to your Linode account&#39;s Managed service. If you [add this public key](/docs/guides/linode-managed/#adding-the-public-key) to a Linode on your account, Linode special forces will be able to log in to the Linode with this key when attempting to resolve issues.  This command can only be accessed by the unrestricted users of an account. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.ManagedApi();
apiInstance.viewManagedSSHKey((error, data, response) => {
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

[**ViewManagedSSHKey200Response**](ViewManagedSSHKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

