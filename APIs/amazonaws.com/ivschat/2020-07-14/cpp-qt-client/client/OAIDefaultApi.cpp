/**
 * Amazon Interactive Video Service Chat
 * <p> <b>Introduction</b> </p> <p>The Amazon IVS Chat control-plane API enables you to create and manage Amazon IVS Chat resources. You also need to integrate with the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API</a>, to enable users to interact with chat rooms in real time.</p> <p>The API is an AWS regional service. For a list of supported regions and Amazon IVS Chat HTTPS service endpoints, see the Amazon IVS Chat information on the <a href=\"https://docs.aws.amazon.com/general/latest/gr/ivs.html\">Amazon IVS page</a> in the <i>AWS General Reference</i>. </p> <p> <b>Notes on terminology:</b> </p> <ul> <li> <p>You create service applications using the Amazon IVS Chat API. We refer to these as <i>applications</i>.</p> </li> <li> <p>You create front-end client applications (browser and Android/iOS apps) using the Amazon IVS Chat Messaging API. We refer to these as <i>clients</i>. </p> </li> </ul> <p> <b>Resources</b> </p> <p>The following resources are part of Amazon IVS Chat:</p> <ul> <li> <p> <b>LoggingConfiguration</b> — A configuration that allows customers to store and record sent messages in a chat room. See the Logging Configuration endpoints for more information.</p> </li> <li> <p> <b>Room</b> — The central Amazon IVS Chat resource through which clients connect to and exchange chat messages. See the Room endpoints for more information.</p> </li> </ul> <p> <b>Tagging</b> </p> <p>A <i>tag</i> is a metadata label that you assign to an AWS resource. A tag comprises a <i>key</i> and a <i>value</i>, both set by you. For example, you might set a tag as <code>topic:nature</code> to label a particular video category. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging AWS Resources</a> for more information, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS Chat has no service-specific constraints beyond what is documented there.</p> <p>Tags can help you identify and organize your AWS resources. For example, you can use the same tag for different resources to indicate that they are related. You can also use tags to manage access (see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Access Tags</a>).</p> <p>The Amazon IVS Chat API has these tag-related endpoints: <a>TagResource</a>, <a>UntagResource</a>, and <a>ListTagsForResource</a>. The following resource supports tagging: Room.</p> <p>At most 50 tags can be applied to a resource.</p> <p> <b>API Access Security</b> </p> <p>Your Amazon IVS Chat applications (service applications and clients) must be authenticated and authorized to access Amazon IVS Chat resources. Note the differences between these concepts:</p> <ul> <li> <p> <i>Authentication</i> is about verifying identity. Requests to the Amazon IVS Chat API must be signed to verify your identity.</p> </li> <li> <p> <i>Authorization</i> is about granting permissions. Your IAM roles need to have permissions for Amazon IVS Chat API requests.</p> </li> </ul> <p>Users (viewers) connect to a room using secure access tokens that you create using the <a>CreateChatToken</a> endpoint through the AWS SDK. You call CreateChatToken for every user’s chat session, passing identity and authorization information about the user.</p> <p> <b>Signing API Requests</b> </p> <p>HTTP API requests must be signed with an AWS SigV4 signature using your AWS security credentials. The AWS Command Line Interface (CLI) and the AWS SDKs take care of signing the underlying API calls for you. However, if your application calls the Amazon IVS Chat HTTP API directly, it’s your responsibility to sign the requests.</p> <p>You generate a signature using valid AWS credentials for an IAM role that has permission to perform the requested action. For example, DeleteMessage requests must be made using an IAM role that has the <code>ivschat:DeleteMessage</code> permission.</p> <p>For more information:</p> <ul> <li> <p>Authentication and generating signatures — See <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html\">Authenticating Requests (Amazon Web Services Signature Version 4)</a> in the <i>Amazon Web Services General Reference</i>.</p> </li> <li> <p>Managing Amazon IVS permissions — See <a href=\"https://docs.aws.amazon.com/ivs/latest/userguide/security-iam.html\">Identity and Access Management</a> on the Security page of the <i>Amazon IVS User Guide</i>.</p> </li> </ul> <p> <b>Amazon Resource Names (ARNs)</b> </p> <p>ARNs uniquely identify AWS resources. An ARN is required when you need to specify a resource unambiguously across all of AWS, such as in IAM policies and API calls. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names</a> in the <i>AWS General Reference</i>.</p> <p> <b>Messaging Endpoints</b> </p> <ul> <li> <p> <a>DeleteMessage</a> — Sends an event to a specific room which directs clients to delete a specific message; that is, unrender it from view and delete it from the client’s chat history. This event’s <code>EventName</code> is <code>aws:DELETE_MESSAGE</code>. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-deletemessage-publish.html\"> DeleteMessage</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>DisconnectUser</a> — Disconnects all connections using a specified user ID from a room. This replicates the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-disconnectuser-publish.html\"> DisconnectUser</a> WebSocket operation in the Amazon IVS Chat Messaging API.</p> </li> <li> <p> <a>SendEvent</a> — Sends an event to a room. Use this within your application’s business logic to send events to clients of a room; e.g., to notify clients to change the way the chat UI is rendered.</p> </li> </ul> <p> <b>Chat Token Endpoint</b> </p> <ul> <li> <p> <a>CreateChatToken</a> — Creates an encrypted token that is used by a chat participant to establish an individual WebSocket chat connection to a room. When the token is used to connect to chat, the connection is valid for the session duration specified in the request. The token becomes invalid at the token-expiration timestamp included in the response.</p> </li> </ul> <p> <b>Room Endpoints</b> </p> <ul> <li> <p> <a>CreateRoom</a> — Creates a room that allows clients to connect and pass messages.</p> </li> <li> <p> <a>DeleteRoom</a> — Deletes the specified room.</p> </li> <li> <p> <a>GetRoom</a> — Gets the specified room.</p> </li> <li> <p> <a>ListRooms</a> — Gets summary information about all your rooms in the AWS region where the API request is processed. </p> </li> <li> <p> <a>UpdateRoom</a> — Updates a room’s configuration.</p> </li> </ul> <p> <b>Logging Configuration Endpoints</b> </p> <ul> <li> <p> <a>CreateLoggingConfiguration</a> — Creates a logging configuration that allows clients to store and record sent messages.</p> </li> <li> <p> <a>DeleteLoggingConfiguration</a> — Deletes the specified logging configuration.</p> </li> <li> <p> <a>GetLoggingConfiguration</a> — Gets the specified logging configuration.</p> </li> <li> <p> <a>ListLoggingConfigurations</a> — Gets summary information about all your logging configurations in the AWS region where the API request is processed.</p> </li> <li> <p> <a>UpdateLoggingConfiguration</a> — Updates a specified logging configuration.</p> </li> </ul> <p> <b>Tags Endpoints</b> </p> <ul> <li> <p> <a>ListTagsForResource</a> — Gets information about AWS tags for the specified ARN.</p> </li> <li> <p> <a>TagResource</a> — Adds or updates tags for the AWS resource with the specified ARN.</p> </li> <li> <p> <a>UntagResource</a> — Removes tags from the resource with the specified ARN.</p> </li> </ul> <p>All the above are HTTP operations. There is a separate <i>messaging</i> API for managing Chat resources; see the <a href=\"https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/chat-messaging-api.html\"> Amazon IVS Chat Messaging API Reference</a>.</p>
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
    QUrl("http://ivschat.{region}.amazonaws.com"),
    "The ivschat multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://ivschat.{region}.amazonaws.com"),
    "The ivschat multi-region endpoint",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","us-east-1",
    QSet<QString>{ {"us-east-1"},{"us-east-2"},{"us-west-1"},{"us-west-2"},{"us-gov-west-1"},{"us-gov-east-1"},{"ca-central-1"},{"eu-north-1"},{"eu-west-1"},{"eu-west-2"},{"eu-west-3"},{"eu-central-1"},{"eu-south-1"},{"af-south-1"},{"ap-northeast-1"},{"ap-northeast-2"},{"ap-northeast-3"},{"ap-southeast-1"},{"ap-southeast-2"},{"ap-east-1"},{"ap-south-1"},{"sa-east-1"},{"me-south-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("http://ivschat.{region}.amazonaws.com.cn"),
    "The ivschat endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://ivschat.{region}.amazonaws.com.cn"),
    "The ivschat endpoint for China (Beijing) and China (Ningxia)",
    QMap<QString, OAIServerVariable>{ 
    {"region", OAIServerVariable("The AWS region","cn-north-1",
    QSet<QString>{ {"cn-north-1"},{"cn-northwest-1"} })}, }));
    
    _serverConfigs.insert("createChatToken", defaultConf);
    _serverIndices.insert("createChatToken", 0);
    _serverConfigs.insert("createLoggingConfiguration", defaultConf);
    _serverIndices.insert("createLoggingConfiguration", 0);
    _serverConfigs.insert("createRoom", defaultConf);
    _serverIndices.insert("createRoom", 0);
    _serverConfigs.insert("deleteLoggingConfiguration", defaultConf);
    _serverIndices.insert("deleteLoggingConfiguration", 0);
    _serverConfigs.insert("deleteMessage", defaultConf);
    _serverIndices.insert("deleteMessage", 0);
    _serverConfigs.insert("deleteRoom", defaultConf);
    _serverIndices.insert("deleteRoom", 0);
    _serverConfigs.insert("disconnectUser", defaultConf);
    _serverIndices.insert("disconnectUser", 0);
    _serverConfigs.insert("getLoggingConfiguration", defaultConf);
    _serverIndices.insert("getLoggingConfiguration", 0);
    _serverConfigs.insert("getRoom", defaultConf);
    _serverIndices.insert("getRoom", 0);
    _serverConfigs.insert("listLoggingConfigurations", defaultConf);
    _serverIndices.insert("listLoggingConfigurations", 0);
    _serverConfigs.insert("listRooms", defaultConf);
    _serverIndices.insert("listRooms", 0);
    _serverConfigs.insert("listTagsForResource", defaultConf);
    _serverIndices.insert("listTagsForResource", 0);
    _serverConfigs.insert("sendEvent", defaultConf);
    _serverIndices.insert("sendEvent", 0);
    _serverConfigs.insert("tagResource", defaultConf);
    _serverIndices.insert("tagResource", 0);
    _serverConfigs.insert("untagResource", defaultConf);
    _serverIndices.insert("untagResource", 0);
    _serverConfigs.insert("updateLoggingConfiguration", defaultConf);
    _serverIndices.insert("updateLoggingConfiguration", 0);
    _serverConfigs.insert("updateRoom", defaultConf);
    _serverIndices.insert("updateRoom", 0);
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

void OAIDefaultApi::createChatToken(const OAICreateChatToken_request &oai_create_chat_token_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createChatToken"][_serverIndices.value("createChatToken")].URL()+"/CreateChatToken");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_chat_token_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createChatTokenCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createChatTokenCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateChatTokenResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createChatTokenSignal(output);
        Q_EMIT createChatTokenSignalFull(worker, output);
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

        Q_EMIT createChatTokenSignalE(output, error_type, error_str);
        Q_EMIT createChatTokenSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createChatTokenSignalError(output, error_type, error_str);
        Q_EMIT createChatTokenSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createLoggingConfiguration(const OAICreateLoggingConfiguration_request &oai_create_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createLoggingConfiguration"][_serverIndices.value("createLoggingConfiguration")].URL()+"/CreateLoggingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_logging_configuration_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createLoggingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createLoggingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateLoggingConfigurationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createLoggingConfigurationSignal(output);
        Q_EMIT createLoggingConfigurationSignalFull(worker, output);
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

        Q_EMIT createLoggingConfigurationSignalE(output, error_type, error_str);
        Q_EMIT createLoggingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createLoggingConfigurationSignalError(output, error_type, error_str);
        Q_EMIT createLoggingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::createRoom(const OAICreateRoom_request &oai_create_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["createRoom"][_serverIndices.value("createRoom")].URL()+"/CreateRoom");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_create_room_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::createRoomCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::createRoomCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICreateRoomResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createRoomSignal(output);
        Q_EMIT createRoomSignalFull(worker, output);
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

        Q_EMIT createRoomSignalE(output, error_type, error_str);
        Q_EMIT createRoomSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createRoomSignalError(output, error_type, error_str);
        Q_EMIT createRoomSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteLoggingConfiguration(const OAIDeleteLoggingConfiguration_request &oai_delete_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteLoggingConfiguration"][_serverIndices.value("deleteLoggingConfiguration")].URL()+"/DeleteLoggingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_logging_configuration_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteLoggingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteLoggingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteLoggingConfigurationSignal();
        Q_EMIT deleteLoggingConfigurationSignalFull(worker);
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

        Q_EMIT deleteLoggingConfigurationSignalE(error_type, error_str);
        Q_EMIT deleteLoggingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteLoggingConfigurationSignalError(error_type, error_str);
        Q_EMIT deleteLoggingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteMessage(const OAIDeleteMessage_request &oai_delete_message_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteMessage"][_serverIndices.value("deleteMessage")].URL()+"/DeleteMessage");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_message_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteMessageCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteMessageCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIDeleteMessageResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteMessageSignal(output);
        Q_EMIT deleteMessageSignalFull(worker, output);
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

        Q_EMIT deleteMessageSignalE(output, error_type, error_str);
        Q_EMIT deleteMessageSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteMessageSignalError(output, error_type, error_str);
        Q_EMIT deleteMessageSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::deleteRoom(const OAIDeleteRoom_request &oai_delete_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["deleteRoom"][_serverIndices.value("deleteRoom")].URL()+"/DeleteRoom");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_delete_room_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::deleteRoomCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::deleteRoomCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT deleteRoomSignal();
        Q_EMIT deleteRoomSignalFull(worker);
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

        Q_EMIT deleteRoomSignalE(error_type, error_str);
        Q_EMIT deleteRoomSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT deleteRoomSignalError(error_type, error_str);
        Q_EMIT deleteRoomSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::disconnectUser(const OAIDisconnectUser_request &oai_disconnect_user_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["disconnectUser"][_serverIndices.value("disconnectUser")].URL()+"/DisconnectUser");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_disconnect_user_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::disconnectUserCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::disconnectUserCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT disconnectUserSignal(output);
        Q_EMIT disconnectUserSignalFull(worker, output);
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

        Q_EMIT disconnectUserSignalE(output, error_type, error_str);
        Q_EMIT disconnectUserSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT disconnectUserSignalError(output, error_type, error_str);
        Q_EMIT disconnectUserSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getLoggingConfiguration(const OAIGetLoggingConfiguration_request &oai_get_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getLoggingConfiguration"][_serverIndices.value("getLoggingConfiguration")].URL()+"/GetLoggingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_logging_configuration_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getLoggingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getLoggingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetLoggingConfigurationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getLoggingConfigurationSignal(output);
        Q_EMIT getLoggingConfigurationSignalFull(worker, output);
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

        Q_EMIT getLoggingConfigurationSignalE(output, error_type, error_str);
        Q_EMIT getLoggingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getLoggingConfigurationSignalError(output, error_type, error_str);
        Q_EMIT getLoggingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::getRoom(const OAIGetRoom_request &oai_get_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["getRoom"][_serverIndices.value("getRoom")].URL()+"/GetRoom");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_get_room_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::getRoomCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::getRoomCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetRoomResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getRoomSignal(output);
        Q_EMIT getRoomSignalFull(worker, output);
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

        Q_EMIT getRoomSignalE(output, error_type, error_str);
        Q_EMIT getRoomSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getRoomSignalError(output, error_type, error_str);
        Q_EMIT getRoomSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listLoggingConfigurations(const OAIListLoggingConfigurations_request &oai_list_logging_configurations_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listLoggingConfigurations"][_serverIndices.value("listLoggingConfigurations")].URL()+"/ListLoggingConfigurations");
    
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

        
        QByteArray output = oai_list_logging_configurations_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listLoggingConfigurationsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listLoggingConfigurationsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListLoggingConfigurationsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listLoggingConfigurationsSignal(output);
        Q_EMIT listLoggingConfigurationsSignalFull(worker, output);
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

        Q_EMIT listLoggingConfigurationsSignalE(output, error_type, error_str);
        Q_EMIT listLoggingConfigurationsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listLoggingConfigurationsSignalError(output, error_type, error_str);
        Q_EMIT listLoggingConfigurationsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::listRooms(const OAIListRooms_request &oai_list_rooms_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers, const ::OpenAPI::OptionalParam<QString> &max_results, const ::OpenAPI::OptionalParam<QString> &next_token) {
    QString fullPath = QString(_serverConfigs["listRooms"][_serverIndices.value("listRooms")].URL()+"/ListRooms");
    
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

        
        QByteArray output = oai_list_rooms_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::listRoomsCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::listRoomsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIListRoomsResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT listRoomsSignal(output);
        Q_EMIT listRoomsSignalFull(worker, output);
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

        Q_EMIT listRoomsSignalE(output, error_type, error_str);
        Q_EMIT listRoomsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT listRoomsSignalError(output, error_type, error_str);
        Q_EMIT listRoomsSignalErrorFull(worker, error_type, error_str);
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

void OAIDefaultApi::sendEvent(const OAISendEvent_request &oai_send_event_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["sendEvent"][_serverIndices.value("sendEvent")].URL()+"/SendEvent");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_send_event_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::sendEventCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::sendEventCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAISendEventResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT sendEventSignal(output);
        Q_EMIT sendEventSignalFull(worker, output);
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

        Q_EMIT sendEventSignalE(output, error_type, error_str);
        Q_EMIT sendEventSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT sendEventSignalError(output, error_type, error_str);
        Q_EMIT sendEventSignalErrorFull(worker, error_type, error_str);
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

void OAIDefaultApi::updateLoggingConfiguration(const OAIUpdateLoggingConfiguration_request &oai_update_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateLoggingConfiguration"][_serverIndices.value("updateLoggingConfiguration")].URL()+"/UpdateLoggingConfiguration");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_logging_configuration_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateLoggingConfigurationCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateLoggingConfigurationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateLoggingConfigurationResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateLoggingConfigurationSignal(output);
        Q_EMIT updateLoggingConfigurationSignalFull(worker, output);
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

        Q_EMIT updateLoggingConfigurationSignalE(output, error_type, error_str);
        Q_EMIT updateLoggingConfigurationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateLoggingConfigurationSignalError(output, error_type, error_str);
        Q_EMIT updateLoggingConfigurationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIDefaultApi::updateRoom(const OAIUpdateRoom_request &oai_update_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256, const ::OpenAPI::OptionalParam<QString> &x_amz_date, const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm, const ::OpenAPI::OptionalParam<QString> &x_amz_credential, const ::OpenAPI::OptionalParam<QString> &x_amz_security_token, const ::OpenAPI::OptionalParam<QString> &x_amz_signature, const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers) {
    QString fullPath = QString(_serverConfigs["updateRoom"][_serverIndices.value("updateRoom")].URL()+"/UpdateRoom");
    
    if (_apiKeys.contains("hmac")) {
        addHeaders("hmac",_apiKeys.find("hmac").value());
    }
    
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_update_room_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIDefaultApi::updateRoomCallback);
    connect(this, &OAIDefaultApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIDefaultApi::updateRoomCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIUpdateRoomResponse output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT updateRoomSignal(output);
        Q_EMIT updateRoomSignalFull(worker, output);
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

        Q_EMIT updateRoomSignalE(output, error_type, error_str);
        Q_EMIT updateRoomSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT updateRoomSignalError(output, error_type, error_str);
        Q_EMIT updateRoomSignalErrorFull(worker, error_type, error_str);
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
