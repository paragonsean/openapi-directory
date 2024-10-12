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

#ifndef OAI_OAISSHApi_H
#define OAI_OAISSHApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIConfigSSH.h"
#include "OAIIPAlias.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISSHApi : public QObject {
    Q_OBJECT

public:
    OAISSHApi(const int timeOut = 0);
    ~OAISSHApi();

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
    virtual void protocolSshGetArgs(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolSshGetConfig(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolSshGetStatistics(const qint32 &agent_num);


    virtual void protocolSshGetStatsHdr();

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolSshGetTrace(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  ipaddress QString [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolSshIpaliasDisable(const qint32 &agent_num, const QString &ipaddress, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  ipaddress QString [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolSshIpaliasEnable(const qint32 &agent_num, const QString &ipaddress, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  ipaddress QString [required]
    * @param[in]  port qint32 [required]
    */
    virtual void protocolSshIpaliasIsenabled(const qint32 &agent_num, const QString &ipaddress, const qint32 &port);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolSshIpaliasList(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  argument QString [required]
    * @param[in]  value QString [required]
    */
    virtual void protocolSshSetConfig(const qint32 &agent_num, const QString &argument, const QString &value);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  enable_or_not QString [required]
    */
    virtual void protocolSshSetTrace(const qint32 &agent_num, const QString &enable_or_not);


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

    void protocolSshGetArgsCallback(OAIHttpRequestWorker *worker);
    void protocolSshGetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolSshGetStatisticsCallback(OAIHttpRequestWorker *worker);
    void protocolSshGetStatsHdrCallback(OAIHttpRequestWorker *worker);
    void protocolSshGetTraceCallback(OAIHttpRequestWorker *worker);
    void protocolSshIpaliasDisableCallback(OAIHttpRequestWorker *worker);
    void protocolSshIpaliasEnableCallback(OAIHttpRequestWorker *worker);
    void protocolSshIpaliasIsenabledCallback(OAIHttpRequestWorker *worker);
    void protocolSshIpaliasListCallback(OAIHttpRequestWorker *worker);
    void protocolSshSetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolSshSetTraceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void protocolSshGetArgsSignal(OAIObject summary);
    void protocolSshGetConfigSignal(OAIConfigSSH summary);
    void protocolSshGetStatisticsSignal(QList<qint32> summary);
    void protocolSshGetStatsHdrSignal(QList<QString> summary);
    void protocolSshGetTraceSignal(OAIConfigSSH summary);
    void protocolSshIpaliasDisableSignal(QString summary);
    void protocolSshIpaliasEnableSignal(QString summary);
    void protocolSshIpaliasIsenabledSignal(QString summary);
    void protocolSshIpaliasListSignal(QList<OAIIPAlias> summary);
    void protocolSshSetConfigSignal(QString summary);
    void protocolSshSetTraceSignal(QString summary);


    void protocolSshGetArgsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void protocolSshGetConfigSignalFull(OAIHttpRequestWorker *worker, OAIConfigSSH summary);
    void protocolSshGetStatisticsSignalFull(OAIHttpRequestWorker *worker, QList<qint32> summary);
    void protocolSshGetStatsHdrSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void protocolSshGetTraceSignalFull(OAIHttpRequestWorker *worker, OAIConfigSSH summary);
    void protocolSshIpaliasDisableSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolSshIpaliasEnableSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolSshIpaliasIsenabledSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolSshIpaliasListSignalFull(OAIHttpRequestWorker *worker, QList<OAIIPAlias> summary);
    void protocolSshSetConfigSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolSshSetTraceSignalFull(OAIHttpRequestWorker *worker, QString summary);

    Q_DECL_DEPRECATED_X("Use protocolSshGetArgsSignalError() instead")
    void protocolSshGetArgsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetArgsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetConfigSignalError() instead")
    void protocolSshGetConfigSignalE(OAIConfigSSH summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetConfigSignalError(OAIConfigSSH summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetStatisticsSignalError() instead")
    void protocolSshGetStatisticsSignalE(QList<qint32> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetStatisticsSignalError(QList<qint32> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetStatsHdrSignalError() instead")
    void protocolSshGetStatsHdrSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetStatsHdrSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetTraceSignalError() instead")
    void protocolSshGetTraceSignalE(OAIConfigSSH summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetTraceSignalError(OAIConfigSSH summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasDisableSignalError() instead")
    void protocolSshIpaliasDisableSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasDisableSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasEnableSignalError() instead")
    void protocolSshIpaliasEnableSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasEnableSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasIsenabledSignalError() instead")
    void protocolSshIpaliasIsenabledSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasIsenabledSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasListSignalError() instead")
    void protocolSshIpaliasListSignalE(QList<OAIIPAlias> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasListSignalError(QList<OAIIPAlias> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshSetConfigSignalError() instead")
    void protocolSshSetConfigSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshSetConfigSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshSetTraceSignalError() instead")
    void protocolSshSetTraceSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshSetTraceSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use protocolSshGetArgsSignalErrorFull() instead")
    void protocolSshGetArgsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetArgsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetConfigSignalErrorFull() instead")
    void protocolSshGetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetStatisticsSignalErrorFull() instead")
    void protocolSshGetStatisticsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetStatisticsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetStatsHdrSignalErrorFull() instead")
    void protocolSshGetStatsHdrSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetStatsHdrSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshGetTraceSignalErrorFull() instead")
    void protocolSshGetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshGetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasDisableSignalErrorFull() instead")
    void protocolSshIpaliasDisableSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasDisableSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasEnableSignalErrorFull() instead")
    void protocolSshIpaliasEnableSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasEnableSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasIsenabledSignalErrorFull() instead")
    void protocolSshIpaliasIsenabledSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasIsenabledSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshIpaliasListSignalErrorFull() instead")
    void protocolSshIpaliasListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshIpaliasListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshSetConfigSignalErrorFull() instead")
    void protocolSshSetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshSetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolSshSetTraceSignalErrorFull() instead")
    void protocolSshSetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolSshSetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
