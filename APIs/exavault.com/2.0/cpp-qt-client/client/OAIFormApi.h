/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIFormApi_H
#define OAI_OAIFormApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIEmptyResponse.h"
#include "OAIFormEntryResponse.h"
#include "OAIFormResponse.h"
#include "OAIUpdateFormByIdRequestBody.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIFormApi : public QObject {
    Q_OBJECT

public:
    OAIFormApi(const int timeOut = 0);
    ~OAIFormApi();

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
    * @param[in]  ev_api_key QString [required]
    * @param[in]  ev_access_token QString [required]
    * @param[in]  id qint64 [required]
    */
    virtual void deleteFormMessageById(const QString &ev_api_key, const QString &ev_access_token, const qint64 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  ev_api_key QString [required]
    * @param[in]  ev_access_token QString [required]
    * @param[in]  include QString [optional]
    */
    virtual void getFormById(const qint32 &id, const QString &ev_api_key, const QString &ev_access_token, const ::OpenAPI::OptionalParam<QString> &include = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  ev_api_key QString [required]
    * @param[in]  ev_access_token QString [required]
    * @param[in]  share_hash QString [required]
    * @param[in]  include QString [optional]
    */
    virtual void getFormByShareHash(const QString &ev_api_key, const QString &ev_access_token, const QString &share_hash, const ::OpenAPI::OptionalParam<QString> &include = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  ev_api_key QString [required]
    * @param[in]  ev_access_token QString [required]
    * @param[in]  id qint32 [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void getFormEntries(const QString &ev_api_key, const QString &ev_access_token, const qint32 &id, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  ev_api_key QString [required]
    * @param[in]  ev_access_token QString [required]
    * @param[in]  oai_update_form_by_id_request_body OAIUpdateFormByIdRequestBody [optional]
    */
    virtual void updateFormById(const qint32 &id, const QString &ev_api_key, const QString &ev_access_token, const ::OpenAPI::OptionalParam<OAIUpdateFormByIdRequestBody> &oai_update_form_by_id_request_body = ::OpenAPI::OptionalParam<OAIUpdateFormByIdRequestBody>());


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

    void deleteFormMessageByIdCallback(OAIHttpRequestWorker *worker);
    void getFormByIdCallback(OAIHttpRequestWorker *worker);
    void getFormByShareHashCallback(OAIHttpRequestWorker *worker);
    void getFormEntriesCallback(OAIHttpRequestWorker *worker);
    void updateFormByIdCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void deleteFormMessageByIdSignal(OAIEmptyResponse summary);
    void getFormByIdSignal(OAIFormResponse summary);
    void getFormByShareHashSignal(OAIFormResponse summary);
    void getFormEntriesSignal(OAIFormEntryResponse summary);
    void updateFormByIdSignal(OAIFormResponse summary);


    void deleteFormMessageByIdSignalFull(OAIHttpRequestWorker *worker, OAIEmptyResponse summary);
    void getFormByIdSignalFull(OAIHttpRequestWorker *worker, OAIFormResponse summary);
    void getFormByShareHashSignalFull(OAIHttpRequestWorker *worker, OAIFormResponse summary);
    void getFormEntriesSignalFull(OAIHttpRequestWorker *worker, OAIFormEntryResponse summary);
    void updateFormByIdSignalFull(OAIHttpRequestWorker *worker, OAIFormResponse summary);

    Q_DECL_DEPRECATED_X("Use deleteFormMessageByIdSignalError() instead")
    void deleteFormMessageByIdSignalE(OAIEmptyResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteFormMessageByIdSignalError(OAIEmptyResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormByIdSignalError() instead")
    void getFormByIdSignalE(OAIFormResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormByIdSignalError(OAIFormResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormByShareHashSignalError() instead")
    void getFormByShareHashSignalE(OAIFormResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormByShareHashSignalError(OAIFormResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormEntriesSignalError() instead")
    void getFormEntriesSignalE(OAIFormEntryResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormEntriesSignalError(OAIFormEntryResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateFormByIdSignalError() instead")
    void updateFormByIdSignalE(OAIFormResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateFormByIdSignalError(OAIFormResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use deleteFormMessageByIdSignalErrorFull() instead")
    void deleteFormMessageByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteFormMessageByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormByIdSignalErrorFull() instead")
    void getFormByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormByShareHashSignalErrorFull() instead")
    void getFormByShareHashSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormByShareHashSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getFormEntriesSignalErrorFull() instead")
    void getFormEntriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getFormEntriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateFormByIdSignalErrorFull() instead")
    void updateFormByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateFormByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
