/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAccounts.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccounts::OAIAccounts(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccounts::OAIAccounts() {
    this->initializeModel();
}

OAIAccounts::~OAIAccounts() {}

void OAIAccounts::initializeModel() {

    m_accounts_isSet = false;
    m_accounts_isValid = false;
}

void OAIAccounts::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccounts::fromJsonObject(QJsonObject json) {

    m_accounts_isValid = ::OpenAPI::fromJsonValue(m_accounts, json[QString("accounts")]);
    m_accounts_isSet = !json[QString("accounts")].isNull() && m_accounts_isValid;
}

QString OAIAccounts::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccounts::asJsonObject() const {
    QJsonObject obj;
    if (m_accounts.size() > 0) {
        obj.insert(QString("accounts"), ::OpenAPI::toJsonValue(m_accounts));
    }
    return obj;
}

QList<OAIAccount> OAIAccounts::getAccounts() const {
    return m_accounts;
}
void OAIAccounts::setAccounts(const QList<OAIAccount> &accounts) {
    m_accounts = accounts;
    m_accounts_isSet = true;
}

bool OAIAccounts::is_accounts_Set() const{
    return m_accounts_isSet;
}

bool OAIAccounts::is_accounts_Valid() const{
    return m_accounts_isValid;
}

bool OAIAccounts::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccounts::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
