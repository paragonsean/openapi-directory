# AuthorizationCodeDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2AuthorizationCodeDefinitionsIdGet**](AuthorizationCodeDefinitionsApi.md#apiV2AuthorizationCodeDefinitionsIdGet) | **GET** /api/v2/AuthorizationCodeDefinitions/{id} | Get an authorization code definition by its ID |
| [**authorizationCodeDefinitionsAddCategoryToDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsAddCategoryToDefinition) | **POST** /api/v2/AuthorizationCodeDefinitions/{ID}/Categories/{categoryID} | Add a category to an authorizationCodeDefintion. |
| [**authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition) | **DELETE** /api/v2/AuthorizationCodeDefinitions/{id} | Disable an authorization code definition |
| [**authorizationCodeDefinitionsGetAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsGetAuthorizationCodeDefinition) | **GET** /api/v2/AuthorizationCodeDefinitions | Get authorization code definitions. |
| [**authorizationCodeDefinitionsPostAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsPostAuthorizationCodeDefinition) | **POST** /api/v2/AuthorizationCodeDefinitions | Add an authorization code definition. |
| [**authorizationCodeDefinitionsPutAuthorizationCodeDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsPutAuthorizationCodeDefinition) | **PUT** /api/v2/AuthorizationCodeDefinitions/{id} | Update an authorization code definition |
| [**authorizationCodeDefinitionsRemoveCategoryFromDefinition**](AuthorizationCodeDefinitionsApi.md#authorizationCodeDefinitionsRemoveCategoryFromDefinition) | **DELETE** /api/v2/AuthorizationCodeDefinitions/{ID}/Categories/{categoryID} | Deletes the category from the authorization code definition. |


<a id="apiV2AuthorizationCodeDefinitionsIdGet"></a>
# **apiV2AuthorizationCodeDefinitionsIdGet**
> AuthorizationCodesSharedModelsAuthorizationCodeDefinition apiV2AuthorizationCodeDefinitionsIdGet(id)

Get an authorization code definition by its ID

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    String id = "id_example"; // String | The ID of the authorization code definition.
    try {
      AuthorizationCodesSharedModelsAuthorizationCodeDefinition result = apiInstance.apiV2AuthorizationCodeDefinitionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#apiV2AuthorizationCodeDefinitionsIdGet");
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
| **id** | **String**| The ID of the authorization code definition. | |

### Return type

[**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsAddCategoryToDefinition"></a>
# **authorizationCodeDefinitionsAddCategoryToDefinition**
> authorizationCodeDefinitionsAddCategoryToDefinition(ID, categoryID)

Add a category to an authorizationCodeDefintion.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    String ID = "ID_example"; // String | 
    String categoryID = "categoryID_example"; // String | A category ID, as a GUID.
    try {
      apiInstance.authorizationCodeDefinitionsAddCategoryToDefinition(ID, categoryID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsAddCategoryToDefinition");
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
| **ID** | **String**|  | |
| **categoryID** | **String**| A category ID, as a GUID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition"></a>
# **authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition**
> authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition(id)

Disable an authorization code definition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    String id = "id_example"; // String | The ID of the authorization code definition.
    try {
      apiInstance.authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsDeleteAuthorizationCodeDefinition");
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
| **id** | **String**| The ID of the authorization code definition. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsGetAuthorizationCodeDefinition"></a>
# **authorizationCodeDefinitionsGetAuthorizationCodeDefinition**
> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition authorizationCodeDefinitionsGetAuthorizationCodeDefinition(limit, offset, name, createdByUserID, deletedByUserID, includeDeleted, categoryID)

Get authorization code definitions.

Additional searches: validationFields[Name]&#x3D;true and dataFields[Name]&#x3D;true. These can be used to search for authorization code definitions that have the specified data or validation fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String name = "name_example"; // String | Optional. If specified, filters definitions by name. Starting and ending wildcards (*) supported.
    Integer createdByUserID = 56; // Integer | Optional. If specified, filters definitions to those created by the given User ID.
    Integer deletedByUserID = 56; // Integer | Optional. If specified, filters definitions to those deleted by the given User ID.
    Boolean includeDeleted = true; // Boolean | Optional. Whether to include deleted definitions. 'False' by default.
    String categoryID = "categoryID_example"; // String | Optional. If specified, filters definitions with the designated categoryID.
    try {
      APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition result = apiInstance.authorizationCodeDefinitionsGetAuthorizationCodeDefinition(limit, offset, name, createdByUserID, deletedByUserID, includeDeleted, categoryID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsGetAuthorizationCodeDefinition");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **name** | **String**| Optional. If specified, filters definitions by name. Starting and ending wildcards (*) supported. | [optional] |
| **createdByUserID** | **Integer**| Optional. If specified, filters definitions to those created by the given User ID. | [optional] |
| **deletedByUserID** | **Integer**| Optional. If specified, filters definitions to those deleted by the given User ID. | [optional] |
| **includeDeleted** | **Boolean**| Optional. Whether to include deleted definitions. &#39;False&#39; by default. | [optional] |
| **categoryID** | **String**| Optional. If specified, filters definitions with the designated categoryID. | [optional] |

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsPostAuthorizationCodeDefinition"></a>
# **authorizationCodeDefinitionsPostAuthorizationCodeDefinition**
> String authorizationCodeDefinitionsPostAuthorizationCodeDefinition(authorizationCodesSharedModelsAuthorizationCodeDefinition)

Add an authorization code definition.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    AuthorizationCodesSharedModelsAuthorizationCodeDefinition authorizationCodesSharedModelsAuthorizationCodeDefinition = new AuthorizationCodesSharedModelsAuthorizationCodeDefinition(); // AuthorizationCodesSharedModelsAuthorizationCodeDefinition | An authorization code definition.
    try {
      String result = apiInstance.authorizationCodeDefinitionsPostAuthorizationCodeDefinition(authorizationCodesSharedModelsAuthorizationCodeDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsPostAuthorizationCodeDefinition");
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
| **authorizationCodesSharedModelsAuthorizationCodeDefinition** | [**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)| An authorization code definition. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsPutAuthorizationCodeDefinition"></a>
# **authorizationCodeDefinitionsPutAuthorizationCodeDefinition**
> authorizationCodeDefinitionsPutAuthorizationCodeDefinition(id, authorizationCodesSharedModelsAuthorizationCodeDefinition)

Update an authorization code definition

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    String id = "id_example"; // String | The ID of the authorization code definition.
    AuthorizationCodesSharedModelsAuthorizationCodeDefinition authorizationCodesSharedModelsAuthorizationCodeDefinition = new AuthorizationCodesSharedModelsAuthorizationCodeDefinition(); // AuthorizationCodesSharedModelsAuthorizationCodeDefinition | An authorization code definition.
    try {
      apiInstance.authorizationCodeDefinitionsPutAuthorizationCodeDefinition(id, authorizationCodesSharedModelsAuthorizationCodeDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsPutAuthorizationCodeDefinition");
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
| **id** | **String**| The ID of the authorization code definition. | |
| **authorizationCodesSharedModelsAuthorizationCodeDefinition** | [**AuthorizationCodesSharedModelsAuthorizationCodeDefinition**](AuthorizationCodesSharedModelsAuthorizationCodeDefinition.md)| An authorization code definition. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCodeDefinitionsRemoveCategoryFromDefinition"></a>
# **authorizationCodeDefinitionsRemoveCategoryFromDefinition**
> authorizationCodeDefinitionsRemoveCategoryFromDefinition(ID, categoryID)

Deletes the category from the authorization code definition.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodeDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodeDefinitionsApi apiInstance = new AuthorizationCodeDefinitionsApi(defaultClient);
    String ID = "ID_example"; // String | 
    String categoryID = "categoryID_example"; // String | A category ID, as a GUID.
    try {
      apiInstance.authorizationCodeDefinitionsRemoveCategoryFromDefinition(ID, categoryID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodeDefinitionsApi#authorizationCodeDefinitionsRemoveCategoryFromDefinition");
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
| **ID** | **String**|  | |
| **categoryID** | **String**| A category ID, as a GUID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

