/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICredentialRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICredentialRepresentation::OAICredentialRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICredentialRepresentation::OAICredentialRepresentation() {
    this->initializeModel();
}

OAICredentialRepresentation::~OAICredentialRepresentation() {}

void OAICredentialRepresentation::initializeModel() {

    m_created_date_isSet = false;
    m_created_date_isValid = false;

    m_credential_data_isSet = false;
    m_credential_data_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;

    m_secret_data_isSet = false;
    m_secret_data_isValid = false;

    m_temporary_isSet = false;
    m_temporary_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_label_isSet = false;
    m_user_label_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAICredentialRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICredentialRepresentation::fromJsonObject(QJsonObject json) {

    m_created_date_isValid = ::OpenAPI::fromJsonValue(m_created_date, json[QString("createdDate")]);
    m_created_date_isSet = !json[QString("createdDate")].isNull() && m_created_date_isValid;

    m_credential_data_isValid = ::OpenAPI::fromJsonValue(m_credential_data, json[QString("credentialData")]);
    m_credential_data_isSet = !json[QString("credentialData")].isNull() && m_credential_data_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;

    m_secret_data_isValid = ::OpenAPI::fromJsonValue(m_secret_data, json[QString("secretData")]);
    m_secret_data_isSet = !json[QString("secretData")].isNull() && m_secret_data_isValid;

    m_temporary_isValid = ::OpenAPI::fromJsonValue(m_temporary, json[QString("temporary")]);
    m_temporary_isSet = !json[QString("temporary")].isNull() && m_temporary_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_label_isValid = ::OpenAPI::fromJsonValue(m_user_label, json[QString("userLabel")]);
    m_user_label_isSet = !json[QString("userLabel")].isNull() && m_user_label_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAICredentialRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICredentialRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_created_date_isSet) {
        obj.insert(QString("createdDate"), ::OpenAPI::toJsonValue(m_created_date));
    }
    if (m_credential_data_isSet) {
        obj.insert(QString("credentialData"), ::OpenAPI::toJsonValue(m_credential_data));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    if (m_secret_data_isSet) {
        obj.insert(QString("secretData"), ::OpenAPI::toJsonValue(m_secret_data));
    }
    if (m_temporary_isSet) {
        obj.insert(QString("temporary"), ::OpenAPI::toJsonValue(m_temporary));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_label_isSet) {
        obj.insert(QString("userLabel"), ::OpenAPI::toJsonValue(m_user_label));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

qint64 OAICredentialRepresentation::getCreatedDate() const {
    return m_created_date;
}
void OAICredentialRepresentation::setCreatedDate(const qint64 &created_date) {
    m_created_date = created_date;
    m_created_date_isSet = true;
}

bool OAICredentialRepresentation::is_created_date_Set() const{
    return m_created_date_isSet;
}

bool OAICredentialRepresentation::is_created_date_Valid() const{
    return m_created_date_isValid;
}

QString OAICredentialRepresentation::getCredentialData() const {
    return m_credential_data;
}
void OAICredentialRepresentation::setCredentialData(const QString &credential_data) {
    m_credential_data = credential_data;
    m_credential_data_isSet = true;
}

bool OAICredentialRepresentation::is_credential_data_Set() const{
    return m_credential_data_isSet;
}

bool OAICredentialRepresentation::is_credential_data_Valid() const{
    return m_credential_data_isValid;
}

QString OAICredentialRepresentation::getId() const {
    return m_id;
}
void OAICredentialRepresentation::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICredentialRepresentation::is_id_Set() const{
    return m_id_isSet;
}

bool OAICredentialRepresentation::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAICredentialRepresentation::getPriority() const {
    return m_priority;
}
void OAICredentialRepresentation::setPriority(const qint32 &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAICredentialRepresentation::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAICredentialRepresentation::is_priority_Valid() const{
    return m_priority_isValid;
}

QString OAICredentialRepresentation::getSecretData() const {
    return m_secret_data;
}
void OAICredentialRepresentation::setSecretData(const QString &secret_data) {
    m_secret_data = secret_data;
    m_secret_data_isSet = true;
}

bool OAICredentialRepresentation::is_secret_data_Set() const{
    return m_secret_data_isSet;
}

bool OAICredentialRepresentation::is_secret_data_Valid() const{
    return m_secret_data_isValid;
}

bool OAICredentialRepresentation::isTemporary() const {
    return m_temporary;
}
void OAICredentialRepresentation::setTemporary(const bool &temporary) {
    m_temporary = temporary;
    m_temporary_isSet = true;
}

bool OAICredentialRepresentation::is_temporary_Set() const{
    return m_temporary_isSet;
}

bool OAICredentialRepresentation::is_temporary_Valid() const{
    return m_temporary_isValid;
}

QString OAICredentialRepresentation::getType() const {
    return m_type;
}
void OAICredentialRepresentation::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICredentialRepresentation::is_type_Set() const{
    return m_type_isSet;
}

bool OAICredentialRepresentation::is_type_Valid() const{
    return m_type_isValid;
}

QString OAICredentialRepresentation::getUserLabel() const {
    return m_user_label;
}
void OAICredentialRepresentation::setUserLabel(const QString &user_label) {
    m_user_label = user_label;
    m_user_label_isSet = true;
}

bool OAICredentialRepresentation::is_user_label_Set() const{
    return m_user_label_isSet;
}

bool OAICredentialRepresentation::is_user_label_Valid() const{
    return m_user_label_isValid;
}

QString OAICredentialRepresentation::getValue() const {
    return m_value;
}
void OAICredentialRepresentation::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAICredentialRepresentation::is_value_Set() const{
    return m_value_isSet;
}

bool OAICredentialRepresentation::is_value_Valid() const{
    return m_value_isValid;
}

bool OAICredentialRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credential_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secret_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_temporary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICredentialRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
