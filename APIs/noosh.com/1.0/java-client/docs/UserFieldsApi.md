# UserFieldsApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProjectHomeUserFieldListOfClient**](UserFieldsApi.md#getProjectHomeUserFieldListOfClient) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id}/projectHomeUserFields | List projec home user fields of client workgroup |
| [**getProjectHomeUserFieldsList**](UserFieldsApi.md#getProjectHomeUserFieldsList) | **GET** /v1/workgroups/{workgroup_id}/projectHomeUserFields | List projec home user fields |


<a id="getProjectHomeUserFieldListOfClient"></a>
# **getProjectHomeUserFieldListOfClient**
> ProjectHomeUserFieldsListVO getProjectHomeUserFieldListOfClient(workgroupId, clientWorkgroupId)

List projec home user fields of client workgroup

List projec home user fields of client workgroup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    UserFieldsApi apiInstance = new UserFieldsApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String clientWorkgroupId = "clientWorkgroupId_example"; // String | 
    try {
      ProjectHomeUserFieldsListVO result = apiInstance.getProjectHomeUserFieldListOfClient(workgroupId, clientWorkgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserFieldsApi#getProjectHomeUserFieldListOfClient");
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
| **clientWorkgroupId** | **String**|  | |

### Return type

[**ProjectHomeUserFieldsListVO**](ProjectHomeUserFieldsListVO.md)

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

<a id="getProjectHomeUserFieldsList"></a>
# **getProjectHomeUserFieldsList**
> ProjectHomeUserFieldsListVO getProjectHomeUserFieldsList(workgroupId)

List projec home user fields

List projec home user fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    UserFieldsApi apiInstance = new UserFieldsApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ProjectHomeUserFieldsListVO result = apiInstance.getProjectHomeUserFieldsList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserFieldsApi#getProjectHomeUserFieldsList");
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

[**ProjectHomeUserFieldsListVO**](ProjectHomeUserFieldsListVO.md)

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

