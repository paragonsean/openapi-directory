/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
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

#include "OAI_conversations__conversation_id__offer_post_request.h"
#include "OAI_conversations__id__offer_post_request.h"
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
    * @param[in]  conversation_id QString [required]
    * @param[in]  oai_conversations__conversation_id__offer_post_request OAI_conversations__conversation_id__offer_post_request [optional]
    */
    virtual void conversationsConversationIdOfferPost(const QString &conversation_id, const ::OpenAPI::OptionalParam<OAI_conversations__conversation_id__offer_post_request> &oai_conversations__conversation_id__offer_post_request = ::OpenAPI::OptionalParam<OAI_conversations__conversation_id__offer_post_request>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  oai_conversations__id__offer_post_request OAI_conversations__id__offer_post_request [optional]
    */
    virtual void conversationsIdOfferPost(const QString &id, const ::OpenAPI::OptionalParam<OAI_conversations__id__offer_post_request> &oai_conversations__id__offer_post_request = ::OpenAPI::OptionalParam<OAI_conversations__id__offer_post_request>());


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

    void conversationsConversationIdOfferPostCallback(OAIHttpRequestWorker *worker);
    void conversationsIdOfferPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void conversationsConversationIdOfferPostSignal();
    void conversationsIdOfferPostSignal();


    void conversationsConversationIdOfferPostSignalFull(OAIHttpRequestWorker *worker);
    void conversationsIdOfferPostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use conversationsConversationIdOfferPostSignalError() instead")
    void conversationsConversationIdOfferPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsConversationIdOfferPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIdOfferPostSignalError() instead")
    void conversationsIdOfferPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIdOfferPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use conversationsConversationIdOfferPostSignalErrorFull() instead")
    void conversationsConversationIdOfferPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsConversationIdOfferPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use conversationsIdOfferPostSignalErrorFull() instead")
    void conversationsIdOfferPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void conversationsIdOfferPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
