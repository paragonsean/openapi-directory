/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomerSettingsRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerSettingsRequest::OAICustomerSettingsRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerSettingsRequest::OAICustomerSettingsRequest() {
    this->initializeModel();
}

OAICustomerSettingsRequest::~OAICustomerSettingsRequest() {}

void OAICustomerSettingsRequest::initializeModel() {

    m_home_room_parent_name_isSet = false;
    m_home_room_parent_name_isValid = false;

    m_home_room_quota_isSet = false;
    m_home_room_quota_isValid = false;

    m_home_rooms_active_isSet = false;
    m_home_rooms_active_isValid = false;
}

void OAICustomerSettingsRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerSettingsRequest::fromJsonObject(QJsonObject json) {

    m_home_room_parent_name_isValid = ::OpenAPI::fromJsonValue(m_home_room_parent_name, json[QString("homeRoomParentName")]);
    m_home_room_parent_name_isSet = !json[QString("homeRoomParentName")].isNull() && m_home_room_parent_name_isValid;

    m_home_room_quota_isValid = ::OpenAPI::fromJsonValue(m_home_room_quota, json[QString("homeRoomQuota")]);
    m_home_room_quota_isSet = !json[QString("homeRoomQuota")].isNull() && m_home_room_quota_isValid;

    m_home_rooms_active_isValid = ::OpenAPI::fromJsonValue(m_home_rooms_active, json[QString("homeRoomsActive")]);
    m_home_rooms_active_isSet = !json[QString("homeRoomsActive")].isNull() && m_home_rooms_active_isValid;
}

QString OAICustomerSettingsRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerSettingsRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_home_room_parent_name_isSet) {
        obj.insert(QString("homeRoomParentName"), ::OpenAPI::toJsonValue(m_home_room_parent_name));
    }
    if (m_home_room_quota_isSet) {
        obj.insert(QString("homeRoomQuota"), ::OpenAPI::toJsonValue(m_home_room_quota));
    }
    if (m_home_rooms_active_isSet) {
        obj.insert(QString("homeRoomsActive"), ::OpenAPI::toJsonValue(m_home_rooms_active));
    }
    return obj;
}

QString OAICustomerSettingsRequest::getHomeRoomParentName() const {
    return m_home_room_parent_name;
}
void OAICustomerSettingsRequest::setHomeRoomParentName(const QString &home_room_parent_name) {
    m_home_room_parent_name = home_room_parent_name;
    m_home_room_parent_name_isSet = true;
}

bool OAICustomerSettingsRequest::is_home_room_parent_name_Set() const{
    return m_home_room_parent_name_isSet;
}

bool OAICustomerSettingsRequest::is_home_room_parent_name_Valid() const{
    return m_home_room_parent_name_isValid;
}

qint64 OAICustomerSettingsRequest::getHomeRoomQuota() const {
    return m_home_room_quota;
}
void OAICustomerSettingsRequest::setHomeRoomQuota(const qint64 &home_room_quota) {
    m_home_room_quota = home_room_quota;
    m_home_room_quota_isSet = true;
}

bool OAICustomerSettingsRequest::is_home_room_quota_Set() const{
    return m_home_room_quota_isSet;
}

bool OAICustomerSettingsRequest::is_home_room_quota_Valid() const{
    return m_home_room_quota_isValid;
}

bool OAICustomerSettingsRequest::isHomeRoomsActive() const {
    return m_home_rooms_active;
}
void OAICustomerSettingsRequest::setHomeRoomsActive(const bool &home_rooms_active) {
    m_home_rooms_active = home_rooms_active;
    m_home_rooms_active_isSet = true;
}

bool OAICustomerSettingsRequest::is_home_rooms_active_Set() const{
    return m_home_rooms_active_isSet;
}

bool OAICustomerSettingsRequest::is_home_rooms_active_Valid() const{
    return m_home_rooms_active_isValid;
}

bool OAICustomerSettingsRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_home_room_parent_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_room_quota_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_rooms_active_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerSettingsRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
