/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDellSwitchDataSourceRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDellSwitchDataSourceRequest::OAIDellSwitchDataSourceRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDellSwitchDataSourceRequest::OAIDellSwitchDataSourceRequest() {
    this->initializeModel();
}

OAIDellSwitchDataSourceRequest::~OAIDellSwitchDataSourceRequest() {}

void OAIDellSwitchDataSourceRequest::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_fqdn_isSet = false;
    m_fqdn_isValid = false;

    m_ip_isSet = false;
    m_ip_isValid = false;

    m_nickname_isSet = false;
    m_nickname_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_proxy_id_isSet = false;
    m_proxy_id_isValid = false;

    m_credentials_isSet = false;
    m_credentials_isValid = false;

    m_switch_type_isSet = false;
    m_switch_type_isValid = false;
}

void OAIDellSwitchDataSourceRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDellSwitchDataSourceRequest::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_fqdn_isValid = ::OpenAPI::fromJsonValue(m_fqdn, json[QString("fqdn")]);
    m_fqdn_isSet = !json[QString("fqdn")].isNull() && m_fqdn_isValid;

    m_ip_isValid = ::OpenAPI::fromJsonValue(m_ip, json[QString("ip")]);
    m_ip_isSet = !json[QString("ip")].isNull() && m_ip_isValid;

    m_nickname_isValid = ::OpenAPI::fromJsonValue(m_nickname, json[QString("nickname")]);
    m_nickname_isSet = !json[QString("nickname")].isNull() && m_nickname_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_proxy_id_isValid = ::OpenAPI::fromJsonValue(m_proxy_id, json[QString("proxy_id")]);
    m_proxy_id_isSet = !json[QString("proxy_id")].isNull() && m_proxy_id_isValid;

    m_credentials_isValid = ::OpenAPI::fromJsonValue(m_credentials, json[QString("credentials")]);
    m_credentials_isSet = !json[QString("credentials")].isNull() && m_credentials_isValid;

    m_switch_type_isValid = ::OpenAPI::fromJsonValue(m_switch_type, json[QString("switch_type")]);
    m_switch_type_isSet = !json[QString("switch_type")].isNull() && m_switch_type_isValid;
}

QString OAIDellSwitchDataSourceRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDellSwitchDataSourceRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_fqdn_isSet) {
        obj.insert(QString("fqdn"), ::OpenAPI::toJsonValue(m_fqdn));
    }
    if (m_ip_isSet) {
        obj.insert(QString("ip"), ::OpenAPI::toJsonValue(m_ip));
    }
    if (m_nickname_isSet) {
        obj.insert(QString("nickname"), ::OpenAPI::toJsonValue(m_nickname));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_proxy_id_isSet) {
        obj.insert(QString("proxy_id"), ::OpenAPI::toJsonValue(m_proxy_id));
    }
    if (m_credentials.isSet()) {
        obj.insert(QString("credentials"), ::OpenAPI::toJsonValue(m_credentials));
    }
    if (m_switch_type.isSet()) {
        obj.insert(QString("switch_type"), ::OpenAPI::toJsonValue(m_switch_type));
    }
    return obj;
}

bool OAIDellSwitchDataSourceRequest::isEnabled() const {
    return m_enabled;
}
void OAIDellSwitchDataSourceRequest::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIDellSwitchDataSourceRequest::getFqdn() const {
    return m_fqdn;
}
void OAIDellSwitchDataSourceRequest::setFqdn(const QString &fqdn) {
    m_fqdn = fqdn;
    m_fqdn_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_fqdn_Set() const{
    return m_fqdn_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_fqdn_Valid() const{
    return m_fqdn_isValid;
}

QString OAIDellSwitchDataSourceRequest::getIp() const {
    return m_ip;
}
void OAIDellSwitchDataSourceRequest::setIp(const QString &ip) {
    m_ip = ip;
    m_ip_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_ip_Set() const{
    return m_ip_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_ip_Valid() const{
    return m_ip_isValid;
}

QString OAIDellSwitchDataSourceRequest::getNickname() const {
    return m_nickname;
}
void OAIDellSwitchDataSourceRequest::setNickname(const QString &nickname) {
    m_nickname = nickname;
    m_nickname_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_nickname_Set() const{
    return m_nickname_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_nickname_Valid() const{
    return m_nickname_isValid;
}

QString OAIDellSwitchDataSourceRequest::getNotes() const {
    return m_notes;
}
void OAIDellSwitchDataSourceRequest::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIDellSwitchDataSourceRequest::getProxyId() const {
    return m_proxy_id;
}
void OAIDellSwitchDataSourceRequest::setProxyId(const QString &proxy_id) {
    m_proxy_id = proxy_id;
    m_proxy_id_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_proxy_id_Set() const{
    return m_proxy_id_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_proxy_id_Valid() const{
    return m_proxy_id_isValid;
}

OAIPasswordCredentials OAIDellSwitchDataSourceRequest::getCredentials() const {
    return m_credentials;
}
void OAIDellSwitchDataSourceRequest::setCredentials(const OAIPasswordCredentials &credentials) {
    m_credentials = credentials;
    m_credentials_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_credentials_Set() const{
    return m_credentials_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_credentials_Valid() const{
    return m_credentials_isValid;
}

OAIDellSwitchType OAIDellSwitchDataSourceRequest::getSwitchType() const {
    return m_switch_type;
}
void OAIDellSwitchDataSourceRequest::setSwitchType(const OAIDellSwitchType &switch_type) {
    m_switch_type = switch_type;
    m_switch_type_isSet = true;
}

bool OAIDellSwitchDataSourceRequest::is_switch_type_Set() const{
    return m_switch_type_isSet;
}

bool OAIDellSwitchDataSourceRequest::is_switch_type_Valid() const{
    return m_switch_type_isValid;
}

bool OAIDellSwitchDataSourceRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fqdn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nickname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proxy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credentials.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_switch_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDellSwitchDataSourceRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_nickname_isValid && m_proxy_id_isValid && true;
}

} // namespace OpenAPI
