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

#include "OAISyncBlocker.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISyncBlocker::OAISyncBlocker(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISyncBlocker::OAISyncBlocker() {
    this->initializeModel();
}

OAISyncBlocker::~OAISyncBlocker() {}

void OAISyncBlocker::initializeModel() {

    m_contexts_isSet = false;
    m_contexts_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_reason_isSet = false;
    m_created_reason_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_resolved_at_isSet = false;
    m_resolved_at_isValid = false;

    m_resolved_reason_isSet = false;
    m_resolved_reason_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAISyncBlocker::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISyncBlocker::fromJsonObject(QJsonObject json) {

    m_contexts_isValid = ::OpenAPI::fromJsonValue(m_contexts, json[QString("contexts")]);
    m_contexts_isSet = !json[QString("contexts")].isNull() && m_contexts_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("createdAt")]);
    m_created_at_isSet = !json[QString("createdAt")].isNull() && m_created_at_isValid;

    m_created_reason_isValid = ::OpenAPI::fromJsonValue(m_created_reason, json[QString("createdReason")]);
    m_created_reason_isSet = !json[QString("createdReason")].isNull() && m_created_reason_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_resolved_at_isValid = ::OpenAPI::fromJsonValue(m_resolved_at, json[QString("resolvedAt")]);
    m_resolved_at_isSet = !json[QString("resolvedAt")].isNull() && m_resolved_at_isValid;

    m_resolved_reason_isValid = ::OpenAPI::fromJsonValue(m_resolved_reason, json[QString("resolvedReason")]);
    m_resolved_reason_isSet = !json[QString("resolvedReason")].isNull() && m_resolved_reason_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAISyncBlocker::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISyncBlocker::asJsonObject() const {
    QJsonObject obj;
    if (m_contexts.isSet()) {
        obj.insert(QString("contexts"), ::OpenAPI::toJsonValue(m_contexts));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("createdAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_reason_isSet) {
        obj.insert(QString("createdReason"), ::OpenAPI::toJsonValue(m_created_reason));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_resolved_at_isSet) {
        obj.insert(QString("resolvedAt"), ::OpenAPI::toJsonValue(m_resolved_at));
    }
    if (m_resolved_reason_isSet) {
        obj.insert(QString("resolvedReason"), ::OpenAPI::toJsonValue(m_resolved_reason));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList OAISyncBlocker::getContexts() const {
    return m_contexts;
}
void OAISyncBlocker::setContexts(const QList &contexts) {
    m_contexts = contexts;
    m_contexts_isSet = true;
}

bool OAISyncBlocker::is_contexts_Set() const{
    return m_contexts_isSet;
}

bool OAISyncBlocker::is_contexts_Valid() const{
    return m_contexts_isValid;
}

QDateTime OAISyncBlocker::getCreatedAt() const {
    return m_created_at;
}
void OAISyncBlocker::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAISyncBlocker::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAISyncBlocker::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAISyncBlocker::getCreatedReason() const {
    return m_created_reason;
}
void OAISyncBlocker::setCreatedReason(const QString &created_reason) {
    m_created_reason = created_reason;
    m_created_reason_isSet = true;
}

bool OAISyncBlocker::is_created_reason_Set() const{
    return m_created_reason_isSet;
}

bool OAISyncBlocker::is_created_reason_Valid() const{
    return m_created_reason_isValid;
}

QString OAISyncBlocker::getId() const {
    return m_id;
}
void OAISyncBlocker::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISyncBlocker::is_id_Set() const{
    return m_id_isSet;
}

bool OAISyncBlocker::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAISyncBlocker::getResolvedAt() const {
    return m_resolved_at;
}
void OAISyncBlocker::setResolvedAt(const QDateTime &resolved_at) {
    m_resolved_at = resolved_at;
    m_resolved_at_isSet = true;
}

bool OAISyncBlocker::is_resolved_at_Set() const{
    return m_resolved_at_isSet;
}

bool OAISyncBlocker::is_resolved_at_Valid() const{
    return m_resolved_at_isValid;
}

QString OAISyncBlocker::getResolvedReason() const {
    return m_resolved_reason;
}
void OAISyncBlocker::setResolvedReason(const QString &resolved_reason) {
    m_resolved_reason = resolved_reason;
    m_resolved_reason_isSet = true;
}

bool OAISyncBlocker::is_resolved_reason_Set() const{
    return m_resolved_reason_isSet;
}

bool OAISyncBlocker::is_resolved_reason_Valid() const{
    return m_resolved_reason_isValid;
}

OAIBlockerStatus OAISyncBlocker::getStatus() const {
    return m_status;
}
void OAISyncBlocker::setStatus(const OAIBlockerStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISyncBlocker::is_status_Set() const{
    return m_status_isSet;
}

bool OAISyncBlocker::is_status_Valid() const{
    return m_status_isValid;
}

OAIBlockerType OAISyncBlocker::getType() const {
    return m_type;
}
void OAISyncBlocker::setType(const OAIBlockerType &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISyncBlocker::is_type_Set() const{
    return m_type_isSet;
}

bool OAISyncBlocker::is_type_Valid() const{
    return m_type_isValid;
}

bool OAISyncBlocker::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contexts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolved_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolved_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISyncBlocker::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_created_at_isValid && m_created_reason_isValid && m_id_isValid && m_status_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
