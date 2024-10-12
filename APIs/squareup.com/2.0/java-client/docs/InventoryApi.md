# InventoryApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchChangeInventory**](InventoryApi.md#batchChangeInventory) | **POST** /v2/inventory/changes/batch-create | BatchChangeInventory |
| [**batchRetrieveInventoryChanges**](InventoryApi.md#batchRetrieveInventoryChanges) | **POST** /v2/inventory/changes/batch-retrieve | BatchRetrieveInventoryChanges |
| [**batchRetrieveInventoryCounts**](InventoryApi.md#batchRetrieveInventoryCounts) | **POST** /v2/inventory/counts/batch-retrieve | BatchRetrieveInventoryCounts |
| [**deprecatedBatchChangeInventory**](InventoryApi.md#deprecatedBatchChangeInventory) | **POST** /v2/inventory/batch-change | DeprecatedBatchChangeInventory |
| [**deprecatedBatchRetrieveInventoryChanges**](InventoryApi.md#deprecatedBatchRetrieveInventoryChanges) | **POST** /v2/inventory/batch-retrieve-changes | DeprecatedBatchRetrieveInventoryChanges |
| [**deprecatedBatchRetrieveInventoryCounts**](InventoryApi.md#deprecatedBatchRetrieveInventoryCounts) | **POST** /v2/inventory/batch-retrieve-counts | DeprecatedBatchRetrieveInventoryCounts |
| [**deprecatedRetrieveInventoryAdjustment**](InventoryApi.md#deprecatedRetrieveInventoryAdjustment) | **GET** /v2/inventory/adjustment/{adjustment_id} | DeprecatedRetrieveInventoryAdjustment |
| [**deprecatedRetrieveInventoryPhysicalCount**](InventoryApi.md#deprecatedRetrieveInventoryPhysicalCount) | **GET** /v2/inventory/physical-count/{physical_count_id} | DeprecatedRetrieveInventoryPhysicalCount |
| [**retrieveInventoryAdjustment**](InventoryApi.md#retrieveInventoryAdjustment) | **GET** /v2/inventory/adjustments/{adjustment_id} | RetrieveInventoryAdjustment |
| [**retrieveInventoryChanges**](InventoryApi.md#retrieveInventoryChanges) | **GET** /v2/inventory/{catalog_object_id}/changes | RetrieveInventoryChanges |
| [**retrieveInventoryCount**](InventoryApi.md#retrieveInventoryCount) | **GET** /v2/inventory/{catalog_object_id} | RetrieveInventoryCount |
| [**retrieveInventoryPhysicalCount**](InventoryApi.md#retrieveInventoryPhysicalCount) | **GET** /v2/inventory/physical-counts/{physical_count_id} | RetrieveInventoryPhysicalCount |
| [**retrieveInventoryTransfer**](InventoryApi.md#retrieveInventoryTransfer) | **GET** /v2/inventory/transfers/{transfer_id} | RetrieveInventoryTransfer |


<a id="batchChangeInventory"></a>
# **batchChangeInventory**
> BatchChangeInventoryResponse batchChangeInventory(batchChangeInventoryRequest)

BatchChangeInventory

Applies adjustments and counts to the provided item quantities.  On success: returns the current calculated counts for all objects referenced in the request. On failure: returns a list of related errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchChangeInventoryRequest batchChangeInventoryRequest = new BatchChangeInventoryRequest(); // BatchChangeInventoryRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchChangeInventoryResponse result = apiInstance.batchChangeInventory(batchChangeInventoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#batchChangeInventory");
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
| **batchChangeInventoryRequest** | [**BatchChangeInventoryRequest**](BatchChangeInventoryRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchChangeInventoryResponse**](BatchChangeInventoryResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="batchRetrieveInventoryChanges"></a>
# **batchRetrieveInventoryChanges**
> BatchRetrieveInventoryChangesResponse batchRetrieveInventoryChanges(batchRetrieveInventoryChangesRequest)

BatchRetrieveInventoryChanges

Returns historical physical counts and adjustments based on the provided filter criteria.  Results are paginated and sorted in ascending order according their &#x60;occurred_at&#x60; timestamp (oldest first).  BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchRetrieveInventoryChangesRequest batchRetrieveInventoryChangesRequest = new BatchRetrieveInventoryChangesRequest(); // BatchRetrieveInventoryChangesRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchRetrieveInventoryChangesResponse result = apiInstance.batchRetrieveInventoryChanges(batchRetrieveInventoryChangesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#batchRetrieveInventoryChanges");
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
| **batchRetrieveInventoryChangesRequest** | [**BatchRetrieveInventoryChangesRequest**](BatchRetrieveInventoryChangesRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchRetrieveInventoryChangesResponse**](BatchRetrieveInventoryChangesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="batchRetrieveInventoryCounts"></a>
# **batchRetrieveInventoryCounts**
> BatchRetrieveInventoryCountsResponse batchRetrieveInventoryCounts(batchRetrieveInventoryCountsRequest)

BatchRetrieveInventoryCounts

Returns current counts for the provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s at the requested [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.  Results are paginated and sorted in descending order according to their &#x60;calculated_at&#x60; timestamp (newest first).  When &#x60;updated_after&#x60; is specified, only counts that have changed since that time (based on the server timestamp for the most recent change) are returned. This allows clients to perform a \&quot;sync\&quot; operation, for example in response to receiving a Webhook notification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchRetrieveInventoryCountsRequest batchRetrieveInventoryCountsRequest = new BatchRetrieveInventoryCountsRequest(); // BatchRetrieveInventoryCountsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchRetrieveInventoryCountsResponse result = apiInstance.batchRetrieveInventoryCounts(batchRetrieveInventoryCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#batchRetrieveInventoryCounts");
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
| **batchRetrieveInventoryCountsRequest** | [**BatchRetrieveInventoryCountsRequest**](BatchRetrieveInventoryCountsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchRetrieveInventoryCountsResponse**](BatchRetrieveInventoryCountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deprecatedBatchChangeInventory"></a>
# **deprecatedBatchChangeInventory**
> BatchChangeInventoryResponse deprecatedBatchChangeInventory(batchChangeInventoryRequest)

DeprecatedBatchChangeInventory

Deprecated version of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory) after the endpoint URL  is updated to conform to the standard convention.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchChangeInventoryRequest batchChangeInventoryRequest = new BatchChangeInventoryRequest(); // BatchChangeInventoryRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchChangeInventoryResponse result = apiInstance.deprecatedBatchChangeInventory(batchChangeInventoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#deprecatedBatchChangeInventory");
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
| **batchChangeInventoryRequest** | [**BatchChangeInventoryRequest**](BatchChangeInventoryRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchChangeInventoryResponse**](BatchChangeInventoryResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deprecatedBatchRetrieveInventoryChanges"></a>
# **deprecatedBatchRetrieveInventoryChanges**
> BatchRetrieveInventoryChangesResponse deprecatedBatchRetrieveInventoryChanges(batchRetrieveInventoryChangesRequest)

DeprecatedBatchRetrieveInventoryChanges

Deprecated version of [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) after the endpoint URL  is updated to conform to the standard convention.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchRetrieveInventoryChangesRequest batchRetrieveInventoryChangesRequest = new BatchRetrieveInventoryChangesRequest(); // BatchRetrieveInventoryChangesRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchRetrieveInventoryChangesResponse result = apiInstance.deprecatedBatchRetrieveInventoryChanges(batchRetrieveInventoryChangesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#deprecatedBatchRetrieveInventoryChanges");
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
| **batchRetrieveInventoryChangesRequest** | [**BatchRetrieveInventoryChangesRequest**](BatchRetrieveInventoryChangesRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchRetrieveInventoryChangesResponse**](BatchRetrieveInventoryChangesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deprecatedBatchRetrieveInventoryCounts"></a>
# **deprecatedBatchRetrieveInventoryCounts**
> BatchRetrieveInventoryCountsResponse deprecatedBatchRetrieveInventoryCounts(batchRetrieveInventoryCountsRequest)

DeprecatedBatchRetrieveInventoryCounts

Deprecated version of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts) after the endpoint URL  is updated to conform to the standard convention.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    BatchRetrieveInventoryCountsRequest batchRetrieveInventoryCountsRequest = new BatchRetrieveInventoryCountsRequest(); // BatchRetrieveInventoryCountsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      BatchRetrieveInventoryCountsResponse result = apiInstance.deprecatedBatchRetrieveInventoryCounts(batchRetrieveInventoryCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#deprecatedBatchRetrieveInventoryCounts");
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
| **batchRetrieveInventoryCountsRequest** | [**BatchRetrieveInventoryCountsRequest**](BatchRetrieveInventoryCountsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**BatchRetrieveInventoryCountsResponse**](BatchRetrieveInventoryCountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deprecatedRetrieveInventoryAdjustment"></a>
# **deprecatedRetrieveInventoryAdjustment**
> RetrieveInventoryAdjustmentResponse deprecatedRetrieveInventoryAdjustment(adjustmentId)

DeprecatedRetrieveInventoryAdjustment

Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-adjustment) after the endpoint URL  is updated to conform to the standard convention.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String adjustmentId = "adjustmentId_example"; // String | ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    try {
      RetrieveInventoryAdjustmentResponse result = apiInstance.deprecatedRetrieveInventoryAdjustment(adjustmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#deprecatedRetrieveInventoryAdjustment");
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
| **adjustmentId** | **String**| ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve. | |

### Return type

[**RetrieveInventoryAdjustmentResponse**](RetrieveInventoryAdjustmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deprecatedRetrieveInventoryPhysicalCount"></a>
# **deprecatedRetrieveInventoryPhysicalCount**
> RetrieveInventoryPhysicalCountResponse deprecatedRetrieveInventoryPhysicalCount(physicalCountId)

DeprecatedRetrieveInventoryPhysicalCount

Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-physical-count) after the endpoint URL  is updated to conform to the standard convention.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String physicalCountId = "physicalCountId_example"; // String | ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    try {
      RetrieveInventoryPhysicalCountResponse result = apiInstance.deprecatedRetrieveInventoryPhysicalCount(physicalCountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#deprecatedRetrieveInventoryPhysicalCount");
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
| **physicalCountId** | **String**| ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve. | |

### Return type

[**RetrieveInventoryPhysicalCountResponse**](RetrieveInventoryPhysicalCountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveInventoryAdjustment"></a>
# **retrieveInventoryAdjustment**
> RetrieveInventoryAdjustmentResponse retrieveInventoryAdjustment(adjustmentId)

RetrieveInventoryAdjustment

Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) object with the provided &#x60;adjustment_id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String adjustmentId = "adjustmentId_example"; // String | ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    try {
      RetrieveInventoryAdjustmentResponse result = apiInstance.retrieveInventoryAdjustment(adjustmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#retrieveInventoryAdjustment");
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
| **adjustmentId** | **String**| ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve. | |

### Return type

[**RetrieveInventoryAdjustmentResponse**](RetrieveInventoryAdjustmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveInventoryChanges"></a>
# **retrieveInventoryChanges**
> RetrieveInventoryChangesResponse retrieveInventoryChanges(catalogObjectId, locationIds, cursor)

RetrieveInventoryChanges

Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at the requested [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.   You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes)  and having the &#x60;catalog_object_ids&#x60; list contain a single element of the &#x60;CatalogObject&#x60; ID.  Results are paginated and sorted in descending order according to their &#x60;occurred_at&#x60; timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint can be  used to display recent changes for a specific item. For more sophisticated queries, use a batch endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String catalogObjectId = "catalogObjectId_example"; // String | ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    String locationIds = "locationIds_example"; // String | The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    try {
      RetrieveInventoryChangesResponse result = apiInstance.retrieveInventoryChanges(catalogObjectId, locationIds, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#retrieveInventoryChanges");
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
| **catalogObjectId** | **String**| ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve. | |
| **locationIds** | **String**| The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations. | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. | [optional] |

### Return type

[**RetrieveInventoryChangesResponse**](RetrieveInventoryChangesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveInventoryCount"></a>
# **retrieveInventoryCount**
> RetrieveInventoryCountResponse retrieveInventoryCount(catalogObjectId, locationIds, cursor)

RetrieveInventoryCount

Retrieves the current calculated stock count for a given [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at a given set of [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String catalogObjectId = "catalogObjectId_example"; // String | ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    String locationIds = "locationIds_example"; // String | The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations.
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    try {
      RetrieveInventoryCountResponse result = apiInstance.retrieveInventoryCount(catalogObjectId, locationIds, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#retrieveInventoryCount");
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
| **catalogObjectId** | **String**| ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve. | |
| **locationIds** | **String**| The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations. | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. | [optional] |

### Return type

[**RetrieveInventoryCountResponse**](RetrieveInventoryCountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveInventoryPhysicalCount"></a>
# **retrieveInventoryPhysicalCount**
> RetrieveInventoryPhysicalCountResponse retrieveInventoryPhysicalCount(physicalCountId)

RetrieveInventoryPhysicalCount

Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) object with the provided &#x60;physical_count_id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String physicalCountId = "physicalCountId_example"; // String | ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    try {
      RetrieveInventoryPhysicalCountResponse result = apiInstance.retrieveInventoryPhysicalCount(physicalCountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#retrieveInventoryPhysicalCount");
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
| **physicalCountId** | **String**| ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve. | |

### Return type

[**RetrieveInventoryPhysicalCountResponse**](RetrieveInventoryPhysicalCountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveInventoryTransfer"></a>
# **retrieveInventoryTransfer**
> RetrieveInventoryTransferResponse retrieveInventoryTransfer(transferId)

RetrieveInventoryTransfer

Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) object with the provided &#x60;transfer_id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String transferId = "transferId_example"; // String | ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve.
    try {
      RetrieveInventoryTransferResponse result = apiInstance.retrieveInventoryTransfer(transferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#retrieveInventoryTransfer");
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
| **transferId** | **String**| ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve. | |

### Return type

[**RetrieveInventoryTransferResponse**](RetrieveInventoryTransferResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

