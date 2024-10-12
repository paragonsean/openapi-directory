# NumbersV2ReplaceItemsApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createReplaceItems**](NumbersV2ReplaceItemsApi.md#createReplaceItems) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/ReplaceItems |  |


<a id="createReplaceItems"></a>
# **createReplaceItems**
> NumbersV2RegulatoryComplianceBundleReplaceItems createReplaceItems(bundleSid, fromBundleSid)



Replaces all bundle items in the target bundle (specified in the path) with all the bundle items of the source bundle (specified by the from_bundle_sid body param)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2ReplaceItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2ReplaceItemsApi apiInstance = new NumbersV2ReplaceItemsApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle where the item assignments are going to be replaced.
    String fromBundleSid = "fromBundleSid_example"; // String | The source bundle sid to copy the item assignments from.
    try {
      NumbersV2RegulatoryComplianceBundleReplaceItems result = apiInstance.createReplaceItems(bundleSid, fromBundleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2ReplaceItemsApi#createReplaceItems");
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
| **bundleSid** | **String**| The unique string that identifies the Bundle where the item assignments are going to be replaced. | |
| **fromBundleSid** | **String**| The source bundle sid to copy the item assignments from. | |

### Return type

[**NumbersV2RegulatoryComplianceBundleReplaceItems**](NumbersV2RegulatoryComplianceBundleReplaceItems.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

