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


import ApiClient from "../ApiClient";
import BatchGetChannelRequest from '../model/BatchGetChannelRequest';
import BatchGetChannelResponse from '../model/BatchGetChannelResponse';
import BatchGetStreamKeyRequest from '../model/BatchGetStreamKeyRequest';
import BatchGetStreamKeyResponse from '../model/BatchGetStreamKeyResponse';
import BatchStartViewerSessionRevocationRequest from '../model/BatchStartViewerSessionRevocationRequest';
import BatchStartViewerSessionRevocationResponse from '../model/BatchStartViewerSessionRevocationResponse';
import CreateChannelRequest from '../model/CreateChannelRequest';
import CreateChannelResponse from '../model/CreateChannelResponse';
import CreateRecordingConfigurationRequest from '../model/CreateRecordingConfigurationRequest';
import CreateRecordingConfigurationResponse from '../model/CreateRecordingConfigurationResponse';
import CreateStreamKeyRequest from '../model/CreateStreamKeyRequest';
import CreateStreamKeyResponse from '../model/CreateStreamKeyResponse';
import DeleteChannelRequest from '../model/DeleteChannelRequest';
import DeletePlaybackKeyPairRequest from '../model/DeletePlaybackKeyPairRequest';
import DeleteRecordingConfigurationRequest from '../model/DeleteRecordingConfigurationRequest';
import DeleteStreamKeyRequest from '../model/DeleteStreamKeyRequest';
import GetChannelRequest from '../model/GetChannelRequest';
import GetChannelResponse from '../model/GetChannelResponse';
import GetPlaybackKeyPairRequest from '../model/GetPlaybackKeyPairRequest';
import GetPlaybackKeyPairResponse from '../model/GetPlaybackKeyPairResponse';
import GetRecordingConfigurationRequest from '../model/GetRecordingConfigurationRequest';
import GetRecordingConfigurationResponse from '../model/GetRecordingConfigurationResponse';
import GetStreamKeyRequest from '../model/GetStreamKeyRequest';
import GetStreamKeyResponse from '../model/GetStreamKeyResponse';
import GetStreamRequest from '../model/GetStreamRequest';
import GetStreamResponse from '../model/GetStreamResponse';
import GetStreamSessionRequest from '../model/GetStreamSessionRequest';
import GetStreamSessionResponse from '../model/GetStreamSessionResponse';
import ImportPlaybackKeyPairRequest from '../model/ImportPlaybackKeyPairRequest';
import ImportPlaybackKeyPairResponse from '../model/ImportPlaybackKeyPairResponse';
import ListChannelsRequest from '../model/ListChannelsRequest';
import ListChannelsResponse from '../model/ListChannelsResponse';
import ListPlaybackKeyPairsRequest from '../model/ListPlaybackKeyPairsRequest';
import ListPlaybackKeyPairsResponse from '../model/ListPlaybackKeyPairsResponse';
import ListRecordingConfigurationsRequest from '../model/ListRecordingConfigurationsRequest';
import ListRecordingConfigurationsResponse from '../model/ListRecordingConfigurationsResponse';
import ListStreamKeysRequest from '../model/ListStreamKeysRequest';
import ListStreamKeysResponse from '../model/ListStreamKeysResponse';
import ListStreamSessionsRequest from '../model/ListStreamSessionsRequest';
import ListStreamSessionsResponse from '../model/ListStreamSessionsResponse';
import ListStreamsRequest from '../model/ListStreamsRequest';
import ListStreamsResponse from '../model/ListStreamsResponse';
import ListTagsForResourceResponse from '../model/ListTagsForResourceResponse';
import PutMetadataRequest from '../model/PutMetadataRequest';
import StartViewerSessionRevocationRequest from '../model/StartViewerSessionRevocationRequest';
import StopStreamRequest from '../model/StopStreamRequest';
import TagResourceRequest from '../model/TagResourceRequest';
import UpdateChannelRequest from '../model/UpdateChannelRequest';
import UpdateChannelResponse from '../model/UpdateChannelResponse';

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
     * Callback function to receive the result of the batchGetChannel operation.
     * @callback module:api/DefaultApi~batchGetChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchGetChannelResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Performs <a>GetChannel</a> on multiple ARNs simultaneously.
     * @param {module:model/BatchGetChannelRequest} batchGetChannelRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchGetChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchGetChannelResponse}
     */
    batchGetChannel(batchGetChannelRequest, opts, callback) {
      opts = opts || {};
      let postBody = batchGetChannelRequest;
      // verify the required parameter 'batchGetChannelRequest' is set
      if (batchGetChannelRequest === undefined || batchGetChannelRequest === null) {
        throw new Error("Missing the required parameter 'batchGetChannelRequest' when calling batchGetChannel");
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
      let returnType = BatchGetChannelResponse;
      return this.apiClient.callApi(
        '/BatchGetChannel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchGetStreamKey operation.
     * @callback module:api/DefaultApi~batchGetStreamKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchGetStreamKeyResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Performs <a>GetStreamKey</a> on multiple ARNs simultaneously.
     * @param {module:model/BatchGetStreamKeyRequest} batchGetStreamKeyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchGetStreamKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchGetStreamKeyResponse}
     */
    batchGetStreamKey(batchGetStreamKeyRequest, opts, callback) {
      opts = opts || {};
      let postBody = batchGetStreamKeyRequest;
      // verify the required parameter 'batchGetStreamKeyRequest' is set
      if (batchGetStreamKeyRequest === undefined || batchGetStreamKeyRequest === null) {
        throw new Error("Missing the required parameter 'batchGetStreamKeyRequest' when calling batchGetStreamKey");
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
      let returnType = BatchGetStreamKeyResponse;
      return this.apiClient.callApi(
        '/BatchGetStreamKey', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the batchStartViewerSessionRevocation operation.
     * @callback module:api/DefaultApi~batchStartViewerSessionRevocationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BatchStartViewerSessionRevocationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Performs <a>StartViewerSessionRevocation</a> on multiple channel ARN and viewer ID pairs simultaneously.
     * @param {module:model/BatchStartViewerSessionRevocationRequest} batchStartViewerSessionRevocationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~batchStartViewerSessionRevocationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BatchStartViewerSessionRevocationResponse}
     */
    batchStartViewerSessionRevocation(batchStartViewerSessionRevocationRequest, opts, callback) {
      opts = opts || {};
      let postBody = batchStartViewerSessionRevocationRequest;
      // verify the required parameter 'batchStartViewerSessionRevocationRequest' is set
      if (batchStartViewerSessionRevocationRequest === undefined || batchStartViewerSessionRevocationRequest === null) {
        throw new Error("Missing the required parameter 'batchStartViewerSessionRevocationRequest' when calling batchStartViewerSessionRevocation");
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
      let returnType = BatchStartViewerSessionRevocationResponse;
      return this.apiClient.callApi(
        '/BatchStartViewerSessionRevocation', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createChannel operation.
     * @callback module:api/DefaultApi~createChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateChannelResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates a new channel and an associated stream key to start streaming.
     * @param {module:model/CreateChannelRequest} createChannelRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateChannelResponse}
     */
    createChannel(createChannelRequest, opts, callback) {
      opts = opts || {};
      let postBody = createChannelRequest;
      // verify the required parameter 'createChannelRequest' is set
      if (createChannelRequest === undefined || createChannelRequest === null) {
        throw new Error("Missing the required parameter 'createChannelRequest' when calling createChannel");
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
      let returnType = CreateChannelResponse;
      return this.apiClient.callApi(
        '/CreateChannel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createRecordingConfiguration operation.
     * @callback module:api/DefaultApi~createRecordingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateRecordingConfigurationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates a new recording configuration, used to enable recording to Amazon S3.</p> <p> <b>Known issue:</b> In the us-east-1 region, if you use the Amazon Web Services CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the <code>state</code> of the recording configuration is <code>CREATE_FAILED</code> (instead of <code>ACTIVE</code>). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)</p> <p> <b>Workaround:</b> Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.</p>
     * @param {module:model/CreateRecordingConfigurationRequest} createRecordingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createRecordingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateRecordingConfigurationResponse}
     */
    createRecordingConfiguration(createRecordingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = createRecordingConfigurationRequest;
      // verify the required parameter 'createRecordingConfigurationRequest' is set
      if (createRecordingConfigurationRequest === undefined || createRecordingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'createRecordingConfigurationRequest' when calling createRecordingConfiguration");
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
      let returnType = CreateRecordingConfigurationResponse;
      return this.apiClient.callApi(
        '/CreateRecordingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createStreamKey operation.
     * @callback module:api/DefaultApi~createStreamKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreateStreamKeyResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Creates a stream key, used to initiate a stream, for the specified channel ARN.</p> <p>Note that <a>CreateChannel</a> creates a stream key. If you subsequently use CreateStreamKey on the same channel, it will fail because a stream key already exists and there is a limit of 1 stream key per channel. To reset the stream key on a channel, use <a>DeleteStreamKey</a> and then CreateStreamKey.</p>
     * @param {module:model/CreateStreamKeyRequest} createStreamKeyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~createStreamKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreateStreamKeyResponse}
     */
    createStreamKey(createStreamKeyRequest, opts, callback) {
      opts = opts || {};
      let postBody = createStreamKeyRequest;
      // verify the required parameter 'createStreamKeyRequest' is set
      if (createStreamKeyRequest === undefined || createStreamKeyRequest === null) {
        throw new Error("Missing the required parameter 'createStreamKeyRequest' when calling createStreamKey");
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
      let returnType = CreateStreamKeyResponse;
      return this.apiClient.callApi(
        '/CreateStreamKey', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteChannel operation.
     * @callback module:api/DefaultApi~deleteChannelCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Deletes the specified channel and its associated stream keys.</p> <p>If you try to delete a live channel, you will get an error (409 ConflictException). To delete a channel that is live, call <a>StopStream</a>, wait for the Amazon EventBridge \"Stream End\" event (to verify that the stream's state is no longer Live), then call DeleteChannel. (See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/eventbridge.html\"> Using EventBridge with Amazon IVS</a>.) </p>
     * @param {module:model/DeleteChannelRequest} deleteChannelRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteChannelCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteChannel(deleteChannelRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteChannelRequest;
      // verify the required parameter 'deleteChannelRequest' is set
      if (deleteChannelRequest === undefined || deleteChannelRequest === null) {
        throw new Error("Missing the required parameter 'deleteChannelRequest' when calling deleteChannel");
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
        '/DeleteChannel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deletePlaybackKeyPair operation.
     * @callback module:api/DefaultApi~deletePlaybackKeyPairCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes a specified authorization key pair. This invalidates future viewer tokens generated using the key pair’s <code>privateKey</code>. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.
     * @param {module:model/DeletePlaybackKeyPairRequest} deletePlaybackKeyPairRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deletePlaybackKeyPairCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deletePlaybackKeyPair(deletePlaybackKeyPairRequest, opts, callback) {
      opts = opts || {};
      let postBody = deletePlaybackKeyPairRequest;
      // verify the required parameter 'deletePlaybackKeyPairRequest' is set
      if (deletePlaybackKeyPairRequest === undefined || deletePlaybackKeyPairRequest === null) {
        throw new Error("Missing the required parameter 'deletePlaybackKeyPairRequest' when calling deletePlaybackKeyPair");
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
        '/DeletePlaybackKeyPair', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteRecordingConfiguration operation.
     * @callback module:api/DefaultApi~deleteRecordingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Deletes the recording configuration for the specified ARN.</p> <p>If you try to delete a recording configuration that is associated with a channel, you will get an error (409 ConflictException). To avoid this, for all channels that reference the recording configuration, first use <a>UpdateChannel</a> to set the <code>recordingConfigurationArn</code> field to an empty string, then use DeleteRecordingConfiguration.</p>
     * @param {module:model/DeleteRecordingConfigurationRequest} deleteRecordingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteRecordingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteRecordingConfiguration(deleteRecordingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteRecordingConfigurationRequest;
      // verify the required parameter 'deleteRecordingConfigurationRequest' is set
      if (deleteRecordingConfigurationRequest === undefined || deleteRecordingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'deleteRecordingConfigurationRequest' when calling deleteRecordingConfiguration");
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
        '/DeleteRecordingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteStreamKey operation.
     * @callback module:api/DefaultApi~deleteStreamKeyCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the stream key for the specified ARN, so it can no longer be used to stream.
     * @param {module:model/DeleteStreamKeyRequest} deleteStreamKeyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~deleteStreamKeyCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteStreamKey(deleteStreamKeyRequest, opts, callback) {
      opts = opts || {};
      let postBody = deleteStreamKeyRequest;
      // verify the required parameter 'deleteStreamKeyRequest' is set
      if (deleteStreamKeyRequest === undefined || deleteStreamKeyRequest === null) {
        throw new Error("Missing the required parameter 'deleteStreamKeyRequest' when calling deleteStreamKey");
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
        '/DeleteStreamKey', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getChannel operation.
     * @callback module:api/DefaultApi~getChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetChannelResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the channel configuration for the specified channel ARN. See also <a>BatchGetChannel</a>.
     * @param {module:model/GetChannelRequest} getChannelRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetChannelResponse}
     */
    getChannel(getChannelRequest, opts, callback) {
      opts = opts || {};
      let postBody = getChannelRequest;
      // verify the required parameter 'getChannelRequest' is set
      if (getChannelRequest === undefined || getChannelRequest === null) {
        throw new Error("Missing the required parameter 'getChannelRequest' when calling getChannel");
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
      let returnType = GetChannelResponse;
      return this.apiClient.callApi(
        '/GetChannel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getPlaybackKeyPair operation.
     * @callback module:api/DefaultApi~getPlaybackKeyPairCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetPlaybackKeyPairResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a specified playback authorization key pair and returns the <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> held by the caller can be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.
     * @param {module:model/GetPlaybackKeyPairRequest} getPlaybackKeyPairRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getPlaybackKeyPairCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetPlaybackKeyPairResponse}
     */
    getPlaybackKeyPair(getPlaybackKeyPairRequest, opts, callback) {
      opts = opts || {};
      let postBody = getPlaybackKeyPairRequest;
      // verify the required parameter 'getPlaybackKeyPairRequest' is set
      if (getPlaybackKeyPairRequest === undefined || getPlaybackKeyPairRequest === null) {
        throw new Error("Missing the required parameter 'getPlaybackKeyPairRequest' when calling getPlaybackKeyPair");
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
      let returnType = GetPlaybackKeyPairResponse;
      return this.apiClient.callApi(
        '/GetPlaybackKeyPair', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRecordingConfiguration operation.
     * @callback module:api/DefaultApi~getRecordingConfigurationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRecordingConfigurationResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the recording configuration for the specified ARN.
     * @param {module:model/GetRecordingConfigurationRequest} getRecordingConfigurationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getRecordingConfigurationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRecordingConfigurationResponse}
     */
    getRecordingConfiguration(getRecordingConfigurationRequest, opts, callback) {
      opts = opts || {};
      let postBody = getRecordingConfigurationRequest;
      // verify the required parameter 'getRecordingConfigurationRequest' is set
      if (getRecordingConfigurationRequest === undefined || getRecordingConfigurationRequest === null) {
        throw new Error("Missing the required parameter 'getRecordingConfigurationRequest' when calling getRecordingConfiguration");
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
      let returnType = GetRecordingConfigurationResponse;
      return this.apiClient.callApi(
        '/GetRecordingConfiguration', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getStream operation.
     * @callback module:api/DefaultApi~getStreamCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetStreamResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets information about the active (live) stream on a specified channel.
     * @param {module:model/GetStreamRequest} getStreamRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getStreamCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetStreamResponse}
     */
    getStream(getStreamRequest, opts, callback) {
      opts = opts || {};
      let postBody = getStreamRequest;
      // verify the required parameter 'getStreamRequest' is set
      if (getStreamRequest === undefined || getStreamRequest === null) {
        throw new Error("Missing the required parameter 'getStreamRequest' when calling getStream");
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
      let returnType = GetStreamResponse;
      return this.apiClient.callApi(
        '/GetStream', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getStreamKey operation.
     * @callback module:api/DefaultApi~getStreamKeyCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetStreamKeyResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets stream-key information for a specified ARN.
     * @param {module:model/GetStreamKeyRequest} getStreamKeyRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getStreamKeyCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetStreamKeyResponse}
     */
    getStreamKey(getStreamKeyRequest, opts, callback) {
      opts = opts || {};
      let postBody = getStreamKeyRequest;
      // verify the required parameter 'getStreamKeyRequest' is set
      if (getStreamKeyRequest === undefined || getStreamKeyRequest === null) {
        throw new Error("Missing the required parameter 'getStreamKeyRequest' when calling getStreamKey");
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
      let returnType = GetStreamKeyResponse;
      return this.apiClient.callApi(
        '/GetStreamKey', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getStreamSession operation.
     * @callback module:api/DefaultApi~getStreamSessionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetStreamSessionResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets metadata on a specified stream.
     * @param {module:model/GetStreamSessionRequest} getStreamSessionRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~getStreamSessionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetStreamSessionResponse}
     */
    getStreamSession(getStreamSessionRequest, opts, callback) {
      opts = opts || {};
      let postBody = getStreamSessionRequest;
      // verify the required parameter 'getStreamSessionRequest' is set
      if (getStreamSessionRequest === undefined || getStreamSessionRequest === null) {
        throw new Error("Missing the required parameter 'getStreamSessionRequest' when calling getStreamSession");
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
      let returnType = GetStreamSessionResponse;
      return this.apiClient.callApi(
        '/GetStreamSession', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the importPlaybackKeyPair operation.
     * @callback module:api/DefaultApi~importPlaybackKeyPairCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImportPlaybackKeyPairResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Imports the public portion of a new key pair and returns its <code>arn</code> and <code>fingerprint</code>. The <code>privateKey</code> can then be used to generate viewer authorization tokens, to grant viewers access to private channels. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.
     * @param {module:model/ImportPlaybackKeyPairRequest} importPlaybackKeyPairRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~importPlaybackKeyPairCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImportPlaybackKeyPairResponse}
     */
    importPlaybackKeyPair(importPlaybackKeyPairRequest, opts, callback) {
      opts = opts || {};
      let postBody = importPlaybackKeyPairRequest;
      // verify the required parameter 'importPlaybackKeyPairRequest' is set
      if (importPlaybackKeyPairRequest === undefined || importPlaybackKeyPairRequest === null) {
        throw new Error("Missing the required parameter 'importPlaybackKeyPairRequest' when calling importPlaybackKeyPair");
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
      let returnType = ImportPlaybackKeyPairResponse;
      return this.apiClient.callApi(
        '/ImportPlaybackKeyPair', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listChannels operation.
     * @callback module:api/DefaultApi~listChannelsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListChannelsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about all channels in your account, in the Amazon Web Services region where the API request is processed. This list can be filtered to match a specified name or recording-configuration ARN. Filters are mutually exclusive and cannot be used together. If you try to use both filters, you will get an error (409 ConflictException).
     * @param {module:model/ListChannelsRequest} listChannelsRequest 
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
     * @param {module:api/DefaultApi~listChannelsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListChannelsResponse}
     */
    listChannels(listChannelsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listChannelsRequest;
      // verify the required parameter 'listChannelsRequest' is set
      if (listChannelsRequest === undefined || listChannelsRequest === null) {
        throw new Error("Missing the required parameter 'listChannelsRequest' when calling listChannels");
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
      let returnType = ListChannelsResponse;
      return this.apiClient.callApi(
        '/ListChannels', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listPlaybackKeyPairs operation.
     * @callback module:api/DefaultApi~listPlaybackKeyPairsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListPlaybackKeyPairsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about playback key pairs. For more information, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a> in the <i>Amazon IVS User Guide</i>.
     * @param {module:model/ListPlaybackKeyPairsRequest} listPlaybackKeyPairsRequest 
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
     * @param {module:api/DefaultApi~listPlaybackKeyPairsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListPlaybackKeyPairsResponse}
     */
    listPlaybackKeyPairs(listPlaybackKeyPairsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listPlaybackKeyPairsRequest;
      // verify the required parameter 'listPlaybackKeyPairsRequest' is set
      if (listPlaybackKeyPairsRequest === undefined || listPlaybackKeyPairsRequest === null) {
        throw new Error("Missing the required parameter 'listPlaybackKeyPairsRequest' when calling listPlaybackKeyPairs");
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
      let returnType = ListPlaybackKeyPairsResponse;
      return this.apiClient.callApi(
        '/ListPlaybackKeyPairs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listRecordingConfigurations operation.
     * @callback module:api/DefaultApi~listRecordingConfigurationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListRecordingConfigurationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about all recording configurations in your account, in the Amazon Web Services region where the API request is processed.
     * @param {module:model/ListRecordingConfigurationsRequest} listRecordingConfigurationsRequest 
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
     * @param {module:api/DefaultApi~listRecordingConfigurationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListRecordingConfigurationsResponse}
     */
    listRecordingConfigurations(listRecordingConfigurationsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listRecordingConfigurationsRequest;
      // verify the required parameter 'listRecordingConfigurationsRequest' is set
      if (listRecordingConfigurationsRequest === undefined || listRecordingConfigurationsRequest === null) {
        throw new Error("Missing the required parameter 'listRecordingConfigurationsRequest' when calling listRecordingConfigurations");
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
      let returnType = ListRecordingConfigurationsResponse;
      return this.apiClient.callApi(
        '/ListRecordingConfigurations', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listStreamKeys operation.
     * @callback module:api/DefaultApi~listStreamKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListStreamKeysResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about stream keys for the specified channel.
     * @param {module:model/ListStreamKeysRequest} listStreamKeysRequest 
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
     * @param {module:api/DefaultApi~listStreamKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListStreamKeysResponse}
     */
    listStreamKeys(listStreamKeysRequest, opts, callback) {
      opts = opts || {};
      let postBody = listStreamKeysRequest;
      // verify the required parameter 'listStreamKeysRequest' is set
      if (listStreamKeysRequest === undefined || listStreamKeysRequest === null) {
        throw new Error("Missing the required parameter 'listStreamKeysRequest' when calling listStreamKeys");
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
      let returnType = ListStreamKeysResponse;
      return this.apiClient.callApi(
        '/ListStreamKeys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listStreamSessions operation.
     * @callback module:api/DefaultApi~listStreamSessionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListStreamSessionsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets a summary of current and previous streams for a specified channel in your account, in the AWS region where the API request is processed.
     * @param {module:model/ListStreamSessionsRequest} listStreamSessionsRequest 
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
     * @param {module:api/DefaultApi~listStreamSessionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListStreamSessionsResponse}
     */
    listStreamSessions(listStreamSessionsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listStreamSessionsRequest;
      // verify the required parameter 'listStreamSessionsRequest' is set
      if (listStreamSessionsRequest === undefined || listStreamSessionsRequest === null) {
        throw new Error("Missing the required parameter 'listStreamSessionsRequest' when calling listStreamSessions");
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
      let returnType = ListStreamSessionsResponse;
      return this.apiClient.callApi(
        '/ListStreamSessions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listStreams operation.
     * @callback module:api/DefaultApi~listStreamsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ListStreamsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets summary information about live streams in your account, in the Amazon Web Services region where the API request is processed.
     * @param {module:model/ListStreamsRequest} listStreamsRequest 
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
     * @param {module:api/DefaultApi~listStreamsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ListStreamsResponse}
     */
    listStreams(listStreamsRequest, opts, callback) {
      opts = opts || {};
      let postBody = listStreamsRequest;
      // verify the required parameter 'listStreamsRequest' is set
      if (listStreamsRequest === undefined || listStreamsRequest === null) {
        throw new Error("Missing the required parameter 'listStreamsRequest' when calling listStreams");
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
      let returnType = ListStreamsResponse;
      return this.apiClient.callApi(
        '/ListStreams', 'POST',
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
     * Gets information about Amazon Web Services tags for the specified ARN.
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
     * Callback function to receive the result of the putMetadata operation.
     * @callback module:api/DefaultApi~putMetadataCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Inserts metadata into the active stream of the specified channel. At most 5 requests per second per channel are allowed, each with a maximum 1 KB payload. (If 5 TPS is not sufficient for your needs, we recommend batching your data into a single PutMetadata call.) At most 155 requests per second per account are allowed. Also see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/metadata.html\">Embedding Metadata within a Video Stream</a> in the <i>Amazon IVS User Guide</i>.
     * @param {module:model/PutMetadataRequest} putMetadataRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~putMetadataCallback} callback The callback function, accepting three arguments: error, data, response
     */
    putMetadata(putMetadataRequest, opts, callback) {
      opts = opts || {};
      let postBody = putMetadataRequest;
      // verify the required parameter 'putMetadataRequest' is set
      if (putMetadataRequest === undefined || putMetadataRequest === null) {
        throw new Error("Missing the required parameter 'putMetadataRequest' when calling putMetadata");
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
        '/PutMetadata', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the startViewerSessionRevocation operation.
     * @callback module:api/DefaultApi~startViewerSessionRevocationCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html\">Setting Up Private Channels</a>.
     * @param {module:model/StartViewerSessionRevocationRequest} startViewerSessionRevocationRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~startViewerSessionRevocationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    startViewerSessionRevocation(startViewerSessionRevocationRequest, opts, callback) {
      opts = opts || {};
      let postBody = startViewerSessionRevocationRequest;
      // verify the required parameter 'startViewerSessionRevocationRequest' is set
      if (startViewerSessionRevocationRequest === undefined || startViewerSessionRevocationRequest === null) {
        throw new Error("Missing the required parameter 'startViewerSessionRevocationRequest' when calling startViewerSessionRevocation");
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
        '/StartViewerSessionRevocation', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the stopStream operation.
     * @callback module:api/DefaultApi~stopStreamCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * <p>Disconnects the incoming RTMPS stream for the specified channel. Can be used in conjunction with <a>DeleteStreamKey</a> to prevent further streaming to a channel.</p> <note> <p>Many streaming client-software libraries automatically reconnect a dropped RTMPS session, so to stop the stream permanently, you may want to first revoke the <code>streamKey</code> attached to the channel.</p> </note>
     * @param {module:model/StopStreamRequest} stopStreamRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~stopStreamCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    stopStream(stopStreamRequest, opts, callback) {
      opts = opts || {};
      let postBody = stopStreamRequest;
      // verify the required parameter 'stopStreamRequest' is set
      if (stopStreamRequest === undefined || stopStreamRequest === null) {
        throw new Error("Missing the required parameter 'stopStreamRequest' when calling stopStream");
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
        '/StopStream', 'POST',
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
     * Adds or updates tags for the Amazon Web Services resource with the specified ARN.
     * @param {String} resourceArn ARN of the resource for which tags are to be added or updated. The ARN must be URL-encoded.
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
     * @param {String} resourceArn ARN of the resource for which tags are to be removed. The ARN must be URL-encoded.
     * @param {Array.<String>} tagKeys Array of tags to be removed. Array of maps, each of the form s<code>tring:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.
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
     * Callback function to receive the result of the updateChannel operation.
     * @callback module:api/DefaultApi~updateChannelCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UpdateChannelResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates a channel's configuration. Live channels cannot be updated. You must stop the ongoing stream, update the channel, and restart the stream for the changes to take effect.
     * @param {module:model/UpdateChannelRequest} updateChannelRequest 
     * @param {Object} opts Optional parameters
     * @param {String} [xAmzContentSha256] 
     * @param {String} [xAmzDate] 
     * @param {String} [xAmzAlgorithm] 
     * @param {String} [xAmzCredential] 
     * @param {String} [xAmzSecurityToken] 
     * @param {String} [xAmzSignature] 
     * @param {String} [xAmzSignedHeaders] 
     * @param {module:api/DefaultApi~updateChannelCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UpdateChannelResponse}
     */
    updateChannel(updateChannelRequest, opts, callback) {
      opts = opts || {};
      let postBody = updateChannelRequest;
      // verify the required parameter 'updateChannelRequest' is set
      if (updateChannelRequest === undefined || updateChannelRequest === null) {
        throw new Error("Missing the required parameter 'updateChannelRequest' when calling updateChannel");
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
      let returnType = UpdateChannelResponse;
      return this.apiClient.callApi(
        '/UpdateChannel', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
