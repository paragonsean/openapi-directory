# SupersimV1BillingPeriodApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listBillingPeriod**](SupersimV1BillingPeriodApi.md#listBillingPeriod) | **GET** /v1/Sims/{SimSid}/BillingPeriods |  |


<a id="listBillingPeriod"></a>
# **listBillingPeriod**
> ListBillingPeriodResponse listBillingPeriod(simSid, pageSize, page, pageToken)



Retrieve a list of Billing Periods for a Super SIM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1BillingPeriodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1BillingPeriodApi apiInstance = new SupersimV1BillingPeriodApi(defaultClient);
    String simSid = "simSid_example"; // String | The SID of the Super SIM to list Billing Periods for.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBillingPeriodResponse result = apiInstance.listBillingPeriod(simSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1BillingPeriodApi#listBillingPeriod");
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
| **simSid** | **String**| The SID of the Super SIM to list Billing Periods for. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBillingPeriodResponse**](ListBillingPeriodResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

