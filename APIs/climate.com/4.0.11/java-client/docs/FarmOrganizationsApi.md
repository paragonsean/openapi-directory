# FarmOrganizationsApi

All URIs are relative to *https://platform.climate.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchFarmOrganizationByTypeAndId**](FarmOrganizationsApi.md#fetchFarmOrganizationByTypeAndId) | **GET** /v4/farmOrganizations/{farmOrganizationType}/{farmOrganizationId} | Retrieve a specific farm organization by organization type and ID |


<a id="fetchFarmOrganizationByTypeAndId"></a>
# **fetchFarmOrganizationByTypeAndId**
> FarmOrganization fetchFarmOrganizationByTypeAndId(farmOrganizationType, farmOrganizationId)

Retrieve a specific farm organization by organization type and ID

Retrieve a given **farm organization** by organization type and ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FarmOrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://platform.climate.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2_authorization_code
    OAuth oauth2_authorization_code = (OAuth) defaultClient.getAuthentication("oauth2_authorization_code");
    oauth2_authorization_code.setAccessToken("YOUR ACCESS TOKEN");

    FarmOrganizationsApi apiInstance = new FarmOrganizationsApi(defaultClient);
    String farmOrganizationType = "farm"; // String | Type of the farm organization.
    UUID farmOrganizationId = UUID.randomUUID(); // UUID | Unique identifier of the farm organization.
    try {
      FarmOrganization result = apiInstance.fetchFarmOrganizationByTypeAndId(farmOrganizationType, farmOrganizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FarmOrganizationsApi#fetchFarmOrganizationByTypeAndId");
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
| **farmOrganizationType** | **String**| Type of the farm organization. | [enum: farm] |
| **farmOrganizationId** | **UUID**| Unique identifier of the farm organization. | |

### Return type

[**FarmOrganization**](FarmOrganization.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested farm organization. |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **400** | Bad Input |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **401** | Unauthorized |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **403** | Forbidden |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **404** | Not Found |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **429** | Too Many Requests |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **500** | Internal Server Error |  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |
| **503** | Server Busy |  * Retry-After - Number of seconds to wait before retrying the request. <br>  * X-Http-Request-Id - Unique identifier assigned to the request. <br>  |

