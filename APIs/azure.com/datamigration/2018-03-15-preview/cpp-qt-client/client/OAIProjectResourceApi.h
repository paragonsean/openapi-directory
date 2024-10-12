/**
 * Azure Data Migration Service Resource Provider
 * The Data Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customer's virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.
 *
 * The version of the OpenAPI document: 2018-03-15-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIProjectResourceApi_H
#define OAI_OAIProjectResourceApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIOperations_List_default_response.h"
#include "OAIProjects_Get_200_response.h"
#include "OAIProjects_List_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProjectResourceApi : public QObject {
    Q_OBJECT

public:
    OAIProjectResourceApi(const int timeOut = 0);
    ~OAIProjectResourceApi();

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
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIProjects_Get_200_response [required]
    */
    virtual void projectsCreateOrUpdate(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &api_version, const OAIProjects_Get_200_response &parameters);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  delete_running_tasks bool [optional]
    */
    virtual void projectsDelete(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &api_version, const ::OpenAPI::OptionalParam<bool> &delete_running_tasks = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void projectsGet(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void projectsList(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIProjects_Get_200_response [required]
    */
    virtual void projectsUpdate(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &api_version, const OAIProjects_Get_200_response &parameters);


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

    void projectsCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void projectsDeleteCallback(OAIHttpRequestWorker *worker);
    void projectsGetCallback(OAIHttpRequestWorker *worker);
    void projectsListCallback(OAIHttpRequestWorker *worker);
    void projectsUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void projectsCreateOrUpdateSignal(OAIProjects_Get_200_response summary);
    void projectsDeleteSignal();
    void projectsGetSignal(OAIProjects_Get_200_response summary);
    void projectsListSignal(OAIProjects_List_200_response summary);
    void projectsUpdateSignal(OAIProjects_Get_200_response summary);


    void projectsCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIProjects_Get_200_response summary);
    void projectsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void projectsGetSignalFull(OAIHttpRequestWorker *worker, OAIProjects_Get_200_response summary);
    void projectsListSignalFull(OAIHttpRequestWorker *worker, OAIProjects_List_200_response summary);
    void projectsUpdateSignalFull(OAIHttpRequestWorker *worker, OAIProjects_Get_200_response summary);

    Q_DECL_DEPRECATED_X("Use projectsCreateOrUpdateSignalError() instead")
    void projectsCreateOrUpdateSignalE(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsCreateOrUpdateSignalError(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsDeleteSignalError() instead")
    void projectsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void projectsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsGetSignalError() instead")
    void projectsGetSignalE(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalError(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsListSignalError() instead")
    void projectsListSignalE(OAIProjects_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsListSignalError(OAIProjects_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsUpdateSignalError() instead")
    void projectsUpdateSignalE(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsUpdateSignalError(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use projectsCreateOrUpdateSignalErrorFull() instead")
    void projectsCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsDeleteSignalErrorFull() instead")
    void projectsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsGetSignalErrorFull() instead")
    void projectsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsListSignalErrorFull() instead")
    void projectsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsUpdateSignalErrorFull() instead")
    void projectsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
