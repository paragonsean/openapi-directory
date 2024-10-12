# MonatsbelegeApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMonatsbelege**](MonatsbelegeApi.md#getMonatsbelege) | **GET** /registrierkassen/{registrierkasseUuid}/monatsbelege |  |


<a id="getMonatsbelege"></a>
# **getMonatsbelege**
> List&lt;Monatsbeleg&gt; getMonatsbelege(registrierkasseUuid, year, month)



Returns a list of &#x60;Monatsbelege&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonatsbelegeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    MonatsbelegeApi apiInstance = new MonatsbelegeApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse`.
    Integer year = 56; // Integer | 
    Integer month = 56; // Integer | 
    try {
      List<Monatsbeleg> result = apiInstance.getMonatsbelege(registrierkasseUuid, year, month);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonatsbelegeApi#getMonatsbelege");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60;. | |
| **year** | **Integer**|  | [optional] |
| **month** | **Integer**|  | [optional] |

### Return type

[**List&lt;Monatsbeleg&gt;**](Monatsbeleg.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about &#x60;Monatsbelege&#x60;. |  -  |

