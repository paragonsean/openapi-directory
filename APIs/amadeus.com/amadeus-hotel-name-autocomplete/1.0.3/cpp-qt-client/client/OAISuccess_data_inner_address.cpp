/**
 * Hotel Name Autocomplete
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISuccess_data_inner_address.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISuccess_data_inner_address::OAISuccess_data_inner_address(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISuccess_data_inner_address::OAISuccess_data_inner_address() {
    this->initializeModel();
}

OAISuccess_data_inner_address::~OAISuccess_data_inner_address() {}

void OAISuccess_data_inner_address::initializeModel() {

    m_city_name_isSet = false;
    m_city_name_isValid = false;

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_state_code_isSet = false;
    m_state_code_isValid = false;
}

void OAISuccess_data_inner_address::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISuccess_data_inner_address::fromJsonObject(QJsonObject json) {

    m_city_name_isValid = ::OpenAPI::fromJsonValue(m_city_name, json[QString("cityName")]);
    m_city_name_isSet = !json[QString("cityName")].isNull() && m_city_name_isValid;

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("countryCode")]);
    m_country_code_isSet = !json[QString("countryCode")].isNull() && m_country_code_isValid;

    m_state_code_isValid = ::OpenAPI::fromJsonValue(m_state_code, json[QString("stateCode")]);
    m_state_code_isSet = !json[QString("stateCode")].isNull() && m_state_code_isValid;
}

QString OAISuccess_data_inner_address::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISuccess_data_inner_address::asJsonObject() const {
    QJsonObject obj;
    if (m_city_name_isSet) {
        obj.insert(QString("cityName"), ::OpenAPI::toJsonValue(m_city_name));
    }
    if (m_country_code_isSet) {
        obj.insert(QString("countryCode"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_state_code_isSet) {
        obj.insert(QString("stateCode"), ::OpenAPI::toJsonValue(m_state_code));
    }
    return obj;
}

QString OAISuccess_data_inner_address::getCityName() const {
    return m_city_name;
}
void OAISuccess_data_inner_address::setCityName(const QString &city_name) {
    m_city_name = city_name;
    m_city_name_isSet = true;
}

bool OAISuccess_data_inner_address::is_city_name_Set() const{
    return m_city_name_isSet;
}

bool OAISuccess_data_inner_address::is_city_name_Valid() const{
    return m_city_name_isValid;
}

QString OAISuccess_data_inner_address::getCountryCode() const {
    return m_country_code;
}
void OAISuccess_data_inner_address::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAISuccess_data_inner_address::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAISuccess_data_inner_address::is_country_code_Valid() const{
    return m_country_code_isValid;
}

QString OAISuccess_data_inner_address::getStateCode() const {
    return m_state_code;
}
void OAISuccess_data_inner_address::setStateCode(const QString &state_code) {
    m_state_code = state_code;
    m_state_code_isSet = true;
}

bool OAISuccess_data_inner_address::is_state_code_Set() const{
    return m_state_code_isSet;
}

bool OAISuccess_data_inner_address::is_state_code_Valid() const{
    return m_state_code_isValid;
}

bool OAISuccess_data_inner_address::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISuccess_data_inner_address::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_city_name_isValid && m_country_code_isValid && true;
}

} // namespace OpenAPI
