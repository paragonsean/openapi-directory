# CollectionApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCollection2UsingPOST**](CollectionApi.md#addCollection2UsingPOST) | **POST** /rest/v1.1/collection/collection | Create new empty collection with given name |
| [**addCollectionUsingPOST**](CollectionApi.md#addCollectionUsingPOST) | **POST** /rest/v1.1/collection/ | Create new empty collection with given name |
| [**deleteCollection2UsingDELETE**](CollectionApi.md#deleteCollection2UsingDELETE) | **DELETE** /rest/v1.1/collection/collection | Delete existing collection with associated profiles and faces. |
| [**deleteCollectionUsingDELETE**](CollectionApi.md#deleteCollectionUsingDELETE) | **DELETE** /rest/v1.1/collection/{id} | Delete existing collection with associated profiles and faces. |
| [**exportCSVUsingGET**](CollectionApi.md#exportCSVUsingGET) | **GET** /rest/v1.1/collection/export/csv | Retrieve collection content for data analysis. |
| [**getAllCollectionProfilesUsingGET**](CollectionApi.md#getAllCollectionProfilesUsingGET) | **GET** /rest/v1.1/collection/{id}/profile | Gets all the profiles associated to a collection |
| [**getAllCollections2UsingGET**](CollectionApi.md#getAllCollections2UsingGET) | **GET** /rest/v1.1/collection/all | Retrieve all collections |
| [**getAllCollectionsUsingGET**](CollectionApi.md#getAllCollectionsUsingGET) | **GET** /rest/v1.1/collection/ | Retrieve all collections |
| [**getCollection2UsingGET**](CollectionApi.md#getCollection2UsingGET) | **GET** /rest/v1.1/collection/collection | Retrieve existing collection content |
| [**getCollectionUsingGET**](CollectionApi.md#getCollectionUsingGET) | **GET** /rest/v1.1/collection/{id} | Retrieve existing collection content |
| [**repurposeCollectionUsingPUT**](CollectionApi.md#repurposeCollectionUsingPUT) | **PUT** /rest/v1.1/collection/purpose | Change purpose of existing collection |
| [**updateCollection2UsingPOST**](CollectionApi.md#updateCollection2UsingPOST) | **POST** /rest/v1.1/collection/{id} | Update an existing collection with a given id |
| [**updateCollectionUsingPATCH**](CollectionApi.md#updateCollectionUsingPATCH) | **PATCH** /rest/v1.1/collection/{id} | Update an existing collection with a given id |


<a id="addCollection2UsingPOST"></a>
# **addCollection2UsingPOST**
> RestResponse addCollection2UsingPOST(accessKey, secretKey, collectionName, preload, evictable, purposes)

Create new empty collection with given name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String collectionName = "collectionName_example"; // String | The name of the collection that will be created
    Boolean preload = false; // Boolean | Defined whether to preload collection
    Boolean evictable = true; // Boolean | Defined whether the collection can be evicted
    List<String> purposes = Arrays.asList(); // List<String> | The newly declared purposes of the collection
    try {
      RestResponse result = apiInstance.addCollection2UsingPOST(accessKey, secretKey, collectionName, preload, evictable, purposes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#addCollection2UsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionName** | **String**| The name of the collection that will be created | |
| **preload** | **Boolean**| Defined whether to preload collection | [optional] [default to false] |
| **evictable** | **Boolean**| Defined whether the collection can be evicted | [optional] [default to true] |
| **purposes** | [**List&lt;String&gt;**](String.md)| The newly declared purposes of the collection | [optional] [enum: FEATURES, LANDMARKS, ATTRIBUTES] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="addCollectionUsingPOST"></a>
# **addCollectionUsingPOST**
> RestResponse addCollectionUsingPOST(accessKey, secretKey, name, preload, evictable, purposes)

Create new empty collection with given name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String name = "name_example"; // String | The name of the collection that will be created
    Boolean preload = false; // Boolean | Defined whether to preload collection
    Boolean evictable = true; // Boolean | Defined whether the collection can be evicted
    List<String> purposes = Arrays.asList(); // List<String> | The newly declared purposes of the collection
    try {
      RestResponse result = apiInstance.addCollectionUsingPOST(accessKey, secretKey, name, preload, evictable, purposes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#addCollectionUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **name** | **String**| The name of the collection that will be created | |
| **preload** | **Boolean**| Defined whether to preload collection | [optional] [default to false] |
| **evictable** | **Boolean**| Defined whether the collection can be evicted | [optional] [default to true] |
| **purposes** | [**List&lt;String&gt;**](String.md)| The newly declared purposes of the collection | [optional] [enum: FEATURES, LANDMARKS, ATTRIBUTES] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="deleteCollection2UsingDELETE"></a>
# **deleteCollection2UsingDELETE**
> RestResponse deleteCollection2UsingDELETE(accessKey, secretKey, collectionId)

Delete existing collection with associated profiles and faces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | The id of the collection that will be removed
    try {
      RestResponse result = apiInstance.deleteCollection2UsingDELETE(accessKey, secretKey, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#deleteCollection2UsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **collectionId** | **String**| The id of the collection that will be removed | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="deleteCollectionUsingDELETE"></a>
# **deleteCollectionUsingDELETE**
> RestResponse deleteCollectionUsingDELETE(accessKey, secretKey, id)

Delete existing collection with associated profiles and faces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String id = "id_example"; // String | The id of the collection that will be removed
    try {
      RestResponse result = apiInstance.deleteCollectionUsingDELETE(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#deleteCollectionUsingDELETE");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **id** | **String**| The id of the collection that will be removed | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="exportCSVUsingGET"></a>
# **exportCSVUsingGET**
> Object exportCSVUsingGET(accessKey, secretKey, collectionId)

Retrieve collection content for data analysis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
    try {
      Object result = apiInstance.exportCSVUsingGET(accessKey, secretKey, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#exportCSVUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionId** | **String**| The id of the collection for which the data will be retrieved | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAllCollectionProfilesUsingGET"></a>
# **getAllCollectionProfilesUsingGET**
> RestResponse getAllCollectionProfilesUsingGET(accessKey, secretKey, id)

Gets all the profiles associated to a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The collection that contains the profile
    try {
      RestResponse result = apiInstance.getAllCollectionProfilesUsingGET(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getAllCollectionProfilesUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **id** | **String**| The collection that contains the profile | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAllCollections2UsingGET"></a>
# **getAllCollections2UsingGET**
> RestResponse getAllCollections2UsingGET(accessKey, secretKey)

Retrieve all collections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    try {
      RestResponse result = apiInstance.getAllCollections2UsingGET(accessKey, secretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getAllCollections2UsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAllCollectionsUsingGET"></a>
# **getAllCollectionsUsingGET**
> RestResponse getAllCollectionsUsingGET(accessKey, secretKey)

Retrieve all collections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    try {
      RestResponse result = apiInstance.getAllCollectionsUsingGET(accessKey, secretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getAllCollectionsUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getCollection2UsingGET"></a>
# **getCollection2UsingGET**
> RestResponse getCollection2UsingGET(accessKey, secretKey, collectionId)

Retrieve existing collection content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
    try {
      RestResponse result = apiInstance.getCollection2UsingGET(accessKey, secretKey, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollection2UsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionId** | **String**| The id of the collection for which the data will be retrieved | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getCollectionUsingGET"></a>
# **getCollectionUsingGET**
> RestResponse getCollectionUsingGET(accessKey, secretKey, id)

Retrieve existing collection content

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The id of the collection for which the data will be retrieved
    try {
      RestResponse result = apiInstance.getCollectionUsingGET(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#getCollectionUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **id** | **String**| The id of the collection for which the data will be retrieved | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="repurposeCollectionUsingPUT"></a>
# **repurposeCollectionUsingPUT**
> RestResponse repurposeCollectionUsingPUT(accessKey, secretKey, collectionId, purposes)

Change purpose of existing collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | The id of the collection for which the data will be retrieved
    List<String> purposes = Arrays.asList(); // List<String> | The newly declared purposes of the collection
    try {
      RestResponse result = apiInstance.repurposeCollectionUsingPUT(accessKey, secretKey, collectionId, purposes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#repurposeCollectionUsingPUT");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **collectionId** | **String**| The id of the collection for which the data will be retrieved | |
| **purposes** | [**List&lt;String&gt;**](String.md)| The newly declared purposes of the collection | [enum: FEATURES, LANDMARKS, ATTRIBUTES] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateCollection2UsingPOST"></a>
# **updateCollection2UsingPOST**
> RestResponse updateCollection2UsingPOST(accessKey, secretKey, id, name, purposes)

Update an existing collection with a given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String id = "id_example"; // String | The id of the collection that will be updated
    String name = "name_example"; // String | The name of the collection that will be updated
    List<String> purposes = Arrays.asList(); // List<String> | The newly declared purposes of the collection
    try {
      RestResponse result = apiInstance.updateCollection2UsingPOST(accessKey, secretKey, id, name, purposes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#updateCollection2UsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **id** | **String**| The id of the collection that will be updated | |
| **name** | **String**| The name of the collection that will be updated | [optional] |
| **purposes** | [**List&lt;String&gt;**](String.md)| The newly declared purposes of the collection | [optional] [enum: FEATURES, LANDMARKS, ATTRIBUTES] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateCollectionUsingPATCH"></a>
# **updateCollectionUsingPATCH**
> RestResponse updateCollectionUsingPATCH(accessKey, secretKey, id, name, purposes)

Update an existing collection with a given id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
    String id = "id_example"; // String | The id of the collection that will be updated
    String name = "name_example"; // String | The name of the collection that will be updated
    List<String> purposes = Arrays.asList(); // List<String> | The newly declared purposes of the collection
    try {
      RestResponse result = apiInstance.updateCollectionUsingPATCH(accessKey, secretKey, id, name, purposes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#updateCollectionUsingPATCH");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey provided by VisageCloud | |
| **id** | **String**| The id of the collection that will be updated | |
| **name** | **String**| The name of the collection that will be updated | [optional] |
| **purposes** | [**List&lt;String&gt;**](String.md)| The newly declared purposes of the collection | [optional] [enum: FEATURES, LANDMARKS, ATTRIBUTES] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

