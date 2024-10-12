# Contribly.InfoApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactFormatsGet**](InfoApi.md#artifactFormatsGet) | **GET** /artifact-formats | Artifact formats
[**changeLogGet**](InfoApi.md#changeLogGet) | **GET** /change-log | Recent changes
[**eventTypesGet**](InfoApi.md#eventTypesGet) | **GET** /event-types | Event types



## artifactFormatsGet

> ArtifactFormats artifactFormatsGet()

Artifact formats

List the available artifact formats

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.InfoApi();
apiInstance.artifactFormatsGet((error, data, response) => {
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

[**ArtifactFormats**](ArtifactFormats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changeLogGet

> [ChangeLogItem] changeLogGet()

Recent changes

The Contribly change log.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.InfoApi();
apiInstance.changeLogGet((error, data, response) => {
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

[**[ChangeLogItem]**](ChangeLogItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventTypesGet

> [EventType] eventTypesGet()

Event types

List available notification event types

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.InfoApi();
apiInstance.eventTypesGet((error, data, response) => {
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

[**[EventType]**](EventType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

