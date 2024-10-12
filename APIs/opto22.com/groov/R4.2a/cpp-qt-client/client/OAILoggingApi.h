/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAILoggingApi_H
#define OAI_OAILoggingApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHttpFileElement.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILoggingApi : public QObject {
    Q_OBJECT

public:
    OAILoggingApi(const int timeOut = 0);
    ~OAILoggingApi();

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
    * @param[in]  minimum_log_level QString [optional]
    * @param[in]  last_timestamp double [optional]
    * @param[in]  filter QString [optional]
    */
    virtual void downloadLogJson(const ::OpenAPI::OptionalParam<QString> &minimum_log_level = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &last_timestamp = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  minimum_log_level QString [optional]
    * @param[in]  last_timestamp double [optional]
    * @param[in]  filter QString [optional]
    */
    virtual void downloadLogText(const ::OpenAPI::OptionalParam<QString> &minimum_log_level = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &last_timestamp = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>());


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

    void downloadLogJsonCallback(OAIHttpRequestWorker *worker);
    void downloadLogTextCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void downloadLogJsonSignal(OAIHttpFileElement summary);
    void downloadLogTextSignal(OAIHttpFileElement summary);


    void downloadLogJsonSignalFull(OAIHttpRequestWorker *worker, OAIHttpFileElement summary);
    void downloadLogTextSignalFull(OAIHttpRequestWorker *worker, OAIHttpFileElement summary);

    Q_DECL_DEPRECATED_X("Use downloadLogJsonSignalError() instead")
    void downloadLogJsonSignalE(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadLogJsonSignalError(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use downloadLogTextSignalError() instead")
    void downloadLogTextSignalE(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadLogTextSignalError(OAIHttpFileElement summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use downloadLogJsonSignalErrorFull() instead")
    void downloadLogJsonSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadLogJsonSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use downloadLogTextSignalErrorFull() instead")
    void downloadLogTextSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadLogTextSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
