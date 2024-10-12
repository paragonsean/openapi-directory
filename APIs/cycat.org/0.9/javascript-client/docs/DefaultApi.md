# CyCatOrgApi.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChild**](DefaultApi.md#getChild) | **GET** /child/{uuid} | 
[**getGenerateUuid**](DefaultApi.md#getGenerateUuid) | **GET** /generate/uuid | 
[**getInfo**](DefaultApi.md#getInfo) | **GET** /info | 
[**getListProject**](DefaultApi.md#getListProject) | **GET** /list/project/{start}/{end} | 
[**getListPublisher**](DefaultApi.md#getListPublisher) | **GET** /list/publisher/{start}/{end} | 
[**getLookup**](DefaultApi.md#getLookup) | **GET** /lookup/{uuid} | 
[**getNamespacefinduuid**](DefaultApi.md#getNamespacefinduuid) | **GET** /namespace/finduuid/{namespace}/{namespaceid} | 
[**getNamespacegetall**](DefaultApi.md#getNamespacegetall) | **GET** /namespace/getall | 
[**getNamespacegetid**](DefaultApi.md#getNamespacegetid) | **GET** /namespace/getid/{namespace} | 
[**getParent**](DefaultApi.md#getParent) | **GET** /parent/{uuid} | 
[**getRelationships**](DefaultApi.md#getRelationships) | **GET** /relationships/{uuid} | 
[**getRelationshipsexpanded**](DefaultApi.md#getRelationshipsexpanded) | **GET** /relationships/expanded/{uuid} | 
[**getSearch**](DefaultApi.md#getSearch) | **GET** /search/{searchquery} | 
[**postPropose**](DefaultApi.md#postPropose) | **POST** /propose | 



## getChild

> getChild(uuid)



Get child UUID(s) from a specified project or publisher UUID.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let uuid = "uuid_example"; // String | 
apiInstance.getChild(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGenerateUuid

> getGenerateUuid()



Generate an UUID version 4 RFC4122-compliant.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
apiInstance.getGenerateUuid((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInfo

> getInfo()



Get information about the CyCAT backend services including status, overall statistics and version.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
apiInstance.getInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListProject

> getListProject(start, end)



List projects registered in CyCAT by pagination (start,end).

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let start = 56; // Number | 
let end = 56; // Number | 
apiInstance.getListProject(start, end, (error, data, response) => {
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
 **start** | **Number**|  | 
 **end** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getListPublisher

> getListPublisher(start, end)



List publishers registered in CyCAT by pagination (start,end).

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let start = 56; // Number | 
let end = 56; // Number | 
apiInstance.getListPublisher(start, end, (error, data, response) => {
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
 **start** | **Number**|  | 
 **end** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLookup

> getLookup(uuid)



Lookup UUID registered in CyCAT.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let uuid = "uuid_example"; // String | 
apiInstance.getLookup(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNamespacefinduuid

> getNamespacefinduuid(namespace, namespaceid)



Get all known UUID for a given namespace id.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let namespace = "namespace_example"; // String | 
let namespaceid = "namespaceid_example"; // String | 
apiInstance.getNamespacefinduuid(namespace, namespaceid, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **namespaceid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNamespacegetall

> getNamespacegetall()



List all known namespaces.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
apiInstance.getNamespacegetall((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNamespacegetid

> getNamespacegetid(namespace)



Get all ID from a given namespace.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let namespace = "namespace_example"; // String | 
apiInstance.getNamespacegetid(namespace, (error, data, response) => {
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
 **namespace** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getParent

> getParent(uuid)



Get parent UUID(s) from a specified project or item UUID.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let uuid = "uuid_example"; // String | 
apiInstance.getParent(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRelationships

> getRelationships(uuid)



Get relationship(s) UUID from a specified UUID.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let uuid = "uuid_example"; // String | 
apiInstance.getRelationships(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRelationshipsexpanded

> getRelationshipsexpanded(uuid)



Get relationship(s) UUID from a specified UUID including the relationships meta information.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let uuid = "uuid_example"; // String | 
apiInstance.getRelationshipsexpanded(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSearch

> getSearch(searchquery)



Full-text search in CyCAT and return matching UUID.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
let searchquery = "searchquery_example"; // String | 
apiInstance.getSearch(searchquery, (error, data, response) => {
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
 **searchquery** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postPropose

> postPropose()



Propose new resource to CyCAT.

### Example

```javascript
import CyCatOrgApi from 'cy_cat_org_api';

let apiInstance = new CyCatOrgApi.DefaultApi();
apiInstance.postPropose((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

