# GetListeNoireApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getListeNoire**](GetListeNoireApi.md#getListeNoire) | **POST** /getlistenoire | Retourne le liste noire |


<a id="getListeNoire"></a>
# **getListeNoire**
> File getListeNoire(keyid, getListeNoire)

Retourne le liste noire

Retourne un fichier csv zippé contenant la liste noire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetListeNoireApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    GetListeNoireApi apiInstance = new GetListeNoireApi(defaultClient);
    String keyid = "keyid_example"; // String | Clé API
    String getListeNoire = "1"; // String | Doit valoir \"1\"
    try {
      File result = apiInstance.getListeNoire(keyid, getListeNoire);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetListeNoireApi#getListeNoire");
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
| **getListeNoire** | **String**| Doit valoir \&quot;1\&quot; | [enum: 1] |

### Return type

[**File**](File.md)

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

