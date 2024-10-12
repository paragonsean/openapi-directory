# DelListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delListeNoire**](DelListeNoireApi.md#delListeNoire) | **POST** /dellistenoire | Ajoute un numero en liste noire |


<a id="delListeNoire"></a>
# **delListeNoire**
> LISTENOIREReponse delListeNoire(keyid, delListeNoire, num)

Ajoute un numero en liste noire

Supprime un numero en liste noire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DelListeNoireApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    DelListeNoireApi apiInstance = new DelListeNoireApi(defaultClient);
    String keyid = "keyid_example"; // String | Clé API
    String delListeNoire = "1"; // String | Doit valoir \"1\"
    String num = "num_example"; // String | numéro de mobile à supprimer
    try {
      LISTENOIREReponse result = apiInstance.delListeNoire(keyid, delListeNoire, num);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelListeNoireApi#delListeNoire");
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
| **delListeNoire** | **String**| Doit valoir \&quot;1\&quot; | [enum: 1] |
| **num** | **String**| numéro de mobile à supprimer | |

### Return type

[**LISTENOIREReponse**](LISTENOIREReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **400** | Erreur |  -  |

