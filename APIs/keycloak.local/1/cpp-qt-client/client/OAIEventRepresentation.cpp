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

#include "OAIEventRepresentation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEventRepresentation::OAIEventRepresentation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEventRepresentation::OAIEventRepresentation() {
    this->initializeModel();
}

OAIEventRepresentation::~OAIEventRepresentation() {}

void OAIEventRepresentation::initializeModel() {

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_ip_address_isSet = false;
    m_ip_address_isValid = false;

    m_realm_id_isSet = false;
    m_realm_id_isValid = false;

    m_session_id_isSet = false;
    m_session_id_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIEventRepresentation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEventRepresentation::fromJsonObject(QJsonObject json) {

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_ip_address_isValid = ::OpenAPI::fromJsonValue(m_ip_address, json[QString("ipAddress")]);
    m_ip_address_isSet = !json[QString("ipAddress")].isNull() && m_ip_address_isValid;

    m_realm_id_isValid = ::OpenAPI::fromJsonValue(m_realm_id, json[QString("realmId")]);
    m_realm_id_isSet = !json[QString("realmId")].isNull() && m_realm_id_isValid;

    m_session_id_isValid = ::OpenAPI::fromJsonValue(m_session_id, json[QString("sessionId")]);
    m_session_id_isSet = !json[QString("sessionId")].isNull() && m_session_id_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;
}

QString OAIEventRepresentation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEventRepresentation::asJsonObject() const {
    QJsonObject obj;
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_details.size() > 0) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_ip_address_isSet) {
        obj.insert(QString("ipAddress"), ::OpenAPI::toJsonValue(m_ip_address));
    }
    if (m_realm_id_isSet) {
        obj.insert(QString("realmId"), ::OpenAPI::toJsonValue(m_realm_id));
    }
    if (m_session_id_isSet) {
        obj.insert(QString("sessionId"), ::OpenAPI::toJsonValue(m_session_id));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIEventRepresentation::getClientId() const {
    return m_client_id;
}
void OAIEventRepresentation::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAIEventRepresentation::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAIEventRepresentation::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QMap<QString, QJsonValue> OAIEventRepresentation::getDetails() const {
    return m_details;
}
void OAIEventRepresentation::setDetails(const QMap<QString, QJsonValue> &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAIEventRepresentation::is_details_Set() const{
    return m_details_isSet;
}

bool OAIEventRepresentation::is_details_Valid() const{
    return m_details_isValid;
}

QString OAIEventRepresentation::getError() const {
    return m_error;
}
void OAIEventRepresentation::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIEventRepresentation::is_error_Set() const{
    return m_error_isSet;
}

bool OAIEventRepresentation::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIEventRepresentation::getIpAddress() const {
    return m_ip_address;
}
void OAIEventRepresentation::setIpAddress(const QString &ip_address) {
    m_ip_address = ip_address;
    m_ip_address_isSet = true;
}

bool OAIEventRepresentation::is_ip_address_Set() const{
    return m_ip_address_isSet;
}

bool OAIEventRepresentation::is_ip_address_Valid() const{
    return m_ip_address_isValid;
}

QString OAIEventRepresentation::getRealmId() const {
    return m_realm_id;
}
void OAIEventRepresentation::setRealmId(const QString &realm_id) {
    m_realm_id = realm_id;
    m_realm_id_isSet = true;
}

bool OAIEventRepresentation::is_realm_id_Set() const{
    return m_realm_id_isSet;
}

bool OAIEventRepresentation::is_realm_id_Valid() const{
    return m_realm_id_isValid;
}

QString OAIEventRepresentation::getSessionId() const {
    return m_session_id;
}
void OAIEventRepresentation::setSessionId(const QString &session_id) {
    m_session_id = session_id;
    m_session_id_isSet = true;
}

bool OAIEventRepresentation::is_session_id_Set() const{
    return m_session_id_isSet;
}

bool OAIEventRepresentation::is_session_id_Valid() const{
    return m_session_id_isValid;
}

qint64 OAIEventRepresentation::getTime() const {
    return m_time;
}
void OAIEventRepresentation::setTime(const qint64 &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIEventRepresentation::is_time_Set() const{
    return m_time_isSet;
}

bool OAIEventRepresentation::is_time_Valid() const{
    return m_time_isValid;
}

QString OAIEventRepresentation::getType() const {
    return m_type;
}
void OAIEventRepresentation::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIEventRepresentation::is_type_Set() const{
    return m_type_isSet;
}

bool OAIEventRepresentation::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIEventRepresentation::getUserId() const {
    return m_user_id;
}
void OAIEventRepresentation::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIEventRepresentation::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIEventRepresentation::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIEventRepresentation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_realm_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEventRepresentation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
