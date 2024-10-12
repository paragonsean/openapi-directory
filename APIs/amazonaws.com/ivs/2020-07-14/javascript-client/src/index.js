/**
 * Amazon Interactive Video Service
 * <p> <b>Introduction</b> </p> <p>The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.</p> <p>The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>Amazon Web Services General Reference</i>.</p> <p> <i> <b>All API request parameters and URLs are case sensitive. </b> </i> </p> <p>For a summary of notable documentation changes in each release, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\"> Document History</a>.</p> <p> <b>Allowed Header Values</b> </p> <ul> <li> <p> <code> <b>Accept:</b> </code> application/json</p> </li> <li> <p> <code> <b>Accept-Encoding:</b> </code> gzip, deflate</p> </li> <li> <p> <code> <b>Content-Type:</b> </code>application/json</p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources contain information about your IVS live stream (see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\"> Getting Started with Amazon IVS</a>):</p> <ul> <li> <p> <b>Channel</b> — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. </p> </li> <li> <p> <b>Stream key</b> — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. <i> <b>Treat the stream key like a secret, since it allows anyone to stream to the channel.</b> </i> </p> </li> <li> <p> <b>Playback key pair</b> — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.</p> </li> <li> <p> <b>Recording configuration</b> — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\"> Access Tags</a>). </p> <p>The Amazon IVS API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.</p> <p>At most 50 tags can be applied to a resource. </p> <p> <b>Authentication versus Authorization</b> </p> <p>Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Amazon IVS private channels</a>. (Private channels are channels that are enabled for \"playback authorization.\")</p> </li> </ul> <p> <b>Authentication</b> </p> <p>All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the <code>ivs:PutMetadata</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Channel Endpoints</b> </p> <ul> <li> <p> <a>CreateChannel</a> — Creates a new channel and an associated stream key to start streaming.</p> </li> <li> <p> <a>GetChannel</a> — Gets the channel configuration for the specified channel ARN.</p> </li> <li> <p> <a>BatchGetChannel</a> — Performs <a>GetChannel</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListChannels</a> — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).</p> </li> <li> <p> <a>UpdateChannel</a> — Updates a channel's configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.</p> </li> <li> <p> <a>DeleteChannel</a> — Deletes the specified channel.</p> </li> </ul> <p> <b>StreamKey Endpoints</b> </p> <ul> <li> <p> <a>CreateStreamKey</a> — Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> </li> <li> <p> <a>GetStreamKey</a> — Gets stream key information for the specified ARN.</p> </li> <li> <p> <a>BatchGetStreamKey</a> — Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.</p> </li> <li> <p> <a>ListStreamKeys</a> — Gets summary information about stream keys for the specified channel.</p> </li> <li> <p> <a>DeleteStreamKey</a> — Deletes the stream key for the specified ARN, so it can no longer be used to stream.</p> </li> </ul> <p> <b>Stream Endpoints</b> </p> <ul> <li> <p> <a>GetStream</a> — Gets information about the active (live) stream on a specified channel.</p> </li> <li> <p> <a>GetStreamSession</a> — Gets metadata on a specified stream.</p> </li> <li> <p> <a>ListStreams</a> — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>ListStreamSessions</a> — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.</p> </li> <li> <p> <a>StopStream</a> — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> </li> <li> <p> <a>PutMetadata</a> — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.</p> </li> </ul> <p> <b>Private Channel Endpoints</b> </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.</p> <ul> <li> <p> <a>ImportPlaybackKeyPair</a> — Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).</p> </li> <li> <p> <a>GetPlaybackKeyPair</a> — Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.</p> </li> <li> <p> <a>ListPlaybackKeyPairs</a> — Gets summary information about playback key pairs.</p> </li> <li> <p> <a>DeletePlaybackKeyPair</a> — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>.</p> </li> <li> <p> <a>StartViewerSessionRevocation</a> — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.</p> </li> <li> <p> <a>BatchStartViewerSessionRevocation</a> — Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.</p> </li> </ul> <p> <b>RecordingConfiguration Endpoints</b> </p> <ul> <li> <p> <a>CreateRecordingConfiguration</a> — Creates a new recording configuration, used to enable recording to Amazon S3.</p> </li> <li> <p> <a>GetRecordingConfiguration</a> — Gets the recording-configuration metadata for the specified ARN.</p> </li> <li> <p> <a>ListRecordingConfigurations</a> — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.</p> </li> <li> <p> <a>DeleteRecordingConfiguration</a> — Deletes the recording configuration for the specified ARN.</p> </li> </ul> <p> <b>Amazon Web Services Tags Endpoints</b> </p> <ul> <li> <p> <a>TagResource</a> — Adds or updates tags for the Amazon Web Services resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> <li> <p> <a>ListTagsForResource</a> — Gets information about Amazon Web Services tags for the specified ARN.</p> </li> </ul>
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
import AudioConfiguration from './model/AudioConfiguration';
import BatchError from './model/BatchError';
import BatchGetChannelRequest from './model/BatchGetChannelRequest';
import BatchGetChannelResponse from './model/BatchGetChannelResponse';
import BatchGetStreamKeyRequest from './model/BatchGetStreamKeyRequest';
import BatchGetStreamKeyResponse from './model/BatchGetStreamKeyResponse';
import BatchStartViewerSessionRevocationError from './model/BatchStartViewerSessionRevocationError';
import BatchStartViewerSessionRevocationRequest from './model/BatchStartViewerSessionRevocationRequest';
import BatchStartViewerSessionRevocationResponse from './model/BatchStartViewerSessionRevocationResponse';
import BatchStartViewerSessionRevocationViewerSession from './model/BatchStartViewerSessionRevocationViewerSession';
import Channel from './model/Channel';
import ChannelLatencyMode from './model/ChannelLatencyMode';
import ChannelSummary from './model/ChannelSummary';
import ChannelType from './model/ChannelType';
import CreateChannelRequest from './model/CreateChannelRequest';
import CreateChannelResponse from './model/CreateChannelResponse';
import CreateChannelResponseChannel from './model/CreateChannelResponseChannel';
import CreateChannelResponseStreamKey from './model/CreateChannelResponseStreamKey';
import CreateRecordingConfigurationRequest from './model/CreateRecordingConfigurationRequest';
import CreateRecordingConfigurationRequestDestinationConfiguration from './model/CreateRecordingConfigurationRequestDestinationConfiguration';
import CreateRecordingConfigurationRequestDestinationConfigurationS3 from './model/CreateRecordingConfigurationRequestDestinationConfigurationS3';
import CreateRecordingConfigurationRequestRenditionConfiguration from './model/CreateRecordingConfigurationRequestRenditionConfiguration';
import CreateRecordingConfigurationRequestThumbnailConfiguration from './model/CreateRecordingConfigurationRequestThumbnailConfiguration';
import CreateRecordingConfigurationResponse from './model/CreateRecordingConfigurationResponse';
import CreateRecordingConfigurationResponseRecordingConfiguration from './model/CreateRecordingConfigurationResponseRecordingConfiguration';
import CreateStreamKeyRequest from './model/CreateStreamKeyRequest';
import CreateStreamKeyResponse from './model/CreateStreamKeyResponse';
import CreateStreamKeyResponseStreamKey from './model/CreateStreamKeyResponseStreamKey';
import DeleteChannelRequest from './model/DeleteChannelRequest';
import DeletePlaybackKeyPairRequest from './model/DeletePlaybackKeyPairRequest';
import DeleteRecordingConfigurationRequest from './model/DeleteRecordingConfigurationRequest';
import DeleteStreamKeyRequest from './model/DeleteStreamKeyRequest';
import DestinationConfiguration from './model/DestinationConfiguration';
import GetChannelRequest from './model/GetChannelRequest';
import GetChannelResponse from './model/GetChannelResponse';
import GetPlaybackKeyPairRequest from './model/GetPlaybackKeyPairRequest';
import GetPlaybackKeyPairResponse from './model/GetPlaybackKeyPairResponse';
import GetPlaybackKeyPairResponseKeyPair from './model/GetPlaybackKeyPairResponseKeyPair';
import GetRecordingConfigurationRequest from './model/GetRecordingConfigurationRequest';
import GetRecordingConfigurationResponse from './model/GetRecordingConfigurationResponse';
import GetStreamKeyRequest from './model/GetStreamKeyRequest';
import GetStreamKeyResponse from './model/GetStreamKeyResponse';
import GetStreamKeyResponseStreamKey from './model/GetStreamKeyResponseStreamKey';
import GetStreamRequest from './model/GetStreamRequest';
import GetStreamResponse from './model/GetStreamResponse';
import GetStreamResponseStream from './model/GetStreamResponseStream';
import GetStreamSessionRequest from './model/GetStreamSessionRequest';
import GetStreamSessionResponse from './model/GetStreamSessionResponse';
import GetStreamSessionResponseStreamSession from './model/GetStreamSessionResponseStreamSession';
import ImportPlaybackKeyPairRequest from './model/ImportPlaybackKeyPairRequest';
import ImportPlaybackKeyPairResponse from './model/ImportPlaybackKeyPairResponse';
import ImportPlaybackKeyPairResponseKeyPair from './model/ImportPlaybackKeyPairResponseKeyPair';
import IngestConfiguration from './model/IngestConfiguration';
import IngestConfigurationAudio from './model/IngestConfigurationAudio';
import IngestConfigurationVideo from './model/IngestConfigurationVideo';
import ListChannelsRequest from './model/ListChannelsRequest';
import ListChannelsResponse from './model/ListChannelsResponse';
import ListPlaybackKeyPairsRequest from './model/ListPlaybackKeyPairsRequest';
import ListPlaybackKeyPairsResponse from './model/ListPlaybackKeyPairsResponse';
import ListRecordingConfigurationsRequest from './model/ListRecordingConfigurationsRequest';
import ListRecordingConfigurationsResponse from './model/ListRecordingConfigurationsResponse';
import ListStreamKeysRequest from './model/ListStreamKeysRequest';
import ListStreamKeysResponse from './model/ListStreamKeysResponse';
import ListStreamSessionsRequest from './model/ListStreamSessionsRequest';
import ListStreamSessionsResponse from './model/ListStreamSessionsResponse';
import ListStreamsRequest from './model/ListStreamsRequest';
import ListStreamsRequestFilterBy from './model/ListStreamsRequestFilterBy';
import ListStreamsResponse from './model/ListStreamsResponse';
import ListTagsForResourceResponse from './model/ListTagsForResourceResponse';
import PlaybackKeyPair from './model/PlaybackKeyPair';
import PlaybackKeyPairSummary from './model/PlaybackKeyPairSummary';
import PutMetadataRequest from './model/PutMetadataRequest';
import RecordingConfiguration from './model/RecordingConfiguration';
import RecordingConfigurationDestinationConfiguration from './model/RecordingConfigurationDestinationConfiguration';
import RecordingConfigurationState from './model/RecordingConfigurationState';
import RecordingConfigurationSummary from './model/RecordingConfigurationSummary';
import RecordingMode from './model/RecordingMode';
import RenditionConfiguration from './model/RenditionConfiguration';
import RenditionConfigurationRendition from './model/RenditionConfigurationRendition';
import RenditionConfigurationRenditionSelection from './model/RenditionConfigurationRenditionSelection';
import S3DestinationConfiguration from './model/S3DestinationConfiguration';
import StartViewerSessionRevocationRequest from './model/StartViewerSessionRevocationRequest';
import StopStreamRequest from './model/StopStreamRequest';
import Stream from './model/Stream';
import StreamEvent from './model/StreamEvent';
import StreamFilters from './model/StreamFilters';
import StreamHealth from './model/StreamHealth';
import StreamKey from './model/StreamKey';
import StreamKeySummary from './model/StreamKeySummary';
import StreamSession from './model/StreamSession';
import StreamSessionChannel from './model/StreamSessionChannel';
import StreamSessionIngestConfiguration from './model/StreamSessionIngestConfiguration';
import StreamSessionRecordingConfiguration from './model/StreamSessionRecordingConfiguration';
import StreamSessionSummary from './model/StreamSessionSummary';
import StreamState from './model/StreamState';
import StreamSummary from './model/StreamSummary';
import TagResourceRequest from './model/TagResourceRequest';
import ThumbnailConfiguration from './model/ThumbnailConfiguration';
import ThumbnailConfigurationResolution from './model/ThumbnailConfigurationResolution';
import ThumbnailConfigurationStorage from './model/ThumbnailConfigurationStorage';
import TranscodePreset from './model/TranscodePreset';
import UpdateChannelRequest from './model/UpdateChannelRequest';
import UpdateChannelResponse from './model/UpdateChannelResponse';
import VideoConfiguration from './model/VideoConfiguration';
import DefaultApi from './api/DefaultApi';


/**
* &lt;p&gt; &lt;b&gt;Introduction&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The Amazon Interactive Video Service (IVS) API is REST compatible, using a standard HTTP API and an Amazon Web Services EventBridge event stream for responses. JSON is used for both requests and responses, including errors.&lt;/p&gt; &lt;p&gt;The API is an Amazon Web Services regional service. For a list of supported regions and Amazon IVS HTTPS service endpoints, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/ivs.html\&quot;&gt;Amazon IVS page&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;i&gt; &lt;b&gt;All API request parameters and URLs are case sensitive. &lt;/b&gt; &lt;/i&gt; &lt;/p&gt; &lt;p&gt;For a summary of notable documentation changes in each release, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/doc-history.html\&quot;&gt; Document History&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Allowed Header Values&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;b&gt;Accept:&lt;/b&gt; &lt;/code&gt; application/json&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;b&gt;Accept-Encoding:&lt;/b&gt; &lt;/code&gt; gzip, deflate&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; &lt;b&gt;Content-Type:&lt;/b&gt; &lt;/code&gt;application/json&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Resources&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The following resources contain information about your IVS live stream (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/getting-started.html\&quot;&gt; Getting Started with Amazon IVS&lt;/a&gt;):&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Channel&lt;/b&gt; — Stores configuration data related to your live stream. You first create a channel and then use the channel’s stream key to start your live stream. See the Channel endpoints for more information. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Stream key&lt;/b&gt; — An identifier assigned by Amazon IVS when you create a channel, which is then used to authorize streaming. See the StreamKey endpoints for more information. &lt;i&gt; &lt;b&gt;Treat the stream key like a secret, since it allows anyone to stream to the channel.&lt;/b&gt; &lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Playback key pair&lt;/b&gt; — Video playback may be restricted using playback-authorization tokens, which use public-key encryption. A playback key pair is the public-private pair of keys used to sign and validate the playback-authorization token. See the PlaybackKeyPair endpoints for more information.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Recording configuration&lt;/b&gt; — Stores configuration related to recording a live stream and where to store the recorded content. Multiple channels can reference the same recording configuration. See the Recording Configuration endpoints for more information.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Tagging&lt;/b&gt; &lt;/p&gt; &lt;p&gt;A &lt;i&gt;tag&lt;/i&gt; is a metadata label that you assign to an Amazon Web Services resource. A tag comprises a &lt;i&gt;key&lt;/i&gt; and a &lt;i&gt;value&lt;/i&gt;, both set by you. For example, you might set a tag as &lt;code&gt;topic:nature&lt;/code&gt; to label a particular video category. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there.&lt;/p&gt; &lt;p&gt;Tags can help you identify and organize your Amazon Web Services resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt; Access Tags&lt;/a&gt;). &lt;/p&gt; &lt;p&gt;The Amazon IVS API has these tag-related endpoints: &lt;a&gt;TagResource&lt;/a&gt;, &lt;a&gt;UntagResource&lt;/a&gt;, and &lt;a&gt;ListTagsForResource&lt;/a&gt;. The following resources support tagging: Channels, Stream Keys, Playback Key Pairs, and Recording Configurations.&lt;/p&gt; &lt;p&gt;At most 50 tags can be applied to a resource. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Authentication versus Authorization&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Note the differences between these concepts:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Authentication&lt;/i&gt; is about verifying identity. You need to be authenticated to sign Amazon IVS API requests.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Authorization&lt;/i&gt; is about granting permissions. Your IAM roles need to have permissions for Amazon IVS API requests. In addition, authorization is needed to view &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Amazon IVS private channels&lt;/a&gt;. (Private channels are channels that are enabled for \&quot;playback authorization.\&quot;)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Authentication&lt;/b&gt; &lt;/p&gt; &lt;p&gt;All Amazon IVS API requests must be authenticated with a signature. The Amazon Web Services Command-Line Interface (CLI) and Amazon IVS Player SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS API directly, it’s your responsibility to sign the requests.&lt;/p&gt; &lt;p&gt;You generate a signature using valid Amazon Web Services credentials that have permission to perform the requested action. For example, you must sign PutMetadata requests with a signature generated from a user account that has the &lt;code&gt;ivs:PutMetadata&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;For more information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Authentication and generating signatures — See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\&quot;&gt;Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Managing Amazon IVS permissions — See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\&quot;&gt;Identity and Access Management&lt;/a&gt; on the Security page of the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Amazon Resource Names (ARNs)&lt;/b&gt; &lt;/p&gt; &lt;p&gt;ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Channel Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateChannel&lt;/a&gt; — Creates a new channel and an associated stream key to start streaming.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetChannel&lt;/a&gt; — Gets the channel configuration for the specified channel ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchGetChannel&lt;/a&gt; — Performs &lt;a&gt;GetChannel&lt;/a&gt; on multiple ARNs simultaneously.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListChannels&lt;/a&gt; — Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 Conflict Exception).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UpdateChannel&lt;/a&gt; — Updates a channel&#39;s configuration. This does not affect an ongoing stream of this channel. You must stop and restart the stream for the changes to take effect.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteChannel&lt;/a&gt; — Deletes the specified channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;StreamKey Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateStreamKey&lt;/a&gt; — Creates a stream key, used to initiate a stream, for the specified channel ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetStreamKey&lt;/a&gt; — Gets stream key information for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchGetStreamKey&lt;/a&gt; — Performs &lt;a&gt;GetStreamKey&lt;/a&gt; on multiple ARNs simultaneously.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStreamKeys&lt;/a&gt; — Gets summary information about stream keys for the specified channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteStreamKey&lt;/a&gt; — Deletes the stream key for the specified ARN, so it can no longer be used to stream.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Stream Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetStream&lt;/a&gt; — Gets information about the active (live) stream on a specified channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetStreamSession&lt;/a&gt; — Gets metadata on a specified stream.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStreams&lt;/a&gt; — Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListStreamSessions&lt;/a&gt; — Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;StopStream&lt;/a&gt; — Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with &lt;a&gt;DeleteStreamKey&lt;/a&gt; to prevent further streaming to a channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutMetadata&lt;/a&gt; — Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Private Channel Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ImportPlaybackKeyPair&lt;/a&gt; — Imports the public portion of a new key pair and returns its &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; can then be used to generate viewer authorization tokens, to grant viewers access to private channels (channels enabled for playback authorization).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetPlaybackKeyPair&lt;/a&gt; — Gets a specified playback authorization key pair and returns the &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListPlaybackKeyPairs&lt;/a&gt; — Gets summary information about playback key pairs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeletePlaybackKeyPair&lt;/a&gt; — Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s &lt;code&gt;privateKey&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; — Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;BatchStartViewerSessionRevocation&lt;/a&gt; — Performs &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; on multiple channel ARN and viewer ID pairs simultaneously.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;RecordingConfiguration Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateRecordingConfiguration&lt;/a&gt; — Creates a new recording configuration, used to enable recording to Amazon S3.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetRecordingConfiguration&lt;/a&gt; — Gets the recording-configuration metadata for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListRecordingConfigurations&lt;/a&gt; — Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteRecordingConfiguration&lt;/a&gt; — Deletes the recording configuration for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Amazon Web Services Tags Endpoints&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TagResource&lt;/a&gt; — Adds or updates tags for the Amazon Web Services resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;UntagResource&lt;/a&gt; — Removes tags from the resource with the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListTagsForResource&lt;/a&gt; — Gets information about Amazon Web Services tags for the specified ARN.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var AmazonInteractiveVideoService = require('index'); // See note below*.
* var xxxSvc = new AmazonInteractiveVideoService.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new AmazonInteractiveVideoService.Yyy(); // Construct a model instance.
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
* var xxxSvc = new AmazonInteractiveVideoService.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new AmazonInteractiveVideoService.Yyy(); // Construct a model instance.
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
     * The AudioConfiguration model constructor.
     * @property {module:model/AudioConfiguration}
     */
    AudioConfiguration,

    /**
     * The BatchError model constructor.
     * @property {module:model/BatchError}
     */
    BatchError,

    /**
     * The BatchGetChannelRequest model constructor.
     * @property {module:model/BatchGetChannelRequest}
     */
    BatchGetChannelRequest,

    /**
     * The BatchGetChannelResponse model constructor.
     * @property {module:model/BatchGetChannelResponse}
     */
    BatchGetChannelResponse,

    /**
     * The BatchGetStreamKeyRequest model constructor.
     * @property {module:model/BatchGetStreamKeyRequest}
     */
    BatchGetStreamKeyRequest,

    /**
     * The BatchGetStreamKeyResponse model constructor.
     * @property {module:model/BatchGetStreamKeyResponse}
     */
    BatchGetStreamKeyResponse,

    /**
     * The BatchStartViewerSessionRevocationError model constructor.
     * @property {module:model/BatchStartViewerSessionRevocationError}
     */
    BatchStartViewerSessionRevocationError,

    /**
     * The BatchStartViewerSessionRevocationRequest model constructor.
     * @property {module:model/BatchStartViewerSessionRevocationRequest}
     */
    BatchStartViewerSessionRevocationRequest,

    /**
     * The BatchStartViewerSessionRevocationResponse model constructor.
     * @property {module:model/BatchStartViewerSessionRevocationResponse}
     */
    BatchStartViewerSessionRevocationResponse,

    /**
     * The BatchStartViewerSessionRevocationViewerSession model constructor.
     * @property {module:model/BatchStartViewerSessionRevocationViewerSession}
     */
    BatchStartViewerSessionRevocationViewerSession,

    /**
     * The Channel model constructor.
     * @property {module:model/Channel}
     */
    Channel,

    /**
     * The ChannelLatencyMode model constructor.
     * @property {module:model/ChannelLatencyMode}
     */
    ChannelLatencyMode,

    /**
     * The ChannelSummary model constructor.
     * @property {module:model/ChannelSummary}
     */
    ChannelSummary,

    /**
     * The ChannelType model constructor.
     * @property {module:model/ChannelType}
     */
    ChannelType,

    /**
     * The CreateChannelRequest model constructor.
     * @property {module:model/CreateChannelRequest}
     */
    CreateChannelRequest,

    /**
     * The CreateChannelResponse model constructor.
     * @property {module:model/CreateChannelResponse}
     */
    CreateChannelResponse,

    /**
     * The CreateChannelResponseChannel model constructor.
     * @property {module:model/CreateChannelResponseChannel}
     */
    CreateChannelResponseChannel,

    /**
     * The CreateChannelResponseStreamKey model constructor.
     * @property {module:model/CreateChannelResponseStreamKey}
     */
    CreateChannelResponseStreamKey,

    /**
     * The CreateRecordingConfigurationRequest model constructor.
     * @property {module:model/CreateRecordingConfigurationRequest}
     */
    CreateRecordingConfigurationRequest,

    /**
     * The CreateRecordingConfigurationRequestDestinationConfiguration model constructor.
     * @property {module:model/CreateRecordingConfigurationRequestDestinationConfiguration}
     */
    CreateRecordingConfigurationRequestDestinationConfiguration,

    /**
     * The CreateRecordingConfigurationRequestDestinationConfigurationS3 model constructor.
     * @property {module:model/CreateRecordingConfigurationRequestDestinationConfigurationS3}
     */
    CreateRecordingConfigurationRequestDestinationConfigurationS3,

    /**
     * The CreateRecordingConfigurationRequestRenditionConfiguration model constructor.
     * @property {module:model/CreateRecordingConfigurationRequestRenditionConfiguration}
     */
    CreateRecordingConfigurationRequestRenditionConfiguration,

    /**
     * The CreateRecordingConfigurationRequestThumbnailConfiguration model constructor.
     * @property {module:model/CreateRecordingConfigurationRequestThumbnailConfiguration}
     */
    CreateRecordingConfigurationRequestThumbnailConfiguration,

    /**
     * The CreateRecordingConfigurationResponse model constructor.
     * @property {module:model/CreateRecordingConfigurationResponse}
     */
    CreateRecordingConfigurationResponse,

    /**
     * The CreateRecordingConfigurationResponseRecordingConfiguration model constructor.
     * @property {module:model/CreateRecordingConfigurationResponseRecordingConfiguration}
     */
    CreateRecordingConfigurationResponseRecordingConfiguration,

    /**
     * The CreateStreamKeyRequest model constructor.
     * @property {module:model/CreateStreamKeyRequest}
     */
    CreateStreamKeyRequest,

    /**
     * The CreateStreamKeyResponse model constructor.
     * @property {module:model/CreateStreamKeyResponse}
     */
    CreateStreamKeyResponse,

    /**
     * The CreateStreamKeyResponseStreamKey model constructor.
     * @property {module:model/CreateStreamKeyResponseStreamKey}
     */
    CreateStreamKeyResponseStreamKey,

    /**
     * The DeleteChannelRequest model constructor.
     * @property {module:model/DeleteChannelRequest}
     */
    DeleteChannelRequest,

    /**
     * The DeletePlaybackKeyPairRequest model constructor.
     * @property {module:model/DeletePlaybackKeyPairRequest}
     */
    DeletePlaybackKeyPairRequest,

    /**
     * The DeleteRecordingConfigurationRequest model constructor.
     * @property {module:model/DeleteRecordingConfigurationRequest}
     */
    DeleteRecordingConfigurationRequest,

    /**
     * The DeleteStreamKeyRequest model constructor.
     * @property {module:model/DeleteStreamKeyRequest}
     */
    DeleteStreamKeyRequest,

    /**
     * The DestinationConfiguration model constructor.
     * @property {module:model/DestinationConfiguration}
     */
    DestinationConfiguration,

    /**
     * The GetChannelRequest model constructor.
     * @property {module:model/GetChannelRequest}
     */
    GetChannelRequest,

    /**
     * The GetChannelResponse model constructor.
     * @property {module:model/GetChannelResponse}
     */
    GetChannelResponse,

    /**
     * The GetPlaybackKeyPairRequest model constructor.
     * @property {module:model/GetPlaybackKeyPairRequest}
     */
    GetPlaybackKeyPairRequest,

    /**
     * The GetPlaybackKeyPairResponse model constructor.
     * @property {module:model/GetPlaybackKeyPairResponse}
     */
    GetPlaybackKeyPairResponse,

    /**
     * The GetPlaybackKeyPairResponseKeyPair model constructor.
     * @property {module:model/GetPlaybackKeyPairResponseKeyPair}
     */
    GetPlaybackKeyPairResponseKeyPair,

    /**
     * The GetRecordingConfigurationRequest model constructor.
     * @property {module:model/GetRecordingConfigurationRequest}
     */
    GetRecordingConfigurationRequest,

    /**
     * The GetRecordingConfigurationResponse model constructor.
     * @property {module:model/GetRecordingConfigurationResponse}
     */
    GetRecordingConfigurationResponse,

    /**
     * The GetStreamKeyRequest model constructor.
     * @property {module:model/GetStreamKeyRequest}
     */
    GetStreamKeyRequest,

    /**
     * The GetStreamKeyResponse model constructor.
     * @property {module:model/GetStreamKeyResponse}
     */
    GetStreamKeyResponse,

    /**
     * The GetStreamKeyResponseStreamKey model constructor.
     * @property {module:model/GetStreamKeyResponseStreamKey}
     */
    GetStreamKeyResponseStreamKey,

    /**
     * The GetStreamRequest model constructor.
     * @property {module:model/GetStreamRequest}
     */
    GetStreamRequest,

    /**
     * The GetStreamResponse model constructor.
     * @property {module:model/GetStreamResponse}
     */
    GetStreamResponse,

    /**
     * The GetStreamResponseStream model constructor.
     * @property {module:model/GetStreamResponseStream}
     */
    GetStreamResponseStream,

    /**
     * The GetStreamSessionRequest model constructor.
     * @property {module:model/GetStreamSessionRequest}
     */
    GetStreamSessionRequest,

    /**
     * The GetStreamSessionResponse model constructor.
     * @property {module:model/GetStreamSessionResponse}
     */
    GetStreamSessionResponse,

    /**
     * The GetStreamSessionResponseStreamSession model constructor.
     * @property {module:model/GetStreamSessionResponseStreamSession}
     */
    GetStreamSessionResponseStreamSession,

    /**
     * The ImportPlaybackKeyPairRequest model constructor.
     * @property {module:model/ImportPlaybackKeyPairRequest}
     */
    ImportPlaybackKeyPairRequest,

    /**
     * The ImportPlaybackKeyPairResponse model constructor.
     * @property {module:model/ImportPlaybackKeyPairResponse}
     */
    ImportPlaybackKeyPairResponse,

    /**
     * The ImportPlaybackKeyPairResponseKeyPair model constructor.
     * @property {module:model/ImportPlaybackKeyPairResponseKeyPair}
     */
    ImportPlaybackKeyPairResponseKeyPair,

    /**
     * The IngestConfiguration model constructor.
     * @property {module:model/IngestConfiguration}
     */
    IngestConfiguration,

    /**
     * The IngestConfigurationAudio model constructor.
     * @property {module:model/IngestConfigurationAudio}
     */
    IngestConfigurationAudio,

    /**
     * The IngestConfigurationVideo model constructor.
     * @property {module:model/IngestConfigurationVideo}
     */
    IngestConfigurationVideo,

    /**
     * The ListChannelsRequest model constructor.
     * @property {module:model/ListChannelsRequest}
     */
    ListChannelsRequest,

    /**
     * The ListChannelsResponse model constructor.
     * @property {module:model/ListChannelsResponse}
     */
    ListChannelsResponse,

    /**
     * The ListPlaybackKeyPairsRequest model constructor.
     * @property {module:model/ListPlaybackKeyPairsRequest}
     */
    ListPlaybackKeyPairsRequest,

    /**
     * The ListPlaybackKeyPairsResponse model constructor.
     * @property {module:model/ListPlaybackKeyPairsResponse}
     */
    ListPlaybackKeyPairsResponse,

    /**
     * The ListRecordingConfigurationsRequest model constructor.
     * @property {module:model/ListRecordingConfigurationsRequest}
     */
    ListRecordingConfigurationsRequest,

    /**
     * The ListRecordingConfigurationsResponse model constructor.
     * @property {module:model/ListRecordingConfigurationsResponse}
     */
    ListRecordingConfigurationsResponse,

    /**
     * The ListStreamKeysRequest model constructor.
     * @property {module:model/ListStreamKeysRequest}
     */
    ListStreamKeysRequest,

    /**
     * The ListStreamKeysResponse model constructor.
     * @property {module:model/ListStreamKeysResponse}
     */
    ListStreamKeysResponse,

    /**
     * The ListStreamSessionsRequest model constructor.
     * @property {module:model/ListStreamSessionsRequest}
     */
    ListStreamSessionsRequest,

    /**
     * The ListStreamSessionsResponse model constructor.
     * @property {module:model/ListStreamSessionsResponse}
     */
    ListStreamSessionsResponse,

    /**
     * The ListStreamsRequest model constructor.
     * @property {module:model/ListStreamsRequest}
     */
    ListStreamsRequest,

    /**
     * The ListStreamsRequestFilterBy model constructor.
     * @property {module:model/ListStreamsRequestFilterBy}
     */
    ListStreamsRequestFilterBy,

    /**
     * The ListStreamsResponse model constructor.
     * @property {module:model/ListStreamsResponse}
     */
    ListStreamsResponse,

    /**
     * The ListTagsForResourceResponse model constructor.
     * @property {module:model/ListTagsForResourceResponse}
     */
    ListTagsForResourceResponse,

    /**
     * The PlaybackKeyPair model constructor.
     * @property {module:model/PlaybackKeyPair}
     */
    PlaybackKeyPair,

    /**
     * The PlaybackKeyPairSummary model constructor.
     * @property {module:model/PlaybackKeyPairSummary}
     */
    PlaybackKeyPairSummary,

    /**
     * The PutMetadataRequest model constructor.
     * @property {module:model/PutMetadataRequest}
     */
    PutMetadataRequest,

    /**
     * The RecordingConfiguration model constructor.
     * @property {module:model/RecordingConfiguration}
     */
    RecordingConfiguration,

    /**
     * The RecordingConfigurationDestinationConfiguration model constructor.
     * @property {module:model/RecordingConfigurationDestinationConfiguration}
     */
    RecordingConfigurationDestinationConfiguration,

    /**
     * The RecordingConfigurationState model constructor.
     * @property {module:model/RecordingConfigurationState}
     */
    RecordingConfigurationState,

    /**
     * The RecordingConfigurationSummary model constructor.
     * @property {module:model/RecordingConfigurationSummary}
     */
    RecordingConfigurationSummary,

    /**
     * The RecordingMode model constructor.
     * @property {module:model/RecordingMode}
     */
    RecordingMode,

    /**
     * The RenditionConfiguration model constructor.
     * @property {module:model/RenditionConfiguration}
     */
    RenditionConfiguration,

    /**
     * The RenditionConfigurationRendition model constructor.
     * @property {module:model/RenditionConfigurationRendition}
     */
    RenditionConfigurationRendition,

    /**
     * The RenditionConfigurationRenditionSelection model constructor.
     * @property {module:model/RenditionConfigurationRenditionSelection}
     */
    RenditionConfigurationRenditionSelection,

    /**
     * The S3DestinationConfiguration model constructor.
     * @property {module:model/S3DestinationConfiguration}
     */
    S3DestinationConfiguration,

    /**
     * The StartViewerSessionRevocationRequest model constructor.
     * @property {module:model/StartViewerSessionRevocationRequest}
     */
    StartViewerSessionRevocationRequest,

    /**
     * The StopStreamRequest model constructor.
     * @property {module:model/StopStreamRequest}
     */
    StopStreamRequest,

    /**
     * The Stream model constructor.
     * @property {module:model/Stream}
     */
    Stream,

    /**
     * The StreamEvent model constructor.
     * @property {module:model/StreamEvent}
     */
    StreamEvent,

    /**
     * The StreamFilters model constructor.
     * @property {module:model/StreamFilters}
     */
    StreamFilters,

    /**
     * The StreamHealth model constructor.
     * @property {module:model/StreamHealth}
     */
    StreamHealth,

    /**
     * The StreamKey model constructor.
     * @property {module:model/StreamKey}
     */
    StreamKey,

    /**
     * The StreamKeySummary model constructor.
     * @property {module:model/StreamKeySummary}
     */
    StreamKeySummary,

    /**
     * The StreamSession model constructor.
     * @property {module:model/StreamSession}
     */
    StreamSession,

    /**
     * The StreamSessionChannel model constructor.
     * @property {module:model/StreamSessionChannel}
     */
    StreamSessionChannel,

    /**
     * The StreamSessionIngestConfiguration model constructor.
     * @property {module:model/StreamSessionIngestConfiguration}
     */
    StreamSessionIngestConfiguration,

    /**
     * The StreamSessionRecordingConfiguration model constructor.
     * @property {module:model/StreamSessionRecordingConfiguration}
     */
    StreamSessionRecordingConfiguration,

    /**
     * The StreamSessionSummary model constructor.
     * @property {module:model/StreamSessionSummary}
     */
    StreamSessionSummary,

    /**
     * The StreamState model constructor.
     * @property {module:model/StreamState}
     */
    StreamState,

    /**
     * The StreamSummary model constructor.
     * @property {module:model/StreamSummary}
     */
    StreamSummary,

    /**
     * The TagResourceRequest model constructor.
     * @property {module:model/TagResourceRequest}
     */
    TagResourceRequest,

    /**
     * The ThumbnailConfiguration model constructor.
     * @property {module:model/ThumbnailConfiguration}
     */
    ThumbnailConfiguration,

    /**
     * The ThumbnailConfigurationResolution model constructor.
     * @property {module:model/ThumbnailConfigurationResolution}
     */
    ThumbnailConfigurationResolution,

    /**
     * The ThumbnailConfigurationStorage model constructor.
     * @property {module:model/ThumbnailConfigurationStorage}
     */
    ThumbnailConfigurationStorage,

    /**
     * The TranscodePreset model constructor.
     * @property {module:model/TranscodePreset}
     */
    TranscodePreset,

    /**
     * The UpdateChannelRequest model constructor.
     * @property {module:model/UpdateChannelRequest}
     */
    UpdateChannelRequest,

    /**
     * The UpdateChannelResponse model constructor.
     * @property {module:model/UpdateChannelResponse}
     */
    UpdateChannelResponse,

    /**
     * The VideoConfiguration model constructor.
     * @property {module:model/VideoConfiguration}
     */
    VideoConfiguration,

    /**
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
