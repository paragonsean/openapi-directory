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

#include "OAIBugtracker_getSettings_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBugtracker_getSettings_200_response::OAIBugtracker_getSettings_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBugtracker_getSettings_200_response::OAIBugtracker_getSettings_200_response() {
    this->initializeModel();
}

OAIBugtracker_getSettings_200_response::~OAIBugtracker_getSettings_200_response() {}

void OAIBugtracker_getSettings_200_response::initializeModel() {

    m_event_types_isSet = false;
    m_event_types_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_token_id_isSet = false;
    m_token_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIBugtracker_getSettings_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBugtracker_getSettings_200_response::fromJsonObject(QJsonObject json) {

    m_event_types_isValid = ::OpenAPI::fromJsonValue(m_event_types, json[QString("event_types")]);
    m_event_types_isSet = !json[QString("event_types")].isNull() && m_event_types_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_token_id_isValid = ::OpenAPI::fromJsonValue(m_token_id, json[QString("token_id")]);
    m_token_id_isSet = !json[QString("token_id")].isNull() && m_token_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIBugtracker_getSettings_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBugtracker_getSettings_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_event_types.size() > 0) {
        obj.insert(QString("event_types"), ::OpenAPI::toJsonValue(m_event_types));
    }
    if (m_settings.isSet()) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_token_id_isSet) {
        obj.insert(QString("token_id"), ::OpenAPI::toJsonValue(m_token_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<QString> OAIBugtracker_getSettings_200_response::getEventTypes() const {
    return m_event_types;
}
void OAIBugtracker_getSettings_200_response::setEventTypes(const QList<QString> &event_types) {
    m_event_types = event_types;
    m_event_types_isSet = true;
}

bool OAIBugtracker_getSettings_200_response::is_event_types_Set() const{
    return m_event_types_isSet;
}

bool OAIBugtracker_getSettings_200_response::is_event_types_Valid() const{
    return m_event_types_isValid;
}

OAIBugtracker_getSettings_200_response_settings OAIBugtracker_getSettings_200_response::getSettings() const {
    return m_settings;
}
void OAIBugtracker_getSettings_200_response::setSettings(const OAIBugtracker_getSettings_200_response_settings &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIBugtracker_getSettings_200_response::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIBugtracker_getSettings_200_response::is_settings_Valid() const{
    return m_settings_isValid;
}

QString OAIBugtracker_getSettings_200_response::getState() const {
    return m_state;
}
void OAIBugtracker_getSettings_200_response::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIBugtracker_getSettings_200_response::is_state_Set() const{
    return m_state_isSet;
}

bool OAIBugtracker_getSettings_200_response::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIBugtracker_getSettings_200_response::getTokenId() const {
    return m_token_id;
}
void OAIBugtracker_getSettings_200_response::setTokenId(const QString &token_id) {
    m_token_id = token_id;
    m_token_id_isSet = true;
}

bool OAIBugtracker_getSettings_200_response::is_token_id_Set() const{
    return m_token_id_isSet;
}

bool OAIBugtracker_getSettings_200_response::is_token_id_Valid() const{
    return m_token_id_isValid;
}

QString OAIBugtracker_getSettings_200_response::getType() const {
    return m_type;
}
void OAIBugtracker_getSettings_200_response::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIBugtracker_getSettings_200_response::is_type_Set() const{
    return m_type_isSet;
}

bool OAIBugtracker_getSettings_200_response::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIBugtracker_getSettings_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_event_types.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBugtracker_getSettings_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
