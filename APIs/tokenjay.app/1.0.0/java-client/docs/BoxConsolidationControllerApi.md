# BoxConsolidationControllerApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**epConsolidate**](BoxConsolidationControllerApi.md#epConsolidate) | **GET** /mosaik/boxconsolidation/consolidate/{p2pkaddress} |  |
| [**mainApp1**](BoxConsolidationControllerApi.md#mainApp1) | **GET** /mosaik/boxconsolidation/ |  |


<a id="epConsolidate"></a>
# **epConsolidate**
> ErgoPayResponse epConsolidate(p2pkaddress)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxConsolidationControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BoxConsolidationControllerApi apiInstance = new BoxConsolidationControllerApi(defaultClient);
    String p2pkaddress = "p2pkaddress_example"; // String | 
    try {
      ErgoPayResponse result = apiInstance.epConsolidate(p2pkaddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxConsolidationControllerApi#epConsolidate");
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
| **p2pkaddress** | **String**|  | |

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

<a id="mainApp1"></a>
# **mainApp1**
> MosaikApp mainApp1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxConsolidationControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    BoxConsolidationControllerApi apiInstance = new BoxConsolidationControllerApi(defaultClient);
    try {
      MosaikApp result = apiInstance.mainApp1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxConsolidationControllerApi#mainApp1");
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

