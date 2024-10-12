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
 * OAIComponent.h
 *
 * &lt;p&gt;Detailed data of an Proton component resource.&lt;/p&gt; &lt;p&gt;For more information about components, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html\&quot;&gt;Proton components&lt;/a&gt; in the &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
 */

#ifndef OAIComponent_H
#define OAIComponent_H

#include <QJsonObject>

#include "OAIDeploymentStatus.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIComponent : public OAIObject {
public:
    OAIComponent();
    OAIComponent(QString json);
    ~OAIComponent() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArn() const;
    void setArn(const QString &arn);
    bool is_arn_Set() const;
    bool is_arn_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAIDeploymentStatus getDeploymentStatus() const;
    void setDeploymentStatus(const OAIDeploymentStatus &deployment_status);
    bool is_deployment_status_Set() const;
    bool is_deployment_status_Valid() const;

    QString getDeploymentStatusMessage() const;
    void setDeploymentStatusMessage(const QString &deployment_status_message);
    bool is_deployment_status_message_Set() const;
    bool is_deployment_status_message_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getEnvironmentName() const;
    void setEnvironmentName(const QString &environment_name);
    bool is_environment_name_Set() const;
    bool is_environment_name_Valid() const;

    QString getLastAttemptedDeploymentId() const;
    void setLastAttemptedDeploymentId(const QString &last_attempted_deployment_id);
    bool is_last_attempted_deployment_id_Set() const;
    bool is_last_attempted_deployment_id_Valid() const;

    QString getLastClientRequestToken() const;
    void setLastClientRequestToken(const QString &last_client_request_token);
    bool is_last_client_request_token_Set() const;
    bool is_last_client_request_token_Valid() const;

    QDateTime getLastDeploymentAttemptedAt() const;
    void setLastDeploymentAttemptedAt(const QDateTime &last_deployment_attempted_at);
    bool is_last_deployment_attempted_at_Set() const;
    bool is_last_deployment_attempted_at_Valid() const;

    QDateTime getLastDeploymentSucceededAt() const;
    void setLastDeploymentSucceededAt(const QDateTime &last_deployment_succeeded_at);
    bool is_last_deployment_succeeded_at_Set() const;
    bool is_last_deployment_succeeded_at_Valid() const;

    QDateTime getLastModifiedAt() const;
    void setLastModifiedAt(const QDateTime &last_modified_at);
    bool is_last_modified_at_Set() const;
    bool is_last_modified_at_Valid() const;

    QString getLastSucceededDeploymentId() const;
    void setLastSucceededDeploymentId(const QString &last_succeeded_deployment_id);
    bool is_last_succeeded_deployment_id_Set() const;
    bool is_last_succeeded_deployment_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getServiceInstanceName() const;
    void setServiceInstanceName(const QString &service_instance_name);
    bool is_service_instance_name_Set() const;
    bool is_service_instance_name_Valid() const;

    QString getServiceName() const;
    void setServiceName(const QString &service_name);
    bool is_service_name_Set() const;
    bool is_service_name_Valid() const;

    QString getServiceSpec() const;
    void setServiceSpec(const QString &service_spec);
    bool is_service_spec_Set() const;
    bool is_service_spec_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_arn;
    bool m_arn_isSet;
    bool m_arn_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAIDeploymentStatus m_deployment_status;
    bool m_deployment_status_isSet;
    bool m_deployment_status_isValid;

    QString m_deployment_status_message;
    bool m_deployment_status_message_isSet;
    bool m_deployment_status_message_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_environment_name;
    bool m_environment_name_isSet;
    bool m_environment_name_isValid;

    QString m_last_attempted_deployment_id;
    bool m_last_attempted_deployment_id_isSet;
    bool m_last_attempted_deployment_id_isValid;

    QString m_last_client_request_token;
    bool m_last_client_request_token_isSet;
    bool m_last_client_request_token_isValid;

    QDateTime m_last_deployment_attempted_at;
    bool m_last_deployment_attempted_at_isSet;
    bool m_last_deployment_attempted_at_isValid;

    QDateTime m_last_deployment_succeeded_at;
    bool m_last_deployment_succeeded_at_isSet;
    bool m_last_deployment_succeeded_at_isValid;

    QDateTime m_last_modified_at;
    bool m_last_modified_at_isSet;
    bool m_last_modified_at_isValid;

    QString m_last_succeeded_deployment_id;
    bool m_last_succeeded_deployment_id_isSet;
    bool m_last_succeeded_deployment_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_service_instance_name;
    bool m_service_instance_name_isSet;
    bool m_service_instance_name_isValid;

    QString m_service_name;
    bool m_service_name_isSet;
    bool m_service_name_isValid;

    QString m_service_spec;
    bool m_service_spec_isSet;
    bool m_service_spec_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIComponent)

#endif // OAIComponent_H
