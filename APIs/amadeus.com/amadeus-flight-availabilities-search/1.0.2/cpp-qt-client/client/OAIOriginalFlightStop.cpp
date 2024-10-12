/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOriginalFlightStop.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOriginalFlightStop::OAIOriginalFlightStop(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOriginalFlightStop::OAIOriginalFlightStop() {
    this->initializeModel();
}

OAIOriginalFlightStop::~OAIOriginalFlightStop() {}

void OAIOriginalFlightStop::initializeModel() {

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_iata_code_isSet = false;
    m_iata_code_isValid = false;
}

void OAIOriginalFlightStop::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOriginalFlightStop::fromJsonObject(QJsonObject json) {

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_iata_code_isValid = ::OpenAPI::fromJsonValue(m_iata_code, json[QString("iataCode")]);
    m_iata_code_isSet = !json[QString("iataCode")].isNull() && m_iata_code_isValid;
}

QString OAIOriginalFlightStop::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOriginalFlightStop::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_iata_code_isSet) {
        obj.insert(QString("iataCode"), ::OpenAPI::toJsonValue(m_iata_code));
    }
    return obj;
}

QString OAIOriginalFlightStop::getDuration() const {
    return m_duration;
}
void OAIOriginalFlightStop::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIOriginalFlightStop::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIOriginalFlightStop::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAIOriginalFlightStop::getIataCode() const {
    return m_iata_code;
}
void OAIOriginalFlightStop::setIataCode(const QString &iata_code) {
    m_iata_code = iata_code;
    m_iata_code_isSet = true;
}

bool OAIOriginalFlightStop::is_iata_code_Set() const{
    return m_iata_code_isSet;
}

bool OAIOriginalFlightStop::is_iata_code_Valid() const{
    return m_iata_code_isValid;
}

bool OAIOriginalFlightStop::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIOriginalFlightStop::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
