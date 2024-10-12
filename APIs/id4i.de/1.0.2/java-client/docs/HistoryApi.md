# HistoryApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addItem**](HistoryApi.md#addItem) | **POST** /api/v1/history/{id4n} | Add history item |
| [**callList**](HistoryApi.md#callList) | **GET** /api/v1/history/{id4n}/{organizationId} | DEPRECATED - List history |
| [**filteredList**](HistoryApi.md#filteredList) | **GET** /api/v1/history/{id4n} | List history |
| [**retrieveItem**](HistoryApi.md#retrieveItem) | **GET** /api/v1/history/{id4n}/{organizationId}/{sequenceId} | Get history item |
| [**updateItem**](HistoryApi.md#updateItem) | **PATCH** /api/v1/history/{id4n}/{organizationId}/{sequenceId} | Update history item |
| [**updateItemVisibility**](HistoryApi.md#updateItemVisibility) | **PUT** /api/v1/history/{id4n}/{organizationId}/{sequenceId}/visibility | Set history item visibility |


<a id="addItem"></a>
# **addItem**
> addItem(id4n, historyItem)

Add history item

Add a new history item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    HistoryItem historyItem = new HistoryItem(); // HistoryItem | The history item to publish
    try {
      apiInstance.addItem(id4n, historyItem);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#addItem");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **historyItem** | [**HistoryItem**](HistoryItem.md)| The history item to publish | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="callList"></a>
# **callList**
> PaginatedResponseOfHistoryItem callList(id4n, organizationId, includePrivate, offset, limit)

DEPRECATED - List history

DEPRECATED - please use filteredList with organization parameter to achieve the same functionality

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    String organizationId = "organizationId_example"; // String | organizationId
    Boolean includePrivate = true; // Boolean | Also return private history entries
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfHistoryItem result = apiInstance.callList(id4n, organizationId, includePrivate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#callList");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **organizationId** | **String**| organizationId | |
| **includePrivate** | **Boolean**| Also return private history entries | [optional] [default to true] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfHistoryItem**](PaginatedResponseOfHistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="filteredList"></a>
# **filteredList**
> PaginatedResponseOfHistoryItem filteredList(id4n, includePrivate, organization, type, qualifier, fromDate, toDate, offset, limit)

List history

Lists the history of a GUID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    Boolean includePrivate = true; // Boolean | Also return private history entries
    String organization = "organization_example"; // String | Show only entries created by one of the given organizations. This parameter can be used multiple times.
    List<String> type = Arrays.asList(); // List<String> | Show only entries matching one of the given history item types. This parameter can be used multiple times.
    List<String> qualifier = Arrays.asList(); // List<String> | Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times.
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | From date time as UTC Date-Time format
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | To date time as UTC Date-Time format
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfHistoryItem result = apiInstance.filteredList(id4n, includePrivate, organization, type, qualifier, fromDate, toDate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#filteredList");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **includePrivate** | **Boolean**| Also return private history entries | [optional] [default to true] |
| **organization** | **String**| Show only entries created by one of the given organizations. This parameter can be used multiple times. | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| Show only entries matching one of the given history item types. This parameter can be used multiple times. | [optional] [enum: CREATED, DESTROYED, RECYCLED, SHIPMENT_PREPARED, STORED, RETRIEVED_FROM_STORAGE, PACKAGED, DISPATCHED, RECEIVED, DELIVERY_REFUSED, REPROCESSING_STARTED, REPROCESSING_STEP_STARTED, REPROCESSING_STEP_CANCELLED, REPROCESSING_STEP_FINISHED, REPROCESSING_CANCELLED, REPROCESSING_FINISHED, DISASSEMBLED, MAINTENANCE_STARTED, MAINTENANCE_STEP_STARTED, MAINTENANCE_STEP_CANCELLED, MAINTENANCE_STEP_FINISHED, MAINTENANCE_CANCELLED, MAINTENANCE_FINISHED, PRODUCTION_STARTED, PRODUCTION_CANCELLED, PRODUCTION_FINISHED, PRODUCTION_STEP_STARTED, PRODUCTION_STEP_CANCELLED, PRODUCTION_STEP_FINISHED, QUALITY_CHECK_PERFORMED] |
| **qualifier** | [**List&lt;String&gt;**](String.md)| Show only entries matching one of the given history item qualifiers (additional property de.id4i.history.item.qualifier). This parameter can be used multiple times. | [optional] |
| **fromDate** | **OffsetDateTime**| From date time as UTC Date-Time format | [optional] |
| **toDate** | **OffsetDateTime**| To date time as UTC Date-Time format | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfHistoryItem**](PaginatedResponseOfHistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="retrieveItem"></a>
# **retrieveItem**
> HistoryItem retrieveItem(id4n, organizationId, sequenceId)

Get history item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    String organizationId = "organizationId_example"; // String | organizationId
    Integer sequenceId = 56; // Integer | sequenceId
    try {
      HistoryItem result = apiInstance.retrieveItem(id4n, organizationId, sequenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#retrieveItem");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **organizationId** | **String**| organizationId | |
| **sequenceId** | **Integer**| sequenceId | |

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateItem"></a>
# **updateItem**
> HistoryItem updateItem(id4n, organizationId, sequenceId, historyItemUpdate)

Update history item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    String organizationId = "organizationId_example"; // String | organizationId
    Integer sequenceId = 56; // Integer | sequenceId
    HistoryItemUpdate historyItemUpdate = new HistoryItemUpdate(); // HistoryItemUpdate | update
    try {
      HistoryItem result = apiInstance.updateItem(id4n, organizationId, sequenceId, historyItemUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#updateItem");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **organizationId** | **String**| organizationId | |
| **sequenceId** | **Integer**| sequenceId | |
| **historyItemUpdate** | [**HistoryItemUpdate**](HistoryItemUpdate.md)| update | |

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="updateItemVisibility"></a>
# **updateItemVisibility**
> HistoryItem updateItemVisibility(id4n, organizationId, sequenceId, visibility)

Set history item visibility

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String id4n = "id4n_example"; // String | GUID to retrieve the history for
    String organizationId = "organizationId_example"; // String | organizationId
    Integer sequenceId = 56; // Integer | sequenceId
    Visibility visibility = new Visibility(); // Visibility | History item visibility restrictions
    try {
      HistoryItem result = apiInstance.updateItemVisibility(id4n, organizationId, sequenceId, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#updateItemVisibility");
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
| **id4n** | **String**| GUID to retrieve the history for | |
| **organizationId** | **String**| organizationId | |
| **sequenceId** | **Integer**| sequenceId | |
| **visibility** | [**Visibility**](Visibility.md)| History item visibility restrictions | |

### Return type

[**HistoryItem**](HistoryItem.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **409** | Conflict |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

