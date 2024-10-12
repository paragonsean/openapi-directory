# MessagesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**messagesIDGet**](MessagesApi.md#messagesIDGet) | **GET** /messages/{ID} |  |
| [**messagesIDMetadataCollectionsGet**](MessagesApi.md#messagesIDMetadataCollectionsGet) | **GET** /messages/{ID}/metadata/collections |  |
| [**messagesIDMetadataGet**](MessagesApi.md#messagesIDMetadataGet) | **GET** /messages/{ID}/metadata |  |
| [**messagesIDMetadataPost**](MessagesApi.md#messagesIDMetadataPost) | **POST** /messages/{ID}/metadata |  |
| [**messagesMetadataFiltersPost**](MessagesApi.md#messagesMetadataFiltersPost) | **POST** /messages/metadata/filters |  |


<a id="messagesIDGet"></a>
# **messagesIDGet**
> EndpointGetMessagesID messagesIDGet(ID)



Fetch an array of messages. You can only retrieve messages authored by you or by users who exist within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetMessagesID result = apiInstance.messagesIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesIDGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetMessagesID**](EndpointGetMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="messagesIDMetadataCollectionsGet"></a>
# **messagesIDMetadataCollectionsGet**
> EndpointGetMessagesIDMetadataCollections messagesIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointGetMessagesIDMetadataCollections result = apiInstance.messagesIDMetadataCollectionsGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesIDMetadataCollectionsGet");
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
| **ID** | **Integer**|  | |

### Return type

[**EndpointGetMessagesIDMetadataCollections**](EndpointGetMessagesIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="messagesIDMetadataGet"></a>
# **messagesIDMetadataGet**
> EndpointGetMessagesIDMetadata messagesIDMetadataGet(ID, offset, limit)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetMessagesIDMetadata result = apiInstance.messagesIDMetadataGet(ID, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesIDMetadataGet");
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
| **ID** | **Integer**|  | |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetMessagesIDMetadata**](EndpointGetMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="messagesIDMetadataPost"></a>
# **messagesIDMetadataPost**
> EndpointPostMessagesIDMetadata messagesIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values)



Attach one-to-many key/value pairs of metadata to a message, so long as the user who authored the message exists within the current access token&#39;s bubble. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by you or the other user in the message&#39;s conversation, using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Bubbled metadata by you or the other user in the message&#39;s conversation, using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message, if it wasn&#39;t you; Private metadata by you, so long as you are using an access token existing within the current bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer ID = 56; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    String metadata0Privacy = "Public"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    String metadata1Privacy = "Public"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    String metadata2Privacy = "Public"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    try {
      EndpointPostMessagesIDMetadata result = apiInstance.messagesIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesIDMetadataPost");
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
| **ID** | **Integer**|  | |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**EndpointPostMessagesIDMetadata**](EndpointPostMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="messagesMetadataFiltersPost"></a>
# **messagesMetadataFiltersPost**
> EndpointPostMessagesMetadataFilters messagesMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset)



Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    Integer limit = 50; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    Integer offset = 0; // Integer | 
    try {
      EndpointPostMessagesMetadataFilters result = apiInstance.messagesMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#messagesMetadataFiltersPost");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**EndpointPostMessagesMetadataFilters**](EndpointPostMessagesMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

