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

#ifndef OAI_OAICOAPApi_H
#define OAI_OAICOAPApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIConfigCOAP.h"
#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICOAPApi : public QObject {
    Q_OBJECT

public:
    OAICOAPApi(const int timeOut = 0);
    ~OAICOAPApi();

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
    virtual void protocolCoapGetArgs(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolCoapGetConfig(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolCoapGetStatistics(const qint32 &agent_num);


    virtual void protocolCoapGetStatsHdr();

    /**
    * @param[in]  agent_num qint32 [required]
    */
    virtual void protocolCoapGetTrace(const qint32 &agent_num);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  argument QString [required]
    * @param[in]  value QString [required]
    */
    virtual void protocolCoapSetConfig(const qint32 &agent_num, const QString &argument, const QString &value);

    /**
    * @param[in]  agent_num qint32 [required]
    * @param[in]  enable_or_not QString [required]
    */
    virtual void protocolCoapSetTrace(const qint32 &agent_num, const QString &enable_or_not);


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

    void protocolCoapGetArgsCallback(OAIHttpRequestWorker *worker);
    void protocolCoapGetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolCoapGetStatisticsCallback(OAIHttpRequestWorker *worker);
    void protocolCoapGetStatsHdrCallback(OAIHttpRequestWorker *worker);
    void protocolCoapGetTraceCallback(OAIHttpRequestWorker *worker);
    void protocolCoapSetConfigCallback(OAIHttpRequestWorker *worker);
    void protocolCoapSetTraceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void protocolCoapGetArgsSignal(OAIObject summary);
    void protocolCoapGetConfigSignal(OAIConfigCOAP summary);
    void protocolCoapGetStatisticsSignal(QList<qint32> summary);
    void protocolCoapGetStatsHdrSignal(QList<QString> summary);
    void protocolCoapGetTraceSignal(OAIConfigCOAP summary);
    void protocolCoapSetConfigSignal(QString summary);
    void protocolCoapSetTraceSignal(QString summary);


    void protocolCoapGetArgsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void protocolCoapGetConfigSignalFull(OAIHttpRequestWorker *worker, OAIConfigCOAP summary);
    void protocolCoapGetStatisticsSignalFull(OAIHttpRequestWorker *worker, QList<qint32> summary);
    void protocolCoapGetStatsHdrSignalFull(OAIHttpRequestWorker *worker, QList<QString> summary);
    void protocolCoapGetTraceSignalFull(OAIHttpRequestWorker *worker, OAIConfigCOAP summary);
    void protocolCoapSetConfigSignalFull(OAIHttpRequestWorker *worker, QString summary);
    void protocolCoapSetTraceSignalFull(OAIHttpRequestWorker *worker, QString summary);

    Q_DECL_DEPRECATED_X("Use protocolCoapGetArgsSignalError() instead")
    void protocolCoapGetArgsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetArgsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetConfigSignalError() instead")
    void protocolCoapGetConfigSignalE(OAIConfigCOAP summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetConfigSignalError(OAIConfigCOAP summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetStatisticsSignalError() instead")
    void protocolCoapGetStatisticsSignalE(QList<qint32> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetStatisticsSignalError(QList<qint32> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetStatsHdrSignalError() instead")
    void protocolCoapGetStatsHdrSignalE(QList<QString> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetStatsHdrSignalError(QList<QString> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetTraceSignalError() instead")
    void protocolCoapGetTraceSignalE(OAIConfigCOAP summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetTraceSignalError(OAIConfigCOAP summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapSetConfigSignalError() instead")
    void protocolCoapSetConfigSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapSetConfigSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapSetTraceSignalError() instead")
    void protocolCoapSetTraceSignalE(QString summary, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapSetTraceSignalError(QString summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use protocolCoapGetArgsSignalErrorFull() instead")
    void protocolCoapGetArgsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetArgsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetConfigSignalErrorFull() instead")
    void protocolCoapGetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetStatisticsSignalErrorFull() instead")
    void protocolCoapGetStatisticsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetStatisticsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetStatsHdrSignalErrorFull() instead")
    void protocolCoapGetStatsHdrSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetStatsHdrSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapGetTraceSignalErrorFull() instead")
    void protocolCoapGetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapGetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapSetConfigSignalErrorFull() instead")
    void protocolCoapSetConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapSetConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use protocolCoapSetTraceSignalErrorFull() instead")
    void protocolCoapSetTraceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void protocolCoapSetTraceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
