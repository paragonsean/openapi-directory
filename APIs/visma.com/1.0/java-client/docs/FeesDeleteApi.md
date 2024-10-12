# FeesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flatRatesDeleteFlatRate**](FeesDeleteApi.md#flatRatesDeleteFlatRate) | **DELETE** /v1/flatrates/{guid} | Delete a flat rate of a phase. |
| [**projectFeesDeleteProjectFree**](FeesDeleteApi.md#projectFeesDeleteProjectFree) | **DELETE** /v1/projectfees/{guid} | Deletes a project fee. |
| [**projectRecurringFeeRulesDeleteProjectRecurringFeeRule**](FeesDeleteApi.md#projectRecurringFeeRulesDeleteProjectRecurringFeeRule) | **DELETE** /v1/projectrecurringfeerules/{guid} | Deletes a projectRecurringFeeRule. |


<a id="flatRatesDeleteFlatRate"></a>
# **flatRatesDeleteFlatRate**
> flatRatesDeleteFlatRate(guid)

Delete a flat rate of a phase.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesDeleteApi apiInstance = new FeesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID of flat rate.
    try {
      apiInstance.flatRatesDeleteFlatRate(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesDeleteApi#flatRatesDeleteFlatRate");
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
| **guid** | **String**| ID of flat rate. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesDeleteProjectFree"></a>
# **projectFeesDeleteProjectFree**
> projectFeesDeleteProjectFree(guid)

Deletes a project fee.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesDeleteApi apiInstance = new FeesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project fee.
    try {
      apiInstance.projectFeesDeleteProjectFree(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesDeleteApi#projectFeesDeleteProjectFree");
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
| **guid** | **String**| GUID used to delete the project fee. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesDeleteProjectRecurringFeeRule"></a>
# **projectRecurringFeeRulesDeleteProjectRecurringFeeRule**
> projectRecurringFeeRulesDeleteProjectRecurringFeeRule(guid)

Deletes a projectRecurringFeeRule.

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesDeleteApi apiInstance = new FeesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the project recurring fee rule.
    try {
      apiInstance.projectRecurringFeeRulesDeleteProjectRecurringFeeRule(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesDeleteApi#projectRecurringFeeRulesDeleteProjectRecurringFeeRule");
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
| **guid** | **String**| GUID used to delete the project recurring fee rule. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

