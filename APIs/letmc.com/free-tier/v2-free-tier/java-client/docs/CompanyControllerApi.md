# CompanyControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyControllerGetCompany**](CompanyControllerApi.md#companyControllerGetCompany) | **GET** /v2/tier1/{shortName}/company | Information about a specific company |


<a id="companyControllerGetCompany"></a>
# **companyControllerGetCompany**
> CompanyModel companyControllerGetCompany(shortName)

Information about a specific company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    CompanyControllerApi apiInstance = new CompanyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    try {
      CompanyModel result = apiInstance.companyControllerGetCompany(shortName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyControllerApi#companyControllerGetCompany");
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
| **shortName** | **String**| The unique client short-name | |

### Return type

[**CompanyModel**](CompanyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

