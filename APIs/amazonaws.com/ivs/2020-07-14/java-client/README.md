# openapi-java-client

Amazon Interactive Video Service
- API version: 2020-07-14
  - Build date: 2024-10-12T12:23:27.693454-04:00[America/New_York]
  - Generator version: 7.9.0

<p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>

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
    defaultClient.setBasePath("http://ivs.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BatchGetChannelRequest batchGetChannelRequest = new BatchGetChannelRequest(); // BatchGetChannelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchGetChannelResponse result = apiInstance.batchGetChannel(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchGetChannel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://ivs.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**batchGetChannel**](docs/DefaultApi.md#batchGetChannel) | **POST** /BatchGetChannel | 
*DefaultApi* | [**batchGetStreamKey**](docs/DefaultApi.md#batchGetStreamKey) | **POST** /BatchGetStreamKey | 
*DefaultApi* | [**batchStartViewerSessionRevocation**](docs/DefaultApi.md#batchStartViewerSessionRevocation) | **POST** /BatchStartViewerSessionRevocation | 
*DefaultApi* | [**createChannel**](docs/DefaultApi.md#createChannel) | **POST** /CreateChannel | 
*DefaultApi* | [**createRecordingConfiguration**](docs/DefaultApi.md#createRecordingConfiguration) | **POST** /CreateRecordingConfiguration | 
*DefaultApi* | [**createStreamKey**](docs/DefaultApi.md#createStreamKey) | **POST** /CreateStreamKey | 
*DefaultApi* | [**deleteChannel**](docs/DefaultApi.md#deleteChannel) | **POST** /DeleteChannel | 
*DefaultApi* | [**deletePlaybackKeyPair**](docs/DefaultApi.md#deletePlaybackKeyPair) | **POST** /DeletePlaybackKeyPair | 
*DefaultApi* | [**deleteRecordingConfiguration**](docs/DefaultApi.md#deleteRecordingConfiguration) | **POST** /DeleteRecordingConfiguration | 
*DefaultApi* | [**deleteStreamKey**](docs/DefaultApi.md#deleteStreamKey) | **POST** /DeleteStreamKey | 
*DefaultApi* | [**getChannel**](docs/DefaultApi.md#getChannel) | **POST** /GetChannel | 
*DefaultApi* | [**getPlaybackKeyPair**](docs/DefaultApi.md#getPlaybackKeyPair) | **POST** /GetPlaybackKeyPair | 
*DefaultApi* | [**getRecordingConfiguration**](docs/DefaultApi.md#getRecordingConfiguration) | **POST** /GetRecordingConfiguration | 
*DefaultApi* | [**getStream**](docs/DefaultApi.md#getStream) | **POST** /GetStream | 
*DefaultApi* | [**getStreamKey**](docs/DefaultApi.md#getStreamKey) | **POST** /GetStreamKey | 
*DefaultApi* | [**getStreamSession**](docs/DefaultApi.md#getStreamSession) | **POST** /GetStreamSession | 
*DefaultApi* | [**importPlaybackKeyPair**](docs/DefaultApi.md#importPlaybackKeyPair) | **POST** /ImportPlaybackKeyPair | 
*DefaultApi* | [**listChannels**](docs/DefaultApi.md#listChannels) | **POST** /ListChannels | 
*DefaultApi* | [**listPlaybackKeyPairs**](docs/DefaultApi.md#listPlaybackKeyPairs) | **POST** /ListPlaybackKeyPairs | 
*DefaultApi* | [**listRecordingConfigurations**](docs/DefaultApi.md#listRecordingConfigurations) | **POST** /ListRecordingConfigurations | 
*DefaultApi* | [**listStreamKeys**](docs/DefaultApi.md#listStreamKeys) | **POST** /ListStreamKeys | 
*DefaultApi* | [**listStreamSessions**](docs/DefaultApi.md#listStreamSessions) | **POST** /ListStreamSessions | 
*DefaultApi* | [**listStreams**](docs/DefaultApi.md#listStreams) | **POST** /ListStreams | 
*DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*DefaultApi* | [**putMetadata**](docs/DefaultApi.md#putMetadata) | **POST** /PutMetadata | 
*DefaultApi* | [**startViewerSessionRevocation**](docs/DefaultApi.md#startViewerSessionRevocation) | **POST** /StartViewerSessionRevocation | 
*DefaultApi* | [**stopStream**](docs/DefaultApi.md#stopStream) | **POST** /StopStream | 
*DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*DefaultApi* | [**updateChannel**](docs/DefaultApi.md#updateChannel) | **POST** /UpdateChannel | 


## Documentation for Models

 - [AudioConfiguration](docs/AudioConfiguration.md)
 - [BatchError](docs/BatchError.md)
 - [BatchGetChannelRequest](docs/BatchGetChannelRequest.md)
 - [BatchGetChannelResponse](docs/BatchGetChannelResponse.md)
 - [BatchGetStreamKeyRequest](docs/BatchGetStreamKeyRequest.md)
 - [BatchGetStreamKeyResponse](docs/BatchGetStreamKeyResponse.md)
 - [BatchStartViewerSessionRevocationError](docs/BatchStartViewerSessionRevocationError.md)
 - [BatchStartViewerSessionRevocationRequest](docs/BatchStartViewerSessionRevocationRequest.md)
 - [BatchStartViewerSessionRevocationResponse](docs/BatchStartViewerSessionRevocationResponse.md)
 - [BatchStartViewerSessionRevocationViewerSession](docs/BatchStartViewerSessionRevocationViewerSession.md)
 - [Channel](docs/Channel.md)
 - [ChannelLatencyMode](docs/ChannelLatencyMode.md)
 - [ChannelSummary](docs/ChannelSummary.md)
 - [ChannelType](docs/ChannelType.md)
 - [CreateChannelRequest](docs/CreateChannelRequest.md)
 - [CreateChannelResponse](docs/CreateChannelResponse.md)
 - [CreateChannelResponseChannel](docs/CreateChannelResponseChannel.md)
 - [CreateChannelResponseStreamKey](docs/CreateChannelResponseStreamKey.md)
 - [CreateRecordingConfigurationRequest](docs/CreateRecordingConfigurationRequest.md)
 - [CreateRecordingConfigurationRequestDestinationConfiguration](docs/CreateRecordingConfigurationRequestDestinationConfiguration.md)
 - [CreateRecordingConfigurationRequestDestinationConfigurationS3](docs/CreateRecordingConfigurationRequestDestinationConfigurationS3.md)
 - [CreateRecordingConfigurationRequestRenditionConfiguration](docs/CreateRecordingConfigurationRequestRenditionConfiguration.md)
 - [CreateRecordingConfigurationRequestThumbnailConfiguration](docs/CreateRecordingConfigurationRequestThumbnailConfiguration.md)
 - [CreateRecordingConfigurationResponse](docs/CreateRecordingConfigurationResponse.md)
 - [CreateRecordingConfigurationResponseRecordingConfiguration](docs/CreateRecordingConfigurationResponseRecordingConfiguration.md)
 - [CreateStreamKeyRequest](docs/CreateStreamKeyRequest.md)
 - [CreateStreamKeyResponse](docs/CreateStreamKeyResponse.md)
 - [CreateStreamKeyResponseStreamKey](docs/CreateStreamKeyResponseStreamKey.md)
 - [DeleteChannelRequest](docs/DeleteChannelRequest.md)
 - [DeletePlaybackKeyPairRequest](docs/DeletePlaybackKeyPairRequest.md)
 - [DeleteRecordingConfigurationRequest](docs/DeleteRecordingConfigurationRequest.md)
 - [DeleteStreamKeyRequest](docs/DeleteStreamKeyRequest.md)
 - [DestinationConfiguration](docs/DestinationConfiguration.md)
 - [GetChannelRequest](docs/GetChannelRequest.md)
 - [GetChannelResponse](docs/GetChannelResponse.md)
 - [GetPlaybackKeyPairRequest](docs/GetPlaybackKeyPairRequest.md)
 - [GetPlaybackKeyPairResponse](docs/GetPlaybackKeyPairResponse.md)
 - [GetPlaybackKeyPairResponseKeyPair](docs/GetPlaybackKeyPairResponseKeyPair.md)
 - [GetRecordingConfigurationRequest](docs/GetRecordingConfigurationRequest.md)
 - [GetRecordingConfigurationResponse](docs/GetRecordingConfigurationResponse.md)
 - [GetStreamKeyRequest](docs/GetStreamKeyRequest.md)
 - [GetStreamKeyResponse](docs/GetStreamKeyResponse.md)
 - [GetStreamKeyResponseStreamKey](docs/GetStreamKeyResponseStreamKey.md)
 - [GetStreamRequest](docs/GetStreamRequest.md)
 - [GetStreamResponse](docs/GetStreamResponse.md)
 - [GetStreamResponseStream](docs/GetStreamResponseStream.md)
 - [GetStreamSessionRequest](docs/GetStreamSessionRequest.md)
 - [GetStreamSessionResponse](docs/GetStreamSessionResponse.md)
 - [GetStreamSessionResponseStreamSession](docs/GetStreamSessionResponseStreamSession.md)
 - [ImportPlaybackKeyPairRequest](docs/ImportPlaybackKeyPairRequest.md)
 - [ImportPlaybackKeyPairResponse](docs/ImportPlaybackKeyPairResponse.md)
 - [ImportPlaybackKeyPairResponseKeyPair](docs/ImportPlaybackKeyPairResponseKeyPair.md)
 - [IngestConfiguration](docs/IngestConfiguration.md)
 - [IngestConfigurationAudio](docs/IngestConfigurationAudio.md)
 - [IngestConfigurationVideo](docs/IngestConfigurationVideo.md)
 - [ListChannelsRequest](docs/ListChannelsRequest.md)
 - [ListChannelsResponse](docs/ListChannelsResponse.md)
 - [ListPlaybackKeyPairsRequest](docs/ListPlaybackKeyPairsRequest.md)
 - [ListPlaybackKeyPairsResponse](docs/ListPlaybackKeyPairsResponse.md)
 - [ListRecordingConfigurationsRequest](docs/ListRecordingConfigurationsRequest.md)
 - [ListRecordingConfigurationsResponse](docs/ListRecordingConfigurationsResponse.md)
 - [ListStreamKeysRequest](docs/ListStreamKeysRequest.md)
 - [ListStreamKeysResponse](docs/ListStreamKeysResponse.md)
 - [ListStreamSessionsRequest](docs/ListStreamSessionsRequest.md)
 - [ListStreamSessionsResponse](docs/ListStreamSessionsResponse.md)
 - [ListStreamsRequest](docs/ListStreamsRequest.md)
 - [ListStreamsRequestFilterBy](docs/ListStreamsRequestFilterBy.md)
 - [ListStreamsResponse](docs/ListStreamsResponse.md)
 - [ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [PlaybackKeyPair](docs/PlaybackKeyPair.md)
 - [PlaybackKeyPairSummary](docs/PlaybackKeyPairSummary.md)
 - [PutMetadataRequest](docs/PutMetadataRequest.md)
 - [RecordingConfiguration](docs/RecordingConfiguration.md)
 - [RecordingConfigurationDestinationConfiguration](docs/RecordingConfigurationDestinationConfiguration.md)
 - [RecordingConfigurationState](docs/RecordingConfigurationState.md)
 - [RecordingConfigurationSummary](docs/RecordingConfigurationSummary.md)
 - [RecordingMode](docs/RecordingMode.md)
 - [RenditionConfiguration](docs/RenditionConfiguration.md)
 - [RenditionConfigurationRendition](docs/RenditionConfigurationRendition.md)
 - [RenditionConfigurationRenditionSelection](docs/RenditionConfigurationRenditionSelection.md)
 - [S3DestinationConfiguration](docs/S3DestinationConfiguration.md)
 - [StartViewerSessionRevocationRequest](docs/StartViewerSessionRevocationRequest.md)
 - [StopStreamRequest](docs/StopStreamRequest.md)
 - [Stream](docs/Stream.md)
 - [StreamEvent](docs/StreamEvent.md)
 - [StreamFilters](docs/StreamFilters.md)
 - [StreamHealth](docs/StreamHealth.md)
 - [StreamKey](docs/StreamKey.md)
 - [StreamKeySummary](docs/StreamKeySummary.md)
 - [StreamSession](docs/StreamSession.md)
 - [StreamSessionChannel](docs/StreamSessionChannel.md)
 - [StreamSessionIngestConfiguration](docs/StreamSessionIngestConfiguration.md)
 - [StreamSessionRecordingConfiguration](docs/StreamSessionRecordingConfiguration.md)
 - [StreamSessionSummary](docs/StreamSessionSummary.md)
 - [StreamState](docs/StreamState.md)
 - [StreamSummary](docs/StreamSummary.md)
 - [TagResourceRequest](docs/TagResourceRequest.md)
 - [ThumbnailConfiguration](docs/ThumbnailConfiguration.md)
 - [ThumbnailConfigurationResolution](docs/ThumbnailConfigurationResolution.md)
 - [ThumbnailConfigurationStorage](docs/ThumbnailConfigurationStorage.md)
 - [TranscodePreset](docs/TranscodePreset.md)
 - [UpdateChannelRequest](docs/UpdateChannelRequest.md)
 - [UpdateChannelResponse](docs/UpdateChannelResponse.md)
 - [VideoConfiguration](docs/VideoConfiguration.md)


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

