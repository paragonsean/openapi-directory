/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITaskRunsApi_H
#define OAI_OAITaskRunsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorSchema.h"
#include "OAITaskRun.h"
#include "OAITaskRunListResult.h"
#include "OAITaskRunUpdateParameters.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITaskRunsApi : public QObject {
    Q_OBJECT

public:
    OAITaskRunsApi(const int timeOut = 0);
    ~OAITaskRunsApi();

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
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  task_run_name QString [required]
    * @param[in]  task_run OAITaskRun [required]
    */
    virtual void taskRunsCreate(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &task_run_name, const OAITaskRun &task_run);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  task_run_name QString [required]
    */
    virtual void taskRunsDelete(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &task_run_name);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  task_run_name QString [required]
    */
    virtual void taskRunsGet(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &task_run_name);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void taskRunsList(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  registry_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  task_run_name QString [required]
    * @param[in]  update_parameters OAITaskRunUpdateParameters [required]
    */
    virtual void taskRunsUpdate(const QString &subscription_id, const QString &resource_group_name, const QString &registry_name, const QString &api_version, const QString &task_run_name, const OAITaskRunUpdateParameters &update_parameters);


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

    void taskRunsCreateCallback(OAIHttpRequestWorker *worker);
    void taskRunsDeleteCallback(OAIHttpRequestWorker *worker);
    void taskRunsGetCallback(OAIHttpRequestWorker *worker);
    void taskRunsListCallback(OAIHttpRequestWorker *worker);
    void taskRunsUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void taskRunsCreateSignal(OAITaskRun summary);
    void taskRunsDeleteSignal();
    void taskRunsGetSignal(OAITaskRun summary);
    void taskRunsListSignal(OAITaskRunListResult summary);
    void taskRunsUpdateSignal(OAITaskRun summary);


    void taskRunsCreateSignalFull(OAIHttpRequestWorker *worker, OAITaskRun summary);
    void taskRunsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void taskRunsGetSignalFull(OAIHttpRequestWorker *worker, OAITaskRun summary);
    void taskRunsListSignalFull(OAIHttpRequestWorker *worker, OAITaskRunListResult summary);
    void taskRunsUpdateSignalFull(OAIHttpRequestWorker *worker, OAITaskRun summary);

    Q_DECL_DEPRECATED_X("Use taskRunsCreateSignalError() instead")
    void taskRunsCreateSignalE(OAITaskRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsCreateSignalError(OAITaskRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsDeleteSignalError() instead")
    void taskRunsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsGetSignalError() instead")
    void taskRunsGetSignalE(OAITaskRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsGetSignalError(OAITaskRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsListSignalError() instead")
    void taskRunsListSignalE(OAITaskRunListResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsListSignalError(OAITaskRunListResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsUpdateSignalError() instead")
    void taskRunsUpdateSignalE(OAITaskRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsUpdateSignalError(OAITaskRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use taskRunsCreateSignalErrorFull() instead")
    void taskRunsCreateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsCreateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsDeleteSignalErrorFull() instead")
    void taskRunsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsGetSignalErrorFull() instead")
    void taskRunsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsListSignalErrorFull() instead")
    void taskRunsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskRunsUpdateSignalErrorFull() instead")
    void taskRunsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskRunsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
