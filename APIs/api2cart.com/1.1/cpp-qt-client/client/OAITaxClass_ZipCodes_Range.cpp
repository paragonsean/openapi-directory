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

#include "OAITaxClass_ZipCodes_Range.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITaxClass_ZipCodes_Range::OAITaxClass_ZipCodes_Range(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITaxClass_ZipCodes_Range::OAITaxClass_ZipCodes_Range() {
    this->initializeModel();
}

OAITaxClass_ZipCodes_Range::~OAITaxClass_ZipCodes_Range() {}

void OAITaxClass_ZipCodes_Range::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_from_isSet = false;
    m_from_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;
}

void OAITaxClass_ZipCodes_Range::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITaxClass_ZipCodes_Range::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_from_isValid = ::OpenAPI::fromJsonValue(m_from, json[QString("from")]);
    m_from_isSet = !json[QString("from")].isNull() && m_from_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;
}

QString OAITaxClass_ZipCodes_Range::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITaxClass_ZipCodes_Range::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_from_isSet) {
        obj.insert(QString("from"), ::OpenAPI::toJsonValue(m_from));
    }
    if (m_to_isSet) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    return obj;
}

OAIObject OAITaxClass_ZipCodes_Range::getAdditionalFields() const {
    return m_additional_fields;
}
void OAITaxClass_ZipCodes_Range::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAITaxClass_ZipCodes_Range::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAITaxClass_ZipCodes_Range::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

OAIObject OAITaxClass_ZipCodes_Range::getCustomFields() const {
    return m_custom_fields;
}
void OAITaxClass_ZipCodes_Range::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAITaxClass_ZipCodes_Range::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAITaxClass_ZipCodes_Range::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAITaxClass_ZipCodes_Range::getFrom() const {
    return m_from;
}
void OAITaxClass_ZipCodes_Range::setFrom(const QString &from) {
    m_from = from;
    m_from_isSet = true;
}

bool OAITaxClass_ZipCodes_Range::is_from_Set() const{
    return m_from_isSet;
}

bool OAITaxClass_ZipCodes_Range::is_from_Valid() const{
    return m_from_isValid;
}

QString OAITaxClass_ZipCodes_Range::getTo() const {
    return m_to;
}
void OAITaxClass_ZipCodes_Range::setTo(const QString &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAITaxClass_ZipCodes_Range::is_to_Set() const{
    return m_to_isSet;
}

bool OAITaxClass_ZipCodes_Range::is_to_Valid() const{
    return m_to_isValid;
}

bool OAITaxClass_ZipCodes_Range::isSet() const {
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

        if (m_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITaxClass_ZipCodes_Range::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
