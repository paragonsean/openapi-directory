# Ecwid.ObjectNameApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createByObjectName**](ObjectNameApi.md#createByObjectName) | **POST** /{objectName} | Create an {objectName}
[**createObjectNameByChildObjectName**](ObjectNameApi.md#createObjectNameByChildObjectName) | **POST** /{objectName}/{objectId}/{childObjectName} | Create an {objectName}
[**deleteObjectNameByChildObjectId**](ObjectNameApi.md#deleteObjectNameByChildObjectId) | **DELETE** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Delete an {childObjectName}
[**deleteObjectNameByObjectId**](ObjectNameApi.md#deleteObjectNameByObjectId) | **DELETE** /{objectName}/{objectId} | Delete an {objectName}
[**getByObjectName**](ObjectNameApi.md#getByObjectName) | **GET** /{objectName} | Search for {objectName}
[**getObjectNameByChildObjectId**](ObjectNameApi.md#getObjectNameByChildObjectId) | **GET** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Retrieve an {childObjectName}
[**getObjectNameByChildObjectName**](ObjectNameApi.md#getObjectNameByChildObjectName) | **GET** /{objectName}/{objectId}/{childObjectName} | Search for {childObjectName}
[**getObjectNameByObjectId**](ObjectNameApi.md#getObjectNameByObjectId) | **GET** /{objectName}/{objectId} | Retrieve an {objectName}
[**replaceObjectNameByChildObjectId**](ObjectNameApi.md#replaceObjectNameByChildObjectId) | **PUT** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Update an {childObjectName}
[**replaceObjectNameByObjectId**](ObjectNameApi.md#replaceObjectNameByObjectId) | **PUT** /{objectName}/{objectId} | Update an {objectName}
[**updateObjectNameByChildObjectId**](ObjectNameApi.md#updateObjectNameByChildObjectId) | **PATCH** /{objectName}/{objectId}/{childObjectName}/{childObjectId} | Update an {childObjectName}
[**updateObjectNameByObjectId**](ObjectNameApi.md#updateObjectNameByObjectId) | **PATCH** /{objectName}/{objectId} | Update an {objectName}



## createByObjectName

> createByObjectName(authorization, objectName, body)

Create an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let body = new Ecwid.ModelObject(); // ModelObject | The {objectName}
apiInstance.createByObjectName(authorization, objectName, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **body** | [**ModelObject**](ModelObject.md)| The {objectName} | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createObjectNameByChildObjectName

> createObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, body)

Create an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectName = "childObjectName_example"; // String | The name of the object
let body = new Ecwid.ModelObject(); // ModelObject | The {childObjectName}
apiInstance.createObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectName** | **String**| The name of the object | 
 **body** | [**ModelObject**](ModelObject.md)| The {childObjectName} | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteObjectNameByChildObjectId

> deleteObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId)

Delete an {childObjectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let childObjectName = "childObjectName_example"; // String | The name of the childObjectName
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
apiInstance.deleteObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **childObjectName** | **String**| The name of the childObjectName | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectId** | **String**| The {childObjectName} ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteObjectNameByObjectId

> deleteObjectNameByObjectId(authorization, objectName, objectId)

Delete an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
apiInstance.deleteObjectNameByObjectId(authorization, objectName, objectId, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getByObjectName

> [ModelObject] getByObjectName(authorization, objectName, opts)

Search for {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let opts = {
  'where': "where_example", // String | The CEQL search expression.
  'pageSize': 789, // Number | The page size. Defaults to 200 if not provided. Maximum of 5000.
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getByObjectName(authorization, objectName, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **where** | **String**| The CEQL search expression. | [optional] 
 **pageSize** | **Number**| The page size. Defaults to 200 if not provided. Maximum of 5000. | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[ModelObject]**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectNameByChildObjectId

> ModelObject getObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId)

Retrieve an {childObjectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let childObjectName = "childObjectName_example"; // String | The name of the childObjectName
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
apiInstance.getObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **childObjectName** | **String**| The name of the childObjectName | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectId** | **String**| The {childObjectName} ID | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectNameByChildObjectName

> [ModelObject] getObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, opts)

Search for {childObjectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectName = "childObjectName_example"; // String | The name of the childObjectName
let opts = {
  'where': "where_example", // String | The CEQL search expression.
  'pageSize': 789, // Number | The page size. Defaults to 200 if not provided. Maximum of 5000.
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getObjectNameByChildObjectName(authorization, objectName, objectId, childObjectName, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectName** | **String**| The name of the childObjectName | 
 **where** | **String**| The CEQL search expression. | [optional] 
 **pageSize** | **Number**| The page size. Defaults to 200 if not provided. Maximum of 5000. | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[ModelObject]**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectNameByObjectId

> ModelObject getObjectNameByObjectId(authorization, objectName, objectId)

Retrieve an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
apiInstance.getObjectNameByObjectId(authorization, objectName, objectId, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/pdf


## replaceObjectNameByChildObjectId

> ModelObject replaceObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body)

Update an {childObjectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let childObjectName = "childObjectName_example"; // String | The name of the childObjectName
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
let body = new Ecwid.ModelObject(); // ModelObject | The {objectName}
apiInstance.replaceObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **childObjectName** | **String**| The name of the childObjectName | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectId** | **String**| The {childObjectName} ID | 
 **body** | [**ModelObject**](ModelObject.md)| The {objectName} | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## replaceObjectNameByObjectId

> ModelObject replaceObjectNameByObjectId(authorization, objectName, objectId, body)

Update an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
let body = new Ecwid.ModelObject(); // ModelObject | The {objectName}
apiInstance.replaceObjectNameByObjectId(authorization, objectName, objectId, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 
 **body** | [**ModelObject**](ModelObject.md)| The {objectName} | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateObjectNameByChildObjectId

> ModelObject updateObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body)

Update an {childObjectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let childObjectName = "childObjectName_example"; // String | The name of the childObjectName
let objectId = "objectId_example"; // String | The {objectName} ID
let childObjectId = "childObjectId_example"; // String | The {childObjectName} ID
let body = new Ecwid.ModelObject(); // ModelObject | The {objectName}
apiInstance.updateObjectNameByChildObjectId(authorization, objectName, childObjectName, objectId, childObjectId, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **childObjectName** | **String**| The name of the childObjectName | 
 **objectId** | **String**| The {objectName} ID | 
 **childObjectId** | **String**| The {childObjectName} ID | 
 **body** | [**ModelObject**](ModelObject.md)| The {objectName} | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateObjectNameByObjectId

> ModelObject updateObjectNameByObjectId(authorization, objectName, objectId, body)

Update an {objectName}

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectNameApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let objectId = "objectId_example"; // String | The {objectName} ID
let body = new Ecwid.ModelObject(); // ModelObject | The {objectName}
apiInstance.updateObjectNameByObjectId(authorization, objectName, objectId, body, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **objectId** | **String**| The {objectName} ID | 
 **body** | [**ModelObject**](ModelObject.md)| The {objectName} | 

### Return type

[**ModelObject**](ModelObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

