/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIApplicationsApi_H
#define OAI_OAIApplicationsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIApplication.h"
#include "OAIApplicationListResult.h"
#include "OAIApplications_ListByCluster_default_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIApplicationsApi : public QObject {
    Q_OBJECT

public:
    OAIApplicationsApi(const int timeOut = 0);
    ~OAIApplicationsApi();

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
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  cluster_name QString [required]
    * @param[in]  application_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIApplication [required]
    */
    virtual void applicationsCreate(const QString &subscription_id, const QString &resource_group_name, const QString &cluster_name, const QString &application_name, const QString &api_version, const OAIApplication &parameters);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  cluster_name QString [required]
    * @param[in]  application_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void applicationsDelete(const QString &subscription_id, const QString &resource_group_name, const QString &cluster_name, const QString &application_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  cluster_name QString [required]
    * @param[in]  application_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void applicationsGet(const QString &subscription_id, const QString &resource_group_name, const QString &cluster_name, const QString &application_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  cluster_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void applicationsListByCluster(const QString &subscription_id, const QString &resource_group_name, const QString &cluster_name, const QString &api_version);


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

    void applicationsCreateCallback(OAIHttpRequestWorker *worker);
    void applicationsDeleteCallback(OAIHttpRequestWorker *worker);
    void applicationsGetCallback(OAIHttpRequestWorker *worker);
    void applicationsListByClusterCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void applicationsCreateSignal(OAIApplication summary);
    void applicationsDeleteSignal();
    void applicationsGetSignal(OAIApplication summary);
    void applicationsListByClusterSignal(OAIApplicationListResult summary);


    void applicationsCreateSignalFull(OAIHttpRequestWorker *worker, OAIApplication summary);
    void applicationsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void applicationsGetSignalFull(OAIHttpRequestWorker *worker, OAIApplication summary);
    void applicationsListByClusterSignalFull(OAIHttpRequestWorker *worker, OAIApplicationListResult summary);

    Q_DECL_DEPRECATED_X("Use applicationsCreateSignalError() instead")
    void applicationsCreateSignalE(OAIApplication summary, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsCreateSignalError(OAIApplication summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsDeleteSignalError() instead")
    void applicationsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsGetSignalError() instead")
    void applicationsGetSignalE(OAIApplication summary, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsGetSignalError(OAIApplication summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsListByClusterSignalError() instead")
    void applicationsListByClusterSignalE(OAIApplicationListResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsListByClusterSignalError(OAIApplicationListResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use applicationsCreateSignalErrorFull() instead")
    void applicationsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsDeleteSignalErrorFull() instead")
    void applicationsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsGetSignalErrorFull() instead")
    void applicationsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use applicationsListByClusterSignalErrorFull() instead")
    void applicationsListByClusterSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void applicationsListByClusterSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
