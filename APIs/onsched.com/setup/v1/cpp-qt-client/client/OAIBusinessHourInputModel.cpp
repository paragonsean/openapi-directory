/**
 * OnSched Setup API
 * Build secure and scalable custom apps for onboarding and setup. Our flexible API provides many options for configuration.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBusinessHourInputModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBusinessHourInputModel::OAIBusinessHourInputModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBusinessHourInputModel::OAIBusinessHourInputModel() {
    this->initializeModel();
}

OAIBusinessHourInputModel::~OAIBusinessHourInputModel() {}

void OAIBusinessHourInputModel::initializeModel() {

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_is24_hours_isSet = false;
    m_is24_hours_isValid = false;

    m_is_open_isSet = false;
    m_is_open_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;
}

void OAIBusinessHourInputModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBusinessHourInputModel::fromJsonObject(QJsonObject json) {

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_is24_hours_isValid = ::OpenAPI::fromJsonValue(m_is24_hours, json[QString("is24Hours")]);
    m_is24_hours_isSet = !json[QString("is24Hours")].isNull() && m_is24_hours_isValid;

    m_is_open_isValid = ::OpenAPI::fromJsonValue(m_is_open, json[QString("isOpen")]);
    m_is_open_isSet = !json[QString("isOpen")].isNull() && m_is_open_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;
}

QString OAIBusinessHourInputModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBusinessHourInputModel::asJsonObject() const {
    QJsonObject obj;
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_is24_hours_isSet) {
        obj.insert(QString("is24Hours"), ::OpenAPI::toJsonValue(m_is24_hours));
    }
    if (m_is_open_isSet) {
        obj.insert(QString("isOpen"), ::OpenAPI::toJsonValue(m_is_open));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    return obj;
}

qint32 OAIBusinessHourInputModel::getEndTime() const {
    return m_end_time;
}
void OAIBusinessHourInputModel::setEndTime(const qint32 &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIBusinessHourInputModel::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIBusinessHourInputModel::is_end_time_Valid() const{
    return m_end_time_isValid;
}

bool OAIBusinessHourInputModel::isIs24Hours() const {
    return m_is24_hours;
}
void OAIBusinessHourInputModel::setIs24Hours(const bool &is24_hours) {
    m_is24_hours = is24_hours;
    m_is24_hours_isSet = true;
}

bool OAIBusinessHourInputModel::is_is24_hours_Set() const{
    return m_is24_hours_isSet;
}

bool OAIBusinessHourInputModel::is_is24_hours_Valid() const{
    return m_is24_hours_isValid;
}

bool OAIBusinessHourInputModel::isIsOpen() const {
    return m_is_open;
}
void OAIBusinessHourInputModel::setIsOpen(const bool &is_open) {
    m_is_open = is_open;
    m_is_open_isSet = true;
}

bool OAIBusinessHourInputModel::is_is_open_Set() const{
    return m_is_open_isSet;
}

bool OAIBusinessHourInputModel::is_is_open_Valid() const{
    return m_is_open_isValid;
}

qint32 OAIBusinessHourInputModel::getStartTime() const {
    return m_start_time;
}
void OAIBusinessHourInputModel::setStartTime(const qint32 &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIBusinessHourInputModel::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIBusinessHourInputModel::is_start_time_Valid() const{
    return m_start_time_isValid;
}

bool OAIBusinessHourInputModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is24_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_open_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBusinessHourInputModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
