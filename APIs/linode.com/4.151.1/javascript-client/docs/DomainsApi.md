# LinodeApi.DomainsApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloneDomain**](DomainsApi.md#cloneDomain) | **POST** /domains/{domainId}/clone | Domain Clone
[**createDomain**](DomainsApi.md#createDomain) | **POST** /domains | Domain Create
[**createDomainRecord**](DomainsApi.md#createDomainRecord) | **POST** /domains/{domainId}/records | Domain Record Create
[**deleteDomain**](DomainsApi.md#deleteDomain) | **DELETE** /domains/{domainId} | Domain Delete
[**deleteDomainRecord**](DomainsApi.md#deleteDomainRecord) | **DELETE** /domains/{domainId}/records/{recordId} | Domain Record Delete
[**getDomain**](DomainsApi.md#getDomain) | **GET** /domains/{domainId} | Domain View
[**getDomainRecord**](DomainsApi.md#getDomainRecord) | **GET** /domains/{domainId}/records/{recordId} | Domain Record View
[**getDomainRecords**](DomainsApi.md#getDomainRecords) | **GET** /domains/{domainId}/records | Domain Records List
[**getDomainZone**](DomainsApi.md#getDomainZone) | **GET** /domains/{domainId}/zone-file | Domain Zone File View
[**getDomains**](DomainsApi.md#getDomains) | **GET** /domains | Domains List
[**importDomain**](DomainsApi.md#importDomain) | **POST** /domains/import | Domain Import
[**updateDomain**](DomainsApi.md#updateDomain) | **PUT** /domains/{domainId} | Domain Update
[**updateDomainRecord**](DomainsApi.md#updateDomainRecord) | **PUT** /domains/{domainId}/records/{recordId} | Domain Record Update



## cloneDomain

> Domain cloneDomain(domainId, cloneDomainRequest)

Domain Clone

Clones a Domain and all associated DNS records from a Domain that is registered in Linode&#39;s DNS manager. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = "domainId_example"; // String | ID of the Domain to clone.
let cloneDomainRequest = new LinodeApi.CloneDomainRequest(); // CloneDomainRequest | Information about the Domain to clone.
apiInstance.cloneDomain(domainId, cloneDomainRequest, (error, data, response) => {
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
 **domainId** | **String**| ID of the Domain to clone. | 
 **cloneDomainRequest** | [**CloneDomainRequest**](CloneDomainRequest.md)| Information about the Domain to clone. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomain

> Domain createDomain(domain)

Domain Create

Adds a new Domain to Linode&#39;s DNS Manager. Linode is not a registrar, and you must own the domain before adding it here. Be sure to point your registrar to Linode&#39;s nameservers so that the records hosted here are used. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domain = new LinodeApi.Domain(); // Domain | Information about the domain you are registering.
apiInstance.createDomain(domain, (error, data, response) => {
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
 **domain** | [**Domain**](Domain.md)| Information about the domain you are registering. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomainRecord

> DomainRecord createDomainRecord(domainId, domainRecord)

Domain Record Create

Adds a new Domain Record to the zonefile this Domain represents.  Each domain can have up to 12,000 active records. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain we are accessing Records for.
let domainRecord = new LinodeApi.DomainRecord(); // DomainRecord | Information about the new Record to add. 
apiInstance.createDomainRecord(domainId, domainRecord, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain we are accessing Records for. | 
 **domainRecord** | [**DomainRecord**](DomainRecord.md)| Information about the new Record to add.  | 

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDomain

> Object deleteDomain(domainId)

Domain Delete

Deletes a Domain from Linode&#39;s DNS Manager. The Domain will be removed from Linode&#39;s nameservers shortly after this operation completes. This also deletes all associated Domain Records. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain to access.
apiInstance.deleteDomain(domainId, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain to access. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDomainRecord

> Object deleteDomainRecord(domainId, recordId)

Domain Record Delete

Deletes a Record on this Domain. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain whose Record you are accessing.
let recordId = 56; // Number | The ID of the Record you are accessing.
apiInstance.deleteDomainRecord(domainId, recordId, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain whose Record you are accessing. | 
 **recordId** | **Number**| The ID of the Record you are accessing. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomain

> Domain getDomain(domainId)

Domain View

This is a single Domain that you have registered in Linode&#39;s DNS Manager. Linode is not a registrar, and in order for this Domain record to work you must own the domain and point your registrar at Linode&#39;s nameservers. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain to access.
apiInstance.getDomain(domainId, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain to access. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainRecord

> DomainRecord getDomainRecord(domainId, recordId)

Domain Record View

View a single Record on this Domain. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain whose Record you are accessing.
let recordId = 56; // Number | The ID of the Record you are accessing.
apiInstance.getDomainRecord(domainId, recordId, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain whose Record you are accessing. | 
 **recordId** | **Number**| The ID of the Record you are accessing. | 

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainRecords

> GetDomainRecords200Response getDomainRecords(domainId, opts)

Domain Records List

Returns a paginated list of Records configured on a Domain in Linode&#39;s DNS Manager. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain we are accessing Records for.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDomainRecords(domainId, opts, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain we are accessing Records for. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDomainRecords200Response**](GetDomainRecords200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainZone

> GetDomainZone200Response getDomainZone(domainId)

Domain Zone File View

Returns the zone file for the last rendered zone for the specified domain. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = "domainId_example"; // String | ID of the Domain.
apiInstance.getDomainZone(domainId, (error, data, response) => {
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
 **domainId** | **String**| ID of the Domain. | 

### Return type

[**GetDomainZone200Response**](GetDomainZone200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomains

> GetDomains200Response getDomains(opts)

Domains List

This is a collection of Domains that you have registered in Linode&#39;s DNS Manager.  Linode is not a registrar, and in order for these to work you must own the domains and point your registrar at Linode&#39;s nameservers. 

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

let apiInstance = new LinodeApi.DomainsApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDomains(opts, (error, data, response) => {
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

[**GetDomains200Response**](GetDomains200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importDomain

> Domain importDomain(opts)

Domain Import

Imports a domain zone from a remote nameserver. Your nameserver must allow zone transfers (AXFR) from the following IPs:    - 96.126.114.97   - 96.126.114.98   - 2600:3c00::5e   - 2600:3c00::5f 

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

let apiInstance = new LinodeApi.DomainsApi();
let opts = {
  'importDomainRequest': new LinodeApi.ImportDomainRequest() // ImportDomainRequest | Information about the Domain to import.
};
apiInstance.importDomain(opts, (error, data, response) => {
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
 **importDomainRequest** | [**ImportDomainRequest**](ImportDomainRequest.md)| Information about the Domain to import. | [optional] 

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomain

> Domain updateDomain(domainId, domain)

Domain Update

Update information about a Domain in Linode&#39;s DNS Manager. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain to access.
let domain = new LinodeApi.Domain(); // Domain | The Domain information to update.
apiInstance.updateDomain(domainId, domain, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain to access. | 
 **domain** | [**Domain**](Domain.md)| The Domain information to update. | 

### Return type

[**Domain**](Domain.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomainRecord

> DomainRecord updateDomainRecord(domainId, recordId, updateDomainRecordRequest)

Domain Record Update

Updates a single Record on this Domain. 

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

let apiInstance = new LinodeApi.DomainsApi();
let domainId = 56; // Number | The ID of the Domain whose Record you are accessing.
let recordId = 56; // Number | The ID of the Record you are accessing.
let updateDomainRecordRequest = new LinodeApi.UpdateDomainRecordRequest(); // UpdateDomainRecordRequest | The values to change.
apiInstance.updateDomainRecord(domainId, recordId, updateDomainRecordRequest, (error, data, response) => {
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
 **domainId** | **Number**| The ID of the Domain whose Record you are accessing. | 
 **recordId** | **Number**| The ID of the Record you are accessing. | 
 **updateDomainRecordRequest** | [**UpdateDomainRecordRequest**](UpdateDomainRecordRequest.md)| The values to change. | 

### Return type

[**DomainRecord**](DomainRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

