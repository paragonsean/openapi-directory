# CveApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkCVE**](CveApi.md#checkCVE) | **POST** /cve/check | Trigger a CVE check |
| [**getAllCve**](CveApi.md#getAllCve) | **GET** /cve | Get all CVE details |
| [**getCVECheckConfiguration**](CveApi.md#getCVECheckConfiguration) | **GET** /cve/check/config | Get CVE check config |
| [**getCVEList**](CveApi.md#getCVEList) | **POST** /cve/list | Get a list of CVE details |
| [**getCve**](CveApi.md#getCve) | **GET** /cve/{cveId} | Get a CVE details |
| [**getLastCVECheck**](CveApi.md#getLastCVECheck) | **GET** /cve/check/last | Get last CVE check result |
| [**readCVEfromFS**](CveApi.md#readCVEfromFS) | **POST** /cve/update/fs | Update CVE database from file system |
| [**updateCVE**](CveApi.md#updateCVE) | **POST** /cve/update | Update CVE database from remote source |
| [**updateCVECheckConfiguration**](CveApi.md#updateCVECheckConfiguration) | **POST** /cve/check/config | Update cve check config |


<a id="checkCVE"></a>
# **checkCVE**
> CheckCVE200Response checkCVE()

Trigger a CVE check

Trigger a CVE check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    try {
      CheckCVE200Response result = apiInstance.checkCVE();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#checkCVE");
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

[**CheckCVE200Response**](CheckCVE200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CVE check result |  -  |

<a id="getAllCve"></a>
# **getAllCve**
> GetAllCve200Response getAllCve()

Get all CVE details

Get all CVE details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    try {
      GetAllCve200Response result = apiInstance.getAllCve();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#getAllCve");
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

[**GetAllCve200Response**](GetAllCve200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CVE details result |  -  |

<a id="getCVECheckConfiguration"></a>
# **getCVECheckConfiguration**
> GetCVECheckConfiguration200Response getCVECheckConfiguration()

Get CVE check config

Get CVE check config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    try {
      GetCVECheckConfiguration200Response result = apiInstance.getCVECheckConfiguration();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#getCVECheckConfiguration");
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

[**GetCVECheckConfiguration200Response**](GetCVECheckConfiguration200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CVE check config |  -  |

<a id="getCVEList"></a>
# **getCVEList**
> GetCVEList200Response getCVEList(getCVEListRequest)

Get a list of CVE details

Get CVE details, from a list passed as parameter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    GetCVEListRequest getCVEListRequest = new GetCVEListRequest(); // GetCVEListRequest | 
    try {
      GetCVEList200Response result = apiInstance.getCVEList(getCVEListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#getCVEList");
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
| **getCVEListRequest** | [**GetCVEListRequest**](GetCVEListRequest.md)|  | [optional] |

### Return type

[**GetCVEList200Response**](GetCVEList200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CVE list |  -  |

<a id="getCve"></a>
# **getCve**
> GetCve200Response getCve(cveId)

Get a CVE details

Get a CVE details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    UUID cveId = UUID.randomUUID(); // UUID | Id of the CVE
    try {
      GetCve200Response result = apiInstance.getCve(cveId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#getCve");
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
| **cveId** | **UUID**| Id of the CVE | |

### Return type

[**GetCve200Response**](GetCve200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CVE details result |  -  |

<a id="getLastCVECheck"></a>
# **getLastCVECheck**
> GetLastCVECheck200Response getLastCVECheck(groupId, nodeId, cveId, _package, severity)

Get last CVE check result

Get last CVE check result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    String groupId = "groupId_example"; // String | Id of node groups you want to get from last CVE check
    String nodeId = "nodeId_example"; // String | Id of nodes you want to get from last CVE check
    String cveId = "cveId_example"; // String | Id of CVE you want to get from last CVE check
    String _package = "_package_example"; // String | Name of packages you want to get from last CVE check
    String severity = "critical"; // String | Severity of the CVE you want to get from last CVE check
    try {
      GetLastCVECheck200Response result = apiInstance.getLastCVECheck(groupId, nodeId, cveId, _package, severity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#getLastCVECheck");
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
| **groupId** | **String**| Id of node groups you want to get from last CVE check | [optional] |
| **nodeId** | **String**| Id of nodes you want to get from last CVE check | [optional] |
| **cveId** | **String**| Id of CVE you want to get from last CVE check | [optional] |
| **_package** | **String**| Name of packages you want to get from last CVE check | [optional] |
| **severity** | **String**| Severity of the CVE you want to get from last CVE check | [optional] [enum: critical, high, medium, low, none, unknown] |

### Return type

[**GetLastCVECheck200Response**](GetLastCVECheck200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Last CVE check |  -  |

<a id="readCVEfromFS"></a>
# **readCVEfromFS**
> ReadCVEfromFS200Response readCVEfromFS()

Update CVE database from file system

Update CVE database from file system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    try {
      ReadCVEfromFS200Response result = apiInstance.readCVEfromFS();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#readCVEfromFS");
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

[**ReadCVEfromFS200Response**](ReadCVEfromFS200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated CVE count |  -  |

<a id="updateCVE"></a>
# **updateCVE**
> UpdateCVE200Response updateCVE(updateCVERequest)

Update CVE database from remote source

Update CVE database from remote source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    UpdateCVERequest updateCVERequest = new UpdateCVERequest(); // UpdateCVERequest | 
    try {
      UpdateCVE200Response result = apiInstance.updateCVE(updateCVERequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#updateCVE");
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
| **updateCVERequest** | [**UpdateCVERequest**](UpdateCVERequest.md)|  | [optional] |

### Return type

[**UpdateCVE200Response**](UpdateCVE200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | updated CVE count |  -  |

<a id="updateCVECheckConfiguration"></a>
# **updateCVECheckConfiguration**
> UpdateCVECheckConfiguration200Response updateCVECheckConfiguration(updateCVECheckConfigurationRequest)

Update cve check config

Update cve check config

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    CveApi apiInstance = new CveApi(defaultClient);
    UpdateCVECheckConfigurationRequest updateCVECheckConfigurationRequest = new UpdateCVECheckConfigurationRequest(); // UpdateCVECheckConfigurationRequest | 
    try {
      UpdateCVECheckConfiguration200Response result = apiInstance.updateCVECheckConfiguration(updateCVECheckConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CveApi#updateCVECheckConfiguration");
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
| **updateCVECheckConfigurationRequest** | [**UpdateCVECheckConfigurationRequest**](UpdateCVECheckConfigurationRequest.md)|  | [optional] |

### Return type

[**UpdateCVECheckConfiguration200Response**](UpdateCVECheckConfiguration200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | new CVE check config |  -  |

