# WorkgroupApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getClientWorkgroupList**](WorkgroupApi.md#getClientWorkgroupList) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups | List client workgroups |
| [**getSpecificClientWorkgroup**](WorkgroupApi.md#getSpecificClientWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/clientWorkgroups/{client_workgroup_id} | Get a specific client workgroups |
| [**getSupplierWorkgroupDetail**](WorkgroupApi.md#getSupplierWorkgroupDetail) | **GET** /v1/workgroups/{workgroup_id}/supplierWorkgroups/{bu_supplier_workgroup_id} | Get the specific supplier of My Group |
| [**getSupplierWorkgroupList**](WorkgroupApi.md#getSupplierWorkgroupList) | **GET** /v1/workgroups/{workgroup_id}/supplierWorkgroups | List supplier workgroups |
| [**getWorkgroupDetail**](WorkgroupApi.md#getWorkgroupDetail) | **GET** /v1/workgroups/{workgroup_id}/detail | Detail workgroup info |
| [**getWorkgroupList**](WorkgroupApi.md#getWorkgroupList) | **GET** /v1/workgroups | List the workgroups |
| [**putWorkgroup**](WorkgroupApi.md#putWorkgroup) | **PUT** /v1/workgroups/{workgroup_id}/detail | Update a specific Workgroup |


<a id="getClientWorkgroupList"></a>
# **getClientWorkgroupList**
> ClientWorkgroupListVO getClientWorkgroupList(workgroupId)

List client workgroups

List client workgroups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ClientWorkgroupListVO result = apiInstance.getClientWorkgroupList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getClientWorkgroupList");
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

[**ClientWorkgroupListVO**](ClientWorkgroupListVO.md)

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

<a id="getSpecificClientWorkgroup"></a>
# **getSpecificClientWorkgroup**
> ClientWorkgroupExpandVO getSpecificClientWorkgroup(workgroupId, clientWorkgroupId)

Get a specific client workgroups

Get a specific client workgroups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String clientWorkgroupId = "clientWorkgroupId_example"; // String | 
    try {
      ClientWorkgroupExpandVO result = apiInstance.getSpecificClientWorkgroup(workgroupId, clientWorkgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getSpecificClientWorkgroup");
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

[**ClientWorkgroupExpandVO**](ClientWorkgroupExpandVO.md)

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

<a id="getSupplierWorkgroupDetail"></a>
# **getSupplierWorkgroupDetail**
> SupplierWorkgroupExpandVO getSupplierWorkgroupDetail(workgroupId, buSupplierWorkgroupId)

Get the specific supplier of My Group

Get the specific supplier of My Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String buSupplierWorkgroupId = "buSupplierWorkgroupId_example"; // String | 
    try {
      SupplierWorkgroupExpandVO result = apiInstance.getSupplierWorkgroupDetail(workgroupId, buSupplierWorkgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getSupplierWorkgroupDetail");
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
| **buSupplierWorkgroupId** | **String**|  | |

### Return type

[**SupplierWorkgroupExpandVO**](SupplierWorkgroupExpandVO.md)

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

<a id="getSupplierWorkgroupList"></a>
# **getSupplierWorkgroupList**
> SupplierWorkgroupListVO getSupplierWorkgroupList(workgroupId)

List supplier workgroups

List supplier workgroups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      SupplierWorkgroupListVO result = apiInstance.getSupplierWorkgroupList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getSupplierWorkgroupList");
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

[**SupplierWorkgroupListVO**](SupplierWorkgroupListVO.md)

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

<a id="getWorkgroupDetail"></a>
# **getWorkgroupDetail**
> WorkgroupExpandVO getWorkgroupDetail(workgroupId)

Detail workgroup info

Detail workgroup info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      WorkgroupExpandVO result = apiInstance.getWorkgroupDetail(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getWorkgroupDetail");
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

[**WorkgroupExpandVO**](WorkgroupExpandVO.md)

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

<a id="getWorkgroupList"></a>
# **getWorkgroupList**
> WorkgroupListVO getWorkgroupList(workgroupName, workgroupTypes)

List the workgroups

List the workgroups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupName = "workgroupName_example"; // String | Workgroup Name
    List<String> workgroupTypes = Arrays.asList(); // List<String> | 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner
    try {
      WorkgroupListVO result = apiInstance.getWorkgroupList(workgroupName, workgroupTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#getWorkgroupList");
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
| **workgroupName** | **String**| Workgroup Name | [optional] |
| **workgroupTypes** | [**List&lt;String&gt;**](String.md)| 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner | [optional] |

### Return type

[**WorkgroupListVO**](WorkgroupListVO.md)

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

<a id="putWorkgroup"></a>
# **putWorkgroup**
> WorkgroupHTTPStatusVO putWorkgroup(workgroupId, workgroupUpdPersistVO)

Update a specific Workgroup

Update a specific Workgroup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkgroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    WorkgroupApi apiInstance = new WorkgroupApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    WorkgroupUpdPersistVO workgroupUpdPersistVO = new WorkgroupUpdPersistVO(); // WorkgroupUpdPersistVO | 
    try {
      WorkgroupHTTPStatusVO result = apiInstance.putWorkgroup(workgroupId, workgroupUpdPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkgroupApi#putWorkgroup");
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
| **workgroupUpdPersistVO** | [**WorkgroupUpdPersistVO**](WorkgroupUpdPersistVO.md)|  | [optional] |

### Return type

[**WorkgroupHTTPStatusVO**](WorkgroupHTTPStatusVO.md)

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

