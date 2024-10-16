/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISynchronizationResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISynchronizationResult::OAISynchronizationResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISynchronizationResult::OAISynchronizationResult() {
    this->initializeModel();
}

OAISynchronizationResult::~OAISynchronizationResult() {}

void OAISynchronizationResult::initializeModel() {

    m_added_isSet = false;
    m_added_isValid = false;

    m_failed_isSet = false;
    m_failed_isValid = false;

    m_ignored_isSet = false;
    m_ignored_isValid = false;

    m_removed_isSet = false;
    m_removed_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAISynchronizationResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISynchronizationResult::fromJsonObject(QJsonObject json) {

    m_added_isValid = ::OpenAPI::fromJsonValue(m_added, json[QString("added")]);
    m_added_isSet = !json[QString("added")].isNull() && m_added_isValid;

    m_failed_isValid = ::OpenAPI::fromJsonValue(m_failed, json[QString("failed")]);
    m_failed_isSet = !json[QString("failed")].isNull() && m_failed_isValid;

    m_ignored_isValid = ::OpenAPI::fromJsonValue(m_ignored, json[QString("ignored")]);
    m_ignored_isSet = !json[QString("ignored")].isNull() && m_ignored_isValid;

    m_removed_isValid = ::OpenAPI::fromJsonValue(m_removed, json[QString("removed")]);
    m_removed_isSet = !json[QString("removed")].isNull() && m_removed_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("updated")]);
    m_updated_isSet = !json[QString("updated")].isNull() && m_updated_isValid;
}

QString OAISynchronizationResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISynchronizationResult::asJsonObject() const {
    QJsonObject obj;
    if (m_added_isSet) {
        obj.insert(QString("added"), ::OpenAPI::toJsonValue(m_added));
    }
    if (m_failed_isSet) {
        obj.insert(QString("failed"), ::OpenAPI::toJsonValue(m_failed));
    }
    if (m_ignored_isSet) {
        obj.insert(QString("ignored"), ::OpenAPI::toJsonValue(m_ignored));
    }
    if (m_removed_isSet) {
        obj.insert(QString("removed"), ::OpenAPI::toJsonValue(m_removed));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_isSet) {
        obj.insert(QString("updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

qint32 OAISynchronizationResult::getAdded() const {
    return m_added;
}
void OAISynchronizationResult::setAdded(const qint32 &added) {
    m_added = added;
    m_added_isSet = true;
}

bool OAISynchronizationResult::is_added_Set() const{
    return m_added_isSet;
}

bool OAISynchronizationResult::is_added_Valid() const{
    return m_added_isValid;
}

qint32 OAISynchronizationResult::getFailed() const {
    return m_failed;
}
void OAISynchronizationResult::setFailed(const qint32 &failed) {
    m_failed = failed;
    m_failed_isSet = true;
}

bool OAISynchronizationResult::is_failed_Set() const{
    return m_failed_isSet;
}

bool OAISynchronizationResult::is_failed_Valid() const{
    return m_failed_isValid;
}

bool OAISynchronizationResult::isIgnored() const {
    return m_ignored;
}
void OAISynchronizationResult::setIgnored(const bool &ignored) {
    m_ignored = ignored;
    m_ignored_isSet = true;
}

bool OAISynchronizationResult::is_ignored_Set() const{
    return m_ignored_isSet;
}

bool OAISynchronizationResult::is_ignored_Valid() const{
    return m_ignored_isValid;
}

qint32 OAISynchronizationResult::getRemoved() const {
    return m_removed;
}
void OAISynchronizationResult::setRemoved(const qint32 &removed) {
    m_removed = removed;
    m_removed_isSet = true;
}

bool OAISynchronizationResult::is_removed_Set() const{
    return m_removed_isSet;
}

bool OAISynchronizationResult::is_removed_Valid() const{
    return m_removed_isValid;
}

QString OAISynchronizationResult::getStatus() const {
    return m_status;
}
void OAISynchronizationResult::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISynchronizationResult::is_status_Set() const{
    return m_status_isSet;
}

bool OAISynchronizationResult::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAISynchronizationResult::getUpdated() const {
    return m_updated;
}
void OAISynchronizationResult::setUpdated(const qint32 &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAISynchronizationResult::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAISynchronizationResult::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAISynchronizationResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_added_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_failed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ignored_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_removed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISynchronizationResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
