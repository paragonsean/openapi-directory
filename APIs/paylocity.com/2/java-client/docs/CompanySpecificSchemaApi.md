# CompanySpecificSchemaApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompanySpecificOpenAPIDocumentation**](CompanySpecificSchemaApi.md#getCompanySpecificOpenAPIDocumentation) | **GET** /v2/companies/{companyId}/openapi | Get Company-Specific Open API Documentation |


<a id="getCompanySpecificOpenAPIDocumentation"></a>
# **getCompanySpecificOpenAPIDocumentation**
> getCompanySpecificOpenAPIDocumentation(authorization, companyId)

Get Company-Specific Open API Documentation

The company-specific Open API endpoint allows the client to GET an Open API document for the Paylocity API that is customized with company-specific resource schemas. These customized resource schemas define certain properties as enumerations of pre-defined values that correspond to the company&#39;s setup with Web Pay. The customized schemas also indicate which properties are required by the company within Web Pay.&lt;br  /&gt;To learn more about Open API, click [here](https://www.openapis.org/)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanySpecificSchemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    CompanySpecificSchemaApi apiInstance = new CompanySpecificSchemaApi(defaultClient);
    String authorization = "authorization_example"; // String | Bearer + JWT
    String companyId = "companyId_example"; // String | Company Id
    try {
      apiInstance.getCompanySpecificOpenAPIDocumentation(authorization, companyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanySpecificSchemaApi#getCompanySpecificOpenAPIDocumentation");
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
| **authorization** | **String**| Bearer + JWT | |
| **companyId** | **String**| Company Id | |

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

