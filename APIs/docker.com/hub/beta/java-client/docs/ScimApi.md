# ScimApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2Scim20ResourceTypesGet**](ScimApi.md#v2Scim20ResourceTypesGet) | **GET** /v2/scim/2.0/ResourceTypes | List resource types |
| [**v2Scim20ResourceTypesNameGet**](ScimApi.md#v2Scim20ResourceTypesNameGet) | **GET** /v2/scim/2.0/ResourceTypes/{name} | Get a resource type |
| [**v2Scim20SchemasGet**](ScimApi.md#v2Scim20SchemasGet) | **GET** /v2/scim/2.0/Schemas | List schemas |
| [**v2Scim20SchemasIdGet**](ScimApi.md#v2Scim20SchemasIdGet) | **GET** /v2/scim/2.0/Schemas/{id} | Get a schema |
| [**v2Scim20ServiceProviderConfigGet**](ScimApi.md#v2Scim20ServiceProviderConfigGet) | **GET** /v2/scim/2.0/ServiceProviderConfig | Get service provider config |
| [**v2Scim20UsersGet**](ScimApi.md#v2Scim20UsersGet) | **GET** /v2/scim/2.0/Users | List users |
| [**v2Scim20UsersIdGet**](ScimApi.md#v2Scim20UsersIdGet) | **GET** /v2/scim/2.0/Users/{id} | Get a user |
| [**v2Scim20UsersIdPut**](ScimApi.md#v2Scim20UsersIdPut) | **PUT** /v2/scim/2.0/Users/{id} | Update a user |
| [**v2Scim20UsersPost**](ScimApi.md#v2Scim20UsersPost) | **POST** /v2/scim/2.0/Users | Create user |


<a id="v2Scim20ResourceTypesGet"></a>
# **v2Scim20ResourceTypesGet**
> V2Scim20ResourceTypesGet200Response v2Scim20ResourceTypesGet()

List resource types

Returns all resource types supported for the SCIM configuration. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    try {
      V2Scim20ResourceTypesGet200Response result = apiInstance.v2Scim20ResourceTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20ResourceTypesGet");
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

[**V2Scim20ResourceTypesGet200Response**](V2Scim20ResourceTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20ResourceTypesNameGet"></a>
# **v2Scim20ResourceTypesNameGet**
> ScimResourceType v2Scim20ResourceTypesNameGet(name)

Get a resource type

Returns a resource type by name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    String name = "User"; // String | 
    try {
      ScimResourceType result = apiInstance.v2Scim20ResourceTypesNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20ResourceTypesNameGet");
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
| **name** | **String**|  | |

### Return type

[**ScimResourceType**](ScimResourceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20SchemasGet"></a>
# **v2Scim20SchemasGet**
> V2Scim20SchemasGet200Response v2Scim20SchemasGet()

List schemas

Returns all schemas supported for the SCIM configuration. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    try {
      V2Scim20SchemasGet200Response result = apiInstance.v2Scim20SchemasGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20SchemasGet");
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

[**V2Scim20SchemasGet200Response**](V2Scim20SchemasGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20SchemasIdGet"></a>
# **v2Scim20SchemasIdGet**
> ScimSchema v2Scim20SchemasIdGet(id)

Get a schema

Returns a schema by ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    String id = "urn:ietf:params:scim:schemas:core:2.0:User"; // String | 
    try {
      ScimSchema result = apiInstance.v2Scim20SchemasIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20SchemasIdGet");
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
| **id** | **String**|  | |

### Return type

[**ScimSchema**](ScimSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20ServiceProviderConfigGet"></a>
# **v2Scim20ServiceProviderConfigGet**
> ScimServiceProviderConfig v2Scim20ServiceProviderConfigGet()

Get service provider config

Returns a service provider config for Docker&#39;s configuration. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    try {
      ScimServiceProviderConfig result = apiInstance.v2Scim20ServiceProviderConfigGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20ServiceProviderConfigGet");
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

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20UsersGet"></a>
# **v2Scim20UsersGet**
> V2Scim20UsersGet200Response v2Scim20UsersGet(startIndex, count, filter, attributes, sortOrder, sortBy)

List users

List users, returns paginated users for an organization. Use &#x60;startIndex&#x60; and &#x60;count&#x60; query parameters to receive paginated results.  **Sorting:**&lt;br&gt; Sorting lets you to specify the order of returned resources by specifying a combination of &#x60;sortBy&#x60; and &#x60;sortOrder&#x60; query parameters.  The &#x60;sortBy&#x60; parameter specifies the attribute whose value will be used to order the returned responses. The &#x60;sortOrder&#x60; parameter defines the order in which the &#x60;sortBy&#x60; parameter is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot;.  **Filtering:**&lt;br&gt; You can request a subset of resources by specifying the &#x60;filter&#x60; query parameter containing a filter expression. Attribute names and attribute operators used in filters are case insensitive. The filter parameter must contain at least one valid expression. Each expression must contain an attribute name followed by an attribute operator and an optional value.  Supported operators are listed below.  - &#x60;eq&#x60; equal - &#x60;ne&#x60; not equal - &#x60;co&#x60; contains - &#x60;sw&#x60; starts with - &#x60;and&#x60; Logical \&quot;and\&quot; - &#x60;or&#x60; Logical \&quot;or\&quot; - &#x60;not&#x60; \&quot;Not\&quot; function - &#x60;()&#x60; Precedence grouping 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    Integer startIndex = 1; // Integer | 
    Integer count = 10; // Integer | 
    String filter = "userName eq \"jon.snow@docker.com\""; // String | 
    String attributes = "userName,displayName"; // String | Comma delimited list of attributes to limit to in the response.
    String sortOrder = "ascending"; // String | 
    String sortBy = "userName"; // String | User attribute to sort by.
    try {
      V2Scim20UsersGet200Response result = apiInstance.v2Scim20UsersGet(startIndex, count, filter, attributes, sortOrder, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20UsersGet");
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
| **startIndex** | **Integer**|  | [optional] |
| **count** | **Integer**|  | [optional] |
| **filter** | **String**|  | [optional] |
| **attributes** | **String**| Comma delimited list of attributes to limit to in the response. | [optional] |
| **sortOrder** | **String**|  | [optional] [enum: ascending, descending] |
| **sortBy** | **String**| User attribute to sort by. | [optional] |

### Return type

[**V2Scim20UsersGet200Response**](V2Scim20UsersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20UsersIdGet"></a>
# **v2Scim20UsersIdGet**
> ScimUser v2Scim20UsersIdGet(id)

Get a user

Returns a user by ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    String id = "d80f7c79-7730-49d8-9a41-7c42fb622d9c"; // String | The user ID.
    try {
      ScimUser result = apiInstance.v2Scim20UsersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20UsersIdGet");
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
| **id** | **String**| The user ID. | |

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20UsersIdPut"></a>
# **v2Scim20UsersIdPut**
> ScimUser v2Scim20UsersIdPut(id, v2Scim20UsersIdPutRequest)

Update a user

Updates a user. Use this route to change the user&#39;s name, activate, and deactivate the user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    String id = "d80f7c79-7730-49d8-9a41-7c42fb622d9c"; // String | The user ID.
    V2Scim20UsersIdPutRequest v2Scim20UsersIdPutRequest = new V2Scim20UsersIdPutRequest(); // V2Scim20UsersIdPutRequest | 
    try {
      ScimUser result = apiInstance.v2Scim20UsersIdPut(id, v2Scim20UsersIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20UsersIdPut");
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
| **id** | **String**| The user ID. | |
| **v2Scim20UsersIdPutRequest** | [**V2Scim20UsersIdPutRequest**](V2Scim20UsersIdPutRequest.md)|  | |

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Error |  -  |

<a id="v2Scim20UsersPost"></a>
# **v2Scim20UsersPost**
> ScimUser v2Scim20UsersPost(v2Scim20UsersPostRequest)

Create user

Creates a user. If the user already exists by email, they are assigned to the organization on the \&quot;company\&quot; team. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScimApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    ScimApi apiInstance = new ScimApi(defaultClient);
    V2Scim20UsersPostRequest v2Scim20UsersPostRequest = new V2Scim20UsersPostRequest(); // V2Scim20UsersPostRequest | 
    try {
      ScimUser result = apiInstance.v2Scim20UsersPost(v2Scim20UsersPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScimApi#v2Scim20UsersPost");
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
| **v2Scim20UsersPostRequest** | [**V2Scim20UsersPostRequest**](V2Scim20UsersPostRequest.md)|  | |

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/scim+json
 - **Accept**: application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Error |  -  |

