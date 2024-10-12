/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIQueryTextsApi_H
#define OAI_OAIQueryTextsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIQueryText.h"
#include "OAIQueryTextsResultList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIQueryTextsApi : public QObject {
    Q_OBJECT

public:
    OAIQueryTextsApi(const int timeOut = 0);
    ~OAIQueryTextsApi();

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
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  query_id QString [required]
    */
    virtual void queryTextsGet(const QString &api_version, const QString &subscription_id, const QString &resource_group_name, const QString &server_name, const QString &query_id);

    /**
    * @param[in]  api_version QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  server_name QString [required]
    * @param[in]  query_ids QList<QString> [required]
    */
    virtual void queryTextsListByServer(const QString &api_version, const QString &subscription_id, const QString &resource_group_name, const QString &server_name, const QList<QString> &query_ids);


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

    void queryTextsGetCallback(OAIHttpRequestWorker *worker);
    void queryTextsListByServerCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void queryTextsGetSignal(OAIQueryText summary);
    void queryTextsListByServerSignal(OAIQueryTextsResultList summary);


    void queryTextsGetSignalFull(OAIHttpRequestWorker *worker, OAIQueryText summary);
    void queryTextsListByServerSignalFull(OAIHttpRequestWorker *worker, OAIQueryTextsResultList summary);

    Q_DECL_DEPRECATED_X("Use queryTextsGetSignalError() instead")
    void queryTextsGetSignalE(OAIQueryText summary, QNetworkReply::NetworkError error_type, QString error_str);
    void queryTextsGetSignalError(OAIQueryText summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryTextsListByServerSignalError() instead")
    void queryTextsListByServerSignalE(OAIQueryTextsResultList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void queryTextsListByServerSignalError(OAIQueryTextsResultList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use queryTextsGetSignalErrorFull() instead")
    void queryTextsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryTextsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use queryTextsListByServerSignalErrorFull() instead")
    void queryTextsListByServerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void queryTextsListByServerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
