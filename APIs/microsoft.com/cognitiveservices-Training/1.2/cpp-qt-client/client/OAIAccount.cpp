/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccount.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccount::OAIAccount(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccount::OAIAccount() {
    this->initializeModel();
}

OAIAccount::~OAIAccount() {}

void OAIAccount::initializeModel() {

    m_email_isSet = false;
    m_email_isValid = false;

    m_keys_isSet = false;
    m_keys_isValid = false;

    m_quotas_isSet = false;
    m_quotas_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIAccount::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccount::fromJsonObject(QJsonObject json) {

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("Email")]);
    m_email_isSet = !json[QString("Email")].isNull() && m_email_isValid;

    m_keys_isValid = ::OpenAPI::fromJsonValue(m_keys, json[QString("Keys")]);
    m_keys_isSet = !json[QString("Keys")].isNull() && m_keys_isValid;

    m_quotas_isValid = ::OpenAPI::fromJsonValue(m_quotas, json[QString("Quotas")]);
    m_quotas_isSet = !json[QString("Quotas")].isNull() && m_quotas_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("UserName")]);
    m_user_name_isSet = !json[QString("UserName")].isNull() && m_user_name_isValid;
}

QString OAIAccount::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccount::asJsonObject() const {
    QJsonObject obj;
    if (m_email_isSet) {
        obj.insert(QString("Email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_keys.isSet()) {
        obj.insert(QString("Keys"), ::OpenAPI::toJsonValue(m_keys));
    }
    if (m_quotas.isSet()) {
        obj.insert(QString("Quotas"), ::OpenAPI::toJsonValue(m_quotas));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("UserName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

QString OAIAccount::getEmail() const {
    return m_email;
}
void OAIAccount::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAccount::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAccount::is_email_Valid() const{
    return m_email_isValid;
}

OAIApiKeys OAIAccount::getKeys() const {
    return m_keys;
}
void OAIAccount::setKeys(const OAIApiKeys &keys) {
    m_keys = keys;
    m_keys_isSet = true;
}

bool OAIAccount::is_keys_Set() const{
    return m_keys_isSet;
}

bool OAIAccount::is_keys_Valid() const{
    return m_keys_isValid;
}

OAIAccountQuota OAIAccount::getQuotas() const {
    return m_quotas;
}
void OAIAccount::setQuotas(const OAIAccountQuota &quotas) {
    m_quotas = quotas;
    m_quotas_isSet = true;
}

bool OAIAccount::is_quotas_Set() const{
    return m_quotas_isSet;
}

bool OAIAccount::is_quotas_Valid() const{
    return m_quotas_isValid;
}

QString OAIAccount::getUserName() const {
    return m_user_name;
}
void OAIAccount::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIAccount::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIAccount::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIAccount::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_keys.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_quotas.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccount::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
