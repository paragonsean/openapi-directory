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

#include "OAIUpdateServiceTemplateVersionInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateServiceTemplateVersionInput::OAIUpdateServiceTemplateVersionInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateServiceTemplateVersionInput::OAIUpdateServiceTemplateVersionInput() {
    this->initializeModel();
}

OAIUpdateServiceTemplateVersionInput::~OAIUpdateServiceTemplateVersionInput() {}

void OAIUpdateServiceTemplateVersionInput::initializeModel() {

    m_compatible_environment_templates_isSet = false;
    m_compatible_environment_templates_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_major_version_isSet = false;
    m_major_version_isValid = false;

    m_minor_version_isSet = false;
    m_minor_version_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_supported_component_sources_isSet = false;
    m_supported_component_sources_isValid = false;

    m_template_name_isSet = false;
    m_template_name_isValid = false;
}

void OAIUpdateServiceTemplateVersionInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateServiceTemplateVersionInput::fromJsonObject(QJsonObject json) {

    m_compatible_environment_templates_isValid = ::OpenAPI::fromJsonValue(m_compatible_environment_templates, json[QString("compatibleEnvironmentTemplates")]);
    m_compatible_environment_templates_isSet = !json[QString("compatibleEnvironmentTemplates")].isNull() && m_compatible_environment_templates_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_major_version_isValid = ::OpenAPI::fromJsonValue(m_major_version, json[QString("majorVersion")]);
    m_major_version_isSet = !json[QString("majorVersion")].isNull() && m_major_version_isValid;

    m_minor_version_isValid = ::OpenAPI::fromJsonValue(m_minor_version, json[QString("minorVersion")]);
    m_minor_version_isSet = !json[QString("minorVersion")].isNull() && m_minor_version_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_supported_component_sources_isValid = ::OpenAPI::fromJsonValue(m_supported_component_sources, json[QString("supportedComponentSources")]);
    m_supported_component_sources_isSet = !json[QString("supportedComponentSources")].isNull() && m_supported_component_sources_isValid;

    m_template_name_isValid = ::OpenAPI::fromJsonValue(m_template_name, json[QString("templateName")]);
    m_template_name_isSet = !json[QString("templateName")].isNull() && m_template_name_isValid;
}

QString OAIUpdateServiceTemplateVersionInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateServiceTemplateVersionInput::asJsonObject() const {
    QJsonObject obj;
    if (m_compatible_environment_templates.isSet()) {
        obj.insert(QString("compatibleEnvironmentTemplates"), ::OpenAPI::toJsonValue(m_compatible_environment_templates));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_major_version_isSet) {
        obj.insert(QString("majorVersion"), ::OpenAPI::toJsonValue(m_major_version));
    }
    if (m_minor_version_isSet) {
        obj.insert(QString("minorVersion"), ::OpenAPI::toJsonValue(m_minor_version));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_supported_component_sources.isSet()) {
        obj.insert(QString("supportedComponentSources"), ::OpenAPI::toJsonValue(m_supported_component_sources));
    }
    if (m_template_name_isSet) {
        obj.insert(QString("templateName"), ::OpenAPI::toJsonValue(m_template_name));
    }
    return obj;
}

QList OAIUpdateServiceTemplateVersionInput::getCompatibleEnvironmentTemplates() const {
    return m_compatible_environment_templates;
}
void OAIUpdateServiceTemplateVersionInput::setCompatibleEnvironmentTemplates(const QList &compatible_environment_templates) {
    m_compatible_environment_templates = compatible_environment_templates;
    m_compatible_environment_templates_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_compatible_environment_templates_Set() const{
    return m_compatible_environment_templates_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_compatible_environment_templates_Valid() const{
    return m_compatible_environment_templates_isValid;
}

QString OAIUpdateServiceTemplateVersionInput::getDescription() const {
    return m_description;
}
void OAIUpdateServiceTemplateVersionInput::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_description_Set() const{
    return m_description_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIUpdateServiceTemplateVersionInput::getMajorVersion() const {
    return m_major_version;
}
void OAIUpdateServiceTemplateVersionInput::setMajorVersion(const QString &major_version) {
    m_major_version = major_version;
    m_major_version_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_major_version_Set() const{
    return m_major_version_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_major_version_Valid() const{
    return m_major_version_isValid;
}

QString OAIUpdateServiceTemplateVersionInput::getMinorVersion() const {
    return m_minor_version;
}
void OAIUpdateServiceTemplateVersionInput::setMinorVersion(const QString &minor_version) {
    m_minor_version = minor_version;
    m_minor_version_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_minor_version_Set() const{
    return m_minor_version_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_minor_version_Valid() const{
    return m_minor_version_isValid;
}

OAITemplateVersionStatus OAIUpdateServiceTemplateVersionInput::getStatus() const {
    return m_status;
}
void OAIUpdateServiceTemplateVersionInput::setStatus(const OAITemplateVersionStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_status_Set() const{
    return m_status_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_status_Valid() const{
    return m_status_isValid;
}

QList OAIUpdateServiceTemplateVersionInput::getSupportedComponentSources() const {
    return m_supported_component_sources;
}
void OAIUpdateServiceTemplateVersionInput::setSupportedComponentSources(const QList &supported_component_sources) {
    m_supported_component_sources = supported_component_sources;
    m_supported_component_sources_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_supported_component_sources_Set() const{
    return m_supported_component_sources_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_supported_component_sources_Valid() const{
    return m_supported_component_sources_isValid;
}

QString OAIUpdateServiceTemplateVersionInput::getTemplateName() const {
    return m_template_name;
}
void OAIUpdateServiceTemplateVersionInput::setTemplateName(const QString &template_name) {
    m_template_name = template_name;
    m_template_name_isSet = true;
}

bool OAIUpdateServiceTemplateVersionInput::is_template_name_Set() const{
    return m_template_name_isSet;
}

bool OAIUpdateServiceTemplateVersionInput::is_template_name_Valid() const{
    return m_template_name_isValid;
}

bool OAIUpdateServiceTemplateVersionInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_compatible_environment_templates.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
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

        if (m_status.isSet()) {
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

bool OAIUpdateServiceTemplateVersionInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_major_version_isValid && m_minor_version_isValid && m_template_name_isValid && true;
}

} // namespace OpenAPI
