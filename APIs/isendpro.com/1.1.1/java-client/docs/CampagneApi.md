# CampagneApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCampagne**](CampagneApi.md#getCampagne) | **GET** /campagne | Retourne les SMS envoyés sur une période donnée |


<a id="getCampagne"></a>
# **getCampagne**
> File getCampagne(keyid, rapportCampagne, dateDeb, dateFin)

Retourne les SMS envoyés sur une période donnée

Retourne les SMS envoyés sur une période donnée en fonction d&#39;une date de début et d&#39;une date de fin.   Les dates sont au format YYYY-MM-DD hh:mm.   Le fichier rapport de campagne est sous la forme d&#39;un fichier zip + contenant un fichier csv contenant le détail des envois. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CampagneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    CampagneApi apiInstance = new CampagneApi(defaultClient);
    String keyid = "keyid_example"; // String | Clé API
    String rapportCampagne = "1"; // String | Doit valoir \"1\"
    String dateDeb = "dateDeb_example"; // String | date de debut au format YYYY-MM-DD hh:mm
    String dateFin = "dateFin_example"; // String | date de fin au format YYYY-MM-DD hh:mm
    try {
      File result = apiInstance.getCampagne(keyid, rapportCampagne, dateDeb, dateFin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CampagneApi#getCampagne");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keyid** | **String**| Clé API | |
| **rapportCampagne** | **String**| Doit valoir \&quot;1\&quot; | [enum: 1] |
| **dateDeb** | **String**| date de debut au format YYYY-MM-DD hh:mm | |
| **dateFin** | **String**| date de fin au format YYYY-MM-DD hh:mm | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, file

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Erreur |  -  |

