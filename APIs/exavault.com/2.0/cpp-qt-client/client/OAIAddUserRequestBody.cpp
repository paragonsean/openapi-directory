/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddUserRequestBody.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddUserRequestBody::OAIAddUserRequestBody(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddUserRequestBody::OAIAddUserRequestBody() {
    this->initializeModel();
}

OAIAddUserRequestBody::~OAIAddUserRequestBody() {}

void OAIAddUserRequestBody::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_expiration_isSet = false;
    m_expiration_isValid = false;

    m_home_resource_isSet = false;
    m_home_resource_isValid = false;

    m_locked_isSet = false;
    m_locked_isValid = false;

    m_nickname_isSet = false;
    m_nickname_isValid = false;

    m_onboarding_isSet = false;
    m_onboarding_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_permissions_isSet = false;
    m_permissions_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;

    m_time_zone_isSet = false;
    m_time_zone_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_welcome_email_isSet = false;
    m_welcome_email_isValid = false;
}

void OAIAddUserRequestBody::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddUserRequestBody::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_expiration_isValid = ::OpenAPI::fromJsonValue(m_expiration, json[QString("expiration")]);
    m_expiration_isSet = !json[QString("expiration")].isNull() && m_expiration_isValid;

    m_home_resource_isValid = ::OpenAPI::fromJsonValue(m_home_resource, json[QString("homeResource")]);
    m_home_resource_isSet = !json[QString("homeResource")].isNull() && m_home_resource_isValid;

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;

    m_nickname_isValid = ::OpenAPI::fromJsonValue(m_nickname, json[QString("nickname")]);
    m_nickname_isSet = !json[QString("nickname")].isNull() && m_nickname_isValid;

    m_onboarding_isValid = ::OpenAPI::fromJsonValue(m_onboarding, json[QString("onboarding")]);
    m_onboarding_isSet = !json[QString("onboarding")].isNull() && m_onboarding_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_permissions_isValid = ::OpenAPI::fromJsonValue(m_permissions, json[QString("permissions")]);
    m_permissions_isSet = !json[QString("permissions")].isNull() && m_permissions_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;

    m_time_zone_isValid = ::OpenAPI::fromJsonValue(m_time_zone, json[QString("timeZone")]);
    m_time_zone_isSet = !json[QString("timeZone")].isNull() && m_time_zone_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_welcome_email_isValid = ::OpenAPI::fromJsonValue(m_welcome_email, json[QString("welcomeEmail")]);
    m_welcome_email_isSet = !json[QString("welcomeEmail")].isNull() && m_welcome_email_isValid;
}

QString OAIAddUserRequestBody::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddUserRequestBody::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_expiration_isSet) {
        obj.insert(QString("expiration"), ::OpenAPI::toJsonValue(m_expiration));
    }
    if (m_home_resource_isSet) {
        obj.insert(QString("homeResource"), ::OpenAPI::toJsonValue(m_home_resource));
    }
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    if (m_nickname_isSet) {
        obj.insert(QString("nickname"), ::OpenAPI::toJsonValue(m_nickname));
    }
    if (m_onboarding_isSet) {
        obj.insert(QString("onboarding"), ::OpenAPI::toJsonValue(m_onboarding));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_permissions.isSet()) {
        obj.insert(QString("permissions"), ::OpenAPI::toJsonValue(m_permissions));
    }
    if (m_role_isSet) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    if (m_time_zone_isSet) {
        obj.insert(QString("timeZone"), ::OpenAPI::toJsonValue(m_time_zone));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_welcome_email_isSet) {
        obj.insert(QString("welcomeEmail"), ::OpenAPI::toJsonValue(m_welcome_email));
    }
    return obj;
}

QString OAIAddUserRequestBody::getEmail() const {
    return m_email;
}
void OAIAddUserRequestBody::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAddUserRequestBody::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAddUserRequestBody::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAddUserRequestBody::getExpiration() const {
    return m_expiration;
}
void OAIAddUserRequestBody::setExpiration(const QString &expiration) {
    m_expiration = expiration;
    m_expiration_isSet = true;
}

bool OAIAddUserRequestBody::is_expiration_Set() const{
    return m_expiration_isSet;
}

bool OAIAddUserRequestBody::is_expiration_Valid() const{
    return m_expiration_isValid;
}

QString OAIAddUserRequestBody::getHomeResource() const {
    return m_home_resource;
}
void OAIAddUserRequestBody::setHomeResource(const QString &home_resource) {
    m_home_resource = home_resource;
    m_home_resource_isSet = true;
}

bool OAIAddUserRequestBody::is_home_resource_Set() const{
    return m_home_resource_isSet;
}

bool OAIAddUserRequestBody::is_home_resource_Valid() const{
    return m_home_resource_isValid;
}

bool OAIAddUserRequestBody::isLocked() const {
    return m_locked;
}
void OAIAddUserRequestBody::setLocked(const bool &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAIAddUserRequestBody::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAIAddUserRequestBody::is_locked_Valid() const{
    return m_locked_isValid;
}

QString OAIAddUserRequestBody::getNickname() const {
    return m_nickname;
}
void OAIAddUserRequestBody::setNickname(const QString &nickname) {
    m_nickname = nickname;
    m_nickname_isSet = true;
}

bool OAIAddUserRequestBody::is_nickname_Set() const{
    return m_nickname_isSet;
}

bool OAIAddUserRequestBody::is_nickname_Valid() const{
    return m_nickname_isValid;
}

bool OAIAddUserRequestBody::isOnboarding() const {
    return m_onboarding;
}
void OAIAddUserRequestBody::setOnboarding(const bool &onboarding) {
    m_onboarding = onboarding;
    m_onboarding_isSet = true;
}

bool OAIAddUserRequestBody::is_onboarding_Set() const{
    return m_onboarding_isSet;
}

bool OAIAddUserRequestBody::is_onboarding_Valid() const{
    return m_onboarding_isValid;
}

QString OAIAddUserRequestBody::getPassword() const {
    return m_password;
}
void OAIAddUserRequestBody::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIAddUserRequestBody::is_password_Set() const{
    return m_password_isSet;
}

bool OAIAddUserRequestBody::is_password_Valid() const{
    return m_password_isValid;
}

OAIAddUserRequestBody_permissions OAIAddUserRequestBody::getPermissions() const {
    return m_permissions;
}
void OAIAddUserRequestBody::setPermissions(const OAIAddUserRequestBody_permissions &permissions) {
    m_permissions = permissions;
    m_permissions_isSet = true;
}

bool OAIAddUserRequestBody::is_permissions_Set() const{
    return m_permissions_isSet;
}

bool OAIAddUserRequestBody::is_permissions_Valid() const{
    return m_permissions_isValid;
}

QString OAIAddUserRequestBody::getRole() const {
    return m_role;
}
void OAIAddUserRequestBody::setRole(const QString &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIAddUserRequestBody::is_role_Set() const{
    return m_role_isSet;
}

bool OAIAddUserRequestBody::is_role_Valid() const{
    return m_role_isValid;
}

QString OAIAddUserRequestBody::getTimeZone() const {
    return m_time_zone;
}
void OAIAddUserRequestBody::setTimeZone(const QString &time_zone) {
    m_time_zone = time_zone;
    m_time_zone_isSet = true;
}

bool OAIAddUserRequestBody::is_time_zone_Set() const{
    return m_time_zone_isSet;
}

bool OAIAddUserRequestBody::is_time_zone_Valid() const{
    return m_time_zone_isValid;
}

QString OAIAddUserRequestBody::getUsername() const {
    return m_username;
}
void OAIAddUserRequestBody::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIAddUserRequestBody::is_username_Set() const{
    return m_username_isSet;
}

bool OAIAddUserRequestBody::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIAddUserRequestBody::isWelcomeEmail() const {
    return m_welcome_email;
}
void OAIAddUserRequestBody::setWelcomeEmail(const bool &welcome_email) {
    m_welcome_email = welcome_email;
    m_welcome_email_isSet = true;
}

bool OAIAddUserRequestBody::is_welcome_email_Set() const{
    return m_welcome_email_isSet;
}

bool OAIAddUserRequestBody::is_welcome_email_Valid() const{
    return m_welcome_email_isValid;
}

bool OAIAddUserRequestBody::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_home_resource_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nickname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_onboarding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_permissions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_role_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_welcome_email_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddUserRequestBody::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && m_home_resource_isValid && m_password_isValid && m_permissions_isValid && m_role_isValid && m_time_zone_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
