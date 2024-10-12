# RepertoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repertoire**](RepertoireApi.md#repertoire) | **PUT** /repertoire | Gestion repertoire (modification) |
| [**repertoireCrea**](RepertoireApi.md#repertoireCrea) | **POST** /repertoire | Gestion repertoire (creation) |


<a id="repertoire"></a>
# **repertoire**
> REPERTOIREmodifreponse repertoire(rePERTOIREmodifrequest)

Gestion repertoire (modification)

Ajoute ou supprime une liste de numéros à un répertoire existant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepertoireApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    RepertoireApi apiInstance = new RepertoireApi(defaultClient);
    REPERTOIREmodifrequest rePERTOIREmodifrequest = new REPERTOIREmodifrequest(); // REPERTOIREmodifrequest | Requête de creation repertoire
    try {
      REPERTOIREmodifreponse result = apiInstance.repertoire(rePERTOIREmodifrequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepertoireApi#repertoire");
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
| **rePERTOIREmodifrequest** | [**REPERTOIREmodifrequest**](REPERTOIREmodifrequest.md)| Requête de creation repertoire | |

### Return type

[**REPERTOIREmodifreponse**](REPERTOIREmodifreponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Erreur |  -  |

<a id="repertoireCrea"></a>
# **repertoireCrea**
> REPERTOIREcreatereponse repertoireCrea(rePERTOIREcreaterequest)

Gestion repertoire (creation)

Cree un nouveau répertoire et retourne son identifiant. Cet identifiant pourra être utilisé pour ajouter ou supprimer des numéros via l&#39;API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepertoireApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    RepertoireApi apiInstance = new RepertoireApi(defaultClient);
    REPERTOIREcreaterequest rePERTOIREcreaterequest = new REPERTOIREcreaterequest(); // REPERTOIREcreaterequest | Creation repertoire
    try {
      REPERTOIREcreatereponse result = apiInstance.repertoireCrea(rePERTOIREcreaterequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepertoireApi#repertoireCrea");
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
| **rePERTOIREcreaterequest** | [**REPERTOIREcreaterequest**](REPERTOIREcreaterequest.md)| Creation repertoire | |

### Return type

[**REPERTOIREcreatereponse**](REPERTOIREcreatereponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Erreur |  -  |

