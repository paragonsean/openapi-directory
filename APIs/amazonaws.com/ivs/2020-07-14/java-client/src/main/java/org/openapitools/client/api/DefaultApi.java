/*
 * Amazon Interactive Video Service
 * <p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-14
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.BatchGetChannelRequest;
import org.openapitools.client.model.BatchGetChannelResponse;
import org.openapitools.client.model.BatchGetStreamKeyRequest;
import org.openapitools.client.model.BatchGetStreamKeyResponse;
import org.openapitools.client.model.BatchStartViewerSessionRevocationRequest;
import org.openapitools.client.model.BatchStartViewerSessionRevocationResponse;
import org.openapitools.client.model.CreateChannelRequest;
import org.openapitools.client.model.CreateChannelResponse;
import org.openapitools.client.model.CreateRecordingConfigurationRequest;
import org.openapitools.client.model.CreateRecordingConfigurationResponse;
import org.openapitools.client.model.CreateStreamKeyRequest;
import org.openapitools.client.model.CreateStreamKeyResponse;
import org.openapitools.client.model.DeleteChannelRequest;
import org.openapitools.client.model.DeletePlaybackKeyPairRequest;
import org.openapitools.client.model.DeleteRecordingConfigurationRequest;
import org.openapitools.client.model.DeleteStreamKeyRequest;
import org.openapitools.client.model.GetChannelRequest;
import org.openapitools.client.model.GetChannelResponse;
import org.openapitools.client.model.GetPlaybackKeyPairRequest;
import org.openapitools.client.model.GetPlaybackKeyPairResponse;
import org.openapitools.client.model.GetRecordingConfigurationRequest;
import org.openapitools.client.model.GetRecordingConfigurationResponse;
import org.openapitools.client.model.GetStreamKeyRequest;
import org.openapitools.client.model.GetStreamKeyResponse;
import org.openapitools.client.model.GetStreamRequest;
import org.openapitools.client.model.GetStreamResponse;
import org.openapitools.client.model.GetStreamSessionRequest;
import org.openapitools.client.model.GetStreamSessionResponse;
import org.openapitools.client.model.ImportPlaybackKeyPairRequest;
import org.openapitools.client.model.ImportPlaybackKeyPairResponse;
import org.openapitools.client.model.ListChannelsRequest;
import org.openapitools.client.model.ListChannelsResponse;
import org.openapitools.client.model.ListPlaybackKeyPairsRequest;
import org.openapitools.client.model.ListPlaybackKeyPairsResponse;
import org.openapitools.client.model.ListRecordingConfigurationsRequest;
import org.openapitools.client.model.ListRecordingConfigurationsResponse;
import org.openapitools.client.model.ListStreamKeysRequest;
import org.openapitools.client.model.ListStreamKeysResponse;
import org.openapitools.client.model.ListStreamSessionsRequest;
import org.openapitools.client.model.ListStreamSessionsResponse;
import org.openapitools.client.model.ListStreamsRequest;
import org.openapitools.client.model.ListStreamsResponse;
import org.openapitools.client.model.ListTagsForResourceResponse;
import org.openapitools.client.model.PutMetadataRequest;
import org.openapitools.client.model.StartViewerSessionRevocationRequest;
import org.openapitools.client.model.StopStreamRequest;
import org.openapitools.client.model.TagResourceRequest;
import org.openapitools.client.model.UpdateChannelRequest;
import org.openapitools.client.model.UpdateChannelResponse;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for batchGetChannel
     * @param batchGetChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchGetChannelCall(BatchGetChannelRequest batchGetChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = batchGetChannelRequest;

        // create path and map variables
        String localVarPath = "/BatchGetChannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call batchGetChannelValidateBeforeCall(BatchGetChannelRequest batchGetChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'batchGetChannelRequest' is set
        if (batchGetChannelRequest == null) {
            throw new ApiException("Missing the required parameter 'batchGetChannelRequest' when calling batchGetChannel(Async)");
        }

        return batchGetChannelCall(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Performs &lt;a&gt;GetChannel&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return BatchGetChannelResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public BatchGetChannelResponse batchGetChannel(BatchGetChannelRequest batchGetChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<BatchGetChannelResponse> localVarResp = batchGetChannelWithHttpInfo(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Performs &lt;a&gt;GetChannel&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;BatchGetChannelResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BatchGetChannelResponse> batchGetChannelWithHttpInfo(BatchGetChannelRequest batchGetChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = batchGetChannelValidateBeforeCall(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<BatchGetChannelResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Performs &lt;a&gt;GetChannel&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchGetChannelAsync(BatchGetChannelRequest batchGetChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<BatchGetChannelResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = batchGetChannelValidateBeforeCall(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<BatchGetChannelResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for batchGetStreamKey
     * @param batchGetStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchGetStreamKeyCall(BatchGetStreamKeyRequest batchGetStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = batchGetStreamKeyRequest;

        // create path and map variables
        String localVarPath = "/BatchGetStreamKey";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call batchGetStreamKeyValidateBeforeCall(BatchGetStreamKeyRequest batchGetStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'batchGetStreamKeyRequest' is set
        if (batchGetStreamKeyRequest == null) {
            throw new ApiException("Missing the required parameter 'batchGetStreamKeyRequest' when calling batchGetStreamKey(Async)");
        }

        return batchGetStreamKeyCall(batchGetStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Performs &lt;a&gt;GetStreamKey&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return BatchGetStreamKeyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public BatchGetStreamKeyResponse batchGetStreamKey(BatchGetStreamKeyRequest batchGetStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<BatchGetStreamKeyResponse> localVarResp = batchGetStreamKeyWithHttpInfo(batchGetStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Performs &lt;a&gt;GetStreamKey&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;BatchGetStreamKeyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BatchGetStreamKeyResponse> batchGetStreamKeyWithHttpInfo(BatchGetStreamKeyRequest batchGetStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = batchGetStreamKeyValidateBeforeCall(batchGetStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<BatchGetStreamKeyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Performs &lt;a&gt;GetStreamKey&lt;/a&gt; on multiple ARNs simultaneously.
     * @param batchGetStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchGetStreamKeyAsync(BatchGetStreamKeyRequest batchGetStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<BatchGetStreamKeyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = batchGetStreamKeyValidateBeforeCall(batchGetStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<BatchGetStreamKeyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for batchStartViewerSessionRevocation
     * @param batchStartViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchStartViewerSessionRevocationCall(BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = batchStartViewerSessionRevocationRequest;

        // create path and map variables
        String localVarPath = "/BatchStartViewerSessionRevocation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call batchStartViewerSessionRevocationValidateBeforeCall(BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'batchStartViewerSessionRevocationRequest' is set
        if (batchStartViewerSessionRevocationRequest == null) {
            throw new ApiException("Missing the required parameter 'batchStartViewerSessionRevocationRequest' when calling batchStartViewerSessionRevocation(Async)");
        }

        return batchStartViewerSessionRevocationCall(batchStartViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Performs &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; on multiple channel ARN and viewer ID pairs simultaneously.
     * @param batchStartViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return BatchStartViewerSessionRevocationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public BatchStartViewerSessionRevocationResponse batchStartViewerSessionRevocation(BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<BatchStartViewerSessionRevocationResponse> localVarResp = batchStartViewerSessionRevocationWithHttpInfo(batchStartViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Performs &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; on multiple channel ARN and viewer ID pairs simultaneously.
     * @param batchStartViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;BatchStartViewerSessionRevocationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BatchStartViewerSessionRevocationResponse> batchStartViewerSessionRevocationWithHttpInfo(BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = batchStartViewerSessionRevocationValidateBeforeCall(batchStartViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<BatchStartViewerSessionRevocationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Performs &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; on multiple channel ARN and viewer ID pairs simultaneously.
     * @param batchStartViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call batchStartViewerSessionRevocationAsync(BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<BatchStartViewerSessionRevocationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = batchStartViewerSessionRevocationValidateBeforeCall(batchStartViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<BatchStartViewerSessionRevocationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createChannel
     * @param createChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createChannelCall(CreateChannelRequest createChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createChannelRequest;

        // create path and map variables
        String localVarPath = "/CreateChannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createChannelValidateBeforeCall(CreateChannelRequest createChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createChannelRequest' is set
        if (createChannelRequest == null) {
            throw new ApiException("Missing the required parameter 'createChannelRequest' when calling createChannel(Async)");
        }

        return createChannelCall(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Creates a new channel and an associated stream key to start streaming.
     * @param createChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateChannelResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public CreateChannelResponse createChannel(CreateChannelRequest createChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateChannelResponse> localVarResp = createChannelWithHttpInfo(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Creates a new channel and an associated stream key to start streaming.
     * @param createChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateChannelResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateChannelResponse> createChannelWithHttpInfo(CreateChannelRequest createChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createChannelValidateBeforeCall(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateChannelResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Creates a new channel and an associated stream key to start streaming.
     * @param createChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createChannelAsync(CreateChannelRequest createChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateChannelResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createChannelValidateBeforeCall(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateChannelResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createRecordingConfiguration
     * @param createRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRecordingConfigurationCall(CreateRecordingConfigurationRequest createRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createRecordingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/CreateRecordingConfiguration";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createRecordingConfigurationValidateBeforeCall(CreateRecordingConfigurationRequest createRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createRecordingConfigurationRequest' is set
        if (createRecordingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'createRecordingConfigurationRequest' when calling createRecordingConfiguration(Async)");
        }

        return createRecordingConfigurationCall(createRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Creates a new recording configuration, used to enable recording to Amazon S3.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Known issue:&lt;/b&gt; In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the &lt;code&gt;state&lt;/code&gt; of the recording configuration is &lt;code&gt;CREATE_FAILED&lt;/code&gt; (instead of &lt;code&gt;ACTIVE&lt;/code&gt;). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)&lt;/p&gt; &lt;p&gt; &lt;b&gt;Workaround:&lt;/b&gt; Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.&lt;/p&gt;
     * @param createRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateRecordingConfigurationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public CreateRecordingConfigurationResponse createRecordingConfiguration(CreateRecordingConfigurationRequest createRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateRecordingConfigurationResponse> localVarResp = createRecordingConfigurationWithHttpInfo(createRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Creates a new recording configuration, used to enable recording to Amazon S3.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Known issue:&lt;/b&gt; In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the &lt;code&gt;state&lt;/code&gt; of the recording configuration is &lt;code&gt;CREATE_FAILED&lt;/code&gt; (instead of &lt;code&gt;ACTIVE&lt;/code&gt;). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)&lt;/p&gt; &lt;p&gt; &lt;b&gt;Workaround:&lt;/b&gt; Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.&lt;/p&gt;
     * @param createRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateRecordingConfigurationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateRecordingConfigurationResponse> createRecordingConfigurationWithHttpInfo(CreateRecordingConfigurationRequest createRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createRecordingConfigurationValidateBeforeCall(createRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateRecordingConfigurationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Creates a new recording configuration, used to enable recording to Amazon S3.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Known issue:&lt;/b&gt; In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the &lt;code&gt;state&lt;/code&gt; of the recording configuration is &lt;code&gt;CREATE_FAILED&lt;/code&gt; (instead of &lt;code&gt;ACTIVE&lt;/code&gt;). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)&lt;/p&gt; &lt;p&gt; &lt;b&gt;Workaround:&lt;/b&gt; Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.&lt;/p&gt;
     * @param createRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRecordingConfigurationAsync(CreateRecordingConfigurationRequest createRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateRecordingConfigurationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createRecordingConfigurationValidateBeforeCall(createRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateRecordingConfigurationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createStreamKey
     * @param createStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createStreamKeyCall(CreateStreamKeyRequest createStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = createStreamKeyRequest;

        // create path and map variables
        String localVarPath = "/CreateStreamKey";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call createStreamKeyValidateBeforeCall(CreateStreamKeyRequest createStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createStreamKeyRequest' is set
        if (createStreamKeyRequest == null) {
            throw new ApiException("Missing the required parameter 'createStreamKeyRequest' when calling createStreamKey(Async)");
        }

        return createStreamKeyCall(createStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Creates a stream key, used to initiate a stream, for the specified channel ARN.&lt;/p&gt; &lt;p&gt;Note that &lt;a&gt;CreateChannel&lt;/a&gt; creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use &lt;a&gt;DeleteStreamKey&lt;/a&gt; and then CreateStreamKey.&lt;/p&gt;
     * @param createStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateStreamKeyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public CreateStreamKeyResponse createStreamKey(CreateStreamKeyRequest createStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateStreamKeyResponse> localVarResp = createStreamKeyWithHttpInfo(createStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Creates a stream key, used to initiate a stream, for the specified channel ARN.&lt;/p&gt; &lt;p&gt;Note that &lt;a&gt;CreateChannel&lt;/a&gt; creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use &lt;a&gt;DeleteStreamKey&lt;/a&gt; and then CreateStreamKey.&lt;/p&gt;
     * @param createStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateStreamKeyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateStreamKeyResponse> createStreamKeyWithHttpInfo(CreateStreamKeyRequest createStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createStreamKeyValidateBeforeCall(createStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateStreamKeyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Creates a stream key, used to initiate a stream, for the specified channel ARN.&lt;/p&gt; &lt;p&gt;Note that &lt;a&gt;CreateChannel&lt;/a&gt; creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use &lt;a&gt;DeleteStreamKey&lt;/a&gt; and then CreateStreamKey.&lt;/p&gt;
     * @param createStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createStreamKeyAsync(CreateStreamKeyRequest createStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateStreamKeyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createStreamKeyValidateBeforeCall(createStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateStreamKeyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteChannel
     * @param deleteChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteChannelCall(DeleteChannelRequest deleteChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deleteChannelRequest;

        // create path and map variables
        String localVarPath = "/DeleteChannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteChannelValidateBeforeCall(DeleteChannelRequest deleteChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteChannelRequest' is set
        if (deleteChannelRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteChannelRequest' when calling deleteChannel(Async)");
        }

        return deleteChannelCall(deleteChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Deletes the specified channel and its associated stream keys.&lt;/p&gt; &lt;p&gt;If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call &lt;a&gt;StopStream&lt;/a&gt;, wait for the Amazon EventBridge \&quot;Stream End\&quot; event (to verify that the stream&#39;s state is no longer Live), then call DeleteChannel. (See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\&quot;&gt; Using EventBridge with Amazon IVS&lt;/a&gt;.) &lt;/p&gt;
     * @param deleteChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public void deleteChannel(DeleteChannelRequest deleteChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteChannelWithHttpInfo(deleteChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * &lt;p&gt;Deletes the specified channel and its associated stream keys.&lt;/p&gt; &lt;p&gt;If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call &lt;a&gt;StopStream&lt;/a&gt;, wait for the Amazon EventBridge \&quot;Stream End\&quot; event (to verify that the stream&#39;s state is no longer Live), then call DeleteChannel. (See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\&quot;&gt; Using EventBridge with Amazon IVS&lt;/a&gt;.) &lt;/p&gt;
     * @param deleteChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteChannelWithHttpInfo(DeleteChannelRequest deleteChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteChannelValidateBeforeCall(deleteChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Deletes the specified channel and its associated stream keys.&lt;/p&gt; &lt;p&gt;If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call &lt;a&gt;StopStream&lt;/a&gt;, wait for the Amazon EventBridge \&quot;Stream End\&quot; event (to verify that the stream&#39;s state is no longer Live), then call DeleteChannel. (See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\&quot;&gt; Using EventBridge with Amazon IVS&lt;/a&gt;.) &lt;/p&gt;
     * @param deleteChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteChannelAsync(DeleteChannelRequest deleteChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteChannelValidateBeforeCall(deleteChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deletePlaybackKeyPair
     * @param deletePlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePlaybackKeyPairCall(DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deletePlaybackKeyPairRequest;

        // create path and map variables
        String localVarPath = "/DeletePlaybackKeyPair";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deletePlaybackKeyPairValidateBeforeCall(DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deletePlaybackKeyPairRequest' is set
        if (deletePlaybackKeyPairRequest == null) {
            throw new ApiException("Missing the required parameter 'deletePlaybackKeyPairRequest' when calling deletePlaybackKeyPair(Async)");
        }

        return deletePlaybackKeyPairCall(deletePlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s &lt;code&gt;privateKey&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param deletePlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public Object deletePlaybackKeyPair(DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = deletePlaybackKeyPairWithHttpInfo(deletePlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s &lt;code&gt;privateKey&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param deletePlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> deletePlaybackKeyPairWithHttpInfo(DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deletePlaybackKeyPairValidateBeforeCall(deletePlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s &lt;code&gt;privateKey&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param deletePlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deletePlaybackKeyPairAsync(DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = deletePlaybackKeyPairValidateBeforeCall(deletePlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRecordingConfiguration
     * @param deleteRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRecordingConfigurationCall(DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deleteRecordingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/DeleteRecordingConfiguration";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteRecordingConfigurationValidateBeforeCall(DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteRecordingConfigurationRequest' is set
        if (deleteRecordingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteRecordingConfigurationRequest' when calling deleteRecordingConfiguration(Async)");
        }

        return deleteRecordingConfigurationCall(deleteRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Deletes the recording configuration for the specified ARN.&lt;/p&gt; &lt;p&gt;If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use &lt;a&gt;UpdateChannel&lt;/a&gt; to set the &lt;code&gt;recordingConfigurationArn&lt;/code&gt; field to an empty string, then use DeleteRecordingConfiguration.&lt;/p&gt;
     * @param deleteRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public void deleteRecordingConfiguration(DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteRecordingConfigurationWithHttpInfo(deleteRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * &lt;p&gt;Deletes the recording configuration for the specified ARN.&lt;/p&gt; &lt;p&gt;If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use &lt;a&gt;UpdateChannel&lt;/a&gt; to set the &lt;code&gt;recordingConfigurationArn&lt;/code&gt; field to an empty string, then use DeleteRecordingConfiguration.&lt;/p&gt;
     * @param deleteRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteRecordingConfigurationWithHttpInfo(DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteRecordingConfigurationValidateBeforeCall(deleteRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Deletes the recording configuration for the specified ARN.&lt;/p&gt; &lt;p&gt;If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use &lt;a&gt;UpdateChannel&lt;/a&gt; to set the &lt;code&gt;recordingConfigurationArn&lt;/code&gt; field to an empty string, then use DeleteRecordingConfiguration.&lt;/p&gt;
     * @param deleteRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRecordingConfigurationAsync(DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRecordingConfigurationValidateBeforeCall(deleteRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteStreamKey
     * @param deleteStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteStreamKeyCall(DeleteStreamKeyRequest deleteStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = deleteStreamKeyRequest;

        // create path and map variables
        String localVarPath = "/DeleteStreamKey";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call deleteStreamKeyValidateBeforeCall(DeleteStreamKeyRequest deleteStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteStreamKeyRequest' is set
        if (deleteStreamKeyRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteStreamKeyRequest' when calling deleteStreamKey(Async)");
        }

        return deleteStreamKeyCall(deleteStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes the stream key for the specified ARN, so it can no longer be used to stream.
     * @param deleteStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public void deleteStreamKey(DeleteStreamKeyRequest deleteStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteStreamKeyWithHttpInfo(deleteStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Deletes the stream key for the specified ARN, so it can no longer be used to stream.
     * @param deleteStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteStreamKeyWithHttpInfo(DeleteStreamKeyRequest deleteStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteStreamKeyValidateBeforeCall(deleteStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Deletes the stream key for the specified ARN, so it can no longer be used to stream.
     * @param deleteStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteStreamKeyAsync(DeleteStreamKeyRequest deleteStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteStreamKeyValidateBeforeCall(deleteStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for getChannel
     * @param getChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getChannelCall(GetChannelRequest getChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getChannelRequest;

        // create path and map variables
        String localVarPath = "/GetChannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getChannelValidateBeforeCall(GetChannelRequest getChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getChannelRequest' is set
        if (getChannelRequest == null) {
            throw new ApiException("Missing the required parameter 'getChannelRequest' when calling getChannel(Async)");
        }

        return getChannelCall(getChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets the channel configuration for the specified channel ARN. See also &lt;a&gt;BatchGetChannel&lt;/a&gt;.
     * @param getChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetChannelResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetChannelResponse getChannel(GetChannelRequest getChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetChannelResponse> localVarResp = getChannelWithHttpInfo(getChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the channel configuration for the specified channel ARN. See also &lt;a&gt;BatchGetChannel&lt;/a&gt;.
     * @param getChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetChannelResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetChannelResponse> getChannelWithHttpInfo(GetChannelRequest getChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getChannelValidateBeforeCall(getChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetChannelResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the channel configuration for the specified channel ARN. See also &lt;a&gt;BatchGetChannel&lt;/a&gt;.
     * @param getChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getChannelAsync(GetChannelRequest getChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetChannelResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getChannelValidateBeforeCall(getChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetChannelResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getPlaybackKeyPair
     * @param getPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaybackKeyPairCall(GetPlaybackKeyPairRequest getPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getPlaybackKeyPairRequest;

        // create path and map variables
        String localVarPath = "/GetPlaybackKeyPair";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getPlaybackKeyPairValidateBeforeCall(GetPlaybackKeyPairRequest getPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getPlaybackKeyPairRequest' is set
        if (getPlaybackKeyPairRequest == null) {
            throw new ApiException("Missing the required parameter 'getPlaybackKeyPairRequest' when calling getPlaybackKeyPair(Async)");
        }

        return getPlaybackKeyPairCall(getPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets a specified playback authorization key pair and returns the &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param getPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetPlaybackKeyPairResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetPlaybackKeyPairResponse getPlaybackKeyPair(GetPlaybackKeyPairRequest getPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetPlaybackKeyPairResponse> localVarResp = getPlaybackKeyPairWithHttpInfo(getPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a specified playback authorization key pair and returns the &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param getPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetPlaybackKeyPairResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetPlaybackKeyPairResponse> getPlaybackKeyPairWithHttpInfo(GetPlaybackKeyPairRequest getPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getPlaybackKeyPairValidateBeforeCall(getPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetPlaybackKeyPairResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a specified playback authorization key pair and returns the &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param getPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getPlaybackKeyPairAsync(GetPlaybackKeyPairRequest getPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetPlaybackKeyPairResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getPlaybackKeyPairValidateBeforeCall(getPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetPlaybackKeyPairResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRecordingConfiguration
     * @param getRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRecordingConfigurationCall(GetRecordingConfigurationRequest getRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getRecordingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/GetRecordingConfiguration";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getRecordingConfigurationValidateBeforeCall(GetRecordingConfigurationRequest getRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getRecordingConfigurationRequest' is set
        if (getRecordingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'getRecordingConfigurationRequest' when calling getRecordingConfiguration(Async)");
        }

        return getRecordingConfigurationCall(getRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets the recording configuration for the specified ARN.
     * @param getRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetRecordingConfigurationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetRecordingConfigurationResponse getRecordingConfiguration(GetRecordingConfigurationRequest getRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetRecordingConfigurationResponse> localVarResp = getRecordingConfigurationWithHttpInfo(getRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the recording configuration for the specified ARN.
     * @param getRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetRecordingConfigurationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRecordingConfigurationResponse> getRecordingConfigurationWithHttpInfo(GetRecordingConfigurationRequest getRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getRecordingConfigurationValidateBeforeCall(getRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetRecordingConfigurationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the recording configuration for the specified ARN.
     * @param getRecordingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRecordingConfigurationAsync(GetRecordingConfigurationRequest getRecordingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetRecordingConfigurationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRecordingConfigurationValidateBeforeCall(getRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetRecordingConfigurationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getStream
     * @param getStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamCall(GetStreamRequest getStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getStreamRequest;

        // create path and map variables
        String localVarPath = "/GetStream";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getStreamValidateBeforeCall(GetStreamRequest getStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getStreamRequest' is set
        if (getStreamRequest == null) {
            throw new ApiException("Missing the required parameter 'getStreamRequest' when calling getStream(Async)");
        }

        return getStreamCall(getStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets information about the active (live) stream on a specified channel.
     * @param getStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetStreamResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
     </table>
     */
    public GetStreamResponse getStream(GetStreamRequest getStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetStreamResponse> localVarResp = getStreamWithHttpInfo(getStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets information about the active (live) stream on a specified channel.
     * @param getStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetStreamResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetStreamResponse> getStreamWithHttpInfo(GetStreamRequest getStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getStreamValidateBeforeCall(getStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetStreamResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets information about the active (live) stream on a specified channel.
     * @param getStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamAsync(GetStreamRequest getStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetStreamResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getStreamValidateBeforeCall(getStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetStreamResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getStreamKey
     * @param getStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamKeyCall(GetStreamKeyRequest getStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getStreamKeyRequest;

        // create path and map variables
        String localVarPath = "/GetStreamKey";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getStreamKeyValidateBeforeCall(GetStreamKeyRequest getStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getStreamKeyRequest' is set
        if (getStreamKeyRequest == null) {
            throw new ApiException("Missing the required parameter 'getStreamKeyRequest' when calling getStreamKey(Async)");
        }

        return getStreamKeyCall(getStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets stream-key information for a specified ARN.
     * @param getStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetStreamKeyResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetStreamKeyResponse getStreamKey(GetStreamKeyRequest getStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetStreamKeyResponse> localVarResp = getStreamKeyWithHttpInfo(getStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets stream-key information for a specified ARN.
     * @param getStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetStreamKeyResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetStreamKeyResponse> getStreamKeyWithHttpInfo(GetStreamKeyRequest getStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getStreamKeyValidateBeforeCall(getStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetStreamKeyResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets stream-key information for a specified ARN.
     * @param getStreamKeyRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamKeyAsync(GetStreamKeyRequest getStreamKeyRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetStreamKeyResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getStreamKeyValidateBeforeCall(getStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetStreamKeyResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getStreamSession
     * @param getStreamSessionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamSessionCall(GetStreamSessionRequest getStreamSessionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getStreamSessionRequest;

        // create path and map variables
        String localVarPath = "/GetStreamSession";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getStreamSessionValidateBeforeCall(GetStreamSessionRequest getStreamSessionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getStreamSessionRequest' is set
        if (getStreamSessionRequest == null) {
            throw new ApiException("Missing the required parameter 'getStreamSessionRequest' when calling getStreamSession(Async)");
        }

        return getStreamSessionCall(getStreamSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets metadata on a specified stream.
     * @param getStreamSessionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetStreamSessionResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetStreamSessionResponse getStreamSession(GetStreamSessionRequest getStreamSessionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetStreamSessionResponse> localVarResp = getStreamSessionWithHttpInfo(getStreamSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets metadata on a specified stream.
     * @param getStreamSessionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetStreamSessionResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetStreamSessionResponse> getStreamSessionWithHttpInfo(GetStreamSessionRequest getStreamSessionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getStreamSessionValidateBeforeCall(getStreamSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetStreamSessionResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets metadata on a specified stream.
     * @param getStreamSessionRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getStreamSessionAsync(GetStreamSessionRequest getStreamSessionRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetStreamSessionResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getStreamSessionValidateBeforeCall(getStreamSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetStreamSessionResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for importPlaybackKeyPair
     * @param importPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importPlaybackKeyPairCall(ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = importPlaybackKeyPairRequest;

        // create path and map variables
        String localVarPath = "/ImportPlaybackKeyPair";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call importPlaybackKeyPairValidateBeforeCall(ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'importPlaybackKeyPairRequest' is set
        if (importPlaybackKeyPairRequest == null) {
            throw new ApiException("Missing the required parameter 'importPlaybackKeyPairRequest' when calling importPlaybackKeyPair(Async)");
        }

        return importPlaybackKeyPairCall(importPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Imports the public portion of a new key pair and returns its &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param importPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ImportPlaybackKeyPairResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ImportPlaybackKeyPairResponse importPlaybackKeyPair(ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<ImportPlaybackKeyPairResponse> localVarResp = importPlaybackKeyPairWithHttpInfo(importPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Imports the public portion of a new key pair and returns its &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param importPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;ImportPlaybackKeyPairResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ImportPlaybackKeyPairResponse> importPlaybackKeyPairWithHttpInfo(ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = importPlaybackKeyPairValidateBeforeCall(importPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<ImportPlaybackKeyPairResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Imports the public portion of a new key pair and returns its &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param importPlaybackKeyPairRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call importPlaybackKeyPairAsync(ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<ImportPlaybackKeyPairResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = importPlaybackKeyPairValidateBeforeCall(importPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<ImportPlaybackKeyPairResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listChannels
     * @param listChannelsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChannelsCall(ListChannelsRequest listChannelsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listChannelsRequest;

        // create path and map variables
        String localVarPath = "/ListChannels";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listChannelsValidateBeforeCall(ListChannelsRequest listChannelsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listChannelsRequest' is set
        if (listChannelsRequest == null) {
            throw new ApiException("Missing the required parameter 'listChannelsRequest' when calling listChannels(Async)");
        }

        return listChannelsCall(listChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).
     * @param listChannelsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListChannelsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ListChannelsResponse listChannels(ListChannelsRequest listChannelsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListChannelsResponse> localVarResp = listChannelsWithHttpInfo(listChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).
     * @param listChannelsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListChannelsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListChannelsResponse> listChannelsWithHttpInfo(ListChannelsRequest listChannelsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listChannelsValidateBeforeCall(listChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListChannelsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).
     * @param listChannelsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listChannelsAsync(ListChannelsRequest listChannelsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListChannelsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listChannelsValidateBeforeCall(listChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListChannelsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPlaybackKeyPairs
     * @param listPlaybackKeyPairsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPlaybackKeyPairsCall(ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listPlaybackKeyPairsRequest;

        // create path and map variables
        String localVarPath = "/ListPlaybackKeyPairs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPlaybackKeyPairsValidateBeforeCall(ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listPlaybackKeyPairsRequest' is set
        if (listPlaybackKeyPairsRequest == null) {
            throw new ApiException("Missing the required parameter 'listPlaybackKeyPairsRequest' when calling listPlaybackKeyPairs(Async)");
        }

        return listPlaybackKeyPairsCall(listPlaybackKeyPairsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about playback key pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param listPlaybackKeyPairsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListPlaybackKeyPairsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListPlaybackKeyPairsResponse listPlaybackKeyPairs(ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListPlaybackKeyPairsResponse> localVarResp = listPlaybackKeyPairsWithHttpInfo(listPlaybackKeyPairsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about playback key pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param listPlaybackKeyPairsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListPlaybackKeyPairsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListPlaybackKeyPairsResponse> listPlaybackKeyPairsWithHttpInfo(ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listPlaybackKeyPairsValidateBeforeCall(listPlaybackKeyPairsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListPlaybackKeyPairsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about playback key pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param listPlaybackKeyPairsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPlaybackKeyPairsAsync(ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListPlaybackKeyPairsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPlaybackKeyPairsValidateBeforeCall(listPlaybackKeyPairsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListPlaybackKeyPairsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRecordingConfigurations
     * @param listRecordingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRecordingConfigurationsCall(ListRecordingConfigurationsRequest listRecordingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listRecordingConfigurationsRequest;

        // create path and map variables
        String localVarPath = "/ListRecordingConfigurations";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listRecordingConfigurationsValidateBeforeCall(ListRecordingConfigurationsRequest listRecordingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listRecordingConfigurationsRequest' is set
        if (listRecordingConfigurationsRequest == null) {
            throw new ApiException("Missing the required parameter 'listRecordingConfigurationsRequest' when calling listRecordingConfigurations(Async)");
        }

        return listRecordingConfigurationsCall(listRecordingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.
     * @param listRecordingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListRecordingConfigurationsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListRecordingConfigurationsResponse listRecordingConfigurations(ListRecordingConfigurationsRequest listRecordingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListRecordingConfigurationsResponse> localVarResp = listRecordingConfigurationsWithHttpInfo(listRecordingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.
     * @param listRecordingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListRecordingConfigurationsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRecordingConfigurationsResponse> listRecordingConfigurationsWithHttpInfo(ListRecordingConfigurationsRequest listRecordingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listRecordingConfigurationsValidateBeforeCall(listRecordingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListRecordingConfigurationsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.
     * @param listRecordingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRecordingConfigurationsAsync(ListRecordingConfigurationsRequest listRecordingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListRecordingConfigurationsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRecordingConfigurationsValidateBeforeCall(listRecordingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListRecordingConfigurationsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listStreamKeys
     * @param listStreamKeysRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamKeysCall(ListStreamKeysRequest listStreamKeysRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listStreamKeysRequest;

        // create path and map variables
        String localVarPath = "/ListStreamKeys";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listStreamKeysValidateBeforeCall(ListStreamKeysRequest listStreamKeysRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listStreamKeysRequest' is set
        if (listStreamKeysRequest == null) {
            throw new ApiException("Missing the required parameter 'listStreamKeysRequest' when calling listStreamKeys(Async)");
        }

        return listStreamKeysCall(listStreamKeysRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about stream keys for the specified channel.
     * @param listStreamKeysRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListStreamKeysResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListStreamKeysResponse listStreamKeys(ListStreamKeysRequest listStreamKeysRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListStreamKeysResponse> localVarResp = listStreamKeysWithHttpInfo(listStreamKeysRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about stream keys for the specified channel.
     * @param listStreamKeysRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListStreamKeysResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListStreamKeysResponse> listStreamKeysWithHttpInfo(ListStreamKeysRequest listStreamKeysRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listStreamKeysValidateBeforeCall(listStreamKeysRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListStreamKeysResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about stream keys for the specified channel.
     * @param listStreamKeysRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamKeysAsync(ListStreamKeysRequest listStreamKeysRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListStreamKeysResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listStreamKeysValidateBeforeCall(listStreamKeysRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListStreamKeysResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listStreamSessions
     * @param listStreamSessionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamSessionsCall(ListStreamSessionsRequest listStreamSessionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listStreamSessionsRequest;

        // create path and map variables
        String localVarPath = "/ListStreamSessions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listStreamSessionsValidateBeforeCall(ListStreamSessionsRequest listStreamSessionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listStreamSessionsRequest' is set
        if (listStreamSessionsRequest == null) {
            throw new ApiException("Missing the required parameter 'listStreamSessionsRequest' when calling listStreamSessions(Async)");
        }

        return listStreamSessionsCall(listStreamSessionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
     * @param listStreamSessionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListStreamSessionsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListStreamSessionsResponse listStreamSessions(ListStreamSessionsRequest listStreamSessionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListStreamSessionsResponse> localVarResp = listStreamSessionsWithHttpInfo(listStreamSessionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
     * @param listStreamSessionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListStreamSessionsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListStreamSessionsResponse> listStreamSessionsWithHttpInfo(ListStreamSessionsRequest listStreamSessionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listStreamSessionsValidateBeforeCall(listStreamSessionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListStreamSessionsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
     * @param listStreamSessionsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamSessionsAsync(ListStreamSessionsRequest listStreamSessionsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListStreamSessionsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listStreamSessionsValidateBeforeCall(listStreamSessionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListStreamSessionsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listStreams
     * @param listStreamsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamsCall(ListStreamsRequest listStreamsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = listStreamsRequest;

        // create path and map variables
        String localVarPath = "/ListStreams";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (maxResults != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("maxResults", maxResults));
        }

        if (nextToken != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("nextToken", nextToken));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listStreamsValidateBeforeCall(ListStreamsRequest listStreamsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listStreamsRequest' is set
        if (listStreamsRequest == null) {
            throw new ApiException("Missing the required parameter 'listStreamsRequest' when calling listStreams(Async)");
        }

        return listStreamsCall(listStreamsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.
     * @param listStreamsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListStreamsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListStreamsResponse listStreams(ListStreamsRequest listStreamsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListStreamsResponse> localVarResp = listStreamsWithHttpInfo(listStreamsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.
     * @param listStreamsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListStreamsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListStreamsResponse> listStreamsWithHttpInfo(ListStreamsRequest listStreamsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listStreamsValidateBeforeCall(listStreamsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListStreamsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.
     * @param listStreamsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listStreamsAsync(ListStreamsRequest listStreamsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListStreamsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listStreamsValidateBeforeCall(listStreamsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListStreamsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listTagsForResource
     * @param resourceArn The ARN of the resource to be retrieved. The ARN must be URL-encoded. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/tags/{resourceArn}"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listTagsForResourceValidateBeforeCall(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling listTagsForResource(Async)");
        }

        return listTagsForResourceCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets information about Amazon Web Services tags for the specified ARN.
     * @param resourceArn The ARN of the resource to be retrieved. The ARN must be URL-encoded. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ListTagsForResourceResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListTagsForResourceResponse listTagsForResource(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<ListTagsForResourceResponse> localVarResp = listTagsForResourceWithHttpInfo(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets information about Amazon Web Services tags for the specified ARN.
     * @param resourceArn The ARN of the resource to be retrieved. The ARN must be URL-encoded. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;ListTagsForResourceResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListTagsForResourceResponse> listTagsForResourceWithHttpInfo(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets information about Amazon Web Services tags for the specified ARN.
     * @param resourceArn The ARN of the resource to be retrieved. The ARN must be URL-encoded. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listTagsForResourceAsync(String resourceArn, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<ListTagsForResourceResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listTagsForResourceValidateBeforeCall(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<ListTagsForResourceResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for putMetadata
     * @param putMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putMetadataCall(PutMetadataRequest putMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = putMetadataRequest;

        // create path and map variables
        String localVarPath = "/PutMetadata";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call putMetadataValidateBeforeCall(PutMetadataRequest putMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'putMetadataRequest' is set
        if (putMetadataRequest == null) {
            throw new ApiException("Missing the required parameter 'putMetadataRequest' when calling putMetadata(Async)");
        }

        return putMetadataCall(putMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\&quot;&gt;Embedding Metadata within a Video Stream&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param putMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public void putMetadata(PutMetadataRequest putMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        putMetadataWithHttpInfo(putMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\&quot;&gt;Embedding Metadata within a Video Stream&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param putMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> putMetadataWithHttpInfo(PutMetadataRequest putMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = putMetadataValidateBeforeCall(putMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\&quot;&gt;Embedding Metadata within a Video Stream&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     * @param putMetadataRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call putMetadataAsync(PutMetadataRequest putMetadataRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = putMetadataValidateBeforeCall(putMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for startViewerSessionRevocation
     * @param startViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startViewerSessionRevocationCall(StartViewerSessionRevocationRequest startViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = startViewerSessionRevocationRequest;

        // create path and map variables
        String localVarPath = "/StartViewerSessionRevocation";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call startViewerSessionRevocationValidateBeforeCall(StartViewerSessionRevocationRequest startViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'startViewerSessionRevocationRequest' is set
        if (startViewerSessionRevocationRequest == null) {
            throw new ApiException("Missing the required parameter 'startViewerSessionRevocationRequest' when calling startViewerSessionRevocation(Async)");
        }

        return startViewerSessionRevocationCall(startViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt;.
     * @param startViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public Object startViewerSessionRevocation(StartViewerSessionRevocationRequest startViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = startViewerSessionRevocationWithHttpInfo(startViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt;.
     * @param startViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> startViewerSessionRevocationWithHttpInfo(StartViewerSessionRevocationRequest startViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = startViewerSessionRevocationValidateBeforeCall(startViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt;.
     * @param startViewerSessionRevocationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ThrottlingException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call startViewerSessionRevocationAsync(StartViewerSessionRevocationRequest startViewerSessionRevocationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = startViewerSessionRevocationValidateBeforeCall(startViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for stopStream
     * @param stopStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StreamUnavailable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call stopStreamCall(StopStreamRequest stopStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = stopStreamRequest;

        // create path and map variables
        String localVarPath = "/StopStream";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call stopStreamValidateBeforeCall(StopStreamRequest stopStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'stopStreamRequest' is set
        if (stopStreamRequest == null) {
            throw new ApiException("Missing the required parameter 'stopStreamRequest' when calling stopStream(Async)");
        }

        return stopStreamCall(stopStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with &lt;a&gt;DeleteStreamKey&lt;/a&gt; to prevent further streaming to a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the &lt;code&gt;streamKey&lt;/code&gt; attached to the channel.&lt;/p&gt; &lt;/note&gt;
     * @param stopStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StreamUnavailable </td><td>  -  </td></tr>
     </table>
     */
    public Object stopStream(StopStreamRequest stopStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = stopStreamWithHttpInfo(stopStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with &lt;a&gt;DeleteStreamKey&lt;/a&gt; to prevent further streaming to a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the &lt;code&gt;streamKey&lt;/code&gt; attached to the channel.&lt;/p&gt; &lt;/note&gt;
     * @param stopStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StreamUnavailable </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> stopStreamWithHttpInfo(StopStreamRequest stopStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = stopStreamValidateBeforeCall(stopStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with &lt;a&gt;DeleteStreamKey&lt;/a&gt; to prevent further streaming to a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the &lt;code&gt;streamKey&lt;/code&gt; attached to the channel.&lt;/p&gt; &lt;/note&gt;
     * @param stopStreamRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ChannelNotBroadcasting </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> StreamUnavailable </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call stopStreamAsync(StopStreamRequest stopStreamRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = stopStreamValidateBeforeCall(stopStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for tagResource
     * @param resourceArn ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = tagResourceRequest;

        // create path and map variables
        String localVarPath = "/tags/{resourceArn}"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call tagResourceValidateBeforeCall(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling tagResource(Async)");
        }

        // verify the required parameter 'tagResourceRequest' is set
        if (tagResourceRequest == null) {
            throw new ApiException("Missing the required parameter 'tagResourceRequest' when calling tagResource(Async)");
        }

        return tagResourceCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Adds or updates tags for the Amazon Web Services resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public Object tagResource(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = tagResourceWithHttpInfo(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Adds or updates tags for the Amazon Web Services resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> tagResourceWithHttpInfo(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Adds or updates tags for the Amazon Web Services resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded. (required)
     * @param tagResourceRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call tagResourceAsync(String resourceArn, TagResourceRequest tagResourceRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = tagResourceValidateBeforeCall(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for untagResource
     * @param resourceArn ARN of the resource for which tags are to be removed. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form s&lt;code&gt;tring:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceCall(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/tags/{resourceArn}#tagKeys"
            .replace("{" + "resourceArn" + "}", localVarApiClient.escapeString(resourceArn.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (tagKeys != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "tagKeys", tagKeys));
        }

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call untagResourceValidateBeforeCall(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'resourceArn' is set
        if (resourceArn == null) {
            throw new ApiException("Missing the required parameter 'resourceArn' when calling untagResource(Async)");
        }

        // verify the required parameter 'tagKeys' is set
        if (tagKeys == null) {
            throw new ApiException("Missing the required parameter 'tagKeys' when calling untagResource(Async)");
        }

        return untagResourceCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Removes tags from the resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be removed. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form s&lt;code&gt;tring:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public Object untagResource(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = untagResourceWithHttpInfo(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Removes tags from the resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be removed. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form s&lt;code&gt;tring:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> untagResourceWithHttpInfo(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Removes tags from the resource with the specified ARN.
     * @param resourceArn ARN of the resource for which tags are to be removed. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form s&lt;code&gt;tring:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there. (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> InternalServerException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call untagResourceAsync(String resourceArn, List<String> tagKeys, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = untagResourceValidateBeforeCall(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateChannel
     * @param updateChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateChannelCall(UpdateChannelRequest updateChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = updateChannelRequest;

        // create path and map variables
        String localVarPath = "/UpdateChannel";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (xAmzContentSha256 != null) {
            localVarHeaderParams.put("X-Amz-Content-Sha256", localVarApiClient.parameterToString(xAmzContentSha256));
        }

        if (xAmzDate != null) {
            localVarHeaderParams.put("X-Amz-Date", localVarApiClient.parameterToString(xAmzDate));
        }

        if (xAmzAlgorithm != null) {
            localVarHeaderParams.put("X-Amz-Algorithm", localVarApiClient.parameterToString(xAmzAlgorithm));
        }

        if (xAmzCredential != null) {
            localVarHeaderParams.put("X-Amz-Credential", localVarApiClient.parameterToString(xAmzCredential));
        }

        if (xAmzSecurityToken != null) {
            localVarHeaderParams.put("X-Amz-Security-Token", localVarApiClient.parameterToString(xAmzSecurityToken));
        }

        if (xAmzSignature != null) {
            localVarHeaderParams.put("X-Amz-Signature", localVarApiClient.parameterToString(xAmzSignature));
        }

        if (xAmzSignedHeaders != null) {
            localVarHeaderParams.put("X-Amz-SignedHeaders", localVarApiClient.parameterToString(xAmzSignedHeaders));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "hmac" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call updateChannelValidateBeforeCall(UpdateChannelRequest updateChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'updateChannelRequest' is set
        if (updateChannelRequest == null) {
            throw new ApiException("Missing the required parameter 'updateChannelRequest' when calling updateChannel(Async)");
        }

        return updateChannelCall(updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Updates a channel&#39;s configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.
     * @param updateChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return UpdateChannelResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public UpdateChannelResponse updateChannel(UpdateChannelRequest updateChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<UpdateChannelResponse> localVarResp = updateChannelWithHttpInfo(updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a channel&#39;s configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.
     * @param updateChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;UpdateChannelResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateChannelResponse> updateChannelWithHttpInfo(UpdateChannelRequest updateChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updateChannelValidateBeforeCall(updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<UpdateChannelResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a channel&#39;s configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.
     * @param updateChannelRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ConflictException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateChannelAsync(UpdateChannelRequest updateChannelRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<UpdateChannelResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateChannelValidateBeforeCall(updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<UpdateChannelResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
