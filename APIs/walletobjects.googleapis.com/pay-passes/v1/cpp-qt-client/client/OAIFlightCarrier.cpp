/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlightCarrier.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightCarrier::OAIFlightCarrier(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightCarrier::OAIFlightCarrier() {
    this->initializeModel();
}

OAIFlightCarrier::~OAIFlightCarrier() {}

void OAIFlightCarrier::initializeModel() {

    m_airline_alliance_logo_isSet = false;
    m_airline_alliance_logo_isValid = false;

    m_airline_logo_isSet = false;
    m_airline_logo_isValid = false;

    m_airline_name_isSet = false;
    m_airline_name_isValid = false;

    m_carrier_iata_code_isSet = false;
    m_carrier_iata_code_isValid = false;

    m_carrier_icao_code_isSet = false;
    m_carrier_icao_code_isValid = false;

    m_kind_isSet = false;
    m_kind_isValid = false;
}

void OAIFlightCarrier::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightCarrier::fromJsonObject(QJsonObject json) {

    m_airline_alliance_logo_isValid = ::OpenAPI::fromJsonValue(m_airline_alliance_logo, json[QString("airlineAllianceLogo")]);
    m_airline_alliance_logo_isSet = !json[QString("airlineAllianceLogo")].isNull() && m_airline_alliance_logo_isValid;

    m_airline_logo_isValid = ::OpenAPI::fromJsonValue(m_airline_logo, json[QString("airlineLogo")]);
    m_airline_logo_isSet = !json[QString("airlineLogo")].isNull() && m_airline_logo_isValid;

    m_airline_name_isValid = ::OpenAPI::fromJsonValue(m_airline_name, json[QString("airlineName")]);
    m_airline_name_isSet = !json[QString("airlineName")].isNull() && m_airline_name_isValid;

    m_carrier_iata_code_isValid = ::OpenAPI::fromJsonValue(m_carrier_iata_code, json[QString("carrierIataCode")]);
    m_carrier_iata_code_isSet = !json[QString("carrierIataCode")].isNull() && m_carrier_iata_code_isValid;

    m_carrier_icao_code_isValid = ::OpenAPI::fromJsonValue(m_carrier_icao_code, json[QString("carrierIcaoCode")]);
    m_carrier_icao_code_isSet = !json[QString("carrierIcaoCode")].isNull() && m_carrier_icao_code_isValid;

    m_kind_isValid = ::OpenAPI::fromJsonValue(m_kind, json[QString("kind")]);
    m_kind_isSet = !json[QString("kind")].isNull() && m_kind_isValid;
}

QString OAIFlightCarrier::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightCarrier::asJsonObject() const {
    QJsonObject obj;
    if (m_airline_alliance_logo.isSet()) {
        obj.insert(QString("airlineAllianceLogo"), ::OpenAPI::toJsonValue(m_airline_alliance_logo));
    }
    if (m_airline_logo.isSet()) {
        obj.insert(QString("airlineLogo"), ::OpenAPI::toJsonValue(m_airline_logo));
    }
    if (m_airline_name.isSet()) {
        obj.insert(QString("airlineName"), ::OpenAPI::toJsonValue(m_airline_name));
    }
    if (m_carrier_iata_code_isSet) {
        obj.insert(QString("carrierIataCode"), ::OpenAPI::toJsonValue(m_carrier_iata_code));
    }
    if (m_carrier_icao_code_isSet) {
        obj.insert(QString("carrierIcaoCode"), ::OpenAPI::toJsonValue(m_carrier_icao_code));
    }
    if (m_kind_isSet) {
        obj.insert(QString("kind"), ::OpenAPI::toJsonValue(m_kind));
    }
    return obj;
}

OAIImage OAIFlightCarrier::getAirlineAllianceLogo() const {
    return m_airline_alliance_logo;
}
void OAIFlightCarrier::setAirlineAllianceLogo(const OAIImage &airline_alliance_logo) {
    m_airline_alliance_logo = airline_alliance_logo;
    m_airline_alliance_logo_isSet = true;
}

bool OAIFlightCarrier::is_airline_alliance_logo_Set() const{
    return m_airline_alliance_logo_isSet;
}

bool OAIFlightCarrier::is_airline_alliance_logo_Valid() const{
    return m_airline_alliance_logo_isValid;
}

OAIImage OAIFlightCarrier::getAirlineLogo() const {
    return m_airline_logo;
}
void OAIFlightCarrier::setAirlineLogo(const OAIImage &airline_logo) {
    m_airline_logo = airline_logo;
    m_airline_logo_isSet = true;
}

bool OAIFlightCarrier::is_airline_logo_Set() const{
    return m_airline_logo_isSet;
}

bool OAIFlightCarrier::is_airline_logo_Valid() const{
    return m_airline_logo_isValid;
}

OAILocalizedString OAIFlightCarrier::getAirlineName() const {
    return m_airline_name;
}
void OAIFlightCarrier::setAirlineName(const OAILocalizedString &airline_name) {
    m_airline_name = airline_name;
    m_airline_name_isSet = true;
}

bool OAIFlightCarrier::is_airline_name_Set() const{
    return m_airline_name_isSet;
}

bool OAIFlightCarrier::is_airline_name_Valid() const{
    return m_airline_name_isValid;
}

QString OAIFlightCarrier::getCarrierIataCode() const {
    return m_carrier_iata_code;
}
void OAIFlightCarrier::setCarrierIataCode(const QString &carrier_iata_code) {
    m_carrier_iata_code = carrier_iata_code;
    m_carrier_iata_code_isSet = true;
}

bool OAIFlightCarrier::is_carrier_iata_code_Set() const{
    return m_carrier_iata_code_isSet;
}

bool OAIFlightCarrier::is_carrier_iata_code_Valid() const{
    return m_carrier_iata_code_isValid;
}

QString OAIFlightCarrier::getCarrierIcaoCode() const {
    return m_carrier_icao_code;
}
void OAIFlightCarrier::setCarrierIcaoCode(const QString &carrier_icao_code) {
    m_carrier_icao_code = carrier_icao_code;
    m_carrier_icao_code_isSet = true;
}

bool OAIFlightCarrier::is_carrier_icao_code_Set() const{
    return m_carrier_icao_code_isSet;
}

bool OAIFlightCarrier::is_carrier_icao_code_Valid() const{
    return m_carrier_icao_code_isValid;
}

QString OAIFlightCarrier::getKind() const {
    return m_kind;
}
void OAIFlightCarrier::setKind(const QString &kind) {
    m_kind = kind;
    m_kind_isSet = true;
}

bool OAIFlightCarrier::is_kind_Set() const{
    return m_kind_isSet;
}

bool OAIFlightCarrier::is_kind_Valid() const{
    return m_kind_isValid;
}

bool OAIFlightCarrier::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_airline_alliance_logo.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_airline_logo.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_airline_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_iata_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_icao_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kind_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightCarrier::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
