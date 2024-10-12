/**
 * NASCAR v2
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRaceResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRaceResult::OAIRaceResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRaceResult::OAIRaceResult() {
    this->initializeModel();
}

OAIRaceResult::~OAIRaceResult() {}

void OAIRaceResult::initializeModel() {

    m_driver_races_isSet = false;
    m_driver_races_isValid = false;

    m_race_isSet = false;
    m_race_isValid = false;
}

void OAIRaceResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRaceResult::fromJsonObject(QJsonObject json) {

    m_driver_races_isValid = ::OpenAPI::fromJsonValue(m_driver_races, json[QString("DriverRaces")]);
    m_driver_races_isSet = !json[QString("DriverRaces")].isNull() && m_driver_races_isValid;

    m_race_isValid = ::OpenAPI::fromJsonValue(m_race, json[QString("Race")]);
    m_race_isSet = !json[QString("Race")].isNull() && m_race_isValid;
}

QString OAIRaceResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRaceResult::asJsonObject() const {
    QJsonObject obj;
    if (m_driver_races.size() > 0) {
        obj.insert(QString("DriverRaces"), ::OpenAPI::toJsonValue(m_driver_races));
    }
    if (m_race.isSet()) {
        obj.insert(QString("Race"), ::OpenAPI::toJsonValue(m_race));
    }
    return obj;
}

QList<OAIDriverRace> OAIRaceResult::getDriverRaces() const {
    return m_driver_races;
}
void OAIRaceResult::setDriverRaces(const QList<OAIDriverRace> &driver_races) {
    m_driver_races = driver_races;
    m_driver_races_isSet = true;
}

bool OAIRaceResult::is_driver_races_Set() const{
    return m_driver_races_isSet;
}

bool OAIRaceResult::is_driver_races_Valid() const{
    return m_driver_races_isValid;
}

OAIRace OAIRaceResult::getRace() const {
    return m_race;
}
void OAIRaceResult::setRace(const OAIRace &race) {
    m_race = race;
    m_race_isSet = true;
}

bool OAIRaceResult::is_race_Set() const{
    return m_race_isSet;
}

bool OAIRaceResult::is_race_Valid() const{
    return m_race_isValid;
}

bool OAIRaceResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_driver_races.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_race.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRaceResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
