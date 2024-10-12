# openapi-java-client

Amazon Interactive Video Service Chat
- API version: 2020-07-14
  - Build date: 2024-10-12T12:28:20.323587-04:00[America/New_York]
  - Generator version: 7.9.0

<p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>

  For more information, please visit [https://github.com/mermade/aws2openapi](https://github.com/mermade/aws2openapi)

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>2020-07-14</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:2020-07-14"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2020-07-14.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://ivschat.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateChatTokenRequest createChatTokenRequest = new CreateChatTokenRequest(); // CreateChatTokenRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChatTokenResponse result = apiInstance.createChatToken(createChatTokenRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChatToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://ivschat.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**createChatToken**](docs/DefaultApi.md#createChatToken) | **POST** /CreateChatToken | 
*DefaultApi* | [**createLoggingConfiguration**](docs/DefaultApi.md#createLoggingConfiguration) | **POST** /CreateLoggingConfiguration | 
*DefaultApi* | [**createRoom**](docs/DefaultApi.md#createRoom) | **POST** /CreateRoom | 
*DefaultApi* | [**deleteLoggingConfiguration**](docs/DefaultApi.md#deleteLoggingConfiguration) | **POST** /DeleteLoggingConfiguration | 
*DefaultApi* | [**deleteMessage**](docs/DefaultApi.md#deleteMessage) | **POST** /DeleteMessage | 
*DefaultApi* | [**deleteRoom**](docs/DefaultApi.md#deleteRoom) | **POST** /DeleteRoom | 
*DefaultApi* | [**disconnectUser**](docs/DefaultApi.md#disconnectUser) | **POST** /DisconnectUser | 
*DefaultApi* | [**getLoggingConfiguration**](docs/DefaultApi.md#getLoggingConfiguration) | **POST** /GetLoggingConfiguration | 
*DefaultApi* | [**getRoom**](docs/DefaultApi.md#getRoom) | **POST** /GetRoom | 
*DefaultApi* | [**listLoggingConfigurations**](docs/DefaultApi.md#listLoggingConfigurations) | **POST** /ListLoggingConfigurations | 
*DefaultApi* | [**listRooms**](docs/DefaultApi.md#listRooms) | **POST** /ListRooms | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*DefaultApi* | [**sendEvent**](docs/DefaultApi.md#sendEvent) | **POST** /SendEvent | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*DefaultApi* | [**updateLoggingConfiguration**](docs/DefaultApi.md#updateLoggingConfiguration) | **POST** /UpdateLoggingConfiguration | 
*DefaultApi* | [**updateRoom**](docs/DefaultApi.md#updateRoom) | **POST** /UpdateRoom | 


## Documentation for Models

 - [ChatTokenCapability](docs/ChatTokenCapability.md)
 - [CloudWatchLogsDestinationConfiguration](docs/CloudWatchLogsDestinationConfiguration.md)
 - [CreateChatTokenRequest](docs/CreateChatTokenRequest.md)
 - [CreateChatTokenResponse](docs/CreateChatTokenResponse.md)
 - [CreateLoggingConfigurationRequest](docs/CreateLoggingConfigurationRequest.md)
 - [CreateLoggingConfigurationRequestDestinationConfiguration](docs/CreateLoggingConfigurationRequestDestinationConfiguration.md)
 - [CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs](docs/CreateLoggingConfigurationRequestDestinationConfigurationCloudWatchLogs.md)
 - [CreateLoggingConfigurationRequestDestinationConfigurationFirehose](docs/CreateLoggingConfigurationRequestDestinationConfigurationFirehose.md)
 - [CreateLoggingConfigurationRequestDestinationConfigurationS3](docs/CreateLoggingConfigurationRequestDestinationConfigurationS3.md)
 - [CreateLoggingConfigurationResponse](docs/CreateLoggingConfigurationResponse.md)
 - [CreateLoggingConfigurationResponseDestinationConfiguration](docs/CreateLoggingConfigurationResponseDestinationConfiguration.md)
 - [CreateLoggingConfigurationState](docs/CreateLoggingConfigurationState.md)
 - [CreateRoomRequest](docs/CreateRoomRequest.md)
 - [CreateRoomRequestMessageReviewHandler](docs/CreateRoomRequestMessageReviewHandler.md)
 - [CreateRoomResponse](docs/CreateRoomResponse.md)
 - [CreateRoomResponseMessageReviewHandler](docs/CreateRoomResponseMessageReviewHandler.md)
 - [DeleteLoggingConfigurationRequest](docs/DeleteLoggingConfigurationRequest.md)
 - [DeleteMessageRequest](docs/DeleteMessageRequest.md)
 - [DeleteMessageResponse](docs/DeleteMessageResponse.md)
 - [DeleteRoomRequest](docs/DeleteRoomRequest.md)
 - [DestinationConfiguration](docs/DestinationConfiguration.md)
 - [DisconnectUserRequest](docs/DisconnectUserRequest.md)
 - [FallbackResult](docs/FallbackResult.md)
 - [FirehoseDestinationConfiguration](docs/FirehoseDestinationConfiguration.md)
 - [GetLoggingConfigurationRequest](docs/GetLoggingConfigurationRequest.md)
 - [GetLoggingConfigurationResponse](docs/GetLoggingConfigurationResponse.md)
 - [GetLoggingConfigurationResponseDestinationConfiguration](docs/GetLoggingConfigurationResponseDestinationConfiguration.md)
 - [GetRoomRequest](docs/GetRoomRequest.md)
 - [GetRoomResponse](docs/GetRoomResponse.md)
 - [ListLoggingConfigurationsRequest](docs/ListLoggingConfigurationsRequest.md)
 - [ListLoggingConfigurationsResponse](docs/ListLoggingConfigurationsResponse.md)
 - [ListRoomsRequest](docs/ListRoomsRequest.md)
 - [ListRoomsResponse](docs/ListRoomsResponse.md)
 - [ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [LoggingConfigurationState](docs/LoggingConfigurationState.md)
 - [LoggingConfigurationSummary](docs/LoggingConfigurationSummary.md)
 - [LoggingConfigurationSummaryDestinationConfiguration](docs/LoggingConfigurationSummaryDestinationConfiguration.md)
 - [MessageReviewHandler](docs/MessageReviewHandler.md)
 - [RoomSummary](docs/RoomSummary.md)
 - [S3DestinationConfiguration](docs/S3DestinationConfiguration.md)
 - [SendEventRequest](docs/SendEventRequest.md)
 - [SendEventResponse](docs/SendEventResponse.md)
 - [TagResourceRequest](docs/TagResourceRequest.md)
 - [UpdateLoggingConfigurationRequest](docs/UpdateLoggingConfigurationRequest.md)
 - [UpdateLoggingConfigurationResponse](docs/UpdateLoggingConfigurationResponse.md)
 - [UpdateLoggingConfigurationState](docs/UpdateLoggingConfigurationState.md)
 - [UpdateRoomRequest](docs/UpdateRoomRequest.md)
 - [UpdateRoomRequestMessageReviewHandler](docs/UpdateRoomRequestMessageReviewHandler.md)
 - [UpdateRoomResponse](docs/UpdateRoomResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="hmac"></a>
### hmac

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author

mike.ralphson@gmail.com

