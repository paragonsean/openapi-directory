/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGitHubAccount.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGitHubAccount::OAIGitHubAccount(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGitHubAccount::OAIGitHubAccount() {
    this->initializeModel();
}

OAIGitHubAccount::~OAIGitHubAccount() {}

void OAIGitHubAccount::initializeModel() {

    m_account_type_isSet = false;
    m_account_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIGitHubAccount::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGitHubAccount::fromJsonObject(QJsonObject json) {

    m_account_type_isValid = ::OpenAPI::fromJsonValue(m_account_type, json[QString("accountType")]);
    m_account_type_isSet = !json[QString("accountType")].isNull() && m_account_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIGitHubAccount::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGitHubAccount::asJsonObject() const {
    QJsonObject obj;
    if (m_account_type_isSet) {
        obj.insert(QString("accountType"), ::OpenAPI::toJsonValue(m_account_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIGitHubAccount::getAccountType() const {
    return m_account_type;
}
void OAIGitHubAccount::setAccountType(const QString &account_type) {
    m_account_type = account_type;
    m_account_type_isSet = true;
}

bool OAIGitHubAccount::is_account_type_Set() const{
    return m_account_type_isSet;
}

bool OAIGitHubAccount::is_account_type_Valid() const{
    return m_account_type_isValid;
}

qint32 OAIGitHubAccount::getId() const {
    return m_id;
}
void OAIGitHubAccount::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGitHubAccount::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGitHubAccount::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIGitHubAccount::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGitHubAccount::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
