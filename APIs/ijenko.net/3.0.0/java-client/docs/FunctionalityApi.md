# FunctionalityApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deviceAddFunctionality_0**](FunctionalityApi.md#deviceAddFunctionality_0) | **POST** /devices/{deviceId}/functionalities | Add dynamically a functionality |
| [**functionalitiesGet**](FunctionalityApi.md#functionalitiesGet) | **GET** /functionalities/{functionalityId} | Information about a Functionality |
| [**functionalityGetMetadata**](FunctionalityApi.md#functionalityGetMetadata) | **GET** /functionalities/{functionalityId}/metadata | List metadata |
| [**functionalityGetTags**](FunctionalityApi.md#functionalityGetTags) | **GET** /functionalities/{functionalityId}/tags | List tags |
| [**functionalityPatch**](FunctionalityApi.md#functionalityPatch) | **PATCH** /functionalities/{functionalityId} | Modify a Functionality |
| [**functionalityPatchMetadata**](FunctionalityApi.md#functionalityPatchMetadata) | **PATCH** /functionalities/{functionalityId}/metadata | Modify metadata |
| [**functionalityPatchTags**](FunctionalityApi.md#functionalityPatchTags) | **PATCH** /functionalities/{functionalityId}/tags | Modify tags |
| [**functionalitySet**](FunctionalityApi.md#functionalitySet) | **PUT** /functionalities/{functionalityId}/attributes/{attributeName} | Modify an Attribute value |
| [**functionalityValue**](FunctionalityApi.md#functionalityValue) | **GET** /functionalities/{functionalityId}/attributes/{attributeName} | Get an Attribute value |
| [**functionalityValues**](FunctionalityApi.md#functionalityValues) | **GET** /functionalities/{functionalityId}/attributes | Get history of multiple attributes |
| [**placeFunctionalities**](FunctionalityApi.md#placeFunctionalities) | **GET** /places/{placeId}/functionalities | List Functionalities |


<a id="deviceAddFunctionality_0"></a>
# **deviceAddFunctionality_0**
> FunctionalityCreated deviceAddFunctionality_0(deviceId, functionalityInfo)

Add dynamically a functionality

Add a *Functionality* to the device.  Required parameters are : - functionality class - endpoint  Each device class has its own restrictions on which Functionality classes can be added and on which endpoints. Only a few devices allow to add Functionalities.  |Device class|Functionality class|Endpoints| |------------|-------------------|---------| |MINT        |CurrentPeriod      |1,2,3    | |MINT        |ElectricityRates   |1,2,3    | |MINT        |GenericRate        |1,2,3    |  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    FunctionalityNew functionalityInfo = new FunctionalityNew(); // FunctionalityNew | 
    try {
      FunctionalityCreated result = apiInstance.deviceAddFunctionality_0(deviceId, functionalityInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#deviceAddFunctionality_0");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **functionalityInfo** | [**FunctionalityNew**](FunctionalityNew.md)|  | |

### Return type

[**FunctionalityCreated**](FunctionalityCreated.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | *Functionality* successfully created. |  * Location - Path of the Program created (&#x60;/programs/{id}&#x60;) <br>  |
| **403** | *Device* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="functionalitiesGet"></a>
# **functionalitiesGet**
> Functionality functionalitiesGet(functionalityId)

Information about a Functionality

Get the *Functionality*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    try {
      Functionality result = apiInstance.functionalitiesGet(functionalityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalitiesGet");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |

### Return type

[**Functionality**](Functionality.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="functionalityGetMetadata"></a>
# **functionalityGetMetadata**
> Map&lt;String, Object&gt; functionalityGetMetadata(functionalityId)

List metadata

Get the metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    try {
      Map<String, Object> result = apiInstance.functionalityGetMetadata(functionalityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityGetMetadata");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="functionalityGetTags"></a>
# **functionalityGetTags**
> Set&lt;String&gt; functionalityGetTags(functionalityId)

List tags

Get the tags of a *Functionality*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    try {
      Set<String> result = apiInstance.functionalityGetTags(functionalityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityGetTags");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |

### Return type

**Set&lt;String&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="functionalityPatch"></a>
# **functionalityPatch**
> functionalityPatch(functionalityId, functionalityPatch)

Modify a Functionality

Modify information about a *Functionality*: its name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    FunctionalityPatch functionalityPatch = new FunctionalityPatch(); // FunctionalityPatch | 
    try {
      apiInstance.functionalityPatch(functionalityId, functionalityPatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityPatch");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **functionalityPatch** | [**FunctionalityPatch**](FunctionalityPatch.md)|  | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Modification successful. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Functionality* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="functionalityPatchMetadata"></a>
# **functionalityPatchMetadata**
> Map&lt;String, Object&gt; functionalityPatchMetadata(functionalityId, metadataPatch)

Modify metadata

Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    MetadataPatch metadataPatch = new MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
    try {
      Map<String, Object> result = apiInstance.functionalityPatchMetadata(functionalityId, metadataPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityPatchMetadata");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. The new metadata is returned. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Functionality* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="functionalityPatchTags"></a>
# **functionalityPatchTags**
> Set&lt;String&gt; functionalityPatchTags(functionalityId, tagsPatch)

Modify tags

Modify the tags of a *Functionality*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    TagsPatch tagsPatch = new TagsPatch(); // TagsPatch | Modifications to apply to the tags list of the resource. 
    try {
      Set<String> result = apiInstance.functionalityPatchTags(functionalityId, tagsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityPatchTags");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **tagsPatch** | [**TagsPatch**](TagsPatch.md)| Modifications to apply to the tags list of the resource.  | |

### Return type

**Set&lt;String&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. The new list of tags is returned. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Functionality* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="functionalitySet"></a>
# **functionalitySet**
> functionalitySet(functionalityId, attributeName, value)

Modify an Attribute value

Modify the value of the *Attribute*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    String attributeName = "attributeName_example"; // String | Identifier of an *Attribute* inside a *Functionality*.
    Object value = null; // Object | New value for the *Attribute*.
    try {
      apiInstance.functionalitySet(functionalityId, attributeName, value);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalitySet");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **attributeName** | **String**| Identifier of an *Attribute* inside a *Functionality*. | |
| **value** | **Object**| New value for the *Attribute*. | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful. |  -  |
| **405** | *Attribute* is not writable.  |  -  |
| **0** | Other error. |  -  |

<a id="functionalityValue"></a>
# **functionalityValue**
> AttributeValue functionalityValue(functionalityId, attributeName)

Get an Attribute value

Get the *Attribute* value and the last time when it changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    String attributeName = "attributeName_example"; // String | Identifier of an *Attribute* inside a *Functionality*.
    try {
      AttributeValue result = apiInstance.functionalityValue(functionalityId, attributeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityValue");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **attributeName** | **String**| Identifier of an *Attribute* inside a *Functionality*. | |

### Return type

[**AttributeValue**](AttributeValue.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **204** | No value has yet been set on this attribute. |  -  |
| **0** | Other error. |  -  |

<a id="functionalityValues"></a>
# **functionalityValues**
> Map&lt;String, List&lt;AttributeValue&gt;&gt; functionalityValues(functionalityId, names, from, to, surround)

Get history of multiple attributes

Get the values of multiple *Attributes* and their history.  If the &#x60;names&#x60; parameter is not given, all the attributes of the *Functionality* are returned. As the list may be huge, this must be avoided.  If the &#x60;to&#x60; parameter is set, &#x60;from&#x60; must also be set.  If &#x60;from&#x60; is not set, only the last value is returned.  The &#x60;surround&#x60; parameter allows to ask also for one value beyond each interval boundaries.  The request may fail if too many values are asked. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
    List<String> names = Arrays.asList(); // List<String> | One or multiple *Attribute* names separated by commas
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Beginning of the time interval.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | End of the interval. Default: now. 
    Boolean surround = true; // Boolean | If true, return also one value before from and one value after to
    try {
      Map<String, List<AttributeValue>> result = apiInstance.functionalityValues(functionalityId, names, from, to, surround);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#functionalityValues");
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
| **functionalityId** | **String**| Unique identifier of a *Functionality*. | |
| **names** | [**List&lt;String&gt;**](String.md)| One or multiple *Attribute* names separated by commas | [optional] |
| **from** | **OffsetDateTime**| Beginning of the time interval. | [optional] |
| **to** | **OffsetDateTime**| End of the interval. Default: now.  | [optional] |
| **surround** | **Boolean**| If true, return also one value before from and one value after to | [optional] |

### Return type

[**Map&lt;String, List&lt;AttributeValue&gt;&gt;**](List.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="placeFunctionalities"></a>
# **placeFunctionalities**
> Set&lt;FunctionalityItem&gt; placeFunctionalities(placeId, devices, functionalities, embedMetadata)

List Functionalities

Get the list of *Functionalities* available in this *Place*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FunctionalityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    FunctionalityApi apiInstance = new FunctionalityApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    String devices = "devices_example"; // String | Devices selector. Device tags or device classes or device ids or '*' for any. Multiple values are separated by '|' and interpreted as « OR ».
    String functionalities = "functionalities_example"; // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
    List<String> embedMetadata = Arrays.asList(); // List<String> | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    try {
      Set<FunctionalityItem> result = apiInstance.placeFunctionalities(placeId, devices, functionalities, embedMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FunctionalityApi#placeFunctionalities");
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
| **placeId** | **String**| Unique identifier of a *Place*. | |
| **devices** | **String**| Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ». | [optional] |
| **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | [optional] |
| **embedMetadata** | [**List&lt;String&gt;**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] |

### Return type

[**Set&lt;FunctionalityItem&gt;**](FunctionalityItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

