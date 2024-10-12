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

#ifndef OAI_OAIGETApi_H
#define OAI_OAIGETApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIOperations_List_200_response.h"
#include "OAIOperations_List_default_response.h"
#include "OAIProjects_Get_200_response.h"
#include "OAIProjects_List_200_response.h"
#include "OAIResourceSkus_ListSkus_200_response.h"
#include "OAIServices_Get_200_response.h"
#include "OAIServices_ListSkus_200_response.h"
#include "OAIServices_List_200_response.h"
#include "OAITasks_Get_200_response.h"
#include "OAITasks_List_200_response.h"
#include "OAIUsages_List_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIGETApi : public QObject {
    Q_OBJECT

public:
    OAIGETApi(const int timeOut = 0);
    ~OAIGETApi();

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
    */
    virtual void operationsList(const QString &api_version);

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
    * @param[in]  api_version QString [required]
    */
    virtual void resourceSkusListSkus(const QString &subscription_id, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void servicesGet(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void servicesListByResourceGroup(const QString &subscription_id, const QString &group_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void servicesListSkus(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void servicesList(const QString &subscription_id, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  task_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  expand QString [optional]
    */
    virtual void tasksGet(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &task_name, const QString &api_version, const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  group_name QString [required]
    * @param[in]  service_name QString [required]
    * @param[in]  project_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  task_type QString [optional]
    */
    virtual void tasksList(const QString &subscription_id, const QString &group_name, const QString &service_name, const QString &project_name, const QString &api_version, const ::OpenAPI::OptionalParam<QString> &task_type = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  location QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void usagesList(const QString &subscription_id, const QString &location, const QString &api_version);


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

    void operationsListCallback(OAIHttpRequestWorker *worker);
    void projectsGetCallback(OAIHttpRequestWorker *worker);
    void projectsListCallback(OAIHttpRequestWorker *worker);
    void resourceSkusListSkusCallback(OAIHttpRequestWorker *worker);
    void servicesGetCallback(OAIHttpRequestWorker *worker);
    void servicesListByResourceGroupCallback(OAIHttpRequestWorker *worker);
    void servicesListSkusCallback(OAIHttpRequestWorker *worker);
    void servicesListCallback(OAIHttpRequestWorker *worker);
    void tasksGetCallback(OAIHttpRequestWorker *worker);
    void tasksListCallback(OAIHttpRequestWorker *worker);
    void usagesListCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void operationsListSignal(OAIOperations_List_200_response summary);
    void projectsGetSignal(OAIProjects_Get_200_response summary);
    void projectsListSignal(OAIProjects_List_200_response summary);
    void resourceSkusListSkusSignal(OAIResourceSkus_ListSkus_200_response summary);
    void servicesGetSignal(OAIServices_Get_200_response summary);
    void servicesListByResourceGroupSignal(OAIServices_List_200_response summary);
    void servicesListSkusSignal(OAIServices_ListSkus_200_response summary);
    void servicesListSignal(OAIServices_List_200_response summary);
    void tasksGetSignal(OAITasks_Get_200_response summary);
    void tasksListSignal(OAITasks_List_200_response summary);
    void usagesListSignal(OAIUsages_List_200_response summary);


    void operationsListSignalFull(OAIHttpRequestWorker *worker, OAIOperations_List_200_response summary);
    void projectsGetSignalFull(OAIHttpRequestWorker *worker, OAIProjects_Get_200_response summary);
    void projectsListSignalFull(OAIHttpRequestWorker *worker, OAIProjects_List_200_response summary);
    void resourceSkusListSkusSignalFull(OAIHttpRequestWorker *worker, OAIResourceSkus_ListSkus_200_response summary);
    void servicesGetSignalFull(OAIHttpRequestWorker *worker, OAIServices_Get_200_response summary);
    void servicesListByResourceGroupSignalFull(OAIHttpRequestWorker *worker, OAIServices_List_200_response summary);
    void servicesListSkusSignalFull(OAIHttpRequestWorker *worker, OAIServices_ListSkus_200_response summary);
    void servicesListSignalFull(OAIHttpRequestWorker *worker, OAIServices_List_200_response summary);
    void tasksGetSignalFull(OAIHttpRequestWorker *worker, OAITasks_Get_200_response summary);
    void tasksListSignalFull(OAIHttpRequestWorker *worker, OAITasks_List_200_response summary);
    void usagesListSignalFull(OAIHttpRequestWorker *worker, OAIUsages_List_200_response summary);

    Q_DECL_DEPRECATED_X("Use operationsListSignalError() instead")
    void operationsListSignalE(OAIOperations_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void operationsListSignalError(OAIOperations_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsGetSignalError() instead")
    void projectsGetSignalE(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalError(OAIProjects_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsListSignalError() instead")
    void projectsListSignalE(OAIProjects_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsListSignalError(OAIProjects_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resourceSkusListSkusSignalError() instead")
    void resourceSkusListSkusSignalE(OAIResourceSkus_ListSkus_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void resourceSkusListSkusSignalError(OAIResourceSkus_ListSkus_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesGetSignalError() instead")
    void servicesGetSignalE(OAIServices_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesGetSignalError(OAIServices_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListByResourceGroupSignalError() instead")
    void servicesListByResourceGroupSignalE(OAIServices_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListByResourceGroupSignalError(OAIServices_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListSkusSignalError() instead")
    void servicesListSkusSignalE(OAIServices_ListSkus_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListSkusSignalError(OAIServices_ListSkus_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListSignalError() instead")
    void servicesListSignalE(OAIServices_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListSignalError(OAIServices_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksGetSignalError() instead")
    void tasksGetSignalE(OAITasks_Get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksGetSignalError(OAITasks_Get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksListSignalError() instead")
    void tasksListSignalE(OAITasks_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksListSignalError(OAITasks_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usagesListSignalError() instead")
    void usagesListSignalE(OAIUsages_List_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void usagesListSignalError(OAIUsages_List_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use operationsListSignalErrorFull() instead")
    void operationsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void operationsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsGetSignalErrorFull() instead")
    void projectsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectsListSignalErrorFull() instead")
    void projectsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use resourceSkusListSkusSignalErrorFull() instead")
    void resourceSkusListSkusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void resourceSkusListSkusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesGetSignalErrorFull() instead")
    void servicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListByResourceGroupSignalErrorFull() instead")
    void servicesListByResourceGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListByResourceGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListSkusSignalErrorFull() instead")
    void servicesListSkusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListSkusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use servicesListSignalErrorFull() instead")
    void servicesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void servicesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksGetSignalErrorFull() instead")
    void tasksGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tasksListSignalErrorFull() instead")
    void tasksListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tasksListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use usagesListSignalErrorFull() instead")
    void usagesListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void usagesListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
