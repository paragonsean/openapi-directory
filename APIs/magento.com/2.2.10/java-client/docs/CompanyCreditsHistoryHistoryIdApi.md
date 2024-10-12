# CompanyCreditsHistoryHistoryIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyCreditCreditHistoryManagementV1UpdatePut**](CompanyCreditsHistoryHistoryIdApi.md#companyCreditCreditHistoryManagementV1UpdatePut) | **PUT** /V1/companyCredits/history/{historyId} | companyCredits/history/{historyId} |


<a id="companyCreditCreditHistoryManagementV1UpdatePut"></a>
# **companyCreditCreditHistoryManagementV1UpdatePut**
> Boolean companyCreditCreditHistoryManagementV1UpdatePut(historyId, companyCreditCreditHistoryManagementV1UpdatePutRequest)

companyCredits/history/{historyId}

Update the PO Number and/or comment for a Reimburse transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyCreditsHistoryHistoryIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CompanyCreditsHistoryHistoryIdApi apiInstance = new CompanyCreditsHistoryHistoryIdApi(defaultClient);
    Integer historyId = 56; // Integer | 
    CompanyCreditCreditHistoryManagementV1UpdatePutRequest companyCreditCreditHistoryManagementV1UpdatePutRequest = new CompanyCreditCreditHistoryManagementV1UpdatePutRequest(); // CompanyCreditCreditHistoryManagementV1UpdatePutRequest | 
    try {
      Boolean result = apiInstance.companyCreditCreditHistoryManagementV1UpdatePut(historyId, companyCreditCreditHistoryManagementV1UpdatePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyCreditsHistoryHistoryIdApi#companyCreditCreditHistoryManagementV1UpdatePut");
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
| **historyId** | **Integer**|  | |
| **companyCreditCreditHistoryManagementV1UpdatePutRequest** | [**CompanyCreditCreditHistoryManagementV1UpdatePutRequest**](CompanyCreditCreditHistoryManagementV1UpdatePutRequest.md)|  | [optional] |

### Return type

**Boolean**

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
| **0** | Unexpected error |  -  |

