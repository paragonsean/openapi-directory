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

#include "OAIAppResponseInternal_allOf_user_permissions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppResponseInternal_allOf_user_permissions::OAIAppResponseInternal_allOf_user_permissions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppResponseInternal_allOf_user_permissions::OAIAppResponseInternal_allOf_user_permissions() {
    this->initializeModel();
}

OAIAppResponseInternal_allOf_user_permissions::~OAIAppResponseInternal_allOf_user_permissions() {}

void OAIAppResponseInternal_allOf_user_permissions::initializeModel() {

    m_permissions_isSet = false;
    m_permissions_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIAppResponseInternal_allOf_user_permissions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppResponseInternal_allOf_user_permissions::fromJsonObject(QJsonObject json) {

    m_permissions_isValid = ::OpenAPI::fromJsonValue(m_permissions, json[QString("permissions")]);
    m_permissions_isSet = !json[QString("permissions")].isNull() && m_permissions_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIAppResponseInternal_allOf_user_permissions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppResponseInternal_allOf_user_permissions::asJsonObject() const {
    QJsonObject obj;
    if (m_permissions.size() > 0) {
        obj.insert(QString("permissions"), ::OpenAPI::toJsonValue(m_permissions));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QList<QString> OAIAppResponseInternal_allOf_user_permissions::getPermissions() const {
    return m_permissions;
}
void OAIAppResponseInternal_allOf_user_permissions::setPermissions(const QList<QString> &permissions) {
    m_permissions = permissions;
    m_permissions_isSet = true;
}

bool OAIAppResponseInternal_allOf_user_permissions::is_permissions_Set() const{
    return m_permissions_isSet;
}

bool OAIAppResponseInternal_allOf_user_permissions::is_permissions_Valid() const{
    return m_permissions_isValid;
}

QString OAIAppResponseInternal_allOf_user_permissions::getUserId() const {
    return m_user_id;
}
void OAIAppResponseInternal_allOf_user_permissions::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIAppResponseInternal_allOf_user_permissions::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIAppResponseInternal_allOf_user_permissions::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIAppResponseInternal_allOf_user_permissions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_permissions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppResponseInternal_allOf_user_permissions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
