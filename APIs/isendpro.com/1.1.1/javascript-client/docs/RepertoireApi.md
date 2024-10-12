# ApiISendPro.RepertoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repertoire**](RepertoireApi.md#repertoire) | **PUT** /repertoire | Gestion repertoire (modification)
[**repertoireCrea**](RepertoireApi.md#repertoireCrea) | **POST** /repertoire | Gestion repertoire (creation)



## repertoire

> REPERTOIREmodifreponse repertoire(rEPERTOIREmodifrequest)

Gestion repertoire (modification)

Ajoute ou supprime une liste de numéros à un répertoire existant.

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.RepertoireApi();
let rEPERTOIREmodifrequest = new ApiISendPro.REPERTOIREmodifrequest(); // REPERTOIREmodifrequest | Requête de creation repertoire
apiInstance.repertoire(rEPERTOIREmodifrequest, (error, data, response) => {
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
 **rEPERTOIREmodifrequest** | [**REPERTOIREmodifrequest**](REPERTOIREmodifrequest.md)| Requête de creation repertoire | 

### Return type

[**REPERTOIREmodifreponse**](REPERTOIREmodifreponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repertoireCrea

> REPERTOIREcreatereponse repertoireCrea(rEPERTOIREcreaterequest)

Gestion repertoire (creation)

Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.RepertoireApi();
let rEPERTOIREcreaterequest = new ApiISendPro.REPERTOIREcreaterequest(); // REPERTOIREcreaterequest | Creation repertoire
apiInstance.repertoireCrea(rEPERTOIREcreaterequest, (error, data, response) => {
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
 **rEPERTOIREcreaterequest** | [**REPERTOIREcreaterequest**](REPERTOIREcreaterequest.md)| Creation repertoire | 

### Return type

[**REPERTOIREcreatereponse**](REPERTOIREcreatereponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

