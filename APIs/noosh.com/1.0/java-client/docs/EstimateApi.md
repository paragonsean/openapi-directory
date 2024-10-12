# EstimateApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEstimate**](EstimateApi.md#getEstimate) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates/{estimate_id} | Get a specific estimate of project |
| [**getEstimateList**](EstimateApi.md#getEstimateList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates | List the Estimates |
| [**postEstimate**](EstimateApi.md#postEstimate) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/estimates | Create a Estimate |


<a id="getEstimate"></a>
# **getEstimate**
> EstimateExpandVO getEstimate(workgroupId, projectId, estimateId)

Get a specific estimate of project

Get a specific estimate of project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String estimateId = "estimateId_example"; // String | 
    try {
      EstimateExpandVO result = apiInstance.getEstimate(workgroupId, projectId, estimateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#getEstimate");
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
| **estimateId** | **String**|  | |

### Return type

[**EstimateExpandVO**](EstimateExpandVO.md)

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

<a id="getEstimateList"></a>
# **getEstimateList**
> EstimateListExpandVO getEstimateList(workgroupId, projectId)

List the Estimates

List the Estimates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      EstimateListExpandVO result = apiInstance.getEstimateList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#getEstimateList");
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

[**EstimateListExpandVO**](EstimateListExpandVO.md)

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

<a id="postEstimate"></a>
# **postEstimate**
> EstimatePO postEstimate(workgroupId, projectId, estimatePO)

Create a Estimate

Create a Estimate

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    EstimateApi apiInstance = new EstimateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    EstimatePO estimatePO = new EstimatePO(); // EstimatePO | 
    try {
      EstimatePO result = apiInstance.postEstimate(workgroupId, projectId, estimatePO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EstimateApi#postEstimate");
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
| **estimatePO** | [**EstimatePO**](EstimatePO.md)|  | [optional] |

### Return type

[**EstimatePO**](EstimatePO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful create |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

