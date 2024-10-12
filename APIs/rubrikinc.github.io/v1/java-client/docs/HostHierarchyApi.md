# HostHierarchyApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHostHierarchyChildren**](HostHierarchyApi.md#getHostHierarchyChildren) | **GET** /host/hierarchy/{id}/children | Get immediate descendant objects |
| [**getHostHierarchyObject**](HostHierarchyApi.md#getHostHierarchyObject) | **GET** /host/hierarchy/{id} | Get summary of a host/share hierarchy object |


<a id="getHostHierarchyChildren"></a>
# **getHostHierarchyChildren**
> HostHierarchyObjectSummaryListResponse getHostHierarchyChildren(id, name, objectType, effectiveSlaDomainId, primaryClusterId, slaAssignment, templateId, vendorType, exportPoint, operatingSystemType, sortBy, sortOrder, limit, offset)

Get immediate descendant objects

Retrieve the list of immediate descendant objects for the specified parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostHierarchyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostHierarchyApi apiInstance = new HostHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the parent host hierarchy object. To get top-level nodes, use **root** as the ID.
    String name = "name_example"; // String | Search object by object name.
    String objectType = "Host"; // String | Filter by node object type.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by ID of effective SLA domain.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    String slaAssignment = "Derived"; // String | Limit a response to the results that have the specified SLA Domain assignment type.
    String templateId = "templateId_example"; // String | Filter by fileset template ID.
    String vendorType = "Isilon"; // String | Filter by NAS vendor.
    String exportPoint = "exportPoint_example"; // String | Search object by export point.
    String operatingSystemType = "ANY"; // String | Filter the summary information based on the operating system type. Accepted values are 'Windows', 'UnixLike', 'ANY', 'NONE'. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
    String sortBy = "Status"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Number of matches to ignore from the beginning of the results.
    try {
      HostHierarchyObjectSummaryListResponse result = apiInstance.getHostHierarchyChildren(id, name, objectType, effectiveSlaDomainId, primaryClusterId, slaAssignment, templateId, vendorType, exportPoint, operatingSystemType, sortBy, sortOrder, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostHierarchyApi#getHostHierarchyChildren");
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
| **id** | **String**| ID of the parent host hierarchy object. To get top-level nodes, use **root** as the ID. | |
| **name** | **String**| Search object by object name. | [optional] |
| **objectType** | **String**| Filter by node object type. | [optional] [enum: Host, Share] |
| **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **templateId** | **String**| Filter by fileset template ID. | [optional] |
| **vendorType** | **String**| Filter by NAS vendor. | [optional] [enum: Isilon, NetApp, FlashBlade] |
| **exportPoint** | **String**| Search object by export point. | [optional] |
| **operatingSystemType** | **String**| Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set. | [optional] [enum: ANY, NONE, UnixLike, Windows] |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: Status, Name, ExportPoint, ShareType, Hostname] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Number of matches to ignore from the beginning of the results. | [optional] |

### Return type

[**HostHierarchyObjectSummaryListResponse**](HostHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of immediate descendant objects. |  -  |

<a id="getHostHierarchyObject"></a>
# **getHostHierarchyObject**
> HostHierarchyObjectSummary getHostHierarchyObject(id)

Get summary of a host/share hierarchy object

Retrieve details for the specified object in the host/share hierarchy. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostHierarchyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostHierarchyApi apiInstance = new HostHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the host hierarchy object.
    try {
      HostHierarchyObjectSummary result = apiInstance.getHostHierarchyObject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostHierarchyApi#getHostHierarchyObject");
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
| **id** | **String**| ID of the host hierarchy object. | |

### Return type

[**HostHierarchyObjectSummary**](HostHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the hierarchy object. |  -  |

