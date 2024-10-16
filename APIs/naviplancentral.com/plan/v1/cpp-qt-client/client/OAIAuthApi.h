/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAuthApi_H
#define OAI_OAIAuthApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAILoginModel.h"
#include "OAIPublicSessionInfoModel.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAuthApi : public QObject {
    Q_OBJECT

public:
    OAIAuthApi(const int timeOut = 0);
    ~OAIAuthApi();

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
    * @param[in]  model OAILoginModel [required]
    */
    virtual void authLoginByModel(const OAILoginModel &model);


    virtual void authLogout();


    virtual void authPasswordRequirements();


    virtual void authResumeSession();


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

    void authLoginByModelCallback(OAIHttpRequestWorker *worker);
    void authLogoutCallback(OAIHttpRequestWorker *worker);
    void authPasswordRequirementsCallback(OAIHttpRequestWorker *worker);
    void authResumeSessionCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void authLoginByModelSignal(OAIPublicSessionInfoModel summary);
    void authLogoutSignal();
    void authPasswordRequirementsSignal();
    void authResumeSessionSignal(OAIPublicSessionInfoModel summary);


    void authLoginByModelSignalFull(OAIHttpRequestWorker *worker, OAIPublicSessionInfoModel summary);
    void authLogoutSignalFull(OAIHttpRequestWorker *worker);
    void authPasswordRequirementsSignalFull(OAIHttpRequestWorker *worker);
    void authResumeSessionSignalFull(OAIHttpRequestWorker *worker, OAIPublicSessionInfoModel summary);

    Q_DECL_DEPRECATED_X("Use authLoginByModelSignalError() instead")
    void authLoginByModelSignalE(OAIPublicSessionInfoModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void authLoginByModelSignalError(OAIPublicSessionInfoModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authLogoutSignalError() instead")
    void authLogoutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authLogoutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authPasswordRequirementsSignalError() instead")
    void authPasswordRequirementsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void authPasswordRequirementsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authResumeSessionSignalError() instead")
    void authResumeSessionSignalE(OAIPublicSessionInfoModel summary, QNetworkReply::NetworkError error_type, QString error_str);
    void authResumeSessionSignalError(OAIPublicSessionInfoModel summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use authLoginByModelSignalErrorFull() instead")
    void authLoginByModelSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authLoginByModelSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authLogoutSignalErrorFull() instead")
    void authLogoutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authLogoutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authPasswordRequirementsSignalErrorFull() instead")
    void authPasswordRequirementsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authPasswordRequirementsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authResumeSessionSignalErrorFull() instead")
    void authResumeSessionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authResumeSessionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
