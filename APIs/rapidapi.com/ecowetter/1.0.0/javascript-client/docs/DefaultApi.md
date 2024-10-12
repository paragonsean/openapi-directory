# HistorischeDaten.DefaultApi

All URIs are relative to *https://api.ecowetter.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicHistoryGet**](DefaultApi.md#publicHistoryGet) | **GET** /public/history | Wetter 2021 für Berlin, Reichstag



## publicHistoryGet

> Object publicHistoryGet(opts)

Wetter 2021 für Berlin, Reichstag

Abfrage der Wettervorhersage für einen Ort, der entweder durch Angabe eines Suchbegriffs mit dem Parameter &#x60;q&#x60; oder durch Geo-Koordinaten in den Parametern &#x60;lat&#x60; und &#x60;lon&#x60; spezifiziert wird.

### Example

```javascript
import HistorischeDaten from 'historische_daten';

let apiInstance = new HistorischeDaten.DefaultApi();
let opts = {
  'q': "Berlin, Reichstag", // String | Ortssuche mit Freitext
  'from': "2021-01-01", // String | Startdatum der Abfrage im Format (JJJJ-MM-DD)
  'to': "2022-01-01" // String | Enddatum der Abfrage im Format (JJJJ-MM-DD)
};
apiInstance.publicHistoryGet(opts, (error, data, response) => {
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
 **q** | **String**| Ortssuche mit Freitext | [optional] 
 **from** | **String**| Startdatum der Abfrage im Format (JJJJ-MM-DD) | [optional] 
 **to** | **String**| Enddatum der Abfrage im Format (JJJJ-MM-DD) | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

