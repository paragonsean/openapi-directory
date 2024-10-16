/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISiteResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISiteResult::OAISiteResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISiteResult::OAISiteResult() {
    this->initializeModel();
}

OAISiteResult::~OAISiteResult() {}

void OAISiteResult::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;
}

void OAISiteResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISiteResult::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("Description")]);
    m_description_isSet = !json[QString("Description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("Id")]);
    m_id_isSet = !json[QString("Id")].isNull() && m_id_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("Latitude")]);
    m_latitude_isSet = !json[QString("Latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("Longitude")]);
    m_longitude_isSet = !json[QString("Longitude")].isNull() && m_longitude_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("Status")]);
    m_status_isSet = !json[QString("Status")].isNull() && m_status_isValid;
}

QString OAISiteResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISiteResult::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("Description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("Id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_latitude_isSet) {
        obj.insert(QString("Latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("Longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_status_isSet) {
        obj.insert(QString("Status"), ::OpenAPI::toJsonValue(m_status));
    }
    return obj;
}

QString OAISiteResult::getDescription() const {
    return m_description;
}
void OAISiteResult::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISiteResult::is_description_Set() const{
    return m_description_isSet;
}

bool OAISiteResult::is_description_Valid() const{
    return m_description_isValid;
}

QString OAISiteResult::getId() const {
    return m_id;
}
void OAISiteResult::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISiteResult::is_id_Set() const{
    return m_id_isSet;
}

bool OAISiteResult::is_id_Valid() const{
    return m_id_isValid;
}

double OAISiteResult::getLatitude() const {
    return m_latitude;
}
void OAISiteResult::setLatitude(const double &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAISiteResult::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAISiteResult::is_latitude_Valid() const{
    return m_latitude_isValid;
}

double OAISiteResult::getLongitude() const {
    return m_longitude;
}
void OAISiteResult::setLongitude(const double &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAISiteResult::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAISiteResult::is_longitude_Valid() const{
    return m_longitude_isValid;
}

QString OAISiteResult::getName() const {
    return m_name;
}
void OAISiteResult::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAISiteResult::is_name_Set() const{
    return m_name_isSet;
}

bool OAISiteResult::is_name_Valid() const{
    return m_name_isValid;
}

QString OAISiteResult::getStatus() const {
    return m_status;
}
void OAISiteResult::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISiteResult::is_status_Set() const{
    return m_status_isSet;
}

bool OAISiteResult::is_status_Valid() const{
    return m_status_isValid;
}

bool OAISiteResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISiteResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
