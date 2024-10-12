# CompanySettingsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompaySettingsList**](CompanySettingsApi.md#getCompaySettingsList) | **GET** /company_settings | Get a list of company settings |


<a id="getCompaySettingsList"></a>
# **getCompaySettingsList**
> GetCompaySettingsList200Response getCompaySettingsList(name, description)

Get a list of company settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompanySettingsApi apiInstance = new CompanySettingsApi(defaultClient);
    String name = "name_example"; // String | Filter by name
    String description = "description_example"; // String | Filter by description
    try {
      GetCompaySettingsList200Response result = apiInstance.getCompaySettingsList(name, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySettingsApi#getCompaySettingsList");
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
| **name** | **String**| Filter by name | [optional] |
| **description** | **String**| Filter by description | [optional] |

### Return type

[**GetCompaySettingsList200Response**](GetCompaySettingsList200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | IntegrationFeatureSetting not found |  -  |

