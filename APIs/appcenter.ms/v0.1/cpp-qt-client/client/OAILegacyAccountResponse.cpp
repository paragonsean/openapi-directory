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

#include "OAILegacyAccountResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyAccountResponse::OAILegacyAccountResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyAccountResponse::OAILegacyAccountResponse() {
    this->initializeModel();
}

OAILegacyAccountResponse::~OAILegacyAccountResponse() {}

void OAILegacyAccountResponse::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;
}

void OAILegacyAccountResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyAccountResponse::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;
}

QString OAILegacyAccountResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyAccountResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_account.size() > 0) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    return obj;
}

QMap<QString, OAILegacyAccountResponse_account_value> OAILegacyAccountResponse::getAccount() const {
    return m_account;
}
void OAILegacyAccountResponse::setAccount(const QMap<QString, OAILegacyAccountResponse_account_value> &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAILegacyAccountResponse::is_account_Set() const{
    return m_account_isSet;
}

bool OAILegacyAccountResponse::is_account_Valid() const{
    return m_account_isValid;
}

bool OAILegacyAccountResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyAccountResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
