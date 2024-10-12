# CorrentlyIo.StromQuittungApi

All URIs are relative to *https://api.corrently.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quittungComit**](StromQuittungApi.md#quittungComit) | **POST** /quittung/commit | Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare
[**quittungCreate**](StromQuittungApi.md#quittungCreate) | **POST** /quittung/create | Create a receipt for an energy delivery (only valid in Germany).
[**quittungPrepare**](StromQuittungApi.md#quittungPrepare) | **POST** /quittung/prepare | Allows to collect data with several requests (or a single) for a receipt.
[**quittungTSE**](StromQuittungApi.md#quittungTSE) | **POST** /quittung/tse | Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).
[**quittungTSEData**](StromQuittungApi.md#quittungTSEData) | **POST** /quittung/tsedata | Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).
[**quittungTSEsignature**](StromQuittungApi.md#quittungTSEsignature) | **POST** /quittung/tsesignature | Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).
[**quittungZugferd**](StromQuittungApi.md#quittungZugferd) | **GET** /quittung/zugferd | Retrieve Zugferd XML for a given receipt (Strom-Quittung).



## quittungComit

> String quittungComit(opts)

Finishs a collection of data and finalizes receipt. Use this method after collecting all data via quittung/prepare

Uses collected fields or provided fields to create a final receipt (Strom-Quittung). 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'quittungComitRequest': new CorrentlyIo.QuittungComitRequest() // QuittungComitRequest | 
};
apiInstance.quittungComit(opts, (error, data, response) => {
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
 **quittungComitRequest** | [**QuittungComitRequest**](QuittungComitRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quittungCreate

> String quittungCreate(quittungCreateRequest)

Create a receipt for an energy delivery (only valid in Germany).

Creates a full featured receipt (Quittung) for an energy delivery as it appears on a charging session or similar events. Allows to embed receipt generation directly into external services. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let quittungCreateRequest = new CorrentlyIo.QuittungCreateRequest(); // QuittungCreateRequest | 
apiInstance.quittungCreate(quittungCreateRequest, (error, data, response) => {
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
 **quittungCreateRequest** | [**QuittungCreateRequest**](QuittungCreateRequest.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quittungPrepare

> String quittungPrepare(opts)

Allows to collect data with several requests (or a single) for a receipt.

During the first call an account parameter will be returned within the result object. Any other parameter will be set inside the preperation. If account is put into body/request in following requests, the existing collection will be extended/updated with the provided body parameters/values. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'quittungComitRequest': new CorrentlyIo.QuittungComitRequest() // QuittungComitRequest | 
};
apiInstance.quittungPrepare(opts, (error, data, response) => {
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
 **quittungComitRequest** | [**QuittungComitRequest**](QuittungComitRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## quittungTSE

> QuittungTSE200Response quittungTSE(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSE(opts, (error, data, response) => {
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
 **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] 

### Return type

[**QuittungTSE200Response**](QuittungTSE200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## quittungTSEData

> quittungTSEData(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

Allows to retrieve input string for a signing process. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSEData(opts, (error, data, response) => {
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
 **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quittungTSEsignature

> quittungTSEsignature(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

Allows to retrieve digital signature for a given receipt. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSEsignature(opts, (error, data, response) => {
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
 **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## quittungZugferd

> quittungZugferd(opts)

Retrieve Zugferd XML for a given receipt (Strom-Quittung).

Allows to retrieve XML of the zugferd invoice. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.StromQuittungApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungZugferd(opts, (error, data, response) => {
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
 **account** | **String**| Quittung Identifier  (serialnumber generated during receipt generation process) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

