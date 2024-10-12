# ObonoRksvApi.ExportApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/csv/registrierkassen/{registrierkasseUuid}/belege | 
[**exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/dep131/registrierkassen/{registrierkasseUuid}/belege | 
[**exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/dep7/registrierkassen/{registrierkasseUuid}/belege | 
[**exportGobdRegistrierkassenRegistrierkasseUuidGet**](ExportApi.md#exportGobdRegistrierkassenRegistrierkasseUuidGet) | **GET** /export/gobd/registrierkassen/{registrierkasseUuid} | 
[**exportHtmlBelegeBelegUuidGet**](ExportApi.md#exportHtmlBelegeBelegUuidGet) | **GET** /export/html/belege/{belegUuid} | 
[**exportPdfBelegeBelegUuidGet**](ExportApi.md#exportPdfBelegeBelegUuidGet) | **GET** /export/pdf/belege/{belegUuid} | 
[**exportQrBelegeBelegUuidGet**](ExportApi.md#exportQrBelegeBelegUuidGet) | **GET** /export/qr/belege/{belegUuid} | 
[**exportThermalPrintBelegeBelegUuidGet**](ExportApi.md#exportThermalPrintBelegeBelegUuidGet) | **GET** /export/thermal-print/belege/{belegUuid} | 
[**exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet**](ExportApi.md#exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet) | **GET** /export/xls/registrierkassen/{registrierkasseUuid}/belege | 



## exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet

> exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.ExportApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
let opts = {
  'before': "before_example", // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example", // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'posten': true // Boolean | Export `Posten` instead of `Belegdaten`.
};
apiInstance.exportCsvRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | 
 **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **posten** | **Boolean**| Export &#x60;Posten&#x60; instead of &#x60;Belegdaten&#x60;. | [optional] 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet

> exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.ExportApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
let opts = {
  'before': "before_example", // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example" // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
};
apiInstance.exportDep131RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | 
 **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet

> exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.ExportApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
let opts = {
  'before': "before_example", // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example" // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
};
apiInstance.exportDep7RegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | 
 **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportGobdRegistrierkassenRegistrierkasseUuidGet

> exportGobdRegistrierkassenRegistrierkasseUuidGet(registrierkasseUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.ExportApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
let opts = {
  'before': "before_example", // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example" // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
};
apiInstance.exportGobdRegistrierkassenRegistrierkasseUuidGet(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | 
 **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportHtmlBelegeBelegUuidGet

> exportHtmlBelegeBelegUuidGet(belegUuid)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';

let apiInstance = new ObonoRksvApi.ExportApi();
let belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
apiInstance.exportHtmlBelegeBelegUuidGet(belegUuid, (error, data, response) => {
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
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportPdfBelegeBelegUuidGet

> exportPdfBelegeBelegUuidGet(belegUuid)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';

let apiInstance = new ObonoRksvApi.ExportApi();
let belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
apiInstance.exportPdfBelegeBelegUuidGet(belegUuid, (error, data, response) => {
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
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportQrBelegeBelegUuidGet

> exportQrBelegeBelegUuidGet(belegUuid)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';

let apiInstance = new ObonoRksvApi.ExportApi();
let belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
apiInstance.exportQrBelegeBelegUuidGet(belegUuid, (error, data, response) => {
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
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportThermalPrintBelegeBelegUuidGet

> exportThermalPrintBelegeBelegUuidGet(belegUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';

let apiInstance = new ObonoRksvApi.ExportApi();
let belegUuid = "belegUuid_example"; // String | The `_uuid` of a particular `Beleg` to export.
let opts = {
  'qr': true, // Boolean | Should the RKSV QR code should be rendered?
  'width': 42, // Number | Number of characters per line.
  'dialect': "'escpos'", // String | The thermal printer dialect.
  'encoding': "'raw'" // String | The encoding of the binary data.
};
apiInstance.exportThermalPrintBelegeBelegUuidGet(belegUuid, opts, (error, data, response) => {
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
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Beleg&#x60; to export. | 
 **qr** | **Boolean**| Should the RKSV QR code should be rendered? | [optional] [default to true]
 **width** | **Number**| Number of characters per line. | [optional] [default to 42]
 **dialect** | **String**| The thermal printer dialect. | [optional] [default to &#39;escpos&#39;]
 **encoding** | **String**| The encoding of the binary data. | [optional] [default to &#39;raw&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet

> exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts)



### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.ExportApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to export.
let opts = {
  'before': "before_example", // String | Only return results that were saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example" // String | Only return results that were saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
};
apiInstance.exportXlsRegistrierkassenRegistrierkasseUuidBelegeGet(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to export. | 
 **before** | **String**| Only return results that were saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that were saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

