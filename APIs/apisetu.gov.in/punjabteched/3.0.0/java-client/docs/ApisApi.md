# ApisApi

All URIs are relative to *https://apisetu.gov.in/punjabteched/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dgcer**](ApisApi.md#dgcer) | **POST** /dgcer/certificate | Degree/ Diploma Certificate |


<a id="dgcer"></a>
# **dgcer**
> dgcer(dgcerRequest)

Degree/ Diploma Certificate

API to verify Degree/ Diploma Certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apisetu.gov.in/punjabteched/v3");
    
    // Configure API key authorization: clientId
    ApiKeyAuth clientId = (ApiKeyAuth) defaultClient.getAuthentication("clientId");
    clientId.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientId.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    DgcerRequest dgcerRequest = new DgcerRequest(); // DgcerRequest | Request format
    try {
      apiInstance.dgcer(dgcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#dgcer");
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
| **dgcerRequest** | [**DgcerRequest**](DgcerRequest.md)| Request format | [optional] |

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate data in response body in PDF, XML or JSON format as requested in format parameter. |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized access |  -  |
| **404** | No record found |  -  |
| **500** | Internal server error |  -  |
| **502** | Bad gateway |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

