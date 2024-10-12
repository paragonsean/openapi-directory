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

#include "OAIRoomUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRoomUser::OAIRoomUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRoomUser::OAIRoomUser() {
    this->initializeModel();
}

OAIRoomUser::~OAIRoomUser() {}

void OAIRoomUser::initializeModel() {

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_granted_isSet = false;
    m_is_granted_isValid = false;

    m_login_isSet = false;
    m_login_isValid = false;

    m_permissions_isSet = false;
    m_permissions_isValid = false;

    m_public_key_container_isSet = false;
    m_public_key_container_isValid = false;

    m_user_info_isSet = false;
    m_user_info_isValid = false;
}

void OAIRoomUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRoomUser::fromJsonObject(QJsonObject json) {

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_granted_isValid = ::OpenAPI::fromJsonValue(m_is_granted, json[QString("isGranted")]);
    m_is_granted_isSet = !json[QString("isGranted")].isNull() && m_is_granted_isValid;

    m_login_isValid = ::OpenAPI::fromJsonValue(m_login, json[QString("login")]);
    m_login_isSet = !json[QString("login")].isNull() && m_login_isValid;

    m_permissions_isValid = ::OpenAPI::fromJsonValue(m_permissions, json[QString("permissions")]);
    m_permissions_isSet = !json[QString("permissions")].isNull() && m_permissions_isValid;

    m_public_key_container_isValid = ::OpenAPI::fromJsonValue(m_public_key_container, json[QString("publicKeyContainer")]);
    m_public_key_container_isSet = !json[QString("publicKeyContainer")].isNull() && m_public_key_container_isValid;

    m_user_info_isValid = ::OpenAPI::fromJsonValue(m_user_info, json[QString("userInfo")]);
    m_user_info_isSet = !json[QString("userInfo")].isNull() && m_user_info_isValid;
}

QString OAIRoomUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRoomUser::asJsonObject() const {
    QJsonObject obj;
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_granted_isSet) {
        obj.insert(QString("isGranted"), ::OpenAPI::toJsonValue(m_is_granted));
    }
    if (m_login_isSet) {
        obj.insert(QString("login"), ::OpenAPI::toJsonValue(m_login));
    }
    if (m_permissions.isSet()) {
        obj.insert(QString("permissions"), ::OpenAPI::toJsonValue(m_permissions));
    }
    if (m_public_key_container.isSet()) {
        obj.insert(QString("publicKeyContainer"), ::OpenAPI::toJsonValue(m_public_key_container));
    }
    if (m_user_info.isSet()) {
        obj.insert(QString("userInfo"), ::OpenAPI::toJsonValue(m_user_info));
    }
    return obj;
}

QString OAIRoomUser::getDisplayName() const {
    return m_display_name;
}
void OAIRoomUser::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIRoomUser::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIRoomUser::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIRoomUser::getEmail() const {
    return m_email;
}
void OAIRoomUser::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIRoomUser::is_email_Set() const{
    return m_email_isSet;
}

bool OAIRoomUser::is_email_Valid() const{
    return m_email_isValid;
}

qint64 OAIRoomUser::getId() const {
    return m_id;
}
void OAIRoomUser::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRoomUser::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRoomUser::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIRoomUser::isIsGranted() const {
    return m_is_granted;
}
void OAIRoomUser::setIsGranted(const bool &is_granted) {
    m_is_granted = is_granted;
    m_is_granted_isSet = true;
}

bool OAIRoomUser::is_is_granted_Set() const{
    return m_is_granted_isSet;
}

bool OAIRoomUser::is_is_granted_Valid() const{
    return m_is_granted_isValid;
}

QString OAIRoomUser::getLogin() const {
    return m_login;
}
void OAIRoomUser::setLogin(const QString &login) {
    m_login = login;
    m_login_isSet = true;
}

bool OAIRoomUser::is_login_Set() const{
    return m_login_isSet;
}

bool OAIRoomUser::is_login_Valid() const{
    return m_login_isValid;
}

OAINodePermissions OAIRoomUser::getPermissions() const {
    return m_permissions;
}
void OAIRoomUser::setPermissions(const OAINodePermissions &permissions) {
    m_permissions = permissions;
    m_permissions_isSet = true;
}

bool OAIRoomUser::is_permissions_Set() const{
    return m_permissions_isSet;
}

bool OAIRoomUser::is_permissions_Valid() const{
    return m_permissions_isValid;
}

OAIPublicKeyContainer OAIRoomUser::getPublicKeyContainer() const {
    return m_public_key_container;
}
void OAIRoomUser::setPublicKeyContainer(const OAIPublicKeyContainer &public_key_container) {
    m_public_key_container = public_key_container;
    m_public_key_container_isSet = true;
}

bool OAIRoomUser::is_public_key_container_Set() const{
    return m_public_key_container_isSet;
}

bool OAIRoomUser::is_public_key_container_Valid() const{
    return m_public_key_container_isValid;
}

OAIUserInfo OAIRoomUser::getUserInfo() const {
    return m_user_info;
}
void OAIRoomUser::setUserInfo(const OAIUserInfo &user_info) {
    m_user_info = user_info;
    m_user_info_isSet = true;
}

bool OAIRoomUser::is_user_info_Set() const{
    return m_user_info_isSet;
}

bool OAIRoomUser::is_user_info_Valid() const{
    return m_user_info_isValid;
}

bool OAIRoomUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_granted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_permissions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_key_container.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_info.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRoomUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_display_name_isValid && m_email_isValid && m_id_isValid && m_is_granted_isValid && m_login_isValid && m_user_info_isValid && true;
}

} // namespace OpenAPI
