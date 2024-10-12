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

#include "OAINSXVManagerDataSource.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINSXVManagerDataSource::OAINSXVManagerDataSource(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINSXVManagerDataSource::OAINSXVManagerDataSource() {
    this->initializeModel();
}

OAINSXVManagerDataSource::~OAINSXVManagerDataSource() {}

void OAINSXVManagerDataSource::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_entity_id_isSet = false;
    m_entity_id_isValid = false;

    m_entity_type_isSet = false;
    m_entity_type_isValid = false;

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

    m_central_cli_enabled_isSet = false;
    m_central_cli_enabled_isValid = false;

    m_credentials_isSet = false;
    m_credentials_isValid = false;

    m_ipfix_enabled_isSet = false;
    m_ipfix_enabled_isValid = false;

    m_vcenter_id_isSet = false;
    m_vcenter_id_isValid = false;
}

void OAINSXVManagerDataSource::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINSXVManagerDataSource::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_entity_id_isValid = ::OpenAPI::fromJsonValue(m_entity_id, json[QString("entity_id")]);
    m_entity_id_isSet = !json[QString("entity_id")].isNull() && m_entity_id_isValid;

    m_entity_type_isValid = ::OpenAPI::fromJsonValue(m_entity_type, json[QString("entity_type")]);
    m_entity_type_isSet = !json[QString("entity_type")].isNull() && m_entity_type_isValid;

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

    m_central_cli_enabled_isValid = ::OpenAPI::fromJsonValue(m_central_cli_enabled, json[QString("central_cli_enabled")]);
    m_central_cli_enabled_isSet = !json[QString("central_cli_enabled")].isNull() && m_central_cli_enabled_isValid;

    m_credentials_isValid = ::OpenAPI::fromJsonValue(m_credentials, json[QString("credentials")]);
    m_credentials_isSet = !json[QString("credentials")].isNull() && m_credentials_isValid;

    m_ipfix_enabled_isValid = ::OpenAPI::fromJsonValue(m_ipfix_enabled, json[QString("ipfix_enabled")]);
    m_ipfix_enabled_isSet = !json[QString("ipfix_enabled")].isNull() && m_ipfix_enabled_isValid;

    m_vcenter_id_isValid = ::OpenAPI::fromJsonValue(m_vcenter_id, json[QString("vcenter_id")]);
    m_vcenter_id_isSet = !json[QString("vcenter_id")].isNull() && m_vcenter_id_isValid;
}

QString OAINSXVManagerDataSource::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINSXVManagerDataSource::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_entity_id_isSet) {
        obj.insert(QString("entity_id"), ::OpenAPI::toJsonValue(m_entity_id));
    }
    if (m_entity_type.isSet()) {
        obj.insert(QString("entity_type"), ::OpenAPI::toJsonValue(m_entity_type));
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
    if (m_central_cli_enabled_isSet) {
        obj.insert(QString("central_cli_enabled"), ::OpenAPI::toJsonValue(m_central_cli_enabled));
    }
    if (m_credentials.isSet()) {
        obj.insert(QString("credentials"), ::OpenAPI::toJsonValue(m_credentials));
    }
    if (m_ipfix_enabled_isSet) {
        obj.insert(QString("ipfix_enabled"), ::OpenAPI::toJsonValue(m_ipfix_enabled));
    }
    if (m_vcenter_id_isSet) {
        obj.insert(QString("vcenter_id"), ::OpenAPI::toJsonValue(m_vcenter_id));
    }
    return obj;
}

bool OAINSXVManagerDataSource::isEnabled() const {
    return m_enabled;
}
void OAINSXVManagerDataSource::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAINSXVManagerDataSource::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAINSXVManagerDataSource::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAINSXVManagerDataSource::getEntityId() const {
    return m_entity_id;
}
void OAINSXVManagerDataSource::setEntityId(const QString &entity_id) {
    m_entity_id = entity_id;
    m_entity_id_isSet = true;
}

bool OAINSXVManagerDataSource::is_entity_id_Set() const{
    return m_entity_id_isSet;
}

bool OAINSXVManagerDataSource::is_entity_id_Valid() const{
    return m_entity_id_isValid;
}

OAIDataSourceType OAINSXVManagerDataSource::getEntityType() const {
    return m_entity_type;
}
void OAINSXVManagerDataSource::setEntityType(const OAIDataSourceType &entity_type) {
    m_entity_type = entity_type;
    m_entity_type_isSet = true;
}

bool OAINSXVManagerDataSource::is_entity_type_Set() const{
    return m_entity_type_isSet;
}

bool OAINSXVManagerDataSource::is_entity_type_Valid() const{
    return m_entity_type_isValid;
}

QString OAINSXVManagerDataSource::getFqdn() const {
    return m_fqdn;
}
void OAINSXVManagerDataSource::setFqdn(const QString &fqdn) {
    m_fqdn = fqdn;
    m_fqdn_isSet = true;
}

bool OAINSXVManagerDataSource::is_fqdn_Set() const{
    return m_fqdn_isSet;
}

bool OAINSXVManagerDataSource::is_fqdn_Valid() const{
    return m_fqdn_isValid;
}

QString OAINSXVManagerDataSource::getIp() const {
    return m_ip;
}
void OAINSXVManagerDataSource::setIp(const QString &ip) {
    m_ip = ip;
    m_ip_isSet = true;
}

bool OAINSXVManagerDataSource::is_ip_Set() const{
    return m_ip_isSet;
}

bool OAINSXVManagerDataSource::is_ip_Valid() const{
    return m_ip_isValid;
}

QString OAINSXVManagerDataSource::getNickname() const {
    return m_nickname;
}
void OAINSXVManagerDataSource::setNickname(const QString &nickname) {
    m_nickname = nickname;
    m_nickname_isSet = true;
}

bool OAINSXVManagerDataSource::is_nickname_Set() const{
    return m_nickname_isSet;
}

bool OAINSXVManagerDataSource::is_nickname_Valid() const{
    return m_nickname_isValid;
}

QString OAINSXVManagerDataSource::getNotes() const {
    return m_notes;
}
void OAINSXVManagerDataSource::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAINSXVManagerDataSource::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAINSXVManagerDataSource::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAINSXVManagerDataSource::getProxyId() const {
    return m_proxy_id;
}
void OAINSXVManagerDataSource::setProxyId(const QString &proxy_id) {
    m_proxy_id = proxy_id;
    m_proxy_id_isSet = true;
}

bool OAINSXVManagerDataSource::is_proxy_id_Set() const{
    return m_proxy_id_isSet;
}

bool OAINSXVManagerDataSource::is_proxy_id_Valid() const{
    return m_proxy_id_isValid;
}

bool OAINSXVManagerDataSource::isCentralCliEnabled() const {
    return m_central_cli_enabled;
}
void OAINSXVManagerDataSource::setCentralCliEnabled(const bool &central_cli_enabled) {
    m_central_cli_enabled = central_cli_enabled;
    m_central_cli_enabled_isSet = true;
}

bool OAINSXVManagerDataSource::is_central_cli_enabled_Set() const{
    return m_central_cli_enabled_isSet;
}

bool OAINSXVManagerDataSource::is_central_cli_enabled_Valid() const{
    return m_central_cli_enabled_isValid;
}

OAIPasswordCredentials OAINSXVManagerDataSource::getCredentials() const {
    return m_credentials;
}
void OAINSXVManagerDataSource::setCredentials(const OAIPasswordCredentials &credentials) {
    m_credentials = credentials;
    m_credentials_isSet = true;
}

bool OAINSXVManagerDataSource::is_credentials_Set() const{
    return m_credentials_isSet;
}

bool OAINSXVManagerDataSource::is_credentials_Valid() const{
    return m_credentials_isValid;
}

bool OAINSXVManagerDataSource::isIpfixEnabled() const {
    return m_ipfix_enabled;
}
void OAINSXVManagerDataSource::setIpfixEnabled(const bool &ipfix_enabled) {
    m_ipfix_enabled = ipfix_enabled;
    m_ipfix_enabled_isSet = true;
}

bool OAINSXVManagerDataSource::is_ipfix_enabled_Set() const{
    return m_ipfix_enabled_isSet;
}

bool OAINSXVManagerDataSource::is_ipfix_enabled_Valid() const{
    return m_ipfix_enabled_isValid;
}

QString OAINSXVManagerDataSource::getVcenterId() const {
    return m_vcenter_id;
}
void OAINSXVManagerDataSource::setVcenterId(const QString &vcenter_id) {
    m_vcenter_id = vcenter_id;
    m_vcenter_id_isSet = true;
}

bool OAINSXVManagerDataSource::is_vcenter_id_Set() const{
    return m_vcenter_id_isSet;
}

bool OAINSXVManagerDataSource::is_vcenter_id_Valid() const{
    return m_vcenter_id_isValid;
}

bool OAINSXVManagerDataSource::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_type.isSet()) {
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

        if (m_central_cli_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credentials.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ipfix_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vcenter_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINSXVManagerDataSource::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
