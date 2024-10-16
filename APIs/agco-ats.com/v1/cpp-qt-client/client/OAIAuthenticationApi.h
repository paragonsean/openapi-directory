/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAuthenticationApi_H
#define OAI_OAIAuthenticationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_AuthenticatedUser.h"
#include "OAIAPI_Models_Credentials.h"
#include "OAIAPI_Models_PasswordReset.h"
#include "OAIAPI_Models_PasswordResetRequest.h"
#include "OAIAPI_Models_TokenOptions.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAuthenticationApi : public QObject {
    Q_OBJECT

public:
    OAIAuthenticationApi(const int timeOut = 0);
    ~OAIAuthenticationApi();

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
    * @param[in]  oaiapi_models_credentials OAIAPI_Models_Credentials [required]
    */
    virtual void authenticationDefault(const OAIAPI_Models_Credentials &oaiapi_models_credentials);


    virtual void authenticationIsAlive();

    /**
    * @param[in]  user_id qint32 [required]
    * @param[in]  oaiapi_models_token_options OAIAPI_Models_TokenOptions [required]
    */
    virtual void authenticationPutManageTokens(const qint32 &user_id, const OAIAPI_Models_TokenOptions &oaiapi_models_token_options);

    /**
    * @param[in]  oaiapi_models_password_reset_request OAIAPI_Models_PasswordResetRequest [required]
    */
    virtual void authenticationRequestPasswordReset(const OAIAPI_Models_PasswordResetRequest &oaiapi_models_password_reset_request);

    /**
    * @param[in]  oaiapi_models_password_reset OAIAPI_Models_PasswordReset [required]
    */
    virtual void authenticationResetPasword(const OAIAPI_Models_PasswordReset &oaiapi_models_password_reset);


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

    void authenticationDefaultCallback(OAIHttpRequestWorker *worker);
    void authenticationIsAliveCallback(OAIHttpRequestWorker *worker);
    void authenticationPutManageTokensCallback(OAIHttpRequestWorker *worker);
    void authenticationRequestPasswordResetCallback(OAIHttpRequestWorker *worker);
    void authenticationResetPaswordCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void authenticationDefaultSignal(OAIAPI_Models_AuthenticatedUser summary);
    void authenticationIsAliveSignal();
    void authenticationPutManageTokensSignal();
    void authenticationRequestPasswordResetSignal();
    void authenticationResetPaswordSignal();


    void authenticationDefaultSignalFull(OAIHttpRequestWorker *worker, OAIAPI_Models_AuthenticatedUser summary);
    void authenticationIsAliveSignalFull(OAIHttpRequestWorker *worker);
    void authenticationPutManageTokensSignalFull(OAIHttpRequestWorker *worker);
    void authenticationRequestPasswordResetSignalFull(OAIHttpRequestWorker *worker);
    void authenticationResetPaswordSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use authenticationDefaultSignalError() instead")
    void authenticationDefaultSignalE(OAIAPI_Models_AuthenticatedUser summary, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationDefaultSignalError(OAIAPI_Models_AuthenticatedUser summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationIsAliveSignalError() instead")
    void authenticationIsAliveSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationIsAliveSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationPutManageTokensSignalError() instead")
    void authenticationPutManageTokensSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationPutManageTokensSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationRequestPasswordResetSignalError() instead")
    void authenticationRequestPasswordResetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationRequestPasswordResetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationResetPaswordSignalError() instead")
    void authenticationResetPaswordSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationResetPaswordSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use authenticationDefaultSignalErrorFull() instead")
    void authenticationDefaultSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationDefaultSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationIsAliveSignalErrorFull() instead")
    void authenticationIsAliveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationIsAliveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationPutManageTokensSignalErrorFull() instead")
    void authenticationPutManageTokensSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationPutManageTokensSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationRequestPasswordResetSignalErrorFull() instead")
    void authenticationRequestPasswordResetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationRequestPasswordResetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authenticationResetPaswordSignalErrorFull() instead")
    void authenticationResetPaswordSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authenticationResetPaswordSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
