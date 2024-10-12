/**
 * Flight Order Management
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDiscount.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiscount::OAIDiscount(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiscount::OAIDiscount() {
    this->initializeModel();
}

OAIDiscount::~OAIDiscount() {}

void OAIDiscount::initializeModel() {

    m_card_number_isSet = false;
    m_card_number_isValid = false;

    m_certificate_number_isSet = false;
    m_certificate_number_isValid = false;

    m_city_name_isSet = false;
    m_city_name_isValid = false;

    m_sub_type_isSet = false;
    m_sub_type_isValid = false;

    m_traveler_type_isSet = false;
    m_traveler_type_isValid = false;
}

void OAIDiscount::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiscount::fromJsonObject(QJsonObject json) {

    m_card_number_isValid = ::OpenAPI::fromJsonValue(m_card_number, json[QString("cardNumber")]);
    m_card_number_isSet = !json[QString("cardNumber")].isNull() && m_card_number_isValid;

    m_certificate_number_isValid = ::OpenAPI::fromJsonValue(m_certificate_number, json[QString("certificateNumber")]);
    m_certificate_number_isSet = !json[QString("certificateNumber")].isNull() && m_certificate_number_isValid;

    m_city_name_isValid = ::OpenAPI::fromJsonValue(m_city_name, json[QString("cityName")]);
    m_city_name_isSet = !json[QString("cityName")].isNull() && m_city_name_isValid;

    m_sub_type_isValid = ::OpenAPI::fromJsonValue(m_sub_type, json[QString("subType")]);
    m_sub_type_isSet = !json[QString("subType")].isNull() && m_sub_type_isValid;

    m_traveler_type_isValid = ::OpenAPI::fromJsonValue(m_traveler_type, json[QString("travelerType")]);
    m_traveler_type_isSet = !json[QString("travelerType")].isNull() && m_traveler_type_isValid;
}

QString OAIDiscount::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiscount::asJsonObject() const {
    QJsonObject obj;
    if (m_card_number_isSet) {
        obj.insert(QString("cardNumber"), ::OpenAPI::toJsonValue(m_card_number));
    }
    if (m_certificate_number_isSet) {
        obj.insert(QString("certificateNumber"), ::OpenAPI::toJsonValue(m_certificate_number));
    }
    if (m_city_name_isSet) {
        obj.insert(QString("cityName"), ::OpenAPI::toJsonValue(m_city_name));
    }
    if (m_sub_type.isSet()) {
        obj.insert(QString("subType"), ::OpenAPI::toJsonValue(m_sub_type));
    }
    if (m_traveler_type.isSet()) {
        obj.insert(QString("travelerType"), ::OpenAPI::toJsonValue(m_traveler_type));
    }
    return obj;
}

QString OAIDiscount::getCardNumber() const {
    return m_card_number;
}
void OAIDiscount::setCardNumber(const QString &card_number) {
    m_card_number = card_number;
    m_card_number_isSet = true;
}

bool OAIDiscount::is_card_number_Set() const{
    return m_card_number_isSet;
}

bool OAIDiscount::is_card_number_Valid() const{
    return m_card_number_isValid;
}

QString OAIDiscount::getCertificateNumber() const {
    return m_certificate_number;
}
void OAIDiscount::setCertificateNumber(const QString &certificate_number) {
    m_certificate_number = certificate_number;
    m_certificate_number_isSet = true;
}

bool OAIDiscount::is_certificate_number_Set() const{
    return m_certificate_number_isSet;
}

bool OAIDiscount::is_certificate_number_Valid() const{
    return m_certificate_number_isValid;
}

QString OAIDiscount::getCityName() const {
    return m_city_name;
}
void OAIDiscount::setCityName(const QString &city_name) {
    m_city_name = city_name;
    m_city_name_isSet = true;
}

bool OAIDiscount::is_city_name_Set() const{
    return m_city_name_isSet;
}

bool OAIDiscount::is_city_name_Valid() const{
    return m_city_name_isValid;
}

OAIDiscountType OAIDiscount::getSubType() const {
    return m_sub_type;
}
void OAIDiscount::setSubType(const OAIDiscountType &sub_type) {
    m_sub_type = sub_type;
    m_sub_type_isSet = true;
}

bool OAIDiscount::is_sub_type_Set() const{
    return m_sub_type_isSet;
}

bool OAIDiscount::is_sub_type_Valid() const{
    return m_sub_type_isValid;
}

OAIDiscountTravelerType OAIDiscount::getTravelerType() const {
    return m_traveler_type;
}
void OAIDiscount::setTravelerType(const OAIDiscountTravelerType &traveler_type) {
    m_traveler_type = traveler_type;
    m_traveler_type_isSet = true;
}

bool OAIDiscount::is_traveler_type_Set() const{
    return m_traveler_type_isSet;
}

bool OAIDiscount::is_traveler_type_Valid() const{
    return m_traveler_type_isValid;
}

bool OAIDiscount::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_card_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_certificate_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_traveler_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiscount::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
