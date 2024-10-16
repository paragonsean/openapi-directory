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

#ifndef OAI_OAIDomainApi_H
#define OAI_OAIDomainApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDomainCreate.h"
#include "OAIDomainResult.h"
#include "OAIError.h"
#include "OAIMultiDomainResult.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDomainApi : public QObject {
    Q_OBJECT

public:
    OAIDomainApi(const int timeOut = 0);
    ~OAIDomainApi();

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
    * @param[in]  domain_key QString [required]
    * @param[in]  checksum QString [required]
    */
    virtual void domainDomainKeyDelete(const QString &domain_key, const QString &checksum);

    /**
    * @param[in]  domain_key QString [required]
    */
    virtual void domainDomainKeyGet(const QString &domain_key);

    /**
    * @param[in]  filters QString [optional]
    */
    virtual void domainGet(const ::OpenAPI::OptionalParam<QString> &filters = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  domain OAIDomainCreate [required]
    */
    virtual void domainPost(const OAIDomainCreate &domain);


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

    void domainDomainKeyDeleteCallback(OAIHttpRequestWorker *worker);
    void domainDomainKeyGetCallback(OAIHttpRequestWorker *worker);
    void domainGetCallback(OAIHttpRequestWorker *worker);
    void domainPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void domainDomainKeyDeleteSignal(OAIObject summary);
    void domainDomainKeyGetSignal(OAIDomainResult summary);
    void domainGetSignal(OAIMultiDomainResult summary);
    void domainPostSignal(OAIDomainResult summary);


    void domainDomainKeyDeleteSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void domainDomainKeyGetSignalFull(OAIHttpRequestWorker *worker, OAIDomainResult summary);
    void domainGetSignalFull(OAIHttpRequestWorker *worker, OAIMultiDomainResult summary);
    void domainPostSignalFull(OAIHttpRequestWorker *worker, OAIDomainResult summary);

    Q_DECL_DEPRECATED_X("Use domainDomainKeyDeleteSignalError() instead")
    void domainDomainKeyDeleteSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void domainDomainKeyDeleteSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainDomainKeyGetSignalError() instead")
    void domainDomainKeyGetSignalE(OAIDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void domainDomainKeyGetSignalError(OAIDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainGetSignalError() instead")
    void domainGetSignalE(OAIMultiDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void domainGetSignalError(OAIMultiDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainPostSignalError() instead")
    void domainPostSignalE(OAIDomainResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void domainPostSignalError(OAIDomainResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use domainDomainKeyDeleteSignalErrorFull() instead")
    void domainDomainKeyDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void domainDomainKeyDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainDomainKeyGetSignalErrorFull() instead")
    void domainDomainKeyGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void domainDomainKeyGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainGetSignalErrorFull() instead")
    void domainGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void domainGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use domainPostSignalErrorFull() instead")
    void domainPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void domainPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
