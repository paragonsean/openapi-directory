# TransportSms77Api

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTransportSms77GetCollection**](TransportSms77Api.md#apiTransportSms77GetCollection) | **GET** /api/transport-sms77 | Retrieves the collection of TransportSms77 resources. |
| [**apiTransportSms77IdDelete**](TransportSms77Api.md#apiTransportSms77IdDelete) | **DELETE** /api/transport-sms77/{id} | Removes the TransportSms77 resource. |
| [**apiTransportSms77IdGet**](TransportSms77Api.md#apiTransportSms77IdGet) | **GET** /api/transport-sms77/{id} | Retrieves a TransportSms77 resource. |
| [**apiTransportSms77IdPatch**](TransportSms77Api.md#apiTransportSms77IdPatch) | **PATCH** /api/transport-sms77/{id} | Updates the TransportSms77 resource. |
| [**apiTransportSms77IdPut**](TransportSms77Api.md#apiTransportSms77IdPut) | **PUT** /api/transport-sms77/{id} | Replaces the TransportSms77 resource. |
| [**apiTransportSms77Post**](TransportSms77Api.md#apiTransportSms77Post) | **POST** /api/transport-sms77 | Creates a TransportSms77 resource. |


<a id="apiTransportSms77GetCollection"></a>
# **apiTransportSms77GetCollection**
> List&lt;TransportSms77Get&gt; apiTransportSms77GetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties)

Retrieves the collection of TransportSms77 resources.

Retrieves the collection of TransportSms77 resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    Integer page = 1; // Integer | The collection page number
    String dataSegmentCode = "dataSegmentCode_example"; // String | 
    List<String> dataSegmentCode2 = Arrays.asList(); // List<String> | 
    String partition = "partition_example"; // String | 
    List<String> partition2 = Arrays.asList(); // List<String> | 
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<TransportSms77Get> result = apiInstance.apiTransportSms77GetCollection(page, dataSegmentCode, dataSegmentCode2, partition, partition2, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77GetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **dataSegmentCode** | **String**|  | [optional] |
| **dataSegmentCode2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **partition** | **String**|  | [optional] |
| **partition2** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;TransportSms77Get&gt;**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSms77 collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSms77IdDelete"></a>
# **apiTransportSms77IdDelete**
> apiTransportSms77IdDelete(id)

Removes the TransportSms77 resource.

Removes the TransportSms77 resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    String id = "id_example"; // String | TransportSms77 identifier
    try {
      apiInstance.apiTransportSms77IdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77IdDelete");
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
| **id** | **String**| TransportSms77 identifier | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | TransportSms77 resource deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSms77IdGet"></a>
# **apiTransportSms77IdGet**
> TransportSms77Get apiTransportSms77IdGet(id)

Retrieves a TransportSms77 resource.

Retrieves a TransportSms77 resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    String id = "id_example"; // String | TransportSms77 identifier
    try {
      TransportSms77Get result = apiInstance.apiTransportSms77IdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77IdGet");
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
| **id** | **String**| TransportSms77 identifier | |

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSms77 resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSms77IdPatch"></a>
# **apiTransportSms77IdPatch**
> TransportSms77Get apiTransportSms77IdPatch(id, transportSms77Patch)

Updates the TransportSms77 resource.

Updates the TransportSms77 resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    String id = "id_example"; // String | TransportSms77 identifier
    TransportSms77Patch transportSms77Patch = new TransportSms77Patch(); // TransportSms77Patch | The updated TransportSms77 resource
    try {
      TransportSms77Get result = apiInstance.apiTransportSms77IdPatch(id, transportSms77Patch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77IdPatch");
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
| **id** | **String**| TransportSms77 identifier | |
| **transportSms77Patch** | [**TransportSms77Patch**](TransportSms77Patch.md)| The updated TransportSms77 resource | |

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSms77 resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSms77IdPut"></a>
# **apiTransportSms77IdPut**
> TransportSms77Get apiTransportSms77IdPut(id, transportSms77Put)

Replaces the TransportSms77 resource.

Replaces the TransportSms77 resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    String id = "id_example"; // String | TransportSms77 identifier
    TransportSms77Put transportSms77Put = new TransportSms77Put(); // TransportSms77Put | The updated TransportSms77 resource
    try {
      TransportSms77Get result = apiInstance.apiTransportSms77IdPut(id, transportSms77Put);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77IdPut");
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
| **id** | **String**| TransportSms77 identifier | |
| **transportSms77Put** | [**TransportSms77Put**](TransportSms77Put.md)| The updated TransportSms77 resource | |

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TransportSms77 resource updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

<a id="apiTransportSms77Post"></a>
# **apiTransportSms77Post**
> TransportSms77Get apiTransportSms77Post(transportSms77Post)

Creates a TransportSms77 resource.

Creates a TransportSms77 resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransportSms77Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    TransportSms77Api apiInstance = new TransportSms77Api(defaultClient);
    TransportSms77Post transportSms77Post = new TransportSms77Post(); // TransportSms77Post | The new TransportSms77 resource
    try {
      TransportSms77Get result = apiInstance.apiTransportSms77Post(transportSms77Post);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransportSms77Api#apiTransportSms77Post");
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
| **transportSms77Post** | [**TransportSms77Post**](TransportSms77Post.md)| The new TransportSms77 resource | |

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/ld+json, text/html
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | TransportSms77 resource created |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable entity |  -  |
| **429** | Too many requests |  -  |

