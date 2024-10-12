# GuidsApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addGuidAlias_0**](GuidsApi.md#addGuidAlias_0) | **POST** /api/v1/id4ns/{id4n}/alias/{aliasType} | Add alias for GUID or Collection |
| [**createGuid**](GuidsApi.md#createGuid) | **POST** /api/v1/guids | Create GUID(s) |
| [**deleteProperties_0**](GuidsApi.md#deleteProperties_0) | **DELETE** /api/v1/id4ns/{id4n}/properties | Delete ID4n properties |
| [**getCollections**](GuidsApi.md#getCollections) | **GET** /api/v1/id4ns/{id4n}/collections | Retrieve collections of an ID |
| [**getGuid**](GuidsApi.md#getGuid) | **GET** /api/v1/guids/{id4n} | Retrieve GUID information |
| [**getGuidAliases_0**](GuidsApi.md#getGuidAliases_0) | **GET** /api/v1/id4ns/{id4n}/alias | Get all aliases for the given GUID or Collection. |
| [**getGuidsWithoutCollection**](GuidsApi.md#getGuidsWithoutCollection) | **GET** /api/v1/guids/withoutCollection | Retrieve GUIDs not in any collection |
| [**getId4n**](GuidsApi.md#getId4n) | **GET** /api/v1/id4ns/{id4n} | Retrieve ID4n information |
| [**getMultipleProperties_0**](GuidsApi.md#getMultipleProperties_0) | **GET** /api/v1/multiple/id4ns/properties | Get multiple ID4n properties |
| [**getProperties_0**](GuidsApi.md#getProperties_0) | **GET** /api/v1/id4ns/{id4n}/properties | Retrieve ID4n properties |
| [**importGS1Codes**](GuidsApi.md#importGS1Codes) | **POST** /api/v1/import/gs1 | Import GS1/MAPP codes |
| [**patchProperties_0**](GuidsApi.md#patchProperties_0) | **PATCH** /api/v1/id4ns/{id4n}/properties | Patch ID4n properties |
| [**removeGuidAlias_0**](GuidsApi.md#removeGuidAlias_0) | **DELETE** /api/v1/id4ns/{id4n}/alias/{aliasType} | Remove aliases from GUID or Collection |
| [**updateGuid**](GuidsApi.md#updateGuid) | **PATCH** /api/v1/guids/{id4n} | Change GUID information. |


<a id="addGuidAlias_0"></a>
# **addGuidAlias_0**
> addGuidAlias_0(id4n, aliasType, guidAlias)

Add alias for GUID or Collection

Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The GUID or Collection to operate on
    String aliasType = "gtin"; // String | Alias type, see the corresponding API model
    GuidAlias guidAlias = new GuidAlias(); // GuidAlias | The alias to add or update
    try {
      apiInstance.addGuidAlias_0(id4n, aliasType, guidAlias);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#addGuidAlias_0");
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
| **id4n** | **String**| The GUID or Collection to operate on | |
| **aliasType** | **String**| Alias type, see the corresponding API model | [enum: gtin, article, mapp, item, rfid, tracking, eclass, unspsc, product, material, reference] |
| **guidAlias** | [**GuidAlias**](GuidAlias.md)| The alias to add or update | |

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

<a id="createGuid"></a>
# **createGuid**
> ListOfId4ns createGuid(createGuidRequest)

Create GUID(s)

Creating one or more GUIDs with a specified length.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    CreateGuidRequest createGuidRequest = new CreateGuidRequest(); // CreateGuidRequest | GUID creation model
    try {
      ListOfId4ns result = apiInstance.createGuid(createGuidRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#createGuid");
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
| **createGuidRequest** | [**CreateGuidRequest**](CreateGuidRequest.md)| GUID creation model | |

### Return type

[**ListOfId4ns**](ListOfId4ns.md)

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

<a id="deleteProperties_0"></a>
# **deleteProperties_0**
> deleteProperties_0(id4n, organizationId, requestBody)

Delete ID4n properties

Partial deletion of id4n properties. If the property does not exist, it will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The id4n
    String organizationId = "organizationId_example"; // String | The organization namespace to work on while deleting the properties.
    List<String> requestBody = Arrays.asList(); // List<String> | A set of property keys to delete.
    try {
      apiInstance.deleteProperties_0(id4n, organizationId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#deleteProperties_0");
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
| **id4n** | **String**| The id4n | |
| **organizationId** | **String**| The organization namespace to work on while deleting the properties. | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| A set of property keys to delete. | |

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
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="getCollections"></a>
# **getCollections**
> PaginatedResponseOfGuidCollection getCollections(id4n, organizationId, offset, limit)

Retrieve collections of an ID

Retrieving all owned or holding collections the specified id4n is assigned to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The ID which the collections should contain
    String organizationId = "organizationId_example"; // String | The organization holding the collections.
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfGuidCollection result = apiInstance.getCollections(id4n, organizationId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getCollections");
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
| **id4n** | **String**| The ID which the collections should contain | |
| **organizationId** | **String**| The organization holding the collections. | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfGuidCollection**](PaginatedResponseOfGuidCollection.md)

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

<a id="getGuid"></a>
# **getGuid**
> Guid getGuid(id4n, organizationId)

Retrieve GUID information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The GUID number
    String organizationId = "organizationId_example"; // String | The organization namespace to resolve.
    try {
      Guid result = apiInstance.getGuid(id4n, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getGuid");
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
| **id4n** | **String**| The GUID number | |
| **organizationId** | **String**| The organization namespace to resolve. | [optional] |

### Return type

[**Guid**](Guid.md)

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

<a id="getGuidAliases_0"></a>
# **getGuidAliases_0**
> Map&lt;String, String&gt; getGuidAliases_0(id4n)

Get all aliases for the given GUID or Collection.

Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The GUID or Collection to operate on
    try {
      Map<String, String> result = apiInstance.getGuidAliases_0(id4n);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getGuidAliases_0");
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
| **id4n** | **String**| The GUID or Collection to operate on | |

### Return type

**Map&lt;String, String&gt;**

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

<a id="getGuidsWithoutCollection"></a>
# **getGuidsWithoutCollection**
> PaginatedResponseOfGuid getGuidsWithoutCollection(organizationId, offset, limit)

Retrieve GUIDs not in any collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | The namespace of the organization to search GUIDs for
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfGuid result = apiInstance.getGuidsWithoutCollection(organizationId, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getGuidsWithoutCollection");
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
| **organizationId** | **String**| The namespace of the organization to search GUIDs for | |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfGuid**](PaginatedResponseOfGuid.md)

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

<a id="getId4n"></a>
# **getId4n**
> Id4nPresentation getId4n(id4n, organizationId)

Retrieve ID4n information

Retrieving basic information about an ID like the type and the creation time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The ID to resolve to
    String organizationId = "organizationId_example"; // String | The organization namespace to resolve.
    try {
      Id4nPresentation result = apiInstance.getId4n(id4n, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getId4n");
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
| **id4n** | **String**| The ID to resolve to | |
| **organizationId** | **String**| The organization namespace to resolve. | [optional] |

### Return type

[**Id4nPresentation**](Id4nPresentation.md)

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

<a id="getMultipleProperties_0"></a>
# **getMultipleProperties_0**
> ListOfId4nProperties getMultipleProperties_0(id4ns, organizationId)

Get multiple ID4n properties

Get a list of ID4n properties for the specified ID4ns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    List<String> id4ns = Arrays.asList(); // List<String> | The list of ID4ns to resolve.
    String organizationId = "organizationId_example"; // String | The organization namespace.
    try {
      ListOfId4nProperties result = apiInstance.getMultipleProperties_0(id4ns, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getMultipleProperties_0");
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
| **id4ns** | [**List&lt;String&gt;**](String.md)| The list of ID4ns to resolve. | |
| **organizationId** | **String**| The organization namespace. | [optional] |

### Return type

[**ListOfId4nProperties**](ListOfId4nProperties.md)

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

<a id="getProperties_0"></a>
# **getProperties_0**
> Map&lt;String, String&gt; getProperties_0(id4n, organizationId)

Retrieve ID4n properties

List all properties of an id4n.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The id4n
    String organizationId = "organizationId_example"; // String | The organization namespace.
    try {
      Map<String, String> result = apiInstance.getProperties_0(id4n, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#getProperties_0");
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
| **id4n** | **String**| The id4n | |
| **organizationId** | **String**| The organization namespace. | [optional] |

### Return type

**Map&lt;String, String&gt;**

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

<a id="importGS1Codes"></a>
# **importGS1Codes**
> importGS1Codes(importGS1CodesRequest)

Import GS1/MAPP codes

Importing GS1/MAPP codes that contain unique components.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    ImportGS1CodesRequest importGS1CodesRequest = new ImportGS1CodesRequest(); // ImportGS1CodesRequest | The information how the MAPP codes should be imported and the list of MAPP codes
    try {
      apiInstance.importGS1Codes(importGS1CodesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#importGS1Codes");
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
| **importGS1CodesRequest** | [**ImportGS1CodesRequest**](ImportGS1CodesRequest.md)| The information how the MAPP codes should be imported and the list of MAPP codes | |

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

<a id="patchProperties_0"></a>
# **patchProperties_0**
> patchProperties_0(id4n, organizationId, requestBody)

Patch ID4n properties

Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The id4n
    String organizationId = "organizationId_example"; // String | The organization namespace to work on while patching the properties.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | The properties to update.
    try {
      apiInstance.patchProperties_0(id4n, organizationId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#patchProperties_0");
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
| **id4n** | **String**| The id4n | |
| **organizationId** | **String**| The organization namespace to work on while patching the properties. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)| The properties to update. | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="removeGuidAlias_0"></a>
# **removeGuidAlias_0**
> removeGuidAlias_0(id4n, aliasType)

Remove aliases from GUID or Collection

Remove the alias of the given type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The GUID or Collection to operate on
    String aliasType = "gtin"; // String | Alias type, see the corresponding API model
    try {
      apiInstance.removeGuidAlias_0(id4n, aliasType);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#removeGuidAlias_0");
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
| **id4n** | **String**| The GUID or Collection to operate on | |
| **aliasType** | **String**| Alias type, see the corresponding API model | [enum: gtin, article, mapp, item, rfid, tracking, eclass, unspsc, product, material, reference] |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="updateGuid"></a>
# **updateGuid**
> Object updateGuid(id4n, guid)

Change GUID information.

Allows ownership transfer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuidsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    GuidsApi apiInstance = new GuidsApi(defaultClient);
    String id4n = "id4n_example"; // String | The GUID number
    Guid guid = new Guid(); // Guid | request
    try {
      Object result = apiInstance.updateGuid(id4n, guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuidsApi#updateGuid");
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
| **id4n** | **String**| The GUID number | |
| **guid** | [**Guid**](Guid.md)| request | |

### Return type

**Object**

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

