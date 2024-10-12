/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIConversationsApi_H
#define OAI_OAIConversationsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIEndpoint_get_conversations_ID.h"
#include "OAIEndpoint_get_conversations_ID_messages.h"
#include "OAIEndpoint_get_conversations_ID_statuses.h"
#include "OAIEndpoint_get_conversations_statuses.h"
#include "OAIEndpoint_patch_conversations_ID_statuses.h"
#include "OAIEndpoint_post_conversations_ID_messages.h"
#include "OAIEndpoint_post_conversations_ID_schedules.h"
#include "OAIEndpoint_post_conversations_ID_searches.h"
#include "OAIEndpoint_post_conversations_schedules.h"
#include "OAIEndpoint_post_conversations_searches.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIConversationsApi : public QObject {
    Q_OBJECT

public:
    OAIConversationsApi(const int timeOut = 0);
    ~OAIConversationsApi();

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
    * @param[in]  id QList<qint32> [required]
    */
    virtual void conversationsIDGet(const QList<qint32> &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  gt_message_id qint32 [optional]
    * @param[in]  exclude_self bool [optional]
    * @param[in]  date QString [optional]
    * @param[in]  bubbled bool [optional]
    * @param[in]  record_seen bool [optional]
    * @param[in]  timeout qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void conversationsIDMessagesGet(const qint32 &id, const ::OpenAPI::OptionalParam<qint32> &gt_message_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &exclude_self = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &bubbled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &record_seen = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &timeout = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  text_raw QString [required]
    * @param[in]  bubbled bool [optional]
    * @param[in]  metadata_0_key QString [optional]
    * @param[in]  metadata_0_privacy QString [optional]
    * @param[in]  metadata_0_values QList<QString> [optional]
    * @param[in]  metadata_1_key QString [optional]
    * @param[in]  metadata_1_privacy QString [optional]
    * @param[in]  metadata_1_values QList<QString> [optional]
    * @param[in]  metadata_2_key QString [optional]
    * @param[in]  metadata_2_privacy QString [optional]
    * @param[in]  metadata_2_values QList<QString> [optional]
    * @param[in]  text_emoticons bool [optional]
    */
    virtual void conversationsIDMessagesPost(const qint32 &id, const QString &text_raw, const ::OpenAPI::OptionalParam<bool> &bubbled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &metadata_0_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &metadata_0_privacy = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &metadata_0_values = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &metadata_1_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &metadata_1_privacy = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &metadata_1_values = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<QString> &metadata_2_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &metadata_2_privacy = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<QString>> &metadata_2_values = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<bool> &text_emoticons = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  id QList<qint32> [required]
    * @param[in]  date QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  roll_up bool [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void conversationsIDSchedulesPost(const QList<qint32> &id, const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &roll_up = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QList<qint32> [required]
    * @param[in]  query QString [required]
    * @param[in]  date QString [optional]
    * @param[in]  gt_message_id qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void conversationsIDSearchesPost(const QList<qint32> &id, const QString &query, const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &gt_message_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QList<qint32> [required]
    */
    virtual void conversationsIDStatusesGet(const QList<qint32> &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  archived_status bool [required]
    */
    virtual void conversationsIDStatusesPatch(const qint32 &id, const bool &archived_status);

    /**
    * @param[in]  date QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  roll_up bool [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void conversationsSchedulesPost(const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &roll_up = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  query QString [required]
    * @param[in]  date QString [optional]
    * @param[in]  gt_message_id qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void conversationsSearchesPost(const QString &query, const ::OpenAPI::OptionalParam<QString> &date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &gt_message_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  filter QString [optional]
    * @param[in]  include_archived bool [optional]
    * @param[in]  bubbled bool [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void conversationsStatusesGet(const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &include_archived = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<bool> &bubbled = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());


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

    void conversationsIDGetCallback(OAIHttpRequestWorker *worker);
    void conversationsIDMessagesGetCallback(OAIHttpRequestWorker *worker);
    void conversationsIDMessagesPostCallback(OAIHttpRequestWorker *worker);
    void conversationsIDSchedulesPostCallback(OAIHttpRequestWorker *worker);
    void conversationsIDSearchesPostCallback(OAIHttpRequestWorker *worker);
    void conversationsIDStatusesGetCallback(OAIHttpRequestWorker *worker);
    void conversationsIDStatusesPatchCallback(OAIHttpRequestWorker *worker);
    void conversationsSchedulesPostCallback(OAIHttpRequestWorker *worker);
    void conversationsSearchesPostCallback(OAIHttpRequestWorker *worker);
    void conversationsStatusesGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void conversationsIDGetSignal(OAIEndpoint_get_conversations_ID summary);
    void conversationsIDMessagesGetSignal(OAIEndpoint_get_conversations_ID_messages summary);
    void conversationsIDMessagesPostSignal(OAIEndpoint_post_conversations_ID_messages summary);
    void conversationsIDSchedulesPostSignal(OAIEndpoint_post_conversations_ID_schedules summary);
    void conversationsIDSearchesPostSignal(OAIEndpoint_post_conversations_ID_searches summary);
    void conversationsIDStatusesGetSignal(OAIEndpoint_get_conversations_ID_statuses summary);
    void conversationsIDStatusesPatchSignal(OAIEndpoint_patch_conversations_ID_statuses summary);
    void conversationsSchedulesPostSignal(OAIEndpoint_post_conversations_schedules summary);
    void conversationsSearchesPostSignal(OAIEndpoint_post_conversations_searches summary);
    void conversationsStatusesGetSignal(OAIEndpoint_get_conversations_statuses summary);


    void conversationsIDGetSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_get_conversations_ID summary);
    void conversationsIDMessagesGetSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_get_conversations_ID_messages summary);
    void conversationsIDMessagesPostSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_post_conversations_ID_messages summary);
    void conversationsIDSchedulesPostSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_post_conversations_ID_schedules summary);
    void conversationsIDSearchesPostSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_post_conversations_ID_searches summary);
    void conversationsIDStatusesGetSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_get_conversations_ID_statuses summary);
    void conversationsIDStatusesPatchSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_patch_conversations_ID_statuses summary);
    void conversationsSchedulesPostSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_post_conversations_schedules summary);
    void conversationsSearchesPostSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_post_conversations_searches summary);
    void conversationsStatusesGetSignalFull(OAIHttpRequestWorker *worker, OAIEndpoint_get_conversations_statuses summary);

    Q_DECL_DEPRECATED_X("Use conversationsIDGetSignalError() instead")
    void conversationsIDGetSignalE(OAIEndpoint_get_conversations_ID summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDGetSignalError(OAIEndpoint_get_conversations_ID summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDMessagesGetSignalError() instead")
    void conversationsIDMessagesGetSignalE(OAIEndpoint_get_conversations_ID_messages summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDMessagesGetSignalError(OAIEndpoint_get_conversations_ID_messages summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDMessagesPostSignalError() instead")
    void conversationsIDMessagesPostSignalE(OAIEndpoint_post_conversations_ID_messages summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDMessagesPostSignalError(OAIEndpoint_post_conversations_ID_messages summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDSchedulesPostSignalError() instead")
    void conversationsIDSchedulesPostSignalE(OAIEndpoint_post_conversations_ID_schedules summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDSchedulesPostSignalError(OAIEndpoint_post_conversations_ID_schedules summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDSearchesPostSignalError() instead")
    void conversationsIDSearchesPostSignalE(OAIEndpoint_post_conversations_ID_searches summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDSearchesPostSignalError(OAIEndpoint_post_conversations_ID_searches summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDStatusesGetSignalError() instead")
    void conversationsIDStatusesGetSignalE(OAIEndpoint_get_conversations_ID_statuses summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDStatusesGetSignalError(OAIEndpoint_get_conversations_ID_statuses summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDStatusesPatchSignalError() instead")
    void conversationsIDStatusesPatchSignalE(OAIEndpoint_patch_conversations_ID_statuses summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDStatusesPatchSignalError(OAIEndpoint_patch_conversations_ID_statuses summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsSchedulesPostSignalError() instead")
    void conversationsSchedulesPostSignalE(OAIEndpoint_post_conversations_schedules summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsSchedulesPostSignalError(OAIEndpoint_post_conversations_schedules summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsSearchesPostSignalError() instead")
    void conversationsSearchesPostSignalE(OAIEndpoint_post_conversations_searches summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsSearchesPostSignalError(OAIEndpoint_post_conversations_searches summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsStatusesGetSignalError() instead")
    void conversationsStatusesGetSignalE(OAIEndpoint_get_conversations_statuses summary, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsStatusesGetSignalError(OAIEndpoint_get_conversations_statuses summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use conversationsIDGetSignalErrorFull() instead")
    void conversationsIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDMessagesGetSignalErrorFull() instead")
    void conversationsIDMessagesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDMessagesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDMessagesPostSignalErrorFull() instead")
    void conversationsIDMessagesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDMessagesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDSchedulesPostSignalErrorFull() instead")
    void conversationsIDSchedulesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDSchedulesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDSearchesPostSignalErrorFull() instead")
    void conversationsIDSearchesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDSearchesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDStatusesGetSignalErrorFull() instead")
    void conversationsIDStatusesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDStatusesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIDStatusesPatchSignalErrorFull() instead")
    void conversationsIDStatusesPatchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIDStatusesPatchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsSchedulesPostSignalErrorFull() instead")
    void conversationsSchedulesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsSchedulesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsSearchesPostSignalErrorFull() instead")
    void conversationsSearchesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsSearchesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsStatusesGetSignalErrorFull() instead")
    void conversationsStatusesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsStatusesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
