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

#include "OAICreateEnvironmentInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateEnvironmentInput::OAICreateEnvironmentInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateEnvironmentInput::OAICreateEnvironmentInput() {
    this->initializeModel();
}

OAICreateEnvironmentInput::~OAICreateEnvironmentInput() {}

void OAICreateEnvironmentInput::initializeModel() {

    m_codebuild_role_arn_isSet = false;
    m_codebuild_role_arn_isValid = false;

    m_component_role_arn_isSet = false;
    m_component_role_arn_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_environment_account_connection_id_isSet = false;
    m_environment_account_connection_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_proton_service_role_arn_isSet = false;
    m_proton_service_role_arn_isValid = false;

    m_provisioning_repository_isSet = false;
    m_provisioning_repository_isValid = false;

    m_spec_isSet = false;
    m_spec_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_template_major_version_isSet = false;
    m_template_major_version_isValid = false;

    m_template_minor_version_isSet = false;
    m_template_minor_version_isValid = false;

    m_template_name_isSet = false;
    m_template_name_isValid = false;
}

void OAICreateEnvironmentInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateEnvironmentInput::fromJsonObject(QJsonObject json) {

    m_codebuild_role_arn_isValid = ::OpenAPI::fromJsonValue(m_codebuild_role_arn, json[QString("codebuildRoleArn")]);
    m_codebuild_role_arn_isSet = !json[QString("codebuildRoleArn")].isNull() && m_codebuild_role_arn_isValid;

    m_component_role_arn_isValid = ::OpenAPI::fromJsonValue(m_component_role_arn, json[QString("componentRoleArn")]);
    m_component_role_arn_isSet = !json[QString("componentRoleArn")].isNull() && m_component_role_arn_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_environment_account_connection_id_isValid = ::OpenAPI::fromJsonValue(m_environment_account_connection_id, json[QString("environmentAccountConnectionId")]);
    m_environment_account_connection_id_isSet = !json[QString("environmentAccountConnectionId")].isNull() && m_environment_account_connection_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_proton_service_role_arn_isValid = ::OpenAPI::fromJsonValue(m_proton_service_role_arn, json[QString("protonServiceRoleArn")]);
    m_proton_service_role_arn_isSet = !json[QString("protonServiceRoleArn")].isNull() && m_proton_service_role_arn_isValid;

    m_provisioning_repository_isValid = ::OpenAPI::fromJsonValue(m_provisioning_repository, json[QString("provisioningRepository")]);
    m_provisioning_repository_isSet = !json[QString("provisioningRepository")].isNull() && m_provisioning_repository_isValid;

    m_spec_isValid = ::OpenAPI::fromJsonValue(m_spec, json[QString("spec")]);
    m_spec_isSet = !json[QString("spec")].isNull() && m_spec_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_template_major_version_isValid = ::OpenAPI::fromJsonValue(m_template_major_version, json[QString("templateMajorVersion")]);
    m_template_major_version_isSet = !json[QString("templateMajorVersion")].isNull() && m_template_major_version_isValid;

    m_template_minor_version_isValid = ::OpenAPI::fromJsonValue(m_template_minor_version, json[QString("templateMinorVersion")]);
    m_template_minor_version_isSet = !json[QString("templateMinorVersion")].isNull() && m_template_minor_version_isValid;

    m_template_name_isValid = ::OpenAPI::fromJsonValue(m_template_name, json[QString("templateName")]);
    m_template_name_isSet = !json[QString("templateName")].isNull() && m_template_name_isValid;
}

QString OAICreateEnvironmentInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateEnvironmentInput::asJsonObject() const {
    QJsonObject obj;
    if (m_codebuild_role_arn_isSet) {
        obj.insert(QString("codebuildRoleArn"), ::OpenAPI::toJsonValue(m_codebuild_role_arn));
    }
    if (m_component_role_arn_isSet) {
        obj.insert(QString("componentRoleArn"), ::OpenAPI::toJsonValue(m_component_role_arn));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_environment_account_connection_id_isSet) {
        obj.insert(QString("environmentAccountConnectionId"), ::OpenAPI::toJsonValue(m_environment_account_connection_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_proton_service_role_arn_isSet) {
        obj.insert(QString("protonServiceRoleArn"), ::OpenAPI::toJsonValue(m_proton_service_role_arn));
    }
    if (m_provisioning_repository.isSet()) {
        obj.insert(QString("provisioningRepository"), ::OpenAPI::toJsonValue(m_provisioning_repository));
    }
    if (m_spec_isSet) {
        obj.insert(QString("spec"), ::OpenAPI::toJsonValue(m_spec));
    }
    if (m_tags.isSet()) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
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

QString OAICreateEnvironmentInput::getCodebuildRoleArn() const {
    return m_codebuild_role_arn;
}
void OAICreateEnvironmentInput::setCodebuildRoleArn(const QString &codebuild_role_arn) {
    m_codebuild_role_arn = codebuild_role_arn;
    m_codebuild_role_arn_isSet = true;
}

bool OAICreateEnvironmentInput::is_codebuild_role_arn_Set() const{
    return m_codebuild_role_arn_isSet;
}

bool OAICreateEnvironmentInput::is_codebuild_role_arn_Valid() const{
    return m_codebuild_role_arn_isValid;
}

QString OAICreateEnvironmentInput::getComponentRoleArn() const {
    return m_component_role_arn;
}
void OAICreateEnvironmentInput::setComponentRoleArn(const QString &component_role_arn) {
    m_component_role_arn = component_role_arn;
    m_component_role_arn_isSet = true;
}

bool OAICreateEnvironmentInput::is_component_role_arn_Set() const{
    return m_component_role_arn_isSet;
}

bool OAICreateEnvironmentInput::is_component_role_arn_Valid() const{
    return m_component_role_arn_isValid;
}

QString OAICreateEnvironmentInput::getDescription() const {
    return m_description;
}
void OAICreateEnvironmentInput::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICreateEnvironmentInput::is_description_Set() const{
    return m_description_isSet;
}

bool OAICreateEnvironmentInput::is_description_Valid() const{
    return m_description_isValid;
}

QString OAICreateEnvironmentInput::getEnvironmentAccountConnectionId() const {
    return m_environment_account_connection_id;
}
void OAICreateEnvironmentInput::setEnvironmentAccountConnectionId(const QString &environment_account_connection_id) {
    m_environment_account_connection_id = environment_account_connection_id;
    m_environment_account_connection_id_isSet = true;
}

bool OAICreateEnvironmentInput::is_environment_account_connection_id_Set() const{
    return m_environment_account_connection_id_isSet;
}

bool OAICreateEnvironmentInput::is_environment_account_connection_id_Valid() const{
    return m_environment_account_connection_id_isValid;
}

QString OAICreateEnvironmentInput::getName() const {
    return m_name;
}
void OAICreateEnvironmentInput::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateEnvironmentInput::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateEnvironmentInput::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateEnvironmentInput::getProtonServiceRoleArn() const {
    return m_proton_service_role_arn;
}
void OAICreateEnvironmentInput::setProtonServiceRoleArn(const QString &proton_service_role_arn) {
    m_proton_service_role_arn = proton_service_role_arn;
    m_proton_service_role_arn_isSet = true;
}

bool OAICreateEnvironmentInput::is_proton_service_role_arn_Set() const{
    return m_proton_service_role_arn_isSet;
}

bool OAICreateEnvironmentInput::is_proton_service_role_arn_Valid() const{
    return m_proton_service_role_arn_isValid;
}

OAICreateEnvironmentInput_provisioningRepository OAICreateEnvironmentInput::getProvisioningRepository() const {
    return m_provisioning_repository;
}
void OAICreateEnvironmentInput::setProvisioningRepository(const OAICreateEnvironmentInput_provisioningRepository &provisioning_repository) {
    m_provisioning_repository = provisioning_repository;
    m_provisioning_repository_isSet = true;
}

bool OAICreateEnvironmentInput::is_provisioning_repository_Set() const{
    return m_provisioning_repository_isSet;
}

bool OAICreateEnvironmentInput::is_provisioning_repository_Valid() const{
    return m_provisioning_repository_isValid;
}

QString OAICreateEnvironmentInput::getSpec() const {
    return m_spec;
}
void OAICreateEnvironmentInput::setSpec(const QString &spec) {
    m_spec = spec;
    m_spec_isSet = true;
}

bool OAICreateEnvironmentInput::is_spec_Set() const{
    return m_spec_isSet;
}

bool OAICreateEnvironmentInput::is_spec_Valid() const{
    return m_spec_isValid;
}

QList OAICreateEnvironmentInput::getTags() const {
    return m_tags;
}
void OAICreateEnvironmentInput::setTags(const QList &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateEnvironmentInput::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateEnvironmentInput::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAICreateEnvironmentInput::getTemplateMajorVersion() const {
    return m_template_major_version;
}
void OAICreateEnvironmentInput::setTemplateMajorVersion(const QString &template_major_version) {
    m_template_major_version = template_major_version;
    m_template_major_version_isSet = true;
}

bool OAICreateEnvironmentInput::is_template_major_version_Set() const{
    return m_template_major_version_isSet;
}

bool OAICreateEnvironmentInput::is_template_major_version_Valid() const{
    return m_template_major_version_isValid;
}

QString OAICreateEnvironmentInput::getTemplateMinorVersion() const {
    return m_template_minor_version;
}
void OAICreateEnvironmentInput::setTemplateMinorVersion(const QString &template_minor_version) {
    m_template_minor_version = template_minor_version;
    m_template_minor_version_isSet = true;
}

bool OAICreateEnvironmentInput::is_template_minor_version_Set() const{
    return m_template_minor_version_isSet;
}

bool OAICreateEnvironmentInput::is_template_minor_version_Valid() const{
    return m_template_minor_version_isValid;
}

QString OAICreateEnvironmentInput::getTemplateName() const {
    return m_template_name;
}
void OAICreateEnvironmentInput::setTemplateName(const QString &template_name) {
    m_template_name = template_name;
    m_template_name_isSet = true;
}

bool OAICreateEnvironmentInput::is_template_name_Set() const{
    return m_template_name_isSet;
}

bool OAICreateEnvironmentInput::is_template_name_Valid() const{
    return m_template_name_isValid;
}

bool OAICreateEnvironmentInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_codebuild_role_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_component_role_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_environment_account_connection_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proton_service_role_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provisioning_repository.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.isSet()) {
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

bool OAICreateEnvironmentInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_spec_isValid && m_template_major_version_isValid && m_template_name_isValid && true;
}

} // namespace OpenAPI
