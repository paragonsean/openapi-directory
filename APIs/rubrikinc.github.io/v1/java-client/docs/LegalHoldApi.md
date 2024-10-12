# LegalHoldApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applyLegalHold**](LegalHoldApi.md#applyLegalHold) | **POST** /legal_hold/snapshot | Apply a Legal Hold |
| [**dissolveLegalHoldSnapshots**](LegalHoldApi.md#dissolveLegalHoldSnapshots) | **POST** /legal_hold/object/{id}/dissolve | Dissolve a collection of snapshots of specified data source from Legal Hold |
| [**getLegalHoldObjects**](LegalHoldApi.md#getLegalHoldObjects) | **GET** /legal_hold/object | Get objects part of Legal Hold |
| [**queryLegalHold**](LegalHoldApi.md#queryLegalHold) | **GET** /legal_hold/snapshot | Get snasphots held under legal hold |


<a id="applyLegalHold"></a>
# **applyLegalHold**
> LegalHoldSummary applyLegalHold(applyLegalHoldDefinition)

Apply a Legal Hold

Places a snapshot on legal hold by specifying the hold requirements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalHoldApi;

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

    LegalHoldApi apiInstance = new LegalHoldApi(defaultClient);
    ApplyLegalHoldDefinition applyLegalHoldDefinition = new ApplyLegalHoldDefinition(); // ApplyLegalHoldDefinition | 
    try {
      LegalHoldSummary result = apiInstance.applyLegalHold(applyLegalHoldDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalHoldApi#applyLegalHold");
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
| **applyLegalHoldDefinition** | [**ApplyLegalHoldDefinition**](ApplyLegalHoldDefinition.md)|  | |

### Return type

[**LegalHoldSummary**](LegalHoldSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary of the hold which has just been created. |  -  |

<a id="dissolveLegalHoldSnapshots"></a>
# **dissolveLegalHoldSnapshots**
> DissolveLegalHoldResponse dissolveLegalHoldSnapshots(id, dissolveLegalHoldDefinition)

Dissolve a collection of snapshots of specified data source from Legal Hold

Dissolve a collection of snapshots of specified data source from Legal Hold.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalHoldApi;

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

    LegalHoldApi apiInstance = new LegalHoldApi(defaultClient);
    String id = "id_example"; // String | ID of the data source.
    DissolveLegalHoldDefinition dissolveLegalHoldDefinition = new DissolveLegalHoldDefinition(); // DissolveLegalHoldDefinition | An object that contains the IDs of the snapshots to remove from legal hold status.
    try {
      DissolveLegalHoldResponse result = apiInstance.dissolveLegalHoldSnapshots(id, dissolveLegalHoldDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalHoldApi#dissolveLegalHoldSnapshots");
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
| **id** | **String**| ID of the data source. | |
| **dissolveLegalHoldDefinition** | [**DissolveLegalHoldDefinition**](DissolveLegalHoldDefinition.md)| An object that contains the IDs of the snapshots to remove from legal hold status. | |

### Return type

[**DissolveLegalHoldResponse**](DissolveLegalHoldResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of snapshots whose legal holds have been successfully dissolved. |  -  |

<a id="getLegalHoldObjects"></a>
# **getLegalHoldObjects**
> ObjectHoldSummaryListResponse getLegalHoldObjects(objectId, limit, offset, objectName, objectType, sortBy, sortOrder)

Get objects part of Legal Hold

Returns the object details for object with snapshots under legal hold.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalHoldApi;

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

    LegalHoldApi apiInstance = new LegalHoldApi(defaultClient);
    String objectId = "objectId_example"; // String | Limit the list to a particular object.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Specifies a number of initial matches to ignore.
    String objectName = "objectName_example"; // String | Limits the list to objects that match a specified value for the object name.
    String objectType = "objectType_example"; // String | Limits the list to objects that match a specified type.
    String sortBy = "objectName"; // String | The attribute used to sort summary information. The optional parameter _sort_order_ specifies ascending or descending sort order.
    String sortOrder = "asc"; // String | Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
    try {
      ObjectHoldSummaryListResponse result = apiInstance.getLegalHoldObjects(objectId, limit, offset, objectName, objectType, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalHoldApi#getLegalHoldObjects");
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
| **objectId** | **String**| Limit the list to a particular object. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Specifies a number of initial matches to ignore. | [optional] |
| **objectName** | **String**| Limits the list to objects that match a specified value for the object name. | [optional] |
| **objectType** | **String**| Limits the list to objects that match a specified type. | [optional] |
| **sortBy** | **String**| The attribute used to sort summary information. The optional parameter _sort_order_ specifies ascending or descending sort order. | [optional] [enum: objectName, objectType, numberOfSnapshotsHeld] |
| **sortOrder** | **String**| Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**ObjectHoldSummaryListResponse**](ObjectHoldSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of details for objects with snasphots in a legal hold status. |  -  |

<a id="queryLegalHold"></a>
# **queryLegalHold**
> LegalHoldSummaryListResponse queryLegalHold(objectId, limit, offset, objectName, objectType, beforeDate, afterDate, placedOnHoldBeforeDate, placedOnHoldAfterDate, sortBy, sortOrder, snapshotType)

Get snasphots held under legal hold

Get summary for snapshots under legal hold. If object_id is passed, return summary information only for snapshots of the object under legal hold else return summary for all snapshots under legal hold.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalHoldApi;

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

    LegalHoldApi apiInstance = new LegalHoldApi(defaultClient);
    String objectId = "objectId_example"; // String | Limit the list to snapshot for the particular object.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | An integer that specifies a number of initial matches to ignore.
    String objectName = "objectName_example"; // String | Limits the list to objects that match a specified value for the object name.
    String objectType = "objectType_example"; // String | Limits the list to objects that match a specified type.
    OffsetDateTime beforeDate = OffsetDateTime.now(); // OffsetDateTime | Limits the list to snapshots with holds created before a specified date.
    OffsetDateTime afterDate = OffsetDateTime.now(); // OffsetDateTime | Limits the list to snapshots with holds created after a specified date.
    OffsetDateTime placedOnHoldBeforeDate = OffsetDateTime.now(); // OffsetDateTime | Limits the list to snapshots which were placed on legal hold before a specified date.
    OffsetDateTime placedOnHoldAfterDate = OffsetDateTime.now(); // OffsetDateTime | Limits the list to snapshots which were placed on legal hold after a specified date.
    String sortBy = "SnapshotTime"; // String | The attribute used to sort summary information. The optional parameter **_sort_order_** specifies ascending or descending sort order.
    String sortOrder = "asc"; // String | Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified.
    String snapshotType = "OnDemand"; // String | Specifies the type of snapshots to be returned.
    try {
      LegalHoldSummaryListResponse result = apiInstance.queryLegalHold(objectId, limit, offset, objectName, objectType, beforeDate, afterDate, placedOnHoldBeforeDate, placedOnHoldAfterDate, sortBy, sortOrder, snapshotType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalHoldApi#queryLegalHold");
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
| **objectId** | **String**| Limit the list to snapshot for the particular object. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| An integer that specifies a number of initial matches to ignore. | [optional] |
| **objectName** | **String**| Limits the list to objects that match a specified value for the object name. | [optional] |
| **objectType** | **String**| Limits the list to objects that match a specified type. | [optional] |
| **beforeDate** | **OffsetDateTime**| Limits the list to snapshots with holds created before a specified date. | [optional] |
| **afterDate** | **OffsetDateTime**| Limits the list to snapshots with holds created after a specified date. | [optional] |
| **placedOnHoldBeforeDate** | **OffsetDateTime**| Limits the list to snapshots which were placed on legal hold before a specified date. | [optional] |
| **placedOnHoldAfterDate** | **OffsetDateTime**| Limits the list to snapshots which were placed on legal hold after a specified date. | [optional] |
| **sortBy** | **String**| The attribute used to sort summary information. The optional parameter **_sort_order_** specifies ascending or descending sort order. | [optional] [enum: SnapshotTime, PlaceOnHoldTime, SnapshotType] |
| **sortOrder** | **String**| Specifies ascending or descending sort order. Summary results are sorted in ascending order when this parameter is not specified. | [optional] [default to asc] [enum: asc, desc] |
| **snapshotType** | **String**| Specifies the type of snapshots to be returned. | [optional] [enum: OnDemand, Scheduled, Protected, Unprotected] |

### Return type

[**LegalHoldSummaryListResponse**](LegalHoldSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for legal holds. |  -  |

