# ViberServiceMessageApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVSMAccount**](ViberServiceMessageApi.md#getVSMAccount) | **GET** /viber_service_msg/{external_id} | Retrieve a Viber Service Message account |


<a id="getVSMAccount"></a>
# **getVSMAccount**
> VSMAccountResponse getVSMAccount(externalId)

Retrieve a Viber Service Message account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViberServiceMessageApi;

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

    ViberServiceMessageApi apiInstance = new ViberServiceMessageApi(defaultClient);
    String externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it will be your Viber Service Message ID.
    try {
      VSMAccountResponse result = apiInstance.getVSMAccount(externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViberServiceMessageApi#getVSMAccount");
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
| **externalId** | **String**| External id of the account you want to retrieve. In this case it will be your Viber Service Message ID. | |

### Return type

[**VSMAccountResponse**](VSMAccountResponse.md)

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

