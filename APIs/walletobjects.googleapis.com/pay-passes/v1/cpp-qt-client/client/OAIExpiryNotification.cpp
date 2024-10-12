/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExpiryNotification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExpiryNotification::OAIExpiryNotification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExpiryNotification::OAIExpiryNotification() {
    this->initializeModel();
}

OAIExpiryNotification::~OAIExpiryNotification() {}

void OAIExpiryNotification::initializeModel() {

    m_enable_notification_isSet = false;
    m_enable_notification_isValid = false;
}

void OAIExpiryNotification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExpiryNotification::fromJsonObject(QJsonObject json) {

    m_enable_notification_isValid = ::OpenAPI::fromJsonValue(m_enable_notification, json[QString("enableNotification")]);
    m_enable_notification_isSet = !json[QString("enableNotification")].isNull() && m_enable_notification_isValid;
}

QString OAIExpiryNotification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExpiryNotification::asJsonObject() const {
    QJsonObject obj;
    if (m_enable_notification_isSet) {
        obj.insert(QString("enableNotification"), ::OpenAPI::toJsonValue(m_enable_notification));
    }
    return obj;
}

bool OAIExpiryNotification::isEnableNotification() const {
    return m_enable_notification;
}
void OAIExpiryNotification::setEnableNotification(const bool &enable_notification) {
    m_enable_notification = enable_notification;
    m_enable_notification_isSet = true;
}

bool OAIExpiryNotification::is_enable_notification_Set() const{
    return m_enable_notification_isSet;
}

bool OAIExpiryNotification::is_enable_notification_Valid() const{
    return m_enable_notification_isValid;
}

bool OAIExpiryNotification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enable_notification_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExpiryNotification::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
