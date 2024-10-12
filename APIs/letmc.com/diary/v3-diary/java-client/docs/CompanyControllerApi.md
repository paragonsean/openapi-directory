# CompanyControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companyControllerGetBranches**](CompanyControllerApi.md#companyControllerGetBranches) | **GET** /v3/diary/{shortName}/company/branches | All branches defined for a company |
| [**v3DiaryShortNameCompanyBranchesBranchIDGet**](CompanyControllerApi.md#v3DiaryShortNameCompanyBranchesBranchIDGet) | **GET** /v3/diary/{shortName}/company/branches/{branchID} | Get a specific branch given its unique Object ID (OID) |


<a id="companyControllerGetBranches"></a>
# **companyControllerGetBranches**
> AdvertisingBranchModelResults companyControllerGetBranches(shortName, offset, count)

All branches defined for a company

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
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      AdvertisingBranchModelResults result = apiInstance.companyControllerGetBranches(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyControllerApi#companyControllerGetBranches");
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
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**AdvertisingBranchModelResults**](AdvertisingBranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v3DiaryShortNameCompanyBranchesBranchIDGet"></a>
# **v3DiaryShortNameCompanyBranchesBranchIDGet**
> AdvertisingBranchModel v3DiaryShortNameCompanyBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

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
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    try {
      AdvertisingBranchModel result = apiInstance.v3DiaryShortNameCompanyBranchesBranchIDGet(shortName, branchID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyControllerApi#v3DiaryShortNameCompanyBranchesBranchIDGet");
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
| **branchID** | **String**| The unique ID of the Branch | |

### Return type

[**AdvertisingBranchModel**](AdvertisingBranchModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

