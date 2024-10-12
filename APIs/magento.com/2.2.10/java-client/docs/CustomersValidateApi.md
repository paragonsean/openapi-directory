# CustomersValidateApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerAccountManagementV1ValidatePut**](CustomersValidateApi.md#customerAccountManagementV1ValidatePut) | **PUT** /V1/customers/validate | customers/validate |


<a id="customerAccountManagementV1ValidatePut"></a>
# **customerAccountManagementV1ValidatePut**
> CustomerDataValidationResultsInterface customerAccountManagementV1ValidatePut(customerAccountManagementV1ValidatePutRequest)

customers/validate

Validate customer data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomersValidateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CustomersValidateApi apiInstance = new CustomersValidateApi(defaultClient);
    CustomerAccountManagementV1ValidatePutRequest customerAccountManagementV1ValidatePutRequest = new CustomerAccountManagementV1ValidatePutRequest(); // CustomerAccountManagementV1ValidatePutRequest | 
    try {
      CustomerDataValidationResultsInterface result = apiInstance.customerAccountManagementV1ValidatePut(customerAccountManagementV1ValidatePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomersValidateApi#customerAccountManagementV1ValidatePut");
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
| **customerAccountManagementV1ValidatePutRequest** | [**CustomerAccountManagementV1ValidatePutRequest**](CustomerAccountManagementV1ValidatePutRequest.md)|  | [optional] |

### Return type

[**CustomerDataValidationResultsInterface**](CustomerDataValidationResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

