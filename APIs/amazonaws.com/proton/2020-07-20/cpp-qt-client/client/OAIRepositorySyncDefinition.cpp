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

#include "OAIRepositorySyncDefinition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRepositorySyncDefinition::OAIRepositorySyncDefinition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRepositorySyncDefinition::OAIRepositorySyncDefinition() {
    this->initializeModel();
}

OAIRepositorySyncDefinition::~OAIRepositorySyncDefinition() {}

void OAIRepositorySyncDefinition::initializeModel() {

    m_branch_isSet = false;
    m_branch_isValid = false;

    m_directory_isSet = false;
    m_directory_isValid = false;

    m_parent_isSet = false;
    m_parent_isValid = false;

    m_target_isSet = false;
    m_target_isValid = false;
}

void OAIRepositorySyncDefinition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRepositorySyncDefinition::fromJsonObject(QJsonObject json) {

    m_branch_isValid = ::OpenAPI::fromJsonValue(m_branch, json[QString("branch")]);
    m_branch_isSet = !json[QString("branch")].isNull() && m_branch_isValid;

    m_directory_isValid = ::OpenAPI::fromJsonValue(m_directory, json[QString("directory")]);
    m_directory_isSet = !json[QString("directory")].isNull() && m_directory_isValid;

    m_parent_isValid = ::OpenAPI::fromJsonValue(m_parent, json[QString("parent")]);
    m_parent_isSet = !json[QString("parent")].isNull() && m_parent_isValid;

    m_target_isValid = ::OpenAPI::fromJsonValue(m_target, json[QString("target")]);
    m_target_isSet = !json[QString("target")].isNull() && m_target_isValid;
}

QString OAIRepositorySyncDefinition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRepositorySyncDefinition::asJsonObject() const {
    QJsonObject obj;
    if (m_branch_isSet) {
        obj.insert(QString("branch"), ::OpenAPI::toJsonValue(m_branch));
    }
    if (m_directory_isSet) {
        obj.insert(QString("directory"), ::OpenAPI::toJsonValue(m_directory));
    }
    if (m_parent_isSet) {
        obj.insert(QString("parent"), ::OpenAPI::toJsonValue(m_parent));
    }
    if (m_target_isSet) {
        obj.insert(QString("target"), ::OpenAPI::toJsonValue(m_target));
    }
    return obj;
}

QString OAIRepositorySyncDefinition::getBranch() const {
    return m_branch;
}
void OAIRepositorySyncDefinition::setBranch(const QString &branch) {
    m_branch = branch;
    m_branch_isSet = true;
}

bool OAIRepositorySyncDefinition::is_branch_Set() const{
    return m_branch_isSet;
}

bool OAIRepositorySyncDefinition::is_branch_Valid() const{
    return m_branch_isValid;
}

QString OAIRepositorySyncDefinition::getDirectory() const {
    return m_directory;
}
void OAIRepositorySyncDefinition::setDirectory(const QString &directory) {
    m_directory = directory;
    m_directory_isSet = true;
}

bool OAIRepositorySyncDefinition::is_directory_Set() const{
    return m_directory_isSet;
}

bool OAIRepositorySyncDefinition::is_directory_Valid() const{
    return m_directory_isValid;
}

QString OAIRepositorySyncDefinition::getParent() const {
    return m_parent;
}
void OAIRepositorySyncDefinition::setParent(const QString &parent) {
    m_parent = parent;
    m_parent_isSet = true;
}

bool OAIRepositorySyncDefinition::is_parent_Set() const{
    return m_parent_isSet;
}

bool OAIRepositorySyncDefinition::is_parent_Valid() const{
    return m_parent_isValid;
}

QString OAIRepositorySyncDefinition::getTarget() const {
    return m_target;
}
void OAIRepositorySyncDefinition::setTarget(const QString &target) {
    m_target = target;
    m_target_isSet = true;
}

bool OAIRepositorySyncDefinition::is_target_Set() const{
    return m_target_isSet;
}

bool OAIRepositorySyncDefinition::is_target_Valid() const{
    return m_target_isValid;
}

bool OAIRepositorySyncDefinition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_branch_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_directory_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRepositorySyncDefinition::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_branch_isValid && m_directory_isValid && m_parent_isValid && m_target_isValid && true;
}

} // namespace OpenAPI
