/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlanDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlanDetails::OAIPlanDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlanDetails::OAIPlanDetails() {
    this->initializeModel();
}

OAIPlanDetails::~OAIPlanDetails() {}

void OAIPlanDetails::initializeModel() {

    m_api_keys_isSet = false;
    m_api_keys_isValid = false;

    m_api_tokens_isSet = false;
    m_api_tokens_isValid = false;

    m_color_schema_isSet = false;
    m_color_schema_isValid = false;

    m_custom_domain_isSet = false;
    m_custom_domain_isValid = false;

    m_custom_name_isSet = false;
    m_custom_name_isValid = false;

    m_direct_links_isSet = false;
    m_direct_links_isValid = false;

    m_ip_whitelist_isSet = false;
    m_ip_whitelist_isValid = false;

    m_sharing_options_isSet = false;
    m_sharing_options_isValid = false;

    m_ssh_keys_isSet = false;
    m_ssh_keys_isValid = false;

    m_storage_add_on_isSet = false;
    m_storage_add_on_isValid = false;

    m_unlimited_users_isSet = false;
    m_unlimited_users_isValid = false;

    m_user_expiration_isSet = false;
    m_user_expiration_isValid = false;

    m_user_import_isSet = false;
    m_user_import_isValid = false;

    m_webhook_options_isSet = false;
    m_webhook_options_isValid = false;
}

void OAIPlanDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlanDetails::fromJsonObject(QJsonObject json) {

    m_api_keys_isValid = ::OpenAPI::fromJsonValue(m_api_keys, json[QString("apiKeys")]);
    m_api_keys_isSet = !json[QString("apiKeys")].isNull() && m_api_keys_isValid;

    m_api_tokens_isValid = ::OpenAPI::fromJsonValue(m_api_tokens, json[QString("apiTokens")]);
    m_api_tokens_isSet = !json[QString("apiTokens")].isNull() && m_api_tokens_isValid;

    m_color_schema_isValid = ::OpenAPI::fromJsonValue(m_color_schema, json[QString("colorSchema")]);
    m_color_schema_isSet = !json[QString("colorSchema")].isNull() && m_color_schema_isValid;

    m_custom_domain_isValid = ::OpenAPI::fromJsonValue(m_custom_domain, json[QString("customDomain")]);
    m_custom_domain_isSet = !json[QString("customDomain")].isNull() && m_custom_domain_isValid;

    m_custom_name_isValid = ::OpenAPI::fromJsonValue(m_custom_name, json[QString("customName")]);
    m_custom_name_isSet = !json[QString("customName")].isNull() && m_custom_name_isValid;

    m_direct_links_isValid = ::OpenAPI::fromJsonValue(m_direct_links, json[QString("directLinks")]);
    m_direct_links_isSet = !json[QString("directLinks")].isNull() && m_direct_links_isValid;

    m_ip_whitelist_isValid = ::OpenAPI::fromJsonValue(m_ip_whitelist, json[QString("ipWhitelist")]);
    m_ip_whitelist_isSet = !json[QString("ipWhitelist")].isNull() && m_ip_whitelist_isValid;

    m_sharing_options_isValid = ::OpenAPI::fromJsonValue(m_sharing_options, json[QString("sharingOptions")]);
    m_sharing_options_isSet = !json[QString("sharingOptions")].isNull() && m_sharing_options_isValid;

    m_ssh_keys_isValid = ::OpenAPI::fromJsonValue(m_ssh_keys, json[QString("sshKeys")]);
    m_ssh_keys_isSet = !json[QString("sshKeys")].isNull() && m_ssh_keys_isValid;

    m_storage_add_on_isValid = ::OpenAPI::fromJsonValue(m_storage_add_on, json[QString("storageAddOn")]);
    m_storage_add_on_isSet = !json[QString("storageAddOn")].isNull() && m_storage_add_on_isValid;

    m_unlimited_users_isValid = ::OpenAPI::fromJsonValue(m_unlimited_users, json[QString("unlimitedUsers")]);
    m_unlimited_users_isSet = !json[QString("unlimitedUsers")].isNull() && m_unlimited_users_isValid;

    m_user_expiration_isValid = ::OpenAPI::fromJsonValue(m_user_expiration, json[QString("userExpiration")]);
    m_user_expiration_isSet = !json[QString("userExpiration")].isNull() && m_user_expiration_isValid;

    m_user_import_isValid = ::OpenAPI::fromJsonValue(m_user_import, json[QString("userImport")]);
    m_user_import_isSet = !json[QString("userImport")].isNull() && m_user_import_isValid;

    m_webhook_options_isValid = ::OpenAPI::fromJsonValue(m_webhook_options, json[QString("webhookOptions")]);
    m_webhook_options_isSet = !json[QString("webhookOptions")].isNull() && m_webhook_options_isValid;
}

QString OAIPlanDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlanDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_api_keys_isSet) {
        obj.insert(QString("apiKeys"), ::OpenAPI::toJsonValue(m_api_keys));
    }
    if (m_api_tokens_isSet) {
        obj.insert(QString("apiTokens"), ::OpenAPI::toJsonValue(m_api_tokens));
    }
    if (m_color_schema_isSet) {
        obj.insert(QString("colorSchema"), ::OpenAPI::toJsonValue(m_color_schema));
    }
    if (m_custom_domain_isSet) {
        obj.insert(QString("customDomain"), ::OpenAPI::toJsonValue(m_custom_domain));
    }
    if (m_custom_name_isSet) {
        obj.insert(QString("customName"), ::OpenAPI::toJsonValue(m_custom_name));
    }
    if (m_direct_links_isSet) {
        obj.insert(QString("directLinks"), ::OpenAPI::toJsonValue(m_direct_links));
    }
    if (m_ip_whitelist_isSet) {
        obj.insert(QString("ipWhitelist"), ::OpenAPI::toJsonValue(m_ip_whitelist));
    }
    if (m_sharing_options.size() > 0) {
        obj.insert(QString("sharingOptions"), ::OpenAPI::toJsonValue(m_sharing_options));
    }
    if (m_ssh_keys_isSet) {
        obj.insert(QString("sshKeys"), ::OpenAPI::toJsonValue(m_ssh_keys));
    }
    if (m_storage_add_on_isSet) {
        obj.insert(QString("storageAddOn"), ::OpenAPI::toJsonValue(m_storage_add_on));
    }
    if (m_unlimited_users_isSet) {
        obj.insert(QString("unlimitedUsers"), ::OpenAPI::toJsonValue(m_unlimited_users));
    }
    if (m_user_expiration_isSet) {
        obj.insert(QString("userExpiration"), ::OpenAPI::toJsonValue(m_user_expiration));
    }
    if (m_user_import_isSet) {
        obj.insert(QString("userImport"), ::OpenAPI::toJsonValue(m_user_import));
    }
    if (m_webhook_options.isSet()) {
        obj.insert(QString("webhookOptions"), ::OpenAPI::toJsonValue(m_webhook_options));
    }
    return obj;
}

qint32 OAIPlanDetails::getApiKeys() const {
    return m_api_keys;
}
void OAIPlanDetails::setApiKeys(const qint32 &api_keys) {
    m_api_keys = api_keys;
    m_api_keys_isSet = true;
}

bool OAIPlanDetails::is_api_keys_Set() const{
    return m_api_keys_isSet;
}

bool OAIPlanDetails::is_api_keys_Valid() const{
    return m_api_keys_isValid;
}

qint32 OAIPlanDetails::getApiTokens() const {
    return m_api_tokens;
}
void OAIPlanDetails::setApiTokens(const qint32 &api_tokens) {
    m_api_tokens = api_tokens;
    m_api_tokens_isSet = true;
}

bool OAIPlanDetails::is_api_tokens_Set() const{
    return m_api_tokens_isSet;
}

bool OAIPlanDetails::is_api_tokens_Valid() const{
    return m_api_tokens_isValid;
}

bool OAIPlanDetails::isColorSchema() const {
    return m_color_schema;
}
void OAIPlanDetails::setColorSchema(const bool &color_schema) {
    m_color_schema = color_schema;
    m_color_schema_isSet = true;
}

bool OAIPlanDetails::is_color_schema_Set() const{
    return m_color_schema_isSet;
}

bool OAIPlanDetails::is_color_schema_Valid() const{
    return m_color_schema_isValid;
}

bool OAIPlanDetails::isCustomDomain() const {
    return m_custom_domain;
}
void OAIPlanDetails::setCustomDomain(const bool &custom_domain) {
    m_custom_domain = custom_domain;
    m_custom_domain_isSet = true;
}

bool OAIPlanDetails::is_custom_domain_Set() const{
    return m_custom_domain_isSet;
}

bool OAIPlanDetails::is_custom_domain_Valid() const{
    return m_custom_domain_isValid;
}

bool OAIPlanDetails::isCustomName() const {
    return m_custom_name;
}
void OAIPlanDetails::setCustomName(const bool &custom_name) {
    m_custom_name = custom_name;
    m_custom_name_isSet = true;
}

bool OAIPlanDetails::is_custom_name_Set() const{
    return m_custom_name_isSet;
}

bool OAIPlanDetails::is_custom_name_Valid() const{
    return m_custom_name_isValid;
}

bool OAIPlanDetails::isDirectLinks() const {
    return m_direct_links;
}
void OAIPlanDetails::setDirectLinks(const bool &direct_links) {
    m_direct_links = direct_links;
    m_direct_links_isSet = true;
}

bool OAIPlanDetails::is_direct_links_Set() const{
    return m_direct_links_isSet;
}

bool OAIPlanDetails::is_direct_links_Valid() const{
    return m_direct_links_isValid;
}

bool OAIPlanDetails::isIpWhitelist() const {
    return m_ip_whitelist;
}
void OAIPlanDetails::setIpWhitelist(const bool &ip_whitelist) {
    m_ip_whitelist = ip_whitelist;
    m_ip_whitelist_isSet = true;
}

bool OAIPlanDetails::is_ip_whitelist_Set() const{
    return m_ip_whitelist_isSet;
}

bool OAIPlanDetails::is_ip_whitelist_Valid() const{
    return m_ip_whitelist_isValid;
}

QList<QString> OAIPlanDetails::getSharingOptions() const {
    return m_sharing_options;
}
void OAIPlanDetails::setSharingOptions(const QList<QString> &sharing_options) {
    m_sharing_options = sharing_options;
    m_sharing_options_isSet = true;
}

bool OAIPlanDetails::is_sharing_options_Set() const{
    return m_sharing_options_isSet;
}

bool OAIPlanDetails::is_sharing_options_Valid() const{
    return m_sharing_options_isValid;
}

qint32 OAIPlanDetails::getSshKeys() const {
    return m_ssh_keys;
}
void OAIPlanDetails::setSshKeys(const qint32 &ssh_keys) {
    m_ssh_keys = ssh_keys;
    m_ssh_keys_isSet = true;
}

bool OAIPlanDetails::is_ssh_keys_Set() const{
    return m_ssh_keys_isSet;
}

bool OAIPlanDetails::is_ssh_keys_Valid() const{
    return m_ssh_keys_isValid;
}

qint32 OAIPlanDetails::getStorageAddOn() const {
    return m_storage_add_on;
}
void OAIPlanDetails::setStorageAddOn(const qint32 &storage_add_on) {
    m_storage_add_on = storage_add_on;
    m_storage_add_on_isSet = true;
}

bool OAIPlanDetails::is_storage_add_on_Set() const{
    return m_storage_add_on_isSet;
}

bool OAIPlanDetails::is_storage_add_on_Valid() const{
    return m_storage_add_on_isValid;
}

bool OAIPlanDetails::isUnlimitedUsers() const {
    return m_unlimited_users;
}
void OAIPlanDetails::setUnlimitedUsers(const bool &unlimited_users) {
    m_unlimited_users = unlimited_users;
    m_unlimited_users_isSet = true;
}

bool OAIPlanDetails::is_unlimited_users_Set() const{
    return m_unlimited_users_isSet;
}

bool OAIPlanDetails::is_unlimited_users_Valid() const{
    return m_unlimited_users_isValid;
}

bool OAIPlanDetails::isUserExpiration() const {
    return m_user_expiration;
}
void OAIPlanDetails::setUserExpiration(const bool &user_expiration) {
    m_user_expiration = user_expiration;
    m_user_expiration_isSet = true;
}

bool OAIPlanDetails::is_user_expiration_Set() const{
    return m_user_expiration_isSet;
}

bool OAIPlanDetails::is_user_expiration_Valid() const{
    return m_user_expiration_isValid;
}

bool OAIPlanDetails::isUserImport() const {
    return m_user_import;
}
void OAIPlanDetails::setUserImport(const bool &user_import) {
    m_user_import = user_import;
    m_user_import_isSet = true;
}

bool OAIPlanDetails::is_user_import_Set() const{
    return m_user_import_isSet;
}

bool OAIPlanDetails::is_user_import_Valid() const{
    return m_user_import_isValid;
}

OAIPlanDetails_webhookOptions OAIPlanDetails::getWebhookOptions() const {
    return m_webhook_options;
}
void OAIPlanDetails::setWebhookOptions(const OAIPlanDetails_webhookOptions &webhook_options) {
    m_webhook_options = webhook_options;
    m_webhook_options_isSet = true;
}

bool OAIPlanDetails::is_webhook_options_Set() const{
    return m_webhook_options_isSet;
}

bool OAIPlanDetails::is_webhook_options_Valid() const{
    return m_webhook_options_isValid;
}

bool OAIPlanDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_keys_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_api_tokens_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_color_schema_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_domain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_direct_links_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_whitelist_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sharing_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssh_keys_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_storage_add_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unlimited_users_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_expiration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_import_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_webhook_options.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlanDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
