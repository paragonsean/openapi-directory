/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISnapshot.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISnapshot::OAISnapshot(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISnapshot::OAISnapshot() {
    this->initializeModel();
}

OAISnapshot::~OAISnapshot() {}

void OAISnapshot::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_apply_scope_isSet = false;
    m_apply_scope_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_update_time_isSet = false;
    m_last_update_time_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_data_isSet = false;
    m_user_data_isValid = false;
}

void OAISnapshot::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISnapshot::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_apply_scope_isValid = ::OpenAPI::fromJsonValue(m_apply_scope, json[QString("applyScope")]);
    m_apply_scope_isSet = !json[QString("applyScope")].isNull() && m_apply_scope_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_update_time_isValid = ::OpenAPI::fromJsonValue(m_last_update_time, json[QString("lastUpdateTime")]);
    m_last_update_time_isSet = !json[QString("lastUpdateTime")].isNull() && m_last_update_time_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_data_isValid = ::OpenAPI::fromJsonValue(m_user_data, json[QString("userData")]);
    m_user_data_isSet = !json[QString("userData")].isNull() && m_user_data_isValid;
}

QString OAISnapshot::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISnapshot::asJsonObject() const {
    QJsonObject obj;
    if (m_account_isSet) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_apply_scope.size() > 0) {
        obj.insert(QString("applyScope"), ::OpenAPI::toJsonValue(m_apply_scope));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_update_time_isSet) {
        obj.insert(QString("lastUpdateTime"), ::OpenAPI::toJsonValue(m_last_update_time));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_data_isSet) {
        obj.insert(QString("userData"), ::OpenAPI::toJsonValue(m_user_data));
    }
    return obj;
}

QString OAISnapshot::getAccount() const {
    return m_account;
}
void OAISnapshot::setAccount(const QString &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAISnapshot::is_account_Set() const{
    return m_account_isSet;
}

bool OAISnapshot::is_account_Valid() const{
    return m_account_isValid;
}

QList<QString> OAISnapshot::getApplyScope() const {
    return m_apply_scope;
}
void OAISnapshot::setApplyScope(const QList<QString> &apply_scope) {
    m_apply_scope = apply_scope;
    m_apply_scope_isSet = true;
}

bool OAISnapshot::is_apply_scope_Set() const{
    return m_apply_scope_isSet;
}

bool OAISnapshot::is_apply_scope_Valid() const{
    return m_apply_scope_isValid;
}

QDateTime OAISnapshot::getCreatedTime() const {
    return m_created_time;
}
void OAISnapshot::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAISnapshot::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAISnapshot::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAISnapshot::getId() const {
    return m_id;
}
void OAISnapshot::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISnapshot::is_id_Set() const{
    return m_id_isSet;
}

bool OAISnapshot::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAISnapshot::getLastUpdateTime() const {
    return m_last_update_time;
}
void OAISnapshot::setLastUpdateTime(const QDateTime &last_update_time) {
    m_last_update_time = last_update_time;
    m_last_update_time_isSet = true;
}

bool OAISnapshot::is_last_update_time_Set() const{
    return m_last_update_time_isSet;
}

bool OAISnapshot::is_last_update_time_Valid() const{
    return m_last_update_time_isValid;
}

QString OAISnapshot::getType() const {
    return m_type;
}
void OAISnapshot::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAISnapshot::is_type_Set() const{
    return m_type_isSet;
}

bool OAISnapshot::is_type_Valid() const{
    return m_type_isValid;
}

QString OAISnapshot::getUserData() const {
    return m_user_data;
}
void OAISnapshot::setUserData(const QString &user_data) {
    m_user_data = user_data;
    m_user_data_isSet = true;
}

bool OAISnapshot::is_user_data_Set() const{
    return m_user_data_isSet;
}

bool OAISnapshot::is_user_data_Valid() const{
    return m_user_data_isValid;
}

bool OAISnapshot::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_apply_scope.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_update_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_data_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISnapshot::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_account_isValid && m_apply_scope_isValid && m_created_time_isValid && m_id_isValid && m_last_update_time_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
