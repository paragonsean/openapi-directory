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

#include "OAILegacyApp_collaborators_value.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyApp_collaborators_value::OAILegacyApp_collaborators_value(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyApp_collaborators_value::OAILegacyApp_collaborators_value() {
    this->initializeModel();
}

OAILegacyApp_collaborators_value::~OAILegacyApp_collaborators_value() {}

void OAILegacyApp_collaborators_value::initializeModel() {

    m_is_current_account_isSet = false;
    m_is_current_account_isValid = false;

    m_permission_isSet = false;
    m_permission_isValid = false;
}

void OAILegacyApp_collaborators_value::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyApp_collaborators_value::fromJsonObject(QJsonObject json) {

    m_is_current_account_isValid = ::OpenAPI::fromJsonValue(m_is_current_account, json[QString("isCurrentAccount")]);
    m_is_current_account_isSet = !json[QString("isCurrentAccount")].isNull() && m_is_current_account_isValid;

    m_permission_isValid = ::OpenAPI::fromJsonValue(m_permission, json[QString("permission")]);
    m_permission_isSet = !json[QString("permission")].isNull() && m_permission_isValid;
}

QString OAILegacyApp_collaborators_value::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyApp_collaborators_value::asJsonObject() const {
    QJsonObject obj;
    if (m_is_current_account_isSet) {
        obj.insert(QString("isCurrentAccount"), ::OpenAPI::toJsonValue(m_is_current_account));
    }
    if (m_permission_isSet) {
        obj.insert(QString("permission"), ::OpenAPI::toJsonValue(m_permission));
    }
    return obj;
}

bool OAILegacyApp_collaborators_value::isIsCurrentAccount() const {
    return m_is_current_account;
}
void OAILegacyApp_collaborators_value::setIsCurrentAccount(const bool &is_current_account) {
    m_is_current_account = is_current_account;
    m_is_current_account_isSet = true;
}

bool OAILegacyApp_collaborators_value::is_is_current_account_Set() const{
    return m_is_current_account_isSet;
}

bool OAILegacyApp_collaborators_value::is_is_current_account_Valid() const{
    return m_is_current_account_isValid;
}

QString OAILegacyApp_collaborators_value::getPermission() const {
    return m_permission;
}
void OAILegacyApp_collaborators_value::setPermission(const QString &permission) {
    m_permission = permission;
    m_permission_isSet = true;
}

bool OAILegacyApp_collaborators_value::is_permission_Set() const{
    return m_permission_isSet;
}

bool OAILegacyApp_collaborators_value::is_permission_Valid() const{
    return m_permission_isValid;
}

bool OAILegacyApp_collaborators_value::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_current_account_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_permission_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyApp_collaborators_value::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
