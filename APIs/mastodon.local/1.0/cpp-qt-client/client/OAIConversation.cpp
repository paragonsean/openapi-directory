/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConversation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConversation::OAIConversation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConversation::OAIConversation() {
    this->initializeModel();
}

OAIConversation::~OAIConversation() {}

void OAIConversation::initializeModel() {

    m_accounts_isSet = false;
    m_accounts_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_status_isSet = false;
    m_last_status_isValid = false;

    m_unread_isSet = false;
    m_unread_isValid = false;
}

void OAIConversation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConversation::fromJsonObject(QJsonObject json) {

    m_accounts_isValid = ::OpenAPI::fromJsonValue(m_accounts, json[QString("accounts")]);
    m_accounts_isSet = !json[QString("accounts")].isNull() && m_accounts_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_status_isValid = ::OpenAPI::fromJsonValue(m_last_status, json[QString("last_status")]);
    m_last_status_isSet = !json[QString("last_status")].isNull() && m_last_status_isValid;

    m_unread_isValid = ::OpenAPI::fromJsonValue(m_unread, json[QString("unread")]);
    m_unread_isSet = !json[QString("unread")].isNull() && m_unread_isValid;
}

QString OAIConversation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConversation::asJsonObject() const {
    QJsonObject obj;
    if (m_accounts.size() > 0) {
        obj.insert(QString("accounts"), ::OpenAPI::toJsonValue(m_accounts));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_status.isSet()) {
        obj.insert(QString("last_status"), ::OpenAPI::toJsonValue(m_last_status));
    }
    if (m_unread_isSet) {
        obj.insert(QString("unread"), ::OpenAPI::toJsonValue(m_unread));
    }
    return obj;
}

QList<OAIAccount> OAIConversation::getAccounts() const {
    return m_accounts;
}
void OAIConversation::setAccounts(const QList<OAIAccount> &accounts) {
    m_accounts = accounts;
    m_accounts_isSet = true;
}

bool OAIConversation::is_accounts_Set() const{
    return m_accounts_isSet;
}

bool OAIConversation::is_accounts_Valid() const{
    return m_accounts_isValid;
}

QString OAIConversation::getId() const {
    return m_id;
}
void OAIConversation::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIConversation::is_id_Set() const{
    return m_id_isSet;
}

bool OAIConversation::is_id_Valid() const{
    return m_id_isValid;
}

OAIStatus OAIConversation::getLastStatus() const {
    return m_last_status;
}
void OAIConversation::setLastStatus(const OAIStatus &last_status) {
    m_last_status = last_status;
    m_last_status_isSet = true;
}

bool OAIConversation::is_last_status_Set() const{
    return m_last_status_isSet;
}

bool OAIConversation::is_last_status_Valid() const{
    return m_last_status_isValid;
}

bool OAIConversation::isUnread() const {
    return m_unread;
}
void OAIConversation::setUnread(const bool &unread) {
    m_unread = unread;
    m_unread_isSet = true;
}

bool OAIConversation::is_unread_Set() const{
    return m_unread_isSet;
}

bool OAIConversation::is_unread_Valid() const{
    return m_unread_isValid;
}

bool OAIConversation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_unread_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConversation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_accounts_isValid && m_id_isValid && m_unread_isValid && true;
}

} // namespace OpenAPI
