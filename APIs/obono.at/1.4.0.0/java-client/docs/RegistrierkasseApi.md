# RegistrierkasseApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDEP**](RegistrierkasseApi.md#getDEP) | **GET** /registrierkassen/{registrierkasseUuid}/dep |  |
| [**getRegistrierkasse**](RegistrierkasseApi.md#getRegistrierkasse) | **GET** /registrierkassen/{registrierkasseUuid} |  |


<a id="getDEP"></a>
# **getDEP**
> getDEP(registrierkasseUuid)



Generates a DEP file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrierkasseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    RegistrierkasseApi apiInstance = new RegistrierkasseApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse` to retrieve the DEP file.
    try {
      apiInstance.getDEP(registrierkasseUuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrierkasseApi#getDEP");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; to retrieve the DEP file. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The DEP file. |  -  |

<a id="getRegistrierkasse"></a>
# **getRegistrierkasse**
> Registrierkasse getRegistrierkasse(registrierkasseUuid)



Returns information about a particular &#x60;Registrierkasse&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrierkasseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    RegistrierkasseApi apiInstance = new RegistrierkasseApi(defaultClient);
    String registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of a particular `Registrierkasse` to fetch.
    try {
      Registrierkasse result = apiInstance.getRegistrierkasse(registrierkasseUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrierkasseApi#getRegistrierkasse");
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
| **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of a particular &#x60;Registrierkasse&#x60; to fetch. | |

### Return type

[**Registrierkasse**](Registrierkasse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about a particular &#x60;Registrierkasse&#x60;. |  -  |
| **404** | This particular &#x60;Registrierkasse&#x60; does not exist. |  -  |

