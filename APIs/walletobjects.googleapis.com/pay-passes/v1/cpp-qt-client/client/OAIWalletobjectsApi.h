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

#ifndef OAI_OAIWalletobjectsApi_H
#define OAI_OAIWalletobjectsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIUploadPrivateDataRequest.h"
#include "OAIUploadPrivateDataResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIWalletobjectsApi : public QObject {
    Q_OBJECT

public:
    OAIWalletobjectsApi(const int timeOut = 0);
    ~OAIWalletobjectsApi();

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
    * @param[in]  oai_upload_private_data_request OAIUploadPrivateDataRequest [optional]
    */
    virtual void walletobjects_walletobjects_v1_privateContent_uploadPrivateData(const ::OpenAPI::OptionalParam<QString> &_xgafv = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &access_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &alt = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &oauth_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &pretty_print = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &quota_user = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_protocol = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &upload_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<OAIUploadPrivateDataRequest> &oai_upload_private_data_request = ::OpenAPI::OptionalParam<OAIUploadPrivateDataRequest>());


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

    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignal(OAIUploadPrivateDataResponse summary);


    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalFull(OAIHttpRequestWorker *worker, OAIUploadPrivateDataResponse summary);

    Q_DECL_DEPRECATED_X("Use walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalError() instead")
    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalE(OAIUploadPrivateDataResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalError(OAIUploadPrivateDataResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalErrorFull() instead")
    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void walletobjects_walletobjects_v1_privateContent_uploadPrivateDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
