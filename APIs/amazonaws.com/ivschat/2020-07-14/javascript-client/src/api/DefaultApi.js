/**
 * Amazon Interactive Video Service Chat
 * <p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>
 *
 * The version of the OpenAPI document: 2020-07-14
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateChatTokenRequest from '../model/CreateChatTokenRequest';
import CreateChatTokenResponse from '../model/CreateChatTokenResponse';
import CreateLoggingConfigurationRequest from '../model/CreateLoggingConfigurationRequest';
import CreateLoggingConfigurationResponse from '../model/CreateLoggingConfigurationResponse';
import CreateRoomRequest from '../model/CreateRoomRequest';
import CreateRoomResponse from '../model/CreateRoomResponse';
import DeleteLoggingConfigurationRequest from '../model/DeleteLoggingConfigurationRequest';
import DeleteMessageRequest from '../model/DeleteMessageRequest';
import DeleteMessageResponse from '../model/DeleteMessageResponse';
import DeleteRoomRequest from '../model/DeleteRoomRequest';
import DisconnectUserRequest from '../model/DisconnectUserRequest';
import GetLoggingConfigurationRequest from '../model/GetLoggingConfigurationRequest';
import GetLoggingConfigurationResponse from '../model/GetLoggingConfigurationResponse';
import GetRoomRequest from '../model/GetRoomRequest';
import GetRoomResponse from '../model/GetRoomResponse';
import ListLoggingConfigurationsRequest from '../model/ListLoggingConfigurationsRequest';
import ListLoggingConfigurationsResponse from '../model/ListLoggingConfigurationsResponse';
import ListRoomsRequest from '../model/ListRoomsRequest';
import ListRoomsResponse from '../model/ListRoomsResponse';
import ListTagsForResourceResponse from '../model/ListTagsForResourceResponse';
import SendEventRequest from '../model/SendEventRequest';
import SendEventResponse from '../model/SendEventResponse';
import TagResourceRequest from '../model/TagResourceRequest';
import UpdateLoggingConfigurationRequest from '../model/UpdateLoggingConfigurationRequest';
import UpdateLoggingConfigurationResponse from '../model/UpdateLoggingConfigurationResponse';
import UpdateRoomRequest from '../model/UpdateRoomRequest';
import UpdateRoomResponse from '../model/UpdateRoomResponse';

/**
* Default service.
* @module api/DefaultApi
* @version 2020-07-14
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createChatToken operation.
     * @callback module:api/DefaultApi~createChatTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateChatTokenResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> <p>Use the <code>capabilities</code> field to permit an end user to send messages or moderate a room.</p> <p>The <code>attributes</code> field securely attaches structured data to the chat session; the data is included within each message sent by the end user and received by other participants in the room. Common use cases for attributes include passing end-user profile data like an icon, display name, colors, badges, and other display features.</p> <p>Encryption keys are owned by Amazon IVS Chat and never used directly by your application.</p>
     * @param {module:model/CreateChatTokenRequest} createChatTokenRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createChatTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateChatTokenResponse}
     */
    createChatToken(createChatTokenRequest, opts, callback) {
      opts = opts || {};
      let postBody = createChatTokenRequest;
      // verify the required parameter 'createChatTokenRequest' is set
      if (createChatTokenRequest === undefined || createChatTokenRequest === null) {
        throw new Error("Missing the required parameter 'createChatTokenRequest' when calling createChatToken");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateChatTokenResponse;
      return this.apiClient.callApi(
        '/CreateChatToken', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createLoggingConfiguration operation.
     * @callback module:api/DefaultApi~createLoggingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateLoggingConfigurationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a logging configuration that allows clients to store and record sent messages.
     * @param {module:model/CreateLoggingConfigurationRequest} createLoggingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createLoggingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateLoggingConfigurationResponse}
     */
    createLoggingConfiguration(createLoggingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = createLoggingConfigurationRequest;
      // verify the required parameter 'createLoggingConfigurationRequest' is set
      if (createLoggingConfigurationRequest === undefined || createLoggingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'createLoggingConfigurationRequest' when calling createLoggingConfiguration");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateLoggingConfigurationResponse;
      return this.apiClient.callApi(
        '/CreateLoggingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRoom operation.
     * @callback module:api/DefaultApi~createRoomCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRoomResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a room that allows clients to connect and pass messages.
     * @param {module:model/CreateRoomRequest} createRoomRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createRoomCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRoomResponse}
     */
    createRoom(createRoomRequest, opts, callback) {
      opts = opts || {};
      let postBody = createRoomRequest;
      // verify the required parameter 'createRoomRequest' is set
      if (createRoomRequest === undefined || createRoomRequest === null) {
        throw new Error("Missing the required parameter 'createRoomRequest' when calling createRoom");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreateRoomResponse;
      return this.apiClient.callApi(
        '/CreateRoom', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteLoggingConfiguration operation.
     * @callback module:api/DefaultApi~deleteLoggingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified logging configuration.
     * @param {module:model/DeleteLoggingConfigurationRequest} deleteLoggingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteLoggingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteLoggingConfiguration(deleteLoggingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteLoggingConfigurationRequest;
      // verify the required parameter 'deleteLoggingConfigurationRequest' is set
      if (deleteLoggingConfigurationRequest === undefined || deleteLoggingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'deleteLoggingConfigurationRequest' when calling deleteLoggingConfiguration");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/DeleteLoggingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteMessage operation.
     * @callback module:api/DefaultApi~deleteMessageCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DeleteMessageResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param {module:model/DeleteMessageRequest} deleteMessageRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteMessageCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DeleteMessageResponse}
     */
    deleteMessage(deleteMessageRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteMessageRequest;
      // verify the required parameter 'deleteMessageRequest' is set
      if (deleteMessageRequest === undefined || deleteMessageRequest === null) {
        throw new Error("Missing the required parameter 'deleteMessageRequest' when calling deleteMessage");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = DeleteMessageResponse;
      return this.apiClient.callApi(
        '/DeleteMessage', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRoom operation.
     * @callback module:api/DefaultApi~deleteRoomCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified room.
     * @param {module:model/DeleteRoomRequest} deleteRoomRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteRoomCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteRoom(deleteRoomRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteRoomRequest;
      // verify the required parameter 'deleteRoomRequest' is set
      if (deleteRoomRequest === undefined || deleteRoomRequest === null) {
        throw new Error("Missing the required parameter 'deleteRoomRequest' when calling deleteRoom");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/DeleteRoom', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the disconnectUser operation.
     * @callback module:api/DefaultApi~disconnectUserCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.
     * @param {module:model/DisconnectUserRequest} disconnectUserRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~disconnectUserCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    disconnectUser(disconnectUserRequest, opts, callback) {
      opts = opts || {};
      let postBody = disconnectUserRequest;
      // verify the required parameter 'disconnectUserRequest' is set
      if (disconnectUserRequest === undefined || disconnectUserRequest === null) {
        throw new Error("Missing the required parameter 'disconnectUserRequest' when calling disconnectUser");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/DisconnectUser', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getLoggingConfiguration operation.
     * @callback module:api/DefaultApi~getLoggingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetLoggingConfigurationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the specified logging configuration.
     * @param {module:model/GetLoggingConfigurationRequest} getLoggingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getLoggingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetLoggingConfigurationResponse}
     */
    getLoggingConfiguration(getLoggingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = getLoggingConfigurationRequest;
      // verify the required parameter 'getLoggingConfigurationRequest' is set
      if (getLoggingConfigurationRequest === undefined || getLoggingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'getLoggingConfigurationRequest' when calling getLoggingConfiguration");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetLoggingConfigurationResponse;
      return this.apiClient.callApi(
        '/GetLoggingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRoom operation.
     * @callback module:api/DefaultApi~getRoomCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRoomResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the specified room.
     * @param {module:model/GetRoomRequest} getRoomRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRoomCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRoomResponse}
     */
    getRoom(getRoomRequest, opts, callback) {
      opts = opts || {};
      let postBody = getRoomRequest;
      // verify the required parameter 'getRoomRequest' is set
      if (getRoomRequest === undefined || getRoomRequest === null) {
        throw new Error("Missing the required parameter 'getRoomRequest' when calling getRoom");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = GetRoomResponse;
      return this.apiClient.callApi(
        '/GetRoom', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listLoggingConfigurations operation.
     * @callback module:api/DefaultApi~listLoggingConfigurationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListLoggingConfigurationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about all your logging configurations in the AWS region where the API request is processed.
     * @param {module:model/ListLoggingConfigurationsRequest} listLoggingConfigurationsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listLoggingConfigurationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListLoggingConfigurationsResponse}
     */
    listLoggingConfigurations(listLoggingConfigurationsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listLoggingConfigurationsRequest;
      // verify the required parameter 'listLoggingConfigurationsRequest' is set
      if (listLoggingConfigurationsRequest === undefined || listLoggingConfigurationsRequest === null) {
        throw new Error("Missing the required parameter 'listLoggingConfigurationsRequest' when calling listLoggingConfigurations");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListLoggingConfigurationsResponse;
      return this.apiClient.callApi(
        '/ListLoggingConfigurations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRooms operation.
     * @callback module:api/DefaultApi~listRoomsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRoomsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about all your rooms in the AWS region where the API request is processed. Results are sorted in descending order of <code>updateTime</code>.
     * @param {module:model/ListRoomsRequest} listRoomsRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {String} [maxResults] Pagination limit
     * @param {String} [nextToken] Pagination token
     * @param {module:api/DefaultApi~listRoomsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRoomsResponse}
     */
    listRooms(listRoomsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listRoomsRequest;
      // verify the required parameter 'listRoomsRequest' is set
      if (listRoomsRequest === undefined || listRoomsRequest === null) {
        throw new Error("Missing the required parameter 'listRoomsRequest' when calling listRooms");
      }

      let pathParams = {
      };
      let queryParams = {
        'maxResults': opts['maxResults'],
        'nextToken': opts['nextToken']
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ListRoomsResponse;
      return this.apiClient.callApi(
        '/ListRooms', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listTagsForResource operation.
     * @callback module:api/DefaultApi~listTagsForResourceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListTagsForResourceResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about AWS tags for the specified ARN.
     * @param {String} resourceArn The ARN of the resource to be retrieved. The ARN must be URL-encoded.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~listTagsForResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListTagsForResourceResponse}
     */
    listTagsForResource(resourceArn, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling listTagsForResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ListTagsForResourceResponse;
      return this.apiClient.callApi(
        '/tags/{resourceArn}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sendEvent operation.
     * @callback module:api/DefaultApi~sendEventCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SendEventResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.
     * @param {module:model/SendEventRequest} sendEventRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~sendEventCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SendEventResponse}
     */
    sendEvent(sendEventRequest, opts, callback) {
      opts = opts || {};
      let postBody = sendEventRequest;
      // verify the required parameter 'sendEventRequest' is set
      if (sendEventRequest === undefined || sendEventRequest === null) {
        throw new Error("Missing the required parameter 'sendEventRequest' when calling sendEvent");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = SendEventResponse;
      return this.apiClient.callApi(
        '/SendEvent', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tagResource operation.
     * @callback module:api/DefaultApi~tagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Adds or updates tags for the AWS resource with the specified ARN.
     * @param {String} resourceArn The ARN of the resource to be tagged. The ARN must be URL-encoded.
     * @param {module:model/TagResourceRequest} tagResourceRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~tagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    tagResource(resourceArn, tagResourceRequest, opts, callback) {
      opts = opts || {};
      let postBody = tagResourceRequest;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling tagResource");
      }
      // verify the required parameter 'tagResourceRequest' is set
      if (tagResourceRequest === undefined || tagResourceRequest === null) {
        throw new Error("Missing the required parameter 'tagResourceRequest' when calling tagResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tags/{resourceArn}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the untagResource operation.
     * @callback module:api/DefaultApi~untagResourceCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Removes tags from the resource with the specified ARN.
     * @param {String} resourceArn The ARN of the resource to be untagged. The ARN must be URL-encoded.
     * @param {Array.<String>} tagKeys Array of tags to be removed. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no constraints beyond what is documented there.
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~untagResourceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    untagResource(resourceArn, tagKeys, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceArn' is set
      if (resourceArn === undefined || resourceArn === null) {
        throw new Error("Missing the required parameter 'resourceArn' when calling untagResource");
      }
      // verify the required parameter 'tagKeys' is set
      if (tagKeys === undefined || tagKeys === null) {
        throw new Error("Missing the required parameter 'tagKeys' when calling untagResource");
      }

      let pathParams = {
        'resourceArn': resourceArn
      };
      let queryParams = {
        'tagKeys': this.apiClient.buildCollectionParam(tagKeys, 'multi')
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tags/{resourceArn}#tagKeys', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateLoggingConfiguration operation.
     * @callback module:api/DefaultApi~updateLoggingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateLoggingConfigurationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a specified logging configuration.
     * @param {module:model/UpdateLoggingConfigurationRequest} updateLoggingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateLoggingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateLoggingConfigurationResponse}
     */
    updateLoggingConfiguration(updateLoggingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = updateLoggingConfigurationRequest;
      // verify the required parameter 'updateLoggingConfigurationRequest' is set
      if (updateLoggingConfigurationRequest === undefined || updateLoggingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'updateLoggingConfigurationRequest' when calling updateLoggingConfiguration");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateLoggingConfigurationResponse;
      return this.apiClient.callApi(
        '/UpdateLoggingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateRoom operation.
     * @callback module:api/DefaultApi~updateRoomCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateRoomResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a room’s configuration.
     * @param {module:model/UpdateRoomRequest} updateRoomRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateRoomCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateRoomResponse}
     */
    updateRoom(updateRoomRequest, opts, callback) {
      opts = opts || {};
      let postBody = updateRoomRequest;
      // verify the required parameter 'updateRoomRequest' is set
      if (updateRoomRequest === undefined || updateRoomRequest === null) {
        throw new Error("Missing the required parameter 'updateRoomRequest' when calling updateRoom");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Amz-Content-Sha256': opts['xAmzContentSha256'],
        'X-Amz-Date': opts['xAmzDate'],
        'X-Amz-Algorithm': opts['xAmzAlgorithm'],
        'X-Amz-Credential': opts['xAmzCredential'],
        'X-Amz-Security-Token': opts['xAmzSecurityToken'],
        'X-Amz-Signature': opts['xAmzSignature'],
        'X-Amz-SignedHeaders': opts['xAmzSignedHeaders']
      };
      let formParams = {
      };

      let authNames = ['hmac'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = UpdateRoomResponse;
      return this.apiClient.callApi(
        '/UpdateRoom', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
