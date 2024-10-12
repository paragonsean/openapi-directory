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

#include "OAIRoomWebhook.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRoomWebhook::OAIRoomWebhook(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRoomWebhook::OAIRoomWebhook() {
    this->initializeModel();
}

OAIRoomWebhook::~OAIRoomWebhook() {}

void OAIRoomWebhook::initializeModel() {

    m_is_assigned_isSet = false;
    m_is_assigned_isValid = false;

    m_webhook_isSet = false;
    m_webhook_isValid = false;
}

void OAIRoomWebhook::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRoomWebhook::fromJsonObject(QJsonObject json) {

    m_is_assigned_isValid = ::OpenAPI::fromJsonValue(m_is_assigned, json[QString("isAssigned")]);
    m_is_assigned_isSet = !json[QString("isAssigned")].isNull() && m_is_assigned_isValid;

    m_webhook_isValid = ::OpenAPI::fromJsonValue(m_webhook, json[QString("webhook")]);
    m_webhook_isSet = !json[QString("webhook")].isNull() && m_webhook_isValid;
}

QString OAIRoomWebhook::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRoomWebhook::asJsonObject() const {
    QJsonObject obj;
    if (m_is_assigned_isSet) {
        obj.insert(QString("isAssigned"), ::OpenAPI::toJsonValue(m_is_assigned));
    }
    if (m_webhook.isSet()) {
        obj.insert(QString("webhook"), ::OpenAPI::toJsonValue(m_webhook));
    }
    return obj;
}

bool OAIRoomWebhook::isIsAssigned() const {
    return m_is_assigned;
}
void OAIRoomWebhook::setIsAssigned(const bool &is_assigned) {
    m_is_assigned = is_assigned;
    m_is_assigned_isSet = true;
}

bool OAIRoomWebhook::is_is_assigned_Set() const{
    return m_is_assigned_isSet;
}

bool OAIRoomWebhook::is_is_assigned_Valid() const{
    return m_is_assigned_isValid;
}

OAIWebhook OAIRoomWebhook::getWebhook() const {
    return m_webhook;
}
void OAIRoomWebhook::setWebhook(const OAIWebhook &webhook) {
    m_webhook = webhook;
    m_webhook_isSet = true;
}

bool OAIRoomWebhook::is_webhook_Set() const{
    return m_webhook_isSet;
}

bool OAIRoomWebhook::is_webhook_Valid() const{
    return m_webhook_isValid;
}

bool OAIRoomWebhook::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_assigned_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_webhook.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRoomWebhook::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_is_assigned_isValid && m_webhook_isValid && true;
}

} // namespace OpenAPI
