/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPrometheusAPIApi_H
#define OAI_OAIPrometheusAPIApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGrafanaBoard.h"
#include "OAIPrometheus.h"
#include "OAISelectedGrafanaConfig.h"
#include <QMap>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPrometheusAPIApi : public QObject {
    Q_OBJECT

public:
    OAIPrometheusAPIApi(const int timeOut = 0);
    ~OAIPrometheusAPIApi();

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


    virtual void idDeletePrometheusConfig();


    virtual void idGetPrometheusConfig();


    virtual void idGetPrometheusPing();


    virtual void idGetPrometheusQuery();


    virtual void idGetPrometheusStaticBoard();

    /**
    * @param[in]  oai_selected_grafana_config QList<OAISelectedGrafanaConfig> [required]
    */
    virtual void idPostPrometheusBoard(const QList<OAISelectedGrafanaConfig> &oai_selected_grafana_config);


    virtual void idPostPrometheusBoardImport();

    /**
    * @param[in]  body QString [optional]
    */
    virtual void idPostPrometheusConfig(const ::OpenAPI::OptionalParam<QString> &body = ::OpenAPI::OptionalParam<QString>());


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

    void idDeletePrometheusConfigCallback(OAIHttpRequestWorker *worker);
    void idGetPrometheusConfigCallback(OAIHttpRequestWorker *worker);
    void idGetPrometheusPingCallback(OAIHttpRequestWorker *worker);
    void idGetPrometheusQueryCallback(OAIHttpRequestWorker *worker);
    void idGetPrometheusStaticBoardCallback(OAIHttpRequestWorker *worker);
    void idPostPrometheusBoardCallback(OAIHttpRequestWorker *worker);
    void idPostPrometheusBoardImportCallback(OAIHttpRequestWorker *worker);
    void idPostPrometheusConfigCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void idDeletePrometheusConfigSignal();
    void idGetPrometheusConfigSignal(OAIPrometheus summary);
    void idGetPrometheusPingSignal();
    void idGetPrometheusQuerySignal();
    void idGetPrometheusStaticBoardSignal(QMap<QString, OAIGrafanaBoard> summary);
    void idPostPrometheusBoardSignal();
    void idPostPrometheusBoardImportSignal(OAIGrafanaBoard summary);
    void idPostPrometheusConfigSignal();


    void idDeletePrometheusConfigSignalFull(OAIHttpRequestWorker *worker);
    void idGetPrometheusConfigSignalFull(OAIHttpRequestWorker *worker, OAIPrometheus summary);
    void idGetPrometheusPingSignalFull(OAIHttpRequestWorker *worker);
    void idGetPrometheusQuerySignalFull(OAIHttpRequestWorker *worker);
    void idGetPrometheusStaticBoardSignalFull(OAIHttpRequestWorker *worker, QMap<QString, OAIGrafanaBoard> summary);
    void idPostPrometheusBoardSignalFull(OAIHttpRequestWorker *worker);
    void idPostPrometheusBoardImportSignalFull(OAIHttpRequestWorker *worker, OAIGrafanaBoard summary);
    void idPostPrometheusConfigSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use idDeletePrometheusConfigSignalError() instead")
    void idDeletePrometheusConfigSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void idDeletePrometheusConfigSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusConfigSignalError() instead")
    void idGetPrometheusConfigSignalE(OAIPrometheus summary, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusConfigSignalError(OAIPrometheus summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusPingSignalError() instead")
    void idGetPrometheusPingSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusPingSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusQuerySignalError() instead")
    void idGetPrometheusQuerySignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusQuerySignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusStaticBoardSignalError() instead")
    void idGetPrometheusStaticBoardSignalE(QMap<QString, OAIGrafanaBoard> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusStaticBoardSignalError(QMap<QString, OAIGrafanaBoard> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusBoardSignalError() instead")
    void idPostPrometheusBoardSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusBoardSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusBoardImportSignalError() instead")
    void idPostPrometheusBoardImportSignalE(OAIGrafanaBoard summary, QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusBoardImportSignalError(OAIGrafanaBoard summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusConfigSignalError() instead")
    void idPostPrometheusConfigSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusConfigSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use idDeletePrometheusConfigSignalErrorFull() instead")
    void idDeletePrometheusConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idDeletePrometheusConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusConfigSignalErrorFull() instead")
    void idGetPrometheusConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusPingSignalErrorFull() instead")
    void idGetPrometheusPingSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusPingSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusQuerySignalErrorFull() instead")
    void idGetPrometheusQuerySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusQuerySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idGetPrometheusStaticBoardSignalErrorFull() instead")
    void idGetPrometheusStaticBoardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idGetPrometheusStaticBoardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusBoardSignalErrorFull() instead")
    void idPostPrometheusBoardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusBoardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusBoardImportSignalErrorFull() instead")
    void idPostPrometheusBoardImportSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusBoardImportSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use idPostPrometheusConfigSignalErrorFull() instead")
    void idPostPrometheusConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void idPostPrometheusConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
