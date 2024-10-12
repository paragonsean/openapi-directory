/**
 * ManagementLockClient
 * Azure resources can be locked to prevent other users in your organization from deleting or modifying resources.
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIManagementLockProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIManagementLockProperties::OAIManagementLockProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIManagementLockProperties::OAIManagementLockProperties() {
    this->initializeModel();
}

OAIManagementLockProperties::~OAIManagementLockProperties() {}

void OAIManagementLockProperties::initializeModel() {

    m_level_isSet = false;
    m_level_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_owners_isSet = false;
    m_owners_isValid = false;
}

void OAIManagementLockProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIManagementLockProperties::fromJsonObject(QJsonObject json) {

    m_level_isValid = ::OpenAPI::fromJsonValue(m_level, json[QString("level")]);
    m_level_isSet = !json[QString("level")].isNull() && m_level_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_owners_isValid = ::OpenAPI::fromJsonValue(m_owners, json[QString("owners")]);
    m_owners_isSet = !json[QString("owners")].isNull() && m_owners_isValid;
}

QString OAIManagementLockProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIManagementLockProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_level_isSet) {
        obj.insert(QString("level"), ::OpenAPI::toJsonValue(m_level));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_owners.size() > 0) {
        obj.insert(QString("owners"), ::OpenAPI::toJsonValue(m_owners));
    }
    return obj;
}

QString OAIManagementLockProperties::getLevel() const {
    return m_level;
}
void OAIManagementLockProperties::setLevel(const QString &level) {
    m_level = level;
    m_level_isSet = true;
}

bool OAIManagementLockProperties::is_level_Set() const{
    return m_level_isSet;
}

bool OAIManagementLockProperties::is_level_Valid() const{
    return m_level_isValid;
}

QString OAIManagementLockProperties::getNotes() const {
    return m_notes;
}
void OAIManagementLockProperties::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIManagementLockProperties::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIManagementLockProperties::is_notes_Valid() const{
    return m_notes_isValid;
}

QList<OAIManagementLockOwner> OAIManagementLockProperties::getOwners() const {
    return m_owners;
}
void OAIManagementLockProperties::setOwners(const QList<OAIManagementLockOwner> &owners) {
    m_owners = owners;
    m_owners_isSet = true;
}

bool OAIManagementLockProperties::is_owners_Set() const{
    return m_owners_isSet;
}

bool OAIManagementLockProperties::is_owners_Valid() const{
    return m_owners_isValid;
}

bool OAIManagementLockProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_level_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owners.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIManagementLockProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_level_isValid && true;
}

} // namespace OpenAPI
