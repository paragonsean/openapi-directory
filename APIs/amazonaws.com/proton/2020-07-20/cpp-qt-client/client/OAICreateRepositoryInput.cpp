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

#include "OAICreateRepositoryInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateRepositoryInput::OAICreateRepositoryInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateRepositoryInput::OAICreateRepositoryInput() {
    this->initializeModel();
}

OAICreateRepositoryInput::~OAICreateRepositoryInput() {}

void OAICreateRepositoryInput::initializeModel() {

    m_connection_arn_isSet = false;
    m_connection_arn_isValid = false;

    m_encryption_key_isSet = false;
    m_encryption_key_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_provider_isSet = false;
    m_provider_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAICreateRepositoryInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateRepositoryInput::fromJsonObject(QJsonObject json) {

    m_connection_arn_isValid = ::OpenAPI::fromJsonValue(m_connection_arn, json[QString("connectionArn")]);
    m_connection_arn_isSet = !json[QString("connectionArn")].isNull() && m_connection_arn_isValid;

    m_encryption_key_isValid = ::OpenAPI::fromJsonValue(m_encryption_key, json[QString("encryptionKey")]);
    m_encryption_key_isSet = !json[QString("encryptionKey")].isNull() && m_encryption_key_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_provider_isValid = ::OpenAPI::fromJsonValue(m_provider, json[QString("provider")]);
    m_provider_isSet = !json[QString("provider")].isNull() && m_provider_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAICreateRepositoryInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateRepositoryInput::asJsonObject() const {
    QJsonObject obj;
    if (m_connection_arn_isSet) {
        obj.insert(QString("connectionArn"), ::OpenAPI::toJsonValue(m_connection_arn));
    }
    if (m_encryption_key_isSet) {
        obj.insert(QString("encryptionKey"), ::OpenAPI::toJsonValue(m_encryption_key));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_provider.isSet()) {
        obj.insert(QString("provider"), ::OpenAPI::toJsonValue(m_provider));
    }
    if (m_tags.isSet()) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QString OAICreateRepositoryInput::getConnectionArn() const {
    return m_connection_arn;
}
void OAICreateRepositoryInput::setConnectionArn(const QString &connection_arn) {
    m_connection_arn = connection_arn;
    m_connection_arn_isSet = true;
}

bool OAICreateRepositoryInput::is_connection_arn_Set() const{
    return m_connection_arn_isSet;
}

bool OAICreateRepositoryInput::is_connection_arn_Valid() const{
    return m_connection_arn_isValid;
}

QString OAICreateRepositoryInput::getEncryptionKey() const {
    return m_encryption_key;
}
void OAICreateRepositoryInput::setEncryptionKey(const QString &encryption_key) {
    m_encryption_key = encryption_key;
    m_encryption_key_isSet = true;
}

bool OAICreateRepositoryInput::is_encryption_key_Set() const{
    return m_encryption_key_isSet;
}

bool OAICreateRepositoryInput::is_encryption_key_Valid() const{
    return m_encryption_key_isValid;
}

QString OAICreateRepositoryInput::getName() const {
    return m_name;
}
void OAICreateRepositoryInput::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateRepositoryInput::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateRepositoryInput::is_name_Valid() const{
    return m_name_isValid;
}

OAIRepositoryProvider OAICreateRepositoryInput::getProvider() const {
    return m_provider;
}
void OAICreateRepositoryInput::setProvider(const OAIRepositoryProvider &provider) {
    m_provider = provider;
    m_provider_isSet = true;
}

bool OAICreateRepositoryInput::is_provider_Set() const{
    return m_provider_isSet;
}

bool OAICreateRepositoryInput::is_provider_Valid() const{
    return m_provider_isValid;
}

QList OAICreateRepositoryInput::getTags() const {
    return m_tags;
}
void OAICreateRepositoryInput::setTags(const QList &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateRepositoryInput::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateRepositoryInput::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAICreateRepositoryInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_connection_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_encryption_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_provider.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateRepositoryInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_connection_arn_isValid && m_name_isValid && m_provider_isValid && true;
}

} // namespace OpenAPI
