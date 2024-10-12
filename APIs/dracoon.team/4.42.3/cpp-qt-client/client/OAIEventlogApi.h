/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIEventlogApi_H
#define OAI_OAIEventlogApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAuditNodeInfoResponse.h"
#include "OAIAuditNodeResponse.h"
#include "OAIErrorResponse.h"
#include "OAILogEventList.h"
#include "OAILogOperationList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEventlogApi : public QObject {
    Q_OBJECT

public:
    OAIEventlogApi(const int timeOut = 0);
    ~OAIEventlogApi();

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
    * @param[in]  parent_id qint64 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestAuditNodeInfo(const ::OpenAPI::OptionalParam<qint64> &parent_id = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    Q_DECL_DEPRECATED virtual void requestAuditNodeUserData(const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_sds_date_format QString [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  date_start QString [optional]
    * @param[in]  date_end QString [optional]
    * @param[in]  type qint32 [optional]
    * @param[in]  user_id qint64 [optional]
    * @param[in]  status QString [optional]
    * @param[in]  user_client QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestLogEventsAsJson(const ::OpenAPI::OptionalParam<QString> &x_sds_date_format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &date_start = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_end = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &type = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint64> &user_id = ::OpenAPI::OptionalParam<qint64>(), const ::OpenAPI::OptionalParam<QString> &status = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &user_client = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  is_deprecated bool [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestLogOperations(const ::OpenAPI::OptionalParam<bool> &is_deprecated = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());


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

    void requestAuditNodeInfoCallback(OAIHttpRequestWorker *worker);
    void requestAuditNodeUserDataCallback(OAIHttpRequestWorker *worker);
    void requestLogEventsAsJsonCallback(OAIHttpRequestWorker *worker);
    void requestLogOperationsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void requestAuditNodeInfoSignal(OAIAuditNodeInfoResponse summary);
    void requestAuditNodeUserDataSignal(QList<OAIAuditNodeResponse> summary);
    void requestLogEventsAsJsonSignal(OAILogEventList summary);
    void requestLogOperationsSignal(OAILogOperationList summary);


    void requestAuditNodeInfoSignalFull(OAIHttpRequestWorker *worker, OAIAuditNodeInfoResponse summary);
    void requestAuditNodeUserDataSignalFull(OAIHttpRequestWorker *worker, QList<OAIAuditNodeResponse> summary);
    void requestLogEventsAsJsonSignalFull(OAIHttpRequestWorker *worker, OAILogEventList summary);
    void requestLogOperationsSignalFull(OAIHttpRequestWorker *worker, OAILogOperationList summary);

    Q_DECL_DEPRECATED_X("Use requestAuditNodeInfoSignalError() instead")
    void requestAuditNodeInfoSignalE(OAIAuditNodeInfoResponse summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestAuditNodeInfoSignalError(OAIAuditNodeInfoResponse summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestAuditNodeUserDataSignalError() instead")
    void requestAuditNodeUserDataSignalE(QList<OAIAuditNodeResponse> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestAuditNodeUserDataSignalError(QList<OAIAuditNodeResponse> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestLogEventsAsJsonSignalError() instead")
    void requestLogEventsAsJsonSignalE(OAILogEventList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestLogEventsAsJsonSignalError(OAILogEventList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestLogOperationsSignalError() instead")
    void requestLogOperationsSignalE(OAILogOperationList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestLogOperationsSignalError(OAILogOperationList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use requestAuditNodeInfoSignalErrorFull() instead")
    void requestAuditNodeInfoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestAuditNodeInfoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestAuditNodeUserDataSignalErrorFull() instead")
    void requestAuditNodeUserDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestAuditNodeUserDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestLogEventsAsJsonSignalErrorFull() instead")
    void requestLogEventsAsJsonSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestLogEventsAsJsonSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestLogOperationsSignalErrorFull() instead")
    void requestLogOperationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestLogOperationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
