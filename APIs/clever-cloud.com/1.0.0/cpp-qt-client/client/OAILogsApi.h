/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAILogsApi_H
#define OAI_OAILogsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILogsApi : public QObject {
    Q_OBJECT

public:
    OAILogsApi(const int timeOut = 0);
    ~OAILogsApi();

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
    * @param[in]  app_id QString [required]
    */
    virtual void logsAppIdDrainsGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void logsAppIdDrainsIdOrUrlDelete(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void logsAppIdDrainsIdOrUrlGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void logsAppIdDrainsPost(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  order QString [optional]
    * @param[in]  after QDateTime [optional]
    * @param[in]  before QDateTime [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  deployment_id QString [optional]
    */
    virtual void logsAppIdGet(const QString &app_id, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &order = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &deployment_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void logsAppIdSseGet(const QString &app_id);

    /**
    * @param[in]  drain_id QString [required]
    */
    virtual void logsDrainsDrainIdPut(const QString &drain_id);


    virtual void logsDrainsGet();

    /**
    * @param[in]  app_id QString [required]
    * @param[in]  download bool [optional]
    */
    virtual void logsLogsChunkedAppIdGet(const QString &app_id, const ::OpenAPI::OptionalParam<bool> &download = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  app_id QString [required]
    * @param[in]  since QDateTime [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  deployment_id QString [optional]
    */
    virtual void logsLogsSocketAppIdGet(const QString &app_id, const ::OpenAPI::OptionalParam<QDateTime> &since = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &deployment_id = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdDrainsGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdDrainsIdOrUrlDelete(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdDrainsIdOrUrlGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdDrainsPost(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdLogsChunkedGet(const QString &app_id);

    /**
    * @param[in]  app_id QString [required]
    */
    virtual void v3LogsAppIdLogsSocketGet(const QString &app_id);


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

    void logsAppIdDrainsGetCallback(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsIdOrUrlDeleteCallback(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsIdOrUrlGetCallback(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsPostCallback(OAIHttpRequestWorker *worker);
    void logsAppIdGetCallback(OAIHttpRequestWorker *worker);
    void logsAppIdSseGetCallback(OAIHttpRequestWorker *worker);
    void logsDrainsDrainIdPutCallback(OAIHttpRequestWorker *worker);
    void logsDrainsGetCallback(OAIHttpRequestWorker *worker);
    void logsLogsChunkedAppIdGetCallback(OAIHttpRequestWorker *worker);
    void logsLogsSocketAppIdGetCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsGetCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsIdOrUrlDeleteCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsIdOrUrlGetCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsPostCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdGetCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdLogsChunkedGetCallback(OAIHttpRequestWorker *worker);
    void v3LogsAppIdLogsSocketGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void logsAppIdDrainsGetSignal();
    void logsAppIdDrainsIdOrUrlDeleteSignal();
    void logsAppIdDrainsIdOrUrlGetSignal();
    void logsAppIdDrainsPostSignal();
    void logsAppIdGetSignal();
    void logsAppIdSseGetSignal();
    void logsDrainsDrainIdPutSignal();
    void logsDrainsGetSignal();
    void logsLogsChunkedAppIdGetSignal();
    void logsLogsSocketAppIdGetSignal();
    void v3LogsAppIdDrainsGetSignal();
    void v3LogsAppIdDrainsIdOrUrlDeleteSignal();
    void v3LogsAppIdDrainsIdOrUrlGetSignal();
    void v3LogsAppIdDrainsPostSignal();
    void v3LogsAppIdGetSignal();
    void v3LogsAppIdLogsChunkedGetSignal();
    void v3LogsAppIdLogsSocketGetSignal();


    void logsAppIdDrainsGetSignalFull(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsIdOrUrlDeleteSignalFull(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsIdOrUrlGetSignalFull(OAIHttpRequestWorker *worker);
    void logsAppIdDrainsPostSignalFull(OAIHttpRequestWorker *worker);
    void logsAppIdGetSignalFull(OAIHttpRequestWorker *worker);
    void logsAppIdSseGetSignalFull(OAIHttpRequestWorker *worker);
    void logsDrainsDrainIdPutSignalFull(OAIHttpRequestWorker *worker);
    void logsDrainsGetSignalFull(OAIHttpRequestWorker *worker);
    void logsLogsChunkedAppIdGetSignalFull(OAIHttpRequestWorker *worker);
    void logsLogsSocketAppIdGetSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsGetSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsIdOrUrlDeleteSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsIdOrUrlGetSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdDrainsPostSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdGetSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdLogsChunkedGetSignalFull(OAIHttpRequestWorker *worker);
    void v3LogsAppIdLogsSocketGetSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsGetSignalError() instead")
    void logsAppIdDrainsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsIdOrUrlDeleteSignalError() instead")
    void logsAppIdDrainsIdOrUrlDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsIdOrUrlDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsIdOrUrlGetSignalError() instead")
    void logsAppIdDrainsIdOrUrlGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsIdOrUrlGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsPostSignalError() instead")
    void logsAppIdDrainsPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdGetSignalError() instead")
    void logsAppIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdSseGetSignalError() instead")
    void logsAppIdSseGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdSseGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsDrainsDrainIdPutSignalError() instead")
    void logsDrainsDrainIdPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsDrainsDrainIdPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsDrainsGetSignalError() instead")
    void logsDrainsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsDrainsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsLogsChunkedAppIdGetSignalError() instead")
    void logsLogsChunkedAppIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsLogsChunkedAppIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsLogsSocketAppIdGetSignalError() instead")
    void logsLogsSocketAppIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void logsLogsSocketAppIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsGetSignalError() instead")
    void v3LogsAppIdDrainsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsIdOrUrlDeleteSignalError() instead")
    void v3LogsAppIdDrainsIdOrUrlDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsIdOrUrlDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsIdOrUrlGetSignalError() instead")
    void v3LogsAppIdDrainsIdOrUrlGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsIdOrUrlGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsPostSignalError() instead")
    void v3LogsAppIdDrainsPostSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsPostSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdGetSignalError() instead")
    void v3LogsAppIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdLogsChunkedGetSignalError() instead")
    void v3LogsAppIdLogsChunkedGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdLogsChunkedGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdLogsSocketGetSignalError() instead")
    void v3LogsAppIdLogsSocketGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdLogsSocketGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsGetSignalErrorFull() instead")
    void logsAppIdDrainsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsIdOrUrlDeleteSignalErrorFull() instead")
    void logsAppIdDrainsIdOrUrlDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsIdOrUrlDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsIdOrUrlGetSignalErrorFull() instead")
    void logsAppIdDrainsIdOrUrlGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsIdOrUrlGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdDrainsPostSignalErrorFull() instead")
    void logsAppIdDrainsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdDrainsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdGetSignalErrorFull() instead")
    void logsAppIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsAppIdSseGetSignalErrorFull() instead")
    void logsAppIdSseGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsAppIdSseGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsDrainsDrainIdPutSignalErrorFull() instead")
    void logsDrainsDrainIdPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsDrainsDrainIdPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsDrainsGetSignalErrorFull() instead")
    void logsDrainsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsDrainsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsLogsChunkedAppIdGetSignalErrorFull() instead")
    void logsLogsChunkedAppIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsLogsChunkedAppIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use logsLogsSocketAppIdGetSignalErrorFull() instead")
    void logsLogsSocketAppIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void logsLogsSocketAppIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsGetSignalErrorFull() instead")
    void v3LogsAppIdDrainsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsIdOrUrlDeleteSignalErrorFull() instead")
    void v3LogsAppIdDrainsIdOrUrlDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsIdOrUrlDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsIdOrUrlGetSignalErrorFull() instead")
    void v3LogsAppIdDrainsIdOrUrlGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsIdOrUrlGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdDrainsPostSignalErrorFull() instead")
    void v3LogsAppIdDrainsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdDrainsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdGetSignalErrorFull() instead")
    void v3LogsAppIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdLogsChunkedGetSignalErrorFull() instead")
    void v3LogsAppIdLogsChunkedGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdLogsChunkedGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use v3LogsAppIdLogsSocketGetSignalErrorFull() instead")
    void v3LogsAppIdLogsSocketGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void v3LogsAppIdLogsSocketGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
