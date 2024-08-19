# DirectivesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkDirective**](DirectivesApi.md#checkDirective) | **POST** /directives/{directiveId}/check | Check that update on a directive is valid |
| [**createDirective**](DirectivesApi.md#createDirective) | **PUT** /directives | Create a directive |
| [**deleteDirective**](DirectivesApi.md#deleteDirective) | **DELETE** /directives/{directiveId} | Delete a directive |
| [**directiveDetails**](DirectivesApi.md#directiveDetails) | **GET** /directives/{directiveId} | Get directive details |
| [**listDirectives**](DirectivesApi.md#listDirectives) | **GET** /directives | List all directives |
| [**updateDirective**](DirectivesApi.md#updateDirective) | **POST** /directives/{directiveId} | Update a directive details |


<a id="checkDirective"></a>
# **checkDirective**
> CheckDirective200Response checkDirective(directiveId, directive)

Check that update on a directive is valid

Check that update on a directive is valid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    UUID directiveId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the directive
    Directive directive = new Directive(); // Directive | 
    try {
      CheckDirective200Response result = apiInstance.checkDirective(directiveId, directive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#checkDirective");
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
| **directiveId** | **UUID**| Id of the directive | |
| **directive** | [**Directive**](Directive.md)|  | |

### Return type

[**CheckDirective200Response**](CheckDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

<a id="createDirective"></a>
# **createDirective**
> CreateDirective200Response createDirective(directiveNew)

Create a directive

Create a new directive from provided parameters. You can specify a source directive to clone it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    DirectiveNew directiveNew = new DirectiveNew(); // DirectiveNew | 
    try {
      CreateDirective200Response result = apiInstance.createDirective(directiveNew);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#createDirective");
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
| **directiveNew** | [**DirectiveNew**](DirectiveNew.md)|  | [optional] |

### Return type

[**CreateDirective200Response**](CreateDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

<a id="deleteDirective"></a>
# **deleteDirective**
> DeleteDirective200Response deleteDirective(directiveId)

Delete a directive

Delete a directive

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    UUID directiveId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the directive
    try {
      DeleteDirective200Response result = apiInstance.deleteDirective(directiveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#deleteDirective");
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
| **directiveId** | **UUID**| Id of the directive | |

### Return type

[**DeleteDirective200Response**](DeleteDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

<a id="directiveDetails"></a>
# **directiveDetails**
> DirectiveDetails200Response directiveDetails(directiveId)

Get directive details

Get all information about a given directive

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    UUID directiveId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the directive
    try {
      DirectiveDetails200Response result = apiInstance.directiveDetails(directiveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#directiveDetails");
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
| **directiveId** | **UUID**| Id of the directive | |

### Return type

[**DirectiveDetails200Response**](DirectiveDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

<a id="listDirectives"></a>
# **listDirectives**
> ListDirectives200Response listDirectives()

List all directives

List all directives

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    try {
      ListDirectives200Response result = apiInstance.listDirectives();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#listDirectives");
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

[**ListDirectives200Response**](ListDirectives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

<a id="updateDirective"></a>
# **updateDirective**
> UpdateDirective200Response updateDirective(directiveId, directive)

Update a directive details

Update directive information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectivesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DirectivesApi apiInstance = new DirectivesApi(defaultClient);
    UUID directiveId = UUID.fromString("9a1773c9-0889-40b6-be89-f6504443ac1b"); // UUID | Id of the directive
    Directive directive = new Directive(); // Directive | 
    try {
      UpdateDirective200Response result = apiInstance.updateDirective(directiveId, directive);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectivesApi#updateDirective");
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
| **directiveId** | **UUID**| Id of the directive | |
| **directive** | [**Directive**](Directive.md)|  | |

### Return type

[**UpdateDirective200Response**](UpdateDirective200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Directives information |  -  |

