# ApiISendPro.CampagneApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCampagne**](CampagneApi.md#getCampagne) | **GET** /campagne | Retourne les SMS envoyés sur une période donnée



## getCampagne

> File getCampagne(keyid, rapportCampagne, dateDeb, dateFin)

Retourne les SMS envoyés sur une période donnée

Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.CampagneApi();
let keyid = "keyid_example"; // String | Clé API
let rapportCampagne = "rapportCampagne_example"; // String | Doit valoir \"1\"
let dateDeb = "dateDeb_example"; // String | date de debut au format YYYY-MM-DD hh:mm
let dateFin = "dateFin_example"; // String | date de fin au format YYYY-MM-DD hh:mm
apiInstance.getCampagne(keyid, rapportCampagne, dateDeb, dateFin, (error, data, response) => {
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
 **rapportCampagne** | **String**| Doit valoir \&quot;1\&quot; | 
 **dateDeb** | **String**| date de debut au format YYYY-MM-DD hh:mm | 
 **dateFin** | **String**| date de fin au format YYYY-MM-DD hh:mm | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, file

