# ApiISendPro.DelListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delListeNoire**](DelListeNoireApi.md#delListeNoire) | **POST** /dellistenoire | Ajoute un numero en liste noire



## delListeNoire

> LISTENOIREReponse delListeNoire(keyid, delListeNoire, num)

Ajoute un numero en liste noire

Supprime un numero en liste noire

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.DelListeNoireApi();
let keyid = "keyid_example"; // String | Clé API
let delListeNoire = "delListeNoire_example"; // String | Doit valoir \"1\"
let num = "num_example"; // String | numéro de mobile à supprimer
apiInstance.delListeNoire(keyid, delListeNoire, num, (error, data, response) => {
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
 **delListeNoire** | **String**| Doit valoir \&quot;1\&quot; | 
 **num** | **String**| numéro de mobile à supprimer | 

### Return type

[**LISTENOIREReponse**](LISTENOIREReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

