/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStoreSecretResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStoreSecretResponse::OAIStoreSecretResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStoreSecretResponse::OAIStoreSecretResponse() {
    this->initializeModel();
}

OAIStoreSecretResponse::~OAIStoreSecretResponse() {}

void OAIStoreSecretResponse::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_secret_isSet = false;
    m_secret_isValid = false;

    m_tenant_id_isSet = false;
    m_tenant_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIStoreSecretResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStoreSecretResponse::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_secret_isValid = ::OpenAPI::fromJsonValue(m_secret, json[QString("secret")]);
    m_secret_isSet = !json[QString("secret")].isNull() && m_secret_isValid;

    m_tenant_id_isValid = ::OpenAPI::fromJsonValue(m_tenant_id, json[QString("tenant_id")]);
    m_tenant_id_isSet = !json[QString("tenant_id")].isNull() && m_tenant_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIStoreSecretResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStoreSecretResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_secret_isSet) {
        obj.insert(QString("secret"), ::OpenAPI::toJsonValue(m_secret));
    }
    if (m_tenant_id_isSet) {
        obj.insert(QString("tenant_id"), ::OpenAPI::toJsonValue(m_tenant_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIStoreSecretResponse::getId() const {
    return m_id;
}
void OAIStoreSecretResponse::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIStoreSecretResponse::is_id_Set() const{
    return m_id_isSet;
}

bool OAIStoreSecretResponse::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIStoreSecretResponse::getName() const {
    return m_name;
}
void OAIStoreSecretResponse::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStoreSecretResponse::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStoreSecretResponse::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIStoreSecretResponse::getSecret() const {
    return m_secret;
}
void OAIStoreSecretResponse::setSecret(const QString &secret) {
    m_secret = secret;
    m_secret_isSet = true;
}

bool OAIStoreSecretResponse::is_secret_Set() const{
    return m_secret_isSet;
}

bool OAIStoreSecretResponse::is_secret_Valid() const{
    return m_secret_isValid;
}

QString OAIStoreSecretResponse::getTenantId() const {
    return m_tenant_id;
}
void OAIStoreSecretResponse::setTenantId(const QString &tenant_id) {
    m_tenant_id = tenant_id;
    m_tenant_id_isSet = true;
}

bool OAIStoreSecretResponse::is_tenant_id_Set() const{
    return m_tenant_id_isSet;
}

bool OAIStoreSecretResponse::is_tenant_id_Valid() const{
    return m_tenant_id_isValid;
}

QString OAIStoreSecretResponse::getType() const {
    return m_type;
}
void OAIStoreSecretResponse::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIStoreSecretResponse::is_type_Set() const{
    return m_type_isSet;
}

bool OAIStoreSecretResponse::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIStoreSecretResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStoreSecretResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
