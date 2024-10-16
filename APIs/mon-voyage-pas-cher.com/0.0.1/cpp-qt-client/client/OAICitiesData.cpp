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

#include "OAICitiesData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICitiesData::OAICitiesData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICitiesData::OAICitiesData() {
    this->initializeModel();
}

OAICitiesData::~OAICitiesData() {}

void OAICitiesData::initializeModel() {

    m_alternatename_isSet = false;
    m_alternatename_isValid = false;

    m_asciiname_isSet = false;
    m_asciiname_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_elevation_isSet = false;
    m_elevation_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_population_isSet = false;
    m_population_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;
}

void OAICitiesData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICitiesData::fromJsonObject(QJsonObject json) {

    m_alternatename_isValid = ::OpenAPI::fromJsonValue(m_alternatename, json[QString("alternatename")]);
    m_alternatename_isSet = !json[QString("alternatename")].isNull() && m_alternatename_isValid;

    m_asciiname_isValid = ::OpenAPI::fromJsonValue(m_asciiname, json[QString("asciiname")]);
    m_asciiname_isSet = !json[QString("asciiname")].isNull() && m_asciiname_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_elevation_isValid = ::OpenAPI::fromJsonValue(m_elevation, json[QString("elevation")]);
    m_elevation_isSet = !json[QString("elevation")].isNull() && m_elevation_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_population_isValid = ::OpenAPI::fromJsonValue(m_population, json[QString("population")]);
    m_population_isSet = !json[QString("population")].isNull() && m_population_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;
}

QString OAICitiesData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICitiesData::asJsonObject() const {
    QJsonObject obj;
    if (m_alternatename.size() > 0) {
        obj.insert(QString("alternatename"), ::OpenAPI::toJsonValue(m_alternatename));
    }
    if (m_asciiname_isSet) {
        obj.insert(QString("asciiname"), ::OpenAPI::toJsonValue(m_asciiname));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_elevation_isSet) {
        obj.insert(QString("elevation"), ::OpenAPI::toJsonValue(m_elevation));
    }
    if (m_latitude_isSet) {
        obj.insert(QString("latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_population_isSet) {
        obj.insert(QString("population"), ::OpenAPI::toJsonValue(m_population));
    }
    if (m_timezone_isSet) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    return obj;
}

QList<QString> OAICitiesData::getAlternatename() const {
    return m_alternatename;
}
void OAICitiesData::setAlternatename(const QList<QString> &alternatename) {
    m_alternatename = alternatename;
    m_alternatename_isSet = true;
}

bool OAICitiesData::is_alternatename_Set() const{
    return m_alternatename_isSet;
}

bool OAICitiesData::is_alternatename_Valid() const{
    return m_alternatename_isValid;
}

QString OAICitiesData::getAsciiname() const {
    return m_asciiname;
}
void OAICitiesData::setAsciiname(const QString &asciiname) {
    m_asciiname = asciiname;
    m_asciiname_isSet = true;
}

bool OAICitiesData::is_asciiname_Set() const{
    return m_asciiname_isSet;
}

bool OAICitiesData::is_asciiname_Valid() const{
    return m_asciiname_isValid;
}

QString OAICitiesData::getCountry() const {
    return m_country;
}
void OAICitiesData::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICitiesData::is_country_Set() const{
    return m_country_isSet;
}

bool OAICitiesData::is_country_Valid() const{
    return m_country_isValid;
}

double OAICitiesData::getElevation() const {
    return m_elevation;
}
void OAICitiesData::setElevation(const double &elevation) {
    m_elevation = elevation;
    m_elevation_isSet = true;
}

bool OAICitiesData::is_elevation_Set() const{
    return m_elevation_isSet;
}

bool OAICitiesData::is_elevation_Valid() const{
    return m_elevation_isValid;
}

double OAICitiesData::getLatitude() const {
    return m_latitude;
}
void OAICitiesData::setLatitude(const double &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAICitiesData::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAICitiesData::is_latitude_Valid() const{
    return m_latitude_isValid;
}

double OAICitiesData::getLongitude() const {
    return m_longitude;
}
void OAICitiesData::setLongitude(const double &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAICitiesData::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAICitiesData::is_longitude_Valid() const{
    return m_longitude_isValid;
}

QString OAICitiesData::getName() const {
    return m_name;
}
void OAICitiesData::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICitiesData::is_name_Set() const{
    return m_name_isSet;
}

bool OAICitiesData::is_name_Valid() const{
    return m_name_isValid;
}

double OAICitiesData::getPopulation() const {
    return m_population;
}
void OAICitiesData::setPopulation(const double &population) {
    m_population = population;
    m_population_isSet = true;
}

bool OAICitiesData::is_population_Set() const{
    return m_population_isSet;
}

bool OAICitiesData::is_population_Valid() const{
    return m_population_isValid;
}

QString OAICitiesData::getTimezone() const {
    return m_timezone;
}
void OAICitiesData::setTimezone(const QString &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAICitiesData::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAICitiesData::is_timezone_Valid() const{
    return m_timezone_isValid;
}

bool OAICitiesData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alternatename.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_asciiname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_elevation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_population_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICitiesData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
