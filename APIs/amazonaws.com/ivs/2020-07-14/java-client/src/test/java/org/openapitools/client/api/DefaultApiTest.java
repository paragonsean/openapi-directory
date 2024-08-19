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

import org.openapitools.client.ApiException;
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
     * Performs &lt;a&gt;GetChannel&lt;/a&gt; on multiple ARNs simultaneously.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchGetChannelTest() throws ApiException {
        BatchGetChannelRequest batchGetChannelRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchGetChannelResponse response = api.batchGetChannel(batchGetChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Performs &lt;a&gt;GetStreamKey&lt;/a&gt; on multiple ARNs simultaneously.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchGetStreamKeyTest() throws ApiException {
        BatchGetStreamKeyRequest batchGetStreamKeyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchGetStreamKeyResponse response = api.batchGetStreamKey(batchGetStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Performs &lt;a&gt;StartViewerSessionRevocation&lt;/a&gt; on multiple channel ARN and viewer ID pairs simultaneously.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchStartViewerSessionRevocationTest() throws ApiException {
        BatchStartViewerSessionRevocationRequest batchStartViewerSessionRevocationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        BatchStartViewerSessionRevocationResponse response = api.batchStartViewerSessionRevocation(batchStartViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Creates a new channel and an associated stream key to start streaming.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createChannelTest() throws ApiException {
        CreateChannelRequest createChannelRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateChannelResponse response = api.createChannel(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a new recording configuration, used to enable recording to Amazon S3.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Known issue:&lt;/b&gt; In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the &lt;code&gt;state&lt;/code&gt; of the recording configuration is &lt;code&gt;CREATE_FAILED&lt;/code&gt; (instead of &lt;code&gt;ACTIVE&lt;/code&gt;). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)&lt;/p&gt; &lt;p&gt; &lt;b&gt;Workaround:&lt;/b&gt; Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createRecordingConfigurationTest() throws ApiException {
        CreateRecordingConfigurationRequest createRecordingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateRecordingConfigurationResponse response = api.createRecordingConfiguration(createRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Creates a stream key, used to initiate a stream, for the specified channel ARN.&lt;/p&gt; &lt;p&gt;Note that &lt;a&gt;CreateChannel&lt;/a&gt; creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use &lt;a&gt;DeleteStreamKey&lt;/a&gt; and then CreateStreamKey.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createStreamKeyTest() throws ApiException {
        CreateStreamKeyRequest createStreamKeyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        CreateStreamKeyResponse response = api.createStreamKey(createStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes the specified channel and its associated stream keys.&lt;/p&gt; &lt;p&gt;If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call &lt;a&gt;StopStream&lt;/a&gt;, wait for the Amazon EventBridge \&quot;Stream End\&quot; event (to verify that the stream&#39;s state is no longer Live), then call DeleteChannel. (See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\&quot;&gt; Using EventBridge with Amazon IVS&lt;/a&gt;.) &lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteChannelTest() throws ApiException {
        DeleteChannelRequest deleteChannelRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteChannel(deleteChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s &lt;code&gt;privateKey&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePlaybackKeyPairTest() throws ApiException {
        DeletePlaybackKeyPairRequest deletePlaybackKeyPairRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.deletePlaybackKeyPair(deletePlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Deletes the recording configuration for the specified ARN.&lt;/p&gt; &lt;p&gt;If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use &lt;a&gt;UpdateChannel&lt;/a&gt; to set the &lt;code&gt;recordingConfigurationArn&lt;/code&gt; field to an empty string, then use DeleteRecordingConfiguration.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRecordingConfigurationTest() throws ApiException {
        DeleteRecordingConfigurationRequest deleteRecordingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteRecordingConfiguration(deleteRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Deletes the stream key for the specified ARN, so it can no longer be used to stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteStreamKeyTest() throws ApiException {
        DeleteStreamKeyRequest deleteStreamKeyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.deleteStreamKey(deleteStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets the channel configuration for the specified channel ARN. See also &lt;a&gt;BatchGetChannel&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getChannelTest() throws ApiException {
        GetChannelRequest getChannelRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetChannelResponse response = api.getChannel(getChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets a specified playback authorization key pair and returns the &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPlaybackKeyPairTest() throws ApiException {
        GetPlaybackKeyPairRequest getPlaybackKeyPairRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetPlaybackKeyPairResponse response = api.getPlaybackKeyPair(getPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets the recording configuration for the specified ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getRecordingConfigurationTest() throws ApiException {
        GetRecordingConfigurationRequest getRecordingConfigurationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetRecordingConfigurationResponse response = api.getRecordingConfiguration(getRecordingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets information about the active (live) stream on a specified channel.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStreamTest() throws ApiException {
        GetStreamRequest getStreamRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetStreamResponse response = api.getStream(getStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets stream-key information for a specified ARN.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStreamKeyTest() throws ApiException {
        GetStreamKeyRequest getStreamKeyRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetStreamKeyResponse response = api.getStreamKey(getStreamKeyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets metadata on a specified stream.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStreamSessionTest() throws ApiException {
        GetStreamSessionRequest getStreamSessionRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        GetStreamSessionResponse response = api.getStreamSession(getStreamSessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Imports the public portion of a new key pair and returns its &lt;code&gt;arn&lt;/code&gt; and &lt;code&gt;fingerprint&lt;/code&gt;. The &lt;code&gt;privateKey&lt;/code&gt; can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void importPlaybackKeyPairTest() throws ApiException {
        ImportPlaybackKeyPairRequest importPlaybackKeyPairRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        ImportPlaybackKeyPairResponse response = api.importPlaybackKeyPair(importPlaybackKeyPairRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listChannelsTest() throws ApiException {
        ListChannelsRequest listChannelsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListChannelsResponse response = api.listChannels(listChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets summary information about playback key pairs. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listPlaybackKeyPairsTest() throws ApiException {
        ListPlaybackKeyPairsRequest listPlaybackKeyPairsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListPlaybackKeyPairsResponse response = api.listPlaybackKeyPairs(listPlaybackKeyPairsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRecordingConfigurationsTest() throws ApiException {
        ListRecordingConfigurationsRequest listRecordingConfigurationsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListRecordingConfigurationsResponse response = api.listRecordingConfigurations(listRecordingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets summary information about stream keys for the specified channel.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listStreamKeysTest() throws ApiException {
        ListStreamKeysRequest listStreamKeysRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListStreamKeysResponse response = api.listStreamKeys(listStreamKeysRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listStreamSessionsTest() throws ApiException {
        ListStreamSessionsRequest listStreamSessionsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListStreamSessionsResponse response = api.listStreamSessions(listStreamSessionsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listStreamsTest() throws ApiException {
        ListStreamsRequest listStreamsRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        String maxResults = null;
        String nextToken = null;
        ListStreamsResponse response = api.listStreams(listStreamsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken);
        // TODO: test validations
    }

    /**
     * Gets information about Amazon Web Services tags for the specified ARN.
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
     * Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\&quot;&gt;Embedding Metadata within a Video Stream&lt;/a&gt; in the &lt;i&gt;Amazon IVS User Guide&lt;/i&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putMetadataTest() throws ApiException {
        PutMetadataRequest putMetadataRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        api.putMetadata(putMetadataRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\&quot;&gt;Setting Up Private Channels&lt;/a&gt;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startViewerSessionRevocationTest() throws ApiException {
        StartViewerSessionRevocationRequest startViewerSessionRevocationRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.startViewerSessionRevocation(startViewerSessionRevocationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * &lt;p&gt;Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with &lt;a&gt;DeleteStreamKey&lt;/a&gt; to prevent further streaming to a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the &lt;code&gt;streamKey&lt;/code&gt; attached to the channel.&lt;/p&gt; &lt;/note&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopStreamTest() throws ApiException {
        StopStreamRequest stopStreamRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        Object response = api.stopStream(stopStreamRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

    /**
     * Adds or updates tags for the Amazon Web Services resource with the specified ARN.
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
     * Updates a channel&#39;s configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateChannelTest() throws ApiException {
        UpdateChannelRequest updateChannelRequest = null;
        String xAmzContentSha256 = null;
        String xAmzDate = null;
        String xAmzAlgorithm = null;
        String xAmzCredential = null;
        String xAmzSecurityToken = null;
        String xAmzSignature = null;
        String xAmzSignedHeaders = null;
        UpdateChannelResponse response = api.updateChannel(updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
        // TODO: test validations
    }

}
