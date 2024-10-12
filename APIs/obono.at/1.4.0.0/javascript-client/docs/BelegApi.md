# ObonoRksvApi.BelegApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addBeleg**](BelegApi.md#addBeleg) | **PUT** /registrierkassen/{registrierkasseUuid}/belege/{belegUuid} | 
[**belegeBelegUuidGet**](BelegApi.md#belegeBelegUuidGet) | **GET** /belege/{belegUuid} | 
[**createAbschluss**](BelegApi.md#createAbschluss) | **POST** /registrierkassen/{registrierkasseUuid}/abschluss | 
[**getBeleg**](BelegApi.md#getBeleg) | **GET** /registrierkassen/{registrierkasseUuid}/belege/{belegUuid} | 
[**getBelege**](BelegApi.md#getBelege) | **GET** /registrierkassen/{registrierkasseUuid}/belege | 



## addBeleg

> addBeleg(registrierkasseUuid, belegUuid, belegdaten)



Signs a receipt and stores it in the \&quot;Datenerfassungsprotokoll\&quot;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.BelegApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to use for signing data.
let belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to store.
let belegdaten = new ObonoRksvApi.Belegdaten(); // Belegdaten | An object that contains all data for a particular `Beleg` and is formatted according to RKSV \"Signaturformat\".
apiInstance.addBeleg(registrierkasseUuid, belegUuid, belegdaten, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to use for signing data. | 
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to store. | 
 **belegdaten** | [**Belegdaten**](Belegdaten.md)| An object that contains all data for a particular &#x60;Beleg&#x60; and is formatted according to RKSV \&quot;Signaturformat\&quot;. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## belegeBelegUuidGet

> Beleg belegeBelegUuidGet(belegUuid)



Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';

let apiInstance = new ObonoRksvApi.BelegApi();
let belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to fetch.
apiInstance.belegeBelegUuidGet(belegUuid, (error, data, response) => {
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
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch. | 

### Return type

[**Beleg**](Beleg.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createAbschluss

> createAbschluss(registrierkasseUuid, abschlussbelegdaten)



Generates an &#x60;Abschlussbeleg&#x60;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.BelegApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the `Beleg` collection.
let abschlussbelegdaten = new ObonoRksvApi.Abschlussbelegdaten(); // Abschlussbelegdaten | An object that contains all data for a particular `Abschlussbeleg`.
apiInstance.createAbschluss(registrierkasseUuid, abschlussbelegdaten, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection. | 
 **abschlussbelegdaten** | [**Abschlussbelegdaten**](Abschlussbelegdaten.md)| An object that contains all data for a particular &#x60;Abschlussbeleg&#x60;. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getBeleg

> Beleg getBeleg(registrierkasseUuid, belegUuid)



Retrieves a particular &#x60;Beleg&#x60; from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.BelegApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` that contains the requested `Beleg`.
let belegUuid = "belegUuid_example"; // String | The `_uuid` of the `Beleg` to fetch.
apiInstance.getBeleg(registrierkasseUuid, belegUuid, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; that contains the requested &#x60;Beleg&#x60;. | 
 **belegUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Beleg&#x60; to fetch. | 

### Return type

[**Beleg**](Beleg.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBelege

> Belege getBelege(registrierkasseUuid, format, opts)



Retrieves the &#x60;Beleg&#x60; collection from the \&quot;Datenerfassungsprotokoll\&quot;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.BelegApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the `Beleg` collection.
let format = "'export'"; // String | Determines the format of the `Beleg` collection.
let opts = {
  'order': "'asc'", // String | Determines the sorting order.
  'limit': 56, // Number | Limits the number of returned results.
  'offset': 0, // Number | Skips the specified number of results from the result set.
  'before': "before_example", // String | Only return results that where saved before the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'after': "after_example", // String | Only return results that where saved after the specified date-time string (i.e., anything that `Date.parse()` can parse).
  'gte': 56, // Number | Only return results that have at least a particular `Belegnummer`.
  'lte': 56 // Number | Only return results that have at most a particular `Belegnummer`.
};
apiInstance.getBelege(registrierkasseUuid, format, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the &#x60;Beleg&#x60; collection. | 
 **format** | **String**| Determines the format of the &#x60;Beleg&#x60; collection. | [default to &#39;export&#39;]
 **order** | **String**| Determines the sorting order. | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Limits the number of returned results. | [optional] 
 **offset** | **Number**| Skips the specified number of results from the result set. | [optional] [default to 0]
 **before** | **String**| Only return results that where saved before the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **after** | **String**| Only return results that where saved after the specified date-time string (i.e., anything that &#x60;Date.parse()&#x60; can parse). | [optional] 
 **gte** | **Number**| Only return results that have at least a particular &#x60;Belegnummer&#x60;. | [optional] 
 **lte** | **Number**| Only return results that have at most a particular &#x60;Belegnummer&#x60;. | [optional] 

### Return type

[**Belege**](Belege.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

