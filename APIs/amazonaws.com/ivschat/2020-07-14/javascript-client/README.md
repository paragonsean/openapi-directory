# amazon_interactive_video_service_chat

AmazonInteractiveVideoServiceChat - JavaScript client for amazon_interactive_video_service_chat
<p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2020-07-14
- Package version: 2020-07-14
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install amazon_interactive_video_service_chat --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your amazon_interactive_video_service_chat from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var AmazonInteractiveVideoServiceChat = require('amazon_interactive_video_service_chat');

var defaultClient = AmazonInteractiveVideoServiceChat.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AmazonInteractiveVideoServiceChat.DefaultApi()
var createChatTokenRequest = new AmazonInteractiveVideoServiceChat.CreateChatTokenRequest(); // {CreateChatTokenRequest} 
var opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // {String} 
  'xAmzDate': "xAmzDate_example", // {String} 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // {String} 
  'xAmzCredential': "xAmzCredential_example", // {String} 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // {String} 
  'xAmzSignature': "xAmzSignature_example", // {String} 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.createChatToken(createChatTokenRequest, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://ivschat.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**createChatToken**](docs/DefaultApi.md#createChatToken) | **POST** /CreateChatToken | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**createLoggingConfiguration**](docs/DefaultApi.md#createLoggingConfiguration) | **POST** /CreateLoggingConfiguration | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**createRoom**](docs/DefaultApi.md#createRoom) | **POST** /CreateRoom | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**deleteLoggingConfiguration**](docs/DefaultApi.md#deleteLoggingConfiguration) | **POST** /DeleteLoggingConfiguration | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**deleteMessage**](docs/DefaultApi.md#deleteMessage) | **POST** /DeleteMessage | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**deleteRoom**](docs/DefaultApi.md#deleteRoom) | **POST** /DeleteRoom | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**disconnectUser**](docs/DefaultApi.md#disconnectUser) | **POST** /DisconnectUser | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**getLoggingConfiguration**](docs/DefaultApi.md#getLoggingConfiguration) | **POST** /GetLoggingConfiguration | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**getRoom**](docs/DefaultApi.md#getRoom) | **POST** /GetRoom | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**listLoggingConfigurations**](docs/DefaultApi.md#listLoggingConfigurations) | **POST** /ListLoggingConfigurations | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**listRooms**](docs/DefaultApi.md#listRooms) | **POST** /ListRooms | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**sendEvent**](docs/DefaultApi.md#sendEvent) | **POST** /SendEvent | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**updateLoggingConfiguration**](docs/DefaultApi.md#updateLoggingConfiguration) | **POST** /UpdateLoggingConfiguration | 
*AmazonInteractiveVideoServiceChat.DefaultApi* | [**updateRoom**](docs/DefaultApi.md#updateRoom) | **POST** /UpdateRoom | 


## Documentation for Models

 - [AmazonInteractiveVideoServiceChat.ChatTokenCapability](docs/ChatTokenCapability.md)
 - [AmazonInteractiveVideoServiceChat.CloudWatchLogsDestinationConfiguration](docs/CloudWatchLogsDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.CreateChatTokenRequest](docs/CreateChatTokenRequest.md)
 - [AmazonInteractiveVideoServiceChat.CreateChatTokenResponse](docs/CreateChatTokenResponse.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationRequest](docs/CreateLoggingConfigurationRequest.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationRequestDestinationConfiguration](docs/CreateLoggingConfigurationRequestDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs](docs/CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationRequestDestinationConfigurationFirehose](docs/CreateLoggingConfigurationRequestDestinationConfigurationFirehose.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationRequestDestinationConfigurationS3](docs/CreateLoggingConfigurationRequestDestinationConfigurationS3.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationResponse](docs/CreateLoggingConfigurationResponse.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationResponseDestinationConfiguration](docs/CreateLoggingConfigurationResponseDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.CreateLoggingConfigurationState](docs/CreateLoggingConfigurationState.md)
 - [AmazonInteractiveVideoServiceChat.CreateRoomRequest](docs/CreateRoomRequest.md)
 - [AmazonInteractiveVideoServiceChat.CreateRoomRequestMessageReviewHandler](docs/CreateRoomRequestMessageReviewHandler.md)
 - [AmazonInteractiveVideoServiceChat.CreateRoomResponse](docs/CreateRoomResponse.md)
 - [AmazonInteractiveVideoServiceChat.CreateRoomResponseMessageReviewHandler](docs/CreateRoomResponseMessageReviewHandler.md)
 - [AmazonInteractiveVideoServiceChat.DeleteLoggingConfigurationRequest](docs/DeleteLoggingConfigurationRequest.md)
 - [AmazonInteractiveVideoServiceChat.DeleteMessageRequest](docs/DeleteMessageRequest.md)
 - [AmazonInteractiveVideoServiceChat.DeleteMessageResponse](docs/DeleteMessageResponse.md)
 - [AmazonInteractiveVideoServiceChat.DeleteRoomRequest](docs/DeleteRoomRequest.md)
 - [AmazonInteractiveVideoServiceChat.DestinationConfiguration](docs/DestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.DisconnectUserRequest](docs/DisconnectUserRequest.md)
 - [AmazonInteractiveVideoServiceChat.FallbackResult](docs/FallbackResult.md)
 - [AmazonInteractiveVideoServiceChat.FirehoseDestinationConfiguration](docs/FirehoseDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.GetLoggingConfigurationRequest](docs/GetLoggingConfigurationRequest.md)
 - [AmazonInteractiveVideoServiceChat.GetLoggingConfigurationResponse](docs/GetLoggingConfigurationResponse.md)
 - [AmazonInteractiveVideoServiceChat.GetLoggingConfigurationResponseDestinationConfiguration](docs/GetLoggingConfigurationResponseDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.GetRoomRequest](docs/GetRoomRequest.md)
 - [AmazonInteractiveVideoServiceChat.GetRoomResponse](docs/GetRoomResponse.md)
 - [AmazonInteractiveVideoServiceChat.ListLoggingConfigurationsRequest](docs/ListLoggingConfigurationsRequest.md)
 - [AmazonInteractiveVideoServiceChat.ListLoggingConfigurationsResponse](docs/ListLoggingConfigurationsResponse.md)
 - [AmazonInteractiveVideoServiceChat.ListRoomsRequest](docs/ListRoomsRequest.md)
 - [AmazonInteractiveVideoServiceChat.ListRoomsResponse](docs/ListRoomsResponse.md)
 - [AmazonInteractiveVideoServiceChat.ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [AmazonInteractiveVideoServiceChat.LoggingConfigurationState](docs/LoggingConfigurationState.md)
 - [AmazonInteractiveVideoServiceChat.LoggingConfigurationSummary](docs/LoggingConfigurationSummary.md)
 - [AmazonInteractiveVideoServiceChat.LoggingConfigurationSummaryDestinationConfiguration](docs/LoggingConfigurationSummaryDestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.MessageReviewHandler](docs/MessageReviewHandler.md)
 - [AmazonInteractiveVideoServiceChat.RoomSummary](docs/RoomSummary.md)
 - [AmazonInteractiveVideoServiceChat.S3DestinationConfiguration](docs/S3DestinationConfiguration.md)
 - [AmazonInteractiveVideoServiceChat.SendEventRequest](docs/SendEventRequest.md)
 - [AmazonInteractiveVideoServiceChat.SendEventResponse](docs/SendEventResponse.md)
 - [AmazonInteractiveVideoServiceChat.TagResourceRequest](docs/TagResourceRequest.md)
 - [AmazonInteractiveVideoServiceChat.UpdateLoggingConfigurationRequest](docs/UpdateLoggingConfigurationRequest.md)
 - [AmazonInteractiveVideoServiceChat.UpdateLoggingConfigurationResponse](docs/UpdateLoggingConfigurationResponse.md)
 - [AmazonInteractiveVideoServiceChat.UpdateLoggingConfigurationState](docs/UpdateLoggingConfigurationState.md)
 - [AmazonInteractiveVideoServiceChat.UpdateRoomRequest](docs/UpdateRoomRequest.md)
 - [AmazonInteractiveVideoServiceChat.UpdateRoomRequestMessageReviewHandler](docs/UpdateRoomRequestMessageReviewHandler.md)
 - [AmazonInteractiveVideoServiceChat.UpdateRoomResponse](docs/UpdateRoomResponse.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

