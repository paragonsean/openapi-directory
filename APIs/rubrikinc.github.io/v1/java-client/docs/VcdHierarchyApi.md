# VcdHierarchyApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVcdHierarchyChildrenV1**](VcdHierarchyApi.md#getVcdHierarchyChildrenV1) | **GET** /vcd/hierarchy/{id}/children | Get immediate descendant objects |
| [**getVcdHierarchyDescendantsV1**](VcdHierarchyApi.md#getVcdHierarchyDescendantsV1) | **GET** /vcd/hierarchy/{id}/descendants | Get list of descendant objects |
| [**getVcdHierarchyObjectV1**](VcdHierarchyApi.md#getVcdHierarchyObjectV1) | **GET** /vcd/hierarchy/{id} | Get summary of a vCD hierarchy object |


<a id="getVcdHierarchyChildrenV1"></a>
# **getVcdHierarchyChildrenV1**
> VcdHierarchyObjectSummaryListResponse getVcdHierarchyChildrenV1(id, sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, objectType, primaryClusterId, slaAssignment, snappableStatus)

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
import org.openapitools.client.api.VcdHierarchyApi;

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

    VcdHierarchyApi apiInstance = new VcdHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
    String sortBy = "Name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Number of matches to ignore from the beginning of the results.
    String name = "name_example"; // String | Search object by object name.
    Boolean isRelic = true; // Boolean | Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic children when this value is not specified.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by ID of effective SLA domain.
    String objectType = "Cluster"; // String | Filter by node object type.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    String snappableStatus = "Protectable"; // String | Filters vCD hierarchy objects based on the specified query value.
    try {
      VcdHierarchyObjectSummaryListResponse result = apiInstance.getVcdHierarchyChildrenV1(id, sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, objectType, primaryClusterId, slaAssignment, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdHierarchyApi#getVcdHierarchyChildrenV1");
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
| **id** | **String**| ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID. | |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: Name, EffectiveSlaDomainName, SlaAssignment, ConnectionStatus, VappCount] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Number of matches to ignore from the beginning of the results. | [optional] |
| **name** | **String**| Search object by object name. | [optional] |
| **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic children when this value is not specified. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] |
| **objectType** | **String**| Filter by node object type. | [optional] [enum: Cluster, VimServer, Org, OrgVdc, Catalog, vApp] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **snappableStatus** | **String**| Filters vCD hierarchy objects based on the specified query value. | [optional] [enum: Protectable] |

### Return type

[**VcdHierarchyObjectSummaryListResponse**](VcdHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of immediate descendant objects. |  -  |

<a id="getVcdHierarchyDescendantsV1"></a>
# **getVcdHierarchyDescendantsV1**
> VcdHierarchyObjectSummaryListResponse getVcdHierarchyDescendantsV1(id, sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, objectType, primaryClusterId, slaAssignment, snappableStatus)

Get list of descendant objects

Retrieve the list of descendant objects for the specified parent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdHierarchyApi;

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

    VcdHierarchyApi apiInstance = new VcdHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID.
    String sortBy = "Name"; // String | Attribute to sort the results on.
    String sortOrder = "asc"; // String | Order for sorting the results, either ascending or descending.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    String name = "name_example"; // String | Search object by object name.
    Boolean isRelic = true; // Boolean | Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic descendants if this query is not set.
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by ID of effective SLA domain.
    String objectType = "Cluster"; // String | Filter by node object type.
    String primaryClusterId = "primaryClusterId_example"; // String | Filter by primary cluster ID, or **local**.
    String slaAssignment = "Derived"; // String | Filter by SLA assignment type.
    String snappableStatus = "Protectable"; // String | Filters vCD hierarchy objects based on the specified query value.
    try {
      VcdHierarchyObjectSummaryListResponse result = apiInstance.getVcdHierarchyDescendantsV1(id, sortBy, sortOrder, limit, offset, name, isRelic, effectiveSlaDomainId, objectType, primaryClusterId, slaAssignment, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdHierarchyApi#getVcdHierarchyDescendantsV1");
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
| **id** | **String**| ID of the parent vCD hierarchy object. To get top-level nodes, use **root** as the ID. | |
| **sortBy** | **String**| Attribute to sort the results on. | [optional] [enum: Name, EffectiveSlaDomainName, SlaAssignment, ConnectionStatus, VappCount] |
| **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **name** | **String**| Search object by object name. | [optional] |
| **isRelic** | **Boolean**| Filter by isRelic field of vCD vApp hierarchy object. Return both relic and non-relic descendants if this query is not set. | [optional] |
| **effectiveSlaDomainId** | **String**| Filter by ID of effective SLA domain. | [optional] |
| **objectType** | **String**| Filter by node object type. | [optional] [enum: Cluster, VimServer, Org, OrgVdc, Catalog, vApp] |
| **primaryClusterId** | **String**| Filter by primary cluster ID, or **local**. | [optional] |
| **slaAssignment** | **String**| Filter by SLA assignment type. | [optional] [enum: Derived, Direct, Unassigned] |
| **snappableStatus** | **String**| Filters vCD hierarchy objects based on the specified query value. | [optional] [enum: Protectable] |

### Return type

[**VcdHierarchyObjectSummaryListResponse**](VcdHierarchyObjectSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary list of descendant objects. |  -  |

<a id="getVcdHierarchyObjectV1"></a>
# **getVcdHierarchyObjectV1**
> VcdHierarchyObjectSummary getVcdHierarchyObjectV1(id)

Get summary of a vCD hierarchy object

Retrieve details for the specified object in the vCD hierarchy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VcdHierarchyApi;

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

    VcdHierarchyApi apiInstance = new VcdHierarchyApi(defaultClient);
    String id = "id_example"; // String | ID of the vCD hierarchy object.
    try {
      VcdHierarchyObjectSummary result = apiInstance.getVcdHierarchyObjectV1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VcdHierarchyApi#getVcdHierarchyObjectV1");
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
| **id** | **String**| ID of the vCD hierarchy object. | |

### Return type

[**VcdHierarchyObjectSummary**](VcdHierarchyObjectSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the hierarchy object. |  -  |

