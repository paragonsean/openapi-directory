/**
 * Mon-voyage-pas-cher.com Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIElevationData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIElevationData::OAIElevationData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIElevationData::OAIElevationData() {
    this->initializeModel();
}

OAIElevationData::~OAIElevationData() {}

void OAIElevationData::initializeModel() {

    m_elevation_isSet = false;
    m_elevation_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_unit_isSet = false;
    m_unit_isValid = false;
}

void OAIElevationData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIElevationData::fromJsonObject(QJsonObject json) {

    m_elevation_isValid = ::OpenAPI::fromJsonValue(m_elevation, json[QString("elevation")]);
    m_elevation_isSet = !json[QString("elevation")].isNull() && m_elevation_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;
}

QString OAIElevationData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIElevationData::asJsonObject() const {
    QJsonObject obj;
    if (m_elevation_isSet) {
        obj.insert(QString("elevation"), ::OpenAPI::toJsonValue(m_elevation));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    return obj;
}

qint32 OAIElevationData::getElevation() const {
    return m_elevation;
}
void OAIElevationData::setElevation(const qint32 &elevation) {
    m_elevation = elevation;
    m_elevation_isSet = true;
}

bool OAIElevationData::is_elevation_Set() const{
    return m_elevation_isSet;
}

bool OAIElevationData::is_elevation_Valid() const{
    return m_elevation_isValid;
}

QString OAIElevationData::getLocation() const {
    return m_location;
}
void OAIElevationData::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIElevationData::is_location_Set() const{
    return m_location_isSet;
}

bool OAIElevationData::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIElevationData::getUnit() const {
    return m_unit;
}
void OAIElevationData::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAIElevationData::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAIElevationData::is_unit_Valid() const{
    return m_unit_isValid;
}

bool OAIElevationData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_elevation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIElevationData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
