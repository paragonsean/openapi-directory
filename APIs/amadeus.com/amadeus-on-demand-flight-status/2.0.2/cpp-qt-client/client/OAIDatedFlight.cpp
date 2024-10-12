/**
 * On-Demand Flight Status
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDatedFlight.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDatedFlight::OAIDatedFlight(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDatedFlight::OAIDatedFlight() {
    this->initializeModel();
}

OAIDatedFlight::~OAIDatedFlight() {}

void OAIDatedFlight::initializeModel() {

    m_flight_designator_isSet = false;
    m_flight_designator_isValid = false;

    m_flight_points_isSet = false;
    m_flight_points_isValid = false;

    m_legs_isSet = false;
    m_legs_isValid = false;

    m_scheduled_departure_date_isSet = false;
    m_scheduled_departure_date_isValid = false;

    m_segments_isSet = false;
    m_segments_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIDatedFlight::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDatedFlight::fromJsonObject(QJsonObject json) {

    m_flight_designator_isValid = ::OpenAPI::fromJsonValue(m_flight_designator, json[QString("flightDesignator")]);
    m_flight_designator_isSet = !json[QString("flightDesignator")].isNull() && m_flight_designator_isValid;

    m_flight_points_isValid = ::OpenAPI::fromJsonValue(m_flight_points, json[QString("flightPoints")]);
    m_flight_points_isSet = !json[QString("flightPoints")].isNull() && m_flight_points_isValid;

    m_legs_isValid = ::OpenAPI::fromJsonValue(m_legs, json[QString("legs")]);
    m_legs_isSet = !json[QString("legs")].isNull() && m_legs_isValid;

    m_scheduled_departure_date_isValid = ::OpenAPI::fromJsonValue(m_scheduled_departure_date, json[QString("scheduledDepartureDate")]);
    m_scheduled_departure_date_isSet = !json[QString("scheduledDepartureDate")].isNull() && m_scheduled_departure_date_isValid;

    m_segments_isValid = ::OpenAPI::fromJsonValue(m_segments, json[QString("segments")]);
    m_segments_isSet = !json[QString("segments")].isNull() && m_segments_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIDatedFlight::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDatedFlight::asJsonObject() const {
    QJsonObject obj;
    if (m_flight_designator.isSet()) {
        obj.insert(QString("flightDesignator"), ::OpenAPI::toJsonValue(m_flight_designator));
    }
    if (m_flight_points.size() > 0) {
        obj.insert(QString("flightPoints"), ::OpenAPI::toJsonValue(m_flight_points));
    }
    if (m_legs.size() > 0) {
        obj.insert(QString("legs"), ::OpenAPI::toJsonValue(m_legs));
    }
    if (m_scheduled_departure_date_isSet) {
        obj.insert(QString("scheduledDepartureDate"), ::OpenAPI::toJsonValue(m_scheduled_departure_date));
    }
    if (m_segments.size() > 0) {
        obj.insert(QString("segments"), ::OpenAPI::toJsonValue(m_segments));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIFlightDesignator OAIDatedFlight::getFlightDesignator() const {
    return m_flight_designator;
}
void OAIDatedFlight::setFlightDesignator(const OAIFlightDesignator &flight_designator) {
    m_flight_designator = flight_designator;
    m_flight_designator_isSet = true;
}

bool OAIDatedFlight::is_flight_designator_Set() const{
    return m_flight_designator_isSet;
}

bool OAIDatedFlight::is_flight_designator_Valid() const{
    return m_flight_designator_isValid;
}

QList<OAIFlightPoint> OAIDatedFlight::getFlightPoints() const {
    return m_flight_points;
}
void OAIDatedFlight::setFlightPoints(const QList<OAIFlightPoint> &flight_points) {
    m_flight_points = flight_points;
    m_flight_points_isSet = true;
}

bool OAIDatedFlight::is_flight_points_Set() const{
    return m_flight_points_isSet;
}

bool OAIDatedFlight::is_flight_points_Valid() const{
    return m_flight_points_isValid;
}

QList<OAILeg> OAIDatedFlight::getLegs() const {
    return m_legs;
}
void OAIDatedFlight::setLegs(const QList<OAILeg> &legs) {
    m_legs = legs;
    m_legs_isSet = true;
}

bool OAIDatedFlight::is_legs_Set() const{
    return m_legs_isSet;
}

bool OAIDatedFlight::is_legs_Valid() const{
    return m_legs_isValid;
}

QDate OAIDatedFlight::getScheduledDepartureDate() const {
    return m_scheduled_departure_date;
}
void OAIDatedFlight::setScheduledDepartureDate(const QDate &scheduled_departure_date) {
    m_scheduled_departure_date = scheduled_departure_date;
    m_scheduled_departure_date_isSet = true;
}

bool OAIDatedFlight::is_scheduled_departure_date_Set() const{
    return m_scheduled_departure_date_isSet;
}

bool OAIDatedFlight::is_scheduled_departure_date_Valid() const{
    return m_scheduled_departure_date_isValid;
}

QList<OAISegment> OAIDatedFlight::getSegments() const {
    return m_segments;
}
void OAIDatedFlight::setSegments(const QList<OAISegment> &segments) {
    m_segments = segments;
    m_segments_isSet = true;
}

bool OAIDatedFlight::is_segments_Set() const{
    return m_segments_isSet;
}

bool OAIDatedFlight::is_segments_Valid() const{
    return m_segments_isValid;
}

QString OAIDatedFlight::getType() const {
    return m_type;
}
void OAIDatedFlight::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDatedFlight::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDatedFlight::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIDatedFlight::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_flight_designator.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_flight_points.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_legs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_departure_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_segments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDatedFlight::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
