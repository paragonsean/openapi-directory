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

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICreateChatTokenResponse.h"
#include "OAICreateChatToken_request.h"
#include "OAICreateLoggingConfigurationResponse.h"
#include "OAICreateLoggingConfiguration_request.h"
#include "OAICreateRoomResponse.h"
#include "OAICreateRoom_request.h"
#include "OAIDeleteLoggingConfiguration_request.h"
#include "OAIDeleteMessageResponse.h"
#include "OAIDeleteMessage_request.h"
#include "OAIDeleteRoom_request.h"
#include "OAIDisconnectUser_request.h"
#include "OAIGetLoggingConfigurationResponse.h"
#include "OAIGetLoggingConfiguration_request.h"
#include "OAIGetRoomResponse.h"
#include "OAIGetRoom_request.h"
#include "OAIListLoggingConfigurationsResponse.h"
#include "OAIListLoggingConfigurations_request.h"
#include "OAIListRoomsResponse.h"
#include "OAIListRooms_request.h"
#include "OAIListTagsForResourceResponse.h"
#include "OAIObject.h"
#include "OAISendEventResponse.h"
#include "OAISendEvent_request.h"
#include "OAITagResource_request.h"
#include "OAIUpdateLoggingConfigurationResponse.h"
#include "OAIUpdateLoggingConfiguration_request.h"
#include "OAIUpdateRoomResponse.h"
#include "OAIUpdateRoom_request.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  oai_create_chat_token_request OAICreateChatToken_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createChatToken(const OAICreateChatToken_request &oai_create_chat_token_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_logging_configuration_request OAICreateLoggingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createLoggingConfiguration(const OAICreateLoggingConfiguration_request &oai_create_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_create_room_request OAICreateRoom_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createRoom(const OAICreateRoom_request &oai_create_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_logging_configuration_request OAIDeleteLoggingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteLoggingConfiguration(const OAIDeleteLoggingConfiguration_request &oai_delete_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_message_request OAIDeleteMessage_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteMessage(const OAIDeleteMessage_request &oai_delete_message_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_delete_room_request OAIDeleteRoom_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteRoom(const OAIDeleteRoom_request &oai_delete_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_disconnect_user_request OAIDisconnectUser_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void disconnectUser(const OAIDisconnectUser_request &oai_disconnect_user_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_logging_configuration_request OAIGetLoggingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getLoggingConfiguration(const OAIGetLoggingConfiguration_request &oai_get_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_get_room_request OAIGetRoom_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRoom(const OAIGetRoom_request &oai_get_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_logging_configurations_request OAIListLoggingConfigurations_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listLoggingConfigurations(const OAIListLoggingConfigurations_request &oai_list_logging_configurations_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_list_rooms_request OAIListRooms_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRooms(const OAIListRooms_request &oai_list_rooms_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void listTagsForResource(const QString &resource_arn, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_send_event_request OAISendEvent_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void sendEvent(const OAISendEvent_request &oai_send_event_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  oai_tag_resource_request OAITagResource_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &resource_arn, const OAITagResource_request &oai_tag_resource_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_arn QString [required]
    * @param[in]  tag_keys QList<QString> [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &resource_arn, const QList<QString> &tag_keys, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_update_logging_configuration_request OAIUpdateLoggingConfiguration_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateLoggingConfiguration(const OAIUpdateLoggingConfiguration_request &oai_update_logging_configuration_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_update_room_request OAIUpdateRoom_request [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateRoom(const OAIUpdateRoom_request &oai_update_room_request, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void createChatTokenCallback(OAIHttpRequestWorker *worker);
    void createLoggingConfigurationCallback(OAIHttpRequestWorker *worker);
    void createRoomCallback(OAIHttpRequestWorker *worker);
    void deleteLoggingConfigurationCallback(OAIHttpRequestWorker *worker);
    void deleteMessageCallback(OAIHttpRequestWorker *worker);
    void deleteRoomCallback(OAIHttpRequestWorker *worker);
    void disconnectUserCallback(OAIHttpRequestWorker *worker);
    void getLoggingConfigurationCallback(OAIHttpRequestWorker *worker);
    void getRoomCallback(OAIHttpRequestWorker *worker);
    void listLoggingConfigurationsCallback(OAIHttpRequestWorker *worker);
    void listRoomsCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void sendEventCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updateLoggingConfigurationCallback(OAIHttpRequestWorker *worker);
    void updateRoomCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void createChatTokenSignal(OAICreateChatTokenResponse summary);
    void createLoggingConfigurationSignal(OAICreateLoggingConfigurationResponse summary);
    void createRoomSignal(OAICreateRoomResponse summary);
    void deleteLoggingConfigurationSignal();
    void deleteMessageSignal(OAIDeleteMessageResponse summary);
    void deleteRoomSignal();
    void disconnectUserSignal(OAIObject summary);
    void getLoggingConfigurationSignal(OAIGetLoggingConfigurationResponse summary);
    void getRoomSignal(OAIGetRoomResponse summary);
    void listLoggingConfigurationsSignal(OAIListLoggingConfigurationsResponse summary);
    void listRoomsSignal(OAIListRoomsResponse summary);
    void listTagsForResourceSignal(OAIListTagsForResourceResponse summary);
    void sendEventSignal(OAISendEventResponse summary);
    void tagResourceSignal(OAIObject summary);
    void untagResourceSignal(OAIObject summary);
    void updateLoggingConfigurationSignal(OAIUpdateLoggingConfigurationResponse summary);
    void updateRoomSignal(OAIUpdateRoomResponse summary);


    void createChatTokenSignalFull(OAIHttpRequestWorker *worker, OAICreateChatTokenResponse summary);
    void createLoggingConfigurationSignalFull(OAIHttpRequestWorker *worker, OAICreateLoggingConfigurationResponse summary);
    void createRoomSignalFull(OAIHttpRequestWorker *worker, OAICreateRoomResponse summary);
    void deleteLoggingConfigurationSignalFull(OAIHttpRequestWorker *worker);
    void deleteMessageSignalFull(OAIHttpRequestWorker *worker, OAIDeleteMessageResponse summary);
    void deleteRoomSignalFull(OAIHttpRequestWorker *worker);
    void disconnectUserSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getLoggingConfigurationSignalFull(OAIHttpRequestWorker *worker, OAIGetLoggingConfigurationResponse summary);
    void getRoomSignalFull(OAIHttpRequestWorker *worker, OAIGetRoomResponse summary);
    void listLoggingConfigurationsSignalFull(OAIHttpRequestWorker *worker, OAIListLoggingConfigurationsResponse summary);
    void listRoomsSignalFull(OAIHttpRequestWorker *worker, OAIListRoomsResponse summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceResponse summary);
    void sendEventSignalFull(OAIHttpRequestWorker *worker, OAISendEventResponse summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateLoggingConfigurationSignalFull(OAIHttpRequestWorker *worker, OAIUpdateLoggingConfigurationResponse summary);
    void updateRoomSignalFull(OAIHttpRequestWorker *worker, OAIUpdateRoomResponse summary);

    Q_DECL_DEPRECATED_X("Use createChatTokenSignalError() instead")
    void createChatTokenSignalE(OAICreateChatTokenResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createChatTokenSignalError(OAICreateChatTokenResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createLoggingConfigurationSignalError() instead")
    void createLoggingConfigurationSignalE(OAICreateLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createLoggingConfigurationSignalError(OAICreateLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRoomSignalError() instead")
    void createRoomSignalE(OAICreateRoomResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createRoomSignalError(OAICreateRoomResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLoggingConfigurationSignalError() instead")
    void deleteLoggingConfigurationSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLoggingConfigurationSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteMessageSignalError() instead")
    void deleteMessageSignalE(OAIDeleteMessageResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteMessageSignalError(OAIDeleteMessageResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRoomSignalError() instead")
    void deleteRoomSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRoomSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disconnectUserSignalError() instead")
    void disconnectUserSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void disconnectUserSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLoggingConfigurationSignalError() instead")
    void getLoggingConfigurationSignalE(OAIGetLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLoggingConfigurationSignalError(OAIGetLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRoomSignalError() instead")
    void getRoomSignalE(OAIGetRoomResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRoomSignalError(OAIGetRoomResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listLoggingConfigurationsSignalError() instead")
    void listLoggingConfigurationsSignalE(OAIListLoggingConfigurationsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listLoggingConfigurationsSignalError(OAIListLoggingConfigurationsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRoomsSignalError() instead")
    void listRoomsSignalE(OAIListRoomsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRoomsSignalError(OAIListRoomsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendEventSignalError() instead")
    void sendEventSignalE(OAISendEventResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sendEventSignalError(OAISendEventResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLoggingConfigurationSignalError() instead")
    void updateLoggingConfigurationSignalE(OAIUpdateLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLoggingConfigurationSignalError(OAIUpdateLoggingConfigurationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRoomSignalError() instead")
    void updateRoomSignalE(OAIUpdateRoomResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRoomSignalError(OAIUpdateRoomResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use createChatTokenSignalErrorFull() instead")
    void createChatTokenSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createChatTokenSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createLoggingConfigurationSignalErrorFull() instead")
    void createLoggingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createLoggingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRoomSignalErrorFull() instead")
    void createRoomSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createRoomSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteLoggingConfigurationSignalErrorFull() instead")
    void deleteLoggingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteLoggingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteMessageSignalErrorFull() instead")
    void deleteMessageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteMessageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRoomSignalErrorFull() instead")
    void deleteRoomSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRoomSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use disconnectUserSignalErrorFull() instead")
    void disconnectUserSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void disconnectUserSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getLoggingConfigurationSignalErrorFull() instead")
    void getLoggingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLoggingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRoomSignalErrorFull() instead")
    void getRoomSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRoomSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listLoggingConfigurationsSignalErrorFull() instead")
    void listLoggingConfigurationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listLoggingConfigurationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRoomsSignalErrorFull() instead")
    void listRoomsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRoomsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sendEventSignalErrorFull() instead")
    void sendEventSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sendEventSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateLoggingConfigurationSignalErrorFull() instead")
    void updateLoggingConfigurationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateLoggingConfigurationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateRoomSignalErrorFull() instead")
    void updateRoomSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateRoomSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
