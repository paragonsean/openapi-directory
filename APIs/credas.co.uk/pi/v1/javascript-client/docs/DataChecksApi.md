# CredasApi.DataChecksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDataCheck**](DataChecksApi.md#addDataCheck) | **POST** /api/datachecks | Creates new data check against a specified registration.



## addDataCheck

> CredasApiModelsDataCheckAddDataCheckResponse addDataCheck(apikey, opts)

Creates new data check against a specified registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.DataChecksApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsDataCheckAddDataCheckRequest': new CredasApi.CredasApiModelsDataCheckAddDataCheckRequest() // CredasApiModelsDataCheckAddDataCheckRequest | Object containing data check details.
};
apiInstance.addDataCheck(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsDataCheckAddDataCheckRequest** | [**CredasApiModelsDataCheckAddDataCheckRequest**](CredasApiModelsDataCheckAddDataCheckRequest.md)| Object containing data check details. | [optional] 

### Return type

[**CredasApiModelsDataCheckAddDataCheckResponse**](CredasApiModelsDataCheckAddDataCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

