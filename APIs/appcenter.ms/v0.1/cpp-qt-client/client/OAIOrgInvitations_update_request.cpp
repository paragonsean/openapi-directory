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

#include "OAIOrgInvitations_update_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrgInvitations_update_request::OAIOrgInvitations_update_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrgInvitations_update_request::OAIOrgInvitations_update_request() {
    this->initializeModel();
}

OAIOrgInvitations_update_request::~OAIOrgInvitations_update_request() {}

void OAIOrgInvitations_update_request::initializeModel() {

    m_role_isSet = false;
    m_role_isValid = false;
}

void OAIOrgInvitations_update_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrgInvitations_update_request::fromJsonObject(QJsonObject json) {

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;
}

QString OAIOrgInvitations_update_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrgInvitations_update_request::asJsonObject() const {
    QJsonObject obj;
    if (m_role_isSet) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    return obj;
}

QString OAIOrgInvitations_update_request::getRole() const {
    return m_role;
}
void OAIOrgInvitations_update_request::setRole(const QString &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAIOrgInvitations_update_request::is_role_Set() const{
    return m_role_isSet;
}

bool OAIOrgInvitations_update_request::is_role_Valid() const{
    return m_role_isValid;
}

bool OAIOrgInvitations_update_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_role_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrgInvitations_update_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
