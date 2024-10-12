/**
 * Branded Fares Upsell
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFlightStop.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlightStop::OAIFlightStop(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlightStop::OAIFlightStop() {
    this->initializeModel();
}

OAIFlightStop::~OAIFlightStop() {}

void OAIFlightStop::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_iata_code_isSet = false;
    m_iata_code_isValid = false;

    m_arrival_at_isSet = false;
    m_arrival_at_isValid = false;

    m_departure_at_isSet = false;
    m_departure_at_isValid = false;
}

void OAIFlightStop::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlightStop::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_iata_code_isValid = ::OpenAPI::fromJsonValue(m_iata_code, json[QString("iataCode")]);
    m_iata_code_isSet = !json[QString("iataCode")].isNull() && m_iata_code_isValid;

    m_arrival_at_isValid = ::OpenAPI::fromJsonValue(m_arrival_at, json[QString("arrivalAt")]);
    m_arrival_at_isSet = !json[QString("arrivalAt")].isNull() && m_arrival_at_isValid;

    m_departure_at_isValid = ::OpenAPI::fromJsonValue(m_departure_at, json[QString("departureAt")]);
    m_departure_at_isSet = !json[QString("departureAt")].isNull() && m_departure_at_isValid;
}

QString OAIFlightStop::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlightStop::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_iata_code_isSet) {
        obj.insert(QString("iataCode"), ::OpenAPI::toJsonValue(m_iata_code));
    }
    if (m_arrival_at_isSet) {
        obj.insert(QString("arrivalAt"), ::OpenAPI::toJsonValue(m_arrival_at));
    }
    if (m_departure_at_isSet) {
        obj.insert(QString("departureAt"), ::OpenAPI::toJsonValue(m_departure_at));
    }
    return obj;
}

QString OAIFlightStop::getDuration() const {
    return m_duration;
}
void OAIFlightStop::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIFlightStop::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIFlightStop::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIFlightStop::getIataCode() const {
    return m_iata_code;
}
void OAIFlightStop::setIataCode(const QString &iata_code) {
    m_iata_code = iata_code;
    m_iata_code_isSet = true;
}

bool OAIFlightStop::is_iata_code_Set() const{
    return m_iata_code_isSet;
}

bool OAIFlightStop::is_iata_code_Valid() const{
    return m_iata_code_isValid;
}

QDateTime OAIFlightStop::getArrivalAt() const {
    return m_arrival_at;
}
void OAIFlightStop::setArrivalAt(const QDateTime &arrival_at) {
    m_arrival_at = arrival_at;
    m_arrival_at_isSet = true;
}

bool OAIFlightStop::is_arrival_at_Set() const{
    return m_arrival_at_isSet;
}

bool OAIFlightStop::is_arrival_at_Valid() const{
    return m_arrival_at_isValid;
}

QDateTime OAIFlightStop::getDepartureAt() const {
    return m_departure_at;
}
void OAIFlightStop::setDepartureAt(const QDateTime &departure_at) {
    m_departure_at = departure_at;
    m_departure_at_isSet = true;
}

bool OAIFlightStop::is_departure_at_Set() const{
    return m_departure_at_isSet;
}

bool OAIFlightStop::is_departure_at_Valid() const{
    return m_departure_at_isValid;
}

bool OAIFlightStop::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iata_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_arrival_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_departure_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFlightStop::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
