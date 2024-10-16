/**
 * Cenit IO - REST API Specification
 * Cenit IO is an Open Platform for Data and Business Integration (iPaaS) 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@cenit.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISchedulerApi_H
#define OAI_OAISchedulerApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIScheduler.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISchedulerApi : public QObject {
    Q_OBJECT

public:
    OAISchedulerApi(const int timeOut = 0);
    ~OAISchedulerApi();

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


    virtual void setupSchedulerGet();

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupSchedulerIdDelete(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void setupSchedulerIdGet(const QString &id);


    virtual void setupSchedulerPost();


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

    void setupSchedulerGetCallback(OAIHttpRequestWorker *worker);
    void setupSchedulerIdDeleteCallback(OAIHttpRequestWorker *worker);
    void setupSchedulerIdGetCallback(OAIHttpRequestWorker *worker);
    void setupSchedulerPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void setupSchedulerGetSignal(QList<OAIScheduler> summary);
    void setupSchedulerIdDeleteSignal();
    void setupSchedulerIdGetSignal(OAIScheduler summary);
    void setupSchedulerPostSignal(OAIScheduler summary);


    void setupSchedulerGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIScheduler> summary);
    void setupSchedulerIdDeleteSignalFull(OAIHttpRequestWorker *worker);
    void setupSchedulerIdGetSignalFull(OAIHttpRequestWorker *worker, OAIScheduler summary);
    void setupSchedulerPostSignalFull(OAIHttpRequestWorker *worker, OAIScheduler summary);

    Q_DECL_DEPRECATED_X("Use setupSchedulerGetSignalError() instead")
    void setupSchedulerGetSignalE(QList<OAIScheduler> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerGetSignalError(QList<OAIScheduler> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerIdDeleteSignalError() instead")
    void setupSchedulerIdDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerIdDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerIdGetSignalError() instead")
    void setupSchedulerIdGetSignalE(OAIScheduler summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerIdGetSignalError(OAIScheduler summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerPostSignalError() instead")
    void setupSchedulerPostSignalE(OAIScheduler summary, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerPostSignalError(OAIScheduler summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use setupSchedulerGetSignalErrorFull() instead")
    void setupSchedulerGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerIdDeleteSignalErrorFull() instead")
    void setupSchedulerIdDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerIdDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerIdGetSignalErrorFull() instead")
    void setupSchedulerIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use setupSchedulerPostSignalErrorFull() instead")
    void setupSchedulerPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void setupSchedulerPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
