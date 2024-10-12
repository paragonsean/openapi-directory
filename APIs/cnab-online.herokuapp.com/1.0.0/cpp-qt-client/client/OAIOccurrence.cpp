/**
 * Cnab Online
 * Processe arquivos de retorno CNAB
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOccurrence.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOccurrence::OAIOccurrence(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOccurrence::OAIOccurrence() {
    this->initializeModel();
}

OAIOccurrence::~OAIOccurrence() {}

void OAIOccurrence::initializeModel() {

    m_attributes_isSet = false;
    m_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIOccurrence::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOccurrence::fromJsonObject(QJsonObject json) {

    m_attributes_isValid = ::OpenAPI::fromJsonValue(m_attributes, json[QString("attributes")]);
    m_attributes_isSet = !json[QString("attributes")].isNull() && m_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIOccurrence::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOccurrence::asJsonObject() const {
    QJsonObject obj;
    if (m_attributes.isSet()) {
        obj.insert(QString("attributes"), ::OpenAPI::toJsonValue(m_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIOccurrence_attributes OAIOccurrence::getAttributes() const {
    return m_attributes;
}
void OAIOccurrence::setAttributes(const OAIOccurrence_attributes &attributes) {
    m_attributes = attributes;
    m_attributes_isSet = true;
}

bool OAIOccurrence::is_attributes_Set() const{
    return m_attributes_isSet;
}

bool OAIOccurrence::is_attributes_Valid() const{
    return m_attributes_isValid;
}

qint32 OAIOccurrence::getId() const {
    return m_id;
}
void OAIOccurrence::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOccurrence::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOccurrence::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOccurrence::getType() const {
    return m_type;
}
void OAIOccurrence::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIOccurrence::is_type_Set() const{
    return m_type_isSet;
}

bool OAIOccurrence::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIOccurrence::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

bool OAIOccurrence::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
