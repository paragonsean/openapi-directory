# DocumentsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createnewdocument**](DocumentsApi.md#createnewdocument) | **POST** /api/dataentities/{acronym}/documents | Create new document |
| [**createorupdateentiredocument**](DocumentsApi.md#createorupdateentiredocument) | **PUT** /api/dataentities/{acronym}/documents | Create or update entire document |
| [**createorupdatepartialdocument**](DocumentsApi.md#createorupdatepartialdocument) | **PATCH** /api/dataentities/{acronym}/documents | Create or update partial document |
| [**deletedocument**](DocumentsApi.md#deletedocument) | **DELETE** /api/dataentities/{acronym}/documents/{id} | Delete document |
| [**getdocument**](DocumentsApi.md#getdocument) | **GET** /api/dataentities/{acronym}/documents/{id} | Get document |
| [**updateentiredocument**](DocumentsApi.md#updateentiredocument) | **PUT** /api/dataentities/{acronym}/documents/{id} | Update entire document |
| [**updatepartialdocument**](DocumentsApi.md#updatepartialdocument) | **PATCH** /api/dataentities/{acronym}/documents/{id} | Update partial document |


<a id="createnewdocument"></a>
# **createnewdocument**
> Createnewdocument createnewdocument(accept, acronym, body)

Create new document

Creates documents through a JSON object where the key is the name of the field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Identifies the kind of data
    Object body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}; // Object | 
    try {
      Createnewdocument result = apiInstance.createnewdocument(accept, acronym, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#createnewdocument");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Identifies the kind of data | [default to {{acronym}}] |
| **body** | **Object**|  | |

### Return type

[**Createnewdocument**](Createnewdocument.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createorupdateentiredocument"></a>
# **createorupdateentiredocument**
> createorupdateentiredocument(accept, acronym, body)

Create or update entire document



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Identifies the kind of data
    Object body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit.... ","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}; // Object | 
    try {
      apiInstance.createorupdateentiredocument(accept, acronym, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#createorupdateentiredocument");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Identifies the kind of data | [default to {{acronym}}] |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createorupdatepartialdocument"></a>
# **createorupdatepartialdocument**
> createorupdatepartialdocument(accept, acronym, body)

Create or update partial document



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Identifies the kind of data
    Object body = {"Boolean":true,"id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}; // Object | 
    try {
      apiInstance.createorupdatepartialdocument(accept, acronym, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#createorupdatepartialdocument");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Identifies the kind of data | [default to {{acronym}}] |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deletedocument"></a>
# **deletedocument**
> deletedocument(contentType, accept, acronym, id)

Delete document

It allows to delete a document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    try {
      apiInstance.deletedocument(contentType, accept, acronym, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#deletedocument");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getdocument"></a>
# **getdocument**
> Usingfilters getdocument(contentType, accept, acronym, id)

Get document

Retrieves a document.    Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    try {
      Usingfilters result = apiInstance.getdocument(contentType, accept, acronym, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#getdocument");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |

### Return type

[**Usingfilters**](Usingfilters.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateentiredocument"></a>
# **updateentiredocument**
> updateentiredocument(accept, acronym, id, body)

Update entire document



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    Object body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}; // Object | 
    try {
      apiInstance.updateentiredocument(accept, acronym, id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#updateentiredocument");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updatepartialdocument"></a>
# **updatepartialdocument**
> updatepartialdocument(accept, acronym, id, body)

Update partial document



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    DocumentsApi apiInstance = new DocumentsApi(defaultClient);
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String acronym = "{{acronym}}"; // String | Two letter word that identifies the data structure
    String id = "{{id}}"; // String | Id of the document
    Object body = {"Boolean":false}; // Object | 
    try {
      apiInstance.updatepartialdocument(accept, acronym, id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentsApi#updatepartialdocument");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **acronym** | **String**| Two letter word that identifies the data structure | [default to {{acronym}}] |
| **id** | **String**| Id of the document | [default to {{id}}] |
| **body** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

