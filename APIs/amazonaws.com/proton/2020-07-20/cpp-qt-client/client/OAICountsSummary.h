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

/*
 * OAICountsSummary.h
 *
 * Summary counts of each Proton resource type.
 */

#ifndef OAICountsSummary_H
#define OAICountsSummary_H

#include <QJsonObject>

#include "OAICountsSummary_components.h"
#include "OAICountsSummary_environmentTemplates.h"
#include "OAICountsSummary_environments.h"
#include "OAICountsSummary_pipelines.h"
#include "OAICountsSummary_serviceInstances.h"
#include "OAICountsSummary_serviceTemplates.h"
#include "OAICountsSummary_services.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICountsSummary_components;
class OAICountsSummary_environmentTemplates;
class OAICountsSummary_environments;
class OAICountsSummary_pipelines;
class OAICountsSummary_serviceInstances;
class OAICountsSummary_serviceTemplates;
class OAICountsSummary_services;

class OAICountsSummary : public OAIObject {
public:
    OAICountsSummary();
    OAICountsSummary(QString json);
    ~OAICountsSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICountsSummary_components getComponents() const;
    void setComponents(const OAICountsSummary_components &components);
    bool is_components_Set() const;
    bool is_components_Valid() const;

    OAICountsSummary_environmentTemplates getEnvironmentTemplates() const;
    void setEnvironmentTemplates(const OAICountsSummary_environmentTemplates &environment_templates);
    bool is_environment_templates_Set() const;
    bool is_environment_templates_Valid() const;

    OAICountsSummary_environments getEnvironments() const;
    void setEnvironments(const OAICountsSummary_environments &environments);
    bool is_environments_Set() const;
    bool is_environments_Valid() const;

    OAICountsSummary_pipelines getPipelines() const;
    void setPipelines(const OAICountsSummary_pipelines &pipelines);
    bool is_pipelines_Set() const;
    bool is_pipelines_Valid() const;

    OAICountsSummary_serviceInstances getServiceInstances() const;
    void setServiceInstances(const OAICountsSummary_serviceInstances &service_instances);
    bool is_service_instances_Set() const;
    bool is_service_instances_Valid() const;

    OAICountsSummary_serviceTemplates getServiceTemplates() const;
    void setServiceTemplates(const OAICountsSummary_serviceTemplates &service_templates);
    bool is_service_templates_Set() const;
    bool is_service_templates_Valid() const;

    OAICountsSummary_services getServices() const;
    void setServices(const OAICountsSummary_services &services);
    bool is_services_Set() const;
    bool is_services_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICountsSummary_components m_components;
    bool m_components_isSet;
    bool m_components_isValid;

    OAICountsSummary_environmentTemplates m_environment_templates;
    bool m_environment_templates_isSet;
    bool m_environment_templates_isValid;

    OAICountsSummary_environments m_environments;
    bool m_environments_isSet;
    bool m_environments_isValid;

    OAICountsSummary_pipelines m_pipelines;
    bool m_pipelines_isSet;
    bool m_pipelines_isValid;

    OAICountsSummary_serviceInstances m_service_instances;
    bool m_service_instances_isSet;
    bool m_service_instances_isValid;

    OAICountsSummary_serviceTemplates m_service_templates;
    bool m_service_templates_isSet;
    bool m_service_templates_isValid;

    OAICountsSummary_services m_services;
    bool m_services_isSet;
    bool m_services_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICountsSummary)

#endif // OAICountsSummary_H
