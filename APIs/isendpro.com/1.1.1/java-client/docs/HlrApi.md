# HlrApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHlr**](HlrApi.md#getHlr) | **POST** /hlr | Vérifier la validité d&#39;un numéro |


<a id="getHlr"></a>
# **getHlr**
> HLRReponse getHlr(hlRrequest)

Vérifier la validité d&#39;un numéro

Réalise un lookup HLR sur les numéros  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HlrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    HlrApi apiInstance = new HlrApi(defaultClient);
    HLRrequest hlRrequest = new HLRrequest(); // HLRrequest | 
    try {
      HLRReponse result = apiInstance.getHlr(hlRrequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HlrApi#getHlr");
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
| **hlRrequest** | [**HLRrequest**](HLRrequest.md)|  | |

### Return type

[**HLRReponse**](HLRReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

