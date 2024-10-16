/**
 * NBA v3 Scores
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStadium.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStadium::OAIStadium(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStadium::OAIStadium() {
    this->initializeModel();
}

OAIStadium::~OAIStadium() {}

void OAIStadium::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_capacity_isSet = false;
    m_capacity_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_geo_lat_isSet = false;
    m_geo_lat_isValid = false;

    m_geo_long_isSet = false;
    m_geo_long_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_stadium_id_isSet = false;
    m_stadium_id_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_zip_isSet = false;
    m_zip_isValid = false;
}

void OAIStadium::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStadium::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("Active")]);
    m_active_isSet = !json[QString("Active")].isNull() && m_active_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("Address")]);
    m_address_isSet = !json[QString("Address")].isNull() && m_address_isValid;

    m_capacity_isValid = ::OpenAPI::fromJsonValue(m_capacity, json[QString("Capacity")]);
    m_capacity_isSet = !json[QString("Capacity")].isNull() && m_capacity_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("City")]);
    m_city_isSet = !json[QString("City")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("Country")]);
    m_country_isSet = !json[QString("Country")].isNull() && m_country_isValid;

    m_geo_lat_isValid = ::OpenAPI::fromJsonValue(m_geo_lat, json[QString("GeoLat")]);
    m_geo_lat_isSet = !json[QString("GeoLat")].isNull() && m_geo_lat_isValid;

    m_geo_long_isValid = ::OpenAPI::fromJsonValue(m_geo_long, json[QString("GeoLong")]);
    m_geo_long_isSet = !json[QString("GeoLong")].isNull() && m_geo_long_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_stadium_id_isValid = ::OpenAPI::fromJsonValue(m_stadium_id, json[QString("StadiumID")]);
    m_stadium_id_isSet = !json[QString("StadiumID")].isNull() && m_stadium_id_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("State")]);
    m_state_isSet = !json[QString("State")].isNull() && m_state_isValid;

    m_zip_isValid = ::OpenAPI::fromJsonValue(m_zip, json[QString("Zip")]);
    m_zip_isSet = !json[QString("Zip")].isNull() && m_zip_isValid;
}

QString OAIStadium::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStadium::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("Active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_address_isSet) {
        obj.insert(QString("Address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_capacity_isSet) {
        obj.insert(QString("Capacity"), ::OpenAPI::toJsonValue(m_capacity));
    }
    if (m_city_isSet) {
        obj.insert(QString("City"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("Country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_geo_lat_isSet) {
        obj.insert(QString("GeoLat"), ::OpenAPI::toJsonValue(m_geo_lat));
    }
    if (m_geo_long_isSet) {
        obj.insert(QString("GeoLong"), ::OpenAPI::toJsonValue(m_geo_long));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_stadium_id_isSet) {
        obj.insert(QString("StadiumID"), ::OpenAPI::toJsonValue(m_stadium_id));
    }
    if (m_state_isSet) {
        obj.insert(QString("State"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_zip_isSet) {
        obj.insert(QString("Zip"), ::OpenAPI::toJsonValue(m_zip));
    }
    return obj;
}

bool OAIStadium::isActive() const {
    return m_active;
}
void OAIStadium::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIStadium::is_active_Set() const{
    return m_active_isSet;
}

bool OAIStadium::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIStadium::getAddress() const {
    return m_address;
}
void OAIStadium::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIStadium::is_address_Set() const{
    return m_address_isSet;
}

bool OAIStadium::is_address_Valid() const{
    return m_address_isValid;
}

qint32 OAIStadium::getCapacity() const {
    return m_capacity;
}
void OAIStadium::setCapacity(const qint32 &capacity) {
    m_capacity = capacity;
    m_capacity_isSet = true;
}

bool OAIStadium::is_capacity_Set() const{
    return m_capacity_isSet;
}

bool OAIStadium::is_capacity_Valid() const{
    return m_capacity_isValid;
}

QString OAIStadium::getCity() const {
    return m_city;
}
void OAIStadium::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIStadium::is_city_Set() const{
    return m_city_isSet;
}

bool OAIStadium::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIStadium::getCountry() const {
    return m_country;
}
void OAIStadium::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIStadium::is_country_Set() const{
    return m_country_isSet;
}

bool OAIStadium::is_country_Valid() const{
    return m_country_isValid;
}

double OAIStadium::getGeoLat() const {
    return m_geo_lat;
}
void OAIStadium::setGeoLat(const double &geo_lat) {
    m_geo_lat = geo_lat;
    m_geo_lat_isSet = true;
}

bool OAIStadium::is_geo_lat_Set() const{
    return m_geo_lat_isSet;
}

bool OAIStadium::is_geo_lat_Valid() const{
    return m_geo_lat_isValid;
}

double OAIStadium::getGeoLong() const {
    return m_geo_long;
}
void OAIStadium::setGeoLong(const double &geo_long) {
    m_geo_long = geo_long;
    m_geo_long_isSet = true;
}

bool OAIStadium::is_geo_long_Set() const{
    return m_geo_long_isSet;
}

bool OAIStadium::is_geo_long_Valid() const{
    return m_geo_long_isValid;
}

QString OAIStadium::getName() const {
    return m_name;
}
void OAIStadium::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStadium::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStadium::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIStadium::getStadiumId() const {
    return m_stadium_id;
}
void OAIStadium::setStadiumId(const qint32 &stadium_id) {
    m_stadium_id = stadium_id;
    m_stadium_id_isSet = true;
}

bool OAIStadium::is_stadium_id_Set() const{
    return m_stadium_id_isSet;
}

bool OAIStadium::is_stadium_id_Valid() const{
    return m_stadium_id_isValid;
}

QString OAIStadium::getState() const {
    return m_state;
}
void OAIStadium::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIStadium::is_state_Set() const{
    return m_state_isSet;
}

bool OAIStadium::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIStadium::getZip() const {
    return m_zip;
}
void OAIStadium::setZip(const QString &zip) {
    m_zip = zip;
    m_zip_isSet = true;
}

bool OAIStadium::is_zip_Set() const{
    return m_zip_isSet;
}

bool OAIStadium::is_zip_Valid() const{
    return m_zip_isValid;
}

bool OAIStadium::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_capacity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_geo_lat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_geo_long_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_stadium_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStadium::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
