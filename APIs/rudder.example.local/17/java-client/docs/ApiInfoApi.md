# ApiInfoApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiGeneralInformations**](ApiInfoApi.md#apiGeneralInformations) | **GET** /info | List all endoints |
| [**apiInformations**](ApiInfoApi.md#apiInformations) | **GET** /info/details/{endpointName} | Get information about one API endpoint |
| [**apiSubInformations**](ApiInfoApi.md#apiSubInformations) | **GET** /info/{sectionId} | Get information on endpoint in a section |


<a id="apiGeneralInformations"></a>
# **apiGeneralInformations**
> ApiGeneralInformations200Response apiGeneralInformations()

List all endoints

List all endpoints and their version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    try {
      ApiGeneralInformations200Response result = apiInstance.apiGeneralInformations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#apiGeneralInformations");
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

[**ApiGeneralInformations200Response**](ApiGeneralInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API endpoints |  -  |

<a id="apiInformations"></a>
# **apiInformations**
> ApiInformations200Response apiInformations(endpointName)

Get information about one API endpoint

Get the description and the list of supported version for one API endpoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    String endpointName = "listAcceptedNodes"; // String | Name of the endpoint for which one wants information
    try {
      ApiInformations200Response result = apiInstance.apiInformations(endpointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#apiInformations");
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
| **endpointName** | **String**| Name of the endpoint for which one wants information | |

### Return type

[**ApiInformations200Response**](ApiInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Endpoint information |  -  |

<a id="apiSubInformations"></a>
# **apiSubInformations**
> ApiSubInformations200Response apiSubInformations(sectionId)

Get information on endpoint in a section

Get all endpoints in the given section with their supported version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ApiInfoApi apiInstance = new ApiInfoApi(defaultClient);
    String sectionId = "nodes"; // String | Id of the API section
    try {
      ApiSubInformations200Response result = apiInstance.apiSubInformations(sectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiInfoApi#apiSubInformations");
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
| **sectionId** | **String**| Id of the API section | |

### Return type

[**ApiSubInformations200Response**](ApiSubInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Endpoint information |  -  |

