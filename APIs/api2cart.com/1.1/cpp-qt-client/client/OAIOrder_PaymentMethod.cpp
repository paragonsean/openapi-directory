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

#include "OAIOrder_PaymentMethod.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrder_PaymentMethod::OAIOrder_PaymentMethod(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrder_PaymentMethod::OAIOrder_PaymentMethod() {
    this->initializeModel();
}

OAIOrder_PaymentMethod::~OAIOrder_PaymentMethod() {}

void OAIOrder_PaymentMethod::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIOrder_PaymentMethod::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrder_PaymentMethod::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIOrder_PaymentMethod::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrder_PaymentMethod::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

OAIObject OAIOrder_PaymentMethod::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIOrder_PaymentMethod::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIOrder_PaymentMethod::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIOrder_PaymentMethod::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

OAIObject OAIOrder_PaymentMethod::getCustomFields() const {
    return m_custom_fields;
}
void OAIOrder_PaymentMethod::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIOrder_PaymentMethod::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIOrder_PaymentMethod::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIOrder_PaymentMethod::getName() const {
    return m_name;
}
void OAIOrder_PaymentMethod::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrder_PaymentMethod::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrder_PaymentMethod::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIOrder_PaymentMethod::isSet() const {
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

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrder_PaymentMethod::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
