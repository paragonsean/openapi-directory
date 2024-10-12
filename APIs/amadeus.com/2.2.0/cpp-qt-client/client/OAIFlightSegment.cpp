/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlightSegment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightSegment::OAIFlightSegment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightSegment::OAIFlightSegment() {
    this->initializeModel();
}

OAIFlightSegment::~OAIFlightSegment() {}

void OAIFlightSegment::initializeModel() {

    m_aircraft_isSet = false;
    m_aircraft_isValid = false;

    m_arrival_isSet = false;
    m_arrival_isValid = false;

    m_carrier_code_isSet = false;
    m_carrier_code_isValid = false;

    m_departure_isSet = false;
    m_departure_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_operating_isSet = false;
    m_operating_isValid = false;

    m_stops_isSet = false;
    m_stops_isValid = false;
}

void OAIFlightSegment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightSegment::fromJsonObject(QJsonObject json) {

    m_aircraft_isValid = ::OpenAPI::fromJsonValue(m_aircraft, json[QString("aircraft")]);
    m_aircraft_isSet = !json[QString("aircraft")].isNull() && m_aircraft_isValid;

    m_arrival_isValid = ::OpenAPI::fromJsonValue(m_arrival, json[QString("arrival")]);
    m_arrival_isSet = !json[QString("arrival")].isNull() && m_arrival_isValid;

    m_carrier_code_isValid = ::OpenAPI::fromJsonValue(m_carrier_code, json[QString("carrierCode")]);
    m_carrier_code_isSet = !json[QString("carrierCode")].isNull() && m_carrier_code_isValid;

    m_departure_isValid = ::OpenAPI::fromJsonValue(m_departure, json[QString("departure")]);
    m_departure_isSet = !json[QString("departure")].isNull() && m_departure_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_operating_isValid = ::OpenAPI::fromJsonValue(m_operating, json[QString("operating")]);
    m_operating_isSet = !json[QString("operating")].isNull() && m_operating_isValid;

    m_stops_isValid = ::OpenAPI::fromJsonValue(m_stops, json[QString("stops")]);
    m_stops_isSet = !json[QString("stops")].isNull() && m_stops_isValid;
}

QString OAIFlightSegment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightSegment::asJsonObject() const {
    QJsonObject obj;
    if (m_aircraft.isSet()) {
        obj.insert(QString("aircraft"), ::OpenAPI::toJsonValue(m_aircraft));
    }
    if (m_arrival.isSet()) {
        obj.insert(QString("arrival"), ::OpenAPI::toJsonValue(m_arrival));
    }
    if (m_carrier_code_isSet) {
        obj.insert(QString("carrierCode"), ::OpenAPI::toJsonValue(m_carrier_code));
    }
    if (m_departure.isSet()) {
        obj.insert(QString("departure"), ::OpenAPI::toJsonValue(m_departure));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_operating.isSet()) {
        obj.insert(QString("operating"), ::OpenAPI::toJsonValue(m_operating));
    }
    if (m_stops.size() > 0) {
        obj.insert(QString("stops"), ::OpenAPI::toJsonValue(m_stops));
    }
    return obj;
}

OAIAircraftEquipment OAIFlightSegment::getAircraft() const {
    return m_aircraft;
}
void OAIFlightSegment::setAircraft(const OAIAircraftEquipment &aircraft) {
    m_aircraft = aircraft;
    m_aircraft_isSet = true;
}

bool OAIFlightSegment::is_aircraft_Set() const{
    return m_aircraft_isSet;
}

bool OAIFlightSegment::is_aircraft_Valid() const{
    return m_aircraft_isValid;
}

OAIFlightEndPoint OAIFlightSegment::getArrival() const {
    return m_arrival;
}
void OAIFlightSegment::setArrival(const OAIFlightEndPoint &arrival) {
    m_arrival = arrival;
    m_arrival_isSet = true;
}

bool OAIFlightSegment::is_arrival_Set() const{
    return m_arrival_isSet;
}

bool OAIFlightSegment::is_arrival_Valid() const{
    return m_arrival_isValid;
}

QString OAIFlightSegment::getCarrierCode() const {
    return m_carrier_code;
}
void OAIFlightSegment::setCarrierCode(const QString &carrier_code) {
    m_carrier_code = carrier_code;
    m_carrier_code_isSet = true;
}

bool OAIFlightSegment::is_carrier_code_Set() const{
    return m_carrier_code_isSet;
}

bool OAIFlightSegment::is_carrier_code_Valid() const{
    return m_carrier_code_isValid;
}

OAIFlightEndPoint OAIFlightSegment::getDeparture() const {
    return m_departure;
}
void OAIFlightSegment::setDeparture(const OAIFlightEndPoint &departure) {
    m_departure = departure;
    m_departure_isSet = true;
}

bool OAIFlightSegment::is_departure_Set() const{
    return m_departure_isSet;
}

bool OAIFlightSegment::is_departure_Valid() const{
    return m_departure_isValid;
}

QString OAIFlightSegment::getDuration() const {
    return m_duration;
}
void OAIFlightSegment::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIFlightSegment::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIFlightSegment::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIFlightSegment::getNumber() const {
    return m_number;
}
void OAIFlightSegment::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIFlightSegment::is_number_Set() const{
    return m_number_isSet;
}

bool OAIFlightSegment::is_number_Valid() const{
    return m_number_isValid;
}

OAIOperatingFlight OAIFlightSegment::getOperating() const {
    return m_operating;
}
void OAIFlightSegment::setOperating(const OAIOperatingFlight &operating) {
    m_operating = operating;
    m_operating_isSet = true;
}

bool OAIFlightSegment::is_operating_Set() const{
    return m_operating_isSet;
}

bool OAIFlightSegment::is_operating_Valid() const{
    return m_operating_isValid;
}

QList<OAIFlightStop> OAIFlightSegment::getStops() const {
    return m_stops;
}
void OAIFlightSegment::setStops(const QList<OAIFlightStop> &stops) {
    m_stops = stops;
    m_stops_isSet = true;
}

bool OAIFlightSegment::is_stops_Set() const{
    return m_stops_isSet;
}

bool OAIFlightSegment::is_stops_Valid() const{
    return m_stops_isValid;
}

bool OAIFlightSegment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aircraft.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_arrival.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_departure.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operating.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_stops.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightSegment::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
