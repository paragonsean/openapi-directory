# CorrentlyIo.TSEApi

All URIs are relative to *https://api.corrently.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quittungTSEData_0**](TSEApi.md#quittungTSEData_0) | **POST** /quittung/tsedata | Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).
[**quittungTSE_0**](TSEApi.md#quittungTSE_0) | **POST** /quittung/tse | Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).
[**quittungTSEsignature_0**](TSEApi.md#quittungTSEsignature_0) | **POST** /quittung/tsesignature | Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).
[**quittungZugferd_0**](TSEApi.md#quittungZugferd_0) | **GET** /quittung/zugferd | Retrieve Zugferd XML for a given receipt (Strom-Quittung).



## quittungTSEData_0

> quittungTSEData_0(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) raw data  only for a given receipt (Strom-Quittung).

Allows to retrieve input string for a signing process. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.TSEApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSEData_0(opts, (error, data, response) => {
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


## quittungTSE_0

> QuittungTSE200Response quittungTSE_0(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) Data for a given receipt (Strom-Quittung).

Allows to retrieve all relevant data assiciated to a TSE service call. E.q. Input parameters, public key and signature. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.TSEApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSE_0(opts, (error, data, response) => {
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


## quittungTSEsignature_0

> quittungTSEsignature_0(opts)

Retrieve TSE (Technische Sicherheitseinrichtung) Signature only for a given receipt (Strom-Quittung).

Allows to retrieve digital signature for a given receipt. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.TSEApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungTSEsignature_0(opts, (error, data, response) => {
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


## quittungZugferd_0

> quittungZugferd_0(opts)

Retrieve Zugferd XML for a given receipt (Strom-Quittung).

Allows to retrieve XML of the zugferd invoice. 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.TSEApi();
let opts = {
  'account': "account_example" // String | Quittung Identifier  (serialnumber generated during receipt generation process)
};
apiInstance.quittungZugferd_0(opts, (error, data, response) => {
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

