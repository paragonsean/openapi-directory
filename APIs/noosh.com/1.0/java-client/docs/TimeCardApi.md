# TimeCardApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMyTimeCard**](TimeCardApi.md#getMyTimeCard) | **GET** /v1/workgroups/{workgroup_id}/myTimeCards/{timeCard_id} | Get a specific my time cards |
| [**getMyTimeCardList**](TimeCardApi.md#getMyTimeCardList) | **GET** /v1/workgroups/{workgroup_id}/myTimeCards | List my time cards |
| [**getReceivedTimeCard**](TimeCardApi.md#getReceivedTimeCard) | **GET** /v1/workgroups/{workgroup_id}/receivedTimeCards/{timeCard_id} | List a specific received time cards |
| [**getReceivedTimeCardList**](TimeCardApi.md#getReceivedTimeCardList) | **GET** /v1/workgroups/{workgroup_id}/receivedTimeCards | List received time cards |


<a id="getMyTimeCard"></a>
# **getMyTimeCard**
> TimeCardDetailVO getMyTimeCard(workgroupId, timeCardId)

Get a specific my time cards

Get a specific my time cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeCardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TimeCardApi apiInstance = new TimeCardApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String timeCardId = "timeCardId_example"; // String | 
    try {
      TimeCardDetailVO result = apiInstance.getMyTimeCard(workgroupId, timeCardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeCardApi#getMyTimeCard");
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
| **timeCardId** | **String**|  | |

### Return type

[**TimeCardDetailVO**](TimeCardDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getMyTimeCardList"></a>
# **getMyTimeCardList**
> TimeCardListVO getMyTimeCardList(workgroupId)

List my time cards

List my time cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeCardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TimeCardApi apiInstance = new TimeCardApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TimeCardListVO result = apiInstance.getMyTimeCardList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeCardApi#getMyTimeCardList");
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

[**TimeCardListVO**](TimeCardListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getReceivedTimeCard"></a>
# **getReceivedTimeCard**
> TimeCardReceivedDetailVO getReceivedTimeCard(workgroupId, timeCardId)

List a specific received time cards

List a specific received time cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeCardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TimeCardApi apiInstance = new TimeCardApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String timeCardId = "timeCardId_example"; // String | 
    try {
      TimeCardReceivedDetailVO result = apiInstance.getReceivedTimeCard(workgroupId, timeCardId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeCardApi#getReceivedTimeCard");
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
| **timeCardId** | **String**|  | |

### Return type

[**TimeCardReceivedDetailVO**](TimeCardReceivedDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getReceivedTimeCardList"></a>
# **getReceivedTimeCardList**
> TimeCardListVO getReceivedTimeCardList(workgroupId)

List received time cards

List received time cards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeCardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    TimeCardApi apiInstance = new TimeCardApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TimeCardListVO result = apiInstance.getReceivedTimeCardList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeCardApi#getReceivedTimeCardList");
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

[**TimeCardListVO**](TimeCardListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

