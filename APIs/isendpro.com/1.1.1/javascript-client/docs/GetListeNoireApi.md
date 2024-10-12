# ApiISendPro.GetListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getListeNoire**](GetListeNoireApi.md#getListeNoire) | **POST** /getlistenoire | Retourne le liste noire



## getListeNoire

> File getListeNoire(keyid, getListeNoire)

Retourne le liste noire

Retourne un fichier csv zippé contenant la liste noire

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.GetListeNoireApi();
let keyid = "keyid_example"; // String | Clé API
let getListeNoire = "getListeNoire_example"; // String | Doit valoir \"1\"
apiInstance.getListeNoire(keyid, getListeNoire, (error, data, response) => {
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
 **keyid** | **String**| Clé API | 
 **getListeNoire** | **String**| Doit valoir \&quot;1\&quot; | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

