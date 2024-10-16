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

#include "OAIContinentData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContinentData::OAIContinentData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContinentData::OAIContinentData() {
    this->initializeModel();
}

OAIContinentData::~OAIContinentData() {}

void OAIContinentData::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_countries_in_isSet = false;
    m_countries_in_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_name_locale_isSet = false;
    m_name_locale_isValid = false;
}

void OAIContinentData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContinentData::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_countries_in_isValid = ::OpenAPI::fromJsonValue(m_countries_in, json[QString("countries_in")]);
    m_countries_in_isSet = !json[QString("countries_in")].isNull() && m_countries_in_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_name_locale_isValid = ::OpenAPI::fromJsonValue(m_name_locale, json[QString("name_locale")]);
    m_name_locale_isSet = !json[QString("name_locale")].isNull() && m_name_locale_isValid;
}

QString OAIContinentData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContinentData::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_countries_in.size() > 0) {
        obj.insert(QString("countries_in"), ::OpenAPI::toJsonValue(m_countries_in));
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
    if (m_name_locale_isSet) {
        obj.insert(QString("name_locale"), ::OpenAPI::toJsonValue(m_name_locale));
    }
    return obj;
}

QString OAIContinentData::getCode() const {
    return m_code;
}
void OAIContinentData::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIContinentData::is_code_Set() const{
    return m_code_isSet;
}

bool OAIContinentData::is_code_Valid() const{
    return m_code_isValid;
}

QList<QString> OAIContinentData::getCountriesIn() const {
    return m_countries_in;
}
void OAIContinentData::setCountriesIn(const QList<QString> &countries_in) {
    m_countries_in = countries_in;
    m_countries_in_isSet = true;
}

bool OAIContinentData::is_countries_in_Set() const{
    return m_countries_in_isSet;
}

bool OAIContinentData::is_countries_in_Valid() const{
    return m_countries_in_isValid;
}

double OAIContinentData::getLatitude() const {
    return m_latitude;
}
void OAIContinentData::setLatitude(const double &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAIContinentData::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAIContinentData::is_latitude_Valid() const{
    return m_latitude_isValid;
}

double OAIContinentData::getLongitude() const {
    return m_longitude;
}
void OAIContinentData::setLongitude(const double &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAIContinentData::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAIContinentData::is_longitude_Valid() const{
    return m_longitude_isValid;
}

QString OAIContinentData::getName() const {
    return m_name;
}
void OAIContinentData::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIContinentData::is_name_Set() const{
    return m_name_isSet;
}

bool OAIContinentData::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIContinentData::getNameLocale() const {
    return m_name_locale;
}
void OAIContinentData::setNameLocale(const QString &name_locale) {
    m_name_locale = name_locale;
    m_name_locale_isSet = true;
}

bool OAIContinentData::is_name_locale_Set() const{
    return m_name_locale_isSet;
}

bool OAIContinentData::is_name_locale_Valid() const{
    return m_name_locale_isValid;
}

bool OAIContinentData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_countries_in.size() > 0) {
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

        if (m_name_locale_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContinentData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
