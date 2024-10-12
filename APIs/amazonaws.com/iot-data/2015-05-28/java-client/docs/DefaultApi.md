# DefaultApi

All URIs are relative to *http://data-ats.iot.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteThingShadow**](DefaultApi.md#deleteThingShadow) | **DELETE** /things/{thingName}/shadow |  |
| [**getRetainedMessage**](DefaultApi.md#getRetainedMessage) | **GET** /retainedMessage/{topic} |  |
| [**getThingShadow**](DefaultApi.md#getThingShadow) | **GET** /things/{thingName}/shadow |  |
| [**listNamedShadowsForThing**](DefaultApi.md#listNamedShadowsForThing) | **GET** /api/things/shadow/ListNamedShadowsForThing/{thingName} |  |
| [**listRetainedMessages**](DefaultApi.md#listRetainedMessages) | **GET** /retainedMessage |  |
| [**publish**](DefaultApi.md#publish) | **POST** /topics/{topic} |  |
| [**updateThingShadow**](DefaultApi.md#updateThingShadow) | **POST** /things/{thingName}/shadow |  |


<a id="deleteThingShadow"></a>
# **deleteThingShadow**
> DeleteThingShadowResponse deleteThingShadow(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name)



&lt;p&gt;Deletes the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;DeleteThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_DeleteThingShadow.html\&quot;&gt;DeleteThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String thingName = "thingName_example"; // String | The name of the thing.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String name = "name_example"; // String | The name of the shadow.
    try {
      DeleteThingShadowResponse result = apiInstance.deleteThingShadow(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteThingShadow");
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
| **thingName** | **String**| The name of the thing. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **name** | **String**| The name of the shadow. | [optional] |

### Return type

[**DeleteThingShadowResponse**](DeleteThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | UnauthorizedException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalFailureException |  -  |
| **486** | MethodNotAllowedException |  -  |
| **487** | UnsupportedDocumentEncodingException |  -  |

<a id="getRetainedMessage"></a>
# **getRetainedMessage**
> GetRetainedMessageResponse getRetainedMessage(topic, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the details of a single retained message for the specified topic.&lt;/p&gt; &lt;p&gt;This action returns the message payload of the retained message, which can incur messaging costs. To list only the topic names of the retained messages, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_ListRetainedMessages.html\&quot;&gt;ListRetainedMessages&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;GetRetainedMessage&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String topic = "topic_example"; // String | The topic name of the retained message to retrieve.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetRetainedMessageResponse result = apiInstance.getRetainedMessage(topic, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRetainedMessage");
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
| **topic** | **String**| The topic name of the retained message to retrieve. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetRetainedMessageResponse**](GetRetainedMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | UnauthorizedException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalFailureException |  -  |
| **486** | MethodNotAllowedException |  -  |

<a id="getThingShadow"></a>
# **getThingShadow**
> GetThingShadowResponse getThingShadow(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name)



&lt;p&gt;Gets the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;GetThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_GetThingShadow.html\&quot;&gt;GetThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String thingName = "thingName_example"; // String | The name of the thing.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String name = "name_example"; // String | The name of the shadow.
    try {
      GetThingShadowResponse result = apiInstance.getThingShadow(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getThingShadow");
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
| **thingName** | **String**| The name of the thing. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **name** | **String**| The name of the shadow. | [optional] |

### Return type

[**GetThingShadowResponse**](GetThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ResourceNotFoundException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | UnauthorizedException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalFailureException |  -  |
| **486** | MethodNotAllowedException |  -  |
| **487** | UnsupportedDocumentEncodingException |  -  |

<a id="listNamedShadowsForThing"></a>
# **listNamedShadowsForThing**
> ListNamedShadowsForThingResponse listNamedShadowsForThing(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, pageSize)



&lt;p&gt;Lists the shadows for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;ListNamedShadowsForThing&lt;/a&gt; action.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String thingName = "thingName_example"; // String | The name of the thing.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to retrieve the next set of results.
    Integer pageSize = 56; // Integer | The result page size.
    try {
      ListNamedShadowsForThingResponse result = apiInstance.listNamedShadowsForThing(thingName, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listNamedShadowsForThing");
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
| **thingName** | **String**| The name of the thing. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to retrieve the next set of results. | [optional] |
| **pageSize** | **Integer**| The result page size. | [optional] |

### Return type

[**ListNamedShadowsForThingResponse**](ListNamedShadowsForThingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ResourceNotFoundException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | ThrottlingException |  -  |
| **483** | UnauthorizedException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | InternalFailureException |  -  |
| **486** | MethodNotAllowedException |  -  |

<a id="listRetainedMessages"></a>
# **listRetainedMessages**
> ListRetainedMessagesResponse listRetainedMessages(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults)



&lt;p&gt;Lists summary information about the retained messages stored for the account.&lt;/p&gt; &lt;p&gt;This action returns only the topic names of the retained messages. It doesn&#39;t return any message payloads. Although this action doesn&#39;t return a message payload, it can still incur messaging costs.&lt;/p&gt; &lt;p&gt;To get the message payload of a retained message, call &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_GetRetainedMessage.html\&quot;&gt;GetRetainedMessage&lt;/a&gt; with the topic name of the retained message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiotfleethubfordevicemanagement.html#awsiotfleethubfordevicemanagement-actions-as-permissions\&quot;&gt;ListRetainedMessages&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return at one time.
    try {
      ListRetainedMessagesResponse result = apiInstance.listRetainedMessages(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRetainedMessages");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| To retrieve the next set of results, the &lt;code&gt;nextToken&lt;/code&gt; value from a previous response; otherwise &lt;b&gt;null&lt;/b&gt; to receive the first set of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return at one time. | [optional] |

### Return type

[**ListRetainedMessagesResponse**](ListRetainedMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InvalidRequestException |  -  |
| **481** | ThrottlingException |  -  |
| **482** | UnauthorizedException |  -  |
| **483** | ServiceUnavailableException |  -  |
| **484** | InternalFailureException |  -  |
| **485** | MethodNotAllowedException |  -  |

<a id="publish"></a>
# **publish**
> publish(topic, publishRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, qos, retain, xAmzMqtt5UserProperties, xAmzMqtt5PayloadFormatIndicator, contentType, responseTopic, xAmzMqtt5CorrelationData, messageExpiry)



&lt;p&gt;Publishes an MQTT message.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;Publish&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information about MQTT messages, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html\&quot;&gt;MQTT Protocol&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt; &lt;p&gt;For more information about messaging costs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/iot-core/pricing/#Messaging\&quot;&gt;Amazon Web Services IoT Core pricing - Messaging&lt;/a&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String topic = "topic_example"; // String | The name of the MQTT topic.
    PublishRequest publishRequest = new PublishRequest(); // PublishRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer qos = 56; // Integer | The Quality of Service (QoS) level. The default QoS level is 0.
    Boolean retain = true; // Boolean | <p>A Boolean value that determines whether to set the RETAIN flag when the message is published.</p> <p>Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.</p> <p>Valid values: <code>true</code> | <code>false</code> </p> <p>Default value: <code>false</code> </p>
    String xAmzMqtt5UserProperties = "xAmzMqtt5UserProperties_example"; // String | <p>A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. <code>userProperties</code> is an HTTP header value in the API.</p> <p>The following example <code>userProperties</code> parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:</p> <p> <code>[{\"deviceName\": \"alpha\"}, {\"deviceCnt\": \"45\"}]</code> </p>
    String xAmzMqtt5PayloadFormatIndicator = "UNSPECIFIED_BYTES"; // String | An <code>Enum</code> string value that indicates whether the payload is formatted as UTF-8. <code>payloadFormatIndicator</code> is an HTTP header value in the API.
    String contentType = "contentType_example"; // String | A UTF-8 encoded string that describes the content of the publishing message.
    String responseTopic = "responseTopic_example"; // String | A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.
    String xAmzMqtt5CorrelationData = "xAmzMqtt5CorrelationData_example"; // String | The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received. <code>correlationData</code> is an HTTP header value in the API.
    Integer messageExpiry = 56; // Integer | A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn't expire. For more information about the limits of <code>messageExpiry</code>, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits\">Amazon Web Services IoT Core message broker and protocol limits and quotas </a> from the Amazon Web Services Reference Guide.
    try {
      apiInstance.publish(topic, publishRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, qos, retain, xAmzMqtt5UserProperties, xAmzMqtt5PayloadFormatIndicator, contentType, responseTopic, xAmzMqtt5CorrelationData, messageExpiry);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publish");
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
| **topic** | **String**| The name of the MQTT topic. | |
| **publishRequest** | [**PublishRequest**](PublishRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **qos** | **Integer**| The Quality of Service (QoS) level. The default QoS level is 0. | [optional] |
| **retain** | **Boolean**| &lt;p&gt;A Boolean value that determines whether to set the RETAIN flag when the message is published.&lt;/p&gt; &lt;p&gt;Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;true&lt;/code&gt; | &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;false&lt;/code&gt; &lt;/p&gt; | [optional] |
| **xAmzMqtt5UserProperties** | **String**| &lt;p&gt;A JSON string that contains an array of JSON objects. If you don’t use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. &lt;code&gt;userProperties&lt;/code&gt; is an HTTP header value in the API.&lt;/p&gt; &lt;p&gt;The following example &lt;code&gt;userProperties&lt;/code&gt; parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:&lt;/p&gt; &lt;p&gt; &lt;code&gt;[{\&quot;deviceName\&quot;: \&quot;alpha\&quot;}, {\&quot;deviceCnt\&quot;: \&quot;45\&quot;}]&lt;/code&gt; &lt;/p&gt; | [optional] |
| **xAmzMqtt5PayloadFormatIndicator** | **String**| An &lt;code&gt;Enum&lt;/code&gt; string value that indicates whether the payload is formatted as UTF-8. &lt;code&gt;payloadFormatIndicator&lt;/code&gt; is an HTTP header value in the API. | [optional] [enum: UNSPECIFIED_BYTES, UTF8_DATA] |
| **contentType** | **String**| A UTF-8 encoded string that describes the content of the publishing message. | [optional] |
| **responseTopic** | **String**| A UTF-8 encoded string that&#39;s used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters. | [optional] |
| **xAmzMqtt5CorrelationData** | **String**| The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it&#39;s received. &lt;code&gt;correlationData&lt;/code&gt; is an HTTP header value in the API. | [optional] |
| **messageExpiry** | **Integer**| A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesn&#39;t expire. For more information about the limits of &lt;code&gt;messageExpiry&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits\&quot;&gt;Amazon Web Services IoT Core message broker and protocol limits and quotas &lt;/a&gt; from the Amazon Web Services Reference Guide. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalFailureException |  -  |
| **481** | InvalidRequestException |  -  |
| **482** | UnauthorizedException |  -  |
| **483** | MethodNotAllowedException |  -  |
| **484** | ThrottlingException |  -  |

<a id="updateThingShadow"></a>
# **updateThingShadow**
> UpdateThingShadowResponse updateThingShadow(thingName, updateThingShadowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name)



&lt;p&gt;Updates the shadow for the specified thing.&lt;/p&gt; &lt;p&gt;Requires permission to access the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions\&quot;&gt;UpdateThingShadow&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/iot/latest/developerguide/API_UpdateThingShadow.html\&quot;&gt;UpdateThingShadow&lt;/a&gt; in the IoT Developer Guide.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data-ats.iot.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String thingName = "thingName_example"; // String | The name of the thing.
    UpdateThingShadowRequest updateThingShadowRequest = new UpdateThingShadowRequest(); // UpdateThingShadowRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String name = "name_example"; // String | The name of the shadow.
    try {
      UpdateThingShadowResponse result = apiInstance.updateThingShadow(thingName, updateThingShadowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateThingShadow");
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
| **thingName** | **String**| The name of the thing. | |
| **updateThingShadowRequest** | [**UpdateThingShadowRequest**](UpdateThingShadowRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **name** | **String**| The name of the shadow. | [optional] |

### Return type

[**UpdateThingShadowResponse**](UpdateThingShadowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | RequestEntityTooLargeException |  -  |
| **482** | InvalidRequestException |  -  |
| **483** | ThrottlingException |  -  |
| **484** | UnauthorizedException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | InternalFailureException |  -  |
| **487** | MethodNotAllowedException |  -  |
| **488** | UnsupportedDocumentEncodingException |  -  |

