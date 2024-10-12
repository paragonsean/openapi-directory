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

#include "OAICountry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICountry::OAICountry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICountry::OAICountry() {
    this->initializeModel();
}

OAICountry::~OAICountry() {}

void OAICountry::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_code2_isSet = false;
    m_code2_isValid = false;

    m_code3_isSet = false;
    m_code3_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAICountry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICountry::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_code2_isValid = ::OpenAPI::fromJsonValue(m_code2, json[QString("code2")]);
    m_code2_isSet = !json[QString("code2")].isNull() && m_code2_isValid;

    m_code3_isValid = ::OpenAPI::fromJsonValue(m_code3, json[QString("code3")]);
    m_code3_isSet = !json[QString("code3")].isNull() && m_code3_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAICountry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICountry::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_code2_isSet) {
        obj.insert(QString("code2"), ::OpenAPI::toJsonValue(m_code2));
    }
    if (m_code3_isSet) {
        obj.insert(QString("code3"), ::OpenAPI::toJsonValue(m_code3));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

OAIObject OAICountry::getAdditionalFields() const {
    return m_additional_fields;
}
void OAICountry::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAICountry::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAICountry::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

QString OAICountry::getCode2() const {
    return m_code2;
}
void OAICountry::setCode2(const QString &code2) {
    m_code2 = code2;
    m_code2_isSet = true;
}

bool OAICountry::is_code2_Set() const{
    return m_code2_isSet;
}

bool OAICountry::is_code2_Valid() const{
    return m_code2_isValid;
}

QString OAICountry::getCode3() const {
    return m_code3;
}
void OAICountry::setCode3(const QString &code3) {
    m_code3 = code3;
    m_code3_isSet = true;
}

bool OAICountry::is_code3_Set() const{
    return m_code3_isSet;
}

bool OAICountry::is_code3_Valid() const{
    return m_code3_isValid;
}

OAIObject OAICountry::getCustomFields() const {
    return m_custom_fields;
}
void OAICountry::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAICountry::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAICountry::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAICountry::getName() const {
    return m_name;
}
void OAICountry::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICountry::is_name_Set() const{
    return m_name_isSet;
}

bool OAICountry::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICountry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
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

bool OAICountry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
