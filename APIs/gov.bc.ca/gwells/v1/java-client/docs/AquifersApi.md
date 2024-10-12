# AquifersApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aquifersFilesList**](AquifersApi.md#aquifersFilesList) | **GET** /aquifers/{aquifer_id}/files |  |
| [**aquifersList**](AquifersApi.md#aquifersList) | **GET** /aquifers/ |  |
| [**aquifersNamesList**](AquifersApi.md#aquifersNamesList) | **GET** /aquifers/names/ |  |
| [**aquifersRead**](AquifersApi.md#aquifersRead) | **GET** /aquifers/{aquifer_id}/ |  |


<a id="aquifersFilesList"></a>
# **aquifersFilesList**
> AquifersFilesList200Response aquifersFilesList(aquiferId)



list files found for the aquifer identified in the uri

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AquifersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AquifersApi apiInstance = new AquifersApi(defaultClient);
    String aquiferId = "aquiferId_example"; // String | 
    try {
      AquifersFilesList200Response result = apiInstance.aquifersFilesList(aquiferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AquifersApi#aquifersFilesList");
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
| **aquiferId** | **String**|  | |

### Return type

[**AquifersFilesList200Response**](AquifersFilesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="aquifersList"></a>
# **aquifersList**
> AquifersList200Response aquifersList(aquiferId, ordering, search, limit, offset)



return a list of aquifers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AquifersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AquifersApi apiInstance = new AquifersApi(defaultClient);
    BigDecimal aquiferId = new BigDecimal(78); // BigDecimal | 
    String ordering = "ordering_example"; // String | Which field to use when ordering the results.
    String search = "search_example"; // String | A search term.
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      AquifersList200Response result = apiInstance.aquifersList(aquiferId, ordering, search, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AquifersApi#aquifersList");
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
| **aquiferId** | **BigDecimal**|  | [optional] |
| **ordering** | **String**| Which field to use when ordering the results. | [optional] |
| **search** | **String**| A search term. | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**AquifersList200Response**](AquifersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="aquifersNamesList"></a>
# **aquifersNamesList**
> List&lt;AquiferSerializerBasic&gt; aquifersNamesList(search)



List all aquifers in a simplified format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AquifersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AquifersApi apiInstance = new AquifersApi(defaultClient);
    String search = "search_example"; // String | A search term.
    try {
      List<AquiferSerializerBasic> result = apiInstance.aquifersNamesList(search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AquifersApi#aquifersNamesList");
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
| **search** | **String**| A search term. | [optional] |

### Return type

[**List&lt;AquiferSerializerBasic&gt;**](AquiferSerializerBasic.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="aquifersRead"></a>
# **aquifersRead**
> Aquifer aquifersRead(aquiferId)



return details of aquifers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AquifersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.nrs.gov.bc.ca/gwells/api/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AquifersApi apiInstance = new AquifersApi(defaultClient);
    Integer aquiferId = 56; // Integer | A unique integer value identifying this aquifer.
    try {
      Aquifer result = apiInstance.aquifersRead(aquiferId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AquifersApi#aquifersRead");
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
| **aquiferId** | **Integer**| A unique integer value identifying this aquifer. | |

### Return type

[**Aquifer**](Aquifer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

