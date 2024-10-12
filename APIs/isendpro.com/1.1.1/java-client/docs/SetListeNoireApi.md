# SetListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setListeNoire**](SetListeNoireApi.md#setListeNoire) | **POST** /setlistenoire | Ajoute un numero en liste noire |


<a id="setListeNoire"></a>
# **setListeNoire**
> LISTENOIREReponse setListeNoire(keyid, setlisteNoire, num)

Ajoute un numero en liste noire

Ajoute un numero en liste noire. Une fois ajouté, les requêtes d&#39;envoi de SMS marketing vers ce numéro seront refusées.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SetListeNoireApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    SetListeNoireApi apiInstance = new SetListeNoireApi(defaultClient);
    String keyid = "keyid_example"; // String | Clé API
    String setlisteNoire = "1"; // String | Doit valoir \"1\"
    String num = "num_example"; // String | numéro de mobile à insérer en liste noire
    try {
      LISTENOIREReponse result = apiInstance.setListeNoire(keyid, setlisteNoire, num);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SetListeNoireApi#setListeNoire");
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
| **setlisteNoire** | **String**| Doit valoir \&quot;1\&quot; | [enum: 1] |
| **num** | **String**| numéro de mobile à insérer en liste noire | |

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

