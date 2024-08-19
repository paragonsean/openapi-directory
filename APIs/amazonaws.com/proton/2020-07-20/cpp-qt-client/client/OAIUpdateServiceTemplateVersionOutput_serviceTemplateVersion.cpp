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

#include "OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion() {
    this->initializeModel();
}

OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::~OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion() {}

void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::initializeModel() {

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_compatible_environment_templates_isSet = false;
    m_compatible_environment_templates_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_last_modified_at_isSet = false;
    m_last_modified_at_isValid = false;

    m_major_version_isSet = false;
    m_major_version_isValid = false;

    m_minor_version_isSet = false;
    m_minor_version_isValid = false;

    m_recommended_minor_version_isSet = false;
    m_recommended_minor_version_isValid = false;

    m_schema_isSet = false;
    m_schema_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_status_message_isSet = false;
    m_status_message_isValid = false;

    m_supported_component_sources_isSet = false;
    m_supported_component_sources_isValid = false;

    m_template_name_isSet = false;
    m_template_name_isValid = false;
}

void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::fromJsonObject(QJsonObject json) {

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_compatible_environment_templates_isValid = ::OpenAPI::fromJsonValue(m_compatible_environment_templates, json[QString("compatibleEnvironmentTemplates")]);
    m_compatible_environment_templates_isSet = !json[QString("compatibleEnvironmentTemplates")].isNull() && m_compatible_environment_templates_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_last_modified_at_isValid = ::OpenAPI::fromJsonValue(m_last_modified_at, json[QString("lastModifiedAt")]);
    m_last_modified_at_isSet = !json[QString("lastModifiedAt")].isNull() && m_last_modified_at_isValid;

    m_major_version_isValid = ::OpenAPI::fromJsonValue(m_major_version, json[QString("majorVersion")]);
    m_major_version_isSet = !json[QString("majorVersion")].isNull() && m_major_version_isValid;

    m_minor_version_isValid = ::OpenAPI::fromJsonValue(m_minor_version, json[QString("minorVersion")]);
    m_minor_version_isSet = !json[QString("minorVersion")].isNull() && m_minor_version_isValid;

    m_recommended_minor_version_isValid = ::OpenAPI::fromJsonValue(m_recommended_minor_version, json[QString("recommendedMinorVersion")]);
    m_recommended_minor_version_isSet = !json[QString("recommendedMinorVersion")].isNull() && m_recommended_minor_version_isValid;

    m_schema_isValid = ::OpenAPI::fromJsonValue(m_schema, json[QString("schema")]);
    m_schema_isSet = !json[QString("schema")].isNull() && m_schema_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_status_message_isValid = ::OpenAPI::fromJsonValue(m_status_message, json[QString("statusMessage")]);
    m_status_message_isSet = !json[QString("statusMessage")].isNull() && m_status_message_isValid;

    m_supported_component_sources_isValid = ::OpenAPI::fromJsonValue(m_supported_component_sources, json[QString("supportedComponentSources")]);
    m_supported_component_sources_isSet = !json[QString("supportedComponentSources")].isNull() && m_supported_component_sources_isValid;

    m_template_name_isValid = ::OpenAPI::fromJsonValue(m_template_name, json[QString("templateName")]);
    m_template_name_isSet = !json[QString("templateName")].isNull() && m_template_name_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_compatible_environment_templates.isSet()) {
        obj.insert(QString("compatibleEnvironmentTemplates"), ::OpenAPI::toJsonValue(m_compatible_environment_templates));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_last_modified_at_isSet) {
        obj.insert(QString("lastModifiedAt"), ::OpenAPI::toJsonValue(m_last_modified_at));
    }
    if (m_major_version_isSet) {
        obj.insert(QString("majorVersion"), ::OpenAPI::toJsonValue(m_major_version));
    }
    if (m_minor_version_isSet) {
        obj.insert(QString("minorVersion"), ::OpenAPI::toJsonValue(m_minor_version));
    }
    if (m_recommended_minor_version_isSet) {
        obj.insert(QString("recommendedMinorVersion"), ::OpenAPI::toJsonValue(m_recommended_minor_version));
    }
    if (m_schema_isSet) {
        obj.insert(QString("schema"), ::OpenAPI::toJsonValue(m_schema));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_status_message_isSet) {
        obj.insert(QString("statusMessage"), ::OpenAPI::toJsonValue(m_status_message));
    }
    if (m_supported_component_sources.isSet()) {
        obj.insert(QString("supportedComponentSources"), ::OpenAPI::toJsonValue(m_supported_component_sources));
    }
    if (m_template_name_isSet) {
        obj.insert(QString("templateName"), ::OpenAPI::toJsonValue(m_template_name));
    }
    return obj;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getArn() const {
    return m_arn;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_arn_Valid() const{
    return m_arn_isValid;
}

QList OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getCompatibleEnvironmentTemplates() const {
    return m_compatible_environment_templates;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setCompatibleEnvironmentTemplates(const QList &compatible_environment_templates) {
    m_compatible_environment_templates = compatible_environment_templates;
    m_compatible_environment_templates_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_compatible_environment_templates_Set() const{
    return m_compatible_environment_templates_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_compatible_environment_templates_Valid() const{
    return m_compatible_environment_templates_isValid;
}

QDateTime OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getCreatedAt() const {
    return m_created_at;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getDescription() const {
    return m_description;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_description_Set() const{
    return m_description_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_description_Valid() const{
    return m_description_isValid;
}

QDateTime OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getLastModifiedAt() const {
    return m_last_modified_at;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setLastModifiedAt(const QDateTime &last_modified_at) {
    m_last_modified_at = last_modified_at;
    m_last_modified_at_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_last_modified_at_Set() const{
    return m_last_modified_at_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_last_modified_at_Valid() const{
    return m_last_modified_at_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getMajorVersion() const {
    return m_major_version;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setMajorVersion(const QString &major_version) {
    m_major_version = major_version;
    m_major_version_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_major_version_Set() const{
    return m_major_version_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_major_version_Valid() const{
    return m_major_version_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getMinorVersion() const {
    return m_minor_version;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setMinorVersion(const QString &minor_version) {
    m_minor_version = minor_version;
    m_minor_version_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_minor_version_Set() const{
    return m_minor_version_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_minor_version_Valid() const{
    return m_minor_version_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getRecommendedMinorVersion() const {
    return m_recommended_minor_version;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setRecommendedMinorVersion(const QString &recommended_minor_version) {
    m_recommended_minor_version = recommended_minor_version;
    m_recommended_minor_version_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_recommended_minor_version_Set() const{
    return m_recommended_minor_version_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_recommended_minor_version_Valid() const{
    return m_recommended_minor_version_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getSchema() const {
    return m_schema;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setSchema(const QString &schema) {
    m_schema = schema;
    m_schema_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_schema_Set() const{
    return m_schema_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_schema_Valid() const{
    return m_schema_isValid;
}

OAITemplateVersionStatus OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getStatus() const {
    return m_status;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setStatus(const OAITemplateVersionStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getStatusMessage() const {
    return m_status_message;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setStatusMessage(const QString &status_message) {
    m_status_message = status_message;
    m_status_message_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_status_message_Set() const{
    return m_status_message_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_status_message_Valid() const{
    return m_status_message_isValid;
}

QList OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getSupportedComponentSources() const {
    return m_supported_component_sources;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setSupportedComponentSources(const QList &supported_component_sources) {
    m_supported_component_sources = supported_component_sources;
    m_supported_component_sources_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_supported_component_sources_Set() const{
    return m_supported_component_sources_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_supported_component_sources_Valid() const{
    return m_supported_component_sources_isValid;
}

QString OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::getTemplateName() const {
    return m_template_name;
}
void OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::setTemplateName(const QString &template_name) {
    m_template_name = template_name;
    m_template_name_isSet = true;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_template_name_Set() const{
    return m_template_name_isSet;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::is_template_name_Valid() const{
    return m_template_name_isValid;
}

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_compatible_environment_templates.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_modified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_major_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minor_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recommended_minor_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schema_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_supported_component_sources.isSet()) {
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

bool OAIUpdateServiceTemplateVersionOutput_serviceTemplateVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_arn_isValid && m_compatible_environment_templates_isValid && m_created_at_isValid && m_last_modified_at_isValid && m_major_version_isValid && m_minor_version_isValid && m_status_isValid && m_template_name_isValid && true;
}

} // namespace OpenAPI
