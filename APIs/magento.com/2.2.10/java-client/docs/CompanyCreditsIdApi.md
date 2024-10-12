# CompanyCreditsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditLimitRepositoryV1SavePut**](CompanyCreditsIdApi.md#companyCreditCreditLimitRepositoryV1SavePut) | **PUT** /V1/companyCredits/{id} | companyCredits/{id} |


<a id="companyCreditCreditLimitRepositoryV1SavePut"></a>
# **companyCreditCreditLimitRepositoryV1SavePut**
> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitRepositoryV1SavePut(id, companyCreditCreditLimitRepositoryV1SavePutRequest)

companyCredits/{id}

Update the following company credit attributes: credit currency, credit limit and setting to exceed credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsIdApi apiInstance = new CompanyCreditsIdApi(defaultClient);
    String id = "id_example"; // String | 
    CompanyCreditCreditLimitRepositoryV1SavePutRequest companyCreditCreditLimitRepositoryV1SavePutRequest = new CompanyCreditCreditLimitRepositoryV1SavePutRequest(); // CompanyCreditCreditLimitRepositoryV1SavePutRequest | 
    try {
      CompanyCreditDataCreditLimitInterface result = apiInstance.companyCreditCreditLimitRepositoryV1SavePut(id, companyCreditCreditLimitRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsIdApi#companyCreditCreditLimitRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **companyCreditCreditLimitRepositoryV1SavePutRequest** | [**CompanyCreditCreditLimitRepositoryV1SavePutRequest**](CompanyCreditCreditLimitRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**CompanyCreditDataCreditLimitInterface**](CompanyCreditDataCreditLimitInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

