/**
 * OnSched API Utility
 * Endpoints for system utilities. e.g.Health
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIHealthApi_H
#define OAI_OAIHealthApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIThreadPoolInfo.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIHealthApi : public QObject {
    Q_OBJECT

public:
    OAIHealthApi(const int timeOut = 0);
    ~OAIHealthApi();

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


    virtual void utilityV1HealthHeartbeatGet();


    virtual void utilityV1HealthThreadinfoGet();


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

    void utilityV1HealthHeartbeatGetCallback(OAIHttpRequestWorker *worker);
    void utilityV1HealthThreadinfoGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void utilityV1HealthHeartbeatGetSignal(QString summary);
    void utilityV1HealthThreadinfoGetSignal(OAIThreadPoolInfo summary);


    void utilityV1HealthHeartbeatGetSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void utilityV1HealthThreadinfoGetSignalFull(OAIHttpRequestWorker *worker, OAIThreadPoolInfo summary);

    Q_DECL_DEPRECATED_X("Use utilityV1HealthHeartbeatGetSignalError() instead")
    void utilityV1HealthHeartbeatGetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void utilityV1HealthHeartbeatGetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use utilityV1HealthThreadinfoGetSignalError() instead")
    void utilityV1HealthThreadinfoGetSignalE(OAIThreadPoolInfo summary, QNetworkReply::NetworkError error_type, QString error_str);
    void utilityV1HealthThreadinfoGetSignalError(OAIThreadPoolInfo summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use utilityV1HealthHeartbeatGetSignalErrorFull() instead")
    void utilityV1HealthHeartbeatGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void utilityV1HealthHeartbeatGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use utilityV1HealthThreadinfoGetSignalErrorFull() instead")
    void utilityV1HealthThreadinfoGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void utilityV1HealthThreadinfoGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
