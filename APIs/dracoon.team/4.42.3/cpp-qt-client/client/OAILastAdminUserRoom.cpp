/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILastAdminUserRoom.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILastAdminUserRoom::OAILastAdminUserRoom(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILastAdminUserRoom::OAILastAdminUserRoom() {
    this->initializeModel();
}

OAILastAdminUserRoom::~OAILastAdminUserRoom() {}

void OAILastAdminUserRoom::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_admin_in_group_isSet = false;
    m_last_admin_in_group_isValid = false;

    m_last_admin_in_group_id_isSet = false;
    m_last_admin_in_group_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_parent_path_isSet = false;
    m_parent_path_isValid = false;
}

void OAILastAdminUserRoom::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILastAdminUserRoom::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_admin_in_group_isValid = ::OpenAPI::fromJsonValue(m_last_admin_in_group, json[QString("lastAdminInGroup")]);
    m_last_admin_in_group_isSet = !json[QString("lastAdminInGroup")].isNull() && m_last_admin_in_group_isValid;

    m_last_admin_in_group_id_isValid = ::OpenAPI::fromJsonValue(m_last_admin_in_group_id, json[QString("lastAdminInGroupId")]);
    m_last_admin_in_group_id_isSet = !json[QString("lastAdminInGroupId")].isNull() && m_last_admin_in_group_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parentId")]);
    m_parent_id_isSet = !json[QString("parentId")].isNull() && m_parent_id_isValid;

    m_parent_path_isValid = ::OpenAPI::fromJsonValue(m_parent_path, json[QString("parentPath")]);
    m_parent_path_isSet = !json[QString("parentPath")].isNull() && m_parent_path_isValid;
}

QString OAILastAdminUserRoom::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILastAdminUserRoom::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_admin_in_group_isSet) {
        obj.insert(QString("lastAdminInGroup"), ::OpenAPI::toJsonValue(m_last_admin_in_group));
    }
    if (m_last_admin_in_group_id_isSet) {
        obj.insert(QString("lastAdminInGroupId"), ::OpenAPI::toJsonValue(m_last_admin_in_group_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parentId"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_parent_path_isSet) {
        obj.insert(QString("parentPath"), ::OpenAPI::toJsonValue(m_parent_path));
    }
    return obj;
}

qint64 OAILastAdminUserRoom::getId() const {
    return m_id;
}
void OAILastAdminUserRoom::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAILastAdminUserRoom::is_id_Set() const{
    return m_id_isSet;
}

bool OAILastAdminUserRoom::is_id_Valid() const{
    return m_id_isValid;
}

bool OAILastAdminUserRoom::isLastAdminInGroup() const {
    return m_last_admin_in_group;
}
void OAILastAdminUserRoom::setLastAdminInGroup(const bool &last_admin_in_group) {
    m_last_admin_in_group = last_admin_in_group;
    m_last_admin_in_group_isSet = true;
}

bool OAILastAdminUserRoom::is_last_admin_in_group_Set() const{
    return m_last_admin_in_group_isSet;
}

bool OAILastAdminUserRoom::is_last_admin_in_group_Valid() const{
    return m_last_admin_in_group_isValid;
}

qint64 OAILastAdminUserRoom::getLastAdminInGroupId() const {
    return m_last_admin_in_group_id;
}
void OAILastAdminUserRoom::setLastAdminInGroupId(const qint64 &last_admin_in_group_id) {
    m_last_admin_in_group_id = last_admin_in_group_id;
    m_last_admin_in_group_id_isSet = true;
}

bool OAILastAdminUserRoom::is_last_admin_in_group_id_Set() const{
    return m_last_admin_in_group_id_isSet;
}

bool OAILastAdminUserRoom::is_last_admin_in_group_id_Valid() const{
    return m_last_admin_in_group_id_isValid;
}

QString OAILastAdminUserRoom::getName() const {
    return m_name;
}
void OAILastAdminUserRoom::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAILastAdminUserRoom::is_name_Set() const{
    return m_name_isSet;
}

bool OAILastAdminUserRoom::is_name_Valid() const{
    return m_name_isValid;
}

qint64 OAILastAdminUserRoom::getParentId() const {
    return m_parent_id;
}
void OAILastAdminUserRoom::setParentId(const qint64 &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAILastAdminUserRoom::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAILastAdminUserRoom::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

QString OAILastAdminUserRoom::getParentPath() const {
    return m_parent_path;
}
void OAILastAdminUserRoom::setParentPath(const QString &parent_path) {
    m_parent_path = parent_path;
    m_parent_path_isSet = true;
}

bool OAILastAdminUserRoom::is_parent_path_Set() const{
    return m_parent_path_isSet;
}

bool OAILastAdminUserRoom::is_parent_path_Valid() const{
    return m_parent_path_isValid;
}

bool OAILastAdminUserRoom::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_admin_in_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_admin_in_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILastAdminUserRoom::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_last_admin_in_group_isValid && m_name_isValid && m_parent_path_isValid && true;
}

} // namespace OpenAPI
