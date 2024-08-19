# KeycloakApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keycloakList**](KeycloakApi.md#keycloakList) | **GET** /keycloak |  |


<a id="keycloakList"></a>
# **keycloakList**
> keycloakList()



serves keycloak config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeycloakApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    KeycloakApi apiInstance = new KeycloakApi(defaultClient);
    try {
      apiInstance.keycloakList();
    } catch (ApiException e) {
      System.err.println("Exception when calling KeycloakApi#keycloakList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

