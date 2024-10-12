# BillingDetailsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBillingDetails**](BillingDetailsApi.md#getBillingDetails) | **GET** /restv2/game/{apiKey}/admin/billingDetails | Retrieves the Billing Details |
| [**putBillingDetails**](BillingDetailsApi.md#putBillingDetails) | **PUT** /restv2/game/{apiKey}/admin/billingDetails | Updates the Billing Details |


<a id="getBillingDetails"></a>
# **getBillingDetails**
> BillingDetailsModel getBillingDetails(apiKey)

Retrieves the Billing Details

Retrieves the Billing Details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    BillingDetailsApi apiInstance = new BillingDetailsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      BillingDetailsModel result = apiInstance.getBillingDetails(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingDetailsApi#getBillingDetails");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**BillingDetailsModel**](BillingDetailsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="putBillingDetails"></a>
# **putBillingDetails**
> BillingDetailsModel putBillingDetails(apiKey, billingDetailsModel)

Updates the Billing Details

Updates the Billing Details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    BillingDetailsApi apiInstance = new BillingDetailsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    BillingDetailsModel billingDetailsModel = new BillingDetailsModel(); // BillingDetailsModel | billingDetails
    try {
      BillingDetailsModel result = apiInstance.putBillingDetails(apiKey, billingDetailsModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingDetailsApi#putBillingDetails");
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
| **apiKey** | **String**| apiKey | |
| **billingDetailsModel** | [**BillingDetailsModel**](BillingDetailsModel.md)| billingDetails | |

### Return type

[**BillingDetailsModel**](BillingDetailsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

