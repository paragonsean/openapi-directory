# amazon_interactive_video_service

AmazonInteractiveVideoService - JavaScript client for amazon_interactive_video_service
<p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>
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
npm install amazon_interactive_video_service --save
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

To use the link you just defined in your project, switch to the directory you want to use your amazon_interactive_video_service from, and run:

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
var AmazonInteractiveVideoService = require('amazon_interactive_video_service');

var defaultClient = AmazonInteractiveVideoService.ApiClient.instance;
// Configure API key authorization: hmac
var hmac = defaultClient.authentications['hmac'];
hmac.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix['Authorization'] = "Token"

var api = new AmazonInteractiveVideoService.DefaultApi()
var batchGetChannelRequest = new AmazonInteractiveVideoService.BatchGetChannelRequest(); // {BatchGetChannelRequest} 
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
api.batchGetChannel(batchGetChannelRequest, opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://ivs.us-east-1.amazonaws.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AmazonInteractiveVideoService.DefaultApi* | [**batchGetChannel**](docs/DefaultApi.md#batchGetChannel) | **POST** /BatchGetChannel | 
*AmazonInteractiveVideoService.DefaultApi* | [**batchGetStreamKey**](docs/DefaultApi.md#batchGetStreamKey) | **POST** /BatchGetStreamKey | 
*AmazonInteractiveVideoService.DefaultApi* | [**batchStartViewerSessionRevocation**](docs/DefaultApi.md#batchStartViewerSessionRevocation) | **POST** /BatchStartViewerSessionRevocation | 
*AmazonInteractiveVideoService.DefaultApi* | [**createChannel**](docs/DefaultApi.md#createChannel) | **POST** /CreateChannel | 
*AmazonInteractiveVideoService.DefaultApi* | [**createRecordingConfiguration**](docs/DefaultApi.md#createRecordingConfiguration) | **POST** /CreateRecordingConfiguration | 
*AmazonInteractiveVideoService.DefaultApi* | [**createStreamKey**](docs/DefaultApi.md#createStreamKey) | **POST** /CreateStreamKey | 
*AmazonInteractiveVideoService.DefaultApi* | [**deleteChannel**](docs/DefaultApi.md#deleteChannel) | **POST** /DeleteChannel | 
*AmazonInteractiveVideoService.DefaultApi* | [**deletePlaybackKeyPair**](docs/DefaultApi.md#deletePlaybackKeyPair) | **POST** /DeletePlaybackKeyPair | 
*AmazonInteractiveVideoService.DefaultApi* | [**deleteRecordingConfiguration**](docs/DefaultApi.md#deleteRecordingConfiguration) | **POST** /DeleteRecordingConfiguration | 
*AmazonInteractiveVideoService.DefaultApi* | [**deleteStreamKey**](docs/DefaultApi.md#deleteStreamKey) | **POST** /DeleteStreamKey | 
*AmazonInteractiveVideoService.DefaultApi* | [**getChannel**](docs/DefaultApi.md#getChannel) | **POST** /GetChannel | 
*AmazonInteractiveVideoService.DefaultApi* | [**getPlaybackKeyPair**](docs/DefaultApi.md#getPlaybackKeyPair) | **POST** /GetPlaybackKeyPair | 
*AmazonInteractiveVideoService.DefaultApi* | [**getRecordingConfiguration**](docs/DefaultApi.md#getRecordingConfiguration) | **POST** /GetRecordingConfiguration | 
*AmazonInteractiveVideoService.DefaultApi* | [**getStream**](docs/DefaultApi.md#getStream) | **POST** /GetStream | 
*AmazonInteractiveVideoService.DefaultApi* | [**getStreamKey**](docs/DefaultApi.md#getStreamKey) | **POST** /GetStreamKey | 
*AmazonInteractiveVideoService.DefaultApi* | [**getStreamSession**](docs/DefaultApi.md#getStreamSession) | **POST** /GetStreamSession | 
*AmazonInteractiveVideoService.DefaultApi* | [**importPlaybackKeyPair**](docs/DefaultApi.md#importPlaybackKeyPair) | **POST** /ImportPlaybackKeyPair | 
*AmazonInteractiveVideoService.DefaultApi* | [**listChannels**](docs/DefaultApi.md#listChannels) | **POST** /ListChannels | 
*AmazonInteractiveVideoService.DefaultApi* | [**listPlaybackKeyPairs**](docs/DefaultApi.md#listPlaybackKeyPairs) | **POST** /ListPlaybackKeyPairs | 
*AmazonInteractiveVideoService.DefaultApi* | [**listRecordingConfigurations**](docs/DefaultApi.md#listRecordingConfigurations) | **POST** /ListRecordingConfigurations | 
*AmazonInteractiveVideoService.DefaultApi* | [**listStreamKeys**](docs/DefaultApi.md#listStreamKeys) | **POST** /ListStreamKeys | 
*AmazonInteractiveVideoService.DefaultApi* | [**listStreamSessions**](docs/DefaultApi.md#listStreamSessions) | **POST** /ListStreamSessions | 
*AmazonInteractiveVideoService.DefaultApi* | [**listStreams**](docs/DefaultApi.md#listStreams) | **POST** /ListStreams | 
*AmazonInteractiveVideoService.DefaultApi* | [**listTagsForResource**](docs/DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
*AmazonInteractiveVideoService.DefaultApi* | [**putMetadata**](docs/DefaultApi.md#putMetadata) | **POST** /PutMetadata | 
*AmazonInteractiveVideoService.DefaultApi* | [**startViewerSessionRevocation**](docs/DefaultApi.md#startViewerSessionRevocation) | **POST** /StartViewerSessionRevocation | 
*AmazonInteractiveVideoService.DefaultApi* | [**stopStream**](docs/DefaultApi.md#stopStream) | **POST** /StopStream | 
*AmazonInteractiveVideoService.DefaultApi* | [**tagResource**](docs/DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
*AmazonInteractiveVideoService.DefaultApi* | [**untagResource**](docs/DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
*AmazonInteractiveVideoService.DefaultApi* | [**updateChannel**](docs/DefaultApi.md#updateChannel) | **POST** /UpdateChannel | 


## Documentation for Models

 - [AmazonInteractiveVideoService.AudioConfiguration](docs/AudioConfiguration.md)
 - [AmazonInteractiveVideoService.BatchError](docs/BatchError.md)
 - [AmazonInteractiveVideoService.BatchGetChannelRequest](docs/BatchGetChannelRequest.md)
 - [AmazonInteractiveVideoService.BatchGetChannelResponse](docs/BatchGetChannelResponse.md)
 - [AmazonInteractiveVideoService.BatchGetStreamKeyRequest](docs/BatchGetStreamKeyRequest.md)
 - [AmazonInteractiveVideoService.BatchGetStreamKeyResponse](docs/BatchGetStreamKeyResponse.md)
 - [AmazonInteractiveVideoService.BatchStartViewerSessionRevocationError](docs/BatchStartViewerSessionRevocationError.md)
 - [AmazonInteractiveVideoService.BatchStartViewerSessionRevocationRequest](docs/BatchStartViewerSessionRevocationRequest.md)
 - [AmazonInteractiveVideoService.BatchStartViewerSessionRevocationResponse](docs/BatchStartViewerSessionRevocationResponse.md)
 - [AmazonInteractiveVideoService.BatchStartViewerSessionRevocationViewerSession](docs/BatchStartViewerSessionRevocationViewerSession.md)
 - [AmazonInteractiveVideoService.Channel](docs/Channel.md)
 - [AmazonInteractiveVideoService.ChannelLatencyMode](docs/ChannelLatencyMode.md)
 - [AmazonInteractiveVideoService.ChannelSummary](docs/ChannelSummary.md)
 - [AmazonInteractiveVideoService.ChannelType](docs/ChannelType.md)
 - [AmazonInteractiveVideoService.CreateChannelRequest](docs/CreateChannelRequest.md)
 - [AmazonInteractiveVideoService.CreateChannelResponse](docs/CreateChannelResponse.md)
 - [AmazonInteractiveVideoService.CreateChannelResponseChannel](docs/CreateChannelResponseChannel.md)
 - [AmazonInteractiveVideoService.CreateChannelResponseStreamKey](docs/CreateChannelResponseStreamKey.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationRequest](docs/CreateRecordingConfigurationRequest.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationRequestDestinationConfiguration](docs/CreateRecordingConfigurationRequestDestinationConfiguration.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationRequestDestinationConfigurationS3](docs/CreateRecordingConfigurationRequestDestinationConfigurationS3.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationRequestRenditionConfiguration](docs/CreateRecordingConfigurationRequestRenditionConfiguration.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationRequestThumbnailConfiguration](docs/CreateRecordingConfigurationRequestThumbnailConfiguration.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationResponse](docs/CreateRecordingConfigurationResponse.md)
 - [AmazonInteractiveVideoService.CreateRecordingConfigurationResponseRecordingConfiguration](docs/CreateRecordingConfigurationResponseRecordingConfiguration.md)
 - [AmazonInteractiveVideoService.CreateStreamKeyRequest](docs/CreateStreamKeyRequest.md)
 - [AmazonInteractiveVideoService.CreateStreamKeyResponse](docs/CreateStreamKeyResponse.md)
 - [AmazonInteractiveVideoService.CreateStreamKeyResponseStreamKey](docs/CreateStreamKeyResponseStreamKey.md)
 - [AmazonInteractiveVideoService.DeleteChannelRequest](docs/DeleteChannelRequest.md)
 - [AmazonInteractiveVideoService.DeletePlaybackKeyPairRequest](docs/DeletePlaybackKeyPairRequest.md)
 - [AmazonInteractiveVideoService.DeleteRecordingConfigurationRequest](docs/DeleteRecordingConfigurationRequest.md)
 - [AmazonInteractiveVideoService.DeleteStreamKeyRequest](docs/DeleteStreamKeyRequest.md)
 - [AmazonInteractiveVideoService.DestinationConfiguration](docs/DestinationConfiguration.md)
 - [AmazonInteractiveVideoService.GetChannelRequest](docs/GetChannelRequest.md)
 - [AmazonInteractiveVideoService.GetChannelResponse](docs/GetChannelResponse.md)
 - [AmazonInteractiveVideoService.GetPlaybackKeyPairRequest](docs/GetPlaybackKeyPairRequest.md)
 - [AmazonInteractiveVideoService.GetPlaybackKeyPairResponse](docs/GetPlaybackKeyPairResponse.md)
 - [AmazonInteractiveVideoService.GetPlaybackKeyPairResponseKeyPair](docs/GetPlaybackKeyPairResponseKeyPair.md)
 - [AmazonInteractiveVideoService.GetRecordingConfigurationRequest](docs/GetRecordingConfigurationRequest.md)
 - [AmazonInteractiveVideoService.GetRecordingConfigurationResponse](docs/GetRecordingConfigurationResponse.md)
 - [AmazonInteractiveVideoService.GetStreamKeyRequest](docs/GetStreamKeyRequest.md)
 - [AmazonInteractiveVideoService.GetStreamKeyResponse](docs/GetStreamKeyResponse.md)
 - [AmazonInteractiveVideoService.GetStreamKeyResponseStreamKey](docs/GetStreamKeyResponseStreamKey.md)
 - [AmazonInteractiveVideoService.GetStreamRequest](docs/GetStreamRequest.md)
 - [AmazonInteractiveVideoService.GetStreamResponse](docs/GetStreamResponse.md)
 - [AmazonInteractiveVideoService.GetStreamResponseStream](docs/GetStreamResponseStream.md)
 - [AmazonInteractiveVideoService.GetStreamSessionRequest](docs/GetStreamSessionRequest.md)
 - [AmazonInteractiveVideoService.GetStreamSessionResponse](docs/GetStreamSessionResponse.md)
 - [AmazonInteractiveVideoService.GetStreamSessionResponseStreamSession](docs/GetStreamSessionResponseStreamSession.md)
 - [AmazonInteractiveVideoService.ImportPlaybackKeyPairRequest](docs/ImportPlaybackKeyPairRequest.md)
 - [AmazonInteractiveVideoService.ImportPlaybackKeyPairResponse](docs/ImportPlaybackKeyPairResponse.md)
 - [AmazonInteractiveVideoService.ImportPlaybackKeyPairResponseKeyPair](docs/ImportPlaybackKeyPairResponseKeyPair.md)
 - [AmazonInteractiveVideoService.IngestConfiguration](docs/IngestConfiguration.md)
 - [AmazonInteractiveVideoService.IngestConfigurationAudio](docs/IngestConfigurationAudio.md)
 - [AmazonInteractiveVideoService.IngestConfigurationVideo](docs/IngestConfigurationVideo.md)
 - [AmazonInteractiveVideoService.ListChannelsRequest](docs/ListChannelsRequest.md)
 - [AmazonInteractiveVideoService.ListChannelsResponse](docs/ListChannelsResponse.md)
 - [AmazonInteractiveVideoService.ListPlaybackKeyPairsRequest](docs/ListPlaybackKeyPairsRequest.md)
 - [AmazonInteractiveVideoService.ListPlaybackKeyPairsResponse](docs/ListPlaybackKeyPairsResponse.md)
 - [AmazonInteractiveVideoService.ListRecordingConfigurationsRequest](docs/ListRecordingConfigurationsRequest.md)
 - [AmazonInteractiveVideoService.ListRecordingConfigurationsResponse](docs/ListRecordingConfigurationsResponse.md)
 - [AmazonInteractiveVideoService.ListStreamKeysRequest](docs/ListStreamKeysRequest.md)
 - [AmazonInteractiveVideoService.ListStreamKeysResponse](docs/ListStreamKeysResponse.md)
 - [AmazonInteractiveVideoService.ListStreamSessionsRequest](docs/ListStreamSessionsRequest.md)
 - [AmazonInteractiveVideoService.ListStreamSessionsResponse](docs/ListStreamSessionsResponse.md)
 - [AmazonInteractiveVideoService.ListStreamsRequest](docs/ListStreamsRequest.md)
 - [AmazonInteractiveVideoService.ListStreamsRequestFilterBy](docs/ListStreamsRequestFilterBy.md)
 - [AmazonInteractiveVideoService.ListStreamsResponse](docs/ListStreamsResponse.md)
 - [AmazonInteractiveVideoService.ListTagsForResourceResponse](docs/ListTagsForResourceResponse.md)
 - [AmazonInteractiveVideoService.PlaybackKeyPair](docs/PlaybackKeyPair.md)
 - [AmazonInteractiveVideoService.PlaybackKeyPairSummary](docs/PlaybackKeyPairSummary.md)
 - [AmazonInteractiveVideoService.PutMetadataRequest](docs/PutMetadataRequest.md)
 - [AmazonInteractiveVideoService.RecordingConfiguration](docs/RecordingConfiguration.md)
 - [AmazonInteractiveVideoService.RecordingConfigurationDestinationConfiguration](docs/RecordingConfigurationDestinationConfiguration.md)
 - [AmazonInteractiveVideoService.RecordingConfigurationState](docs/RecordingConfigurationState.md)
 - [AmazonInteractiveVideoService.RecordingConfigurationSummary](docs/RecordingConfigurationSummary.md)
 - [AmazonInteractiveVideoService.RecordingMode](docs/RecordingMode.md)
 - [AmazonInteractiveVideoService.RenditionConfiguration](docs/RenditionConfiguration.md)
 - [AmazonInteractiveVideoService.RenditionConfigurationRendition](docs/RenditionConfigurationRendition.md)
 - [AmazonInteractiveVideoService.RenditionConfigurationRenditionSelection](docs/RenditionConfigurationRenditionSelection.md)
 - [AmazonInteractiveVideoService.S3DestinationConfiguration](docs/S3DestinationConfiguration.md)
 - [AmazonInteractiveVideoService.StartViewerSessionRevocationRequest](docs/StartViewerSessionRevocationRequest.md)
 - [AmazonInteractiveVideoService.StopStreamRequest](docs/StopStreamRequest.md)
 - [AmazonInteractiveVideoService.Stream](docs/Stream.md)
 - [AmazonInteractiveVideoService.StreamEvent](docs/StreamEvent.md)
 - [AmazonInteractiveVideoService.StreamFilters](docs/StreamFilters.md)
 - [AmazonInteractiveVideoService.StreamHealth](docs/StreamHealth.md)
 - [AmazonInteractiveVideoService.StreamKey](docs/StreamKey.md)
 - [AmazonInteractiveVideoService.StreamKeySummary](docs/StreamKeySummary.md)
 - [AmazonInteractiveVideoService.StreamSession](docs/StreamSession.md)
 - [AmazonInteractiveVideoService.StreamSessionChannel](docs/StreamSessionChannel.md)
 - [AmazonInteractiveVideoService.StreamSessionIngestConfiguration](docs/StreamSessionIngestConfiguration.md)
 - [AmazonInteractiveVideoService.StreamSessionRecordingConfiguration](docs/StreamSessionRecordingConfiguration.md)
 - [AmazonInteractiveVideoService.StreamSessionSummary](docs/StreamSessionSummary.md)
 - [AmazonInteractiveVideoService.StreamState](docs/StreamState.md)
 - [AmazonInteractiveVideoService.StreamSummary](docs/StreamSummary.md)
 - [AmazonInteractiveVideoService.TagResourceRequest](docs/TagResourceRequest.md)
 - [AmazonInteractiveVideoService.ThumbnailConfiguration](docs/ThumbnailConfiguration.md)
 - [AmazonInteractiveVideoService.ThumbnailConfigurationResolution](docs/ThumbnailConfigurationResolution.md)
 - [AmazonInteractiveVideoService.ThumbnailConfigurationStorage](docs/ThumbnailConfigurationStorage.md)
 - [AmazonInteractiveVideoService.TranscodePreset](docs/TranscodePreset.md)
 - [AmazonInteractiveVideoService.UpdateChannelRequest](docs/UpdateChannelRequest.md)
 - [AmazonInteractiveVideoService.UpdateChannelResponse](docs/UpdateChannelResponse.md)
 - [AmazonInteractiveVideoService.VideoConfiguration](docs/VideoConfiguration.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### hmac


- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

