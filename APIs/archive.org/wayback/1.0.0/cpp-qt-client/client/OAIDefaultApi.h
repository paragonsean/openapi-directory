/**
 * Wayback API
 * API for Internet Archive's Wayback Machine
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAvailabilityRequest.h"
#include "OAIAvailabilityResults.h"
#include "OAIError.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  url QString [required]
    * @param[in]  timestamp QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  timeout double [optional]
    * @param[in]  closest QString [optional]
    * @param[in]  status_code qint32 [optional]
    * @param[in]  tag QString [optional]
    */
    virtual void waybackV1AvailableGet(const QString &url, const ::OpenAPI::OptionalParam<QString> &timestamp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &timeout = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &closest = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &status_code = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &tag = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  url QString [required]
    * @param[in]  timestamp QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  timeout double [optional]
    * @param[in]  closest QString [optional]
    * @param[in]  status_code qint32 [optional]
    * @param[in]  tag QString [optional]
    * @param[in]  oai_availability_request QList<OAIAvailabilityRequest> [optional]
    */
    virtual void waybackV1AvailablePost(const QString &url, const ::OpenAPI::OptionalParam<QString> &timestamp = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &timeout = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &closest = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &status_code = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QList<OAIAvailabilityRequest>> &oai_availability_request = ::OpenAPI::OptionalParam<QList<OAIAvailabilityRequest>>());


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

    void waybackV1AvailableGetCallback(OAIHttpRequestWorker *worker);
    void waybackV1AvailablePostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void waybackV1AvailableGetSignal();
    void waybackV1AvailablePostSignal();


    void waybackV1AvailableGetSignalFull(OAIHttpRequestWorker *worker);
    void waybackV1AvailablePostSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use waybackV1AvailableGetSignalError() instead")
    void waybackV1AvailableGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void waybackV1AvailableGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use waybackV1AvailablePostSignalError() instead")
    void waybackV1AvailablePostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void waybackV1AvailablePostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use waybackV1AvailableGetSignalErrorFull() instead")
    void waybackV1AvailableGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void waybackV1AvailableGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use waybackV1AvailablePostSignalErrorFull() instead")
    void waybackV1AvailablePostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void waybackV1AvailablePostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
