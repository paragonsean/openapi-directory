/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAgentsApi_H
#define OAI_OAIAgentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Agent_.h"
#include "OAIBuildSystem_Shared_DTO_ActivityRun.h"
#include "OAIBuildSystem_Shared_DTO_Agent.h"
#include "OAIBuildSystem_Shared_DTO_AgentStatus.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAgentsApi : public QObject {
    Q_OBJECT

public:
    OAIAgentsApi(const int timeOut = 0);
    ~OAIAgentsApi();

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
    * @param[in]  agent_id qint32 [required]
    */
    virtual void agentsDeleteAgent(const qint32 &agent_id);

    /**
    * @param[in]  agent_id qint32 [required]
    */
    virtual void agentsGetAgentActivityRun(const qint32 &agent_id);

    /**
    * @param[in]  agent_id qint32 [required]
    */
    virtual void agentsGetAgentAsync(const qint32 &agent_id);

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void agentsGetAgents(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());


    virtual void agentsGetCurrentAgentActivityRun();


    virtual void agentsGetCurrentAgentAsync();

    /**
    * @param[in]  oai_build_system_shared_dto_agent OAIBuildSystem_Shared_DTO_Agent [required]
    */
    virtual void agentsPostAgent(const OAIBuildSystem_Shared_DTO_Agent &oai_build_system_shared_dto_agent);

    /**
    * @param[in]  agent_id qint32 [required]
    * @param[in]  oai_build_system_shared_dto_agent OAIBuildSystem_Shared_DTO_Agent [required]
    */
    virtual void agentsPutAgent(const qint32 &agent_id, const OAIBuildSystem_Shared_DTO_Agent &oai_build_system_shared_dto_agent);

    /**
    * @param[in]  agent_id qint32 [required]
    * @param[in]  oai_build_system_shared_dto_activity_run OAIBuildSystem_Shared_DTO_ActivityRun [required]
    */
    virtual void agentsPutAgentActivityRun(const qint32 &agent_id, const OAIBuildSystem_Shared_DTO_ActivityRun &oai_build_system_shared_dto_activity_run);

    /**
    * @param[in]  agent_id qint32 [required]
    * @param[in]  oai_build_system_shared_dto_agent_status OAIBuildSystem_Shared_DTO_AgentStatus [required]
    */
    virtual void agentsPutAgentStatus(const qint32 &agent_id, const OAIBuildSystem_Shared_DTO_AgentStatus &oai_build_system_shared_dto_agent_status);


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

    void agentsDeleteAgentCallback(OAIHttpRequestWorker *worker);
    void agentsGetAgentActivityRunCallback(OAIHttpRequestWorker *worker);
    void agentsGetAgentAsyncCallback(OAIHttpRequestWorker *worker);
    void agentsGetAgentsCallback(OAIHttpRequestWorker *worker);
    void agentsGetCurrentAgentActivityRunCallback(OAIHttpRequestWorker *worker);
    void agentsGetCurrentAgentAsyncCallback(OAIHttpRequestWorker *worker);
    void agentsPostAgentCallback(OAIHttpRequestWorker *worker);
    void agentsPutAgentCallback(OAIHttpRequestWorker *worker);
    void agentsPutAgentActivityRunCallback(OAIHttpRequestWorker *worker);
    void agentsPutAgentStatusCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void agentsDeleteAgentSignal();
    void agentsGetAgentActivityRunSignal(OAIBuildSystem_Shared_DTO_ActivityRun summary);
    void agentsGetAgentAsyncSignal(OAIBuildSystem_Shared_DTO_Agent summary);
    void agentsGetAgentsSignal(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Agent_ summary);
    void agentsGetCurrentAgentActivityRunSignal(OAIBuildSystem_Shared_DTO_ActivityRun summary);
    void agentsGetCurrentAgentAsyncSignal(OAIBuildSystem_Shared_DTO_Agent summary);
    void agentsPostAgentSignal(qint32 summary);
    void agentsPutAgentSignal();
    void agentsPutAgentActivityRunSignal();
    void agentsPutAgentStatusSignal();


    void agentsDeleteAgentSignalFull(OAIHttpRequestWorker *worker);
    void agentsGetAgentActivityRunSignalFull(OAIHttpRequestWorker *worker, OAIBuildSystem_Shared_DTO_ActivityRun summary);
    void agentsGetAgentAsyncSignalFull(OAIHttpRequestWorker *worker, OAIBuildSystem_Shared_DTO_Agent summary);
    void agentsGetAgentsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Agent_ summary);
    void agentsGetCurrentAgentActivityRunSignalFull(OAIHttpRequestWorker *worker, OAIBuildSystem_Shared_DTO_ActivityRun summary);
    void agentsGetCurrentAgentAsyncSignalFull(OAIHttpRequestWorker *worker, OAIBuildSystem_Shared_DTO_Agent summary);
    void agentsPostAgentSignalFull(OAIHttpRequestWorker *worker, qint32 summary);
    void agentsPutAgentSignalFull(OAIHttpRequestWorker *worker);
    void agentsPutAgentActivityRunSignalFull(OAIHttpRequestWorker *worker);
    void agentsPutAgentStatusSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use agentsDeleteAgentSignalError() instead")
    void agentsDeleteAgentSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void agentsDeleteAgentSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentActivityRunSignalError() instead")
    void agentsGetAgentActivityRunSignalE(OAIBuildSystem_Shared_DTO_ActivityRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentActivityRunSignalError(OAIBuildSystem_Shared_DTO_ActivityRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentAsyncSignalError() instead")
    void agentsGetAgentAsyncSignalE(OAIBuildSystem_Shared_DTO_Agent summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentAsyncSignalError(OAIBuildSystem_Shared_DTO_Agent summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentsSignalError() instead")
    void agentsGetAgentsSignalE(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Agent_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentsSignalError(OAIAPI_PagedResponse_BuildSystem_Shared_DTO_Agent_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetCurrentAgentActivityRunSignalError() instead")
    void agentsGetCurrentAgentActivityRunSignalE(OAIBuildSystem_Shared_DTO_ActivityRun summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetCurrentAgentActivityRunSignalError(OAIBuildSystem_Shared_DTO_ActivityRun summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetCurrentAgentAsyncSignalError() instead")
    void agentsGetCurrentAgentAsyncSignalE(OAIBuildSystem_Shared_DTO_Agent summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetCurrentAgentAsyncSignalError(OAIBuildSystem_Shared_DTO_Agent summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPostAgentSignalError() instead")
    void agentsPostAgentSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPostAgentSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentSignalError() instead")
    void agentsPutAgentSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentActivityRunSignalError() instead")
    void agentsPutAgentActivityRunSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentActivityRunSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentStatusSignalError() instead")
    void agentsPutAgentStatusSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentStatusSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use agentsDeleteAgentSignalErrorFull() instead")
    void agentsDeleteAgentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsDeleteAgentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentActivityRunSignalErrorFull() instead")
    void agentsGetAgentActivityRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentActivityRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentAsyncSignalErrorFull() instead")
    void agentsGetAgentAsyncSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentAsyncSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetAgentsSignalErrorFull() instead")
    void agentsGetAgentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetAgentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetCurrentAgentActivityRunSignalErrorFull() instead")
    void agentsGetCurrentAgentActivityRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetCurrentAgentActivityRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsGetCurrentAgentAsyncSignalErrorFull() instead")
    void agentsGetCurrentAgentAsyncSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsGetCurrentAgentAsyncSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPostAgentSignalErrorFull() instead")
    void agentsPostAgentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPostAgentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentSignalErrorFull() instead")
    void agentsPutAgentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentActivityRunSignalErrorFull() instead")
    void agentsPutAgentActivityRunSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentActivityRunSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use agentsPutAgentStatusSignalErrorFull() instead")
    void agentsPutAgentStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void agentsPutAgentStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
