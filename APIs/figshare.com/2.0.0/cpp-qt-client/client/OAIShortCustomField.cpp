/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShortCustomField.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShortCustomField::OAIShortCustomField(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShortCustomField::OAIShortCustomField() {
    this->initializeModel();
}

OAIShortCustomField::~OAIShortCustomField() {}

void OAIShortCustomField::initializeModel() {

    m_field_type_isSet = false;
    m_field_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIShortCustomField::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShortCustomField::fromJsonObject(QJsonObject json) {

    m_field_type_isValid = ::OpenAPI::fromJsonValue(m_field_type, json[QString("field_type")]);
    m_field_type_isSet = !json[QString("field_type")].isNull() && m_field_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIShortCustomField::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShortCustomField::asJsonObject() const {
    QJsonObject obj;
    if (m_field_type_isSet) {
        obj.insert(QString("field_type"), ::OpenAPI::toJsonValue(m_field_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIShortCustomField::getFieldType() const {
    return m_field_type;
}
void OAIShortCustomField::setFieldType(const QString &field_type) {
    m_field_type = field_type;
    m_field_type_isSet = true;
}

bool OAIShortCustomField::is_field_type_Set() const{
    return m_field_type_isSet;
}

bool OAIShortCustomField::is_field_type_Valid() const{
    return m_field_type_isValid;
}

qint64 OAIShortCustomField::getId() const {
    return m_id;
}
void OAIShortCustomField::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShortCustomField::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShortCustomField::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIShortCustomField::getName() const {
    return m_name;
}
void OAIShortCustomField::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShortCustomField::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShortCustomField::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIShortCustomField::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_field_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShortCustomField::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_field_type_isValid && m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
