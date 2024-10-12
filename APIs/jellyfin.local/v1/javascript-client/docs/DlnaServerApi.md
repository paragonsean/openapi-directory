# JellyfinApi.DlnaServerApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConnectionManager**](DlnaServerApi.md#getConnectionManager) | **GET** /Dlna/{serverId}/ConnectionManager | Gets Dlna media receiver registrar xml.
[**getConnectionManager2**](DlnaServerApi.md#getConnectionManager2) | **GET** /Dlna/{serverId}/ConnectionManager/ConnectionManager | Gets Dlna media receiver registrar xml.
[**getConnectionManager3**](DlnaServerApi.md#getConnectionManager3) | **GET** /Dlna/{serverId}/ConnectionManager/ConnectionManager.xml | Gets Dlna media receiver registrar xml.
[**getContentDirectory**](DlnaServerApi.md#getContentDirectory) | **GET** /Dlna/{serverId}/ContentDirectory | Gets Dlna content directory xml.
[**getContentDirectory2**](DlnaServerApi.md#getContentDirectory2) | **GET** /Dlna/{serverId}/ContentDirectory/ContentDirectory | Gets Dlna content directory xml.
[**getContentDirectory3**](DlnaServerApi.md#getContentDirectory3) | **GET** /Dlna/{serverId}/ContentDirectory/ContentDirectory.xml | Gets Dlna content directory xml.
[**getDescriptionXml**](DlnaServerApi.md#getDescriptionXml) | **GET** /Dlna/{serverId}/description | Get Description Xml.
[**getDescriptionXml2**](DlnaServerApi.md#getDescriptionXml2) | **GET** /Dlna/{serverId}/description.xml | Get Description Xml.
[**getIcon**](DlnaServerApi.md#getIcon) | **GET** /Dlna/icons/{fileName} | Gets a server icon.
[**getIconId**](DlnaServerApi.md#getIconId) | **GET** /Dlna/{serverId}/icons/{fileName} | Gets a server icon.
[**getMediaReceiverRegistrar**](DlnaServerApi.md#getMediaReceiverRegistrar) | **GET** /Dlna/{serverId}/MediaReceiverRegistrar | Gets Dlna media receiver registrar xml.
[**getMediaReceiverRegistrar2**](DlnaServerApi.md#getMediaReceiverRegistrar2) | **GET** /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar | Gets Dlna media receiver registrar xml.
[**getMediaReceiverRegistrar3**](DlnaServerApi.md#getMediaReceiverRegistrar3) | **GET** /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml | Gets Dlna media receiver registrar xml.
[**processConnectionManagerControlRequest**](DlnaServerApi.md#processConnectionManagerControlRequest) | **POST** /Dlna/{serverId}/ConnectionManager/Control | Process a connection manager control request.
[**processContentDirectoryControlRequest**](DlnaServerApi.md#processContentDirectoryControlRequest) | **POST** /Dlna/{serverId}/ContentDirectory/Control | Process a content directory control request.
[**processMediaReceiverRegistrarControlRequest**](DlnaServerApi.md#processMediaReceiverRegistrarControlRequest) | **POST** /Dlna/{serverId}/MediaReceiverRegistrar/Control | Process a media receiver registrar control request.



## getConnectionManager

> File getConnectionManager(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getConnectionManager(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getConnectionManager2

> File getConnectionManager2(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getConnectionManager2(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getConnectionManager3

> File getConnectionManager3(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getConnectionManager3(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getContentDirectory

> File getContentDirectory(serverId)

Gets Dlna content directory xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getContentDirectory(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getContentDirectory2

> File getContentDirectory2(serverId)

Gets Dlna content directory xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getContentDirectory2(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getContentDirectory3

> File getContentDirectory3(serverId)

Gets Dlna content directory xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getContentDirectory3(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getDescriptionXml

> File getDescriptionXml(serverId)

Get Description Xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getDescriptionXml(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getDescriptionXml2

> File getDescriptionXml2(serverId)

Get Description Xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getDescriptionXml2(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getIcon

> File getIcon(fileName)

Gets a server icon.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let fileName = "fileName_example"; // String | The icon filename.
apiInstance.getIcon(fileName, (error, data, response) => {
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
 **fileName** | **String**| The icon filename. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getIconId

> File getIconId(serverId, fileName)

Gets a server icon.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
let fileName = "fileName_example"; // String | The icon filename.
apiInstance.getIconId(serverId, fileName, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 
 **fileName** | **String**| The icon filename. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMediaReceiverRegistrar

> File getMediaReceiverRegistrar(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getMediaReceiverRegistrar(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMediaReceiverRegistrar2

> File getMediaReceiverRegistrar2(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getMediaReceiverRegistrar2(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## getMediaReceiverRegistrar3

> File getMediaReceiverRegistrar3(serverId)

Gets Dlna media receiver registrar xml.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.getMediaReceiverRegistrar3(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## processConnectionManagerControlRequest

> File processConnectionManagerControlRequest(serverId)

Process a connection manager control request.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.processConnectionManagerControlRequest(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## processContentDirectoryControlRequest

> File processContentDirectoryControlRequest(serverId)

Process a content directory control request.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.processContentDirectoryControlRequest(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml


## processMediaReceiverRegistrarControlRequest

> File processMediaReceiverRegistrarControlRequest(serverId)

Process a media receiver registrar control request.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.DlnaServerApi();
let serverId = "serverId_example"; // String | Server UUID.
apiInstance.processMediaReceiverRegistrarControlRequest(serverId, (error, data, response) => {
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
 **serverId** | **String**| Server UUID. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/xml

