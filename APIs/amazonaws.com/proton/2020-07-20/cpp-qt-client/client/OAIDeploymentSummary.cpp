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

#include "OAIDeploymentSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeploymentSummary::OAIDeploymentSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeploymentSummary::OAIDeploymentSummary() {
    this->initializeModel();
}

OAIDeploymentSummary::~OAIDeploymentSummary() {}

void OAIDeploymentSummary::initializeModel() {

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_completed_at_isSet = false;
    m_completed_at_isValid = false;

    m_component_name_isSet = false;
    m_component_name_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_deployment_status_isSet = false;
    m_deployment_status_isValid = false;

    m_environment_name_isSet = false;
    m_environment_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_attempted_deployment_id_isSet = false;
    m_last_attempted_deployment_id_isValid = false;

    m_last_modified_at_isSet = false;
    m_last_modified_at_isValid = false;

    m_last_succeeded_deployment_id_isSet = false;
    m_last_succeeded_deployment_id_isValid = false;

    m_service_instance_name_isSet = false;
    m_service_instance_name_isValid = false;

    m_service_name_isSet = false;
    m_service_name_isValid = false;

    m_target_arn_isSet = false;
    m_target_arn_isValid = false;

    m_target_resource_created_at_isSet = false;
    m_target_resource_created_at_isValid = false;

    m_target_resource_type_isSet = false;
    m_target_resource_type_isValid = false;
}

void OAIDeploymentSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeploymentSummary::fromJsonObject(QJsonObject json) {

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_completed_at_isValid = ::OpenAPI::fromJsonValue(m_completed_at, json[QString("completedAt")]);
    m_completed_at_isSet = !json[QString("completedAt")].isNull() && m_completed_at_isValid;

    m_component_name_isValid = ::OpenAPI::fromJsonValue(m_component_name, json[QString("componentName")]);
    m_component_name_isSet = !json[QString("componentName")].isNull() && m_component_name_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_deployment_status_isValid = ::OpenAPI::fromJsonValue(m_deployment_status, json[QString("deploymentStatus")]);
    m_deployment_status_isSet = !json[QString("deploymentStatus")].isNull() && m_deployment_status_isValid;

    m_environment_name_isValid = ::OpenAPI::fromJsonValue(m_environment_name, json[QString("environmentName")]);
    m_environment_name_isSet = !json[QString("environmentName")].isNull() && m_environment_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_attempted_deployment_id_isValid = ::OpenAPI::fromJsonValue(m_last_attempted_deployment_id, json[QString("lastAttemptedDeploymentId")]);
    m_last_attempted_deployment_id_isSet = !json[QString("lastAttemptedDeploymentId")].isNull() && m_last_attempted_deployment_id_isValid;

    m_last_modified_at_isValid = ::OpenAPI::fromJsonValue(m_last_modified_at, json[QString("lastModifiedAt")]);
    m_last_modified_at_isSet = !json[QString("lastModifiedAt")].isNull() && m_last_modified_at_isValid;

    m_last_succeeded_deployment_id_isValid = ::OpenAPI::fromJsonValue(m_last_succeeded_deployment_id, json[QString("lastSucceededDeploymentId")]);
    m_last_succeeded_deployment_id_isSet = !json[QString("lastSucceededDeploymentId")].isNull() && m_last_succeeded_deployment_id_isValid;

    m_service_instance_name_isValid = ::OpenAPI::fromJsonValue(m_service_instance_name, json[QString("serviceInstanceName")]);
    m_service_instance_name_isSet = !json[QString("serviceInstanceName")].isNull() && m_service_instance_name_isValid;

    m_service_name_isValid = ::OpenAPI::fromJsonValue(m_service_name, json[QString("serviceName")]);
    m_service_name_isSet = !json[QString("serviceName")].isNull() && m_service_name_isValid;

    m_target_arn_isValid = ::OpenAPI::fromJsonValue(m_target_arn, json[QString("targetArn")]);
    m_target_arn_isSet = !json[QString("targetArn")].isNull() && m_target_arn_isValid;

    m_target_resource_created_at_isValid = ::OpenAPI::fromJsonValue(m_target_resource_created_at, json[QString("targetResourceCreatedAt")]);
    m_target_resource_created_at_isSet = !json[QString("targetResourceCreatedAt")].isNull() && m_target_resource_created_at_isValid;

    m_target_resource_type_isValid = ::OpenAPI::fromJsonValue(m_target_resource_type, json[QString("targetResourceType")]);
    m_target_resource_type_isSet = !json[QString("targetResourceType")].isNull() && m_target_resource_type_isValid;
}

QString OAIDeploymentSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeploymentSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_completed_at_isSet) {
        obj.insert(QString("completedAt"), ::OpenAPI::toJsonValue(m_completed_at));
    }
    if (m_component_name_isSet) {
        obj.insert(QString("componentName"), ::OpenAPI::toJsonValue(m_component_name));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_deployment_status.isSet()) {
        obj.insert(QString("deploymentStatus"), ::OpenAPI::toJsonValue(m_deployment_status));
    }
    if (m_environment_name_isSet) {
        obj.insert(QString("environmentName"), ::OpenAPI::toJsonValue(m_environment_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_attempted_deployment_id_isSet) {
        obj.insert(QString("lastAttemptedDeploymentId"), ::OpenAPI::toJsonValue(m_last_attempted_deployment_id));
    }
    if (m_last_modified_at_isSet) {
        obj.insert(QString("lastModifiedAt"), ::OpenAPI::toJsonValue(m_last_modified_at));
    }
    if (m_last_succeeded_deployment_id_isSet) {
        obj.insert(QString("lastSucceededDeploymentId"), ::OpenAPI::toJsonValue(m_last_succeeded_deployment_id));
    }
    if (m_service_instance_name_isSet) {
        obj.insert(QString("serviceInstanceName"), ::OpenAPI::toJsonValue(m_service_instance_name));
    }
    if (m_service_name_isSet) {
        obj.insert(QString("serviceName"), ::OpenAPI::toJsonValue(m_service_name));
    }
    if (m_target_arn_isSet) {
        obj.insert(QString("targetArn"), ::OpenAPI::toJsonValue(m_target_arn));
    }
    if (m_target_resource_created_at_isSet) {
        obj.insert(QString("targetResourceCreatedAt"), ::OpenAPI::toJsonValue(m_target_resource_created_at));
    }
    if (m_target_resource_type.isSet()) {
        obj.insert(QString("targetResourceType"), ::OpenAPI::toJsonValue(m_target_resource_type));
    }
    return obj;
}

QString OAIDeploymentSummary::getArn() const {
    return m_arn;
}
void OAIDeploymentSummary::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIDeploymentSummary::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIDeploymentSummary::is_arn_Valid() const{
    return m_arn_isValid;
}

QDateTime OAIDeploymentSummary::getCompletedAt() const {
    return m_completed_at;
}
void OAIDeploymentSummary::setCompletedAt(const QDateTime &completed_at) {
    m_completed_at = completed_at;
    m_completed_at_isSet = true;
}

bool OAIDeploymentSummary::is_completed_at_Set() const{
    return m_completed_at_isSet;
}

bool OAIDeploymentSummary::is_completed_at_Valid() const{
    return m_completed_at_isValid;
}

QString OAIDeploymentSummary::getComponentName() const {
    return m_component_name;
}
void OAIDeploymentSummary::setComponentName(const QString &component_name) {
    m_component_name = component_name;
    m_component_name_isSet = true;
}

bool OAIDeploymentSummary::is_component_name_Set() const{
    return m_component_name_isSet;
}

bool OAIDeploymentSummary::is_component_name_Valid() const{
    return m_component_name_isValid;
}

QDateTime OAIDeploymentSummary::getCreatedAt() const {
    return m_created_at;
}
void OAIDeploymentSummary::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIDeploymentSummary::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIDeploymentSummary::is_created_at_Valid() const{
    return m_created_at_isValid;
}

OAIDeploymentStatus OAIDeploymentSummary::getDeploymentStatus() const {
    return m_deployment_status;
}
void OAIDeploymentSummary::setDeploymentStatus(const OAIDeploymentStatus &deployment_status) {
    m_deployment_status = deployment_status;
    m_deployment_status_isSet = true;
}

bool OAIDeploymentSummary::is_deployment_status_Set() const{
    return m_deployment_status_isSet;
}

bool OAIDeploymentSummary::is_deployment_status_Valid() const{
    return m_deployment_status_isValid;
}

QString OAIDeploymentSummary::getEnvironmentName() const {
    return m_environment_name;
}
void OAIDeploymentSummary::setEnvironmentName(const QString &environment_name) {
    m_environment_name = environment_name;
    m_environment_name_isSet = true;
}

bool OAIDeploymentSummary::is_environment_name_Set() const{
    return m_environment_name_isSet;
}

bool OAIDeploymentSummary::is_environment_name_Valid() const{
    return m_environment_name_isValid;
}

QString OAIDeploymentSummary::getId() const {
    return m_id;
}
void OAIDeploymentSummary::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDeploymentSummary::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDeploymentSummary::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDeploymentSummary::getLastAttemptedDeploymentId() const {
    return m_last_attempted_deployment_id;
}
void OAIDeploymentSummary::setLastAttemptedDeploymentId(const QString &last_attempted_deployment_id) {
    m_last_attempted_deployment_id = last_attempted_deployment_id;
    m_last_attempted_deployment_id_isSet = true;
}

bool OAIDeploymentSummary::is_last_attempted_deployment_id_Set() const{
    return m_last_attempted_deployment_id_isSet;
}

bool OAIDeploymentSummary::is_last_attempted_deployment_id_Valid() const{
    return m_last_attempted_deployment_id_isValid;
}

QDateTime OAIDeploymentSummary::getLastModifiedAt() const {
    return m_last_modified_at;
}
void OAIDeploymentSummary::setLastModifiedAt(const QDateTime &last_modified_at) {
    m_last_modified_at = last_modified_at;
    m_last_modified_at_isSet = true;
}

bool OAIDeploymentSummary::is_last_modified_at_Set() const{
    return m_last_modified_at_isSet;
}

bool OAIDeploymentSummary::is_last_modified_at_Valid() const{
    return m_last_modified_at_isValid;
}

QString OAIDeploymentSummary::getLastSucceededDeploymentId() const {
    return m_last_succeeded_deployment_id;
}
void OAIDeploymentSummary::setLastSucceededDeploymentId(const QString &last_succeeded_deployment_id) {
    m_last_succeeded_deployment_id = last_succeeded_deployment_id;
    m_last_succeeded_deployment_id_isSet = true;
}

bool OAIDeploymentSummary::is_last_succeeded_deployment_id_Set() const{
    return m_last_succeeded_deployment_id_isSet;
}

bool OAIDeploymentSummary::is_last_succeeded_deployment_id_Valid() const{
    return m_last_succeeded_deployment_id_isValid;
}

QString OAIDeploymentSummary::getServiceInstanceName() const {
    return m_service_instance_name;
}
void OAIDeploymentSummary::setServiceInstanceName(const QString &service_instance_name) {
    m_service_instance_name = service_instance_name;
    m_service_instance_name_isSet = true;
}

bool OAIDeploymentSummary::is_service_instance_name_Set() const{
    return m_service_instance_name_isSet;
}

bool OAIDeploymentSummary::is_service_instance_name_Valid() const{
    return m_service_instance_name_isValid;
}

QString OAIDeploymentSummary::getServiceName() const {
    return m_service_name;
}
void OAIDeploymentSummary::setServiceName(const QString &service_name) {
    m_service_name = service_name;
    m_service_name_isSet = true;
}

bool OAIDeploymentSummary::is_service_name_Set() const{
    return m_service_name_isSet;
}

bool OAIDeploymentSummary::is_service_name_Valid() const{
    return m_service_name_isValid;
}

QString OAIDeploymentSummary::getTargetArn() const {
    return m_target_arn;
}
void OAIDeploymentSummary::setTargetArn(const QString &target_arn) {
    m_target_arn = target_arn;
    m_target_arn_isSet = true;
}

bool OAIDeploymentSummary::is_target_arn_Set() const{
    return m_target_arn_isSet;
}

bool OAIDeploymentSummary::is_target_arn_Valid() const{
    return m_target_arn_isValid;
}

QDateTime OAIDeploymentSummary::getTargetResourceCreatedAt() const {
    return m_target_resource_created_at;
}
void OAIDeploymentSummary::setTargetResourceCreatedAt(const QDateTime &target_resource_created_at) {
    m_target_resource_created_at = target_resource_created_at;
    m_target_resource_created_at_isSet = true;
}

bool OAIDeploymentSummary::is_target_resource_created_at_Set() const{
    return m_target_resource_created_at_isSet;
}

bool OAIDeploymentSummary::is_target_resource_created_at_Valid() const{
    return m_target_resource_created_at_isValid;
}

OAIDeploymentTargetResourceType OAIDeploymentSummary::getTargetResourceType() const {
    return m_target_resource_type;
}
void OAIDeploymentSummary::setTargetResourceType(const OAIDeploymentTargetResourceType &target_resource_type) {
    m_target_resource_type = target_resource_type;
    m_target_resource_type_isSet = true;
}

bool OAIDeploymentSummary::is_target_resource_type_Set() const{
    return m_target_resource_type_isSet;
}

bool OAIDeploymentSummary::is_target_resource_type_Valid() const{
    return m_target_resource_type_isValid;
}

bool OAIDeploymentSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_completed_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_component_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deployment_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_attempted_deployment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_modified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_succeeded_deployment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_instance_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_resource_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_resource_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeploymentSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_arn_isValid && m_created_at_isValid && m_deployment_status_isValid && m_environment_name_isValid && m_id_isValid && m_last_modified_at_isValid && m_target_arn_isValid && m_target_resource_created_at_isValid && m_target_resource_type_isValid && true;
}

} // namespace OpenAPI
