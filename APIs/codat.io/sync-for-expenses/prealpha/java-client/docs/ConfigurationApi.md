# ConfigurationApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompanyConfiguration**](ConfigurationApi.md#getCompanyConfiguration) | **GET** /companies/{companyId}/sync/expenses/config | Get company configuration |
| [**saveCompanyConfiguration**](ConfigurationApi.md#saveCompanyConfiguration) | **POST** /companies/{companyId}/sync/expenses/config | Set company configuration |


<a id="getCompanyConfiguration"></a>
# **getCompanyConfiguration**
> CompanyConfiguration getCompanyConfiguration(companyId)

Get company configuration

Gets a companies expense sync configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    try {
      CompanyConfiguration result = apiInstance.getCompanyConfiguration(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#getCompanyConfiguration");
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
| **companyId** | **UUID**|  | |

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="saveCompanyConfiguration"></a>
# **saveCompanyConfiguration**
> CompanyConfiguration saveCompanyConfiguration(companyId, companyConfiguration)

Set company configuration

Sets a companies expense sync configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    CompanyConfiguration companyConfiguration = new CompanyConfiguration(); // CompanyConfiguration | 
    try {
      CompanyConfiguration result = apiInstance.saveCompanyConfiguration(companyId, companyConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#saveCompanyConfiguration");
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
| **companyId** | **UUID**|  | |
| **companyConfiguration** | [**CompanyConfiguration**](CompanyConfiguration.md)|  | [optional] |

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

