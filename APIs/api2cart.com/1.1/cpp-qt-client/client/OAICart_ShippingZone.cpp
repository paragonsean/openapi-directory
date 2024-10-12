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

#include "OAICart_ShippingZone.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICart_ShippingZone::OAICart_ShippingZone(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICart_ShippingZone::OAICart_ShippingZone() {
    this->initializeModel();
}

OAICart_ShippingZone::~OAICart_ShippingZone() {}

void OAICart_ShippingZone::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_country_iso2_codes_isSet = false;
    m_country_iso2_codes_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAICart_ShippingZone::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICart_ShippingZone::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_country_iso2_codes_isValid = ::OpenAPI::fromJsonValue(m_country_iso2_codes, json[QString("country_iso2_codes")]);
    m_country_iso2_codes_isSet = !json[QString("country_iso2_codes")].isNull() && m_country_iso2_codes_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAICart_ShippingZone::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICart_ShippingZone::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_country_iso2_codes.size() > 0) {
        obj.insert(QString("country_iso2_codes"), ::OpenAPI::toJsonValue(m_country_iso2_codes));
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
    return obj;
}

OAIObject OAICart_ShippingZone::getAdditionalFields() const {
    return m_additional_fields;
}
void OAICart_ShippingZone::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAICart_ShippingZone::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAICart_ShippingZone::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

QString OAICart_ShippingZone::getCode() const {
    return m_code;
}
void OAICart_ShippingZone::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAICart_ShippingZone::is_code_Set() const{
    return m_code_isSet;
}

bool OAICart_ShippingZone::is_code_Valid() const{
    return m_code_isValid;
}

QString OAICart_ShippingZone::getCountry() const {
    return m_country;
}
void OAICart_ShippingZone::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICart_ShippingZone::is_country_Set() const{
    return m_country_isSet;
}

bool OAICart_ShippingZone::is_country_Valid() const{
    return m_country_isValid;
}

QList<QString> OAICart_ShippingZone::getCountryIso2Codes() const {
    return m_country_iso2_codes;
}
void OAICart_ShippingZone::setCountryIso2Codes(const QList<QString> &country_iso2_codes) {
    m_country_iso2_codes = country_iso2_codes;
    m_country_iso2_codes_isSet = true;
}

bool OAICart_ShippingZone::is_country_iso2_codes_Set() const{
    return m_country_iso2_codes_isSet;
}

bool OAICart_ShippingZone::is_country_iso2_codes_Valid() const{
    return m_country_iso2_codes_isValid;
}

OAIObject OAICart_ShippingZone::getCustomFields() const {
    return m_custom_fields;
}
void OAICart_ShippingZone::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAICart_ShippingZone::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAICart_ShippingZone::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAICart_ShippingZone::getId() const {
    return m_id;
}
void OAICart_ShippingZone::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICart_ShippingZone::is_id_Set() const{
    return m_id_isSet;
}

bool OAICart_ShippingZone::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICart_ShippingZone::getName() const {
    return m_name;
}
void OAICart_ShippingZone::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICart_ShippingZone::is_name_Set() const{
    return m_name_isSet;
}

bool OAICart_ShippingZone::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICart_ShippingZone::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_iso2_codes.size() > 0) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAICart_ShippingZone::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
