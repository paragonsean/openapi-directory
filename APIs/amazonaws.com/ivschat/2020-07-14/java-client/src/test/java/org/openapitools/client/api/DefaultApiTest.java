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

import org.openapitools.client.ApiException;
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
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * &lt;p&gt;Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;capabilities&lt;/code&gt; field to permit an end user to send messages or moderate a room.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;attributes&lt;/code&gt; field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.&lt;/p&gt; &lt;p&gt;Encryption keys are owned by Amazon IVS Chat and never used directly by your application.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createChatTokenTest() throws ApiException {
        CreateChatTokenRequest createChatTokenRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateChatTokenResponse response = api.createChatToken(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a logging configuration that allows clients to store and record sent messages.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createLoggingConfigurationTest() throws ApiException {
        CreateLoggingConfigurationRequest createLoggingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateLoggingConfigurationResponse response = api.createLoggingConfiguration(createLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a room that allows clients to connect and pass messages.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createRoomTest() throws ApiException {
        CreateRoomRequest createRoomRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateRoomResponse response = api.createRoom(createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the specified logging configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteLoggingConfigurationTest() throws ApiException {
        DeleteLoggingConfigurationRequest deleteLoggingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteLoggingConfiguration(deleteLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s &lt;code&gt;EventName&lt;/code&gt; is &lt;code&gt;aws:DELETE_MESSAGE&lt;/code&gt;. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\&quot;&gt; DeleteMessage&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteMessageTest() throws ApiException {
        DeleteMessageRequest deleteMessageRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        DeleteMessageResponse response = api.deleteMessage(deleteMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the specified room.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRoomTest() throws ApiException {
        DeleteRoomRequest deleteRoomRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteRoom(deleteRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Disconnects all connections using a specified user ID from a room. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\&quot;&gt; DisconnectUser&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void disconnectUserTest() throws ApiException {
        DisconnectUserRequest disconnectUserRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.disconnectUser(disconnectUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets the specified logging configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLoggingConfigurationTest() throws ApiException {
        GetLoggingConfigurationRequest getLoggingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetLoggingConfigurationResponse response = api.getLoggingConfiguration(getLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets the specified room.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRoomTest() throws ApiException {
        GetRoomRequest getRoomRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetRoomResponse response = api.getRoom(getRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets summary information about all your logging configurations in the AWS region where the API request is processed.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listLoggingConfigurationsTest() throws ApiException {
        ListLoggingConfigurationsRequest listLoggingConfigurationsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListLoggingConfigurationsResponse response = api.listLoggingConfigurations(listLoggingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of &lt;code&gt;updateTime&lt;/code&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRoomsTest() throws ApiException {
        ListRoomsRequest listRoomsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListRoomsResponse response = api.listRooms(listRoomsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets information about AWS tags for the specified ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTagsForResourceTest() throws ApiException {
        String resourceArn = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        ListTagsForResourceResponse response = api.listTagsForResource(resourceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sendEventTest() throws ApiException {
        SendEventRequest sendEventRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        SendEventResponse response = api.sendEvent(sendEventRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds or updates tags for the AWS resource with the specified ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void tagResourceTest() throws ApiException {
        String resourceArn = null;
        TagResourceRequest tagResourceRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.tagResource(resourceArn, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Removes tags from the resource with the specified ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void untagResourceTest() throws ApiException {
        String resourceArn = null;
        List<String> tagKeys = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.untagResource(resourceArn, tagKeys, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates a specified logging configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateLoggingConfigurationTest() throws ApiException {
        UpdateLoggingConfigurationRequest updateLoggingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateLoggingConfigurationResponse response = api.updateLoggingConfiguration(updateLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Updates a room’s configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateRoomTest() throws ApiException {
        UpdateRoomRequest updateRoomRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateRoomResponse response = api.updateRoom(updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
