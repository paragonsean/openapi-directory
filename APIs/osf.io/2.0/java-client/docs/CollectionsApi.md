# CollectionsApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**collectionsAddMetadata**](CollectionsApi.md#collectionsAddMetadata) | **POST** /collections/{collection_id}/collected_metadata/ | Add Metadata or Subjects to a Entity in a Collection |
| [**collectionsCollectedMetadata**](CollectionsApi.md#collectionsCollectedMetadata) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id}/subjects/ | Retrieve subject data for a specific piece of metadata info for a collection |
| [**collectionsCreate**](CollectionsApi.md#collectionsCreate) | **POST** /collections/ | Create a Collection |
| [**collectionsDelete**](CollectionsApi.md#collectionsDelete) | **DELETE** /collections/{collection_id}/ | Delete a Collection |
| [**collectionsDetail**](CollectionsApi.md#collectionsDetail) | **GET** /collections/{collection_id}/ | Retrieve a Collection |
| [**collectionsLinkedNodesList**](CollectionsApi.md#collectionsLinkedNodesList) | **GET** /collections/{collection_id}/linked_nodes | List All Linked Nodes for a Collection |
| [**collectionsLinkedNodesRelationships**](CollectionsApi.md#collectionsLinkedNodesRelationships) | **POST** /collections/{collection_id}/linked_nodes/relationships/ | Link Nodes to Collection |
| [**collectionsLinkedNodesRelationshipsCreate**](CollectionsApi.md#collectionsLinkedNodesRelationshipsCreate) | **GET** /collections/{collection_id}/linked_nodes/relationships/ | Give a Sparse List of Node Ids |
| [**collectionsLinkedNodesRelationshipsDelete**](CollectionsApi.md#collectionsLinkedNodesRelationshipsDelete) | **DELETE** /collections/{collection_id}/linked_nodes/relationships/ | Remove Nodes From Collection |
| [**collectionsLinkedPreprintsList**](CollectionsApi.md#collectionsLinkedPreprintsList) | **GET** /collections/{collection_id}/linked_preprints/ | List All Linked Preprints for a Collection |
| [**collectionsLinkedRegistrationsList**](CollectionsApi.md#collectionsLinkedRegistrationsList) | **GET** /collections/{collection_id}/linked_registrations/ | List All Linked Registrations for a Collection |
| [**collectionsLinkedRegistrationsRelationships**](CollectionsApi.md#collectionsLinkedRegistrationsRelationships) | **POST** /collections/{collection_id}/linked_registrations/relationships/ | Link Registrations to Collection |
| [**collectionsLinkedRegistrationsRelationshipsCreate**](CollectionsApi.md#collectionsLinkedRegistrationsRelationshipsCreate) | **GET** /collections/{collection_id}/linked_registrations/relationships/ | Give a Sparse List of Registrations Ids |
| [**collectionsLinkedRegistrationsRelationshipsDelete**](CollectionsApi.md#collectionsLinkedRegistrationsRelationshipsDelete) | **DELETE** /collections/{collection_id}/linked_registrations/relationships/ | Remove Registrations From Collection |
| [**collectionsList**](CollectionsApi.md#collectionsList) | **GET** /collections/ | List all Collections |
| [**collectionsMetadataDelete**](CollectionsApi.md#collectionsMetadataDelete) | **DELETE** /collections/{collection_id}/collected_metadata/{cgm_id} | Delete Collection Metadata from entitiy |
| [**collectionsMetadataDetail**](CollectionsApi.md#collectionsMetadataDetail) | **POST** /collections/{collection_id}/collected_metadata/{cgm_id} | Add Metadata or Subjects to an Entity in a Collection |
| [**collectionsMetadataRegistrationsDetail**](CollectionsApi.md#collectionsMetadataRegistrationsDetail) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id} | Retrieve Specific Metadata for a Collection |
| [**collectionsMetadataRegistrationsList**](CollectionsApi.md#collectionsMetadataRegistrationsList) | **GET** /collections/{collection_id}/collected_metadata/ | Retrieve a list of collected metadata for a collection |
| [**collectionsMetadataSubjectsRelationships**](CollectionsApi.md#collectionsMetadataSubjectsRelationships) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects/ | Retrieve subject metadata for a specific piece of metadata in a collection |
| [**collectionsMetadataSubjectsRelationshipsUpdate**](CollectionsApi.md#collectionsMetadataSubjectsRelationshipsUpdate) | **POST** /collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects/ | Update subjects for a specific piece of metadata in a collection |


<a id="collectionsAddMetadata"></a>
# **collectionsAddMetadata**
> collectionsAddMetadata(collectionId, body)

Add Metadata or Subjects to a Entity in a Collection

List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    Object body = null; // Object | 
    try {
      apiInstance.collectionsAddMetadata(collectionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsAddMetadata");
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
| **collectionId** | **String**| A short id for that collection | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="collectionsCollectedMetadata"></a>
# **collectionsCollectedMetadata**
> collectionsCollectedMetadata(collectionId, cgmId)

Retrieve subject data for a specific piece of metadata info for a collection

 #### Permissions In order to view these subject it must be a public collection or a user must have read permissions for collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error, other then permissions errors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    try {
      apiInstance.collectionsCollectedMetadata(collectionId, cgmId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsCollectedMetadata");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |

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
| **200** | OK |  -  |

<a id="collectionsCreate"></a>
# **collectionsCreate**
> collectionsCreate(body)

Create a Collection

Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.collectionsCreate(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsCreate");
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
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="collectionsDelete"></a>
# **collectionsDelete**
> collectionsDelete(collectionId)

Delete a Collection

Deletes a collection, if the user has appropriate permissions. #### Permissions Users must have write permissions on a collection in order to delete it #### Returns Nothing is returned in the body

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsDelete(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsDelete");
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
| **collectionId** | **String**| A short id for that collection | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="collectionsDetail"></a>
# **collectionsDetail**
> List&lt;Collection&gt; collectionsDetail(collectionId)

Retrieve a Collection

Retrieves a collection, if the user has appropriate permissions.  #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      List<Collection> result = apiInstance.collectionsDetail(collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsDetail");
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
| **collectionId** | **String**| A short id for that collection | |

### Return type

[**List&lt;Collection&gt;**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsLinkedNodesList"></a>
# **collectionsLinkedNodesList**
> collectionsLinkedNodesList(collectionId)

List All Linked Nodes for a Collection

List of all nodes linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsLinkedNodesList(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedNodesList");
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
| **collectionId** | **String**| A short id for that collection | |

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
| **200** | OK |  -  |

<a id="collectionsLinkedNodesRelationships"></a>
# **collectionsLinkedNodesRelationships**
> collectionsLinkedNodesRelationships(collectionId, body)

Link Nodes to Collection

This endpoint allow users to a add a node to a collection by issuing a POST request. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    Object body = null; // Object | 
    try {
      apiInstance.collectionsLinkedNodesRelationships(collectionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedNodesRelationships");
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
| **collectionId** | **String**| A short id for that collection | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="collectionsLinkedNodesRelationshipsCreate"></a>
# **collectionsLinkedNodesRelationshipsCreate**
> collectionsLinkedNodesRelationshipsCreate(collectionId)

Give a Sparse List of Node Ids

List of all the node ids linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsLinkedNodesRelationshipsCreate(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedNodesRelationshipsCreate");
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
| **collectionId** | **String**| A short id for that collection | |

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
| **200** | OK |  -  |

<a id="collectionsLinkedNodesRelationshipsDelete"></a>
# **collectionsLinkedNodesRelationshipsDelete**
> collectionsLinkedNodesRelationshipsDelete(collectionId, body)

Remove Nodes From Collection

 This removes associated nodes from a collection #### Permissions Any user with write permissions on this collection should be to remove nodes from this collection. #### Returns Nothing in the response body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    Object body = null; // Object | 
    try {
      apiInstance.collectionsLinkedNodesRelationshipsDelete(collectionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedNodesRelationshipsDelete");
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
| **collectionId** | **String**| A short id for that collection | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsLinkedPreprintsList"></a>
# **collectionsLinkedPreprintsList**
> collectionsLinkedPreprintsList(collectionId)

List All Linked Preprints for a Collection

List of all preprints linked to the given collection. #### Permissions This returns all public preprints associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsLinkedPreprintsList(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedPreprintsList");
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
| **collectionId** | **String**| A short id for that collection | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, links, meta

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsLinkedRegistrationsList"></a>
# **collectionsLinkedRegistrationsList**
> collectionsLinkedRegistrationsList(collectionId)

List All Linked Registrations for a Collection

List of all registrations linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsLinkedRegistrationsList(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedRegistrationsList");
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
| **collectionId** | **String**| A short id for that collection | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, links, meta

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsLinkedRegistrationsRelationships"></a>
# **collectionsLinkedRegistrationsRelationships**
> collectionsLinkedRegistrationsRelationships(collectionId, body)

Link Registrations to Collection

This endpoint allow users to a add a registration to a collection by issuing a POST request. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    Object body = null; // Object | 
    try {
      apiInstance.collectionsLinkedRegistrationsRelationships(collectionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedRegistrationsRelationships");
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
| **collectionId** | **String**| A short id for that collection | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="collectionsLinkedRegistrationsRelationshipsCreate"></a>
# **collectionsLinkedRegistrationsRelationshipsCreate**
> collectionsLinkedRegistrationsRelationshipsCreate(collectionId)

Give a Sparse List of Registrations Ids

List of all the registration ids linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsLinkedRegistrationsRelationshipsCreate(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedRegistrationsRelationshipsCreate");
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
| **collectionId** | **String**| A short id for that collection | |

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
| **200** | OK |  -  |

<a id="collectionsLinkedRegistrationsRelationshipsDelete"></a>
# **collectionsLinkedRegistrationsRelationshipsDelete**
> collectionsLinkedRegistrationsRelationshipsDelete(collectionId, body)

Remove Registrations From Collection

 This removes associated registrations from a collection #### Permissions Any user with write permissions on this collection should be to remove registrations from this collection. #### Returns Nothing in the response body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    Object body = null; // Object | 
    try {
      apiInstance.collectionsLinkedRegistrationsRelationshipsDelete(collectionId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsLinkedRegistrationsRelationshipsDelete");
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
| **collectionId** | **String**| A short id for that collection | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsList"></a>
# **collectionsList**
> List&lt;Collection&gt; collectionsList()

List all Collections

Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    try {
      List<Collection> result = apiInstance.collectionsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Collection&gt;**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsMetadataDelete"></a>
# **collectionsMetadataDelete**
> collectionsMetadataDelete(collectionId, cgmId)

Delete Collection Metadata from entitiy

 #### Permissions Only a user with collection admin permissions can delete collected metadata #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    try {
      apiInstance.collectionsMetadataDelete(collectionId, cgmId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataDelete");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | NO CONTENT |  -  |

<a id="collectionsMetadataDetail"></a>
# **collectionsMetadataDetail**
> collectionsMetadataDetail(collectionId, cgmId, body)

Add Metadata or Subjects to an Entity in a Collection

List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    Object body = null; // Object | 
    try {
      apiInstance.collectionsMetadataDetail(collectionId, cgmId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataDetail");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="collectionsMetadataRegistrationsDetail"></a>
# **collectionsMetadataRegistrationsDetail**
> collectionsMetadataRegistrationsDetail(collectionId, cgmId)

Retrieve Specific Metadata for a Collection

 #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    try {
      apiInstance.collectionsMetadataRegistrationsDetail(collectionId, cgmId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataRegistrationsDetail");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: data, meta

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionsMetadataRegistrationsList"></a>
# **collectionsMetadataRegistrationsList**
> collectionsMetadataRegistrationsList(collectionId)

Retrieve a list of collected metadata for a collection

List of user created metadata for entities within a collection. #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    try {
      apiInstance.collectionsMetadataRegistrationsList(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataRegistrationsList");
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
| **collectionId** | **String**| A short id for that collection | |

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
| **200** | OK |  -  |

<a id="collectionsMetadataSubjectsRelationships"></a>
# **collectionsMetadataSubjectsRelationships**
> collectionsMetadataSubjectsRelationships(collectionId, cgmId)

Retrieve subject metadata for a specific piece of metadata in a collection

 #### Permissions This is public for a logged out user when an entity is public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    try {
      apiInstance.collectionsMetadataSubjectsRelationships(collectionId, cgmId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataSubjectsRelationships");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |

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
| **200** | OK |  -  |

<a id="collectionsMetadataSubjectsRelationshipsUpdate"></a>
# **collectionsMetadataSubjectsRelationshipsUpdate**
> collectionsMetadataSubjectsRelationshipsUpdate(collectionId, cgmId, body)

Update subjects for a specific piece of metadata in a collection

 #### Permissions This is editable for a user with a write permission for this collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CollectionsApi apiInstance = new CollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | A short id for that collection
    String cgmId = "cgmId_example"; // String | A short id for that piece of metadata
    Object body = null; // Object | 
    try {
      apiInstance.collectionsMetadataSubjectsRelationshipsUpdate(collectionId, cgmId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionsApi#collectionsMetadataSubjectsRelationshipsUpdate");
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
| **collectionId** | **String**| A short id for that collection | |
| **cgmId** | **String**| A short id for that piece of metadata | |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

