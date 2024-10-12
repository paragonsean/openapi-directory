# BioLinkApi.MmeApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postDiseaseMme**](MmeApi.md#postDiseaseMme) | **POST** /mme/disease | Match a patient to diseases based on their phenotypes
[**postFlyMme**](MmeApi.md#postFlyMme) | **POST** /mme/fly | Match a patient to fruit fly genes based on similar phenotypes
[**postMouseMme**](MmeApi.md#postMouseMme) | **POST** /mme/mouse | Match a patient to mouse genes based on similar phenotypes
[**postNematodeMme**](MmeApi.md#postNematodeMme) | **POST** /mme/nematode | Match a patient to nematode genes based on similar phenotypes
[**postZebrafishMme**](MmeApi.md#postZebrafishMme) | **POST** /mme/zebrafish | Match a patient to zebrafish genes based on similar phenotypes



## postDiseaseMme

> postDiseaseMme(body)

Match a patient to diseases based on their phenotypes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MmeApi();
let body = {key: null}; // Object | 
apiInstance.postDiseaseMme(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postFlyMme

> postFlyMme(body)

Match a patient to fruit fly genes based on similar phenotypes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MmeApi();
let body = {key: null}; // Object | 
apiInstance.postFlyMme(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postMouseMme

> postMouseMme(body)

Match a patient to mouse genes based on similar phenotypes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MmeApi();
let body = {key: null}; // Object | 
apiInstance.postMouseMme(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postNematodeMme

> postNematodeMme(body)

Match a patient to nematode genes based on similar phenotypes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MmeApi();
let body = {key: null}; // Object | 
apiInstance.postNematodeMme(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postZebrafishMme

> postZebrafishMme(body)

Match a patient to zebrafish genes based on similar phenotypes

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MmeApi();
let body = {key: null}; // Object | 
apiInstance.postZebrafishMme(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

