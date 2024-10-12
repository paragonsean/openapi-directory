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

#include "OAIActiveDirectory.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActiveDirectory::OAIActiveDirectory(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActiveDirectory::OAIActiveDirectory() {
    this->initializeModel();
}

OAIActiveDirectory::~OAIActiveDirectory() {}

void OAIActiveDirectory::initializeModel() {

    m_alias_isSet = false;
    m_alias_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_global_available_isSet = false;
    m_is_global_available_isValid = false;
}

void OAIActiveDirectory::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActiveDirectory::fromJsonObject(QJsonObject json) {

    m_alias_isValid = ::OpenAPI::fromJsonValue(m_alias, json[QString("alias")]);
    m_alias_isSet = !json[QString("alias")].isNull() && m_alias_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_global_available_isValid = ::OpenAPI::fromJsonValue(m_is_global_available, json[QString("isGlobalAvailable")]);
    m_is_global_available_isSet = !json[QString("isGlobalAvailable")].isNull() && m_is_global_available_isValid;
}

QString OAIActiveDirectory::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActiveDirectory::asJsonObject() const {
    QJsonObject obj;
    if (m_alias_isSet) {
        obj.insert(QString("alias"), ::OpenAPI::toJsonValue(m_alias));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_global_available_isSet) {
        obj.insert(QString("isGlobalAvailable"), ::OpenAPI::toJsonValue(m_is_global_available));
    }
    return obj;
}

QString OAIActiveDirectory::getAlias() const {
    return m_alias;
}
void OAIActiveDirectory::setAlias(const QString &alias) {
    m_alias = alias;
    m_alias_isSet = true;
}

bool OAIActiveDirectory::is_alias_Set() const{
    return m_alias_isSet;
}

bool OAIActiveDirectory::is_alias_Valid() const{
    return m_alias_isValid;
}

qint32 OAIActiveDirectory::getId() const {
    return m_id;
}
void OAIActiveDirectory::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIActiveDirectory::is_id_Set() const{
    return m_id_isSet;
}

bool OAIActiveDirectory::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIActiveDirectory::isIsGlobalAvailable() const {
    return m_is_global_available;
}
void OAIActiveDirectory::setIsGlobalAvailable(const bool &is_global_available) {
    m_is_global_available = is_global_available;
    m_is_global_available_isSet = true;
}

bool OAIActiveDirectory::is_is_global_available_Set() const{
    return m_is_global_available_isSet;
}

bool OAIActiveDirectory::is_is_global_available_Valid() const{
    return m_is_global_available_isValid;
}

bool OAIActiveDirectory::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_global_available_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActiveDirectory::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_alias_isValid && m_id_isValid && m_is_global_available_isValid && true;
}

} // namespace OpenAPI
