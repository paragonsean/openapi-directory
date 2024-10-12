# ApiISendPro.SetListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setListeNoire**](SetListeNoireApi.md#setListeNoire) | **POST** /setlistenoire | Ajoute un numero en liste noire



## setListeNoire

> LISTENOIREReponse setListeNoire(keyid, setlisteNoire, num)

Ajoute un numero en liste noire

Ajoute un numero en liste noire. Une fois ajouté, les requêtes d&#39;envoi de SMS marketing vers ce numéro seront refusées.

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.SetListeNoireApi();
let keyid = "keyid_example"; // String | Clé API
let setlisteNoire = "setlisteNoire_example"; // String | Doit valoir \"1\"
let num = "num_example"; // String | numéro de mobile à insérer en liste noire
apiInstance.setListeNoire(keyid, setlisteNoire, num, (error, data, response) => {
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
 **setlisteNoire** | **String**| Doit valoir \&quot;1\&quot; | 
 **num** | **String**| numéro de mobile à insérer en liste noire | 

### Return type

[**LISTENOIREReponse**](LISTENOIREReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

