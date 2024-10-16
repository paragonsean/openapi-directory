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

#include "OAILinkAADtoUserRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILinkAADtoUserRequest::OAILinkAADtoUserRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILinkAADtoUserRequest::OAILinkAADtoUserRequest() {
    this->initializeModel();
}

OAILinkAADtoUserRequest::~OAILinkAADtoUserRequest() {}

void OAILinkAADtoUserRequest::initializeModel() {

    m_aad_tenant_ids_isSet = false;
    m_aad_tenant_ids_isValid = false;

    m_role_isSet = false;
    m_role_isValid = false;
}

void OAILinkAADtoUserRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILinkAADtoUserRequest::fromJsonObject(QJsonObject json) {

    m_aad_tenant_ids_isValid = ::OpenAPI::fromJsonValue(m_aad_tenant_ids, json[QString("aad_tenant_ids")]);
    m_aad_tenant_ids_isSet = !json[QString("aad_tenant_ids")].isNull() && m_aad_tenant_ids_isValid;

    m_role_isValid = ::OpenAPI::fromJsonValue(m_role, json[QString("role")]);
    m_role_isSet = !json[QString("role")].isNull() && m_role_isValid;
}

QString OAILinkAADtoUserRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILinkAADtoUserRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_aad_tenant_ids.size() > 0) {
        obj.insert(QString("aad_tenant_ids"), ::OpenAPI::toJsonValue(m_aad_tenant_ids));
    }
    if (m_role_isSet) {
        obj.insert(QString("role"), ::OpenAPI::toJsonValue(m_role));
    }
    return obj;
}

QList<QString> OAILinkAADtoUserRequest::getAadTenantIds() const {
    return m_aad_tenant_ids;
}
void OAILinkAADtoUserRequest::setAadTenantIds(const QList<QString> &aad_tenant_ids) {
    m_aad_tenant_ids = aad_tenant_ids;
    m_aad_tenant_ids_isSet = true;
}

bool OAILinkAADtoUserRequest::is_aad_tenant_ids_Set() const{
    return m_aad_tenant_ids_isSet;
}

bool OAILinkAADtoUserRequest::is_aad_tenant_ids_Valid() const{
    return m_aad_tenant_ids_isValid;
}

QString OAILinkAADtoUserRequest::getRole() const {
    return m_role;
}
void OAILinkAADtoUserRequest::setRole(const QString &role) {
    m_role = role;
    m_role_isSet = true;
}

bool OAILinkAADtoUserRequest::is_role_Set() const{
    return m_role_isSet;
}

bool OAILinkAADtoUserRequest::is_role_Valid() const{
    return m_role_isValid;
}

bool OAILinkAADtoUserRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aad_tenant_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_role_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILinkAADtoUserRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_aad_tenant_ids_isValid && true;
}

} // namespace OpenAPI
