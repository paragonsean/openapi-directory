# DataStoreApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchReadTags**](DataStoreApi.md#batchReadTags) | **POST** /v1/data-store/read |  |
| [**listAllTags**](DataStoreApi.md#listAllTags) | **GET** /v1/data-store/tags |  |
| [**listDeviceTags**](DataStoreApi.md#listDeviceTags) | **GET** /v1/data-store/devices/{id}/tags |  |
| [**listDevices**](DataStoreApi.md#listDevices) | **GET** /v1/data-store/devices |  |
| [**readTag**](DataStoreApi.md#readTag) | **GET** /v1/data-store/read/{id} |  |
| [**writeTag**](DataStoreApi.md#writeTag) | **POST** /v1/data-store/write/{id} |  |


<a id="batchReadTags"></a>
# **batchReadTags**
> List&lt;TagValue&gt; batchReadTags(tags)



Read selected tags from the data store. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    List<TagReference> tags = Arrays.asList(); // List<TagReference> | Tag references for the tags to read.
    try {
      List<TagValue> result = apiInstance.batchReadTags(tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#batchReadTags");
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
| **tags** | [**List&lt;TagReference&gt;**](TagReference.md)| Tag references for the tags to read. | |

### Return type

[**List&lt;TagValue&gt;**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllTags"></a>
# **listAllTags**
> List&lt;TagDefinition&gt; listAllTags()



List all data store tags defined in the project. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    try {
      List<TagDefinition> result = apiInstance.listAllTags();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#listAllTags");
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

[**List&lt;TagDefinition&gt;**](TagDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeviceTags"></a>
# **listDeviceTags**
> List&lt;TagDefinition&gt; listDeviceTags(id)



List tags of the given device. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | ID of the device to use.
    try {
      List<TagDefinition> result = apiInstance.listDeviceTags(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#listDeviceTags");
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
| **id** | **BigDecimal**| ID of the device to use. | |

### Return type

[**List&lt;TagDefinition&gt;**](TagDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDevices"></a>
# **listDevices**
> List&lt;DataStoreDevice&gt; listDevices()



List devices available in the data store. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    try {
      List<DataStoreDevice> result = apiInstance.listDevices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#listDevices");
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

[**List&lt;DataStoreDevice&gt;**](DataStoreDevice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="readTag"></a>
# **readTag**
> TagValue readTag(id, index, count)



Read the current value of a single tag. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | ID of the tag to read.
    BigDecimal index = new BigDecimal("0.0"); // BigDecimal | Table index to start reading at.
    BigDecimal count = new BigDecimal("1.0"); // BigDecimal | Number of elements to read from a table.
    try {
      TagValue result = apiInstance.readTag(id, index, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#readTag");
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
| **id** | **BigDecimal**| ID of the tag to read. | |
| **index** | **BigDecimal**| Table index to start reading at. | [optional] [default to 0.0] |
| **count** | **BigDecimal**| Number of elements to read from a table. | [optional] [default to 1.0] |

### Return type

[**TagValue**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="writeTag"></a>
# **writeTag**
> TagValue writeTag(id, value, index)



Writes a new value to the given tag. Authorized for admins and editors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataStoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataStoreApi apiInstance = new DataStoreApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | ID of the tag to write.
    String value = "value_example"; // String | Value to write to the tag. Must be a string, number, or boolean.
    BigDecimal index = new BigDecimal("0.0"); // BigDecimal | For array tags, the index to write the value to.
    try {
      TagValue result = apiInstance.writeTag(id, value, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataStoreApi#writeTag");
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
| **id** | **BigDecimal**| ID of the tag to write. | |
| **value** | **String**| Value to write to the tag. Must be a string, number, or boolean. | |
| **index** | **BigDecimal**| For array tags, the index to write the value to. | [optional] [default to 0.0] |

### Return type

[**TagValue**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

