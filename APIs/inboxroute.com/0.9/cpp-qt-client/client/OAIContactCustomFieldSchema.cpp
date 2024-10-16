/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContactCustomFieldSchema.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContactCustomFieldSchema::OAIContactCustomFieldSchema(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContactCustomFieldSchema::OAIContactCustomFieldSchema() {
    this->initializeModel();
}

OAIContactCustomFieldSchema::~OAIContactCustomFieldSchema() {}

void OAIContactCustomFieldSchema::initializeModel() {

    m_key_isSet = false;
    m_key_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_required_isSet = false;
    m_required_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIContactCustomFieldSchema::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContactCustomFieldSchema::fromJsonObject(QJsonObject json) {

    m_key_isValid = ::OpenAPI::fromJsonValue(m_key, json[QString("key")]);
    m_key_isSet = !json[QString("key")].isNull() && m_key_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_required_isValid = ::OpenAPI::fromJsonValue(m_required, json[QString("required")]);
    m_required_isSet = !json[QString("required")].isNull() && m_required_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIContactCustomFieldSchema::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContactCustomFieldSchema::asJsonObject() const {
    QJsonObject obj;
    if (m_key_isSet) {
        obj.insert(QString("key"), ::OpenAPI::toJsonValue(m_key));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_required_isSet) {
        obj.insert(QString("required"), ::OpenAPI::toJsonValue(m_required));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIContactCustomFieldSchema::getKey() const {
    return m_key;
}
void OAIContactCustomFieldSchema::setKey(const QString &key) {
    m_key = key;
    m_key_isSet = true;
}

bool OAIContactCustomFieldSchema::is_key_Set() const{
    return m_key_isSet;
}

bool OAIContactCustomFieldSchema::is_key_Valid() const{
    return m_key_isValid;
}

QString OAIContactCustomFieldSchema::getLabel() const {
    return m_label;
}
void OAIContactCustomFieldSchema::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIContactCustomFieldSchema::is_label_Set() const{
    return m_label_isSet;
}

bool OAIContactCustomFieldSchema::is_label_Valid() const{
    return m_label_isValid;
}

bool OAIContactCustomFieldSchema::isRequired() const {
    return m_required;
}
void OAIContactCustomFieldSchema::setRequired(const bool &required) {
    m_required = required;
    m_required_isSet = true;
}

bool OAIContactCustomFieldSchema::is_required_Set() const{
    return m_required_isSet;
}

bool OAIContactCustomFieldSchema::is_required_Valid() const{
    return m_required_isValid;
}

qint32 OAIContactCustomFieldSchema::getType() const {
    return m_type;
}
void OAIContactCustomFieldSchema::setType(const qint32 &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIContactCustomFieldSchema::is_type_Set() const{
    return m_type_isSet;
}

bool OAIContactCustomFieldSchema::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIContactCustomFieldSchema::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_isSet) {
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

bool OAIContactCustomFieldSchema::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_key_isValid && m_label_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
