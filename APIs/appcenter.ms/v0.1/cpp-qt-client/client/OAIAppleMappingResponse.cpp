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

#include "OAIAppleMappingResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppleMappingResponse::OAIAppleMappingResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppleMappingResponse::OAIAppleMappingResponse() {
    this->initializeModel();
}

OAIAppleMappingResponse::~OAIAppleMappingResponse() {}

void OAIAppleMappingResponse::initializeModel() {

    m_app_id_isSet = false;
    m_app_id_isValid = false;

    m_apple_id_isSet = false;
    m_apple_id_isValid = false;

    m_service_connection_id_isSet = false;
    m_service_connection_id_isValid = false;

    m_team_identifier_isSet = false;
    m_team_identifier_isValid = false;
}

void OAIAppleMappingResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppleMappingResponse::fromJsonObject(QJsonObject json) {

    m_app_id_isValid = ::OpenAPI::fromJsonValue(m_app_id, json[QString("app_id")]);
    m_app_id_isSet = !json[QString("app_id")].isNull() && m_app_id_isValid;

    m_apple_id_isValid = ::OpenAPI::fromJsonValue(m_apple_id, json[QString("apple_id")]);
    m_apple_id_isSet = !json[QString("apple_id")].isNull() && m_apple_id_isValid;

    m_service_connection_id_isValid = ::OpenAPI::fromJsonValue(m_service_connection_id, json[QString("service_connection_id")]);
    m_service_connection_id_isSet = !json[QString("service_connection_id")].isNull() && m_service_connection_id_isValid;

    m_team_identifier_isValid = ::OpenAPI::fromJsonValue(m_team_identifier, json[QString("team_identifier")]);
    m_team_identifier_isSet = !json[QString("team_identifier")].isNull() && m_team_identifier_isValid;
}

QString OAIAppleMappingResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppleMappingResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_app_id_isSet) {
        obj.insert(QString("app_id"), ::OpenAPI::toJsonValue(m_app_id));
    }
    if (m_apple_id_isSet) {
        obj.insert(QString("apple_id"), ::OpenAPI::toJsonValue(m_apple_id));
    }
    if (m_service_connection_id_isSet) {
        obj.insert(QString("service_connection_id"), ::OpenAPI::toJsonValue(m_service_connection_id));
    }
    if (m_team_identifier_isSet) {
        obj.insert(QString("team_identifier"), ::OpenAPI::toJsonValue(m_team_identifier));
    }
    return obj;
}

QString OAIAppleMappingResponse::getAppId() const {
    return m_app_id;
}
void OAIAppleMappingResponse::setAppId(const QString &app_id) {
    m_app_id = app_id;
    m_app_id_isSet = true;
}

bool OAIAppleMappingResponse::is_app_id_Set() const{
    return m_app_id_isSet;
}

bool OAIAppleMappingResponse::is_app_id_Valid() const{
    return m_app_id_isValid;
}

QString OAIAppleMappingResponse::getAppleId() const {
    return m_apple_id;
}
void OAIAppleMappingResponse::setAppleId(const QString &apple_id) {
    m_apple_id = apple_id;
    m_apple_id_isSet = true;
}

bool OAIAppleMappingResponse::is_apple_id_Set() const{
    return m_apple_id_isSet;
}

bool OAIAppleMappingResponse::is_apple_id_Valid() const{
    return m_apple_id_isValid;
}

QString OAIAppleMappingResponse::getServiceConnectionId() const {
    return m_service_connection_id;
}
void OAIAppleMappingResponse::setServiceConnectionId(const QString &service_connection_id) {
    m_service_connection_id = service_connection_id;
    m_service_connection_id_isSet = true;
}

bool OAIAppleMappingResponse::is_service_connection_id_Set() const{
    return m_service_connection_id_isSet;
}

bool OAIAppleMappingResponse::is_service_connection_id_Valid() const{
    return m_service_connection_id_isValid;
}

QString OAIAppleMappingResponse::getTeamIdentifier() const {
    return m_team_identifier;
}
void OAIAppleMappingResponse::setTeamIdentifier(const QString &team_identifier) {
    m_team_identifier = team_identifier;
    m_team_identifier_isSet = true;
}

bool OAIAppleMappingResponse::is_team_identifier_Set() const{
    return m_team_identifier_isSet;
}

bool OAIAppleMappingResponse::is_team_identifier_Valid() const{
    return m_team_identifier_isValid;
}

bool OAIAppleMappingResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_app_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_apple_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_connection_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppleMappingResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
