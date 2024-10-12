# BranchControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2Tier1ShortNameBranchBranchesBranchIDGet**](BranchControllerApi.md#v2Tier1ShortNameBranchBranchesBranchIDGet) | **GET** /v2/tier1/{shortName}/branch/branches/{branchID} | Get a specific branch given its unique Object ID (OID) |
| [**v2Tier1ShortNameBranchBranchesGet**](BranchControllerApi.md#v2Tier1ShortNameBranchBranchesGet) | **GET** /v2/tier1/{shortName}/branch/branches | All branches defined for a company |


<a id="v2Tier1ShortNameBranchBranchesBranchIDGet"></a>
# **v2Tier1ShortNameBranchBranchesBranchIDGet**
> BranchModel v2Tier1ShortNameBranchBranchesBranchIDGet(shortName, branchID)

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
      BranchModel result = apiInstance.v2Tier1ShortNameBranchBranchesBranchIDGet(shortName, branchID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchControllerApi#v2Tier1ShortNameBranchBranchesBranchIDGet");
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
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameBranchBranchesGet"></a>
# **v2Tier1ShortNameBranchBranchesGet**
> BranchModelResults v2Tier1ShortNameBranchBranchesGet(shortName, offset, count)

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
      BranchModelResults result = apiInstance.v2Tier1ShortNameBranchBranchesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BranchControllerApi#v2Tier1ShortNameBranchBranchesGet");
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
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

