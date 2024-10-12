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

#include "OAICreateRoomResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateRoomResponse::OAICreateRoomResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateRoomResponse::OAICreateRoomResponse() {
    this->initializeModel();
}

OAICreateRoomResponse::~OAICreateRoomResponse() {}

void OAICreateRoomResponse::initializeModel() {

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_create_time_isSet = false;
    m_create_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_logging_configuration_identifiers_isSet = false;
    m_logging_configuration_identifiers_isValid = false;

    m_maximum_message_length_isSet = false;
    m_maximum_message_length_isValid = false;

    m_maximum_message_rate_per_second_isSet = false;
    m_maximum_message_rate_per_second_isValid = false;

    m_message_review_handler_isSet = false;
    m_message_review_handler_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_update_time_isSet = false;
    m_update_time_isValid = false;
}

void OAICreateRoomResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateRoomResponse::fromJsonObject(QJsonObject json) {

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_create_time_isValid = ::OpenAPI::fromJsonValue(m_create_time, json[QString("createTime")]);
    m_create_time_isSet = !json[QString("createTime")].isNull() && m_create_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_logging_configuration_identifiers_isValid = ::OpenAPI::fromJsonValue(m_logging_configuration_identifiers, json[QString("loggingConfigurationIdentifiers")]);
    m_logging_configuration_identifiers_isSet = !json[QString("loggingConfigurationIdentifiers")].isNull() && m_logging_configuration_identifiers_isValid;

    m_maximum_message_length_isValid = ::OpenAPI::fromJsonValue(m_maximum_message_length, json[QString("maximumMessageLength")]);
    m_maximum_message_length_isSet = !json[QString("maximumMessageLength")].isNull() && m_maximum_message_length_isValid;

    m_maximum_message_rate_per_second_isValid = ::OpenAPI::fromJsonValue(m_maximum_message_rate_per_second, json[QString("maximumMessageRatePerSecond")]);
    m_maximum_message_rate_per_second_isSet = !json[QString("maximumMessageRatePerSecond")].isNull() && m_maximum_message_rate_per_second_isValid;

    m_message_review_handler_isValid = ::OpenAPI::fromJsonValue(m_message_review_handler, json[QString("messageReviewHandler")]);
    m_message_review_handler_isSet = !json[QString("messageReviewHandler")].isNull() && m_message_review_handler_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_update_time_isValid = ::OpenAPI::fromJsonValue(m_update_time, json[QString("updateTime")]);
    m_update_time_isSet = !json[QString("updateTime")].isNull() && m_update_time_isValid;
}

QString OAICreateRoomResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateRoomResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_create_time_isSet) {
        obj.insert(QString("createTime"), ::OpenAPI::toJsonValue(m_create_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_logging_configuration_identifiers.isSet()) {
        obj.insert(QString("loggingConfigurationIdentifiers"), ::OpenAPI::toJsonValue(m_logging_configuration_identifiers));
    }
    if (m_maximum_message_length_isSet) {
        obj.insert(QString("maximumMessageLength"), ::OpenAPI::toJsonValue(m_maximum_message_length));
    }
    if (m_maximum_message_rate_per_second_isSet) {
        obj.insert(QString("maximumMessageRatePerSecond"), ::OpenAPI::toJsonValue(m_maximum_message_rate_per_second));
    }
    if (m_message_review_handler.isSet()) {
        obj.insert(QString("messageReviewHandler"), ::OpenAPI::toJsonValue(m_message_review_handler));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_tags.isSet()) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_update_time_isSet) {
        obj.insert(QString("updateTime"), ::OpenAPI::toJsonValue(m_update_time));
    }
    return obj;
}

QString OAICreateRoomResponse::getArn() const {
    return m_arn;
}
void OAICreateRoomResponse::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAICreateRoomResponse::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAICreateRoomResponse::is_arn_Valid() const{
    return m_arn_isValid;
}

QDateTime OAICreateRoomResponse::getCreateTime() const {
    return m_create_time;
}
void OAICreateRoomResponse::setCreateTime(const QDateTime &create_time) {
    m_create_time = create_time;
    m_create_time_isSet = true;
}

bool OAICreateRoomResponse::is_create_time_Set() const{
    return m_create_time_isSet;
}

bool OAICreateRoomResponse::is_create_time_Valid() const{
    return m_create_time_isValid;
}

QString OAICreateRoomResponse::getId() const {
    return m_id;
}
void OAICreateRoomResponse::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreateRoomResponse::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreateRoomResponse::is_id_Valid() const{
    return m_id_isValid;
}

QList OAICreateRoomResponse::getLoggingConfigurationIdentifiers() const {
    return m_logging_configuration_identifiers;
}
void OAICreateRoomResponse::setLoggingConfigurationIdentifiers(const QList &logging_configuration_identifiers) {
    m_logging_configuration_identifiers = logging_configuration_identifiers;
    m_logging_configuration_identifiers_isSet = true;
}

bool OAICreateRoomResponse::is_logging_configuration_identifiers_Set() const{
    return m_logging_configuration_identifiers_isSet;
}

bool OAICreateRoomResponse::is_logging_configuration_identifiers_Valid() const{
    return m_logging_configuration_identifiers_isValid;
}

qint32 OAICreateRoomResponse::getMaximumMessageLength() const {
    return m_maximum_message_length;
}
void OAICreateRoomResponse::setMaximumMessageLength(const qint32 &maximum_message_length) {
    m_maximum_message_length = maximum_message_length;
    m_maximum_message_length_isSet = true;
}

bool OAICreateRoomResponse::is_maximum_message_length_Set() const{
    return m_maximum_message_length_isSet;
}

bool OAICreateRoomResponse::is_maximum_message_length_Valid() const{
    return m_maximum_message_length_isValid;
}

qint32 OAICreateRoomResponse::getMaximumMessageRatePerSecond() const {
    return m_maximum_message_rate_per_second;
}
void OAICreateRoomResponse::setMaximumMessageRatePerSecond(const qint32 &maximum_message_rate_per_second) {
    m_maximum_message_rate_per_second = maximum_message_rate_per_second;
    m_maximum_message_rate_per_second_isSet = true;
}

bool OAICreateRoomResponse::is_maximum_message_rate_per_second_Set() const{
    return m_maximum_message_rate_per_second_isSet;
}

bool OAICreateRoomResponse::is_maximum_message_rate_per_second_Valid() const{
    return m_maximum_message_rate_per_second_isValid;
}

OAICreateRoomResponse_messageReviewHandler OAICreateRoomResponse::getMessageReviewHandler() const {
    return m_message_review_handler;
}
void OAICreateRoomResponse::setMessageReviewHandler(const OAICreateRoomResponse_messageReviewHandler &message_review_handler) {
    m_message_review_handler = message_review_handler;
    m_message_review_handler_isSet = true;
}

bool OAICreateRoomResponse::is_message_review_handler_Set() const{
    return m_message_review_handler_isSet;
}

bool OAICreateRoomResponse::is_message_review_handler_Valid() const{
    return m_message_review_handler_isValid;
}

QString OAICreateRoomResponse::getName() const {
    return m_name;
}
void OAICreateRoomResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateRoomResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateRoomResponse::is_name_Valid() const{
    return m_name_isValid;
}

QMap OAICreateRoomResponse::getTags() const {
    return m_tags;
}
void OAICreateRoomResponse::setTags(const QMap &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateRoomResponse::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateRoomResponse::is_tags_Valid() const{
    return m_tags_isValid;
}

QDateTime OAICreateRoomResponse::getUpdateTime() const {
    return m_update_time;
}
void OAICreateRoomResponse::setUpdateTime(const QDateTime &update_time) {
    m_update_time = update_time;
    m_update_time_isSet = true;
}

bool OAICreateRoomResponse::is_update_time_Set() const{
    return m_update_time_isSet;
}

bool OAICreateRoomResponse::is_update_time_Valid() const{
    return m_update_time_isValid;
}

bool OAICreateRoomResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_create_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logging_configuration_identifiers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_message_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maximum_message_rate_per_second_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_review_handler.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateRoomResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
