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

#include "OAIUpdateComponentInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateComponentInput::OAIUpdateComponentInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateComponentInput::OAIUpdateComponentInput() {
    this->initializeModel();
}

OAIUpdateComponentInput::~OAIUpdateComponentInput() {}

void OAIUpdateComponentInput::initializeModel() {

    m_client_token_isSet = false;
    m_client_token_isValid = false;

    m_deployment_type_isSet = false;
    m_deployment_type_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_service_instance_name_isSet = false;
    m_service_instance_name_isValid = false;

    m_service_name_isSet = false;
    m_service_name_isValid = false;

    m_service_spec_isSet = false;
    m_service_spec_isValid = false;

    m_template_file_isSet = false;
    m_template_file_isValid = false;
}

void OAIUpdateComponentInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateComponentInput::fromJsonObject(QJsonObject json) {

    m_client_token_isValid = ::OpenAPI::fromJsonValue(m_client_token, json[QString("clientToken")]);
    m_client_token_isSet = !json[QString("clientToken")].isNull() && m_client_token_isValid;

    m_deployment_type_isValid = ::OpenAPI::fromJsonValue(m_deployment_type, json[QString("deploymentType")]);
    m_deployment_type_isSet = !json[QString("deploymentType")].isNull() && m_deployment_type_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_service_instance_name_isValid = ::OpenAPI::fromJsonValue(m_service_instance_name, json[QString("serviceInstanceName")]);
    m_service_instance_name_isSet = !json[QString("serviceInstanceName")].isNull() && m_service_instance_name_isValid;

    m_service_name_isValid = ::OpenAPI::fromJsonValue(m_service_name, json[QString("serviceName")]);
    m_service_name_isSet = !json[QString("serviceName")].isNull() && m_service_name_isValid;

    m_service_spec_isValid = ::OpenAPI::fromJsonValue(m_service_spec, json[QString("serviceSpec")]);
    m_service_spec_isSet = !json[QString("serviceSpec")].isNull() && m_service_spec_isValid;

    m_template_file_isValid = ::OpenAPI::fromJsonValue(m_template_file, json[QString("templateFile")]);
    m_template_file_isSet = !json[QString("templateFile")].isNull() && m_template_file_isValid;
}

QString OAIUpdateComponentInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateComponentInput::asJsonObject() const {
    QJsonObject obj;
    if (m_client_token_isSet) {
        obj.insert(QString("clientToken"), ::OpenAPI::toJsonValue(m_client_token));
    }
    if (m_deployment_type.isSet()) {
        obj.insert(QString("deploymentType"), ::OpenAPI::toJsonValue(m_deployment_type));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_service_instance_name_isSet) {
        obj.insert(QString("serviceInstanceName"), ::OpenAPI::toJsonValue(m_service_instance_name));
    }
    if (m_service_name_isSet) {
        obj.insert(QString("serviceName"), ::OpenAPI::toJsonValue(m_service_name));
    }
    if (m_service_spec_isSet) {
        obj.insert(QString("serviceSpec"), ::OpenAPI::toJsonValue(m_service_spec));
    }
    if (m_template_file_isSet) {
        obj.insert(QString("templateFile"), ::OpenAPI::toJsonValue(m_template_file));
    }
    return obj;
}

QString OAIUpdateComponentInput::getClientToken() const {
    return m_client_token;
}
void OAIUpdateComponentInput::setClientToken(const QString &client_token) {
    m_client_token = client_token;
    m_client_token_isSet = true;
}

bool OAIUpdateComponentInput::is_client_token_Set() const{
    return m_client_token_isSet;
}

bool OAIUpdateComponentInput::is_client_token_Valid() const{
    return m_client_token_isValid;
}

OAIComponentDeploymentUpdateType OAIUpdateComponentInput::getDeploymentType() const {
    return m_deployment_type;
}
void OAIUpdateComponentInput::setDeploymentType(const OAIComponentDeploymentUpdateType &deployment_type) {
    m_deployment_type = deployment_type;
    m_deployment_type_isSet = true;
}

bool OAIUpdateComponentInput::is_deployment_type_Set() const{
    return m_deployment_type_isSet;
}

bool OAIUpdateComponentInput::is_deployment_type_Valid() const{
    return m_deployment_type_isValid;
}

QString OAIUpdateComponentInput::getDescription() const {
    return m_description;
}
void OAIUpdateComponentInput::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIUpdateComponentInput::is_description_Set() const{
    return m_description_isSet;
}

bool OAIUpdateComponentInput::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIUpdateComponentInput::getName() const {
    return m_name;
}
void OAIUpdateComponentInput::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateComponentInput::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateComponentInput::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateComponentInput::getServiceInstanceName() const {
    return m_service_instance_name;
}
void OAIUpdateComponentInput::setServiceInstanceName(const QString &service_instance_name) {
    m_service_instance_name = service_instance_name;
    m_service_instance_name_isSet = true;
}

bool OAIUpdateComponentInput::is_service_instance_name_Set() const{
    return m_service_instance_name_isSet;
}

bool OAIUpdateComponentInput::is_service_instance_name_Valid() const{
    return m_service_instance_name_isValid;
}

QString OAIUpdateComponentInput::getServiceName() const {
    return m_service_name;
}
void OAIUpdateComponentInput::setServiceName(const QString &service_name) {
    m_service_name = service_name;
    m_service_name_isSet = true;
}

bool OAIUpdateComponentInput::is_service_name_Set() const{
    return m_service_name_isSet;
}

bool OAIUpdateComponentInput::is_service_name_Valid() const{
    return m_service_name_isValid;
}

QString OAIUpdateComponentInput::getServiceSpec() const {
    return m_service_spec;
}
void OAIUpdateComponentInput::setServiceSpec(const QString &service_spec) {
    m_service_spec = service_spec;
    m_service_spec_isSet = true;
}

bool OAIUpdateComponentInput::is_service_spec_Set() const{
    return m_service_spec_isSet;
}

bool OAIUpdateComponentInput::is_service_spec_Valid() const{
    return m_service_spec_isValid;
}

QString OAIUpdateComponentInput::getTemplateFile() const {
    return m_template_file;
}
void OAIUpdateComponentInput::setTemplateFile(const QString &template_file) {
    m_template_file = template_file;
    m_template_file_isSet = true;
}

bool OAIUpdateComponentInput::is_template_file_Set() const{
    return m_template_file_isSet;
}

bool OAIUpdateComponentInput::is_template_file_Valid() const{
    return m_template_file_isValid;
}

bool OAIUpdateComponentInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deployment_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

        if (m_service_spec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_file_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateComponentInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_deployment_type_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
