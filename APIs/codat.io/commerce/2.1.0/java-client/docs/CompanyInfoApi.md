# CompanyInfoApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompanyInfo**](CompanyInfoApi.md#getCompanyInfo) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-info | Get company info |


<a id="getCompanyInfo"></a>
# **getCompanyInfo**
> CompanyInfo getCompanyInfo(companyId, connectionId)

Get company info

Retrieve information about the company, as seen in the commerce platform.  This may include information like addresses, tax registration details and social media or website information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    CompanyInfoApi apiInstance = new CompanyInfoApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    UUID connectionId = UUID.fromString("2e9d2c44-f675-40ba-8049-353bfcb5e171"); // UUID | 
    try {
      CompanyInfo result = apiInstance.getCompanyInfo(companyId, connectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyInfoApi#getCompanyInfo");
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
| **connectionId** | **UUID**|  | |

### Return type

[**CompanyInfo**](CompanyInfo.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

