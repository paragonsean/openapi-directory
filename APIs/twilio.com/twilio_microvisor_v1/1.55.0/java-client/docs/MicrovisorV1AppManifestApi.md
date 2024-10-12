# MicrovisorV1AppManifestApi

All URIs are relative to *https://microvisor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAppManifest**](MicrovisorV1AppManifestApi.md#fetchAppManifest) | **GET** /v1/Apps/{AppSid}/Manifest |  |


<a id="fetchAppManifest"></a>
# **fetchAppManifest**
> MicrovisorV1AppAppManifest fetchAppManifest(appSid)



Retrieve the Manifest for an App.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MicrovisorV1AppManifestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://microvisor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MicrovisorV1AppManifestApi apiInstance = new MicrovisorV1AppManifestApi(defaultClient);
    String appSid = "appSid_example"; // String | A 34-character string that uniquely identifies this App.
    try {
      MicrovisorV1AppAppManifest result = apiInstance.fetchAppManifest(appSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MicrovisorV1AppManifestApi#fetchAppManifest");
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
| **appSid** | **String**| A 34-character string that uniquely identifies this App. | |

### Return type

[**MicrovisorV1AppAppManifest**](MicrovisorV1AppAppManifest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

