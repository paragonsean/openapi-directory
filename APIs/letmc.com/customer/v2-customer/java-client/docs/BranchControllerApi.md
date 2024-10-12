# BranchControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**branchControllerGetBranches**](BranchControllerApi.md#branchControllerGetBranches) | **GET** /v2/customer/{shortName}/branch/branches | All branches defined for a company |
| [**v2CustomerShortNameBranchBranchesBranchIDGet**](BranchControllerApi.md#v2CustomerShortNameBranchBranchesBranchIDGet) | **GET** /v2/customer/{shortName}/branch/branches/{branchID} | Get a specific branch given its unique Object ID (OID) |


<a id="branchControllerGetBranches"></a>
# **branchControllerGetBranches**
> BranchModelResults branchControllerGetBranches(shortName, offset, count)

All branches defined for a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    BranchControllerApi apiInstance = new BranchControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      BranchModelResults result = apiInstance.branchControllerGetBranches(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchControllerApi#branchControllerGetBranches");
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

[**BranchModelResults**](BranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2CustomerShortNameBranchBranchesBranchIDGet"></a>
# **v2CustomerShortNameBranchBranchesBranchIDGet**
> BranchModel v2CustomerShortNameBranchBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BranchControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    BranchControllerApi apiInstance = new BranchControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    try {
      BranchModel result = apiInstance.v2CustomerShortNameBranchBranchesBranchIDGet(shortName, branchID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchControllerApi#v2CustomerShortNameBranchBranchesBranchIDGet");
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

[**BranchModel**](BranchModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

