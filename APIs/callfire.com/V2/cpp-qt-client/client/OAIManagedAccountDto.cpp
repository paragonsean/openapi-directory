/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIManagedAccountDto.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIManagedAccountDto::OAIManagedAccountDto(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIManagedAccountDto::OAIManagedAccountDto() {
    this->initializeModel();
}

OAIManagedAccountDto::~OAIManagedAccountDto() {}

void OAIManagedAccountDto::initializeModel() {

    m_account_holder_id_isSet = false;
    m_account_holder_id_isValid = false;

    m_credits_isSet = false;
    m_credits_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_login_isSet = false;
    m_last_login_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIManagedAccountDto::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIManagedAccountDto::fromJsonObject(QJsonObject json) {

    m_account_holder_id_isValid = ::OpenAPI::fromJsonValue(m_account_holder_id, json[QString("accountHolderId")]);
    m_account_holder_id_isSet = !json[QString("accountHolderId")].isNull() && m_account_holder_id_isValid;

    m_credits_isValid = ::OpenAPI::fromJsonValue(m_credits, json[QString("credits")]);
    m_credits_isSet = !json[QString("credits")].isNull() && m_credits_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_login_isValid = ::OpenAPI::fromJsonValue(m_last_login, json[QString("lastLogin")]);
    m_last_login_isSet = !json[QString("lastLogin")].isNull() && m_last_login_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIManagedAccountDto::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIManagedAccountDto::asJsonObject() const {
    QJsonObject obj;
    if (m_account_holder_id_isSet) {
        obj.insert(QString("accountHolderId"), ::OpenAPI::toJsonValue(m_account_holder_id));
    }
    if (m_credits_isSet) {
        obj.insert(QString("credits"), ::OpenAPI::toJsonValue(m_credits));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_login_isSet) {
        obj.insert(QString("lastLogin"), ::OpenAPI::toJsonValue(m_last_login));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

QString OAIManagedAccountDto::getAccountHolderId() const {
    return m_account_holder_id;
}
void OAIManagedAccountDto::setAccountHolderId(const QString &account_holder_id) {
    m_account_holder_id = account_holder_id;
    m_account_holder_id_isSet = true;
}

bool OAIManagedAccountDto::is_account_holder_id_Set() const{
    return m_account_holder_id_isSet;
}

bool OAIManagedAccountDto::is_account_holder_id_Valid() const{
    return m_account_holder_id_isValid;
}

double OAIManagedAccountDto::getCredits() const {
    return m_credits;
}
void OAIManagedAccountDto::setCredits(const double &credits) {
    m_credits = credits;
    m_credits_isSet = true;
}

bool OAIManagedAccountDto::is_credits_Set() const{
    return m_credits_isSet;
}

bool OAIManagedAccountDto::is_credits_Valid() const{
    return m_credits_isValid;
}

QString OAIManagedAccountDto::getEmail() const {
    return m_email;
}
void OAIManagedAccountDto::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIManagedAccountDto::is_email_Set() const{
    return m_email_isSet;
}

bool OAIManagedAccountDto::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIManagedAccountDto::getId() const {
    return m_id;
}
void OAIManagedAccountDto::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIManagedAccountDto::is_id_Set() const{
    return m_id_isSet;
}

bool OAIManagedAccountDto::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIManagedAccountDto::getLastLogin() const {
    return m_last_login;
}
void OAIManagedAccountDto::setLastLogin(const QDateTime &last_login) {
    m_last_login = last_login;
    m_last_login_isSet = true;
}

bool OAIManagedAccountDto::is_last_login_Set() const{
    return m_last_login_isSet;
}

bool OAIManagedAccountDto::is_last_login_Valid() const{
    return m_last_login_isValid;
}

QString OAIManagedAccountDto::getName() const {
    return m_name;
}
void OAIManagedAccountDto::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIManagedAccountDto::is_name_Set() const{
    return m_name_isSet;
}

bool OAIManagedAccountDto::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIManagedAccountDto::getState() const {
    return m_state;
}
void OAIManagedAccountDto::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIManagedAccountDto::is_state_Set() const{
    return m_state_isSet;
}

bool OAIManagedAccountDto::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIManagedAccountDto::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_holder_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credits_isSet) {
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

        if (m_last_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIManagedAccountDto::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
