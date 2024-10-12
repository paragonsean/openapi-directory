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

#include "OAINotificationScope.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotificationScope::OAINotificationScope(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotificationScope::OAINotificationScope() {
    this->initializeModel();
}

OAINotificationScope::~OAINotificationScope() {}

void OAINotificationScope::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAINotificationScope::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotificationScope::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAINotificationScope::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotificationScope::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

qint32 OAINotificationScope::getId() const {
    return m_id;
}
void OAINotificationScope::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAINotificationScope::is_id_Set() const{
    return m_id_isSet;
}

bool OAINotificationScope::is_id_Valid() const{
    return m_id_isValid;
}

QString OAINotificationScope::getName() const {
    return m_name;
}
void OAINotificationScope::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINotificationScope::is_name_Set() const{
    return m_name_isSet;
}

bool OAINotificationScope::is_name_Valid() const{
    return m_name_isValid;
}

bool OAINotificationScope::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotificationScope::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
