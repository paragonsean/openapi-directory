# ApisApi

All URIs are relative to *https://apisetu.gov.in/dgft*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importerExporterCodeVerificationAPI**](ApisApi.md#importerExporterCodeVerificationAPI) | **GET** /v1/iec/{iec} | Importer-Exporter Code (IEC) Verification API. |


<a id="importerExporterCodeVerificationAPI"></a>
# **importerExporterCodeVerificationAPI**
> ImporterExporterCodeVerificationAPI200Response importerExporterCodeVerificationAPI(iec)

Importer-Exporter Code (IEC) Verification API.

Description of Importer-Exporter Code (IEC) Verification API.

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
    defaultClient.setBasePath("https://apisetu.gov.in/dgft");
    
    // Configure API key authorization: clientId
    ApiKeyAuth clientId = (ApiKeyAuth) defaultClient.getAuthentication("clientId");
    clientId.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientId.setApiKeyPrefix("Token");

    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String iec = "iec_example"; // String | Importer-Exporter code
    try {
      ImporterExporterCodeVerificationAPI200Response result = apiInstance.importerExporterCodeVerificationAPI(iec);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#importerExporterCodeVerificationAPI");
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
| **iec** | **String**| Importer-Exporter code | |

### Return type

[**ImporterExporterCodeVerificationAPI200Response**](ImporterExporterCodeVerificationAPI200Response.md)

### Authorization

[clientId](../README.md#clientId), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad Request |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |
| **503** | Service Unavailable |  -  |
| **504** | Gateway Timeout |  -  |

