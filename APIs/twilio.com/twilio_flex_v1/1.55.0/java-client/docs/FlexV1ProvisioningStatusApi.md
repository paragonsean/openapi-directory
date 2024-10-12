# FlexV1ProvisioningStatusApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchProvisioningStatus**](FlexV1ProvisioningStatusApi.md#fetchProvisioningStatus) | **GET** /v1/account/provision/status |  |


<a id="fetchProvisioningStatus"></a>
# **fetchProvisioningStatus**
> FlexV1ProvisioningStatus fetchProvisioningStatus()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ProvisioningStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ProvisioningStatusApi apiInstance = new FlexV1ProvisioningStatusApi(defaultClient);
    try {
      FlexV1ProvisioningStatus result = apiInstance.fetchProvisioningStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ProvisioningStatusApi#fetchProvisioningStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FlexV1ProvisioningStatus**](FlexV1ProvisioningStatus.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

