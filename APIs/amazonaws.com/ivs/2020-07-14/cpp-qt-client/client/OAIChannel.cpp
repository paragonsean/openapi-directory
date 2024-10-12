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
 */

#include "OAIChannel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIChannel::OAIChannel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIChannel::OAIChannel() {
    this->initializeModel();
}

OAIChannel::~OAIChannel() {}

void OAIChannel::initializeModel() {

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_authorized_isSet = false;
    m_authorized_isValid = false;

    m_ingest_endpoint_isSet = false;
    m_ingest_endpoint_isValid = false;

    m_insecure_ingest_isSet = false;
    m_insecure_ingest_isValid = false;

    m_latency_mode_isSet = false;
    m_latency_mode_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_playback_url_isSet = false;
    m_playback_url_isValid = false;

    m_preset_isSet = false;
    m_preset_isValid = false;

    m_recording_configuration_arn_isSet = false;
    m_recording_configuration_arn_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIChannel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIChannel::fromJsonObject(QJsonObject json) {

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_authorized_isValid = ::OpenAPI::fromJsonValue(m_authorized, json[QString("authorized")]);
    m_authorized_isSet = !json[QString("authorized")].isNull() && m_authorized_isValid;

    m_ingest_endpoint_isValid = ::OpenAPI::fromJsonValue(m_ingest_endpoint, json[QString("ingestEndpoint")]);
    m_ingest_endpoint_isSet = !json[QString("ingestEndpoint")].isNull() && m_ingest_endpoint_isValid;

    m_insecure_ingest_isValid = ::OpenAPI::fromJsonValue(m_insecure_ingest, json[QString("insecureIngest")]);
    m_insecure_ingest_isSet = !json[QString("insecureIngest")].isNull() && m_insecure_ingest_isValid;

    m_latency_mode_isValid = ::OpenAPI::fromJsonValue(m_latency_mode, json[QString("latencyMode")]);
    m_latency_mode_isSet = !json[QString("latencyMode")].isNull() && m_latency_mode_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_playback_url_isValid = ::OpenAPI::fromJsonValue(m_playback_url, json[QString("playbackUrl")]);
    m_playback_url_isSet = !json[QString("playbackUrl")].isNull() && m_playback_url_isValid;

    m_preset_isValid = ::OpenAPI::fromJsonValue(m_preset, json[QString("preset")]);
    m_preset_isSet = !json[QString("preset")].isNull() && m_preset_isValid;

    m_recording_configuration_arn_isValid = ::OpenAPI::fromJsonValue(m_recording_configuration_arn, json[QString("recordingConfigurationArn")]);
    m_recording_configuration_arn_isSet = !json[QString("recordingConfigurationArn")].isNull() && m_recording_configuration_arn_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIChannel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIChannel::asJsonObject() const {
    QJsonObject obj;
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_authorized_isSet) {
        obj.insert(QString("authorized"), ::OpenAPI::toJsonValue(m_authorized));
    }
    if (m_ingest_endpoint_isSet) {
        obj.insert(QString("ingestEndpoint"), ::OpenAPI::toJsonValue(m_ingest_endpoint));
    }
    if (m_insecure_ingest_isSet) {
        obj.insert(QString("insecureIngest"), ::OpenAPI::toJsonValue(m_insecure_ingest));
    }
    if (m_latency_mode.isSet()) {
        obj.insert(QString("latencyMode"), ::OpenAPI::toJsonValue(m_latency_mode));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_playback_url_isSet) {
        obj.insert(QString("playbackUrl"), ::OpenAPI::toJsonValue(m_playback_url));
    }
    if (m_preset.isSet()) {
        obj.insert(QString("preset"), ::OpenAPI::toJsonValue(m_preset));
    }
    if (m_recording_configuration_arn_isSet) {
        obj.insert(QString("recordingConfigurationArn"), ::OpenAPI::toJsonValue(m_recording_configuration_arn));
    }
    if (m_tags.isSet()) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIChannel::getArn() const {
    return m_arn;
}
void OAIChannel::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIChannel::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIChannel::is_arn_Valid() const{
    return m_arn_isValid;
}

bool OAIChannel::getAuthorized() const {
    return m_authorized;
}
void OAIChannel::setAuthorized(const bool &authorized) {
    m_authorized = authorized;
    m_authorized_isSet = true;
}

bool OAIChannel::is_authorized_Set() const{
    return m_authorized_isSet;
}

bool OAIChannel::is_authorized_Valid() const{
    return m_authorized_isValid;
}

QString OAIChannel::getIngestEndpoint() const {
    return m_ingest_endpoint;
}
void OAIChannel::setIngestEndpoint(const QString &ingest_endpoint) {
    m_ingest_endpoint = ingest_endpoint;
    m_ingest_endpoint_isSet = true;
}

bool OAIChannel::is_ingest_endpoint_Set() const{
    return m_ingest_endpoint_isSet;
}

bool OAIChannel::is_ingest_endpoint_Valid() const{
    return m_ingest_endpoint_isValid;
}

bool OAIChannel::getInsecureIngest() const {
    return m_insecure_ingest;
}
void OAIChannel::setInsecureIngest(const bool &insecure_ingest) {
    m_insecure_ingest = insecure_ingest;
    m_insecure_ingest_isSet = true;
}

bool OAIChannel::is_insecure_ingest_Set() const{
    return m_insecure_ingest_isSet;
}

bool OAIChannel::is_insecure_ingest_Valid() const{
    return m_insecure_ingest_isValid;
}

OAIChannelLatencyMode OAIChannel::getLatencyMode() const {
    return m_latency_mode;
}
void OAIChannel::setLatencyMode(const OAIChannelLatencyMode &latency_mode) {
    m_latency_mode = latency_mode;
    m_latency_mode_isSet = true;
}

bool OAIChannel::is_latency_mode_Set() const{
    return m_latency_mode_isSet;
}

bool OAIChannel::is_latency_mode_Valid() const{
    return m_latency_mode_isValid;
}

QString OAIChannel::getName() const {
    return m_name;
}
void OAIChannel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIChannel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIChannel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIChannel::getPlaybackUrl() const {
    return m_playback_url;
}
void OAIChannel::setPlaybackUrl(const QString &playback_url) {
    m_playback_url = playback_url;
    m_playback_url_isSet = true;
}

bool OAIChannel::is_playback_url_Set() const{
    return m_playback_url_isSet;
}

bool OAIChannel::is_playback_url_Valid() const{
    return m_playback_url_isValid;
}

OAITranscodePreset OAIChannel::getPreset() const {
    return m_preset;
}
void OAIChannel::setPreset(const OAITranscodePreset &preset) {
    m_preset = preset;
    m_preset_isSet = true;
}

bool OAIChannel::is_preset_Set() const{
    return m_preset_isSet;
}

bool OAIChannel::is_preset_Valid() const{
    return m_preset_isValid;
}

QString OAIChannel::getRecordingConfigurationArn() const {
    return m_recording_configuration_arn;
}
void OAIChannel::setRecordingConfigurationArn(const QString &recording_configuration_arn) {
    m_recording_configuration_arn = recording_configuration_arn;
    m_recording_configuration_arn_isSet = true;
}

bool OAIChannel::is_recording_configuration_arn_Set() const{
    return m_recording_configuration_arn_isSet;
}

bool OAIChannel::is_recording_configuration_arn_Valid() const{
    return m_recording_configuration_arn_isValid;
}

QMap OAIChannel::getTags() const {
    return m_tags;
}
void OAIChannel::setTags(const QMap &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIChannel::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIChannel::is_tags_Valid() const{
    return m_tags_isValid;
}

OAIChannelType OAIChannel::getType() const {
    return m_type;
}
void OAIChannel::setType(const OAIChannelType &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIChannel::is_type_Set() const{
    return m_type_isSet;
}

bool OAIChannel::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIChannel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_authorized_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ingest_endpoint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_insecure_ingest_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latency_mode.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_playback_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preset.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_recording_configuration_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIChannel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
