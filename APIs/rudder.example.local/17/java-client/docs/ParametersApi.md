# ParametersApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createParameter**](ParametersApi.md#createParameter) | **PUT** /parameters | Create a new parameter |
| [**deleteParameter**](ParametersApi.md#deleteParameter) | **DELETE** /parameters/{parameterId} | Delete a parameter |
| [**listParameters**](ParametersApi.md#listParameters) | **GET** /parameters | List all global parameters |
| [**parameterDetails**](ParametersApi.md#parameterDetails) | **GET** /parameters/{parameterId} | Get the value of a parameter |
| [**updateParameter**](ParametersApi.md#updateParameter) | **POST** /parameters/{parameterId} | Update a parameter&#39;s value |


<a id="createParameter"></a>
# **createParameter**
> CreateParameter200Response createParameter(parameter)

Create a new parameter

Create a new global parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    Parameter parameter = new Parameter(); // Parameter | 
    try {
      CreateParameter200Response result = apiInstance.createParameter(parameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#createParameter");
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
| **parameter** | [**Parameter**](Parameter.md)|  | |

### Return type

[**CreateParameter200Response**](CreateParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="deleteParameter"></a>
# **deleteParameter**
> DeleteParameter200Response deleteParameter(parameterId)

Delete a parameter

Delete an existing parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    String parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
    try {
      DeleteParameter200Response result = apiInstance.deleteParameter(parameterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#deleteParameter");
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
| **parameterId** | **String**| Id of the parameter to manage | |

### Return type

[**DeleteParameter200Response**](DeleteParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |
| **500** | Non existing parameter |  -  |

<a id="listParameters"></a>
# **listParameters**
> ListParameters200Response listParameters()

List all global parameters

Get the current value of all the global parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    try {
      ListParameters200Response result = apiInstance.listParameters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#listParameters");
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

[**ListParameters200Response**](ListParameters200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="parameterDetails"></a>
# **parameterDetails**
> ParameterDetails200Response parameterDetails(parameterId)

Get the value of a parameter

Get the current value of a given parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    String parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
    try {
      ParameterDetails200Response result = apiInstance.parameterDetails(parameterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#parameterDetails");
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
| **parameterId** | **String**| Id of the parameter to manage | |

### Return type

[**ParameterDetails200Response**](ParameterDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

<a id="updateParameter"></a>
# **updateParameter**
> UpdateParameter200Response updateParameter(parameterId)

Update a parameter&#39;s value

Update the properties of a parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    String parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
    try {
      UpdateParameter200Response result = apiInstance.updateParameter(parameterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#updateParameter");
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
| **parameterId** | **String**| Id of the parameter to manage | |

### Return type

[**UpdateParameter200Response**](UpdateParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |

