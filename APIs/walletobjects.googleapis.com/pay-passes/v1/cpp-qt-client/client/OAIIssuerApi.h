/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIIssuerApi_H
#define OAI_OAIIssuerApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIIssuer.h"
#include "OAIIssuerListResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIIssuerApi : public QObject {
    Q_OBJECT

public:
    OAIIssuerApi(const int timeOut = 0);
    ~OAIIssuerApi();

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
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    */
    virtual void walletobjects_issuer_get(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_issuer OAIIssuer [optional]
    */
    virtual void walletobjects_issuer_insert(const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIIssuer> &oai_issuer = ::OpenAPI::OptionalParam<OAIIssuer>());

    /**
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    */
    virtual void walletobjects_issuer_list(const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_issuer OAIIssuer [optional]
    */
    virtual void walletobjects_issuer_patch(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIIssuer> &oai_issuer = ::OpenAPI::OptionalParam<OAIIssuer>());

    /**
    * @param[in]  resource_id QString [required]
    * @param[in]  _xgafv QString [optional]
    * @param[in]  access_token QString [optional]
    * @param[in]  alt QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  fields QString [optional]
    * @param[in]  key QString [optional]
    * @param[in]  oauth_token QString [optional]
    * @param[in]  pretty_print bool [optional]
    * @param[in]  quota_user QString [optional]
    * @param[in]  upload_protocol QString [optional]
    * @param[in]  upload_type QString [optional]
    * @param[in]  oai_issuer OAIIssuer [optional]
    */
    virtual void walletobjects_issuer_update(const QString &resource_id, const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIIssuer> &oai_issuer = ::OpenAPI::OptionalParam<OAIIssuer>());


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

    void walletobjects_issuer_getCallback(OAIHttpRequestWorker *worker);
    void walletobjects_issuer_insertCallback(OAIHttpRequestWorker *worker);
    void walletobjects_issuer_listCallback(OAIHttpRequestWorker *worker);
    void walletobjects_issuer_patchCallback(OAIHttpRequestWorker *worker);
    void walletobjects_issuer_updateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void walletobjects_issuer_getSignal(OAIIssuer summary);
    void walletobjects_issuer_insertSignal(OAIIssuer summary);
    void walletobjects_issuer_listSignal(OAIIssuerListResponse summary);
    void walletobjects_issuer_patchSignal(OAIIssuer summary);
    void walletobjects_issuer_updateSignal(OAIIssuer summary);


    void walletobjects_issuer_getSignalFull(OAIHttpRequestWorker *worker, OAIIssuer summary);
    void walletobjects_issuer_insertSignalFull(OAIHttpRequestWorker *worker, OAIIssuer summary);
    void walletobjects_issuer_listSignalFull(OAIHttpRequestWorker *worker, OAIIssuerListResponse summary);
    void walletobjects_issuer_patchSignalFull(OAIHttpRequestWorker *worker, OAIIssuer summary);
    void walletobjects_issuer_updateSignalFull(OAIHttpRequestWorker *worker, OAIIssuer summary);

    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_getSignalError() instead")
    void walletobjects_issuer_getSignalE(OAIIssuer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_getSignalError(OAIIssuer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_insertSignalError() instead")
    void walletobjects_issuer_insertSignalE(OAIIssuer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_insertSignalError(OAIIssuer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_listSignalError() instead")
    void walletobjects_issuer_listSignalE(OAIIssuerListResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_listSignalError(OAIIssuerListResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_patchSignalError() instead")
    void walletobjects_issuer_patchSignalE(OAIIssuer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_patchSignalError(OAIIssuer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_updateSignalError() instead")
    void walletobjects_issuer_updateSignalE(OAIIssuer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_updateSignalError(OAIIssuer summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_getSignalErrorFull() instead")
    void walletobjects_issuer_getSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_getSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_insertSignalErrorFull() instead")
    void walletobjects_issuer_insertSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_insertSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_listSignalErrorFull() instead")
    void walletobjects_issuer_listSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_listSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_patchSignalErrorFull() instead")
    void walletobjects_issuer_patchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_patchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use walletobjects_issuer_updateSignalErrorFull() instead")
    void walletobjects_issuer_updateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_issuer_updateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
