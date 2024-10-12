# ExchangeRateApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExchangeRateList**](ExchangeRateApi.md#getExchangeRateList) | **GET** /v1/workgroups/{workgroup_id}/exchangeRate | Get Exchange Rate List |
| [**postExchangeRate**](ExchangeRateApi.md#postExchangeRate) | **POST** /v1/workgroups/{workgroup_id}/exchangeRate | Create Exchange Rates |


<a id="getExchangeRateList"></a>
# **getExchangeRateList**
> MultiExchangeRateListVO getExchangeRateList(workgroupId)

Get Exchange Rate List

Get Exchange Rate List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExchangeRateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ExchangeRateApi apiInstance = new ExchangeRateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      MultiExchangeRateListVO result = apiInstance.getExchangeRateList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExchangeRateApi#getExchangeRateList");
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
| **workgroupId** | **String**|  | |

### Return type

[**MultiExchangeRateListVO**](MultiExchangeRateListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="postExchangeRate"></a>
# **postExchangeRate**
> Object postExchangeRate(workgroupId, multiExchangeRatePersistListVO)

Create Exchange Rates

Create Exchange Rates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExchangeRateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ExchangeRateApi apiInstance = new ExchangeRateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    MultiExchangeRatePersistListVO multiExchangeRatePersistListVO = new MultiExchangeRatePersistListVO(); // MultiExchangeRatePersistListVO | 
    try {
      Object result = apiInstance.postExchangeRate(workgroupId, multiExchangeRatePersistListVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExchangeRateApi#postExchangeRate");
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
| **workgroupId** | **String**|  | |
| **multiExchangeRatePersistListVO** | [**MultiExchangeRatePersistListVO**](MultiExchangeRatePersistListVO.md)|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

