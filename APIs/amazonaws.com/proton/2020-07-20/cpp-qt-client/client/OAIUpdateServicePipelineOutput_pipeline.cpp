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

#include "OAIUpdateServicePipelineOutput_pipeline.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateServicePipelineOutput_pipeline::OAIUpdateServicePipelineOutput_pipeline(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateServicePipelineOutput_pipeline::OAIUpdateServicePipelineOutput_pipeline() {
    this->initializeModel();
}

OAIUpdateServicePipelineOutput_pipeline::~OAIUpdateServicePipelineOutput_pipeline() {}

void OAIUpdateServicePipelineOutput_pipeline::initializeModel() {

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_deployment_status_isSet = false;
    m_deployment_status_isValid = false;

    m_deployment_status_message_isSet = false;
    m_deployment_status_message_isValid = false;

    m_last_attempted_deployment_id_isSet = false;
    m_last_attempted_deployment_id_isValid = false;

    m_last_deployment_attempted_at_isSet = false;
    m_last_deployment_attempted_at_isValid = false;

    m_last_deployment_succeeded_at_isSet = false;
    m_last_deployment_succeeded_at_isValid = false;

    m_last_succeeded_deployment_id_isSet = false;
    m_last_succeeded_deployment_id_isValid = false;

    m_spec_isSet = false;
    m_spec_isValid = false;

    m_template_major_version_isSet = false;
    m_template_major_version_isValid = false;

    m_template_minor_version_isSet = false;
    m_template_minor_version_isValid = false;

    m_template_name_isSet = false;
    m_template_name_isValid = false;
}

void OAIUpdateServicePipelineOutput_pipeline::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateServicePipelineOutput_pipeline::fromJsonObject(QJsonObject json) {

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_deployment_status_isValid = ::OpenAPI::fromJsonValue(m_deployment_status, json[QString("deploymentStatus")]);
    m_deployment_status_isSet = !json[QString("deploymentStatus")].isNull() && m_deployment_status_isValid;

    m_deployment_status_message_isValid = ::OpenAPI::fromJsonValue(m_deployment_status_message, json[QString("deploymentStatusMessage")]);
    m_deployment_status_message_isSet = !json[QString("deploymentStatusMessage")].isNull() && m_deployment_status_message_isValid;

    m_last_attempted_deployment_id_isValid = ::OpenAPI::fromJsonValue(m_last_attempted_deployment_id, json[QString("lastAttemptedDeploymentId")]);
    m_last_attempted_deployment_id_isSet = !json[QString("lastAttemptedDeploymentId")].isNull() && m_last_attempted_deployment_id_isValid;

    m_last_deployment_attempted_at_isValid = ::OpenAPI::fromJsonValue(m_last_deployment_attempted_at, json[QString("lastDeploymentAttemptedAt")]);
    m_last_deployment_attempted_at_isSet = !json[QString("lastDeploymentAttemptedAt")].isNull() && m_last_deployment_attempted_at_isValid;

    m_last_deployment_succeeded_at_isValid = ::OpenAPI::fromJsonValue(m_last_deployment_succeeded_at, json[QString("lastDeploymentSucceededAt")]);
    m_last_deployment_succeeded_at_isSet = !json[QString("lastDeploymentSucceededAt")].isNull() && m_last_deployment_succeeded_at_isValid;

    m_last_succeeded_deployment_id_isValid = ::OpenAPI::fromJsonValue(m_last_succeeded_deployment_id, json[QString("lastSucceededDeploymentId")]);
    m_last_succeeded_deployment_id_isSet = !json[QString("lastSucceededDeploymentId")].isNull() && m_last_succeeded_deployment_id_isValid;

    m_spec_isValid = ::OpenAPI::fromJsonValue(m_spec, json[QString("spec")]);
    m_spec_isSet = !json[QString("spec")].isNull() && m_spec_isValid;

    m_template_major_version_isValid = ::OpenAPI::fromJsonValue(m_template_major_version, json[QString("templateMajorVersion")]);
    m_template_major_version_isSet = !json[QString("templateMajorVersion")].isNull() && m_template_major_version_isValid;

    m_template_minor_version_isValid = ::OpenAPI::fromJsonValue(m_template_minor_version, json[QString("templateMinorVersion")]);
    m_template_minor_version_isSet = !json[QString("templateMinorVersion")].isNull() && m_template_minor_version_isValid;

    m_template_name_isValid = ::OpenAPI::fromJsonValue(m_template_name, json[QString("templateName")]);
    m_template_name_isSet = !json[QString("templateName")].isNull() && m_template_name_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateServicePipelineOutput_pipeline::asJsonObject() const {
    QJsonObject obj;
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_deployment_status.isSet()) {
        obj.insert(QString("deploymentStatus"), ::OpenAPI::toJsonValue(m_deployment_status));
    }
    if (m_deployment_status_message_isSet) {
        obj.insert(QString("deploymentStatusMessage"), ::OpenAPI::toJsonValue(m_deployment_status_message));
    }
    if (m_last_attempted_deployment_id_isSet) {
        obj.insert(QString("lastAttemptedDeploymentId"), ::OpenAPI::toJsonValue(m_last_attempted_deployment_id));
    }
    if (m_last_deployment_attempted_at_isSet) {
        obj.insert(QString("lastDeploymentAttemptedAt"), ::OpenAPI::toJsonValue(m_last_deployment_attempted_at));
    }
    if (m_last_deployment_succeeded_at_isSet) {
        obj.insert(QString("lastDeploymentSucceededAt"), ::OpenAPI::toJsonValue(m_last_deployment_succeeded_at));
    }
    if (m_last_succeeded_deployment_id_isSet) {
        obj.insert(QString("lastSucceededDeploymentId"), ::OpenAPI::toJsonValue(m_last_succeeded_deployment_id));
    }
    if (m_spec_isSet) {
        obj.insert(QString("spec"), ::OpenAPI::toJsonValue(m_spec));
    }
    if (m_template_major_version_isSet) {
        obj.insert(QString("templateMajorVersion"), ::OpenAPI::toJsonValue(m_template_major_version));
    }
    if (m_template_minor_version_isSet) {
        obj.insert(QString("templateMinorVersion"), ::OpenAPI::toJsonValue(m_template_minor_version));
    }
    if (m_template_name_isSet) {
        obj.insert(QString("templateName"), ::OpenAPI::toJsonValue(m_template_name));
    }
    return obj;
}

QString OAIUpdateServicePipelineOutput_pipeline::getArn() const {
    return m_arn;
}
void OAIUpdateServicePipelineOutput_pipeline::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_arn_Valid() const{
    return m_arn_isValid;
}

QDateTime OAIUpdateServicePipelineOutput_pipeline::getCreatedAt() const {
    return m_created_at;
}
void OAIUpdateServicePipelineOutput_pipeline::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_created_at_Valid() const{
    return m_created_at_isValid;
}

OAIDeploymentStatus OAIUpdateServicePipelineOutput_pipeline::getDeploymentStatus() const {
    return m_deployment_status;
}
void OAIUpdateServicePipelineOutput_pipeline::setDeploymentStatus(const OAIDeploymentStatus &deployment_status) {
    m_deployment_status = deployment_status;
    m_deployment_status_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_deployment_status_Set() const{
    return m_deployment_status_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_deployment_status_Valid() const{
    return m_deployment_status_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getDeploymentStatusMessage() const {
    return m_deployment_status_message;
}
void OAIUpdateServicePipelineOutput_pipeline::setDeploymentStatusMessage(const QString &deployment_status_message) {
    m_deployment_status_message = deployment_status_message;
    m_deployment_status_message_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_deployment_status_message_Set() const{
    return m_deployment_status_message_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_deployment_status_message_Valid() const{
    return m_deployment_status_message_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getLastAttemptedDeploymentId() const {
    return m_last_attempted_deployment_id;
}
void OAIUpdateServicePipelineOutput_pipeline::setLastAttemptedDeploymentId(const QString &last_attempted_deployment_id) {
    m_last_attempted_deployment_id = last_attempted_deployment_id;
    m_last_attempted_deployment_id_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_attempted_deployment_id_Set() const{
    return m_last_attempted_deployment_id_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_attempted_deployment_id_Valid() const{
    return m_last_attempted_deployment_id_isValid;
}

QDateTime OAIUpdateServicePipelineOutput_pipeline::getLastDeploymentAttemptedAt() const {
    return m_last_deployment_attempted_at;
}
void OAIUpdateServicePipelineOutput_pipeline::setLastDeploymentAttemptedAt(const QDateTime &last_deployment_attempted_at) {
    m_last_deployment_attempted_at = last_deployment_attempted_at;
    m_last_deployment_attempted_at_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_deployment_attempted_at_Set() const{
    return m_last_deployment_attempted_at_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_deployment_attempted_at_Valid() const{
    return m_last_deployment_attempted_at_isValid;
}

QDateTime OAIUpdateServicePipelineOutput_pipeline::getLastDeploymentSucceededAt() const {
    return m_last_deployment_succeeded_at;
}
void OAIUpdateServicePipelineOutput_pipeline::setLastDeploymentSucceededAt(const QDateTime &last_deployment_succeeded_at) {
    m_last_deployment_succeeded_at = last_deployment_succeeded_at;
    m_last_deployment_succeeded_at_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_deployment_succeeded_at_Set() const{
    return m_last_deployment_succeeded_at_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_deployment_succeeded_at_Valid() const{
    return m_last_deployment_succeeded_at_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getLastSucceededDeploymentId() const {
    return m_last_succeeded_deployment_id;
}
void OAIUpdateServicePipelineOutput_pipeline::setLastSucceededDeploymentId(const QString &last_succeeded_deployment_id) {
    m_last_succeeded_deployment_id = last_succeeded_deployment_id;
    m_last_succeeded_deployment_id_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_succeeded_deployment_id_Set() const{
    return m_last_succeeded_deployment_id_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_last_succeeded_deployment_id_Valid() const{
    return m_last_succeeded_deployment_id_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getSpec() const {
    return m_spec;
}
void OAIUpdateServicePipelineOutput_pipeline::setSpec(const QString &spec) {
    m_spec = spec;
    m_spec_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_spec_Set() const{
    return m_spec_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_spec_Valid() const{
    return m_spec_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getTemplateMajorVersion() const {
    return m_template_major_version;
}
void OAIUpdateServicePipelineOutput_pipeline::setTemplateMajorVersion(const QString &template_major_version) {
    m_template_major_version = template_major_version;
    m_template_major_version_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_major_version_Set() const{
    return m_template_major_version_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_major_version_Valid() const{
    return m_template_major_version_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getTemplateMinorVersion() const {
    return m_template_minor_version;
}
void OAIUpdateServicePipelineOutput_pipeline::setTemplateMinorVersion(const QString &template_minor_version) {
    m_template_minor_version = template_minor_version;
    m_template_minor_version_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_minor_version_Set() const{
    return m_template_minor_version_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_minor_version_Valid() const{
    return m_template_minor_version_isValid;
}

QString OAIUpdateServicePipelineOutput_pipeline::getTemplateName() const {
    return m_template_name;
}
void OAIUpdateServicePipelineOutput_pipeline::setTemplateName(const QString &template_name) {
    m_template_name = template_name;
    m_template_name_isSet = true;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_name_Set() const{
    return m_template_name_isSet;
}

bool OAIUpdateServicePipelineOutput_pipeline::is_template_name_Valid() const{
    return m_template_name_isValid;
}

bool OAIUpdateServicePipelineOutput_pipeline::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arn_isSet) {
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

        if (m_deployment_status_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_attempted_deployment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_deployment_attempted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_deployment_succeeded_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_succeeded_deployment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_major_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_minor_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateServicePipelineOutput_pipeline::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_arn_isValid && m_created_at_isValid && m_deployment_status_isValid && m_last_deployment_attempted_at_isValid && m_last_deployment_succeeded_at_isValid && m_template_major_version_isValid && m_template_minor_version_isValid && m_template_name_isValid && true;
}

} // namespace OpenAPI
