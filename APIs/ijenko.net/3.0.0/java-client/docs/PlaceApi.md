# PlaceApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placeBuses**](PlaceApi.md#placeBuses) | **GET** /places/{placeId}/buses | List Buses |
| [**placeGetMetadata**](PlaceApi.md#placeGetMetadata) | **GET** /places/{placeId}/metadata | List metadata |
| [**placeOpenPairing**](PlaceApi.md#placeOpenPairing) | **PUT** /places/{placeId}/buses/{busId}/pairing | Open/Close the pairing window |
| [**placePairing**](PlaceApi.md#placePairing) | **GET** /places/{placeId}/buses/{busId}/pairing | State of the pairing window |
| [**placePatch**](PlaceApi.md#placePatch) | **PATCH** /places/{placeId} | Update a Place |
| [**placePatchMetadata**](PlaceApi.md#placePatchMetadata) | **PATCH** /places/{placeId}/metadata | Modify metadata |
| [**placesGet**](PlaceApi.md#placesGet) | **GET** /places/{placeId} | Information about a Place |


<a id="placeBuses"></a>
# **placeBuses**
> Set&lt;BusItem&gt; placeBuses(placeId, withPairing)

List Buses

Get the list of *Buses* available on the gateway of this *Place*. If &#x60;withPairing&#x60; is &#x60;true&#x60;, return only buses that allow device pairing (see &#x60;/places/{placeId}/buses/{busId}/pairing&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    Boolean withPairing = false; // Boolean | Filter out buses that have no pairing window
    try {
      Set<BusItem> result = apiInstance.placeBuses(placeId, withPairing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeBuses");
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
| **withPairing** | **Boolean**| Filter out buses that have no pairing window | [optional] [default to false] |

### Return type

[**Set&lt;BusItem&gt;**](BusItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **403** | *Bus* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |

<a id="placeGetMetadata"></a>
# **placeGetMetadata**
> Map&lt;String, Object&gt; placeGetMetadata(placeId)

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
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    try {
      Map<String, Object> result = apiInstance.placeGetMetadata(placeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetMetadata");
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

<a id="placeOpenPairing"></a>
# **placeOpenPairing**
> BusPairing placeOpenPairing(placeId, busId, pairing)

Open/Close the pairing window

Open/Close the pairing window.  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    String busId = "busId_example"; // String | Unique identifier of a *Bus*.
    BusPairing pairing = new BusPairing(); // BusPairing | 
    try {
      BusPairing result = apiInstance.placeOpenPairing(placeId, busId, pairing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeOpenPairing");
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
| **busId** | **String**| Unique identifier of a *Bus*. | |
| **pairing** | [**BusPairing**](BusPairing.md)|  | |

### Return type

[**BusPairing**](BusPairing.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | State information. |  -  |
| **403** | *Bus* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="placePairing"></a>
# **placePairing**
> BusPairing placePairing(placeId, busId)

State of the pairing window

Get the state of the pairing window of the *Bus*.  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    String busId = "busId_example"; // String | Unique identifier of a *Bus*.
    try {
      BusPairing result = apiInstance.placePairing(placeId, busId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placePairing");
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
| **busId** | **String**| Unique identifier of a *Bus*. | |

### Return type

[**BusPairing**](BusPairing.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | State information. |  -  |
| **403** | *Bus* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |

<a id="placePatch"></a>
# **placePatch**
> placePatch(placeId, placePatch)

Update a Place

Change information about a *Place*.  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    PlacePatch placePatch = new PlacePatch(); // PlacePatch | 
    try {
      apiInstance.placePatch(placeId, placePatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placePatch");
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
| **placePatch** | [**PlacePatch**](PlacePatch.md)|  | |

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
| **403** | The authentication token doesn&#39;t allow to modify the *Account*.  |  -  |
| **0** | Other error. |  -  |

<a id="placePatchMetadata"></a>
# **placePatchMetadata**
> Map&lt;String, Object&gt; placePatchMetadata(placeId, metadataPatch)

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
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    MetadataPatch metadataPatch = new MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
    try {
      Map<String, Object> result = apiInstance.placePatchMetadata(placeId, metadataPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placePatchMetadata");
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
| **403** | *Place* doesn&#39;t exist or the requester doesn&#39;t have access.  |  -  |
| **0** | Other error. |  -  |

<a id="placesGet"></a>
# **placesGet**
> Place placesGet(placeId)

Information about a Place

Get information about a *Place*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

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

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    try {
      Place result = apiInstance.placesGet(placeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placesGet");
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

### Return type

[**Place**](Place.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | *Place* doesn&#39;t exist or the requester doesn&#39;t have access.  |  -  |

