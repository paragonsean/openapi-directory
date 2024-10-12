/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOperatingFlight.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOperatingFlight::OAIOperatingFlight(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOperatingFlight::OAIOperatingFlight() {
    this->initializeModel();
}

OAIOperatingFlight::~OAIOperatingFlight() {}

void OAIOperatingFlight::initializeModel() {

    m_carrier_code_isSet = false;
    m_carrier_code_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;
}

void OAIOperatingFlight::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOperatingFlight::fromJsonObject(QJsonObject json) {

    m_carrier_code_isValid = ::OpenAPI::fromJsonValue(m_carrier_code, json[QString("carrierCode")]);
    m_carrier_code_isSet = !json[QString("carrierCode")].isNull() && m_carrier_code_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;
}

QString OAIOperatingFlight::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOperatingFlight::asJsonObject() const {
    QJsonObject obj;
    if (m_carrier_code_isSet) {
        obj.insert(QString("carrierCode"), ::OpenAPI::toJsonValue(m_carrier_code));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    return obj;
}

QString OAIOperatingFlight::getCarrierCode() const {
    return m_carrier_code;
}
void OAIOperatingFlight::setCarrierCode(const QString &carrier_code) {
    m_carrier_code = carrier_code;
    m_carrier_code_isSet = true;
}

bool OAIOperatingFlight::is_carrier_code_Set() const{
    return m_carrier_code_isSet;
}

bool OAIOperatingFlight::is_carrier_code_Valid() const{
    return m_carrier_code_isValid;
}

QString OAIOperatingFlight::getNumber() const {
    return m_number;
}
void OAIOperatingFlight::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIOperatingFlight::is_number_Set() const{
    return m_number_isSet;
}

bool OAIOperatingFlight::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIOperatingFlight::getSuffix() const {
    return m_suffix;
}
void OAIOperatingFlight::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAIOperatingFlight::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAIOperatingFlight::is_suffix_Valid() const{
    return m_suffix_isValid;
}

bool OAIOperatingFlight::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_carrier_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOperatingFlight::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
