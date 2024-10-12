/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProduct_Review_Rating.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProduct_Review_Rating::OAIProduct_Review_Rating(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProduct_Review_Rating::OAIProduct_Review_Rating() {
    this->initializeModel();
}

OAIProduct_Review_Rating::~OAIProduct_Review_Rating() {}

void OAIProduct_Review_Rating::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIProduct_Review_Rating::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProduct_Review_Rating::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIProduct_Review_Rating::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProduct_Review_Rating::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

OAIObject OAIProduct_Review_Rating::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIProduct_Review_Rating::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIProduct_Review_Rating::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIProduct_Review_Rating::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

OAIObject OAIProduct_Review_Rating::getCustomFields() const {
    return m_custom_fields;
}
void OAIProduct_Review_Rating::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIProduct_Review_Rating::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIProduct_Review_Rating::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIProduct_Review_Rating::getId() const {
    return m_id;
}
void OAIProduct_Review_Rating::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProduct_Review_Rating::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProduct_Review_Rating::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProduct_Review_Rating::getName() const {
    return m_name;
}
void OAIProduct_Review_Rating::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProduct_Review_Rating::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProduct_Review_Rating::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIProduct_Review_Rating::getValue() const {
    return m_value;
}
void OAIProduct_Review_Rating::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIProduct_Review_Rating::is_value_Set() const{
    return m_value_isSet;
}

bool OAIProduct_Review_Rating::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIProduct_Review_Rating::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
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

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProduct_Review_Rating::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
