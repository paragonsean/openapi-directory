# ReturnsIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaRmaManagementV1SaveRmaPut**](ReturnsIdApi.md#rmaRmaManagementV1SaveRmaPut) | **PUT** /V1/returns/{id} | returns/{id} |
| [**rmaRmaRepositoryV1DeleteDelete**](ReturnsIdApi.md#rmaRmaRepositoryV1DeleteDelete) | **DELETE** /V1/returns/{id} | returns/{id} |
| [**rmaRmaRepositoryV1GetGet**](ReturnsIdApi.md#rmaRmaRepositoryV1GetGet) | **GET** /V1/returns/{id} | returns/{id} |


<a id="rmaRmaManagementV1SaveRmaPut"></a>
# **rmaRmaManagementV1SaveRmaPut**
> RmaDataRmaInterface rmaRmaManagementV1SaveRmaPut(id, rmaRmaManagementV1SaveRmaPostRequest)

returns/{id}

Save RMA

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdApi apiInstance = new ReturnsIdApi(defaultClient);
    String id = "id_example"; // String | 
    RmaRmaManagementV1SaveRmaPostRequest rmaRmaManagementV1SaveRmaPostRequest = new RmaRmaManagementV1SaveRmaPostRequest(); // RmaRmaManagementV1SaveRmaPostRequest | 
    try {
      RmaDataRmaInterface result = apiInstance.rmaRmaManagementV1SaveRmaPut(id, rmaRmaManagementV1SaveRmaPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdApi#rmaRmaManagementV1SaveRmaPut");
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
| **id** | **String**|  | |
| **rmaRmaManagementV1SaveRmaPostRequest** | [**RmaRmaManagementV1SaveRmaPostRequest**](RmaRmaManagementV1SaveRmaPostRequest.md)|  | [optional] |

### Return type

[**RmaDataRmaInterface**](RmaDataRmaInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="rmaRmaRepositoryV1DeleteDelete"></a>
# **rmaRmaRepositoryV1DeleteDelete**
> Boolean rmaRmaRepositoryV1DeleteDelete(id, rmaRmaManagementV1SaveRmaPostRequest)

returns/{id}

Delete RMA

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdApi apiInstance = new ReturnsIdApi(defaultClient);
    String id = "id_example"; // String | 
    RmaRmaManagementV1SaveRmaPostRequest rmaRmaManagementV1SaveRmaPostRequest = new RmaRmaManagementV1SaveRmaPostRequest(); // RmaRmaManagementV1SaveRmaPostRequest | 
    try {
      Boolean result = apiInstance.rmaRmaRepositoryV1DeleteDelete(id, rmaRmaManagementV1SaveRmaPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdApi#rmaRmaRepositoryV1DeleteDelete");
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
| **id** | **String**|  | |
| **rmaRmaManagementV1SaveRmaPostRequest** | [**RmaRmaManagementV1SaveRmaPostRequest**](RmaRmaManagementV1SaveRmaPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="rmaRmaRepositoryV1GetGet"></a>
# **rmaRmaRepositoryV1GetGet**
> RmaDataRmaInterface rmaRmaRepositoryV1GetGet(id)

returns/{id}

Return data object for specified RMA id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdApi apiInstance = new ReturnsIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      RmaDataRmaInterface result = apiInstance.rmaRmaRepositoryV1GetGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdApi#rmaRmaRepositoryV1GetGet");
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
| **id** | **Integer**|  | |

### Return type

[**RmaDataRmaInterface**](RmaDataRmaInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

