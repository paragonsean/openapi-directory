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

#include "OAIFlightFilters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightFilters::OAIFlightFilters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightFilters::OAIFlightFilters() {
    this->initializeModel();
}

OAIFlightFilters::~OAIFlightFilters() {}

void OAIFlightFilters::initializeModel() {

    m_bus_segment_allowed_isSet = false;
    m_bus_segment_allowed_isValid = false;

    m_cabin_restrictions_isSet = false;
    m_cabin_restrictions_isValid = false;

    m_carrier_restrictions_isSet = false;
    m_carrier_restrictions_isValid = false;

    m_connection_restriction_isSet = false;
    m_connection_restriction_isValid = false;

    m_cross_border_allowed_isSet = false;
    m_cross_border_allowed_isValid = false;

    m_max_flight_time_isSet = false;
    m_max_flight_time_isValid = false;

    m_more_overnights_allowed_isSet = false;
    m_more_overnights_allowed_isValid = false;

    m_rail_segment_allowed_isSet = false;
    m_rail_segment_allowed_isValid = false;

    m_return_to_departure_airport_isSet = false;
    m_return_to_departure_airport_isValid = false;
}

void OAIFlightFilters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightFilters::fromJsonObject(QJsonObject json) {

    m_bus_segment_allowed_isValid = ::OpenAPI::fromJsonValue(m_bus_segment_allowed, json[QString("busSegmentAllowed")]);
    m_bus_segment_allowed_isSet = !json[QString("busSegmentAllowed")].isNull() && m_bus_segment_allowed_isValid;

    m_cabin_restrictions_isValid = ::OpenAPI::fromJsonValue(m_cabin_restrictions, json[QString("cabinRestrictions")]);
    m_cabin_restrictions_isSet = !json[QString("cabinRestrictions")].isNull() && m_cabin_restrictions_isValid;

    m_carrier_restrictions_isValid = ::OpenAPI::fromJsonValue(m_carrier_restrictions, json[QString("carrierRestrictions")]);
    m_carrier_restrictions_isSet = !json[QString("carrierRestrictions")].isNull() && m_carrier_restrictions_isValid;

    m_connection_restriction_isValid = ::OpenAPI::fromJsonValue(m_connection_restriction, json[QString("connectionRestriction")]);
    m_connection_restriction_isSet = !json[QString("connectionRestriction")].isNull() && m_connection_restriction_isValid;

    m_cross_border_allowed_isValid = ::OpenAPI::fromJsonValue(m_cross_border_allowed, json[QString("crossBorderAllowed")]);
    m_cross_border_allowed_isSet = !json[QString("crossBorderAllowed")].isNull() && m_cross_border_allowed_isValid;

    m_max_flight_time_isValid = ::OpenAPI::fromJsonValue(m_max_flight_time, json[QString("maxFlightTime")]);
    m_max_flight_time_isSet = !json[QString("maxFlightTime")].isNull() && m_max_flight_time_isValid;

    m_more_overnights_allowed_isValid = ::OpenAPI::fromJsonValue(m_more_overnights_allowed, json[QString("moreOvernightsAllowed")]);
    m_more_overnights_allowed_isSet = !json[QString("moreOvernightsAllowed")].isNull() && m_more_overnights_allowed_isValid;

    m_rail_segment_allowed_isValid = ::OpenAPI::fromJsonValue(m_rail_segment_allowed, json[QString("railSegmentAllowed")]);
    m_rail_segment_allowed_isSet = !json[QString("railSegmentAllowed")].isNull() && m_rail_segment_allowed_isValid;

    m_return_to_departure_airport_isValid = ::OpenAPI::fromJsonValue(m_return_to_departure_airport, json[QString("returnToDepartureAirport")]);
    m_return_to_departure_airport_isSet = !json[QString("returnToDepartureAirport")].isNull() && m_return_to_departure_airport_isValid;
}

QString OAIFlightFilters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightFilters::asJsonObject() const {
    QJsonObject obj;
    if (m_bus_segment_allowed_isSet) {
        obj.insert(QString("busSegmentAllowed"), ::OpenAPI::toJsonValue(m_bus_segment_allowed));
    }
    if (m_cabin_restrictions.size() > 0) {
        obj.insert(QString("cabinRestrictions"), ::OpenAPI::toJsonValue(m_cabin_restrictions));
    }
    if (m_carrier_restrictions.isSet()) {
        obj.insert(QString("carrierRestrictions"), ::OpenAPI::toJsonValue(m_carrier_restrictions));
    }
    if (m_connection_restriction.isSet()) {
        obj.insert(QString("connectionRestriction"), ::OpenAPI::toJsonValue(m_connection_restriction));
    }
    if (m_cross_border_allowed_isSet) {
        obj.insert(QString("crossBorderAllowed"), ::OpenAPI::toJsonValue(m_cross_border_allowed));
    }
    if (m_max_flight_time_isSet) {
        obj.insert(QString("maxFlightTime"), ::OpenAPI::toJsonValue(m_max_flight_time));
    }
    if (m_more_overnights_allowed_isSet) {
        obj.insert(QString("moreOvernightsAllowed"), ::OpenAPI::toJsonValue(m_more_overnights_allowed));
    }
    if (m_rail_segment_allowed_isSet) {
        obj.insert(QString("railSegmentAllowed"), ::OpenAPI::toJsonValue(m_rail_segment_allowed));
    }
    if (m_return_to_departure_airport_isSet) {
        obj.insert(QString("returnToDepartureAirport"), ::OpenAPI::toJsonValue(m_return_to_departure_airport));
    }
    return obj;
}

bool OAIFlightFilters::isBusSegmentAllowed() const {
    return m_bus_segment_allowed;
}
void OAIFlightFilters::setBusSegmentAllowed(const bool &bus_segment_allowed) {
    m_bus_segment_allowed = bus_segment_allowed;
    m_bus_segment_allowed_isSet = true;
}

bool OAIFlightFilters::is_bus_segment_allowed_Set() const{
    return m_bus_segment_allowed_isSet;
}

bool OAIFlightFilters::is_bus_segment_allowed_Valid() const{
    return m_bus_segment_allowed_isValid;
}

QList<OAICabinRestriction> OAIFlightFilters::getCabinRestrictions() const {
    return m_cabin_restrictions;
}
void OAIFlightFilters::setCabinRestrictions(const QList<OAICabinRestriction> &cabin_restrictions) {
    m_cabin_restrictions = cabin_restrictions;
    m_cabin_restrictions_isSet = true;
}

bool OAIFlightFilters::is_cabin_restrictions_Set() const{
    return m_cabin_restrictions_isSet;
}

bool OAIFlightFilters::is_cabin_restrictions_Valid() const{
    return m_cabin_restrictions_isValid;
}

OAICarrierRestrictions OAIFlightFilters::getCarrierRestrictions() const {
    return m_carrier_restrictions;
}
void OAIFlightFilters::setCarrierRestrictions(const OAICarrierRestrictions &carrier_restrictions) {
    m_carrier_restrictions = carrier_restrictions;
    m_carrier_restrictions_isSet = true;
}

bool OAIFlightFilters::is_carrier_restrictions_Set() const{
    return m_carrier_restrictions_isSet;
}

bool OAIFlightFilters::is_carrier_restrictions_Valid() const{
    return m_carrier_restrictions_isValid;
}

OAIConnectionRestriction OAIFlightFilters::getConnectionRestriction() const {
    return m_connection_restriction;
}
void OAIFlightFilters::setConnectionRestriction(const OAIConnectionRestriction &connection_restriction) {
    m_connection_restriction = connection_restriction;
    m_connection_restriction_isSet = true;
}

bool OAIFlightFilters::is_connection_restriction_Set() const{
    return m_connection_restriction_isSet;
}

bool OAIFlightFilters::is_connection_restriction_Valid() const{
    return m_connection_restriction_isValid;
}

bool OAIFlightFilters::isCrossBorderAllowed() const {
    return m_cross_border_allowed;
}
void OAIFlightFilters::setCrossBorderAllowed(const bool &cross_border_allowed) {
    m_cross_border_allowed = cross_border_allowed;
    m_cross_border_allowed_isSet = true;
}

bool OAIFlightFilters::is_cross_border_allowed_Set() const{
    return m_cross_border_allowed_isSet;
}

bool OAIFlightFilters::is_cross_border_allowed_Valid() const{
    return m_cross_border_allowed_isValid;
}

double OAIFlightFilters::getMaxFlightTime() const {
    return m_max_flight_time;
}
void OAIFlightFilters::setMaxFlightTime(const double &max_flight_time) {
    m_max_flight_time = max_flight_time;
    m_max_flight_time_isSet = true;
}

bool OAIFlightFilters::is_max_flight_time_Set() const{
    return m_max_flight_time_isSet;
}

bool OAIFlightFilters::is_max_flight_time_Valid() const{
    return m_max_flight_time_isValid;
}

bool OAIFlightFilters::isMoreOvernightsAllowed() const {
    return m_more_overnights_allowed;
}
void OAIFlightFilters::setMoreOvernightsAllowed(const bool &more_overnights_allowed) {
    m_more_overnights_allowed = more_overnights_allowed;
    m_more_overnights_allowed_isSet = true;
}

bool OAIFlightFilters::is_more_overnights_allowed_Set() const{
    return m_more_overnights_allowed_isSet;
}

bool OAIFlightFilters::is_more_overnights_allowed_Valid() const{
    return m_more_overnights_allowed_isValid;
}

bool OAIFlightFilters::isRailSegmentAllowed() const {
    return m_rail_segment_allowed;
}
void OAIFlightFilters::setRailSegmentAllowed(const bool &rail_segment_allowed) {
    m_rail_segment_allowed = rail_segment_allowed;
    m_rail_segment_allowed_isSet = true;
}

bool OAIFlightFilters::is_rail_segment_allowed_Set() const{
    return m_rail_segment_allowed_isSet;
}

bool OAIFlightFilters::is_rail_segment_allowed_Valid() const{
    return m_rail_segment_allowed_isValid;
}

bool OAIFlightFilters::isReturnToDepartureAirport() const {
    return m_return_to_departure_airport;
}
void OAIFlightFilters::setReturnToDepartureAirport(const bool &return_to_departure_airport) {
    m_return_to_departure_airport = return_to_departure_airport;
    m_return_to_departure_airport_isSet = true;
}

bool OAIFlightFilters::is_return_to_departure_airport_Set() const{
    return m_return_to_departure_airport_isSet;
}

bool OAIFlightFilters::is_return_to_departure_airport_Valid() const{
    return m_return_to_departure_airport_isValid;
}

bool OAIFlightFilters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bus_segment_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cabin_restrictions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_carrier_restrictions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_connection_restriction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cross_border_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_flight_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_more_overnights_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rail_segment_allowed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_return_to_departure_airport_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightFilters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
