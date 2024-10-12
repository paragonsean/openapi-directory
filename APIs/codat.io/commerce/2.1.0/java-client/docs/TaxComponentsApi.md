# TaxComponentsApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getTaxComponents**](TaxComponentsApi.md#getTaxComponents) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-taxComponents | List tax components |


<a id="getTaxComponents"></a>
# **getTaxComponents**
> TaxComponents getTaxComponents(companyId, connectionId)

List tax components

This endpoint returns a lits of tax rates from the commerce platform, including tax rate names and values. This supports the mapping of tax rates from the commerce platform to the accounting platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxComponentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    TaxComponentsApi apiInstance = new TaxComponentsApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    UUID connectionId = UUID.fromString("2e9d2c44-f675-40ba-8049-353bfcb5e171"); // UUID | 
    try {
      TaxComponents result = apiInstance.getTaxComponents(companyId, connectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxComponentsApi#getTaxComponents");
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

[**TaxComponents**](TaxComponents.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

