# RfqApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRfq**](RfqApi.md#getRfq) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs/{rfq_id} | Get a specific Rfq |
| [**getRfqList**](RfqApi.md#getRfqList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfqs | List the rfqs |


<a id="getRfq"></a>
# **getRfq**
> RfqExpandVO getRfq(workgroupId, projectId, rfqId)

Get a specific Rfq

Get a specific Rfq

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RfqApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    RfqApi apiInstance = new RfqApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String rfqId = "rfqId_example"; // String | 
    try {
      RfqExpandVO result = apiInstance.getRfq(workgroupId, projectId, rfqId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfqApi#getRfq");
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
| **projectId** | **String**|  | |
| **rfqId** | **String**|  | |

### Return type

[**RfqExpandVO**](RfqExpandVO.md)

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

<a id="getRfqList"></a>
# **getRfqList**
> RfqListVO getRfqList(workgroupId, projectId)

List the rfqs

List the rfqs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RfqApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    RfqApi apiInstance = new RfqApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      RfqListVO result = apiInstance.getRfqList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfqApi#getRfqList");
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
| **projectId** | **String**|  | |

### Return type

[**RfqListVO**](RfqListVO.md)

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

