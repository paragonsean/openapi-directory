# CompanyCreditsCompanyCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet**](CompanyCreditsCompanyCompanyIdApi.md#companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet) | **GET** /V1/companyCredits/company/{companyId} | companyCredits/company/{companyId} |


<a id="companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet"></a>
# **companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet**
> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet(companyId)

companyCredits/company/{companyId}

Returns data on the credit limit for a specified company.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsCompanyCompanyIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsCompanyCompanyIdApi apiInstance = new CompanyCreditsCompanyCompanyIdApi(defaultClient);
    Integer companyId = 56; // Integer | 
    try {
      CompanyCreditDataCreditLimitInterface result = apiInstance.companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsCompanyCompanyIdApi#companyCreditCreditLimitManagementV1GetCreditByCompanyIdGet");
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
| **companyId** | **Integer**|  | |

### Return type

[**CompanyCreditDataCreditLimitInterface**](CompanyCreditDataCreditLimitInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

