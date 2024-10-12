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

#include "OAIDefaultApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIDefaultApi::OAIDefaultApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIDefaultApi::~OAIDefaultApi() {
}

void OAIDefaultApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://ivs.{region}.amazonaws.com"),
    "The Amazon IVS multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://ivs.{region}.amazonaws.com"),
    "The Amazon IVS multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://ivs.{region}.amazonaws.com.cn"),
    "The Amazon IVS endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://ivs.{region}.amazonaws.com.cn"),
    "The Amazon IVS endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    _serverConfigs.insert("batchGetChannel", defaultConf);
    _serverIndices.insert("batchGetChannel", 0);
    _serverConfigs.insert("batchGetStreamKey", defaultConf);
    _serverIndices.insert("batchGetStreamKey", 0);
    _serverConfigs.insert("batchStartViewerSessionRevocation", defaultConf);
    _serverIndices.insert("batchStartViewerSessionRevocation", 0);
    _serverConfigs.insert("createChannel", defaultConf);
    _serverIndices.insert("createChannel", 0);
    _serverConfigs.insert("createRecordingConfiguration", defaultConf);
    _serverIndices.insert("createRecordingConfiguration", 0);
    _serverConfigs.insert("createStreamKey", defaultConf);
    _serverIndices.insert("createStreamKey", 0);
    _serverConfigs.insert("deleteChannel", defaultConf);
    _serverIndices.insert("deleteChannel", 0);
    _serverConfigs.insert("deletePlaybackKeyPair", defaultConf);
    _serverIndices.insert("deletePlaybackKeyPair", 0);
    _serverConfigs.insert("deleteRecordingConfiguration", defaultConf);
    _serverIndices.insert("deleteRecordingConfiguration", 0);
    _serverConfigs.insert("deleteStreamKey", defaultConf);
    _serverIndices.insert("deleteStreamKey", 0);
    _serverConfigs.insert("getChannel", defaultConf);
    _serverIndices.insert("getChannel", 0);
    _serverConfigs.insert("getPlaybackKeyPair", defaultConf);
    _serverIndices.insert("getPlaybackKeyPair", 0);
    _serverConfigs.insert("getRecordingConfiguration", defaultConf);
    _serverIndices.insert("getRecordingConfiguration", 0);
    _serverConfigs.insert("getStream", defaultConf);
    _serverIndices.insert("getStream", 0);
    _serverConfigs.insert("getStreamKey", defaultConf);
    _serverIndices.insert("getStreamKey", 0);
    _serverConfigs.insert("getStreamSession", defaultConf);
    _serverIndices.insert("getStreamSession", 0);
    _serverConfigs.insert("importPlaybackKeyPair", defaultConf);
    _serverIndices.insert("importPlaybackKeyPair", 0);
    _serverConfigs.insert("listChannels", defaultConf);
    _serverIndices.insert("listChannels", 0);
    _serverConfigs.insert("listPlaybackKeyPairs", defaultConf);
    _serverIndices.insert("listPlaybackKeyPairs", 0);
    _serverConfigs.insert("listRecordingConfigurations", defaultConf);
    _serverIndices.insert("listRecordingConfigurations", 0);
    _serverConfigs.insert("listStreamKeys", defaultConf);
    _serverIndices.insert("listStreamKeys", 0);
    _serverConfigs.insert("listStreamSessions", defaultConf);
    _serverIndices.insert("listStreamSessions", 0);
    _serverConfigs.insert("listStreams", defaultConf);
    _serverIndices.insert("listStreams", 0);
    _serverConfigs.insert("listTagsForResource", defaultConf);
    _serverIndices.insert("listTagsForResource", 0);
    _serverConfigs.insert("putMetadata", defaultConf);
    _serverIndices.insert("putMetadata", 0);
    _serverConfigs.insert("startViewerSessionRevocation", defaultConf);
    _serverIndices.insert("startViewerSessionRevocation", 0);
    _serverConfigs.insert("stopStream", defaultConf);
    _serverIndices.insert("stopStream", 0);
    _serverConfigs.insert("tagResource", defaultConf);
    _serverIndices.insert("tagResource", 0);
    _serverConfigs.insert("untagResource", defaultConf);
    _serverIndices.insert("untagResource", 0);
    _serverConfigs.insert("updateChannel", defaultConf);
    _serverIndices.insert("updateChannel", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIDefaultApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIDefaultApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIDefaultApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIDefaultApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIDefaultApi::setUsername(const QString &username) {
    _username = username;
}

void OAIDefaultApi::setPassword(const QString &password) {
    _password = password;
}


void OAIDefaultApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIDefaultApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIDefaultApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAIDefaultApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIDefaultApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAIDefaultApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIDefaultApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIDefaultApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIDefaultApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIDefaultApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIDefaultApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAIDefaultApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAIDefaultApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAIDefaultApi::batchGetChannel(const OAIBatchGetChannel_request &oai_batch_get_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["batchGetChannel"][_serverIndices.value("batchGetChannel")].URL()+"/BatchGetChannel");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_batch_get_channel_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::batchGetChannelCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::batchGetChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBatchGetChannelResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT batchGetChannelSignal(output);
        Q_EMIT batchGetChannelSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT batchGetChannelSignalE(output, error_type, error_str);
        Q_EMIT batchGetChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT batchGetChannelSignalError(output, error_type, error_str);
        Q_EMIT batchGetChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::batchGetStreamKey(const OAIBatchGetStreamKey_request &oai_batch_get_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["batchGetStreamKey"][_serverIndices.value("batchGetStreamKey")].URL()+"/BatchGetStreamKey");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_batch_get_stream_key_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::batchGetStreamKeyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::batchGetStreamKeyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBatchGetStreamKeyResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT batchGetStreamKeySignal(output);
        Q_EMIT batchGetStreamKeySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT batchGetStreamKeySignalE(output, error_type, error_str);
        Q_EMIT batchGetStreamKeySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT batchGetStreamKeySignalError(output, error_type, error_str);
        Q_EMIT batchGetStreamKeySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::batchStartViewerSessionRevocation(const OAIBatchStartViewerSessionRevocation_request &oai_batch_start_viewer_session_revocation_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["batchStartViewerSessionRevocation"][_serverIndices.value("batchStartViewerSessionRevocation")].URL()+"/BatchStartViewerSessionRevocation");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_batch_start_viewer_session_revocation_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::batchStartViewerSessionRevocationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::batchStartViewerSessionRevocationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIBatchStartViewerSessionRevocationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT batchStartViewerSessionRevocationSignal(output);
        Q_EMIT batchStartViewerSessionRevocationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT batchStartViewerSessionRevocationSignalE(output, error_type, error_str);
        Q_EMIT batchStartViewerSessionRevocationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT batchStartViewerSessionRevocationSignalError(output, error_type, error_str);
        Q_EMIT batchStartViewerSessionRevocationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createChannel(const OAICreateChannel_request &oai_create_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createChannel"][_serverIndices.value("createChannel")].URL()+"/CreateChannel");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_channel_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createChannelCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateChannelResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createChannelSignal(output);
        Q_EMIT createChannelSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createChannelSignalE(output, error_type, error_str);
        Q_EMIT createChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createChannelSignalError(output, error_type, error_str);
        Q_EMIT createChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createRecordingConfiguration(const OAICreateRecordingConfiguration_request &oai_create_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createRecordingConfiguration"][_serverIndices.value("createRecordingConfiguration")].URL()+"/CreateRecordingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_recording_configuration_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createRecordingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createRecordingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateRecordingConfigurationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createRecordingConfigurationSignal(output);
        Q_EMIT createRecordingConfigurationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createRecordingConfigurationSignalE(output, error_type, error_str);
        Q_EMIT createRecordingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createRecordingConfigurationSignalError(output, error_type, error_str);
        Q_EMIT createRecordingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createStreamKey(const OAICreateStreamKey_request &oai_create_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createStreamKey"][_serverIndices.value("createStreamKey")].URL()+"/CreateStreamKey");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_stream_key_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createStreamKeyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createStreamKeyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateStreamKeyResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createStreamKeySignal(output);
        Q_EMIT createStreamKeySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT createStreamKeySignalE(output, error_type, error_str);
        Q_EMIT createStreamKeySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createStreamKeySignalError(output, error_type, error_str);
        Q_EMIT createStreamKeySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteChannel(const OAIDeleteChannel_request &oai_delete_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteChannel"][_serverIndices.value("deleteChannel")].URL()+"/DeleteChannel");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_channel_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteChannelCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteChannelSignal();
        Q_EMIT deleteChannelSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteChannelSignalE(error_type, error_str);
        Q_EMIT deleteChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteChannelSignalError(error_type, error_str);
        Q_EMIT deleteChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deletePlaybackKeyPair(const OAIDeletePlaybackKeyPair_request &oai_delete_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deletePlaybackKeyPair"][_serverIndices.value("deletePlaybackKeyPair")].URL()+"/DeletePlaybackKeyPair");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_playback_key_pair_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deletePlaybackKeyPairCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deletePlaybackKeyPairCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deletePlaybackKeyPairSignal(output);
        Q_EMIT deletePlaybackKeyPairSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deletePlaybackKeyPairSignalE(output, error_type, error_str);
        Q_EMIT deletePlaybackKeyPairSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deletePlaybackKeyPairSignalError(output, error_type, error_str);
        Q_EMIT deletePlaybackKeyPairSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteRecordingConfiguration(const OAIDeleteRecordingConfiguration_request &oai_delete_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteRecordingConfiguration"][_serverIndices.value("deleteRecordingConfiguration")].URL()+"/DeleteRecordingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_recording_configuration_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteRecordingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteRecordingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteRecordingConfigurationSignal();
        Q_EMIT deleteRecordingConfigurationSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteRecordingConfigurationSignalE(error_type, error_str);
        Q_EMIT deleteRecordingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteRecordingConfigurationSignalError(error_type, error_str);
        Q_EMIT deleteRecordingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteStreamKey(const OAIDeleteStreamKey_request &oai_delete_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteStreamKey"][_serverIndices.value("deleteStreamKey")].URL()+"/DeleteStreamKey");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_stream_key_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteStreamKeyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteStreamKeyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteStreamKeySignal();
        Q_EMIT deleteStreamKeySignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT deleteStreamKeySignalE(error_type, error_str);
        Q_EMIT deleteStreamKeySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteStreamKeySignalError(error_type, error_str);
        Q_EMIT deleteStreamKeySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getChannel(const OAIGetChannel_request &oai_get_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getChannel"][_serverIndices.value("getChannel")].URL()+"/GetChannel");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_channel_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getChannelCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetChannelResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getChannelSignal(output);
        Q_EMIT getChannelSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getChannelSignalE(output, error_type, error_str);
        Q_EMIT getChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getChannelSignalError(output, error_type, error_str);
        Q_EMIT getChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getPlaybackKeyPair(const OAIGetPlaybackKeyPair_request &oai_get_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getPlaybackKeyPair"][_serverIndices.value("getPlaybackKeyPair")].URL()+"/GetPlaybackKeyPair");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_playback_key_pair_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getPlaybackKeyPairCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getPlaybackKeyPairCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetPlaybackKeyPairResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getPlaybackKeyPairSignal(output);
        Q_EMIT getPlaybackKeyPairSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getPlaybackKeyPairSignalE(output, error_type, error_str);
        Q_EMIT getPlaybackKeyPairSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getPlaybackKeyPairSignalError(output, error_type, error_str);
        Q_EMIT getPlaybackKeyPairSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRecordingConfiguration(const OAIGetRecordingConfiguration_request &oai_get_recording_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getRecordingConfiguration"][_serverIndices.value("getRecordingConfiguration")].URL()+"/GetRecordingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_recording_configuration_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRecordingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRecordingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRecordingConfigurationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRecordingConfigurationSignal(output);
        Q_EMIT getRecordingConfigurationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getRecordingConfigurationSignalE(output, error_type, error_str);
        Q_EMIT getRecordingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRecordingConfigurationSignalError(output, error_type, error_str);
        Q_EMIT getRecordingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getStream(const OAIGetStream_request &oai_get_stream_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getStream"][_serverIndices.value("getStream")].URL()+"/GetStream");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_stream_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getStreamCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getStreamCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetStreamResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getStreamSignal(output);
        Q_EMIT getStreamSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getStreamSignalE(output, error_type, error_str);
        Q_EMIT getStreamSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getStreamSignalError(output, error_type, error_str);
        Q_EMIT getStreamSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getStreamKey(const OAIGetStreamKey_request &oai_get_stream_key_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getStreamKey"][_serverIndices.value("getStreamKey")].URL()+"/GetStreamKey");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_stream_key_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getStreamKeyCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getStreamKeyCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetStreamKeyResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getStreamKeySignal(output);
        Q_EMIT getStreamKeySignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getStreamKeySignalE(output, error_type, error_str);
        Q_EMIT getStreamKeySignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getStreamKeySignalError(output, error_type, error_str);
        Q_EMIT getStreamKeySignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getStreamSession(const OAIGetStreamSession_request &oai_get_stream_session_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getStreamSession"][_serverIndices.value("getStreamSession")].URL()+"/GetStreamSession");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_stream_session_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getStreamSessionCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getStreamSessionCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetStreamSessionResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getStreamSessionSignal(output);
        Q_EMIT getStreamSessionSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getStreamSessionSignalE(output, error_type, error_str);
        Q_EMIT getStreamSessionSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getStreamSessionSignalError(output, error_type, error_str);
        Q_EMIT getStreamSessionSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::importPlaybackKeyPair(const OAIImportPlaybackKeyPair_request &oai_import_playback_key_pair_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["importPlaybackKeyPair"][_serverIndices.value("importPlaybackKeyPair")].URL()+"/ImportPlaybackKeyPair");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_import_playback_key_pair_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::importPlaybackKeyPairCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::importPlaybackKeyPairCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIImportPlaybackKeyPairResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT importPlaybackKeyPairSignal(output);
        Q_EMIT importPlaybackKeyPairSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT importPlaybackKeyPairSignalE(output, error_type, error_str);
        Q_EMIT importPlaybackKeyPairSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT importPlaybackKeyPairSignalError(output, error_type, error_str);
        Q_EMIT importPlaybackKeyPairSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listChannels(const OAIListChannels_request &oai_list_channels_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listChannels"][_serverIndices.value("listChannels")].URL()+"/ListChannels");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_channels_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listChannelsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listChannelsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListChannelsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listChannelsSignal(output);
        Q_EMIT listChannelsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listChannelsSignalE(output, error_type, error_str);
        Q_EMIT listChannelsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listChannelsSignalError(output, error_type, error_str);
        Q_EMIT listChannelsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listPlaybackKeyPairs(const OAIListPlaybackKeyPairs_request &oai_list_playback_key_pairs_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listPlaybackKeyPairs"][_serverIndices.value("listPlaybackKeyPairs")].URL()+"/ListPlaybackKeyPairs");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_playback_key_pairs_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listPlaybackKeyPairsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listPlaybackKeyPairsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListPlaybackKeyPairsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listPlaybackKeyPairsSignal(output);
        Q_EMIT listPlaybackKeyPairsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listPlaybackKeyPairsSignalE(output, error_type, error_str);
        Q_EMIT listPlaybackKeyPairsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listPlaybackKeyPairsSignalError(output, error_type, error_str);
        Q_EMIT listPlaybackKeyPairsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listRecordingConfigurations(const OAIListRecordingConfigurations_request &oai_list_recording_configurations_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listRecordingConfigurations"][_serverIndices.value("listRecordingConfigurations")].URL()+"/ListRecordingConfigurations");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_recording_configurations_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listRecordingConfigurationsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listRecordingConfigurationsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListRecordingConfigurationsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listRecordingConfigurationsSignal(output);
        Q_EMIT listRecordingConfigurationsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listRecordingConfigurationsSignalE(output, error_type, error_str);
        Q_EMIT listRecordingConfigurationsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listRecordingConfigurationsSignalError(output, error_type, error_str);
        Q_EMIT listRecordingConfigurationsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listStreamKeys(const OAIListStreamKeys_request &oai_list_stream_keys_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listStreamKeys"][_serverIndices.value("listStreamKeys")].URL()+"/ListStreamKeys");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_stream_keys_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listStreamKeysCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listStreamKeysCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListStreamKeysResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listStreamKeysSignal(output);
        Q_EMIT listStreamKeysSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listStreamKeysSignalE(output, error_type, error_str);
        Q_EMIT listStreamKeysSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listStreamKeysSignalError(output, error_type, error_str);
        Q_EMIT listStreamKeysSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listStreamSessions(const OAIListStreamSessions_request &oai_list_stream_sessions_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listStreamSessions"][_serverIndices.value("listStreamSessions")].URL()+"/ListStreamSessions");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_stream_sessions_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listStreamSessionsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listStreamSessionsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListStreamSessionsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listStreamSessionsSignal(output);
        Q_EMIT listStreamSessionsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listStreamSessionsSignalE(output, error_type, error_str);
        Q_EMIT listStreamSessionsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listStreamSessionsSignalError(output, error_type, error_str);
        Q_EMIT listStreamSessionsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listStreams(const OAIListStreams_request &oai_list_streams_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listStreams"][_serverIndices.value("listStreams")].URL()+"/ListStreams");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (max_results.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "maxResults", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("maxResults")).append(querySuffix).append(QUrl::toPercentEncoding(max_results.stringValue()));
    }
    if (next_token.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "nextToken", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("nextToken")).append(querySuffix).append(QUrl::toPercentEncoding(next_token.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_list_streams_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listStreamsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listStreamsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListStreamsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listStreamsSignal(output);
        Q_EMIT listStreamsSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listStreamsSignalE(output, error_type, error_str);
        Q_EMIT listStreamsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listStreamsSignalError(output, error_type, error_str);
        Q_EMIT listStreamsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["listTagsForResource"][_serverIndices.value("listTagsForResource")].URL()+"/tags/{resourceArn}");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    
    {
        QString resource_arnPathParam("{");
        resource_arnPathParam.append("resourceArn").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resourceArn", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resourceArn"+pathSuffix : pathPrefix;
        fullPath.replace(resource_arnPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource_arn)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listTagsForResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listTagsForResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListTagsForResourceResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listTagsForResourceSignal(output);
        Q_EMIT listTagsForResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT listTagsForResourceSignalE(output, error_type, error_str);
        Q_EMIT listTagsForResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listTagsForResourceSignalError(output, error_type, error_str);
        Q_EMIT listTagsForResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::putMetadata(const OAIPutMetadata_request &oai_put_metadata_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["putMetadata"][_serverIndices.value("putMetadata")].URL()+"/PutMetadata");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_put_metadata_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::putMetadataCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::putMetadataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT putMetadataSignal();
        Q_EMIT putMetadataSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT putMetadataSignalE(error_type, error_str);
        Q_EMIT putMetadataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT putMetadataSignalError(error_type, error_str);
        Q_EMIT putMetadataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::startViewerSessionRevocation(const OAIStartViewerSessionRevocation_request &oai_start_viewer_session_revocation_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["startViewerSessionRevocation"][_serverIndices.value("startViewerSessionRevocation")].URL()+"/StartViewerSessionRevocation");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_start_viewer_session_revocation_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::startViewerSessionRevocationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::startViewerSessionRevocationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT startViewerSessionRevocationSignal(output);
        Q_EMIT startViewerSessionRevocationSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT startViewerSessionRevocationSignalE(output, error_type, error_str);
        Q_EMIT startViewerSessionRevocationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT startViewerSessionRevocationSignalError(output, error_type, error_str);
        Q_EMIT startViewerSessionRevocationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::stopStream(const OAIStopStream_request &oai_stop_stream_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["stopStream"][_serverIndices.value("stopStream")].URL()+"/StopStream");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_stop_stream_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::stopStreamCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::stopStreamCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT stopStreamSignal(output);
        Q_EMIT stopStreamSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT stopStreamSignalE(output, error_type, error_str);
        Q_EMIT stopStreamSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT stopStreamSignalError(output, error_type, error_str);
        Q_EMIT stopStreamSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["tagResource"][_serverIndices.value("tagResource")].URL()+"/tags/{resourceArn}");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    
    {
        QString resource_arnPathParam("{");
        resource_arnPathParam.append("resourceArn").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resourceArn", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resourceArn"+pathSuffix : pathPrefix;
        fullPath.replace(resource_arnPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource_arn)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_tag_resource_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::tagResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::tagResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT tagResourceSignal(output);
        Q_EMIT tagResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT tagResourceSignalE(output, error_type, error_str);
        Q_EMIT tagResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT tagResourceSignalError(output, error_type, error_str);
        Q_EMIT tagResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::untagResource(const QString &resource_arn, const QList<QString> &tag_keys, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["untagResource"][_serverIndices.value("untagResource")].URL()+"/tags/{resourceArn}#tagKeys");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    
    {
        QString resource_arnPathParam("{");
        resource_arnPathParam.append("resourceArn").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "resourceArn", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"resourceArn"+pathSuffix : pathPrefix;
        fullPath.replace(resource_arnPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(resource_arn)));
    }
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "tagKeys", true);
        if (tag_keys.size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QString t : tag_keys) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("tagKeys=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("tagKeys").append(querySuffix);
                qint32 count = 0;
                for (QString t : tag_keys) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("tagKeys").append(querySuffix);
                qint32 count = 0;
                for (QString t : tag_keys) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("tagKeys").append(querySuffix);
                qint32 count = 0;
                for (QString t : tag_keys) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("tagKeys").append(querySuffix);
                qint32 count = 0;
                for (QString t : tag_keys) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("tagKeys").append(querySuffix);
                qint32 count = 0;
                for (QString t : tag_keys) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "DELETE");


    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::untagResourceCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::untagResourceCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT untagResourceSignal(output);
        Q_EMIT untagResourceSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT untagResourceSignalE(output, error_type, error_str);
        Q_EMIT untagResourceSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT untagResourceSignalError(output, error_type, error_str);
        Q_EMIT untagResourceSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateChannel(const OAIUpdateChannel_request &oai_update_channel_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateChannel"][_serverIndices.value("updateChannel")].URL()+"/UpdateChannel");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_channel_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    if (x_amz_content_sha256.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_content_sha256.value()).isEmpty()) {
            input.headers.insert("X-Amz-Content-Sha256", ::OpenAPI::toStringValue(x_amz_content_sha256.value()));
        }
        }
    if (x_amz_date.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_date.value()).isEmpty()) {
            input.headers.insert("X-Amz-Date", ::OpenAPI::toStringValue(x_amz_date.value()));
        }
        }
    if (x_amz_algorithm.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_algorithm.value()).isEmpty()) {
            input.headers.insert("X-Amz-Algorithm", ::OpenAPI::toStringValue(x_amz_algorithm.value()));
        }
        }
    if (x_amz_credential.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_credential.value()).isEmpty()) {
            input.headers.insert("X-Amz-Credential", ::OpenAPI::toStringValue(x_amz_credential.value()));
        }
        }
    if (x_amz_security_token.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_security_token.value()).isEmpty()) {
            input.headers.insert("X-Amz-Security-Token", ::OpenAPI::toStringValue(x_amz_security_token.value()));
        }
        }
    if (x_amz_signature.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signature.value()).isEmpty()) {
            input.headers.insert("X-Amz-Signature", ::OpenAPI::toStringValue(x_amz_signature.value()));
        }
        }
    if (x_amz_signed_headers.hasValue())
    {
        if (!::OpenAPI::toStringValue(x_amz_signed_headers.value()).isEmpty()) {
            input.headers.insert("X-Amz-SignedHeaders", ::OpenAPI::toStringValue(x_amz_signed_headers.value()));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateChannelCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateChannelCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateChannelResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateChannelSignal(output);
        Q_EMIT updateChannelSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT updateChannelSignalE(output, error_type, error_str);
        Q_EMIT updateChannelSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateChannelSignalError(output, error_type, error_str);
        Q_EMIT updateChannelSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
