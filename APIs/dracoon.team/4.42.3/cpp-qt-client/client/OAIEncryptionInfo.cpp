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

#include "OAIEncryptionInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEncryptionInfo::OAIEncryptionInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEncryptionInfo::OAIEncryptionInfo() {
    this->initializeModel();
}

OAIEncryptionInfo::~OAIEncryptionInfo() {}

void OAIEncryptionInfo::initializeModel() {

    m_data_space_key_state_isSet = false;
    m_data_space_key_state_isValid = false;

    m_room_key_state_isSet = false;
    m_room_key_state_isValid = false;

    m_user_key_state_isSet = false;
    m_user_key_state_isValid = false;
}

void OAIEncryptionInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEncryptionInfo::fromJsonObject(QJsonObject json) {

    m_data_space_key_state_isValid = ::OpenAPI::fromJsonValue(m_data_space_key_state, json[QString("dataSpaceKeyState")]);
    m_data_space_key_state_isSet = !json[QString("dataSpaceKeyState")].isNull() && m_data_space_key_state_isValid;

    m_room_key_state_isValid = ::OpenAPI::fromJsonValue(m_room_key_state, json[QString("roomKeyState")]);
    m_room_key_state_isSet = !json[QString("roomKeyState")].isNull() && m_room_key_state_isValid;

    m_user_key_state_isValid = ::OpenAPI::fromJsonValue(m_user_key_state, json[QString("userKeyState")]);
    m_user_key_state_isSet = !json[QString("userKeyState")].isNull() && m_user_key_state_isValid;
}

QString OAIEncryptionInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEncryptionInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_data_space_key_state_isSet) {
        obj.insert(QString("dataSpaceKeyState"), ::OpenAPI::toJsonValue(m_data_space_key_state));
    }
    if (m_room_key_state_isSet) {
        obj.insert(QString("roomKeyState"), ::OpenAPI::toJsonValue(m_room_key_state));
    }
    if (m_user_key_state_isSet) {
        obj.insert(QString("userKeyState"), ::OpenAPI::toJsonValue(m_user_key_state));
    }
    return obj;
}

QString OAIEncryptionInfo::getDataSpaceKeyState() const {
    return m_data_space_key_state;
}
void OAIEncryptionInfo::setDataSpaceKeyState(const QString &data_space_key_state) {
    m_data_space_key_state = data_space_key_state;
    m_data_space_key_state_isSet = true;
}

bool OAIEncryptionInfo::is_data_space_key_state_Set() const{
    return m_data_space_key_state_isSet;
}

bool OAIEncryptionInfo::is_data_space_key_state_Valid() const{
    return m_data_space_key_state_isValid;
}

QString OAIEncryptionInfo::getRoomKeyState() const {
    return m_room_key_state;
}
void OAIEncryptionInfo::setRoomKeyState(const QString &room_key_state) {
    m_room_key_state = room_key_state;
    m_room_key_state_isSet = true;
}

bool OAIEncryptionInfo::is_room_key_state_Set() const{
    return m_room_key_state_isSet;
}

bool OAIEncryptionInfo::is_room_key_state_Valid() const{
    return m_room_key_state_isValid;
}

QString OAIEncryptionInfo::getUserKeyState() const {
    return m_user_key_state;
}
void OAIEncryptionInfo::setUserKeyState(const QString &user_key_state) {
    m_user_key_state = user_key_state;
    m_user_key_state_isSet = true;
}

bool OAIEncryptionInfo::is_user_key_state_Set() const{
    return m_user_key_state_isSet;
}

bool OAIEncryptionInfo::is_user_key_state_Valid() const{
    return m_user_key_state_isValid;
}

bool OAIEncryptionInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_space_key_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_room_key_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_key_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEncryptionInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_space_key_state_isValid && m_room_key_state_isValid && m_user_key_state_isValid && true;
}

} // namespace OpenAPI
