/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateNetworkMerakiAuthUser_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkMerakiAuthUser_request::OAIUpdateNetworkMerakiAuthUser_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkMerakiAuthUser_request::OAIUpdateNetworkMerakiAuthUser_request() {
    this->initializeModel();
}

OAIUpdateNetworkMerakiAuthUser_request::~OAIUpdateNetworkMerakiAuthUser_request() {}

void OAIUpdateNetworkMerakiAuthUser_request::initializeModel() {

    m_authorizations_isSet = false;
    m_authorizations_isValid = false;

    m_email_password_to_user_isSet = false;
    m_email_password_to_user_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;
}

void OAIUpdateNetworkMerakiAuthUser_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkMerakiAuthUser_request::fromJsonObject(QJsonObject json) {

    m_authorizations_isValid = ::OpenAPI::fromJsonValue(m_authorizations, json[QString("authorizations")]);
    m_authorizations_isSet = !json[QString("authorizations")].isNull() && m_authorizations_isValid;

    m_email_password_to_user_isValid = ::OpenAPI::fromJsonValue(m_email_password_to_user, json[QString("emailPasswordToUser")]);
    m_email_password_to_user_isSet = !json[QString("emailPasswordToUser")].isNull() && m_email_password_to_user_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;
}

QString OAIUpdateNetworkMerakiAuthUser_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkMerakiAuthUser_request::asJsonObject() const {
    QJsonObject obj;
    if (m_authorizations.size() > 0) {
        obj.insert(QString("authorizations"), ::OpenAPI::toJsonValue(m_authorizations));
    }
    if (m_email_password_to_user_isSet) {
        obj.insert(QString("emailPasswordToUser"), ::OpenAPI::toJsonValue(m_email_password_to_user));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    return obj;
}

QList<OAIUpdateNetworkMerakiAuthUser_request_authorizations_inner> OAIUpdateNetworkMerakiAuthUser_request::getAuthorizations() const {
    return m_authorizations;
}
void OAIUpdateNetworkMerakiAuthUser_request::setAuthorizations(const QList<OAIUpdateNetworkMerakiAuthUser_request_authorizations_inner> &authorizations) {
    m_authorizations = authorizations;
    m_authorizations_isSet = true;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_authorizations_Set() const{
    return m_authorizations_isSet;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_authorizations_Valid() const{
    return m_authorizations_isValid;
}

bool OAIUpdateNetworkMerakiAuthUser_request::isEmailPasswordToUser() const {
    return m_email_password_to_user;
}
void OAIUpdateNetworkMerakiAuthUser_request::setEmailPasswordToUser(const bool &email_password_to_user) {
    m_email_password_to_user = email_password_to_user;
    m_email_password_to_user_isSet = true;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_email_password_to_user_Set() const{
    return m_email_password_to_user_isSet;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_email_password_to_user_Valid() const{
    return m_email_password_to_user_isValid;
}

QString OAIUpdateNetworkMerakiAuthUser_request::getName() const {
    return m_name;
}
void OAIUpdateNetworkMerakiAuthUser_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateNetworkMerakiAuthUser_request::getPassword() const {
    return m_password;
}
void OAIUpdateNetworkMerakiAuthUser_request::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUpdateNetworkMerakiAuthUser_request::is_password_Valid() const{
    return m_password_isValid;
}

bool OAIUpdateNetworkMerakiAuthUser_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_authorizations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_password_to_user_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkMerakiAuthUser_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
