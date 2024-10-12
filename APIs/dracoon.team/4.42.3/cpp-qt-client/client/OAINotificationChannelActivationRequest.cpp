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

#include "OAINotificationChannelActivationRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINotificationChannelActivationRequest::OAINotificationChannelActivationRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINotificationChannelActivationRequest::OAINotificationChannelActivationRequest() {
    this->initializeModel();
}

OAINotificationChannelActivationRequest::~OAINotificationChannelActivationRequest() {}

void OAINotificationChannelActivationRequest::initializeModel() {

    m_channel_id_isSet = false;
    m_channel_id_isValid = false;

    m_is_enabled_isSet = false;
    m_is_enabled_isValid = false;
}

void OAINotificationChannelActivationRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINotificationChannelActivationRequest::fromJsonObject(QJsonObject json) {

    m_channel_id_isValid = ::OpenAPI::fromJsonValue(m_channel_id, json[QString("channelId")]);
    m_channel_id_isSet = !json[QString("channelId")].isNull() && m_channel_id_isValid;

    m_is_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_enabled, json[QString("isEnabled")]);
    m_is_enabled_isSet = !json[QString("isEnabled")].isNull() && m_is_enabled_isValid;
}

QString OAINotificationChannelActivationRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINotificationChannelActivationRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_channel_id_isSet) {
        obj.insert(QString("channelId"), ::OpenAPI::toJsonValue(m_channel_id));
    }
    if (m_is_enabled_isSet) {
        obj.insert(QString("isEnabled"), ::OpenAPI::toJsonValue(m_is_enabled));
    }
    return obj;
}

qint32 OAINotificationChannelActivationRequest::getChannelId() const {
    return m_channel_id;
}
void OAINotificationChannelActivationRequest::setChannelId(const qint32 &channel_id) {
    m_channel_id = channel_id;
    m_channel_id_isSet = true;
}

bool OAINotificationChannelActivationRequest::is_channel_id_Set() const{
    return m_channel_id_isSet;
}

bool OAINotificationChannelActivationRequest::is_channel_id_Valid() const{
    return m_channel_id_isValid;
}

bool OAINotificationChannelActivationRequest::isIsEnabled() const {
    return m_is_enabled;
}
void OAINotificationChannelActivationRequest::setIsEnabled(const bool &is_enabled) {
    m_is_enabled = is_enabled;
    m_is_enabled_isSet = true;
}

bool OAINotificationChannelActivationRequest::is_is_enabled_Set() const{
    return m_is_enabled_isSet;
}

bool OAINotificationChannelActivationRequest::is_is_enabled_Valid() const{
    return m_is_enabled_isValid;
}

bool OAINotificationChannelActivationRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_channel_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINotificationChannelActivationRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_channel_id_isValid && m_is_enabled_isValid && true;
}

} // namespace OpenAPI
