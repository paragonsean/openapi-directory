/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISharedRulesApi_H
#define OAI_OAISharedRulesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError.h"
#include "OAIMultiSharedRulesResult.h"
#include "OAISharedRules.h"
#include "OAISharedRulesCreate.h"
#include "OAISharedRulesResult.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISharedRulesApi : public QObject {
    Q_OBJECT

public:
    OAISharedRulesApi(const int timeOut = 0);
    ~OAISharedRulesApi();

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
    * @param[in]  filters QString [optional]
    */
    virtual void sharedRulesGet(const ::OpenAPI::OptionalParam<QString> &filters = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  shared_rules OAISharedRulesCreate [required]
    */
    virtual void sharedRulesPost(const OAISharedRulesCreate &shared_rules);

    /**
    * @param[in]  shared_rules_key QString [required]
    */
    virtual void sharedRulesSharedRulesKeyGet(const QString &shared_rules_key);

    /**
    * @param[in]  shared_rules_key QString [required]
    * @param[in]  shared_rules OAISharedRules [required]
    */
    virtual void sharedRulesSharedRulesKeyPut(const QString &shared_rules_key, const OAISharedRules &shared_rules);


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

    void sharedRulesGetCallback(OAIHttpRequestWorker *worker);
    void sharedRulesPostCallback(OAIHttpRequestWorker *worker);
    void sharedRulesSharedRulesKeyGetCallback(OAIHttpRequestWorker *worker);
    void sharedRulesSharedRulesKeyPutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void sharedRulesGetSignal(OAIMultiSharedRulesResult summary);
    void sharedRulesPostSignal(OAISharedRulesResult summary);
    void sharedRulesSharedRulesKeyGetSignal(OAISharedRulesResult summary);
    void sharedRulesSharedRulesKeyPutSignal(OAISharedRulesResult summary);


    void sharedRulesGetSignalFull(OAIHttpRequestWorker *worker, OAIMultiSharedRulesResult summary);
    void sharedRulesPostSignalFull(OAIHttpRequestWorker *worker, OAISharedRulesResult summary);
    void sharedRulesSharedRulesKeyGetSignalFull(OAIHttpRequestWorker *worker, OAISharedRulesResult summary);
    void sharedRulesSharedRulesKeyPutSignalFull(OAIHttpRequestWorker *worker, OAISharedRulesResult summary);

    Q_DECL_DEPRECATED_X("Use sharedRulesGetSignalError() instead")
    void sharedRulesGetSignalE(OAIMultiSharedRulesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesGetSignalError(OAIMultiSharedRulesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesPostSignalError() instead")
    void sharedRulesPostSignalE(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesPostSignalError(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesSharedRulesKeyGetSignalError() instead")
    void sharedRulesSharedRulesKeyGetSignalE(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesSharedRulesKeyGetSignalError(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesSharedRulesKeyPutSignalError() instead")
    void sharedRulesSharedRulesKeyPutSignalE(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesSharedRulesKeyPutSignalError(OAISharedRulesResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use sharedRulesGetSignalErrorFull() instead")
    void sharedRulesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesPostSignalErrorFull() instead")
    void sharedRulesPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesSharedRulesKeyGetSignalErrorFull() instead")
    void sharedRulesSharedRulesKeyGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesSharedRulesKeyGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use sharedRulesSharedRulesKeyPutSignalErrorFull() instead")
    void sharedRulesSharedRulesKeyPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void sharedRulesSharedRulesKeyPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
