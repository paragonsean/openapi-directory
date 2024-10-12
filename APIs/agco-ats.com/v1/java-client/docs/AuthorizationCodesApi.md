# AuthorizationCodesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizationCodesDeleteAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesDeleteAuthorizationCode) | **DELETE** /api/v2/AuthorizationCodes/{id} | Hide an authorization code. |
| [**authorizationCodesGetAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesGetAuthorizationCode) | **GET** /api/v2/AuthorizationCodes/{id} | Get an authorization code by its ID. |
| [**authorizationCodesGetAuthorizationCodes**](AuthorizationCodesApi.md#authorizationCodesGetAuthorizationCodes) | **GET** /api/v2/AuthorizationCodes | Get authorization codes. |
| [**authorizationCodesGetContactInformation**](AuthorizationCodesApi.md#authorizationCodesGetContactInformation) | **GET** /api/v2/AuthorizationCodes/{id}/ContactInformation | Get contact information for an authorization code. |
| [**authorizationCodesPostAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesPostAuthorizationCode) | **POST** /api/v2/AuthorizationCodes | Generates an authorization code using the provided definition and parameters. |
| [**authorizationCodesPutAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesPutAuthorizationCode) | **PUT** /api/v2/AuthorizationCodes/{id} | Update an authorization code. |
| [**authorizationCodesValidateAuthorizationCode**](AuthorizationCodesApi.md#authorizationCodesValidateAuthorizationCode) | **GET** /api/v2/AuthorizationCodes/{id}/Validate | No Documentation Found. |


<a id="authorizationCodesDeleteAuthorizationCode"></a>
# **authorizationCodesDeleteAuthorizationCode**
> authorizationCodesDeleteAuthorizationCode(id)

Hide an authorization code.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    Integer id = 56; // Integer | The id of the authorization code.
    try {
      apiInstance.authorizationCodesDeleteAuthorizationCode(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesDeleteAuthorizationCode");
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
| **id** | **Integer**| The id of the authorization code. | |

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

<a id="authorizationCodesGetAuthorizationCode"></a>
# **authorizationCodesGetAuthorizationCode**
> AuthorizationCodesSharedModelsAuthorizationCode authorizationCodesGetAuthorizationCode(id)

Get an authorization code by its ID.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    Integer id = 56; // Integer | The id of the authorization code.
    try {
      AuthorizationCodesSharedModelsAuthorizationCode result = apiInstance.authorizationCodesGetAuthorizationCode(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesGetAuthorizationCode");
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
| **id** | **Integer**| The id of the authorization code. | |

### Return type

[**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)

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

<a id="authorizationCodesGetAuthorizationCodes"></a>
# **authorizationCodesGetAuthorizationCodes**
> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode authorizationCodesGetAuthorizationCodes(code, limit, offset, definitionID, createdByUserID, deletedByUserID, includeDeleted)

Get authorization codes.

Additional searches: validationParameters[Name]&#x3D;Value and dataParameters[Name]&#x3D;Value. These can be used to search for authorization codes that have been generated using specified values for data or validation parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    String code = "code_example"; // String | Optional. If provided, searches for entities with the provided authorization code.
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    String definitionID = "definitionID_example"; // String | Optional. If specified, filters codes by definition id.
    Integer createdByUserID = 56; // Integer | Optional. If specified, filters codes to those created by the given User ID.
    Integer deletedByUserID = 56; // Integer | Optional. If specified, filters codes to those deleted by the given User ID.
    Boolean includeDeleted = true; // Boolean | Optional. Whether to include deleted codes. 'False' by default.
    try {
      APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode result = apiInstance.authorizationCodesGetAuthorizationCodes(code, limit, offset, definitionID, createdByUserID, deletedByUserID, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesGetAuthorizationCodes");
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
| **code** | **String**| Optional. If provided, searches for entities with the provided authorization code. | [optional] |
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **definitionID** | **String**| Optional. If specified, filters codes by definition id. | [optional] |
| **createdByUserID** | **Integer**| Optional. If specified, filters codes to those created by the given User ID. | [optional] |
| **deletedByUserID** | **Integer**| Optional. If specified, filters codes to those deleted by the given User ID. | [optional] |
| **includeDeleted** | **Boolean**| Optional. Whether to include deleted codes. &#39;False&#39; by default. | [optional] |

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationCode.md)

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

<a id="authorizationCodesGetContactInformation"></a>
# **authorizationCodesGetContactInformation**
> AuthorizationCodesSharedModelsAuthorizationContactInformation authorizationCodesGetContactInformation(id)

Get contact information for an authorization code.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    Integer id = 56; // Integer | The id of the authorization code.
    try {
      AuthorizationCodesSharedModelsAuthorizationContactInformation result = apiInstance.authorizationCodesGetContactInformation(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesGetContactInformation");
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
| **id** | **Integer**| The id of the authorization code. | |

### Return type

[**AuthorizationCodesSharedModelsAuthorizationContactInformation**](AuthorizationCodesSharedModelsAuthorizationContactInformation.md)

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

<a id="authorizationCodesPostAuthorizationCode"></a>
# **authorizationCodesPostAuthorizationCode**
> Integer authorizationCodesPostAuthorizationCode(authorizationCodesSharedModelsAuthorizationCode)

Generates an authorization code using the provided definition and parameters.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    AuthorizationCodesSharedModelsAuthorizationCode authorizationCodesSharedModelsAuthorizationCode = new AuthorizationCodesSharedModelsAuthorizationCode(); // AuthorizationCodesSharedModelsAuthorizationCode | The model from which to generate an authorization code.
    try {
      Integer result = apiInstance.authorizationCodesPostAuthorizationCode(authorizationCodesSharedModelsAuthorizationCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesPostAuthorizationCode");
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
| **authorizationCodesSharedModelsAuthorizationCode** | [**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)| The model from which to generate an authorization code. | |

### Return type

**Integer**

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

<a id="authorizationCodesPutAuthorizationCode"></a>
# **authorizationCodesPutAuthorizationCode**
> authorizationCodesPutAuthorizationCode(id, authorizationCodesSharedModelsAuthorizationCode)

Update an authorization code.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    Integer id = 56; // Integer | The id of the authorization code.
    AuthorizationCodesSharedModelsAuthorizationCode authorizationCodesSharedModelsAuthorizationCode = new AuthorizationCodesSharedModelsAuthorizationCode(); // AuthorizationCodesSharedModelsAuthorizationCode | The model from which to update an authorization code.
    try {
      apiInstance.authorizationCodesPutAuthorizationCode(id, authorizationCodesSharedModelsAuthorizationCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesPutAuthorizationCode");
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
| **id** | **Integer**| The id of the authorization code. | |
| **authorizationCodesSharedModelsAuthorizationCode** | [**AuthorizationCodesSharedModelsAuthorizationCode**](AuthorizationCodesSharedModelsAuthorizationCode.md)| The model from which to update an authorization code. | |

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

<a id="authorizationCodesValidateAuthorizationCode"></a>
# **authorizationCodesValidateAuthorizationCode**
> AuthorizationCodesSharedModelsCodeValidationModel authorizationCodesValidateAuthorizationCode(id)

No Documentation Found.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCodesApi apiInstance = new AuthorizationCodesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      AuthorizationCodesSharedModelsCodeValidationModel result = apiInstance.authorizationCodesValidateAuthorizationCode(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCodesApi#authorizationCodesValidateAuthorizationCode");
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
| **id** | **Integer**|  | |

### Return type

[**AuthorizationCodesSharedModelsCodeValidationModel**](AuthorizationCodesSharedModelsCodeValidationModel.md)

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

