# WhatsAppApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getWAAccount**](WhatsAppApi.md#getWAAccount) | **GET** /whatsapp/{external_id} | Retrieve a Whatsapp account |


<a id="getWAAccount"></a>
# **getWAAccount**
> WAAccountResponse getWAAccount(externalId)

Retrieve a Whatsapp account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WhatsAppApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
    String externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it will be the WhatsApp number.
    try {
      WAAccountResponse result = apiInstance.getWAAccount(externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WhatsAppApi#getWAAccount");
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
| **externalId** | **String**| External id of the account you want to retrieve. In this case it will be the WhatsApp number. | |

### Return type

[**WAAccountResponse**](WAAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **401** | Unauthorized. |  -  |
| **404** | Not Found. |  -  |

