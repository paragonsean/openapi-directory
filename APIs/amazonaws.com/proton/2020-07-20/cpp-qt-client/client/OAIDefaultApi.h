/**
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAcceptEnvironmentAccountConnectionInput.h"
#include "OAIAcceptEnvironmentAccountConnectionOutput.h"
#include "OAICancelComponentDeploymentInput.h"
#include "OAICancelComponentDeploymentOutput.h"
#include "OAICancelEnvironmentDeploymentInput.h"
#include "OAICancelEnvironmentDeploymentOutput.h"
#include "OAICancelServiceInstanceDeploymentInput.h"
#include "OAICancelServiceInstanceDeploymentOutput.h"
#include "OAICancelServicePipelineDeploymentInput.h"
#include "OAICancelServicePipelineDeploymentOutput.h"
#include "OAICreateComponentInput.h"
#include "OAICreateComponentOutput.h"
#include "OAICreateEnvironmentAccountConnectionInput.h"
#include "OAICreateEnvironmentAccountConnectionOutput.h"
#include "OAICreateEnvironmentInput.h"
#include "OAICreateEnvironmentOutput.h"
#include "OAICreateEnvironmentTemplateInput.h"
#include "OAICreateEnvironmentTemplateOutput.h"
#include "OAICreateEnvironmentTemplateVersionInput.h"
#include "OAICreateEnvironmentTemplateVersionOutput.h"
#include "OAICreateRepositoryInput.h"
#include "OAICreateRepositoryOutput.h"
#include "OAICreateServiceInput.h"
#include "OAICreateServiceInstanceInput.h"
#include "OAICreateServiceInstanceOutput.h"
#include "OAICreateServiceOutput.h"
#include "OAICreateServiceSyncConfigInput.h"
#include "OAICreateServiceSyncConfigOutput.h"
#include "OAICreateServiceTemplateInput.h"
#include "OAICreateServiceTemplateOutput.h"
#include "OAICreateServiceTemplateVersionInput.h"
#include "OAICreateServiceTemplateVersionOutput.h"
#include "OAICreateTemplateSyncConfigInput.h"
#include "OAICreateTemplateSyncConfigOutput.h"
#include "OAIDeleteComponentInput.h"
#include "OAIDeleteComponentOutput.h"
#include "OAIDeleteDeploymentInput.h"
#include "OAIDeleteDeploymentOutput.h"
#include "OAIDeleteEnvironmentAccountConnectionInput.h"
#include "OAIDeleteEnvironmentAccountConnectionOutput.h"
#include "OAIDeleteEnvironmentInput.h"
#include "OAIDeleteEnvironmentOutput.h"
#include "OAIDeleteEnvironmentTemplateInput.h"
#include "OAIDeleteEnvironmentTemplateOutput.h"
#include "OAIDeleteEnvironmentTemplateVersionInput.h"
#include "OAIDeleteEnvironmentTemplateVersionOutput.h"
#include "OAIDeleteRepositoryInput.h"
#include "OAIDeleteRepositoryOutput.h"
#include "OAIDeleteServiceInput.h"
#include "OAIDeleteServiceOutput.h"
#include "OAIDeleteServiceSyncConfigInput.h"
#include "OAIDeleteServiceSyncConfigOutput.h"
#include "OAIDeleteServiceTemplateInput.h"
#include "OAIDeleteServiceTemplateOutput.h"
#include "OAIDeleteServiceTemplateVersionInput.h"
#include "OAIDeleteServiceTemplateVersionOutput.h"
#include "OAIDeleteTemplateSyncConfigInput.h"
#include "OAIDeleteTemplateSyncConfigOutput.h"
#include "OAIGetAccountSettingsOutput.h"
#include "OAIGetComponentInput.h"
#include "OAIGetComponentOutput.h"
#include "OAIGetDeploymentInput.h"
#include "OAIGetDeploymentOutput.h"
#include "OAIGetEnvironmentAccountConnectionInput.h"
#include "OAIGetEnvironmentAccountConnectionOutput.h"
#include "OAIGetEnvironmentInput.h"
#include "OAIGetEnvironmentOutput.h"
#include "OAIGetEnvironmentTemplateInput.h"
#include "OAIGetEnvironmentTemplateOutput.h"
#include "OAIGetEnvironmentTemplateVersionInput.h"
#include "OAIGetEnvironmentTemplateVersionOutput.h"
#include "OAIGetRepositoryInput.h"
#include "OAIGetRepositoryOutput.h"
#include "OAIGetRepositorySyncStatusInput.h"
#include "OAIGetRepositorySyncStatusOutput.h"
#include "OAIGetResourcesSummaryOutput.h"
#include "OAIGetServiceInput.h"
#include "OAIGetServiceInstanceInput.h"
#include "OAIGetServiceInstanceOutput.h"
#include "OAIGetServiceInstanceSyncStatusInput.h"
#include "OAIGetServiceInstanceSyncStatusOutput.h"
#include "OAIGetServiceOutput.h"
#include "OAIGetServiceSyncBlockerSummaryInput.h"
#include "OAIGetServiceSyncBlockerSummaryOutput.h"
#include "OAIGetServiceSyncConfigInput.h"
#include "OAIGetServiceSyncConfigOutput.h"
#include "OAIGetServiceTemplateInput.h"
#include "OAIGetServiceTemplateOutput.h"
#include "OAIGetServiceTemplateVersionInput.h"
#include "OAIGetServiceTemplateVersionOutput.h"
#include "OAIGetTemplateSyncConfigInput.h"
#include "OAIGetTemplateSyncConfigOutput.h"
#include "OAIGetTemplateSyncStatusInput.h"
#include "OAIGetTemplateSyncStatusOutput.h"
#include "OAIListComponentOutputsInput.h"
#include "OAIListComponentOutputsOutput.h"
#include "OAIListComponentProvisionedResourcesInput.h"
#include "OAIListComponentProvisionedResourcesOutput.h"
#include "OAIListComponentsInput.h"
#include "OAIListComponentsOutput.h"
#include "OAIListDeploymentsInput.h"
#include "OAIListDeploymentsOutput.h"
#include "OAIListEnvironmentAccountConnectionsInput.h"
#include "OAIListEnvironmentAccountConnectionsOutput.h"
#include "OAIListEnvironmentOutputsInput.h"
#include "OAIListEnvironmentOutputsOutput.h"
#include "OAIListEnvironmentProvisionedResourcesInput.h"
#include "OAIListEnvironmentProvisionedResourcesOutput.h"
#include "OAIListEnvironmentTemplateVersionsInput.h"
#include "OAIListEnvironmentTemplateVersionsOutput.h"
#include "OAIListEnvironmentTemplatesInput.h"
#include "OAIListEnvironmentTemplatesOutput.h"
#include "OAIListEnvironmentsInput.h"
#include "OAIListEnvironmentsOutput.h"
#include "OAIListRepositoriesInput.h"
#include "OAIListRepositoriesOutput.h"
#include "OAIListRepositorySyncDefinitionsInput.h"
#include "OAIListRepositorySyncDefinitionsOutput.h"
#include "OAIListServiceInstanceOutputsInput.h"
#include "OAIListServiceInstanceOutputsOutput.h"
#include "OAIListServiceInstanceProvisionedResourcesInput.h"
#include "OAIListServiceInstanceProvisionedResourcesOutput.h"
#include "OAIListServiceInstancesInput.h"
#include "OAIListServiceInstancesOutput.h"
#include "OAIListServicePipelineOutputsInput.h"
#include "OAIListServicePipelineOutputsOutput.h"
#include "OAIListServicePipelineProvisionedResourcesInput.h"
#include "OAIListServicePipelineProvisionedResourcesOutput.h"
#include "OAIListServiceTemplateVersionsInput.h"
#include "OAIListServiceTemplateVersionsOutput.h"
#include "OAIListServiceTemplatesInput.h"
#include "OAIListServiceTemplatesOutput.h"
#include "OAIListServicesInput.h"
#include "OAIListServicesOutput.h"
#include "OAIListTagsForResourceInput.h"
#include "OAIListTagsForResourceOutput.h"
#include "OAINotifyResourceDeploymentStatusChangeInput.h"
#include "OAIObject.h"
#include "OAIRejectEnvironmentAccountConnectionInput.h"
#include "OAIRejectEnvironmentAccountConnectionOutput.h"
#include "OAITagResourceInput.h"
#include "OAIUntagResourceInput.h"
#include "OAIUpdateAccountSettingsInput.h"
#include "OAIUpdateAccountSettingsOutput.h"
#include "OAIUpdateComponentInput.h"
#include "OAIUpdateComponentOutput.h"
#include "OAIUpdateEnvironmentAccountConnectionInput.h"
#include "OAIUpdateEnvironmentAccountConnectionOutput.h"
#include "OAIUpdateEnvironmentInput.h"
#include "OAIUpdateEnvironmentOutput.h"
#include "OAIUpdateEnvironmentTemplateInput.h"
#include "OAIUpdateEnvironmentTemplateOutput.h"
#include "OAIUpdateEnvironmentTemplateVersionInput.h"
#include "OAIUpdateEnvironmentTemplateVersionOutput.h"
#include "OAIUpdateServiceInput.h"
#include "OAIUpdateServiceInstanceInput.h"
#include "OAIUpdateServiceInstanceOutput.h"
#include "OAIUpdateServiceOutput.h"
#include "OAIUpdateServicePipelineInput.h"
#include "OAIUpdateServicePipelineOutput.h"
#include "OAIUpdateServiceSyncBlockerInput.h"
#include "OAIUpdateServiceSyncBlockerOutput.h"
#include "OAIUpdateServiceSyncConfigInput.h"
#include "OAIUpdateServiceSyncConfigOutput.h"
#include "OAIUpdateServiceTemplateInput.h"
#include "OAIUpdateServiceTemplateOutput.h"
#include "OAIUpdateServiceTemplateVersionInput.h"
#include "OAIUpdateServiceTemplateVersionOutput.h"
#include "OAIUpdateTemplateSyncConfigInput.h"
#include "OAIUpdateTemplateSyncConfigOutput.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_accept_environment_account_connection_input OAIAcceptEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void acceptEnvironmentAccountConnection(const QString &x_amz_target, const OAIAcceptEnvironmentAccountConnectionInput &oai_accept_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_cancel_component_deployment_input OAICancelComponentDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void cancelComponentDeployment(const QString &x_amz_target, const OAICancelComponentDeploymentInput &oai_cancel_component_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_cancel_environment_deployment_input OAICancelEnvironmentDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void cancelEnvironmentDeployment(const QString &x_amz_target, const OAICancelEnvironmentDeploymentInput &oai_cancel_environment_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_cancel_service_instance_deployment_input OAICancelServiceInstanceDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void cancelServiceInstanceDeployment(const QString &x_amz_target, const OAICancelServiceInstanceDeploymentInput &oai_cancel_service_instance_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_cancel_service_pipeline_deployment_input OAICancelServicePipelineDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void cancelServicePipelineDeployment(const QString &x_amz_target, const OAICancelServicePipelineDeploymentInput &oai_cancel_service_pipeline_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_component_input OAICreateComponentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createComponent(const QString &x_amz_target, const OAICreateComponentInput &oai_create_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_environment_input OAICreateEnvironmentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createEnvironment(const QString &x_amz_target, const OAICreateEnvironmentInput &oai_create_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_environment_account_connection_input OAICreateEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createEnvironmentAccountConnection(const QString &x_amz_target, const OAICreateEnvironmentAccountConnectionInput &oai_create_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_environment_template_input OAICreateEnvironmentTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createEnvironmentTemplate(const QString &x_amz_target, const OAICreateEnvironmentTemplateInput &oai_create_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_environment_template_version_input OAICreateEnvironmentTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createEnvironmentTemplateVersion(const QString &x_amz_target, const OAICreateEnvironmentTemplateVersionInput &oai_create_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_repository_input OAICreateRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createRepository(const QString &x_amz_target, const OAICreateRepositoryInput &oai_create_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_service_input OAICreateServiceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createService(const QString &x_amz_target, const OAICreateServiceInput &oai_create_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_service_instance_input OAICreateServiceInstanceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createServiceInstance(const QString &x_amz_target, const OAICreateServiceInstanceInput &oai_create_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_service_sync_config_input OAICreateServiceSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createServiceSyncConfig(const QString &x_amz_target, const OAICreateServiceSyncConfigInput &oai_create_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_service_template_input OAICreateServiceTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createServiceTemplate(const QString &x_amz_target, const OAICreateServiceTemplateInput &oai_create_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_service_template_version_input OAICreateServiceTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createServiceTemplateVersion(const QString &x_amz_target, const OAICreateServiceTemplateVersionInput &oai_create_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_create_template_sync_config_input OAICreateTemplateSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void createTemplateSyncConfig(const QString &x_amz_target, const OAICreateTemplateSyncConfigInput &oai_create_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_component_input OAIDeleteComponentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteComponent(const QString &x_amz_target, const OAIDeleteComponentInput &oai_delete_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_deployment_input OAIDeleteDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteDeployment(const QString &x_amz_target, const OAIDeleteDeploymentInput &oai_delete_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_environment_input OAIDeleteEnvironmentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteEnvironment(const QString &x_amz_target, const OAIDeleteEnvironmentInput &oai_delete_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_environment_account_connection_input OAIDeleteEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteEnvironmentAccountConnection(const QString &x_amz_target, const OAIDeleteEnvironmentAccountConnectionInput &oai_delete_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_environment_template_input OAIDeleteEnvironmentTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteEnvironmentTemplate(const QString &x_amz_target, const OAIDeleteEnvironmentTemplateInput &oai_delete_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_environment_template_version_input OAIDeleteEnvironmentTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteEnvironmentTemplateVersion(const QString &x_amz_target, const OAIDeleteEnvironmentTemplateVersionInput &oai_delete_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_repository_input OAIDeleteRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteRepository(const QString &x_amz_target, const OAIDeleteRepositoryInput &oai_delete_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_service_input OAIDeleteServiceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteService(const QString &x_amz_target, const OAIDeleteServiceInput &oai_delete_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_service_sync_config_input OAIDeleteServiceSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteServiceSyncConfig(const QString &x_amz_target, const OAIDeleteServiceSyncConfigInput &oai_delete_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_service_template_input OAIDeleteServiceTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteServiceTemplate(const QString &x_amz_target, const OAIDeleteServiceTemplateInput &oai_delete_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_service_template_version_input OAIDeleteServiceTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteServiceTemplateVersion(const QString &x_amz_target, const OAIDeleteServiceTemplateVersionInput &oai_delete_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_delete_template_sync_config_input OAIDeleteTemplateSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void deleteTemplateSyncConfig(const QString &x_amz_target, const OAIDeleteTemplateSyncConfigInput &oai_delete_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  body OAIObject [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getAccountSettings(const QString &x_amz_target, const OAIObject &body, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_component_input OAIGetComponentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getComponent(const QString &x_amz_target, const OAIGetComponentInput &oai_get_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_deployment_input OAIGetDeploymentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getDeployment(const QString &x_amz_target, const OAIGetDeploymentInput &oai_get_deployment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_environment_input OAIGetEnvironmentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getEnvironment(const QString &x_amz_target, const OAIGetEnvironmentInput &oai_get_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_environment_account_connection_input OAIGetEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getEnvironmentAccountConnection(const QString &x_amz_target, const OAIGetEnvironmentAccountConnectionInput &oai_get_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_environment_template_input OAIGetEnvironmentTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getEnvironmentTemplate(const QString &x_amz_target, const OAIGetEnvironmentTemplateInput &oai_get_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_environment_template_version_input OAIGetEnvironmentTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getEnvironmentTemplateVersion(const QString &x_amz_target, const OAIGetEnvironmentTemplateVersionInput &oai_get_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_repository_input OAIGetRepositoryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRepository(const QString &x_amz_target, const OAIGetRepositoryInput &oai_get_repository_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_repository_sync_status_input OAIGetRepositorySyncStatusInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getRepositorySyncStatus(const QString &x_amz_target, const OAIGetRepositorySyncStatusInput &oai_get_repository_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  body OAIObject [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getResourcesSummary(const QString &x_amz_target, const OAIObject &body, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_input OAIGetServiceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getService(const QString &x_amz_target, const OAIGetServiceInput &oai_get_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_instance_input OAIGetServiceInstanceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceInstance(const QString &x_amz_target, const OAIGetServiceInstanceInput &oai_get_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_instance_sync_status_input OAIGetServiceInstanceSyncStatusInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceInstanceSyncStatus(const QString &x_amz_target, const OAIGetServiceInstanceSyncStatusInput &oai_get_service_instance_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_sync_blocker_summary_input OAIGetServiceSyncBlockerSummaryInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceSyncBlockerSummary(const QString &x_amz_target, const OAIGetServiceSyncBlockerSummaryInput &oai_get_service_sync_blocker_summary_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_sync_config_input OAIGetServiceSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceSyncConfig(const QString &x_amz_target, const OAIGetServiceSyncConfigInput &oai_get_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_template_input OAIGetServiceTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceTemplate(const QString &x_amz_target, const OAIGetServiceTemplateInput &oai_get_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_service_template_version_input OAIGetServiceTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getServiceTemplateVersion(const QString &x_amz_target, const OAIGetServiceTemplateVersionInput &oai_get_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_template_sync_config_input OAIGetTemplateSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getTemplateSyncConfig(const QString &x_amz_target, const OAIGetTemplateSyncConfigInput &oai_get_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_get_template_sync_status_input OAIGetTemplateSyncStatusInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void getTemplateSyncStatus(const QString &x_amz_target, const OAIGetTemplateSyncStatusInput &oai_get_template_sync_status_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_component_outputs_input OAIListComponentOutputsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listComponentOutputs(const QString &x_amz_target, const OAIListComponentOutputsInput &oai_list_component_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_component_provisioned_resources_input OAIListComponentProvisionedResourcesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listComponentProvisionedResources(const QString &x_amz_target, const OAIListComponentProvisionedResourcesInput &oai_list_component_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_components_input OAIListComponentsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listComponents(const QString &x_amz_target, const OAIListComponentsInput &oai_list_components_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_deployments_input OAIListDeploymentsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listDeployments(const QString &x_amz_target, const OAIListDeploymentsInput &oai_list_deployments_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environment_account_connections_input OAIListEnvironmentAccountConnectionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironmentAccountConnections(const QString &x_amz_target, const OAIListEnvironmentAccountConnectionsInput &oai_list_environment_account_connections_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environment_outputs_input OAIListEnvironmentOutputsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironmentOutputs(const QString &x_amz_target, const OAIListEnvironmentOutputsInput &oai_list_environment_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environment_provisioned_resources_input OAIListEnvironmentProvisionedResourcesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironmentProvisionedResources(const QString &x_amz_target, const OAIListEnvironmentProvisionedResourcesInput &oai_list_environment_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environment_template_versions_input OAIListEnvironmentTemplateVersionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironmentTemplateVersions(const QString &x_amz_target, const OAIListEnvironmentTemplateVersionsInput &oai_list_environment_template_versions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environment_templates_input OAIListEnvironmentTemplatesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironmentTemplates(const QString &x_amz_target, const OAIListEnvironmentTemplatesInput &oai_list_environment_templates_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_environments_input OAIListEnvironmentsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listEnvironments(const QString &x_amz_target, const OAIListEnvironmentsInput &oai_list_environments_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_repositories_input OAIListRepositoriesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRepositories(const QString &x_amz_target, const OAIListRepositoriesInput &oai_list_repositories_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_repository_sync_definitions_input OAIListRepositorySyncDefinitionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listRepositorySyncDefinitions(const QString &x_amz_target, const OAIListRepositorySyncDefinitionsInput &oai_list_repository_sync_definitions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_instance_outputs_input OAIListServiceInstanceOutputsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServiceInstanceOutputs(const QString &x_amz_target, const OAIListServiceInstanceOutputsInput &oai_list_service_instance_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_instance_provisioned_resources_input OAIListServiceInstanceProvisionedResourcesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServiceInstanceProvisionedResources(const QString &x_amz_target, const OAIListServiceInstanceProvisionedResourcesInput &oai_list_service_instance_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_instances_input OAIListServiceInstancesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServiceInstances(const QString &x_amz_target, const OAIListServiceInstancesInput &oai_list_service_instances_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_pipeline_outputs_input OAIListServicePipelineOutputsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServicePipelineOutputs(const QString &x_amz_target, const OAIListServicePipelineOutputsInput &oai_list_service_pipeline_outputs_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_pipeline_provisioned_resources_input OAIListServicePipelineProvisionedResourcesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServicePipelineProvisionedResources(const QString &x_amz_target, const OAIListServicePipelineProvisionedResourcesInput &oai_list_service_pipeline_provisioned_resources_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_template_versions_input OAIListServiceTemplateVersionsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServiceTemplateVersions(const QString &x_amz_target, const OAIListServiceTemplateVersionsInput &oai_list_service_template_versions_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_service_templates_input OAIListServiceTemplatesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServiceTemplates(const QString &x_amz_target, const OAIListServiceTemplatesInput &oai_list_service_templates_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_services_input OAIListServicesInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listServices(const QString &x_amz_target, const OAIListServicesInput &oai_list_services_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_list_tags_for_resource_input OAIListTagsForResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    * @param[in]  max_results QString [optional]
    * @param[in]  next_token QString [optional]
    */
    virtual void listTagsForResource(const QString &x_amz_target, const OAIListTagsForResourceInput &oai_list_tags_for_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &max_results = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &next_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_notify_resource_deployment_status_change_input OAINotifyResourceDeploymentStatusChangeInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void notifyResourceDeploymentStatusChange(const QString &x_amz_target, const OAINotifyResourceDeploymentStatusChangeInput &oai_notify_resource_deployment_status_change_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_reject_environment_account_connection_input OAIRejectEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void rejectEnvironmentAccountConnection(const QString &x_amz_target, const OAIRejectEnvironmentAccountConnectionInput &oai_reject_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_tag_resource_input OAITagResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void tagResource(const QString &x_amz_target, const OAITagResourceInput &oai_tag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_untag_resource_input OAIUntagResourceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void untagResource(const QString &x_amz_target, const OAIUntagResourceInput &oai_untag_resource_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_account_settings_input OAIUpdateAccountSettingsInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateAccountSettings(const QString &x_amz_target, const OAIUpdateAccountSettingsInput &oai_update_account_settings_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_component_input OAIUpdateComponentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateComponent(const QString &x_amz_target, const OAIUpdateComponentInput &oai_update_component_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_environment_input OAIUpdateEnvironmentInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateEnvironment(const QString &x_amz_target, const OAIUpdateEnvironmentInput &oai_update_environment_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_environment_account_connection_input OAIUpdateEnvironmentAccountConnectionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateEnvironmentAccountConnection(const QString &x_amz_target, const OAIUpdateEnvironmentAccountConnectionInput &oai_update_environment_account_connection_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_environment_template_input OAIUpdateEnvironmentTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateEnvironmentTemplate(const QString &x_amz_target, const OAIUpdateEnvironmentTemplateInput &oai_update_environment_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_environment_template_version_input OAIUpdateEnvironmentTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateEnvironmentTemplateVersion(const QString &x_amz_target, const OAIUpdateEnvironmentTemplateVersionInput &oai_update_environment_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_input OAIUpdateServiceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateService(const QString &x_amz_target, const OAIUpdateServiceInput &oai_update_service_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_instance_input OAIUpdateServiceInstanceInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServiceInstance(const QString &x_amz_target, const OAIUpdateServiceInstanceInput &oai_update_service_instance_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_pipeline_input OAIUpdateServicePipelineInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServicePipeline(const QString &x_amz_target, const OAIUpdateServicePipelineInput &oai_update_service_pipeline_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_sync_blocker_input OAIUpdateServiceSyncBlockerInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServiceSyncBlocker(const QString &x_amz_target, const OAIUpdateServiceSyncBlockerInput &oai_update_service_sync_blocker_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_sync_config_input OAIUpdateServiceSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServiceSyncConfig(const QString &x_amz_target, const OAIUpdateServiceSyncConfigInput &oai_update_service_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_template_input OAIUpdateServiceTemplateInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServiceTemplate(const QString &x_amz_target, const OAIUpdateServiceTemplateInput &oai_update_service_template_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_service_template_version_input OAIUpdateServiceTemplateVersionInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateServiceTemplateVersion(const QString &x_amz_target, const OAIUpdateServiceTemplateVersionInput &oai_update_service_template_version_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_amz_target QString [required]
    * @param[in]  oai_update_template_sync_config_input OAIUpdateTemplateSyncConfigInput [required]
    * @param[in]  x_amz_content_sha256 QString [optional]
    * @param[in]  x_amz_date QString [optional]
    * @param[in]  x_amz_algorithm QString [optional]
    * @param[in]  x_amz_credential QString [optional]
    * @param[in]  x_amz_security_token QString [optional]
    * @param[in]  x_amz_signature QString [optional]
    * @param[in]  x_amz_signed_headers QString [optional]
    */
    virtual void updateTemplateSyncConfig(const QString &x_amz_target, const OAIUpdateTemplateSyncConfigInput &oai_update_template_sync_config_input, const ::OpenAPI::OptionalParam<QString> &x_amz_content_sha256 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_algorithm = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_credential = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_security_token = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signature = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_amz_signed_headers = ::OpenAPI::OptionalParam<QString>());


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

    void acceptEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void cancelComponentDeploymentCallback(OAIHttpRequestWorker *worker);
    void cancelEnvironmentDeploymentCallback(OAIHttpRequestWorker *worker);
    void cancelServiceInstanceDeploymentCallback(OAIHttpRequestWorker *worker);
    void cancelServicePipelineDeploymentCallback(OAIHttpRequestWorker *worker);
    void createComponentCallback(OAIHttpRequestWorker *worker);
    void createEnvironmentCallback(OAIHttpRequestWorker *worker);
    void createEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void createEnvironmentTemplateCallback(OAIHttpRequestWorker *worker);
    void createEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void createRepositoryCallback(OAIHttpRequestWorker *worker);
    void createServiceCallback(OAIHttpRequestWorker *worker);
    void createServiceInstanceCallback(OAIHttpRequestWorker *worker);
    void createServiceSyncConfigCallback(OAIHttpRequestWorker *worker);
    void createServiceTemplateCallback(OAIHttpRequestWorker *worker);
    void createServiceTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void createTemplateSyncConfigCallback(OAIHttpRequestWorker *worker);
    void deleteComponentCallback(OAIHttpRequestWorker *worker);
    void deleteDeploymentCallback(OAIHttpRequestWorker *worker);
    void deleteEnvironmentCallback(OAIHttpRequestWorker *worker);
    void deleteEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void deleteEnvironmentTemplateCallback(OAIHttpRequestWorker *worker);
    void deleteEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void deleteRepositoryCallback(OAIHttpRequestWorker *worker);
    void deleteServiceCallback(OAIHttpRequestWorker *worker);
    void deleteServiceSyncConfigCallback(OAIHttpRequestWorker *worker);
    void deleteServiceTemplateCallback(OAIHttpRequestWorker *worker);
    void deleteServiceTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void deleteTemplateSyncConfigCallback(OAIHttpRequestWorker *worker);
    void getAccountSettingsCallback(OAIHttpRequestWorker *worker);
    void getComponentCallback(OAIHttpRequestWorker *worker);
    void getDeploymentCallback(OAIHttpRequestWorker *worker);
    void getEnvironmentCallback(OAIHttpRequestWorker *worker);
    void getEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void getEnvironmentTemplateCallback(OAIHttpRequestWorker *worker);
    void getEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void getRepositoryCallback(OAIHttpRequestWorker *worker);
    void getRepositorySyncStatusCallback(OAIHttpRequestWorker *worker);
    void getResourcesSummaryCallback(OAIHttpRequestWorker *worker);
    void getServiceCallback(OAIHttpRequestWorker *worker);
    void getServiceInstanceCallback(OAIHttpRequestWorker *worker);
    void getServiceInstanceSyncStatusCallback(OAIHttpRequestWorker *worker);
    void getServiceSyncBlockerSummaryCallback(OAIHttpRequestWorker *worker);
    void getServiceSyncConfigCallback(OAIHttpRequestWorker *worker);
    void getServiceTemplateCallback(OAIHttpRequestWorker *worker);
    void getServiceTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void getTemplateSyncConfigCallback(OAIHttpRequestWorker *worker);
    void getTemplateSyncStatusCallback(OAIHttpRequestWorker *worker);
    void listComponentOutputsCallback(OAIHttpRequestWorker *worker);
    void listComponentProvisionedResourcesCallback(OAIHttpRequestWorker *worker);
    void listComponentsCallback(OAIHttpRequestWorker *worker);
    void listDeploymentsCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentAccountConnectionsCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentOutputsCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentProvisionedResourcesCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentTemplateVersionsCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentTemplatesCallback(OAIHttpRequestWorker *worker);
    void listEnvironmentsCallback(OAIHttpRequestWorker *worker);
    void listRepositoriesCallback(OAIHttpRequestWorker *worker);
    void listRepositorySyncDefinitionsCallback(OAIHttpRequestWorker *worker);
    void listServiceInstanceOutputsCallback(OAIHttpRequestWorker *worker);
    void listServiceInstanceProvisionedResourcesCallback(OAIHttpRequestWorker *worker);
    void listServiceInstancesCallback(OAIHttpRequestWorker *worker);
    void listServicePipelineOutputsCallback(OAIHttpRequestWorker *worker);
    void listServicePipelineProvisionedResourcesCallback(OAIHttpRequestWorker *worker);
    void listServiceTemplateVersionsCallback(OAIHttpRequestWorker *worker);
    void listServiceTemplatesCallback(OAIHttpRequestWorker *worker);
    void listServicesCallback(OAIHttpRequestWorker *worker);
    void listTagsForResourceCallback(OAIHttpRequestWorker *worker);
    void notifyResourceDeploymentStatusChangeCallback(OAIHttpRequestWorker *worker);
    void rejectEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void tagResourceCallback(OAIHttpRequestWorker *worker);
    void untagResourceCallback(OAIHttpRequestWorker *worker);
    void updateAccountSettingsCallback(OAIHttpRequestWorker *worker);
    void updateComponentCallback(OAIHttpRequestWorker *worker);
    void updateEnvironmentCallback(OAIHttpRequestWorker *worker);
    void updateEnvironmentAccountConnectionCallback(OAIHttpRequestWorker *worker);
    void updateEnvironmentTemplateCallback(OAIHttpRequestWorker *worker);
    void updateEnvironmentTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void updateServiceCallback(OAIHttpRequestWorker *worker);
    void updateServiceInstanceCallback(OAIHttpRequestWorker *worker);
    void updateServicePipelineCallback(OAIHttpRequestWorker *worker);
    void updateServiceSyncBlockerCallback(OAIHttpRequestWorker *worker);
    void updateServiceSyncConfigCallback(OAIHttpRequestWorker *worker);
    void updateServiceTemplateCallback(OAIHttpRequestWorker *worker);
    void updateServiceTemplateVersionCallback(OAIHttpRequestWorker *worker);
    void updateTemplateSyncConfigCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void acceptEnvironmentAccountConnectionSignal(OAIAcceptEnvironmentAccountConnectionOutput summary);
    void cancelComponentDeploymentSignal(OAICancelComponentDeploymentOutput summary);
    void cancelEnvironmentDeploymentSignal(OAICancelEnvironmentDeploymentOutput summary);
    void cancelServiceInstanceDeploymentSignal(OAICancelServiceInstanceDeploymentOutput summary);
    void cancelServicePipelineDeploymentSignal(OAICancelServicePipelineDeploymentOutput summary);
    void createComponentSignal(OAICreateComponentOutput summary);
    void createEnvironmentSignal(OAICreateEnvironmentOutput summary);
    void createEnvironmentAccountConnectionSignal(OAICreateEnvironmentAccountConnectionOutput summary);
    void createEnvironmentTemplateSignal(OAICreateEnvironmentTemplateOutput summary);
    void createEnvironmentTemplateVersionSignal(OAICreateEnvironmentTemplateVersionOutput summary);
    void createRepositorySignal(OAICreateRepositoryOutput summary);
    void createServiceSignal(OAICreateServiceOutput summary);
    void createServiceInstanceSignal(OAICreateServiceInstanceOutput summary);
    void createServiceSyncConfigSignal(OAICreateServiceSyncConfigOutput summary);
    void createServiceTemplateSignal(OAICreateServiceTemplateOutput summary);
    void createServiceTemplateVersionSignal(OAICreateServiceTemplateVersionOutput summary);
    void createTemplateSyncConfigSignal(OAICreateTemplateSyncConfigOutput summary);
    void deleteComponentSignal(OAIDeleteComponentOutput summary);
    void deleteDeploymentSignal(OAIDeleteDeploymentOutput summary);
    void deleteEnvironmentSignal(OAIDeleteEnvironmentOutput summary);
    void deleteEnvironmentAccountConnectionSignal(OAIDeleteEnvironmentAccountConnectionOutput summary);
    void deleteEnvironmentTemplateSignal(OAIDeleteEnvironmentTemplateOutput summary);
    void deleteEnvironmentTemplateVersionSignal(OAIDeleteEnvironmentTemplateVersionOutput summary);
    void deleteRepositorySignal(OAIDeleteRepositoryOutput summary);
    void deleteServiceSignal(OAIDeleteServiceOutput summary);
    void deleteServiceSyncConfigSignal(OAIDeleteServiceSyncConfigOutput summary);
    void deleteServiceTemplateSignal(OAIDeleteServiceTemplateOutput summary);
    void deleteServiceTemplateVersionSignal(OAIDeleteServiceTemplateVersionOutput summary);
    void deleteTemplateSyncConfigSignal(OAIDeleteTemplateSyncConfigOutput summary);
    void getAccountSettingsSignal(OAIGetAccountSettingsOutput summary);
    void getComponentSignal(OAIGetComponentOutput summary);
    void getDeploymentSignal(OAIGetDeploymentOutput summary);
    void getEnvironmentSignal(OAIGetEnvironmentOutput summary);
    void getEnvironmentAccountConnectionSignal(OAIGetEnvironmentAccountConnectionOutput summary);
    void getEnvironmentTemplateSignal(OAIGetEnvironmentTemplateOutput summary);
    void getEnvironmentTemplateVersionSignal(OAIGetEnvironmentTemplateVersionOutput summary);
    void getRepositorySignal(OAIGetRepositoryOutput summary);
    void getRepositorySyncStatusSignal(OAIGetRepositorySyncStatusOutput summary);
    void getResourcesSummarySignal(OAIGetResourcesSummaryOutput summary);
    void getServiceSignal(OAIGetServiceOutput summary);
    void getServiceInstanceSignal(OAIGetServiceInstanceOutput summary);
    void getServiceInstanceSyncStatusSignal(OAIGetServiceInstanceSyncStatusOutput summary);
    void getServiceSyncBlockerSummarySignal(OAIGetServiceSyncBlockerSummaryOutput summary);
    void getServiceSyncConfigSignal(OAIGetServiceSyncConfigOutput summary);
    void getServiceTemplateSignal(OAIGetServiceTemplateOutput summary);
    void getServiceTemplateVersionSignal(OAIGetServiceTemplateVersionOutput summary);
    void getTemplateSyncConfigSignal(OAIGetTemplateSyncConfigOutput summary);
    void getTemplateSyncStatusSignal(OAIGetTemplateSyncStatusOutput summary);
    void listComponentOutputsSignal(OAIListComponentOutputsOutput summary);
    void listComponentProvisionedResourcesSignal(OAIListComponentProvisionedResourcesOutput summary);
    void listComponentsSignal(OAIListComponentsOutput summary);
    void listDeploymentsSignal(OAIListDeploymentsOutput summary);
    void listEnvironmentAccountConnectionsSignal(OAIListEnvironmentAccountConnectionsOutput summary);
    void listEnvironmentOutputsSignal(OAIListEnvironmentOutputsOutput summary);
    void listEnvironmentProvisionedResourcesSignal(OAIListEnvironmentProvisionedResourcesOutput summary);
    void listEnvironmentTemplateVersionsSignal(OAIListEnvironmentTemplateVersionsOutput summary);
    void listEnvironmentTemplatesSignal(OAIListEnvironmentTemplatesOutput summary);
    void listEnvironmentsSignal(OAIListEnvironmentsOutput summary);
    void listRepositoriesSignal(OAIListRepositoriesOutput summary);
    void listRepositorySyncDefinitionsSignal(OAIListRepositorySyncDefinitionsOutput summary);
    void listServiceInstanceOutputsSignal(OAIListServiceInstanceOutputsOutput summary);
    void listServiceInstanceProvisionedResourcesSignal(OAIListServiceInstanceProvisionedResourcesOutput summary);
    void listServiceInstancesSignal(OAIListServiceInstancesOutput summary);
    void listServicePipelineOutputsSignal(OAIListServicePipelineOutputsOutput summary);
    void listServicePipelineProvisionedResourcesSignal(OAIListServicePipelineProvisionedResourcesOutput summary);
    void listServiceTemplateVersionsSignal(OAIListServiceTemplateVersionsOutput summary);
    void listServiceTemplatesSignal(OAIListServiceTemplatesOutput summary);
    void listServicesSignal(OAIListServicesOutput summary);
    void listTagsForResourceSignal(OAIListTagsForResourceOutput summary);
    void notifyResourceDeploymentStatusChangeSignal(OAIObject summary);
    void rejectEnvironmentAccountConnectionSignal(OAIRejectEnvironmentAccountConnectionOutput summary);
    void tagResourceSignal(OAIObject summary);
    void untagResourceSignal(OAIObject summary);
    void updateAccountSettingsSignal(OAIUpdateAccountSettingsOutput summary);
    void updateComponentSignal(OAIUpdateComponentOutput summary);
    void updateEnvironmentSignal(OAIUpdateEnvironmentOutput summary);
    void updateEnvironmentAccountConnectionSignal(OAIUpdateEnvironmentAccountConnectionOutput summary);
    void updateEnvironmentTemplateSignal(OAIUpdateEnvironmentTemplateOutput summary);
    void updateEnvironmentTemplateVersionSignal(OAIUpdateEnvironmentTemplateVersionOutput summary);
    void updateServiceSignal(OAIUpdateServiceOutput summary);
    void updateServiceInstanceSignal(OAIUpdateServiceInstanceOutput summary);
    void updateServicePipelineSignal(OAIUpdateServicePipelineOutput summary);
    void updateServiceSyncBlockerSignal(OAIUpdateServiceSyncBlockerOutput summary);
    void updateServiceSyncConfigSignal(OAIUpdateServiceSyncConfigOutput summary);
    void updateServiceTemplateSignal(OAIUpdateServiceTemplateOutput summary);
    void updateServiceTemplateVersionSignal(OAIUpdateServiceTemplateVersionOutput summary);
    void updateTemplateSyncConfigSignal(OAIUpdateTemplateSyncConfigOutput summary);


    void acceptEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAIAcceptEnvironmentAccountConnectionOutput summary);
    void cancelComponentDeploymentSignalFull(OAIHttpRequestWorker *worker, OAICancelComponentDeploymentOutput summary);
    void cancelEnvironmentDeploymentSignalFull(OAIHttpRequestWorker *worker, OAICancelEnvironmentDeploymentOutput summary);
    void cancelServiceInstanceDeploymentSignalFull(OAIHttpRequestWorker *worker, OAICancelServiceInstanceDeploymentOutput summary);
    void cancelServicePipelineDeploymentSignalFull(OAIHttpRequestWorker *worker, OAICancelServicePipelineDeploymentOutput summary);
    void createComponentSignalFull(OAIHttpRequestWorker *worker, OAICreateComponentOutput summary);
    void createEnvironmentSignalFull(OAIHttpRequestWorker *worker, OAICreateEnvironmentOutput summary);
    void createEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAICreateEnvironmentAccountConnectionOutput summary);
    void createEnvironmentTemplateSignalFull(OAIHttpRequestWorker *worker, OAICreateEnvironmentTemplateOutput summary);
    void createEnvironmentTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAICreateEnvironmentTemplateVersionOutput summary);
    void createRepositorySignalFull(OAIHttpRequestWorker *worker, OAICreateRepositoryOutput summary);
    void createServiceSignalFull(OAIHttpRequestWorker *worker, OAICreateServiceOutput summary);
    void createServiceInstanceSignalFull(OAIHttpRequestWorker *worker, OAICreateServiceInstanceOutput summary);
    void createServiceSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAICreateServiceSyncConfigOutput summary);
    void createServiceTemplateSignalFull(OAIHttpRequestWorker *worker, OAICreateServiceTemplateOutput summary);
    void createServiceTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAICreateServiceTemplateVersionOutput summary);
    void createTemplateSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAICreateTemplateSyncConfigOutput summary);
    void deleteComponentSignalFull(OAIHttpRequestWorker *worker, OAIDeleteComponentOutput summary);
    void deleteDeploymentSignalFull(OAIHttpRequestWorker *worker, OAIDeleteDeploymentOutput summary);
    void deleteEnvironmentSignalFull(OAIHttpRequestWorker *worker, OAIDeleteEnvironmentOutput summary);
    void deleteEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAIDeleteEnvironmentAccountConnectionOutput summary);
    void deleteEnvironmentTemplateSignalFull(OAIHttpRequestWorker *worker, OAIDeleteEnvironmentTemplateOutput summary);
    void deleteEnvironmentTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIDeleteEnvironmentTemplateVersionOutput summary);
    void deleteRepositorySignalFull(OAIHttpRequestWorker *worker, OAIDeleteRepositoryOutput summary);
    void deleteServiceSignalFull(OAIHttpRequestWorker *worker, OAIDeleteServiceOutput summary);
    void deleteServiceSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIDeleteServiceSyncConfigOutput summary);
    void deleteServiceTemplateSignalFull(OAIHttpRequestWorker *worker, OAIDeleteServiceTemplateOutput summary);
    void deleteServiceTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIDeleteServiceTemplateVersionOutput summary);
    void deleteTemplateSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIDeleteTemplateSyncConfigOutput summary);
    void getAccountSettingsSignalFull(OAIHttpRequestWorker *worker, OAIGetAccountSettingsOutput summary);
    void getComponentSignalFull(OAIHttpRequestWorker *worker, OAIGetComponentOutput summary);
    void getDeploymentSignalFull(OAIHttpRequestWorker *worker, OAIGetDeploymentOutput summary);
    void getEnvironmentSignalFull(OAIHttpRequestWorker *worker, OAIGetEnvironmentOutput summary);
    void getEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAIGetEnvironmentAccountConnectionOutput summary);
    void getEnvironmentTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetEnvironmentTemplateOutput summary);
    void getEnvironmentTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIGetEnvironmentTemplateVersionOutput summary);
    void getRepositorySignalFull(OAIHttpRequestWorker *worker, OAIGetRepositoryOutput summary);
    void getRepositorySyncStatusSignalFull(OAIHttpRequestWorker *worker, OAIGetRepositorySyncStatusOutput summary);
    void getResourcesSummarySignalFull(OAIHttpRequestWorker *worker, OAIGetResourcesSummaryOutput summary);
    void getServiceSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceOutput summary);
    void getServiceInstanceSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceInstanceOutput summary);
    void getServiceInstanceSyncStatusSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceInstanceSyncStatusOutput summary);
    void getServiceSyncBlockerSummarySignalFull(OAIHttpRequestWorker *worker, OAIGetServiceSyncBlockerSummaryOutput summary);
    void getServiceSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceSyncConfigOutput summary);
    void getServiceTemplateSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceTemplateOutput summary);
    void getServiceTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIGetServiceTemplateVersionOutput summary);
    void getTemplateSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIGetTemplateSyncConfigOutput summary);
    void getTemplateSyncStatusSignalFull(OAIHttpRequestWorker *worker, OAIGetTemplateSyncStatusOutput summary);
    void listComponentOutputsSignalFull(OAIHttpRequestWorker *worker, OAIListComponentOutputsOutput summary);
    void listComponentProvisionedResourcesSignalFull(OAIHttpRequestWorker *worker, OAIListComponentProvisionedResourcesOutput summary);
    void listComponentsSignalFull(OAIHttpRequestWorker *worker, OAIListComponentsOutput summary);
    void listDeploymentsSignalFull(OAIHttpRequestWorker *worker, OAIListDeploymentsOutput summary);
    void listEnvironmentAccountConnectionsSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentAccountConnectionsOutput summary);
    void listEnvironmentOutputsSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentOutputsOutput summary);
    void listEnvironmentProvisionedResourcesSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentProvisionedResourcesOutput summary);
    void listEnvironmentTemplateVersionsSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentTemplateVersionsOutput summary);
    void listEnvironmentTemplatesSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentTemplatesOutput summary);
    void listEnvironmentsSignalFull(OAIHttpRequestWorker *worker, OAIListEnvironmentsOutput summary);
    void listRepositoriesSignalFull(OAIHttpRequestWorker *worker, OAIListRepositoriesOutput summary);
    void listRepositorySyncDefinitionsSignalFull(OAIHttpRequestWorker *worker, OAIListRepositorySyncDefinitionsOutput summary);
    void listServiceInstanceOutputsSignalFull(OAIHttpRequestWorker *worker, OAIListServiceInstanceOutputsOutput summary);
    void listServiceInstanceProvisionedResourcesSignalFull(OAIHttpRequestWorker *worker, OAIListServiceInstanceProvisionedResourcesOutput summary);
    void listServiceInstancesSignalFull(OAIHttpRequestWorker *worker, OAIListServiceInstancesOutput summary);
    void listServicePipelineOutputsSignalFull(OAIHttpRequestWorker *worker, OAIListServicePipelineOutputsOutput summary);
    void listServicePipelineProvisionedResourcesSignalFull(OAIHttpRequestWorker *worker, OAIListServicePipelineProvisionedResourcesOutput summary);
    void listServiceTemplateVersionsSignalFull(OAIHttpRequestWorker *worker, OAIListServiceTemplateVersionsOutput summary);
    void listServiceTemplatesSignalFull(OAIHttpRequestWorker *worker, OAIListServiceTemplatesOutput summary);
    void listServicesSignalFull(OAIHttpRequestWorker *worker, OAIListServicesOutput summary);
    void listTagsForResourceSignalFull(OAIHttpRequestWorker *worker, OAIListTagsForResourceOutput summary);
    void notifyResourceDeploymentStatusChangeSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void rejectEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAIRejectEnvironmentAccountConnectionOutput summary);
    void tagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void untagResourceSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateAccountSettingsSignalFull(OAIHttpRequestWorker *worker, OAIUpdateAccountSettingsOutput summary);
    void updateComponentSignalFull(OAIHttpRequestWorker *worker, OAIUpdateComponentOutput summary);
    void updateEnvironmentSignalFull(OAIHttpRequestWorker *worker, OAIUpdateEnvironmentOutput summary);
    void updateEnvironmentAccountConnectionSignalFull(OAIHttpRequestWorker *worker, OAIUpdateEnvironmentAccountConnectionOutput summary);
    void updateEnvironmentTemplateSignalFull(OAIHttpRequestWorker *worker, OAIUpdateEnvironmentTemplateOutput summary);
    void updateEnvironmentTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIUpdateEnvironmentTemplateVersionOutput summary);
    void updateServiceSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceOutput summary);
    void updateServiceInstanceSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceInstanceOutput summary);
    void updateServicePipelineSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServicePipelineOutput summary);
    void updateServiceSyncBlockerSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceSyncBlockerOutput summary);
    void updateServiceSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceSyncConfigOutput summary);
    void updateServiceTemplateSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceTemplateOutput summary);
    void updateServiceTemplateVersionSignalFull(OAIHttpRequestWorker *worker, OAIUpdateServiceTemplateVersionOutput summary);
    void updateTemplateSyncConfigSignalFull(OAIHttpRequestWorker *worker, OAIUpdateTemplateSyncConfigOutput summary);

    Q_DECL_DEPRECATED_X("Use acceptEnvironmentAccountConnectionSignalError() instead")
    void acceptEnvironmentAccountConnectionSignalE(OAIAcceptEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptEnvironmentAccountConnectionSignalError(OAIAcceptEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelComponentDeploymentSignalError() instead")
    void cancelComponentDeploymentSignalE(OAICancelComponentDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelComponentDeploymentSignalError(OAICancelComponentDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelEnvironmentDeploymentSignalError() instead")
    void cancelEnvironmentDeploymentSignalE(OAICancelEnvironmentDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelEnvironmentDeploymentSignalError(OAICancelEnvironmentDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelServiceInstanceDeploymentSignalError() instead")
    void cancelServiceInstanceDeploymentSignalE(OAICancelServiceInstanceDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelServiceInstanceDeploymentSignalError(OAICancelServiceInstanceDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelServicePipelineDeploymentSignalError() instead")
    void cancelServicePipelineDeploymentSignalE(OAICancelServicePipelineDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelServicePipelineDeploymentSignalError(OAICancelServicePipelineDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createComponentSignalError() instead")
    void createComponentSignalE(OAICreateComponentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createComponentSignalError(OAICreateComponentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentSignalError() instead")
    void createEnvironmentSignalE(OAICreateEnvironmentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentSignalError(OAICreateEnvironmentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentAccountConnectionSignalError() instead")
    void createEnvironmentAccountConnectionSignalE(OAICreateEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentAccountConnectionSignalError(OAICreateEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentTemplateSignalError() instead")
    void createEnvironmentTemplateSignalE(OAICreateEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentTemplateSignalError(OAICreateEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentTemplateVersionSignalError() instead")
    void createEnvironmentTemplateVersionSignalE(OAICreateEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentTemplateVersionSignalError(OAICreateEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalError() instead")
    void createRepositorySignalE(OAICreateRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalError(OAICreateRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceSignalError() instead")
    void createServiceSignalE(OAICreateServiceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceSignalError(OAICreateServiceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceInstanceSignalError() instead")
    void createServiceInstanceSignalE(OAICreateServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceInstanceSignalError(OAICreateServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceSyncConfigSignalError() instead")
    void createServiceSyncConfigSignalE(OAICreateServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceSyncConfigSignalError(OAICreateServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTemplateSignalError() instead")
    void createServiceTemplateSignalE(OAICreateServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTemplateSignalError(OAICreateServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTemplateVersionSignalError() instead")
    void createServiceTemplateVersionSignalE(OAICreateServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTemplateVersionSignalError(OAICreateServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createTemplateSyncConfigSignalError() instead")
    void createTemplateSyncConfigSignalE(OAICreateTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void createTemplateSyncConfigSignalError(OAICreateTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteComponentSignalError() instead")
    void deleteComponentSignalE(OAIDeleteComponentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteComponentSignalError(OAIDeleteComponentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDeploymentSignalError() instead")
    void deleteDeploymentSignalE(OAIDeleteDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDeploymentSignalError(OAIDeleteDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentSignalError() instead")
    void deleteEnvironmentSignalE(OAIDeleteEnvironmentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentSignalError(OAIDeleteEnvironmentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentAccountConnectionSignalError() instead")
    void deleteEnvironmentAccountConnectionSignalE(OAIDeleteEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentAccountConnectionSignalError(OAIDeleteEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentTemplateSignalError() instead")
    void deleteEnvironmentTemplateSignalE(OAIDeleteEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentTemplateSignalError(OAIDeleteEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentTemplateVersionSignalError() instead")
    void deleteEnvironmentTemplateVersionSignalE(OAIDeleteEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentTemplateVersionSignalError(OAIDeleteEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalError() instead")
    void deleteRepositorySignalE(OAIDeleteRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalError(OAIDeleteRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceSignalError() instead")
    void deleteServiceSignalE(OAIDeleteServiceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSignalError(OAIDeleteServiceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceSyncConfigSignalError() instead")
    void deleteServiceSyncConfigSignalE(OAIDeleteServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSyncConfigSignalError(OAIDeleteServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTemplateSignalError() instead")
    void deleteServiceTemplateSignalE(OAIDeleteServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTemplateSignalError(OAIDeleteServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTemplateVersionSignalError() instead")
    void deleteServiceTemplateVersionSignalE(OAIDeleteServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTemplateVersionSignalError(OAIDeleteServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTemplateSyncConfigSignalError() instead")
    void deleteTemplateSyncConfigSignalE(OAIDeleteTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTemplateSyncConfigSignalError(OAIDeleteTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSettingsSignalError() instead")
    void getAccountSettingsSignalE(OAIGetAccountSettingsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSettingsSignalError(OAIGetAccountSettingsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getComponentSignalError() instead")
    void getComponentSignalE(OAIGetComponentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getComponentSignalError(OAIGetComponentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeploymentSignalError() instead")
    void getDeploymentSignalE(OAIGetDeploymentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeploymentSignalError(OAIGetDeploymentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentSignalError() instead")
    void getEnvironmentSignalE(OAIGetEnvironmentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentSignalError(OAIGetEnvironmentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentAccountConnectionSignalError() instead")
    void getEnvironmentAccountConnectionSignalE(OAIGetEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentAccountConnectionSignalError(OAIGetEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentTemplateSignalError() instead")
    void getEnvironmentTemplateSignalE(OAIGetEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentTemplateSignalError(OAIGetEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentTemplateVersionSignalError() instead")
    void getEnvironmentTemplateVersionSignalE(OAIGetEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentTemplateVersionSignalError(OAIGetEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySignalError() instead")
    void getRepositorySignalE(OAIGetRepositoryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySignalError(OAIGetRepositoryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySyncStatusSignalError() instead")
    void getRepositorySyncStatusSignalE(OAIGetRepositorySyncStatusOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySyncStatusSignalError(OAIGetRepositorySyncStatusOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getResourcesSummarySignalError() instead")
    void getResourcesSummarySignalE(OAIGetResourcesSummaryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getResourcesSummarySignalError(OAIGetResourcesSummaryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSignalError() instead")
    void getServiceSignalE(OAIGetServiceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSignalError(OAIGetServiceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceInstanceSignalError() instead")
    void getServiceInstanceSignalE(OAIGetServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceInstanceSignalError(OAIGetServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceInstanceSyncStatusSignalError() instead")
    void getServiceInstanceSyncStatusSignalE(OAIGetServiceInstanceSyncStatusOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceInstanceSyncStatusSignalError(OAIGetServiceInstanceSyncStatusOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSyncBlockerSummarySignalError() instead")
    void getServiceSyncBlockerSummarySignalE(OAIGetServiceSyncBlockerSummaryOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSyncBlockerSummarySignalError(OAIGetServiceSyncBlockerSummaryOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSyncConfigSignalError() instead")
    void getServiceSyncConfigSignalE(OAIGetServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSyncConfigSignalError(OAIGetServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTemplateSignalError() instead")
    void getServiceTemplateSignalE(OAIGetServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTemplateSignalError(OAIGetServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTemplateVersionSignalError() instead")
    void getServiceTemplateVersionSignalE(OAIGetServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTemplateVersionSignalError(OAIGetServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTemplateSyncConfigSignalError() instead")
    void getTemplateSyncConfigSignalE(OAIGetTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTemplateSyncConfigSignalError(OAIGetTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTemplateSyncStatusSignalError() instead")
    void getTemplateSyncStatusSignalE(OAIGetTemplateSyncStatusOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTemplateSyncStatusSignalError(OAIGetTemplateSyncStatusOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentOutputsSignalError() instead")
    void listComponentOutputsSignalE(OAIListComponentOutputsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentOutputsSignalError(OAIListComponentOutputsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentProvisionedResourcesSignalError() instead")
    void listComponentProvisionedResourcesSignalE(OAIListComponentProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentProvisionedResourcesSignalError(OAIListComponentProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentsSignalError() instead")
    void listComponentsSignalE(OAIListComponentsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentsSignalError(OAIListComponentsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDeploymentsSignalError() instead")
    void listDeploymentsSignalE(OAIListDeploymentsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listDeploymentsSignalError(OAIListDeploymentsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentAccountConnectionsSignalError() instead")
    void listEnvironmentAccountConnectionsSignalE(OAIListEnvironmentAccountConnectionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentAccountConnectionsSignalError(OAIListEnvironmentAccountConnectionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentOutputsSignalError() instead")
    void listEnvironmentOutputsSignalE(OAIListEnvironmentOutputsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentOutputsSignalError(OAIListEnvironmentOutputsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentProvisionedResourcesSignalError() instead")
    void listEnvironmentProvisionedResourcesSignalE(OAIListEnvironmentProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentProvisionedResourcesSignalError(OAIListEnvironmentProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentTemplateVersionsSignalError() instead")
    void listEnvironmentTemplateVersionsSignalE(OAIListEnvironmentTemplateVersionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentTemplateVersionsSignalError(OAIListEnvironmentTemplateVersionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentTemplatesSignalError() instead")
    void listEnvironmentTemplatesSignalE(OAIListEnvironmentTemplatesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentTemplatesSignalError(OAIListEnvironmentTemplatesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentsSignalError() instead")
    void listEnvironmentsSignalE(OAIListEnvironmentsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentsSignalError(OAIListEnvironmentsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalError() instead")
    void listRepositoriesSignalE(OAIListRepositoriesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalError(OAIListRepositoriesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositorySyncDefinitionsSignalError() instead")
    void listRepositorySyncDefinitionsSignalE(OAIListRepositorySyncDefinitionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositorySyncDefinitionsSignalError(OAIListRepositorySyncDefinitionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstanceOutputsSignalError() instead")
    void listServiceInstanceOutputsSignalE(OAIListServiceInstanceOutputsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstanceOutputsSignalError(OAIListServiceInstanceOutputsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstanceProvisionedResourcesSignalError() instead")
    void listServiceInstanceProvisionedResourcesSignalE(OAIListServiceInstanceProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstanceProvisionedResourcesSignalError(OAIListServiceInstanceProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstancesSignalError() instead")
    void listServiceInstancesSignalE(OAIListServiceInstancesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstancesSignalError(OAIListServiceInstancesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicePipelineOutputsSignalError() instead")
    void listServicePipelineOutputsSignalE(OAIListServicePipelineOutputsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicePipelineOutputsSignalError(OAIListServicePipelineOutputsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicePipelineProvisionedResourcesSignalError() instead")
    void listServicePipelineProvisionedResourcesSignalE(OAIListServicePipelineProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicePipelineProvisionedResourcesSignalError(OAIListServicePipelineProvisionedResourcesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceTemplateVersionsSignalError() instead")
    void listServiceTemplateVersionsSignalE(OAIListServiceTemplateVersionsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceTemplateVersionsSignalError(OAIListServiceTemplateVersionsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceTemplatesSignalError() instead")
    void listServiceTemplatesSignalE(OAIListServiceTemplatesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceTemplatesSignalError(OAIListServiceTemplatesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicesSignalError() instead")
    void listServicesSignalE(OAIListServicesOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicesSignalError(OAIListServicesOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalError() instead")
    void listTagsForResourceSignalE(OAIListTagsForResourceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalError(OAIListTagsForResourceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use notifyResourceDeploymentStatusChangeSignalError() instead")
    void notifyResourceDeploymentStatusChangeSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void notifyResourceDeploymentStatusChangeSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rejectEnvironmentAccountConnectionSignalError() instead")
    void rejectEnvironmentAccountConnectionSignalE(OAIRejectEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rejectEnvironmentAccountConnectionSignalError(OAIRejectEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalError() instead")
    void tagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalError() instead")
    void untagResourceSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSettingsSignalError() instead")
    void updateAccountSettingsSignalE(OAIUpdateAccountSettingsOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSettingsSignalError(OAIUpdateAccountSettingsOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateComponentSignalError() instead")
    void updateComponentSignalE(OAIUpdateComponentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateComponentSignalError(OAIUpdateComponentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentSignalError() instead")
    void updateEnvironmentSignalE(OAIUpdateEnvironmentOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentSignalError(OAIUpdateEnvironmentOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentAccountConnectionSignalError() instead")
    void updateEnvironmentAccountConnectionSignalE(OAIUpdateEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentAccountConnectionSignalError(OAIUpdateEnvironmentAccountConnectionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentTemplateSignalError() instead")
    void updateEnvironmentTemplateSignalE(OAIUpdateEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentTemplateSignalError(OAIUpdateEnvironmentTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentTemplateVersionSignalError() instead")
    void updateEnvironmentTemplateVersionSignalE(OAIUpdateEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentTemplateVersionSignalError(OAIUpdateEnvironmentTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSignalError() instead")
    void updateServiceSignalE(OAIUpdateServiceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSignalError(OAIUpdateServiceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceInstanceSignalError() instead")
    void updateServiceInstanceSignalE(OAIUpdateServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceInstanceSignalError(OAIUpdateServiceInstanceOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServicePipelineSignalError() instead")
    void updateServicePipelineSignalE(OAIUpdateServicePipelineOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServicePipelineSignalError(OAIUpdateServicePipelineOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSyncBlockerSignalError() instead")
    void updateServiceSyncBlockerSignalE(OAIUpdateServiceSyncBlockerOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSyncBlockerSignalError(OAIUpdateServiceSyncBlockerOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSyncConfigSignalError() instead")
    void updateServiceSyncConfigSignalE(OAIUpdateServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSyncConfigSignalError(OAIUpdateServiceSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceTemplateSignalError() instead")
    void updateServiceTemplateSignalE(OAIUpdateServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceTemplateSignalError(OAIUpdateServiceTemplateOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceTemplateVersionSignalError() instead")
    void updateServiceTemplateVersionSignalE(OAIUpdateServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceTemplateVersionSignalError(OAIUpdateServiceTemplateVersionOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateTemplateSyncConfigSignalError() instead")
    void updateTemplateSyncConfigSignalE(OAIUpdateTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateTemplateSyncConfigSignalError(OAIUpdateTemplateSyncConfigOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use acceptEnvironmentAccountConnectionSignalErrorFull() instead")
    void acceptEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void acceptEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelComponentDeploymentSignalErrorFull() instead")
    void cancelComponentDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelComponentDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelEnvironmentDeploymentSignalErrorFull() instead")
    void cancelEnvironmentDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelEnvironmentDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelServiceInstanceDeploymentSignalErrorFull() instead")
    void cancelServiceInstanceDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelServiceInstanceDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cancelServicePipelineDeploymentSignalErrorFull() instead")
    void cancelServicePipelineDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cancelServicePipelineDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createComponentSignalErrorFull() instead")
    void createComponentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createComponentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentSignalErrorFull() instead")
    void createEnvironmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentAccountConnectionSignalErrorFull() instead")
    void createEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentTemplateSignalErrorFull() instead")
    void createEnvironmentTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createEnvironmentTemplateVersionSignalErrorFull() instead")
    void createEnvironmentTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createEnvironmentTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createRepositorySignalErrorFull() instead")
    void createRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceSignalErrorFull() instead")
    void createServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceInstanceSignalErrorFull() instead")
    void createServiceInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceSyncConfigSignalErrorFull() instead")
    void createServiceSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTemplateSignalErrorFull() instead")
    void createServiceTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createServiceTemplateVersionSignalErrorFull() instead")
    void createServiceTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createServiceTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createTemplateSyncConfigSignalErrorFull() instead")
    void createTemplateSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createTemplateSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteComponentSignalErrorFull() instead")
    void deleteComponentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteComponentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteDeploymentSignalErrorFull() instead")
    void deleteDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentSignalErrorFull() instead")
    void deleteEnvironmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentAccountConnectionSignalErrorFull() instead")
    void deleteEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentTemplateSignalErrorFull() instead")
    void deleteEnvironmentTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteEnvironmentTemplateVersionSignalErrorFull() instead")
    void deleteEnvironmentTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteEnvironmentTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteRepositorySignalErrorFull() instead")
    void deleteRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceSignalErrorFull() instead")
    void deleteServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceSyncConfigSignalErrorFull() instead")
    void deleteServiceSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTemplateSignalErrorFull() instead")
    void deleteServiceTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteServiceTemplateVersionSignalErrorFull() instead")
    void deleteServiceTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteServiceTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use deleteTemplateSyncConfigSignalErrorFull() instead")
    void deleteTemplateSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void deleteTemplateSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAccountSettingsSignalErrorFull() instead")
    void getAccountSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAccountSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getComponentSignalErrorFull() instead")
    void getComponentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getComponentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getDeploymentSignalErrorFull() instead")
    void getDeploymentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeploymentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentSignalErrorFull() instead")
    void getEnvironmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentAccountConnectionSignalErrorFull() instead")
    void getEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentTemplateSignalErrorFull() instead")
    void getEnvironmentTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getEnvironmentTemplateVersionSignalErrorFull() instead")
    void getEnvironmentTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEnvironmentTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySignalErrorFull() instead")
    void getRepositorySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getRepositorySyncStatusSignalErrorFull() instead")
    void getRepositorySyncStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getRepositorySyncStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getResourcesSummarySignalErrorFull() instead")
    void getResourcesSummarySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getResourcesSummarySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSignalErrorFull() instead")
    void getServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceInstanceSignalErrorFull() instead")
    void getServiceInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceInstanceSyncStatusSignalErrorFull() instead")
    void getServiceInstanceSyncStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceInstanceSyncStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSyncBlockerSummarySignalErrorFull() instead")
    void getServiceSyncBlockerSummarySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSyncBlockerSummarySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceSyncConfigSignalErrorFull() instead")
    void getServiceSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTemplateSignalErrorFull() instead")
    void getServiceTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getServiceTemplateVersionSignalErrorFull() instead")
    void getServiceTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getServiceTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTemplateSyncConfigSignalErrorFull() instead")
    void getTemplateSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTemplateSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTemplateSyncStatusSignalErrorFull() instead")
    void getTemplateSyncStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTemplateSyncStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentOutputsSignalErrorFull() instead")
    void listComponentOutputsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentOutputsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentProvisionedResourcesSignalErrorFull() instead")
    void listComponentProvisionedResourcesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentProvisionedResourcesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listComponentsSignalErrorFull() instead")
    void listComponentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listComponentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listDeploymentsSignalErrorFull() instead")
    void listDeploymentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listDeploymentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentAccountConnectionsSignalErrorFull() instead")
    void listEnvironmentAccountConnectionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentAccountConnectionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentOutputsSignalErrorFull() instead")
    void listEnvironmentOutputsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentOutputsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentProvisionedResourcesSignalErrorFull() instead")
    void listEnvironmentProvisionedResourcesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentProvisionedResourcesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentTemplateVersionsSignalErrorFull() instead")
    void listEnvironmentTemplateVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentTemplateVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentTemplatesSignalErrorFull() instead")
    void listEnvironmentTemplatesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentTemplatesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listEnvironmentsSignalErrorFull() instead")
    void listEnvironmentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listEnvironmentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositoriesSignalErrorFull() instead")
    void listRepositoriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositoriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listRepositorySyncDefinitionsSignalErrorFull() instead")
    void listRepositorySyncDefinitionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listRepositorySyncDefinitionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstanceOutputsSignalErrorFull() instead")
    void listServiceInstanceOutputsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstanceOutputsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstanceProvisionedResourcesSignalErrorFull() instead")
    void listServiceInstanceProvisionedResourcesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstanceProvisionedResourcesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceInstancesSignalErrorFull() instead")
    void listServiceInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicePipelineOutputsSignalErrorFull() instead")
    void listServicePipelineOutputsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicePipelineOutputsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicePipelineProvisionedResourcesSignalErrorFull() instead")
    void listServicePipelineProvisionedResourcesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicePipelineProvisionedResourcesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceTemplateVersionsSignalErrorFull() instead")
    void listServiceTemplateVersionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceTemplateVersionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServiceTemplatesSignalErrorFull() instead")
    void listServiceTemplatesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServiceTemplatesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listServicesSignalErrorFull() instead")
    void listServicesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listServicesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use listTagsForResourceSignalErrorFull() instead")
    void listTagsForResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void listTagsForResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use notifyResourceDeploymentStatusChangeSignalErrorFull() instead")
    void notifyResourceDeploymentStatusChangeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void notifyResourceDeploymentStatusChangeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rejectEnvironmentAccountConnectionSignalErrorFull() instead")
    void rejectEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rejectEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tagResourceSignalErrorFull() instead")
    void tagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use untagResourceSignalErrorFull() instead")
    void untagResourceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void untagResourceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateAccountSettingsSignalErrorFull() instead")
    void updateAccountSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateAccountSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateComponentSignalErrorFull() instead")
    void updateComponentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateComponentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentSignalErrorFull() instead")
    void updateEnvironmentSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentAccountConnectionSignalErrorFull() instead")
    void updateEnvironmentAccountConnectionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentAccountConnectionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentTemplateSignalErrorFull() instead")
    void updateEnvironmentTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateEnvironmentTemplateVersionSignalErrorFull() instead")
    void updateEnvironmentTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateEnvironmentTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSignalErrorFull() instead")
    void updateServiceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceInstanceSignalErrorFull() instead")
    void updateServiceInstanceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceInstanceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServicePipelineSignalErrorFull() instead")
    void updateServicePipelineSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServicePipelineSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSyncBlockerSignalErrorFull() instead")
    void updateServiceSyncBlockerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSyncBlockerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceSyncConfigSignalErrorFull() instead")
    void updateServiceSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceTemplateSignalErrorFull() instead")
    void updateServiceTemplateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceTemplateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateServiceTemplateVersionSignalErrorFull() instead")
    void updateServiceTemplateVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateServiceTemplateVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateTemplateSyncConfigSignalErrorFull() instead")
    void updateTemplateSyncConfigSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateTemplateSyncConfigSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
