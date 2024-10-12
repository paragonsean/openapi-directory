# CustomerAlertsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStoreAlerts**](CustomerAlertsApi.md#getStoreAlerts) | **GET** /v2/user/customer/stores/{storeId}/alerts | Get store&#39;s alerts |
| [**saveStoreAlerts**](CustomerAlertsApi.md#saveStoreAlerts) | **POST** /v2/user/customer/stores/{storeId}/alerts | Save store alerts |


<a id="getStoreAlerts"></a>
# **getStoreAlerts**
> StoreAlerts getStoreAlerts(storeId, ifNoneMatch)

Get store&#39;s alerts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAlertsApi apiInstance = new CustomerAlertsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    try {
      StoreAlerts result = apiInstance.getStoreAlerts(storeId, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAlertsApi#getStoreAlerts");
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
| **storeId** | **String**| Your store identifier | |
| **ifNoneMatch** | **String**| ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  | [optional] |

### Return type

[**StoreAlerts**](StoreAlerts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User account alerts information |  -  |
| **304** | The ETag sent in the http header If-None-Match did not change. So you are up to date ! |  * ETag - The ETag value to identify the resource.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3  <br>  * Last-Modified - Last modification UTC date of the resource\\ For more details go to this link: https://tools.ietf.org/html/rfc7232#section-2.2  <br>  |
| **404** | Store not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveStoreAlerts"></a>
# **saveStoreAlerts**
> saveStoreAlerts(storeId, requestBody)

Save store alerts

You just have to send the alert you want to update, does not need all alerts. (PARTIAL UPDATE ACCEPTED)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAlertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CustomerAlertsApi apiInstance = new CustomerAlertsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    Map<String, SaveStoreAlertRequest> requestBody = new HashMap(); // Map<String, SaveStoreAlertRequest> | 
    try {
      apiInstance.saveStoreAlerts(storeId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAlertsApi#saveStoreAlerts");
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
| **storeId** | **String**| Your store identifier | |
| **requestBody** | [**Map&lt;String, SaveStoreAlertRequest&gt;**](SaveStoreAlertRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Store alerts saved |  -  |
| **400** | BadRequest |  -  |
| **404** | Store not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

