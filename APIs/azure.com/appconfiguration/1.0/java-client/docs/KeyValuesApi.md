# KeyValuesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkKeyValue**](KeyValuesApi.md#checkKeyValue) | **HEAD** /kv/{key} | Requests the headers and status of the given resource. |
| [**checkKeyValues**](KeyValuesApi.md#checkKeyValues) | **HEAD** /kv | Requests the headers and status of the given resource. |
| [**deleteKeyValue**](KeyValuesApi.md#deleteKeyValue) | **DELETE** /kv/{key} | Deletes a key-value. |
| [**getKeyValue**](KeyValuesApi.md#getKeyValue) | **GET** /kv/{key} | Gets a single key-value. |
| [**getKeyValues**](KeyValuesApi.md#getKeyValues) | **GET** /kv | Gets a list of key-values. |
| [**putKeyValue**](KeyValuesApi.md#putKeyValue) | **PUT** /kv/{key} | Creates a key-value. |


<a id="checkKeyValue"></a>
# **checkKeyValue**
> checkKeyValue(key, apiVersion, label, syncToken, acceptDatetime, ifMatch, ifNoneMatch, $select)

Requests the headers and status of the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to retrieve.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label of the key-value to retrieve.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      apiInstance.checkKeyValue(key, apiVersion, label, syncToken, acceptDatetime, ifMatch, ifNoneMatch, $select);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#checkKeyValue");
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
| **key** | **String**| The key of the key-value to retrieve. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label of the key-value to retrieve. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |
| **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  * Last-Modified - A UTC datetime that specifies the last time the resource was modified. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="checkKeyValues"></a>
# **checkKeyValues**
> checkKeyValues(apiVersion, key, label, syncToken, after, acceptDatetime, $select)

Requests the headers and status of the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String key = "key_example"; // String | A filter used to match keys.
    String label = "label_example"; // String | A filter used to match labels
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      apiInstance.checkKeyValues(apiVersion, key, label, syncToken, after, acceptDatetime, $select);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#checkKeyValues");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **key** | **String**| A filter used to match keys. | [optional] |
| **label** | **String**| A filter used to match labels | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="deleteKeyValue"></a>
# **deleteKeyValue**
> KeyValue deleteKeyValue(key, apiVersion, label, syncToken, ifMatch)

Deletes a key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to delete.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label of the key-value to delete.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    try {
      KeyValue result = apiInstance.deleteKeyValue(key, apiVersion, label, syncToken, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#deleteKeyValue");
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
| **key** | **String**| The key of the key-value to delete. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label of the key-value to delete. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **204** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="getKeyValue"></a>
# **getKeyValue**
> KeyValue getKeyValue(key, apiVersion, label, syncToken, acceptDatetime, ifMatch, ifNoneMatch, $select)

Gets a single key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to retrieve.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label of the key-value to retrieve.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      KeyValue result = apiInstance.getKeyValue(key, apiVersion, label, syncToken, acceptDatetime, ifMatch, ifNoneMatch, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#getKeyValue");
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
| **key** | **String**| The key of the key-value to retrieve. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label of the key-value to retrieve. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |
| **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  * Last-Modified - A UTC datetime that specifies the last time the resource was modified. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="getKeyValues"></a>
# **getKeyValues**
> KeyValueListResult getKeyValues(apiVersion, key, label, syncToken, after, acceptDatetime, $select)

Gets a list of key-values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String key = "key_example"; // String | A filter used to match keys.
    String label = "label_example"; // String | A filter used to match labels
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      KeyValueListResult result = apiInstance.getKeyValues(apiVersion, key, label, syncToken, after, acceptDatetime, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#getKeyValues");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **key** | **String**| A filter used to match keys. | [optional] |
| **label** | **String**| A filter used to match labels | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: key, label, content_type, value, last_modified, tags, locked, etag] |

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.kvset+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="putKeyValue"></a>
# **putKeyValue**
> KeyValue putKeyValue(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch, entity)

Creates a key-value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    KeyValuesApi apiInstance = new KeyValuesApi(defaultClient);
    String key = "key_example"; // String | The key of the key-value to create.
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String label = "label_example"; // String | The label of the key-value to create.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String ifMatch = "ifMatch_example"; // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
    KeyValue entity = new KeyValue(); // KeyValue | The key-value to create.
    try {
      KeyValue result = apiInstance.putKeyValue(key, apiVersion, label, syncToken, ifMatch, ifNoneMatch, entity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyValuesApi#putKeyValue");
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
| **key** | **String**| The key of the key-value to create. | |
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **label** | **String**| The label of the key-value to create. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] |
| **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] |
| **entity** | [**KeyValue**](KeyValue.md)| The key-value to create. | [optional] |

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.microsoft.appconfig.kv+json, application/vnd.microsoft.appconfig.kvset+json, application/json, text/json, application/*+json, application/json-patch+json
 - **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * ETag - An identifier representing the returned state of the resource. <br>  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

