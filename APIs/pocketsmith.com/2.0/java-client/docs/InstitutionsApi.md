# InstitutionsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**institutionsIdDelete**](InstitutionsApi.md#institutionsIdDelete) | **DELETE** /institutions/{id} | Delete institution |
| [**institutionsIdGet**](InstitutionsApi.md#institutionsIdGet) | **GET** /institutions/{id} | Get institution |
| [**institutionsIdPut**](InstitutionsApi.md#institutionsIdPut) | **PUT** /institutions/{id} | Update institution |
| [**usersIdInstitutionsGet**](InstitutionsApi.md#usersIdInstitutionsGet) | **GET** /users/{id}/institutions | List institutions in user |
| [**usersIdInstitutionsPost**](InstitutionsApi.md#usersIdInstitutionsPost) | **POST** /users/{id}/institutions | Create institution in user |


<a id="institutionsIdDelete"></a>
# **institutionsIdDelete**
> institutionsIdDelete(id, mergeIntoInstitutionId)

Delete institution

Deletes an institution and all data within. Alternatively, another institution can be provided to merge the data into to avoid losing it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the institution.
    Integer mergeIntoInstitutionId = 44; // Integer | The unique identifier of the institution to merge into.
    try {
      apiInstance.institutionsIdDelete(id, mergeIntoInstitutionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsIdDelete");
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
| **id** | **Integer**| The unique identifier of the institution. | |
| **mergeIntoInstitutionId** | **Integer**| The unique identifier of the institution to merge into. | [optional] |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="institutionsIdGet"></a>
# **institutionsIdGet**
> Institution institutionsIdGet(id)

Get institution

Gets an institution by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the institution.
    try {
      Institution result = apiInstance.institutionsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsIdGet");
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
| **id** | **Integer**| The unique identifier of the institution. | |

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="institutionsIdPut"></a>
# **institutionsIdPut**
> Institution institutionsIdPut(id, institutionsIdPutRequest)

Update institution

Updates the title and currency code for an institution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the institution.
    InstitutionsIdPutRequest institutionsIdPutRequest = new InstitutionsIdPutRequest(); // InstitutionsIdPutRequest | 
    try {
      Institution result = apiInstance.institutionsIdPut(id, institutionsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#institutionsIdPut");
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
| **id** | **Integer**| The unique identifier of the institution. | |
| **institutionsIdPutRequest** | [**InstitutionsIdPutRequest**](InstitutionsIdPutRequest.md)|  | [optional] |

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="usersIdInstitutionsGet"></a>
# **usersIdInstitutionsGet**
> List&lt;Institution&gt; usersIdInstitutionsGet(id)

List institutions in user

Lists all the institutions belonging to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user
    try {
      List<Institution> result = apiInstance.usersIdInstitutionsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#usersIdInstitutionsGet");
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
| **id** | **Integer**| The unique identifier of the user | |

### Return type

[**List&lt;Institution&gt;**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdInstitutionsPost"></a>
# **usersIdInstitutionsPost**
> Institution usersIdInstitutionsPost(id, usersIdInstitutionsPostRequest)

Create institution in user

Creates an institution belonging to a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstitutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    InstitutionsApi apiInstance = new InstitutionsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user
    UsersIdInstitutionsPostRequest usersIdInstitutionsPostRequest = new UsersIdInstitutionsPostRequest(); // UsersIdInstitutionsPostRequest | 
    try {
      Institution result = apiInstance.usersIdInstitutionsPost(id, usersIdInstitutionsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstitutionsApi#usersIdInstitutionsPost");
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
| **id** | **Integer**| The unique identifier of the user | |
| **usersIdInstitutionsPostRequest** | [**UsersIdInstitutionsPostRequest**](UsersIdInstitutionsPostRequest.md)|  | [optional] |

### Return type

[**Institution**](Institution.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

