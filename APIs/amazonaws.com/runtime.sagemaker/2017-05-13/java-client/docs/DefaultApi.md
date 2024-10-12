# DefaultApi

All URIs are relative to *http://runtime.sagemaker.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invokeEndpoint**](DefaultApi.md#invokeEndpoint) | **POST** /endpoints/{EndpointName}/invocations |  |
| [**invokeEndpointAsync**](DefaultApi.md#invokeEndpointAsync) | **POST** /endpoints/{EndpointName}/async-invocations#X-Amzn-SageMaker-InputLocation |  |


<a id="invokeEndpoint"></a>
# **invokeEndpoint**
> InvokeEndpointOutput invokeEndpoint(endpointName, invokeEndpointRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, contentType, accept, xAmznSageMakerCustomAttributes, xAmznSageMakerTargetModel, xAmznSageMakerTargetVariant, xAmznSageMakerTargetContainerHostname, xAmznSageMakerInferenceId, xAmznSageMakerEnableExplanations)



&lt;p&gt;After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint. &lt;/p&gt; &lt;p&gt;For an overview of Amazon SageMaker, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html\&quot;&gt;How It Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. &lt;/p&gt; &lt;p&gt;Calls to &lt;code&gt;InvokeEndpoint&lt;/code&gt; are authenticated by using Amazon Web Services Signature Version 4. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A customer&#39;s model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker determines the account ID from the authentication token that is supplied by the caller.&lt;/p&gt; &lt;/note&gt;

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
    defaultClient.setBasePath("http://runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String endpointName = "endpointName_example"; // String | The name of the endpoint that you specified when you created the endpoint using the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html\">CreateEndpoint</a> API. 
    InvokeEndpointRequest invokeEndpointRequest = new InvokeEndpointRequest(); // InvokeEndpointRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String contentType = "contentType_example"; // String | The MIME type of the input data in the request body.
    String accept = "accept_example"; // String | The desired MIME type of the inference in the response.
    String xAmznSageMakerCustomAttributes = "xAmznSageMakerCustomAttributes_example"; // String | <p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href=\"https://tools.ietf.org/html/rfc7230#section-3.2.6\">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID:</code> in your post-processing function.</p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK.</p>
    String xAmznSageMakerTargetModel = "xAmznSageMakerTargetModel_example"; // String | The model to request for inference when invoking a multi-model endpoint.
    String xAmznSageMakerTargetVariant = "xAmznSageMakerTargetVariant_example"; // String | <p>Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.</p> <p>For information about how to use variant targeting to perform a/b testing, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html\">Test models in production</a> </p>
    String xAmznSageMakerTargetContainerHostname = "xAmznSageMakerTargetContainerHostname_example"; // String | If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.
    String xAmznSageMakerInferenceId = "xAmznSageMakerInferenceId_example"; // String | If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html\">Capture Data</a>.
    String xAmznSageMakerEnableExplanations = "xAmznSageMakerEnableExplanations_example"; // String | An optional JMESPath expression used to override the <code>EnableExplanations</code> parameter of the <code>ClarifyExplainerConfig</code> API. See the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable\">EnableExplanations</a> section in the developer guide for more information. 
    try {
      InvokeEndpointOutput result = apiInstance.invokeEndpoint(endpointName, invokeEndpointRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, contentType, accept, xAmznSageMakerCustomAttributes, xAmznSageMakerTargetModel, xAmznSageMakerTargetVariant, xAmznSageMakerTargetContainerHostname, xAmznSageMakerInferenceId, xAmznSageMakerEnableExplanations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#invokeEndpoint");
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
| **endpointName** | **String**| The name of the endpoint that you specified when you created the endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; API.  | |
| **invokeEndpointRequest** | [**InvokeEndpointRequest**](InvokeEndpointRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **contentType** | **String**| The MIME type of the input data in the request body. | [optional] |
| **accept** | **String**| The desired MIME type of the inference in the response. | [optional] |
| **xAmznSageMakerCustomAttributes** | **String**| &lt;p&gt;Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc7230#section-3.2.6\&quot;&gt;Section 3.3.6. Field Value Components&lt;/a&gt; of the Hypertext Transfer Protocol (HTTP/1.1). &lt;/p&gt; &lt;p&gt;The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with &lt;code&gt;Trace ID:&lt;/code&gt; in your post-processing function.&lt;/p&gt; &lt;p&gt;This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK.&lt;/p&gt; | [optional] |
| **xAmznSageMakerTargetModel** | **String**| The model to request for inference when invoking a multi-model endpoint. | [optional] |
| **xAmznSageMakerTargetVariant** | **String**| &lt;p&gt;Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.&lt;/p&gt; &lt;p&gt;For information about how to use variant targeting to perform a/b testing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html\&quot;&gt;Test models in production&lt;/a&gt; &lt;/p&gt; | [optional] |
| **xAmznSageMakerTargetContainerHostname** | **String**| If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke. | [optional] |
| **xAmznSageMakerInferenceId** | **String**| If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html\&quot;&gt;Capture Data&lt;/a&gt;. | [optional] |
| **xAmznSageMakerEnableExplanations** | **String**| An optional JMESPath expression used to override the &lt;code&gt;EnableExplanations&lt;/code&gt; parameter of the &lt;code&gt;ClarifyExplainerConfig&lt;/code&gt; API. See the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable\&quot;&gt;EnableExplanations&lt;/a&gt; section in the developer guide for more information.  | [optional] |

### Return type

[**InvokeEndpointOutput**](InvokeEndpointOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | InternalFailure |  -  |
| **481** | ServiceUnavailable |  -  |
| **482** | ValidationError |  -  |
| **483** | ModelError |  -  |
| **484** | InternalDependencyException |  -  |
| **485** | ModelNotReadyException |  -  |

<a id="invokeEndpointAsync"></a>
# **invokeEndpointAsync**
> InvokeEndpointAsyncOutput invokeEndpointAsync(endpointName, xAmznSageMakerInputLocation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmznSageMakerContentType, xAmznSageMakerAccept, xAmznSageMakerCustomAttributes, xAmznSageMakerInferenceId, xAmznSageMakerRequestTTLSeconds, xAmznSageMakerInvocationTimeoutSeconds)



&lt;p&gt;After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint in an asynchronous manner.&lt;/p&gt; &lt;p&gt;Inference requests sent to this API are enqueued for asynchronous processing. The processing of the inference request may or may not complete before you receive a response from this API. The response from this API will not contain the result of the inference request but contain information about where you can locate it.&lt;/p&gt; &lt;p&gt;Amazon SageMaker strips all &lt;code&gt;POST&lt;/code&gt; headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.&lt;/p&gt; &lt;p&gt;Calls to &lt;code&gt;InvokeEndpointAsync&lt;/code&gt; are authenticated by using Amazon Web Services Signature Version 4. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;.&lt;/p&gt;

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
    defaultClient.setBasePath("http://runtime.sagemaker.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String endpointName = "endpointName_example"; // String | The name of the endpoint that you specified when you created the endpoint using the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html\"> <code>CreateEndpoint</code> </a> API.
    String xAmznSageMakerInputLocation = "xAmznSageMakerInputLocation_example"; // String | The Amazon S3 URI where the inference request payload is stored.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmznSageMakerContentType = "xAmznSageMakerContentType_example"; // String | The MIME type of the input data in the request body.
    String xAmznSageMakerAccept = "xAmznSageMakerAccept_example"; // String | The desired MIME type of the inference in the response.
    String xAmznSageMakerCustomAttributes = "xAmznSageMakerCustomAttributes_example"; // String | <p>Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in <a href=\"https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6\">Section 3.3.6. Field Value Components</a> of the Hypertext Transfer Protocol (HTTP/1.1). </p> <p>The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with <code>Trace ID</code>: in your post-processing function. </p> <p>This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK. </p>
    String xAmznSageMakerInferenceId = "xAmznSageMakerInferenceId_example"; // String | The identifier for the inference request. Amazon SageMaker will generate an identifier for you if none is specified. 
    Integer xAmznSageMakerRequestTTLSeconds = 56; // Integer | Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.
    Integer xAmznSageMakerInvocationTimeoutSeconds = 56; // Integer | Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.
    try {
      InvokeEndpointAsyncOutput result = apiInstance.invokeEndpointAsync(endpointName, xAmznSageMakerInputLocation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmznSageMakerContentType, xAmznSageMakerAccept, xAmznSageMakerCustomAttributes, xAmznSageMakerInferenceId, xAmznSageMakerRequestTTLSeconds, xAmznSageMakerInvocationTimeoutSeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#invokeEndpointAsync");
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
| **endpointName** | **String**| The name of the endpoint that you specified when you created the endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html\&quot;&gt; &lt;code&gt;CreateEndpoint&lt;/code&gt; &lt;/a&gt; API. | |
| **xAmznSageMakerInputLocation** | **String**| The Amazon S3 URI where the inference request payload is stored. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmznSageMakerContentType** | **String**| The MIME type of the input data in the request body. | [optional] |
| **xAmznSageMakerAccept** | **String**| The desired MIME type of the inference in the response. | [optional] |
| **xAmznSageMakerCustomAttributes** | **String**| &lt;p&gt;Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in &lt;a href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6\&quot;&gt;Section 3.3.6. Field Value Components&lt;/a&gt; of the Hypertext Transfer Protocol (HTTP/1.1). &lt;/p&gt; &lt;p&gt;The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with &lt;code&gt;Trace ID&lt;/code&gt;: in your post-processing function. &lt;/p&gt; &lt;p&gt;This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK. &lt;/p&gt; | [optional] |
| **xAmznSageMakerInferenceId** | **String**| The identifier for the inference request. Amazon SageMaker will generate an identifier for you if none is specified.  | [optional] |
| **xAmznSageMakerRequestTTLSeconds** | **Integer**| Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds. | [optional] |
| **xAmznSageMakerInvocationTimeoutSeconds** | **Integer**| Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds. | [optional] |

### Return type

[**InvokeEndpointAsyncOutput**](InvokeEndpointAsyncOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | InternalFailure |  -  |
| **481** | ServiceUnavailable |  -  |
| **482** | ValidationError |  -  |

