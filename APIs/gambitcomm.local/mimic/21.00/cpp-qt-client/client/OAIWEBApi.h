/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIWEBApi_H
#define OAI_OAIWEBApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIConfigWEB.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIWEBApi : public QObject {
    Q_OBJECT

public:
    OAIWEBApi(const int timeOut = 0);
    ~OAIWEBApi();

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
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolWebGetArgs(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolWebGetConfig(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolWebGetStatistics(const qint32 &agent_num);


    virtual void protocolWebGetStatsHdr();

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolWebGetTrace(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolWebPortAdd(const qint32 &agent_num, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolWebPortExists(const qint32 &agent_num, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolWebPortRemove(const qint32 &agent_num, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    * @param[in]  protocol QString [required]
    * @param[in]  version QString [required]
    */
    virtual void protocolWebPortSet(const qint32 &agent_num, const qint32 &port, const QString &protocol, const QString &version);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolWebPortStart(const qint32 &agent_num, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolWebPortStop(const qint32 &agent_num, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  argument QString [required]
    * @param[in]  value QString [required]
    */
    virtual void protocolWebSetConfig(const qint32 &agent_num, const QString &argument, const QString &value);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  enable_or_not QString [required]
    */
    virtual void protocolWebSetTrace(const qint32 &agent_num, const QString &enable_or_not);


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

    void protocolWebGetArgsCallback(OAIHttpRequestWorker *worker);
    void protocolWebGetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolWebGetStatisticsCallback(OAIHttpRequestWorker *worker);
    void protocolWebGetStatsHdrCallback(OAIHttpRequestWorker *worker);
    void protocolWebGetTraceCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortAddCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortExistsCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortRemoveCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortSetCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortStartCallback(OAIHttpRequestWorker *worker);
    void protocolWebPortStopCallback(OAIHttpRequestWorker *worker);
    void protocolWebSetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolWebSetTraceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void protocolWebGetArgsSignal(OAIObject summary);
    void protocolWebGetConfigSignal(OAIConfigWEB summary);
    void protocolWebGetStatisticsSignal(QList<qint32> summary);
    void protocolWebGetStatsHdrSignal(QList<QString> summary);
    void protocolWebGetTraceSignal(OAIConfigWEB summary);
    void protocolWebPortAddSignal(QString summary);
    void protocolWebPortExistsSignal(QList<QString> summary);
    void protocolWebPortRemoveSignal(QString summary);
    void protocolWebPortSetSignal(QString summary);
    void protocolWebPortStartSignal(QString summary);
    void protocolWebPortStopSignal(QString summary);
    void protocolWebSetConfigSignal(QString summary);
    void protocolWebSetTraceSignal(QString summary);


    void protocolWebGetArgsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void protocolWebGetConfigSignalFull(OAIHttpRequestWorker *worker, OAIConfigWEB summary);
    void protocolWebGetStatisticsSignalFull(OAIHttpRequestWorker *worker, QList<qint32> summary);
    void protocolWebGetStatsHdrSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void protocolWebGetTraceSignalFull(OAIHttpRequestWorker *worker, OAIConfigWEB summary);
    void protocolWebPortAddSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebPortExistsSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void protocolWebPortRemoveSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebPortSetSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebPortStartSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebPortStopSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebSetConfigSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolWebSetTraceSignalFull(OAIHttpRequestWorker *worker, QString summary);

    Q_DECL_DEPRECATED_X("Use protocolWebGetArgsSignalError() instead")
    void protocolWebGetArgsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetArgsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetConfigSignalError() instead")
    void protocolWebGetConfigSignalE(OAIConfigWEB summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetConfigSignalError(OAIConfigWEB summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetStatisticsSignalError() instead")
    void protocolWebGetStatisticsSignalE(QList<qint32> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetStatisticsSignalError(QList<qint32> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetStatsHdrSignalError() instead")
    void protocolWebGetStatsHdrSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetStatsHdrSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetTraceSignalError() instead")
    void protocolWebGetTraceSignalE(OAIConfigWEB summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetTraceSignalError(OAIConfigWEB summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortAddSignalError() instead")
    void protocolWebPortAddSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortAddSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortExistsSignalError() instead")
    void protocolWebPortExistsSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortExistsSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortRemoveSignalError() instead")
    void protocolWebPortRemoveSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortRemoveSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortSetSignalError() instead")
    void protocolWebPortSetSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortSetSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortStartSignalError() instead")
    void protocolWebPortStartSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortStartSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortStopSignalError() instead")
    void protocolWebPortStopSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortStopSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebSetConfigSignalError() instead")
    void protocolWebSetConfigSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebSetConfigSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebSetTraceSignalError() instead")
    void protocolWebSetTraceSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebSetTraceSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use protocolWebGetArgsSignalErrorFull() instead")
    void protocolWebGetArgsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetArgsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetConfigSignalErrorFull() instead")
    void protocolWebGetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetStatisticsSignalErrorFull() instead")
    void protocolWebGetStatisticsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetStatisticsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetStatsHdrSignalErrorFull() instead")
    void protocolWebGetStatsHdrSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetStatsHdrSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebGetTraceSignalErrorFull() instead")
    void protocolWebGetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebGetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortAddSignalErrorFull() instead")
    void protocolWebPortAddSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortAddSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortExistsSignalErrorFull() instead")
    void protocolWebPortExistsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortExistsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortRemoveSignalErrorFull() instead")
    void protocolWebPortRemoveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortRemoveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortSetSignalErrorFull() instead")
    void protocolWebPortSetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortSetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortStartSignalErrorFull() instead")
    void protocolWebPortStartSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortStartSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebPortStopSignalErrorFull() instead")
    void protocolWebPortStopSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebPortStopSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebSetConfigSignalErrorFull() instead")
    void protocolWebSetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebSetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolWebSetTraceSignalErrorFull() instead")
    void protocolWebSetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolWebSetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
