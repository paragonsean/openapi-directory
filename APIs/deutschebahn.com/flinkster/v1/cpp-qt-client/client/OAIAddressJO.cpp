/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddressJO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddressJO::OAIAddressJO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddressJO::OAIAddressJO() {
    this->initializeModel();
}

OAIAddressJO::~OAIAddressJO() {}

void OAIAddressJO::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_district_isSet = false;
    m_district_isValid = false;

    m_iso_country_code_isSet = false;
    m_iso_country_code_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_street_isSet = false;
    m_street_isValid = false;

    m_zip_isSet = false;
    m_zip_isValid = false;
}

void OAIAddressJO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddressJO::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_district_isValid = ::OpenAPI::fromJsonValue(m_district, json[QString("district")]);
    m_district_isSet = !json[QString("district")].isNull() && m_district_isValid;

    m_iso_country_code_isValid = ::OpenAPI::fromJsonValue(m_iso_country_code, json[QString("isoCountryCode")]);
    m_iso_country_code_isSet = !json[QString("isoCountryCode")].isNull() && m_iso_country_code_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_street_isValid = ::OpenAPI::fromJsonValue(m_street, json[QString("street")]);
    m_street_isSet = !json[QString("street")].isNull() && m_street_isValid;

    m_zip_isValid = ::OpenAPI::fromJsonValue(m_zip, json[QString("zip")]);
    m_zip_isSet = !json[QString("zip")].isNull() && m_zip_isValid;
}

QString OAIAddressJO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddressJO::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_district_isSet) {
        obj.insert(QString("district"), ::OpenAPI::toJsonValue(m_district));
    }
    if (m_iso_country_code_isSet) {
        obj.insert(QString("isoCountryCode"), ::OpenAPI::toJsonValue(m_iso_country_code));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_street_isSet) {
        obj.insert(QString("street"), ::OpenAPI::toJsonValue(m_street));
    }
    if (m_zip_isSet) {
        obj.insert(QString("zip"), ::OpenAPI::toJsonValue(m_zip));
    }
    return obj;
}

QString OAIAddressJO::getCity() const {
    return m_city;
}
void OAIAddressJO::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIAddressJO::is_city_Set() const{
    return m_city_isSet;
}

bool OAIAddressJO::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIAddressJO::getDistrict() const {
    return m_district;
}
void OAIAddressJO::setDistrict(const QString &district) {
    m_district = district;
    m_district_isSet = true;
}

bool OAIAddressJO::is_district_Set() const{
    return m_district_isSet;
}

bool OAIAddressJO::is_district_Valid() const{
    return m_district_isValid;
}

QString OAIAddressJO::getIsoCountryCode() const {
    return m_iso_country_code;
}
void OAIAddressJO::setIsoCountryCode(const QString &iso_country_code) {
    m_iso_country_code = iso_country_code;
    m_iso_country_code_isSet = true;
}

bool OAIAddressJO::is_iso_country_code_Set() const{
    return m_iso_country_code_isSet;
}

bool OAIAddressJO::is_iso_country_code_Valid() const{
    return m_iso_country_code_isValid;
}

QString OAIAddressJO::getNumber() const {
    return m_number;
}
void OAIAddressJO::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIAddressJO::is_number_Set() const{
    return m_number_isSet;
}

bool OAIAddressJO::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIAddressJO::getStreet() const {
    return m_street;
}
void OAIAddressJO::setStreet(const QString &street) {
    m_street = street;
    m_street_isSet = true;
}

bool OAIAddressJO::is_street_Set() const{
    return m_street_isSet;
}

bool OAIAddressJO::is_street_Valid() const{
    return m_street_isValid;
}

QString OAIAddressJO::getZip() const {
    return m_zip;
}
void OAIAddressJO::setZip(const QString &zip) {
    m_zip = zip;
    m_zip_isSet = true;
}

bool OAIAddressJO::is_zip_Set() const{
    return m_zip_isSet;
}

bool OAIAddressJO::is_zip_Valid() const{
    return m_zip_isValid;
}

bool OAIAddressJO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_district_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iso_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_isSet) {
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

bool OAIAddressJO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
