# RfeApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRfe**](RfeApi.md#getRfe) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes/{rfe_id} | Get a specific Rfe |
| [**getRfeList**](RfeApi.md#getRfeList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes | List the RFES |
| [**postRfe**](RfeApi.md#postRfe) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/rfes | Create a RFE |


<a id="getRfe"></a>
# **getRfe**
> RfeExpandVO getRfe(workgroupId, projectId, rfeId)

Get a specific Rfe

Get a specific Rfe

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RfeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    RfeApi apiInstance = new RfeApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String rfeId = "rfeId_example"; // String | 
    try {
      RfeExpandVO result = apiInstance.getRfe(workgroupId, projectId, rfeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfeApi#getRfe");
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
| **rfeId** | **String**|  | |

### Return type

[**RfeExpandVO**](RfeExpandVO.md)

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

<a id="getRfeList"></a>
# **getRfeList**
> RfeListVO getRfeList(workgroupId, projectId)

List the RFES

List the RFES

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RfeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    RfeApi apiInstance = new RfeApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      RfeListVO result = apiInstance.getRfeList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfeApi#getRfeList");
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

[**RfeListVO**](RfeListVO.md)

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

<a id="postRfe"></a>
# **postRfe**
> RfqVO postRfe(workgroupId, projectId, rfePO)

Create a RFE

Create a RFE

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RfeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    RfeApi apiInstance = new RfeApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    RfePO rfePO = new RfePO(); // RfePO | 
    try {
      RfqVO result = apiInstance.postRfe(workgroupId, projectId, rfePO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RfeApi#postRfe");
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
| **rfePO** | [**RfePO**](RfePO.md)|  | [optional] |

### Return type

[**RfqVO**](RfqVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful update |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

