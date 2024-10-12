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

#include "OAIFormOfIdentification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFormOfIdentification::OAIFormOfIdentification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFormOfIdentification::OAIFormOfIdentification() {
    this->initializeModel();
}

OAIFormOfIdentification::~OAIFormOfIdentification() {}

void OAIFormOfIdentification::initializeModel() {

    m_carrier_code_isSet = false;
    m_carrier_code_isValid = false;

    m_flight_offer_ids_isSet = false;
    m_flight_offer_ids_isValid = false;

    m_identification_type_isSet = false;
    m_identification_type_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_traveler_ids_isSet = false;
    m_traveler_ids_isValid = false;
}

void OAIFormOfIdentification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFormOfIdentification::fromJsonObject(QJsonObject json) {

    m_carrier_code_isValid = ::OpenAPI::fromJsonValue(m_carrier_code, json[QString("carrierCode")]);
    m_carrier_code_isSet = !json[QString("carrierCode")].isNull() && m_carrier_code_isValid;

    m_flight_offer_ids_isValid = ::OpenAPI::fromJsonValue(m_flight_offer_ids, json[QString("flightOfferIds")]);
    m_flight_offer_ids_isSet = !json[QString("flightOfferIds")].isNull() && m_flight_offer_ids_isValid;

    m_identification_type_isValid = ::OpenAPI::fromJsonValue(m_identification_type, json[QString("identificationType")]);
    m_identification_type_isSet = !json[QString("identificationType")].isNull() && m_identification_type_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_traveler_ids_isValid = ::OpenAPI::fromJsonValue(m_traveler_ids, json[QString("travelerIds")]);
    m_traveler_ids_isSet = !json[QString("travelerIds")].isNull() && m_traveler_ids_isValid;
}

QString OAIFormOfIdentification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFormOfIdentification::asJsonObject() const {
    QJsonObject obj;
    if (m_carrier_code_isSet) {
        obj.insert(QString("carrierCode"), ::OpenAPI::toJsonValue(m_carrier_code));
    }
    if (m_flight_offer_ids.size() > 0) {
        obj.insert(QString("flightOfferIds"), ::OpenAPI::toJsonValue(m_flight_offer_ids));
    }
    if (m_identification_type_isSet) {
        obj.insert(QString("identificationType"), ::OpenAPI::toJsonValue(m_identification_type));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_traveler_ids.size() > 0) {
        obj.insert(QString("travelerIds"), ::OpenAPI::toJsonValue(m_traveler_ids));
    }
    return obj;
}

QString OAIFormOfIdentification::getCarrierCode() const {
    return m_carrier_code;
}
void OAIFormOfIdentification::setCarrierCode(const QString &carrier_code) {
    m_carrier_code = carrier_code;
    m_carrier_code_isSet = true;
}

bool OAIFormOfIdentification::is_carrier_code_Set() const{
    return m_carrier_code_isSet;
}

bool OAIFormOfIdentification::is_carrier_code_Valid() const{
    return m_carrier_code_isValid;
}

QList<QString> OAIFormOfIdentification::getFlightOfferIds() const {
    return m_flight_offer_ids;
}
void OAIFormOfIdentification::setFlightOfferIds(const QList<QString> &flight_offer_ids) {
    m_flight_offer_ids = flight_offer_ids;
    m_flight_offer_ids_isSet = true;
}

bool OAIFormOfIdentification::is_flight_offer_ids_Set() const{
    return m_flight_offer_ids_isSet;
}

bool OAIFormOfIdentification::is_flight_offer_ids_Valid() const{
    return m_flight_offer_ids_isValid;
}

QString OAIFormOfIdentification::getIdentificationType() const {
    return m_identification_type;
}
void OAIFormOfIdentification::setIdentificationType(const QString &identification_type) {
    m_identification_type = identification_type;
    m_identification_type_isSet = true;
}

bool OAIFormOfIdentification::is_identification_type_Set() const{
    return m_identification_type_isSet;
}

bool OAIFormOfIdentification::is_identification_type_Valid() const{
    return m_identification_type_isValid;
}

QString OAIFormOfIdentification::getNumber() const {
    return m_number;
}
void OAIFormOfIdentification::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIFormOfIdentification::is_number_Set() const{
    return m_number_isSet;
}

bool OAIFormOfIdentification::is_number_Valid() const{
    return m_number_isValid;
}

QList<QString> OAIFormOfIdentification::getTravelerIds() const {
    return m_traveler_ids;
}
void OAIFormOfIdentification::setTravelerIds(const QList<QString> &traveler_ids) {
    m_traveler_ids = traveler_ids;
    m_traveler_ids_isSet = true;
}

bool OAIFormOfIdentification::is_traveler_ids_Set() const{
    return m_traveler_ids_isSet;
}

bool OAIFormOfIdentification::is_traveler_ids_Valid() const{
    return m_traveler_ids_isValid;
}

bool OAIFormOfIdentification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_carrier_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flight_offer_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_identification_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traveler_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFormOfIdentification::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
