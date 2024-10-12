# SpecTemplateApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSpecTemplate**](SpecTemplateApi.md#getSpecTemplate) | **GET** /v1/workgroups/{workgroup_id}/specTemplates/{spec_template_id} | Get a specific Spec Template |
| [**getSpecTemplateList**](SpecTemplateApi.md#getSpecTemplateList) | **GET** /v1/workgroups/{workgroup_id}/specTemplates | List Spec Templates of Workgroup Level  |


<a id="getSpecTemplate"></a>
# **getSpecTemplate**
> SpecTemplateExpandVO getSpecTemplate(workgroupId, specTemplateId)

Get a specific Spec Template

Get a specific Spec Template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecTemplateApi apiInstance = new SpecTemplateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String specTemplateId = "specTemplateId_example"; // String | 
    try {
      SpecTemplateExpandVO result = apiInstance.getSpecTemplate(workgroupId, specTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecTemplateApi#getSpecTemplate");
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
| **specTemplateId** | **String**|  | |

### Return type

[**SpecTemplateExpandVO**](SpecTemplateExpandVO.md)

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

<a id="getSpecTemplateList"></a>
# **getSpecTemplateList**
> SpecTemplateListVO getSpecTemplateList(workgroupId)

List Spec Templates of Workgroup Level 

List Spec Templates of Workgroup Level 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecTemplateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecTemplateApi apiInstance = new SpecTemplateApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      SpecTemplateListVO result = apiInstance.getSpecTemplateList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecTemplateApi#getSpecTemplateList");
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

[**SpecTemplateListVO**](SpecTemplateListVO.md)

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

