/*
 * Amazon Interactive Video Service Chat
 * <p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>
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


import org.openapitools.client.model.CreateChatTokenRequest;
import org.openapitools.client.model.CreateChatTokenResponse;
import org.openapitools.client.model.CreateLoggingConfigurationRequest;
import org.openapitools.client.model.CreateLoggingConfigurationResponse;
import org.openapitools.client.model.CreateRoomRequest;
import org.openapitools.client.model.CreateRoomResponse;
import org.openapitools.client.model.DeleteLoggingConfigurationRequest;
import org.openapitools.client.model.DeleteMessageRequest;
import org.openapitools.client.model.DeleteMessageResponse;
import org.openapitools.client.model.DeleteRoomRequest;
import org.openapitools.client.model.DisconnectUserRequest;
import org.openapitools.client.model.GetLoggingConfigurationRequest;
import org.openapitools.client.model.GetLoggingConfigurationResponse;
import org.openapitools.client.model.GetRoomRequest;
import org.openapitools.client.model.GetRoomResponse;
import org.openapitools.client.model.ListLoggingConfigurationsRequest;
import org.openapitools.client.model.ListLoggingConfigurationsResponse;
import org.openapitools.client.model.ListRoomsRequest;
import org.openapitools.client.model.ListRoomsResponse;
import org.openapitools.client.model.ListTagsForResourceResponse;
import org.openapitools.client.model.SendEventRequest;
import org.openapitools.client.model.SendEventResponse;
import org.openapitools.client.model.TagResourceRequest;
import org.openapitools.client.model.UpdateLoggingConfigurationRequest;
import org.openapitools.client.model.UpdateLoggingConfigurationResponse;
import org.openapitools.client.model.UpdateRoomRequest;
import org.openapitools.client.model.UpdateRoomResponse;

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
     * Build call for createChatToken
     * @param createChatTokenRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createChatTokenCall(CreateChatTokenRequest createChatTokenRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createChatTokenRequest;

        // create path and map variables
        String localVarPath = "/CreateChatToken";

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
    private okhttp3.Call createChatTokenValidateBeforeCall(CreateChatTokenRequest createChatTokenRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createChatTokenRequest' is set
        if (createChatTokenRequest == null) {
            throw new ApiException("Missing the required parameter 'createChatTokenRequest' when calling createChatToken(Async)");
        }

        return createChatTokenCall(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * &lt;p&gt;Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;capabilities&lt;/code&gt; field to permit an end user to send messages or moderate a room.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;attributes&lt;/code&gt; field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.&lt;/p&gt; &lt;p&gt;Encryption keys are owned by Amazon IVS Chat and never used directly by your application.&lt;/p&gt;
     * @param createChatTokenRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateChatTokenResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateChatTokenResponse createChatToken(CreateChatTokenRequest createChatTokenRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateChatTokenResponse> localVarResp = createChatTokenWithHttpInfo(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * &lt;p&gt;Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;capabilities&lt;/code&gt; field to permit an end user to send messages or moderate a room.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;attributes&lt;/code&gt; field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.&lt;/p&gt; &lt;p&gt;Encryption keys are owned by Amazon IVS Chat and never used directly by your application.&lt;/p&gt;
     * @param createChatTokenRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateChatTokenResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateChatTokenResponse> createChatTokenWithHttpInfo(CreateChatTokenRequest createChatTokenRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createChatTokenValidateBeforeCall(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateChatTokenResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * &lt;p&gt;Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;capabilities&lt;/code&gt; field to permit an end user to send messages or moderate a room.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;attributes&lt;/code&gt; field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.&lt;/p&gt; &lt;p&gt;Encryption keys are owned by Amazon IVS Chat and never used directly by your application.&lt;/p&gt;
     * @param createChatTokenRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createChatTokenAsync(CreateChatTokenRequest createChatTokenRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateChatTokenResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createChatTokenValidateBeforeCall(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateChatTokenResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createLoggingConfiguration
     * @param createLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLoggingConfigurationCall(CreateLoggingConfigurationRequest createLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createLoggingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/CreateLoggingConfiguration";

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
    private okhttp3.Call createLoggingConfigurationValidateBeforeCall(CreateLoggingConfigurationRequest createLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createLoggingConfigurationRequest' is set
        if (createLoggingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'createLoggingConfigurationRequest' when calling createLoggingConfiguration(Async)");
        }

        return createLoggingConfigurationCall(createLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Creates a logging configuration that allows clients to store and record sent messages.
     * @param createLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateLoggingConfigurationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateLoggingConfigurationResponse createLoggingConfiguration(CreateLoggingConfigurationRequest createLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateLoggingConfigurationResponse> localVarResp = createLoggingConfigurationWithHttpInfo(createLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Creates a logging configuration that allows clients to store and record sent messages.
     * @param createLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateLoggingConfigurationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateLoggingConfigurationResponse> createLoggingConfigurationWithHttpInfo(CreateLoggingConfigurationRequest createLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createLoggingConfigurationValidateBeforeCall(createLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateLoggingConfigurationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Creates a logging configuration that allows clients to store and record sent messages.
     * @param createLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createLoggingConfigurationAsync(CreateLoggingConfigurationRequest createLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateLoggingConfigurationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createLoggingConfigurationValidateBeforeCall(createLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateLoggingConfigurationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for createRoom
     * @param createRoomRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRoomCall(CreateRoomRequest createRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = createRoomRequest;

        // create path and map variables
        String localVarPath = "/CreateRoom";

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
    private okhttp3.Call createRoomValidateBeforeCall(CreateRoomRequest createRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'createRoomRequest' is set
        if (createRoomRequest == null) {
            throw new ApiException("Missing the required parameter 'createRoomRequest' when calling createRoom(Async)");
        }

        return createRoomCall(createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Creates a room that allows clients to connect and pass messages.
     * @param createRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return CreateRoomResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public CreateRoomResponse createRoom(CreateRoomRequest createRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<CreateRoomResponse> localVarResp = createRoomWithHttpInfo(createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Creates a room that allows clients to connect and pass messages.
     * @param createRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;CreateRoomResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CreateRoomResponse> createRoomWithHttpInfo(CreateRoomRequest createRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = createRoomValidateBeforeCall(createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<CreateRoomResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Creates a room that allows clients to connect and pass messages.
     * @param createRoomRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ServiceQuotaExceededException </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 485 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call createRoomAsync(CreateRoomRequest createRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<CreateRoomResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = createRoomValidateBeforeCall(createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<CreateRoomResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteLoggingConfiguration
     * @param deleteLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLoggingConfigurationCall(DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = deleteLoggingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/DeleteLoggingConfiguration";

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
    private okhttp3.Call deleteLoggingConfigurationValidateBeforeCall(DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteLoggingConfigurationRequest' is set
        if (deleteLoggingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteLoggingConfigurationRequest' when calling deleteLoggingConfiguration(Async)");
        }

        return deleteLoggingConfigurationCall(deleteLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes the specified logging configuration.
     * @param deleteLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public void deleteLoggingConfiguration(DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteLoggingConfigurationWithHttpInfo(deleteLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Deletes the specified logging configuration.
     * @param deleteLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteLoggingConfigurationWithHttpInfo(DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteLoggingConfigurationValidateBeforeCall(deleteLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Deletes the specified logging configuration.
     * @param deleteLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteLoggingConfigurationAsync(DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteLoggingConfigurationValidateBeforeCall(deleteLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteMessage
     * @param deleteMessageRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteMessageCall(DeleteMessageRequest deleteMessageRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = deleteMessageRequest;

        // create path and map variables
        String localVarPath = "/DeleteMessage";

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
    private okhttp3.Call deleteMessageValidateBeforeCall(DeleteMessageRequest deleteMessageRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteMessageRequest' is set
        if (deleteMessageRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteMessageRequest' when calling deleteMessage(Async)");
        }

        return deleteMessageCall(deleteMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s &lt;code&gt;EventName&lt;/code&gt; is &lt;code&gt;aws:DELETE_MESSAGE&lt;/code&gt;. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\&quot;&gt; DeleteMessage&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param deleteMessageRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return DeleteMessageResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public DeleteMessageResponse deleteMessage(DeleteMessageRequest deleteMessageRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<DeleteMessageResponse> localVarResp = deleteMessageWithHttpInfo(deleteMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s &lt;code&gt;EventName&lt;/code&gt; is &lt;code&gt;aws:DELETE_MESSAGE&lt;/code&gt;. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\&quot;&gt; DeleteMessage&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param deleteMessageRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;DeleteMessageResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<DeleteMessageResponse> deleteMessageWithHttpInfo(DeleteMessageRequest deleteMessageRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteMessageValidateBeforeCall(deleteMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<DeleteMessageResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s &lt;code&gt;EventName&lt;/code&gt; is &lt;code&gt;aws:DELETE_MESSAGE&lt;/code&gt;. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\&quot;&gt; DeleteMessage&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param deleteMessageRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteMessageAsync(DeleteMessageRequest deleteMessageRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<DeleteMessageResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteMessageValidateBeforeCall(deleteMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<DeleteMessageResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for deleteRoom
     * @param deleteRoomRequest  (required)
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
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRoomCall(DeleteRoomRequest deleteRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = deleteRoomRequest;

        // create path and map variables
        String localVarPath = "/DeleteRoom";

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
    private okhttp3.Call deleteRoomValidateBeforeCall(DeleteRoomRequest deleteRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'deleteRoomRequest' is set
        if (deleteRoomRequest == null) {
            throw new ApiException("Missing the required parameter 'deleteRoomRequest' when calling deleteRoom(Async)");
        }

        return deleteRoomCall(deleteRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Deletes the specified room.
     * @param deleteRoomRequest  (required)
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
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public void deleteRoom(DeleteRoomRequest deleteRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        deleteRoomWithHttpInfo(deleteRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    }

    /**
     * 
     * Deletes the specified room.
     * @param deleteRoomRequest  (required)
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
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> deleteRoomWithHttpInfo(DeleteRoomRequest deleteRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = deleteRoomValidateBeforeCall(deleteRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Deletes the specified room.
     * @param deleteRoomRequest  (required)
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
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call deleteRoomAsync(DeleteRoomRequest deleteRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = deleteRoomValidateBeforeCall(deleteRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for disconnectUser
     * @param disconnectUserRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disconnectUserCall(DisconnectUserRequest disconnectUserRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = disconnectUserRequest;

        // create path and map variables
        String localVarPath = "/DisconnectUser";

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
    private okhttp3.Call disconnectUserValidateBeforeCall(DisconnectUserRequest disconnectUserRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'disconnectUserRequest' is set
        if (disconnectUserRequest == null) {
            throw new ApiException("Missing the required parameter 'disconnectUserRequest' when calling disconnectUser(Async)");
        }

        return disconnectUserCall(disconnectUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Disconnects all connections using a specified user ID from a room. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\&quot;&gt; DisconnectUser&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param disconnectUserRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public Object disconnectUser(DisconnectUserRequest disconnectUserRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<Object> localVarResp = disconnectUserWithHttpInfo(disconnectUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Disconnects all connections using a specified user ID from a room. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\&quot;&gt; DisconnectUser&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param disconnectUserRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> disconnectUserWithHttpInfo(DisconnectUserRequest disconnectUserRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = disconnectUserValidateBeforeCall(disconnectUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Disconnects all connections using a specified user ID from a room. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\&quot;&gt; DisconnectUser&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param disconnectUserRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call disconnectUserAsync(DisconnectUserRequest disconnectUserRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = disconnectUserValidateBeforeCall(disconnectUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getLoggingConfiguration
     * @param getLoggingConfigurationRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLoggingConfigurationCall(GetLoggingConfigurationRequest getLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = getLoggingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/GetLoggingConfiguration";

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
    private okhttp3.Call getLoggingConfigurationValidateBeforeCall(GetLoggingConfigurationRequest getLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getLoggingConfigurationRequest' is set
        if (getLoggingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'getLoggingConfigurationRequest' when calling getLoggingConfiguration(Async)");
        }

        return getLoggingConfigurationCall(getLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets the specified logging configuration.
     * @param getLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetLoggingConfigurationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetLoggingConfigurationResponse getLoggingConfiguration(GetLoggingConfigurationRequest getLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetLoggingConfigurationResponse> localVarResp = getLoggingConfigurationWithHttpInfo(getLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the specified logging configuration.
     * @param getLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetLoggingConfigurationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetLoggingConfigurationResponse> getLoggingConfigurationWithHttpInfo(GetLoggingConfigurationRequest getLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getLoggingConfigurationValidateBeforeCall(getLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetLoggingConfigurationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the specified logging configuration.
     * @param getLoggingConfigurationRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getLoggingConfigurationAsync(GetLoggingConfigurationRequest getLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetLoggingConfigurationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getLoggingConfigurationValidateBeforeCall(getLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetLoggingConfigurationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for getRoom
     * @param getRoomRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRoomCall(GetRoomRequest getRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = getRoomRequest;

        // create path and map variables
        String localVarPath = "/GetRoom";

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
    private okhttp3.Call getRoomValidateBeforeCall(GetRoomRequest getRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'getRoomRequest' is set
        if (getRoomRequest == null) {
            throw new ApiException("Missing the required parameter 'getRoomRequest' when calling getRoom(Async)");
        }

        return getRoomCall(getRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Gets the specified room.
     * @param getRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return GetRoomResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public GetRoomResponse getRoom(GetRoomRequest getRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<GetRoomResponse> localVarResp = getRoomWithHttpInfo(getRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets the specified room.
     * @param getRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;GetRoomResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<GetRoomResponse> getRoomWithHttpInfo(GetRoomRequest getRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = getRoomValidateBeforeCall(getRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<GetRoomResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets the specified room.
     * @param getRoomRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getRoomAsync(GetRoomRequest getRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<GetRoomResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = getRoomValidateBeforeCall(getRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<GetRoomResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listLoggingConfigurations
     * @param listLoggingConfigurationsRequest  (required)
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
    public okhttp3.Call listLoggingConfigurationsCall(ListLoggingConfigurationsRequest listLoggingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listLoggingConfigurationsRequest;

        // create path and map variables
        String localVarPath = "/ListLoggingConfigurations";

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
    private okhttp3.Call listLoggingConfigurationsValidateBeforeCall(ListLoggingConfigurationsRequest listLoggingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listLoggingConfigurationsRequest' is set
        if (listLoggingConfigurationsRequest == null) {
            throw new ApiException("Missing the required parameter 'listLoggingConfigurationsRequest' when calling listLoggingConfigurations(Async)");
        }

        return listLoggingConfigurationsCall(listLoggingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about all your logging configurations in the AWS region where the API request is processed.
     * @param listLoggingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListLoggingConfigurationsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListLoggingConfigurationsResponse listLoggingConfigurations(ListLoggingConfigurationsRequest listLoggingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListLoggingConfigurationsResponse> localVarResp = listLoggingConfigurationsWithHttpInfo(listLoggingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about all your logging configurations in the AWS region where the API request is processed.
     * @param listLoggingConfigurationsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListLoggingConfigurationsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListLoggingConfigurationsResponse> listLoggingConfigurationsWithHttpInfo(ListLoggingConfigurationsRequest listLoggingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listLoggingConfigurationsValidateBeforeCall(listLoggingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListLoggingConfigurationsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about all your logging configurations in the AWS region where the API request is processed.
     * @param listLoggingConfigurationsRequest  (required)
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
    public okhttp3.Call listLoggingConfigurationsAsync(ListLoggingConfigurationsRequest listLoggingConfigurationsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListLoggingConfigurationsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listLoggingConfigurationsValidateBeforeCall(listLoggingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListLoggingConfigurationsResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for listRooms
     * @param listRoomsRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRoomsCall(ListRoomsRequest listRoomsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = listRoomsRequest;

        // create path and map variables
        String localVarPath = "/ListRooms";

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
    private okhttp3.Call listRoomsValidateBeforeCall(ListRoomsRequest listRoomsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'listRoomsRequest' is set
        if (listRoomsRequest == null) {
            throw new ApiException("Missing the required parameter 'listRoomsRequest' when calling listRooms(Async)");
        }

        return listRoomsCall(listRoomsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);

    }

    /**
     * 
     * Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of &lt;code&gt;updateTime&lt;/code&gt;.
     * @param listRoomsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ListRoomsResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ListRoomsResponse listRooms(ListRoomsRequest listRoomsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        ApiResponse<ListRoomsResponse> localVarResp = listRoomsWithHttpInfo(listRoomsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        return localVarResp.getData();
    }

    /**
     * 
     * Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of &lt;code&gt;updateTime&lt;/code&gt;.
     * @param listRoomsRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @param maxResults Pagination limit (optional)
     * @param nextToken Pagination token (optional)
     * @return ApiResponse&lt;ListRoomsResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<ListRoomsResponse> listRoomsWithHttpInfo(ListRoomsRequest listRoomsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken) throws ApiException {
        okhttp3.Call localVarCall = listRoomsValidateBeforeCall(listRoomsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, null);
        Type localVarReturnType = new TypeToken<ListRoomsResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of &lt;code&gt;updateTime&lt;/code&gt;.
     * @param listRoomsRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listRoomsAsync(ListRoomsRequest listRoomsRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, String maxResults, String nextToken, final ApiCallback<ListRoomsResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = listRoomsValidateBeforeCall(listRoomsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, _callback);
        Type localVarReturnType = new TypeToken<ListRoomsResponse>(){}.getType();
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
     * Gets information about AWS tags for the specified ARN.
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
     * Gets information about AWS tags for the specified ARN.
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
     * Gets information about AWS tags for the specified ARN.
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
     * Build call for sendEvent
     * @param sendEventRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendEventCall(SendEventRequest sendEventRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = sendEventRequest;

        // create path and map variables
        String localVarPath = "/SendEvent";

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
    private okhttp3.Call sendEventValidateBeforeCall(SendEventRequest sendEventRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'sendEventRequest' is set
        if (sendEventRequest == null) {
            throw new ApiException("Missing the required parameter 'sendEventRequest' when calling sendEvent(Async)");
        }

        return sendEventCall(sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.
     * @param sendEventRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return SendEventResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public SendEventResponse sendEvent(SendEventRequest sendEventRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<SendEventResponse> localVarResp = sendEventWithHttpInfo(sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.
     * @param sendEventRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;SendEventResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<SendEventResponse> sendEventWithHttpInfo(SendEventRequest sendEventRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = sendEventValidateBeforeCall(sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<SendEventResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.
     * @param sendEventRequest  (required)
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
        <tr><td> 480 </td><td> ThrottlingException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call sendEventAsync(SendEventRequest sendEventRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<SendEventResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = sendEventValidateBeforeCall(sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<SendEventResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for tagResource
     * @param resourceArn The ARN of the resource to be tagged. The ARN must be URL-encoded. (required)
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
     * Adds or updates tags for the AWS resource with the specified ARN.
     * @param resourceArn The ARN of the resource to be tagged. The ARN must be URL-encoded. (required)
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
     * Adds or updates tags for the AWS resource with the specified ARN.
     * @param resourceArn The ARN of the resource to be tagged. The ARN must be URL-encoded. (required)
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
     * Adds or updates tags for the AWS resource with the specified ARN.
     * @param resourceArn The ARN of the resource to be tagged. The ARN must be URL-encoded. (required)
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
     * @param resourceArn The ARN of the resource to be untagged. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for details, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no constraints beyond what is documented there. (required)
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
     * @param resourceArn The ARN of the resource to be untagged. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for details, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no constraints beyond what is documented there. (required)
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
     * @param resourceArn The ARN of the resource to be untagged. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for details, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no constraints beyond what is documented there. (required)
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
     * @param resourceArn The ARN of the resource to be untagged. The ARN must be URL-encoded. (required)
     * @param tagKeys Array of tags to be removed. Array of maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for details, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no constraints beyond what is documented there. (required)
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
     * Build call for updateLoggingConfiguration
     * @param updateLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLoggingConfigurationCall(UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateLoggingConfigurationRequest;

        // create path and map variables
        String localVarPath = "/UpdateLoggingConfiguration";

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
    private okhttp3.Call updateLoggingConfigurationValidateBeforeCall(UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'updateLoggingConfigurationRequest' is set
        if (updateLoggingConfigurationRequest == null) {
            throw new ApiException("Missing the required parameter 'updateLoggingConfigurationRequest' when calling updateLoggingConfiguration(Async)");
        }

        return updateLoggingConfigurationCall(updateLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Updates a specified logging configuration.
     * @param updateLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return UpdateLoggingConfigurationResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public UpdateLoggingConfigurationResponse updateLoggingConfiguration(UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<UpdateLoggingConfigurationResponse> localVarResp = updateLoggingConfigurationWithHttpInfo(updateLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a specified logging configuration.
     * @param updateLoggingConfigurationRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;UpdateLoggingConfigurationResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateLoggingConfigurationResponse> updateLoggingConfigurationWithHttpInfo(UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updateLoggingConfigurationValidateBeforeCall(updateLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<UpdateLoggingConfigurationResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a specified logging configuration.
     * @param updateLoggingConfigurationRequest  (required)
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
        <tr><td> 480 </td><td> ConflictException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 484 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateLoggingConfigurationAsync(UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<UpdateLoggingConfigurationResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateLoggingConfigurationValidateBeforeCall(updateLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<UpdateLoggingConfigurationResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for updateRoom
     * @param updateRoomRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRoomCall(UpdateRoomRequest updateRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = updateRoomRequest;

        // create path and map variables
        String localVarPath = "/UpdateRoom";

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
    private okhttp3.Call updateRoomValidateBeforeCall(UpdateRoomRequest updateRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'updateRoomRequest' is set
        if (updateRoomRequest == null) {
            throw new ApiException("Missing the required parameter 'updateRoomRequest' when calling updateRoom(Async)");
        }

        return updateRoomCall(updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);

    }

    /**
     * 
     * Updates a room’s configuration.
     * @param updateRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return UpdateRoomResponse
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public UpdateRoomResponse updateRoom(UpdateRoomRequest updateRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        ApiResponse<UpdateRoomResponse> localVarResp = updateRoomWithHttpInfo(updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        return localVarResp.getData();
    }

    /**
     * 
     * Updates a room’s configuration.
     * @param updateRoomRequest  (required)
     * @param xAmzContentSha256  (optional)
     * @param xAmzDate  (optional)
     * @param xAmzAlgorithm  (optional)
     * @param xAmzCredential  (optional)
     * @param xAmzSecurityToken  (optional)
     * @param xAmzSignature  (optional)
     * @param xAmzSignedHeaders  (optional)
     * @return ApiResponse&lt;UpdateRoomResponse&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Success </td><td>  -  </td></tr>
        <tr><td> 480 </td><td> AccessDeniedException </td><td>  -  </td></tr>
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<UpdateRoomResponse> updateRoomWithHttpInfo(UpdateRoomRequest updateRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders) throws ApiException {
        okhttp3.Call localVarCall = updateRoomValidateBeforeCall(updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, null);
        Type localVarReturnType = new TypeToken<UpdateRoomResponse>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Updates a room’s configuration.
     * @param updateRoomRequest  (required)
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
        <tr><td> 481 </td><td> ResourceNotFoundException </td><td>  -  </td></tr>
        <tr><td> 482 </td><td> PendingVerification </td><td>  -  </td></tr>
        <tr><td> 483 </td><td> ValidationException </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call updateRoomAsync(UpdateRoomRequest updateRoomRequest, String xAmzContentSha256, String xAmzDate, String xAmzAlgorithm, String xAmzCredential, String xAmzSecurityToken, String xAmzSignature, String xAmzSignedHeaders, final ApiCallback<UpdateRoomResponse> _callback) throws ApiException {

        okhttp3.Call localVarCall = updateRoomValidateBeforeCall(updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, _callback);
        Type localVarReturnType = new TypeToken<UpdateRoomResponse>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
