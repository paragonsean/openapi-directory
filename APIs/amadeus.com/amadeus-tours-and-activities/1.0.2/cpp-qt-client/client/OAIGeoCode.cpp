/**
 * Tours and Activities
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGeoCode.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGeoCode::OAIGeoCode(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGeoCode::OAIGeoCode() {
    this->initializeModel();
}

OAIGeoCode::~OAIGeoCode() {}

void OAIGeoCode::initializeModel() {

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;
}

void OAIGeoCode::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGeoCode::fromJsonObject(QJsonObject json) {

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;
}

QString OAIGeoCode::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGeoCode::asJsonObject() const {
    QJsonObject obj;
    if (m_latitude_isSet) {
        obj.insert(QString("latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    return obj;
}

double OAIGeoCode::getLatitude() const {
    return m_latitude;
}
void OAIGeoCode::setLatitude(const double &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAIGeoCode::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAIGeoCode::is_latitude_Valid() const{
    return m_latitude_isValid;
}

double OAIGeoCode::getLongitude() const {
    return m_longitude;
}
void OAIGeoCode::setLongitude(const double &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAIGeoCode::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAIGeoCode::is_longitude_Valid() const{
    return m_longitude_isValid;
}

bool OAIGeoCode::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGeoCode::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
