# BucketsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteBucketsID**](BucketsApi.md#deleteBucketsID) | **DELETE** /buckets/{bucketID} | Delete a bucket |
| [**deleteBucketsIDLabelsID**](BucketsApi.md#deleteBucketsIDLabelsID) | **DELETE** /buckets/{bucketID}/labels/{labelID} | Delete a label from a bucket |
| [**deleteBucketsIDMembersID**](BucketsApi.md#deleteBucketsIDMembersID) | **DELETE** /buckets/{bucketID}/members/{userID} | Remove a member from a bucket |
| [**deleteBucketsIDOwnersID**](BucketsApi.md#deleteBucketsIDOwnersID) | **DELETE** /buckets/{bucketID}/owners/{userID} | Remove an owner from a bucket |
| [**getBuckets**](BucketsApi.md#getBuckets) | **GET** /buckets | List all buckets |
| [**getBucketsID**](BucketsApi.md#getBucketsID) | **GET** /buckets/{bucketID} | Retrieve a bucket |
| [**getBucketsIDLabels**](BucketsApi.md#getBucketsIDLabels) | **GET** /buckets/{bucketID}/labels | List all labels for a bucket |
| [**getBucketsIDMembers**](BucketsApi.md#getBucketsIDMembers) | **GET** /buckets/{bucketID}/members | List all users with member privileges for a bucket |
| [**getBucketsIDOwners**](BucketsApi.md#getBucketsIDOwners) | **GET** /buckets/{bucketID}/owners | List all owners of a bucket |
| [**getSourcesIDBuckets_0**](BucketsApi.md#getSourcesIDBuckets_0) | **GET** /sources/{sourceID}/buckets | Get buckets in a source |
| [**patchBucketsID**](BucketsApi.md#patchBucketsID) | **PATCH** /buckets/{bucketID} | Update a bucket |
| [**postBuckets**](BucketsApi.md#postBuckets) | **POST** /buckets | Create a bucket |
| [**postBucketsIDLabels**](BucketsApi.md#postBucketsIDLabels) | **POST** /buckets/{bucketID}/labels | Add a label to a bucket |
| [**postBucketsIDMembers**](BucketsApi.md#postBucketsIDMembers) | **POST** /buckets/{bucketID}/members | Add a member to a bucket |
| [**postBucketsIDOwners**](BucketsApi.md#postBucketsIDOwners) | **POST** /buckets/{bucketID}/owners | Add an owner to a bucket |


<a id="deleteBucketsID"></a>
# **deleteBucketsID**
> deleteBucketsID(bucketID, zapTraceSpan)

Delete a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The ID of the bucket to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteBucketsID(bucketID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#deleteBucketsID");
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
| **bucketID** | **String**| The ID of the bucket to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Bucket not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteBucketsIDLabelsID"></a>
# **deleteBucketsIDLabelsID**
> deleteBucketsIDLabelsID(bucketID, labelID, zapTraceSpan)

Delete a label from a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String labelID = "labelID_example"; // String | The ID of the label to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteBucketsIDLabelsID(bucketID, labelID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#deleteBucketsIDLabelsID");
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
| **bucketID** | **String**| The bucket ID. | |
| **labelID** | **String**| The ID of the label to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete has been accepted |  -  |
| **404** | Bucket not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteBucketsIDMembersID"></a>
# **deleteBucketsIDMembersID**
> deleteBucketsIDMembersID(userID, bucketID, zapTraceSpan)

Remove a member from a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the member to remove.
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteBucketsIDMembersID(userID, bucketID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#deleteBucketsIDMembersID");
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
| **userID** | **String**| The ID of the member to remove. | |
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Member removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteBucketsIDOwnersID"></a>
# **deleteBucketsIDOwnersID**
> deleteBucketsIDOwnersID(userID, bucketID, zapTraceSpan)

Remove an owner from a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the owner to remove.
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteBucketsIDOwnersID(userID, bucketID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#deleteBucketsIDOwnersID");
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
| **userID** | **String**| The ID of the owner to remove. | |
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Owner removed |  -  |
| **0** | Unexpected error |  -  |

<a id="getBuckets"></a>
# **getBuckets**
> Buckets getBuckets(zapTraceSpan, offset, limit, after, org, orgID, name, id)

List all buckets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    String after = "after_example"; // String | The last resource ID from which to seek from (but not including). This is to be used instead of `offset`. 
    String org = "org_example"; // String | The name of the organization.
    String orgID = "orgID_example"; // String | The organization ID.
    String name = "name_example"; // String | Only returns buckets with a specific name.
    String id = "id_example"; // String | Only returns buckets with a specific ID.
    try {
      Buckets result = apiInstance.getBuckets(zapTraceSpan, offset, limit, after, org, orgID, name, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBuckets");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **after** | **String**| The last resource ID from which to seek from (but not including). This is to be used instead of &#x60;offset&#x60;.  | [optional] |
| **org** | **String**| The name of the organization. | [optional] |
| **orgID** | **String**| The organization ID. | [optional] |
| **name** | **String**| Only returns buckets with a specific name. | [optional] |
| **id** | **String**| Only returns buckets with a specific ID. | [optional] |

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of buckets |  -  |
| **0** | Unexpected error |  -  |

<a id="getBucketsID"></a>
# **getBucketsID**
> Bucket getBucketsID(bucketID, zapTraceSpan)

Retrieve a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Bucket result = apiInstance.getBucketsID(bucketID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBucketsID");
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
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bucket details |  -  |
| **0** | Unexpected error |  -  |

<a id="getBucketsIDLabels"></a>
# **getBucketsIDLabels**
> LabelsResponse getBucketsIDLabels(bucketID, zapTraceSpan)

List all labels for a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelsResponse result = apiInstance.getBucketsIDLabels(bucketID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBucketsIDLabels");
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
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all labels for a bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="getBucketsIDMembers"></a>
# **getBucketsIDMembers**
> ResourceMembers getBucketsIDMembers(bucketID, zapTraceSpan)

List all users with member privileges for a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getBucketsIDMembers(bucketID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBucketsIDMembers");
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
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of bucket members |  -  |
| **0** | Unexpected error |  -  |

<a id="getBucketsIDOwners"></a>
# **getBucketsIDOwners**
> ResourceOwners getBucketsIDOwners(bucketID, zapTraceSpan)

List all owners of a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getBucketsIDOwners(bucketID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getBucketsIDOwners");
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
| **bucketID** | **String**| The bucket ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of bucket owners |  -  |
| **0** | Unexpected error |  -  |

<a id="getSourcesIDBuckets_0"></a>
# **getSourcesIDBuckets_0**
> Buckets getSourcesIDBuckets_0(sourceID, zapTraceSpan, org)

Get buckets in a source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String sourceID = "sourceID_example"; // String | The source ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String org = "org_example"; // String | The name of the organization.
    try {
      Buckets result = apiInstance.getSourcesIDBuckets_0(sourceID, zapTraceSpan, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#getSourcesIDBuckets_0");
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
| **sourceID** | **String**| The source ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **org** | **String**| The name of the organization. | [optional] |

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A source |  -  |
| **404** | Source not found |  -  |
| **0** | Unexpected error |  -  |

<a id="patchBucketsID"></a>
# **patchBucketsID**
> Bucket patchBucketsID(bucketID, patchBucketRequest, zapTraceSpan)

Update a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    PatchBucketRequest patchBucketRequest = new PatchBucketRequest(); // PatchBucketRequest | Bucket update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Bucket result = apiInstance.patchBucketsID(bucketID, patchBucketRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#patchBucketsID");
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
| **bucketID** | **String**| The bucket ID. | |
| **patchBucketRequest** | [**PatchBucketRequest**](PatchBucketRequest.md)| Bucket update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An updated bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="postBuckets"></a>
# **postBuckets**
> Bucket postBuckets(postBucketRequest, zapTraceSpan)

Create a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    PostBucketRequest postBucketRequest = new PostBucketRequest(); // PostBucketRequest | Bucket to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Bucket result = apiInstance.postBuckets(postBucketRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#postBuckets");
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
| **postBucketRequest** | [**PostBucketRequest**](PostBucketRequest.md)| Bucket to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Bucket**](Bucket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bucket created |  -  |
| **422** | Request body failed validation |  -  |
| **0** | Unexpected error |  -  |

<a id="postBucketsIDLabels"></a>
# **postBucketsIDLabels**
> LabelResponse postBucketsIDLabels(bucketID, labelMapping, zapTraceSpan)

Add a label to a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    LabelMapping labelMapping = new LabelMapping(); // LabelMapping | Label to add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      LabelResponse result = apiInstance.postBucketsIDLabels(bucketID, labelMapping, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#postBucketsIDLabels");
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
| **bucketID** | **String**| The bucket ID. | |
| **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly added label |  -  |
| **0** | Unexpected error |  -  |

<a id="postBucketsIDMembers"></a>
# **postBucketsIDMembers**
> ResourceMember postBucketsIDMembers(bucketID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postBucketsIDMembers(bucketID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#postBucketsIDMembers");
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
| **bucketID** | **String**| The bucket ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Member added to bucket |  -  |
| **0** | Unexpected error |  -  |

<a id="postBucketsIDOwners"></a>
# **postBucketsIDOwners**
> ResourceOwner postBucketsIDOwners(bucketID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to a bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketID = "bucketID_example"; // String | The bucket ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postBucketsIDOwners(bucketID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#postBucketsIDOwners");
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
| **bucketID** | **String**| The bucket ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bucket owner added |  -  |
| **0** | Unexpected error |  -  |

