# ComptageApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**comptage**](ComptageApi.md#comptage) | **POST** /comptage | Compter le nombre de caractère  |


<a id="comptage"></a>
# **comptage**
> ComptageReponse comptage(comptageRequest)

Compter le nombre de caractère 

Compte le nombre de SMS necessaire à un envoi

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComptageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    ComptageApi apiInstance = new ComptageApi(defaultClient);
    ComptageRequest comptageRequest = new ComptageRequest(); // ComptageRequest | sms request
    try {
      ComptageReponse result = apiInstance.comptage(comptageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComptageApi#comptage");
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
| **comptageRequest** | [**ComptageRequest**](ComptageRequest.md)| sms request | |

### Return type

[**ComptageReponse**](ComptageReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, etat

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

