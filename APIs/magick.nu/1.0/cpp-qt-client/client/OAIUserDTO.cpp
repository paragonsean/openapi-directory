/**
 * Tradeworks
 * Authentication is required to access all methods of the API. Enter username and password.                 Credentials are automatically set as you type.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserDTO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserDTO::OAIUserDTO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserDTO::OAIUserDTO() {
    this->initializeModel();
}

OAIUserDTO::~OAIUserDTO() {}

void OAIUserDTO::initializeModel() {

    m_affiliate_id_isSet = false;
    m_affiliate_id_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_subscription_type_isSet = false;
    m_subscription_type_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIUserDTO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserDTO::fromJsonObject(QJsonObject json) {

    m_affiliate_id_isValid = ::OpenAPI::fromJsonValue(m_affiliate_id, json[QString("affiliateId")]);
    m_affiliate_id_isSet = !json[QString("affiliateId")].isNull() && m_affiliate_id_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_subscription_type_isValid = ::OpenAPI::fromJsonValue(m_subscription_type, json[QString("subscriptionType")]);
    m_subscription_type_isSet = !json[QString("subscriptionType")].isNull() && m_subscription_type_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIUserDTO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserDTO::asJsonObject() const {
    QJsonObject obj;
    if (m_affiliate_id_isSet) {
        obj.insert(QString("affiliateId"), ::OpenAPI::toJsonValue(m_affiliate_id));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_subscription_type_isSet) {
        obj.insert(QString("subscriptionType"), ::OpenAPI::toJsonValue(m_subscription_type));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIUserDTO::getAffiliateId() const {
    return m_affiliate_id;
}
void OAIUserDTO::setAffiliateId(const QString &affiliate_id) {
    m_affiliate_id = affiliate_id;
    m_affiliate_id_isSet = true;
}

bool OAIUserDTO::is_affiliate_id_Set() const{
    return m_affiliate_id_isSet;
}

bool OAIUserDTO::is_affiliate_id_Valid() const{
    return m_affiliate_id_isValid;
}

QString OAIUserDTO::getEmail() const {
    return m_email;
}
void OAIUserDTO::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUserDTO::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUserDTO::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIUserDTO::getFirstName() const {
    return m_first_name;
}
void OAIUserDTO::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIUserDTO::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIUserDTO::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIUserDTO::getLastName() const {
    return m_last_name;
}
void OAIUserDTO::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIUserDTO::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIUserDTO::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIUserDTO::getPassword() const {
    return m_password;
}
void OAIUserDTO::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUserDTO::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUserDTO::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIUserDTO::getSubscriptionType() const {
    return m_subscription_type;
}
void OAIUserDTO::setSubscriptionType(const QString &subscription_type) {
    m_subscription_type = subscription_type;
    m_subscription_type_isSet = true;
}

bool OAIUserDTO::is_subscription_type_Set() const{
    return m_subscription_type_isSet;
}

bool OAIUserDTO::is_subscription_type_Valid() const{
    return m_subscription_type_isValid;
}

QString OAIUserDTO::getUsername() const {
    return m_username;
}
void OAIUserDTO::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIUserDTO::is_username_Set() const{
    return m_username_isSet;
}

bool OAIUserDTO::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIUserDTO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_affiliate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserDTO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
