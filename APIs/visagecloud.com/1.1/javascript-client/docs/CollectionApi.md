# VisageCloud.CollectionApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCollection2UsingPOST**](CollectionApi.md#addCollection2UsingPOST) | **POST** /rest/v1.1/collection/collection | Create new empty collection with given name
[**addCollectionUsingPOST**](CollectionApi.md#addCollectionUsingPOST) | **POST** /rest/v1.1/collection/ | Create new empty collection with given name
[**deleteCollection2UsingDELETE**](CollectionApi.md#deleteCollection2UsingDELETE) | **DELETE** /rest/v1.1/collection/collection | Delete existing collection with associated profiles and faces.
[**deleteCollectionUsingDELETE**](CollectionApi.md#deleteCollectionUsingDELETE) | **DELETE** /rest/v1.1/collection/{id} | Delete existing collection with associated profiles and faces.
[**exportCSVUsingGET**](CollectionApi.md#exportCSVUsingGET) | **GET** /rest/v1.1/collection/export/csv | Retrieve collection content for data analysis.
[**getAllCollectionProfilesUsingGET**](CollectionApi.md#getAllCollectionProfilesUsingGET) | **GET** /rest/v1.1/collection/{id}/profile | Gets all the profiles associated to a collection
[**getAllCollections2UsingGET**](CollectionApi.md#getAllCollections2UsingGET) | **GET** /rest/v1.1/collection/all | Retrieve all collections
[**getAllCollectionsUsingGET**](CollectionApi.md#getAllCollectionsUsingGET) | **GET** /rest/v1.1/collection/ | Retrieve all collections
[**getCollection2UsingGET**](CollectionApi.md#getCollection2UsingGET) | **GET** /rest/v1.1/collection/collection | Retrieve existing collection content
[**getCollectionUsingGET**](CollectionApi.md#getCollectionUsingGET) | **GET** /rest/v1.1/collection/{id} | Retrieve existing collection content
[**repurposeCollectionUsingPUT**](CollectionApi.md#repurposeCollectionUsingPUT) | **PUT** /rest/v1.1/collection/purpose | Change purpose of existing collection
[**updateCollection2UsingPOST**](CollectionApi.md#updateCollection2UsingPOST) | **POST** /rest/v1.1/collection/{id} | Update an existing collection with a given id
[**updateCollectionUsingPATCH**](CollectionApi.md#updateCollectionUsingPATCH) | **PATCH** /rest/v1.1/collection/{id} | Update an existing collection with a given id



## addCollection2UsingPOST

> RestResponse addCollection2UsingPOST(accessKey, secretKey, collectionName, opts)

Create new empty collection with given name

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let collectionName = "collectionName_example"; // String | The name of the collection that will be created
let opts = {
  'preload': false, // Boolean | Defined whether to preload collection
  'evictable': true, // Boolean | Defined whether the collection can be evicted
  'purposes': ["null"] // [String] | The newly declared purposes of the collection
};
apiInstance.addCollection2UsingPOST(accessKey, secretKey, collectionName, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionName** | **String**| The name of the collection that will be created | 
 **preload** | **Boolean**| Defined whether to preload collection | [optional] [default to false]
 **evictable** | **Boolean**| Defined whether the collection can be evicted | [optional] [default to true]
 **purposes** | [**[String]**](String.md)| The newly declared purposes of the collection | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addCollectionUsingPOST

> RestResponse addCollectionUsingPOST(accessKey, secretKey, name, opts)

Create new empty collection with given name

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let name = "name_example"; // String | The name of the collection that will be created
let opts = {
  'preload': false, // Boolean | Defined whether to preload collection
  'evictable': true, // Boolean | Defined whether the collection can be evicted
  'purposes': ["null"] // [String] | The newly declared purposes of the collection
};
apiInstance.addCollectionUsingPOST(accessKey, secretKey, name, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **name** | **String**| The name of the collection that will be created | 
 **preload** | **Boolean**| Defined whether to preload collection | [optional] [default to false]
 **evictable** | **Boolean**| Defined whether the collection can be evicted | [optional] [default to true]
 **purposes** | [**[String]**](String.md)| The newly declared purposes of the collection | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCollection2UsingDELETE

> RestResponse deleteCollection2UsingDELETE(accessKey, secretKey, collectionId)

Delete existing collection with associated profiles and faces.

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | The id of the collection that will be removed
apiInstance.deleteCollection2UsingDELETE(accessKey, secretKey, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **collectionId** | **String**| The id of the collection that will be removed | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCollectionUsingDELETE

> RestResponse deleteCollectionUsingDELETE(accessKey, secretKey, id)

Delete existing collection with associated profiles and faces.

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let id = "id_example"; // String | The id of the collection that will be removed
apiInstance.deleteCollectionUsingDELETE(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **id** | **String**| The id of the collection that will be removed | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportCSVUsingGET

> Object exportCSVUsingGET(accessKey, secretKey, collectionId)

Retrieve collection content for data analysis.

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
apiInstance.exportCSVUsingGET(accessKey, secretKey, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionId** | **String**| The id of the collection for which the data will be retrieved | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getAllCollectionProfilesUsingGET

> RestResponse getAllCollectionProfilesUsingGET(accessKey, secretKey, id)

Gets all the profiles associated to a collection

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The collection that contains the profile
apiInstance.getAllCollectionProfilesUsingGET(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllCollections2UsingGET

> RestResponse getAllCollections2UsingGET(accessKey, secretKey)

Retrieve all collections

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
apiInstance.getAllCollections2UsingGET(accessKey, secretKey, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllCollectionsUsingGET

> RestResponse getAllCollectionsUsingGET(accessKey, secretKey)

Retrieve all collections

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
apiInstance.getAllCollectionsUsingGET(accessKey, secretKey, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCollection2UsingGET

> RestResponse getCollection2UsingGET(accessKey, secretKey, collectionId)

Retrieve existing collection content

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
apiInstance.getCollection2UsingGET(accessKey, secretKey, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionId** | **String**| The id of the collection for which the data will be retrieved | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCollectionUsingGET

> RestResponse getCollectionUsingGET(accessKey, secretKey, id)

Retrieve existing collection content

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The id of the collection for which the data will be retrieved
apiInstance.getCollectionUsingGET(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The id of the collection for which the data will be retrieved | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repurposeCollectionUsingPUT

> RestResponse repurposeCollectionUsingPUT(accessKey, secretKey, collectionId, purposes)

Change purpose of existing collection

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
let purposes = ["null"]; // [String] | The newly declared purposes of the collection
apiInstance.repurposeCollectionUsingPUT(accessKey, secretKey, collectionId, purposes, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **collectionId** | **String**| The id of the collection for which the data will be retrieved | 
 **purposes** | [**[String]**](String.md)| The newly declared purposes of the collection | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCollection2UsingPOST

> RestResponse updateCollection2UsingPOST(accessKey, secretKey, id, opts)

Update an existing collection with a given id

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let id = "id_example"; // String | The id of the collection that will be updated
let opts = {
  'name': "name_example", // String | The name of the collection that will be updated
  'purposes': ["null"] // [String] | The newly declared purposes of the collection
};
apiInstance.updateCollection2UsingPOST(accessKey, secretKey, id, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **id** | **String**| The id of the collection that will be updated | 
 **name** | **String**| The name of the collection that will be updated | [optional] 
 **purposes** | [**[String]**](String.md)| The newly declared purposes of the collection | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCollectionUsingPATCH

> RestResponse updateCollectionUsingPATCH(accessKey, secretKey, id, opts)

Update an existing collection with a given id

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.CollectionApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let id = "id_example"; // String | The id of the collection that will be updated
let opts = {
  'name': "name_example", // String | The name of the collection that will be updated
  'purposes': ["null"] // [String] | The newly declared purposes of the collection
};
apiInstance.updateCollectionUsingPATCH(accessKey, secretKey, id, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **id** | **String**| The id of the collection that will be updated | 
 **name** | **String**| The name of the collection that will be updated | [optional] 
 **purposes** | [**[String]**](String.md)| The newly declared purposes of the collection | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

