# CompanyCreditsCreditIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditLimitRepositoryV1GetGet**](CompanyCreditsCreditIdApi.md#companyCreditCreditLimitRepositoryV1GetGet) | **GET** /V1/companyCredits/{creditId} | companyCredits/{creditId} |


<a id="companyCreditCreditLimitRepositoryV1GetGet"></a>
# **companyCreditCreditLimitRepositoryV1GetGet**
> CompanyCreditDataCreditLimitInterface companyCreditCreditLimitRepositoryV1GetGet(creditId, reload)

companyCredits/{creditId}

Returns data on the credit limit for a specified credit limit ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsCreditIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsCreditIdApi apiInstance = new CompanyCreditsCreditIdApi(defaultClient);
    Integer creditId = 56; // Integer | 
    Boolean reload = true; // Boolean | [optional]
    try {
      CompanyCreditDataCreditLimitInterface result = apiInstance.companyCreditCreditLimitRepositoryV1GetGet(creditId, reload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsCreditIdApi#companyCreditCreditLimitRepositoryV1GetGet");
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
| **creditId** | **Integer**|  | |
| **reload** | **Boolean**| [optional] | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

