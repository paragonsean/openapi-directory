# CompanyCodesApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllCompanyCodesAndDescriptionsByResource**](CompanyCodesApi.md#getAllCompanyCodesAndDescriptionsByResource) | **GET** /v2/companies/{companyId}/codes/{codeResource} | Get All Company Codes |


<a id="getAllCompanyCodesAndDescriptionsByResource"></a>
# **getAllCompanyCodesAndDescriptionsByResource**
> List&lt;CompanyCodes&gt; getAllCompanyCodesAndDescriptionsByResource(companyId, codeResource)

Get All Company Codes

Get All Company Codes for the selected company and resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    CompanyCodesApi apiInstance = new CompanyCodesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String codeResource = "codeResource_example"; // String | Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions.
    try {
      List<CompanyCodes> result = apiInstance.getAllCompanyCodesAndDescriptionsByResource(companyId, codeResource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCodesApi#getAllCompanyCodesAndDescriptionsByResource");
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
| **companyId** | **String**| Company Id | |
| **codeResource** | **String**| Type of Company Code. Common values costcenter1, costcenter2, costcenter3, deductions, earnings, taxes, paygrade, positions. | |

### Return type

[**List&lt;CompanyCodes&gt;**](CompanyCodes.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Invalid Code Resource |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

