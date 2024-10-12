from typing import List, Dict
from aiohttp import web

from openapi_server.models.invoke_endpoint_async_output import InvokeEndpointAsyncOutput
from openapi_server.models.invoke_endpoint_output import InvokeEndpointOutput
from openapi_server.models.invoke_endpoint_request import InvokeEndpointRequest
from openapi_server import util


async def invoke_endpoint(request: web.Request, endpoint_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, content_type=None, accept=None, x_amzn_sage_maker_custom_attributes=None, x_amzn_sage_maker_target_model=None, x_amzn_sage_maker_target_variant=None, x_amzn_sage_maker_target_container_hostname=None, x_amzn_sage_maker_inference_id=None, x_amzn_sage_maker_enable_explanations=None) -> web.Response:
    """invoke_endpoint

    &lt;p&gt;After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint. &lt;/p&gt; &lt;p&gt;For an overview of Amazon SageMaker, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works.html\&quot;&gt;How It Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Amazon SageMaker strips all POST headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax. &lt;/p&gt; &lt;p&gt;Calls to &lt;code&gt;InvokeEndpoint&lt;/code&gt; are authenticated by using Amazon Web Services Signature Version 4. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;A customer&#39;s model containers must respond to requests within 60 seconds. The model itself can have a maximum processing time of 60 seconds before responding to invocations. If your model is going to take 50-60 seconds of processing time, the SDK socket timeout should be set to be 70 seconds.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Endpoints are scoped to an individual account, and are not public. The URL does not contain the account ID, but Amazon SageMaker determines the account ID from the authentication token that is supplied by the caller.&lt;/p&gt; &lt;/note&gt;

    :param endpoint_name: The name of the endpoint that you specified when you created the endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; API. 
    :type endpoint_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param content_type: The MIME type of the input data in the request body.
    :type content_type: str
    :param accept: The desired MIME type of the inference in the response.
    :type accept: str
    :param x_amzn_sage_maker_custom_attributes: &lt;p&gt;Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc7230#section-3.2.6\&quot;&gt;Section 3.3.6. Field Value Components&lt;/a&gt; of the Hypertext Transfer Protocol (HTTP/1.1). &lt;/p&gt; &lt;p&gt;The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with &lt;code&gt;Trace ID:&lt;/code&gt; in your post-processing function.&lt;/p&gt; &lt;p&gt;This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK.&lt;/p&gt;
    :type x_amzn_sage_maker_custom_attributes: str
    :param x_amzn_sage_maker_target_model: The model to request for inference when invoking a multi-model endpoint.
    :type x_amzn_sage_maker_target_model: str
    :param x_amzn_sage_maker_target_variant: &lt;p&gt;Specify the production variant to send the inference request to when invoking an endpoint that is running two or more variants. Note that this parameter overrides the default behavior for the endpoint, which is to distribute the invocation traffic based on the variant weights.&lt;/p&gt; &lt;p&gt;For information about how to use variant targeting to perform a/b testing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html\&quot;&gt;Test models in production&lt;/a&gt; &lt;/p&gt;
    :type x_amzn_sage_maker_target_variant: str
    :param x_amzn_sage_maker_target_container_hostname: If the endpoint hosts multiple containers and is configured to use direct invocation, this parameter specifies the host name of the container to invoke.
    :type x_amzn_sage_maker_target_container_hostname: str
    :param x_amzn_sage_maker_inference_id: If you provide a value, it is added to the captured data when you enable data capture on the endpoint. For information about data capture, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html\&quot;&gt;Capture Data&lt;/a&gt;.
    :type x_amzn_sage_maker_inference_id: str
    :param x_amzn_sage_maker_enable_explanations: An optional JMESPath expression used to override the &lt;code&gt;EnableExplanations&lt;/code&gt; parameter of the &lt;code&gt;ClarifyExplainerConfig&lt;/code&gt; API. See the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html#clarify-online-explainability-create-endpoint-enable\&quot;&gt;EnableExplanations&lt;/a&gt; section in the developer guide for more information. 
    :type x_amzn_sage_maker_enable_explanations: str

    """
    body = InvokeEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def invoke_endpoint_async(request: web.Request, endpoint_name, x_amzn_sage_maker_input_location, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amzn_sage_maker_content_type=None, x_amzn_sage_maker_accept=None, x_amzn_sage_maker_custom_attributes=None, x_amzn_sage_maker_inference_id=None, x_amzn_sage_maker_request_ttl_seconds=None, x_amzn_sage_maker_invocation_timeout_seconds=None) -> web.Response:
    """invoke_endpoint_async

    &lt;p&gt;After you deploy a model into production using Amazon SageMaker hosting services, your client applications use this API to get inferences from the model hosted at the specified endpoint in an asynchronous manner.&lt;/p&gt; &lt;p&gt;Inference requests sent to this API are enqueued for asynchronous processing. The processing of the inference request may or may not complete before you receive a response from this API. The response from this API will not contain the result of the inference request but contain information about where you can locate it.&lt;/p&gt; &lt;p&gt;Amazon SageMaker strips all &lt;code&gt;POST&lt;/code&gt; headers except those supported by the API. Amazon SageMaker might add additional headers. You should not rely on the behavior of headers outside those enumerated in the request syntax.&lt;/p&gt; &lt;p&gt;Calls to &lt;code&gt;InvokeEndpointAsync&lt;/code&gt; are authenticated by using Amazon Web Services Signature Version 4. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon S3 API Reference&lt;/i&gt;.&lt;/p&gt;

    :param endpoint_name: The name of the endpoint that you specified when you created the endpoint using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html\&quot;&gt; &lt;code&gt;CreateEndpoint&lt;/code&gt; &lt;/a&gt; API.
    :type endpoint_name: str
    :param x_amzn_sage_maker_input_location: The Amazon S3 URI where the inference request payload is stored.
    :type x_amzn_sage_maker_input_location: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param x_amzn_sage_maker_content_type: The MIME type of the input data in the request body.
    :type x_amzn_sage_maker_content_type: str
    :param x_amzn_sage_maker_accept: The desired MIME type of the inference in the response.
    :type x_amzn_sage_maker_accept: str
    :param x_amzn_sage_maker_custom_attributes: &lt;p&gt;Provides additional information about a request for an inference submitted to a model hosted at an Amazon SageMaker endpoint. The information is an opaque value that is forwarded verbatim. You could use this value, for example, to provide an ID that you can use to track a request or to provide other metadata that a service endpoint was programmed to process. The value must consist of no more than 1024 visible US-ASCII characters as specified in &lt;a href&#x3D;\&quot;https://datatracker.ietf.org/doc/html/rfc7230#section-3.2.6\&quot;&gt;Section 3.3.6. Field Value Components&lt;/a&gt; of the Hypertext Transfer Protocol (HTTP/1.1). &lt;/p&gt; &lt;p&gt;The code in your model is responsible for setting or updating any custom attributes in the response. If your code does not set this value in the response, an empty value is returned. For example, if a custom attribute represents the trace ID, your model can prepend the custom attribute with &lt;code&gt;Trace ID&lt;/code&gt;: in your post-processing function. &lt;/p&gt; &lt;p&gt;This feature is currently supported in the Amazon Web Services SDKs but not in the Amazon SageMaker Python SDK. &lt;/p&gt;
    :type x_amzn_sage_maker_custom_attributes: str
    :param x_amzn_sage_maker_inference_id: The identifier for the inference request. Amazon SageMaker will generate an identifier for you if none is specified. 
    :type x_amzn_sage_maker_inference_id: str
    :param x_amzn_sage_maker_request_ttl_seconds: Maximum age in seconds a request can be in the queue before it is marked as expired. The default is 6 hours, or 21,600 seconds.
    :type x_amzn_sage_maker_request_ttl_seconds: int
    :param x_amzn_sage_maker_invocation_timeout_seconds: Maximum amount of time in seconds a request can be processed before it is marked as expired. The default is 15 minutes, or 900 seconds.
    :type x_amzn_sage_maker_invocation_timeout_seconds: int

    """
    return web.Response(status=200)
