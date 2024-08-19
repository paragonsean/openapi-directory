# BabelFeeControllerApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkForNotifications**](BabelFeeControllerApi.md#checkForNotifications) | **GET** /mosaik/babelfee/notificationcheck |  |
| [**ergoPayCreateBabelBox1**](BabelFeeControllerApi.md#ergoPayCreateBabelBox1) | **GET** /cancelbabel/{boxId} |  |
| [**getBabelFeeOverview**](BabelFeeControllerApi.md#getBabelFeeOverview) | **GET** /mosaik/babelfee/ |  |


<a id="checkForNotifications"></a>
# **checkForNotifications**
> NotificationCheckResponse checkForNotifications()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeControllerApi apiInstance = new BabelFeeControllerApi(defaultClient);
    try {
      NotificationCheckResponse result = apiInstance.checkForNotifications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeControllerApi#checkForNotifications");
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

[**NotificationCheckResponse**](NotificationCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="ergoPayCreateBabelBox1"></a>
# **ergoPayCreateBabelBox1**
> ErgoPayResponse ergoPayCreateBabelBox1(boxId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeControllerApi apiInstance = new BabelFeeControllerApi(defaultClient);
    String boxId = "boxId_example"; // String | 
    try {
      ErgoPayResponse result = apiInstance.ergoPayCreateBabelBox1(boxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeControllerApi#ergoPayCreateBabelBox1");
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
| **boxId** | **String**|  | |

### Return type

[**ErgoPayResponse**](ErgoPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="getBabelFeeOverview"></a>
# **getBabelFeeOverview**
> MosaikApp getBabelFeeOverview()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BabelFeeControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BabelFeeControllerApi apiInstance = new BabelFeeControllerApi(defaultClient);
    try {
      MosaikApp result = apiInstance.getBabelFeeOverview();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BabelFeeControllerApi#getBabelFeeOverview");
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

[**MosaikApp**](MosaikApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

