# CustomFieldsApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllCustomFieldsByCategory**](CustomFieldsApi.md#getAllCustomFieldsByCategory) | **GET** /v2/companies/{companyId}/customfields/{category} | Get All Custom Fields |


<a id="getAllCustomFieldsByCategory"></a>
# **getAllCustomFieldsByCategory**
> List&lt;CustomFieldDefinition&gt; getAllCustomFieldsByCategory(companyId, category)

Get All Custom Fields

Get All Custom Fields for the selected company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String category = "category_example"; // String | Custom Fields Category
    try {
      List<CustomFieldDefinition> result = apiInstance.getAllCustomFieldsByCategory(companyId, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#getAllCustomFieldsByCategory");
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
| **category** | **String**| Custom Fields Category | |

### Return type

[**List&lt;CustomFieldDefinition&gt;**](CustomFieldDefinition.md)

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
| **404** | Invalid Category |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

