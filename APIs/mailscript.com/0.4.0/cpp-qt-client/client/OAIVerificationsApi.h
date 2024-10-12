/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVerificationsApi_H
#define OAI_OAIVerificationsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddVerificationResponse.h"
#include "OAIAddVerification_request.h"
#include "OAIErrorResponse.h"
#include "OAIGetAllVerificationsResponse.h"
#include "OAIVerify_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVerificationsApi : public QObject {
    Q_OBJECT

public:
    OAIVerificationsApi(const int timeOut = 0);
    ~OAIVerificationsApi();

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
    * @param[in]  oai_add_verification_request OAIAddVerification_request [required]
    */
    virtual void addVerification(const OAIAddVerification_request &oai_add_verification_request);


    virtual void getAllVerifications();

    /**
    * @param[in]  verification QString [required]
    * @param[in]  oai_verify_request OAIVerify_request [required]
    */
    virtual void verify(const QString &verification, const OAIVerify_request &oai_verify_request);


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

    void addVerificationCallback(OAIHttpRequestWorker *worker);
    void getAllVerificationsCallback(OAIHttpRequestWorker *worker);
    void verifyCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addVerificationSignal(OAIAddVerificationResponse summary);
    void getAllVerificationsSignal(OAIGetAllVerificationsResponse summary);
    void verifySignal();


    void addVerificationSignalFull(OAIHttpRequestWorker *worker, OAIAddVerificationResponse summary);
    void getAllVerificationsSignalFull(OAIHttpRequestWorker *worker, OAIGetAllVerificationsResponse summary);
    void verifySignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use addVerificationSignalError() instead")
    void addVerificationSignalE(OAIAddVerificationResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addVerificationSignalError(OAIAddVerificationResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAllVerificationsSignalError() instead")
    void getAllVerificationsSignalE(OAIGetAllVerificationsResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAllVerificationsSignalError(OAIGetAllVerificationsResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifySignalError() instead")
    void verifySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void verifySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addVerificationSignalErrorFull() instead")
    void addVerificationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addVerificationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAllVerificationsSignalErrorFull() instead")
    void getAllVerificationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAllVerificationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use verifySignalErrorFull() instead")
    void verifySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void verifySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
