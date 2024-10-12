# NumbersV2BundleCopyApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBundleCopy**](NumbersV2BundleCopyApi.md#createBundleCopy) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies |  |
| [**listBundleCopy**](NumbersV2BundleCopyApi.md#listBundleCopy) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Copies |  |


<a id="createBundleCopy"></a>
# **createBundleCopy**
> NumbersV2RegulatoryComplianceBundleBundleCopy createBundleCopy(bundleSid, friendlyName)



Creates a new copy of a Bundle. It will internally create copies of all the bundle items (identities and documents) of the original bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleCopyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleCopyApi apiInstance = new NumbersV2BundleCopyApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle to be copied.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the copied bundle.
    try {
      NumbersV2RegulatoryComplianceBundleBundleCopy result = apiInstance.createBundleCopy(bundleSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleCopyApi#createBundleCopy");
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
| **bundleSid** | **String**| The unique string that identifies the Bundle to be copied. | |
| **friendlyName** | **String**| The string that you assigned to describe the copied bundle. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceBundleBundleCopy**](NumbersV2RegulatoryComplianceBundleBundleCopy.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listBundleCopy"></a>
# **listBundleCopy**
> ListBundleCopyResponse listBundleCopy(bundleSid, pageSize, page, pageToken)



Retrieve a list of all Bundles Copies for a Bundle.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2BundleCopyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2BundleCopyApi apiInstance = new NumbersV2BundleCopyApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBundleCopyResponse result = apiInstance.listBundleCopy(bundleSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2BundleCopyApi#listBundleCopy");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBundleCopyResponse**](ListBundleCopyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

