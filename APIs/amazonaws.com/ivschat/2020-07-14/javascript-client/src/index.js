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


import ApiClient from './ApiClient';
import ChatTokenCapability from './model/ChatTokenCapability';
import CloudWatchLogsDestinationConfiguration from './model/CloudWatchLogsDestinationConfiguration';
import CreateChatTokenRequest from './model/CreateChatTokenRequest';
import CreateChatTokenResponse from './model/CreateChatTokenResponse';
import CreateLoggingConfigurationRequest from './model/CreateLoggingConfigurationRequest';
import CreateLoggingConfigurationRequestDestinationConfiguration from './model/CreateLoggingConfigurationRequestDestinationConfiguration';
import CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs from './model/CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs';
import CreateLoggingConfigurationRequestDestinationConfigurationFirehose from './model/CreateLoggingConfigurationRequestDestinationConfigurationFirehose';
import CreateLoggingConfigurationRequestDestinationConfigurationS3 from './model/CreateLoggingConfigurationRequestDestinationConfigurationS3';
import CreateLoggingConfigurationResponse from './model/CreateLoggingConfigurationResponse';
import CreateLoggingConfigurationResponseDestinationConfiguration from './model/CreateLoggingConfigurationResponseDestinationConfiguration';
import CreateLoggingConfigurationState from './model/CreateLoggingConfigurationState';
import CreateRoomRequest from './model/CreateRoomRequest';
import CreateRoomRequestMessageReviewHandler from './model/CreateRoomRequestMessageReviewHandler';
import CreateRoomResponse from './model/CreateRoomResponse';
import CreateRoomResponseMessageReviewHandler from './model/CreateRoomResponseMessageReviewHandler';
import DeleteLoggingConfigurationRequest from './model/DeleteLoggingConfigurationRequest';
import DeleteMessageRequest from './model/DeleteMessageRequest';
import DeleteMessageResponse from './model/DeleteMessageResponse';
import DeleteRoomRequest from './model/DeleteRoomRequest';
import DestinationConfiguration from './model/DestinationConfiguration';
import DisconnectUserRequest from './model/DisconnectUserRequest';
import FallbackResult from './model/FallbackResult';
import FirehoseDestinationConfiguration from './model/FirehoseDestinationConfiguration';
import GetLoggingConfigurationRequest from './model/GetLoggingConfigurationRequest';
import GetLoggingConfigurationResponse from './model/GetLoggingConfigurationResponse';
import GetLoggingConfigurationResponseDestinationConfiguration from './model/GetLoggingConfigurationResponseDestinationConfiguration';
import GetRoomRequest from './model/GetRoomRequest';
import GetRoomResponse from './model/GetRoomResponse';
import ListLoggingConfigurationsRequest from './model/ListLoggingConfigurationsRequest';
import ListLoggingConfigurationsResponse from './model/ListLoggingConfigurationsResponse';
import ListRoomsRequest from './model/ListRoomsRequest';
import ListRoomsResponse from './model/ListRoomsResponse';
import ListTagsForResourceResponse from './model/ListTagsForResourceResponse';
import LoggingConfigurationState from './model/LoggingConfigurationState';
import LoggingConfigurationSummary from './model/LoggingConfigurationSummary';
import LoggingConfigurationSummaryDestinationConfiguration from './model/LoggingConfigurationSummaryDestinationConfiguration';
import MessageReviewHandler from './model/MessageReviewHandler';
import RoomSummary from './model/RoomSummary';
import S3DestinationConfiguration from './model/S3DestinationConfiguration';
import SendEventRequest from './model/SendEventRequest';
import SendEventResponse from './model/SendEventResponse';
import TagResourceRequest from './model/TagResourceRequest';
import UpdateLoggingConfigurationRequest from './model/UpdateLoggingConfigurationRequest';
import UpdateLoggingConfigurationResponse from './model/UpdateLoggingConfigurationResponse';
import UpdateLoggingConfigurationState from './model/UpdateLoggingConfigurationState';
import UpdateRoomRequest from './model/UpdateRoomRequest';
import UpdateRoomRequestMessageReviewHandler from './model/UpdateRoomRequestMessageReviewHandler';
import UpdateRoomResponse from './model/UpdateRoomResponse';
import DefaultApi from './api/DefaultApi';


/**
* &lt;p&gt; &lt;b&gt;Introduction&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\&quot;&gt; Amazon IVS Chat Messaging API&lt;/a&gt;, to enable users to interact with chat rooms in real time.&lt;/p&gt; &lt;p&gt;The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/ivs.html\&quot;&gt;Amazon IVS page&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Notes on terminology:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You create service applications using the Amazon IVS Chat API. We refer to these as &lt;i&gt;applications&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as &lt;i&gt;clients&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Resources&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The following resources are part of Amazon IVS Chat:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;LoggingConfiguration&lt;/b&gt; — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Room&lt;/b&gt; — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Tagging&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A &lt;i&gt;tag&lt;/i&gt; is a metadata label that you assign to an AWS resource. A tag comprises a &lt;i&gt;key&lt;/i&gt; and a &lt;i&gt;value&lt;/i&gt;, both set by you. For example, you might set a tag as &lt;code&gt;topic:nature&lt;/code&gt; to label a particular video category. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging AWS Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS Chat has no service-specific constraints beyond what is documented there.&lt;/p&gt; &lt;p&gt;Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt;Access Tags&lt;/a&gt;).&lt;/p&gt; &lt;p&gt;The Amazon IVS Chat API has these tag-related endpoints: &lt;a&gt;TagResource&lt;/a&gt;, &lt;a&gt;UntagResource&lt;/a&gt;, and &lt;a&gt;ListTagsForResource&lt;/a&gt;. The following resource supports tagging: Room.&lt;/p&gt; &lt;p&gt;At most 50 tags can be applied to a resource.&lt;/p&gt; &lt;p&gt; &lt;b&gt;API Access Security&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Authentication&lt;/i&gt; is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Authorization&lt;/i&gt; is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Users (viewers) connect to a room using secure access tokens that you create using the &lt;a&gt;CreateChatToken&lt;/a&gt; endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Signing API Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.&lt;/p&gt; &lt;p&gt;You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the &lt;code&gt;ivschat:DeleteMessage&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;For more information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Authentication and generating signatures — See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Managing Amazon IVS permissions — See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\&quot;&gt;Identity and Access Management&lt;/a&gt; on the Security page of the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Amazon Resource Names (ARNs)&lt;/b&gt; &lt;/p&gt; &lt;p&gt;ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Messaging Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteMessage&lt;/a&gt; — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s &lt;code&gt;EventName&lt;/code&gt; is &lt;code&gt;aws:DELETE_MESSAGE&lt;/code&gt;. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\&quot;&gt; DeleteMessage&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DisconnectUser&lt;/a&gt; — Disconnects all connections using a specified user ID from a room. This replicates the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\&quot;&gt; DisconnectUser&lt;/a&gt; WebSocket operation in the Amazon IVS Chat Messaging API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;SendEvent&lt;/a&gt; — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Chat Token Endpoint&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateChatToken&lt;/a&gt; — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Room Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateRoom&lt;/a&gt; — Creates a room that allows clients to connect and pass messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteRoom&lt;/a&gt; — Deletes the specified room.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetRoom&lt;/a&gt; — Gets the specified room.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListRooms&lt;/a&gt; — Gets summary information about all your rooms in the AWS region where the API request is processed. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateRoom&lt;/a&gt; — Updates a room’s configuration.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Logging Configuration Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateLoggingConfiguration&lt;/a&gt; — Creates a logging configuration that allows clients to store and record sent messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteLoggingConfiguration&lt;/a&gt; — Deletes the specified logging configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetLoggingConfiguration&lt;/a&gt; — Gets the specified logging configuration.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListLoggingConfigurations&lt;/a&gt; — Gets summary information about all your logging configurations in the AWS region where the API request is processed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateLoggingConfiguration&lt;/a&gt; — Updates a specified logging configuration.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Tags Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt; — Gets information about AWS tags for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt; — Adds or updates tags for the AWS resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt; — Removes tags from the resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;All the above are HTTP operations. There is a separate &lt;i&gt;messaging&lt;/i&gt; API for managing Chat resources; see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\&quot;&gt; Amazon IVS Chat Messaging API Reference&lt;/a&gt;.&lt;/p&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AmazonInteractiveVideoServiceChat = require('index'); // See note below*.
* var xxxSvc = new AmazonInteractiveVideoServiceChat.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AmazonInteractiveVideoServiceChat.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new AmazonInteractiveVideoServiceChat.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AmazonInteractiveVideoServiceChat.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2020-07-14
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ChatTokenCapability model constructor.
     * @property {module:model/ChatTokenCapability}
     */
    ChatTokenCapability,

    /**
     * The CloudWatchLogsDestinationConfiguration model constructor.
     * @property {module:model/CloudWatchLogsDestinationConfiguration}
     */
    CloudWatchLogsDestinationConfiguration,

    /**
     * The CreateChatTokenRequest model constructor.
     * @property {module:model/CreateChatTokenRequest}
     */
    CreateChatTokenRequest,

    /**
     * The CreateChatTokenResponse model constructor.
     * @property {module:model/CreateChatTokenResponse}
     */
    CreateChatTokenResponse,

    /**
     * The CreateLoggingConfigurationRequest model constructor.
     * @property {module:model/CreateLoggingConfigurationRequest}
     */
    CreateLoggingConfigurationRequest,

    /**
     * The CreateLoggingConfigurationRequestDestinationConfiguration model constructor.
     * @property {module:model/CreateLoggingConfigurationRequestDestinationConfiguration}
     */
    CreateLoggingConfigurationRequestDestinationConfiguration,

    /**
     * The CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs model constructor.
     * @property {module:model/CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs}
     */
    CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs,

    /**
     * The CreateLoggingConfigurationRequestDestinationConfigurationFirehose model constructor.
     * @property {module:model/CreateLoggingConfigurationRequestDestinationConfigurationFirehose}
     */
    CreateLoggingConfigurationRequestDestinationConfigurationFirehose,

    /**
     * The CreateLoggingConfigurationRequestDestinationConfigurationS3 model constructor.
     * @property {module:model/CreateLoggingConfigurationRequestDestinationConfigurationS3}
     */
    CreateLoggingConfigurationRequestDestinationConfigurationS3,

    /**
     * The CreateLoggingConfigurationResponse model constructor.
     * @property {module:model/CreateLoggingConfigurationResponse}
     */
    CreateLoggingConfigurationResponse,

    /**
     * The CreateLoggingConfigurationResponseDestinationConfiguration model constructor.
     * @property {module:model/CreateLoggingConfigurationResponseDestinationConfiguration}
     */
    CreateLoggingConfigurationResponseDestinationConfiguration,

    /**
     * The CreateLoggingConfigurationState model constructor.
     * @property {module:model/CreateLoggingConfigurationState}
     */
    CreateLoggingConfigurationState,

    /**
     * The CreateRoomRequest model constructor.
     * @property {module:model/CreateRoomRequest}
     */
    CreateRoomRequest,

    /**
     * The CreateRoomRequestMessageReviewHandler model constructor.
     * @property {module:model/CreateRoomRequestMessageReviewHandler}
     */
    CreateRoomRequestMessageReviewHandler,

    /**
     * The CreateRoomResponse model constructor.
     * @property {module:model/CreateRoomResponse}
     */
    CreateRoomResponse,

    /**
     * The CreateRoomResponseMessageReviewHandler model constructor.
     * @property {module:model/CreateRoomResponseMessageReviewHandler}
     */
    CreateRoomResponseMessageReviewHandler,

    /**
     * The DeleteLoggingConfigurationRequest model constructor.
     * @property {module:model/DeleteLoggingConfigurationRequest}
     */
    DeleteLoggingConfigurationRequest,

    /**
     * The DeleteMessageRequest model constructor.
     * @property {module:model/DeleteMessageRequest}
     */
    DeleteMessageRequest,

    /**
     * The DeleteMessageResponse model constructor.
     * @property {module:model/DeleteMessageResponse}
     */
    DeleteMessageResponse,

    /**
     * The DeleteRoomRequest model constructor.
     * @property {module:model/DeleteRoomRequest}
     */
    DeleteRoomRequest,

    /**
     * The DestinationConfiguration model constructor.
     * @property {module:model/DestinationConfiguration}
     */
    DestinationConfiguration,

    /**
     * The DisconnectUserRequest model constructor.
     * @property {module:model/DisconnectUserRequest}
     */
    DisconnectUserRequest,

    /**
     * The FallbackResult model constructor.
     * @property {module:model/FallbackResult}
     */
    FallbackResult,

    /**
     * The FirehoseDestinationConfiguration model constructor.
     * @property {module:model/FirehoseDestinationConfiguration}
     */
    FirehoseDestinationConfiguration,

    /**
     * The GetLoggingConfigurationRequest model constructor.
     * @property {module:model/GetLoggingConfigurationRequest}
     */
    GetLoggingConfigurationRequest,

    /**
     * The GetLoggingConfigurationResponse model constructor.
     * @property {module:model/GetLoggingConfigurationResponse}
     */
    GetLoggingConfigurationResponse,

    /**
     * The GetLoggingConfigurationResponseDestinationConfiguration model constructor.
     * @property {module:model/GetLoggingConfigurationResponseDestinationConfiguration}
     */
    GetLoggingConfigurationResponseDestinationConfiguration,

    /**
     * The GetRoomRequest model constructor.
     * @property {module:model/GetRoomRequest}
     */
    GetRoomRequest,

    /**
     * The GetRoomResponse model constructor.
     * @property {module:model/GetRoomResponse}
     */
    GetRoomResponse,

    /**
     * The ListLoggingConfigurationsRequest model constructor.
     * @property {module:model/ListLoggingConfigurationsRequest}
     */
    ListLoggingConfigurationsRequest,

    /**
     * The ListLoggingConfigurationsResponse model constructor.
     * @property {module:model/ListLoggingConfigurationsResponse}
     */
    ListLoggingConfigurationsResponse,

    /**
     * The ListRoomsRequest model constructor.
     * @property {module:model/ListRoomsRequest}
     */
    ListRoomsRequest,

    /**
     * The ListRoomsResponse model constructor.
     * @property {module:model/ListRoomsResponse}
     */
    ListRoomsResponse,

    /**
     * The ListTagsForResourceResponse model constructor.
     * @property {module:model/ListTagsForResourceResponse}
     */
    ListTagsForResourceResponse,

    /**
     * The LoggingConfigurationState model constructor.
     * @property {module:model/LoggingConfigurationState}
     */
    LoggingConfigurationState,

    /**
     * The LoggingConfigurationSummary model constructor.
     * @property {module:model/LoggingConfigurationSummary}
     */
    LoggingConfigurationSummary,

    /**
     * The LoggingConfigurationSummaryDestinationConfiguration model constructor.
     * @property {module:model/LoggingConfigurationSummaryDestinationConfiguration}
     */
    LoggingConfigurationSummaryDestinationConfiguration,

    /**
     * The MessageReviewHandler model constructor.
     * @property {module:model/MessageReviewHandler}
     */
    MessageReviewHandler,

    /**
     * The RoomSummary model constructor.
     * @property {module:model/RoomSummary}
     */
    RoomSummary,

    /**
     * The S3DestinationConfiguration model constructor.
     * @property {module:model/S3DestinationConfiguration}
     */
    S3DestinationConfiguration,

    /**
     * The SendEventRequest model constructor.
     * @property {module:model/SendEventRequest}
     */
    SendEventRequest,

    /**
     * The SendEventResponse model constructor.
     * @property {module:model/SendEventResponse}
     */
    SendEventResponse,

    /**
     * The TagResourceRequest model constructor.
     * @property {module:model/TagResourceRequest}
     */
    TagResourceRequest,

    /**
     * The UpdateLoggingConfigurationRequest model constructor.
     * @property {module:model/UpdateLoggingConfigurationRequest}
     */
    UpdateLoggingConfigurationRequest,

    /**
     * The UpdateLoggingConfigurationResponse model constructor.
     * @property {module:model/UpdateLoggingConfigurationResponse}
     */
    UpdateLoggingConfigurationResponse,

    /**
     * The UpdateLoggingConfigurationState model constructor.
     * @property {module:model/UpdateLoggingConfigurationState}
     */
    UpdateLoggingConfigurationState,

    /**
     * The UpdateRoomRequest model constructor.
     * @property {module:model/UpdateRoomRequest}
     */
    UpdateRoomRequest,

    /**
     * The UpdateRoomRequestMessageReviewHandler model constructor.
     * @property {module:model/UpdateRoomRequestMessageReviewHandler}
     */
    UpdateRoomRequestMessageReviewHandler,

    /**
     * The UpdateRoomResponse model constructor.
     * @property {module:model/UpdateRoomResponse}
     */
    UpdateRoomResponse,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
