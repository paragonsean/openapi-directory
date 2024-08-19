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

import ApiClient from '../ApiClient';

/**
 * The UpdateChannelRequest model module.
 * @module model/UpdateChannelRequest
 * @version 2020-07-14
 */
class UpdateChannelRequest {
    /**
     * Constructs a new <code>UpdateChannelRequest</code>.
     * @alias module:model/UpdateChannelRequest
     * @param arn {String} ARN of the channel to be updated.
     */
    constructor(arn) { 
        
        UpdateChannelRequest.initialize(this, arn);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, arn) { 
        obj['arn'] = arn;
    }

    /**
     * Constructs a <code>UpdateChannelRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateChannelRequest} obj Optional instance to populate.
     * @return {module:model/UpdateChannelRequest} The populated <code>UpdateChannelRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateChannelRequest();

            if (data.hasOwnProperty('arn')) {
                obj['arn'] = ApiClient.convertToType(data['arn'], 'String');
            }
            if (data.hasOwnProperty('authorized')) {
                obj['authorized'] = ApiClient.convertToType(data['authorized'], 'Boolean');
            }
            if (data.hasOwnProperty('insecureIngest')) {
                obj['insecureIngest'] = ApiClient.convertToType(data['insecureIngest'], 'Boolean');
            }
            if (data.hasOwnProperty('latencyMode')) {
                obj['latencyMode'] = ApiClient.convertToType(data['latencyMode'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('preset')) {
                obj['preset'] = ApiClient.convertToType(data['preset'], 'String');
            }
            if (data.hasOwnProperty('recordingConfigurationArn')) {
                obj['recordingConfigurationArn'] = ApiClient.convertToType(data['recordingConfigurationArn'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateChannelRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateChannelRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateChannelRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['arn'] && !(typeof data['arn'] === 'string' || data['arn'] instanceof String)) {
            throw new Error("Expected the field `arn` to be a primitive type in the JSON string but got " + data['arn']);
        }
        // ensure the json data is a string
        if (data['latencyMode'] && !(typeof data['latencyMode'] === 'string' || data['latencyMode'] instanceof String)) {
            throw new Error("Expected the field `latencyMode` to be a primitive type in the JSON string but got " + data['latencyMode']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['preset'] && !(typeof data['preset'] === 'string' || data['preset'] instanceof String)) {
            throw new Error("Expected the field `preset` to be a primitive type in the JSON string but got " + data['preset']);
        }
        // ensure the json data is a string
        if (data['recordingConfigurationArn'] && !(typeof data['recordingConfigurationArn'] === 'string' || data['recordingConfigurationArn'] instanceof String)) {
            throw new Error("Expected the field `recordingConfigurationArn` to be a primitive type in the JSON string but got " + data['recordingConfigurationArn']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

UpdateChannelRequest.RequiredProperties = ["arn"];

/**
 * ARN of the channel to be updated.
 * @member {String} arn
 */
UpdateChannelRequest.prototype['arn'] = undefined;

/**
 * Whether the channel is private (enabled for playback authorization).
 * @member {Boolean} authorized
 */
UpdateChannelRequest.prototype['authorized'] = undefined;

/**
 * Whether the channel allows insecure RTMP ingest. Default: <code>false</code>.
 * @member {Boolean} insecureIngest
 */
UpdateChannelRequest.prototype['insecureIngest'] = undefined;

/**
 * Channel latency mode. Use <code>NORMAL</code> to broadcast and deliver live video up to Full HD. Use <code>LOW</code> for near-real-time interaction with viewers. (Note: In the Amazon IVS console, <code>LOW</code> and <code>NORMAL</code> correspond to Ultra-low and Standard, respectively.)
 * @member {module:model/UpdateChannelRequest.LatencyModeEnum} latencyMode
 */
UpdateChannelRequest.prototype['latencyMode'] = undefined;

/**
 * Channel name.
 * @member {String} name
 */
UpdateChannelRequest.prototype['name'] = undefined;

/**
 * Optional transcode preset for the channel. This is selectable only for <code>ADVANCED_HD</code> and <code>ADVANCED_SD</code> channel types. For those channel types, the default <code>preset</code> is <code>HIGHER_BANDWIDTH_DELIVERY</code>. For other channel types (<code>BASIC</code> and <code>STANDARD</code>), <code>preset</code> is the empty string (<code>\"\"</code>).
 * @member {module:model/UpdateChannelRequest.PresetEnum} preset
 */
UpdateChannelRequest.prototype['preset'] = undefined;

/**
 * Recording-configuration ARN. If this is set to an empty string, recording is disabled. A value other than an empty string indicates that recording is enabled
 * @member {String} recordingConfigurationArn
 */
UpdateChannelRequest.prototype['recordingConfigurationArn'] = undefined;

/**
 * <p>Channel type, which determines the allowable resolution and bitrate. <i>If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.</i> Some types generate multiple qualities (renditions) from the original input; this automatically gives viewers the best experience for their devices and network conditions. Some types provide transcoded video; transcoding allows higher playback quality across a range of download speeds. Default: <code>STANDARD</code>. Valid values:</p> <ul> <li> <p> <code>BASIC</code>: Video is transmuxed: Amazon IVS delivers the original input quality to viewers. The viewer’s video-quality choice is limited to the original input. Input resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. Original audio is passed through.</p> </li> <li> <p> <code>STANDARD</code>: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default when you create a channel.</p> </li> <li> <p> <code>ADVANCED_SD</code>: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.</p> </li> <li> <p> <code>ADVANCED_HD</code>: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.</p> </li> </ul> <p>Optional <i>transcode presets</i> (available for the <code>ADVANCED</code> types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets:</p> <ul> <li> <p> <i>Constrained bandwidth delivery</i> uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads)</p> </li> <li> <p> <i>Higher bandwidth delivery</i> uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes).</p> </li> </ul>
 * @member {module:model/UpdateChannelRequest.TypeEnum} type
 */
UpdateChannelRequest.prototype['type'] = undefined;





/**
 * Allowed values for the <code>latencyMode</code> property.
 * @enum {String}
 * @readonly
 */
UpdateChannelRequest['LatencyModeEnum'] = {

    /**
     * value: "NORMAL"
     * @const
     */
    "NORMAL": "NORMAL",

    /**
     * value: "LOW"
     * @const
     */
    "LOW": "LOW"
};


/**
 * Allowed values for the <code>preset</code> property.
 * @enum {String}
 * @readonly
 */
UpdateChannelRequest['PresetEnum'] = {

    /**
     * value: "HIGHER_BANDWIDTH_DELIVERY"
     * @const
     */
    "HIGHER_BANDWIDTH_DELIVERY": "HIGHER_BANDWIDTH_DELIVERY",

    /**
     * value: "CONSTRAINED_BANDWIDTH_DELIVERY"
     * @const
     */
    "CONSTRAINED_BANDWIDTH_DELIVERY": "CONSTRAINED_BANDWIDTH_DELIVERY"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
UpdateChannelRequest['TypeEnum'] = {

    /**
     * value: "BASIC"
     * @const
     */
    "BASIC": "BASIC",

    /**
     * value: "STANDARD"
     * @const
     */
    "STANDARD": "STANDARD",

    /**
     * value: "ADVANCED_SD"
     * @const
     */
    "ADVANCED_SD": "ADVANCED_SD",

    /**
     * value: "ADVANCED_HD"
     * @const
     */
    "ADVANCED_HD": "ADVANCED_HD"
};



export default UpdateChannelRequest;

