/**
 * Vault API
 * Welcome to the Vault API 👋  When you're looking to connect to an API, the first step is authentication.  Vault helps you handle OAuth flows, store API keys, and refresh access tokens from users (called consumers in Apideck).  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Get Started  To use the Apideck APIs, you need to sign up for free at [https://app.apideck.com/signup](). Follow the steps below to get started.  - [Create a free account.](https://app.apideck.com/signup) - Go to the [Dashboard](https://app.apideck.com/unify/unified-apis/dashboard). - Get your API key and the application ID. - Select and configure the integrations you want to make available to your users. Through the Unify dashboard, you can configure which connectors you want to support as integrations. - Retrieve the client_id and client_secret for the integration you want to activate (Only needed for OAuth integrations). - Soon, you can skip the previous step and use the Apideck sandbox credentials to get you started instead (upcoming) - Register the redirect URI for the example app (https://unify.apideck.com/vault/callback) in the list of redirect URIs under your app's settings - Use the [publishing guides](/app-listing-requirements) to get your integration listed across app marketplaces.  ### Hosted Vault  Hosted Vault (vault.apideck.com) is a no-code solution, so you don't need to build your own UI to handle the integration settings and authentication.  ![Hosted Vault - Integrations portal](https://github.com/apideck-samples/integration-settings/raw/master/public/img/vault.png)  Behind the scenes, Hosted Vault implements the Vault API endpoints and handles the following features for your customers:  - Add a connection - Handle the OAuth flow - Configure connection settings per integration - Manage connections - Discover and propose integration options - Search for integrations (upcoming) - Give integration suggestions based on provided metadata (email or website) when creating the session (upcoming)  To use Hosted Vault, you will need to first [**create a session**](https://developers.apideck.com/apis/vault/reference#operation/sessionsCreate). This can be achieved by making a POST request to the Vault API to create a valid session for a user, hereafter referred to as the consumer ID.  Example using curl:  ``` curl -X POST https://unify.apideck.com/vault/sessions     -H \"Content-Type: application/json\"     -H \"Authorization: Bearer <your-api-key>\"     -H \"X-APIDECK-CONSUMER-ID: <consumer-id>\"     -H \"X-APIDECK-APP-ID: <application-id>\"     -d '{\"consumer_metadata\": { \"account_name\" : \"Sample\", \"user_name\": \"Sand Box\", \"email\": \"sand@box.com\", \"image\": \"https://unavatar.now.sh/jake\" }, \"theme\": { \"vault_name\": \"Intercom\", \"primary_color\": \"#286efa\", \"sidepanel_background_color\": \"#286efa\",\"sidepanel_text_color\": \"#FFFFFF\", \"favicon\": \"https://res.cloudinary.com/apideck/icons/intercom\" }}' ```  ### Vault API  _Beware, this is strategy takes more time to implement in comparison to Hosted Vault._  If you are building your integration settings UI manually, you can call the Vault API directly.  The Vault API is for those who want to completely white label the in-app integrations overview and authentication experience. All the available endpoints are listed below.  Through the API, your customers authenticate directly in your app, where Vault will still take care of redirecting to the auth provider and back to your app.  If you're already storing access tokens, we will help you migrate through our Vault Migration API (upcoming).  ## Domain model  At its core, a domain model creates a web of interconnected entities.  Our domain model contains five main entity types: Consumer (user, account, team, machine), Application, Connector, Integration, and Connection.  ## Connection state  The connection state is computed based on the connection flow below.  ![](https://developers.apideck.com/api-references/vault/connection-flow.png)  More information about the connection state can be found in the [Connection state](https://developers.apideck.com/guides/connection-states) guide.  ## Unify and Proxy integration  The only thing you need to use the Unify APIs and Proxy is the consumer id; thereafter, Vault will do the look-up in the background to handle the token injection before performing the API call(s).  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-app-id      | String  | Yes      | The id of your Unify application. Available at https://app.apideck.com/api-keys. | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes. |  ## Guides  - [Get started with Apideck](https://developers.apideck.com/getting-started) - [Get started with Vault](https://developers.apideck.com/guides/vault) - [Authorize connection via Vault](https://developers.apideck.com/guides/authorize-connections) - [Vault connection status](https://developers.apideck.com/guides/connection-states) - [How to build an integrations UI with Vault](https://github.com/apideck-samples/integration-settings)   ## FAQ  **What purpose does Vault serve? Can I just handle the authentication and access token myself?** You can store everything yourself, but that defeats the purpose of using Apideck Unify. Handling tokens for multiple providers can quickly become very complex.  ### Is my data secure?  Vault employs data minimization, therefore only requesting the minimum amount of scopes needed to perform an API request.  ### How do I migrate existing data?  Using our migration API, you can migrate the access tokens and accounts to Apideck Vault.  ### Can I use Vault in combination with existing integrations?  Yes, you can. The flexibility of Unify allows you to quickly the use cases you need while keeping a gradual migration path based on your timeline and requirements.  ### How does Vault work for Apideck Ecosystem customers?  Once logged in, pick your ecosystem; on the left-hand side of the screen, you'll have the option to create an application underneath the Unify section.  ### How to integrate Apideck Vault  This section covers everything you need to know to authenticate your customers through Vault. Vault provides **three auth strategies** to use API tokens from your customers:  - Vault API - Hosted Vault - Vault Widget (JS, React, Vue)  You can also opt to bypass Vault and still take care of authentication flows yourself. Make sure to put the right safeguards in place to protect your customers' tokens and other sensitive data.  ### What auth types does Vault support?  We support all the common authentication types, including: API keys, OAuth, Basic auth, and more.  #### API keys  For Services supporting the API key strategy, you can use Hosted Vault will need to provide an in-app form where users can configure their API keys provided by the integration service.  #### OAuth 2.0  ##### Authorization Code Grant Type Flow  Vault handles the complete Authorization Code Grant Type Flow for you. This flow only supports browser-based (passive) authentication because most identity providers don't allow entering a username and password to be entered into applications that they don't own.  Certain connectors require an OAuth redirect authentication flow, where the end-user is redirected to the provider's website or mobile app to authenticate.  This is being handled by the `/authorize` endpoint.  #### Basic auth  Basic authentication is a simple authentication scheme built into the HTTP protocol. The required fields to complete basic auth are handled by Hosted Vault or by updating the connection through the Vault API below.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConnection.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConnection::OAIConnection(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConnection::OAIConnection() {
    this->initializeModel();
}

OAIConnection::~OAIConnection() {}

void OAIConnection::initializeModel() {

    m_auth_type_isSet = false;
    m_auth_type_isValid = false;

    m_authorize_url_isSet = false;
    m_authorize_url_isValid = false;

    m_configurable_resources_isSet = false;
    m_configurable_resources_isValid = false;

    m_configuration_isSet = false;
    m_configuration_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_form_fields_isSet = false;
    m_form_fields_isValid = false;

    m_has_guide_isSet = false;
    m_has_guide_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_integration_state_isSet = false;
    m_integration_state_isValid = false;

    m_logo_isSet = false;
    m_logo_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_oauth_grant_type_isSet = false;
    m_oauth_grant_type_isValid = false;

    m_resource_schema_support_isSet = false;
    m_resource_schema_support_isValid = false;

    m_resource_settings_support_isSet = false;
    m_resource_settings_support_isValid = false;

    m_revoke_url_isSet = false;
    m_revoke_url_isValid = false;

    m_schema_support_isSet = false;
    m_schema_support_isValid = false;

    m_service_id_isSet = false;
    m_service_id_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_settings_required_for_authorization_isSet = false;
    m_settings_required_for_authorization_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscriptions_isSet = false;
    m_subscriptions_isValid = false;

    m_tag_line_isSet = false;
    m_tag_line_isValid = false;

    m_unified_api_isSet = false;
    m_unified_api_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_validation_support_isSet = false;
    m_validation_support_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAIConnection::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConnection::fromJsonObject(QJsonObject json) {

    m_auth_type_isValid = ::OpenAPI::fromJsonValue(m_auth_type, json[QString("auth_type")]);
    m_auth_type_isSet = !json[QString("auth_type")].isNull() && m_auth_type_isValid;

    m_authorize_url_isValid = ::OpenAPI::fromJsonValue(m_authorize_url, json[QString("authorize_url")]);
    m_authorize_url_isSet = !json[QString("authorize_url")].isNull() && m_authorize_url_isValid;

    m_configurable_resources_isValid = ::OpenAPI::fromJsonValue(m_configurable_resources, json[QString("configurable_resources")]);
    m_configurable_resources_isSet = !json[QString("configurable_resources")].isNull() && m_configurable_resources_isValid;

    m_configuration_isValid = ::OpenAPI::fromJsonValue(m_configuration, json[QString("configuration")]);
    m_configuration_isSet = !json[QString("configuration")].isNull() && m_configuration_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_form_fields_isValid = ::OpenAPI::fromJsonValue(m_form_fields, json[QString("form_fields")]);
    m_form_fields_isSet = !json[QString("form_fields")].isNull() && m_form_fields_isValid;

    m_has_guide_isValid = ::OpenAPI::fromJsonValue(m_has_guide, json[QString("has_guide")]);
    m_has_guide_isSet = !json[QString("has_guide")].isNull() && m_has_guide_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_integration_state_isValid = ::OpenAPI::fromJsonValue(m_integration_state, json[QString("integration_state")]);
    m_integration_state_isSet = !json[QString("integration_state")].isNull() && m_integration_state_isValid;

    m_logo_isValid = ::OpenAPI::fromJsonValue(m_logo, json[QString("logo")]);
    m_logo_isSet = !json[QString("logo")].isNull() && m_logo_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_oauth_grant_type_isValid = ::OpenAPI::fromJsonValue(m_oauth_grant_type, json[QString("oauth_grant_type")]);
    m_oauth_grant_type_isSet = !json[QString("oauth_grant_type")].isNull() && m_oauth_grant_type_isValid;

    m_resource_schema_support_isValid = ::OpenAPI::fromJsonValue(m_resource_schema_support, json[QString("resource_schema_support")]);
    m_resource_schema_support_isSet = !json[QString("resource_schema_support")].isNull() && m_resource_schema_support_isValid;

    m_resource_settings_support_isValid = ::OpenAPI::fromJsonValue(m_resource_settings_support, json[QString("resource_settings_support")]);
    m_resource_settings_support_isSet = !json[QString("resource_settings_support")].isNull() && m_resource_settings_support_isValid;

    m_revoke_url_isValid = ::OpenAPI::fromJsonValue(m_revoke_url, json[QString("revoke_url")]);
    m_revoke_url_isSet = !json[QString("revoke_url")].isNull() && m_revoke_url_isValid;

    m_schema_support_isValid = ::OpenAPI::fromJsonValue(m_schema_support, json[QString("schema_support")]);
    m_schema_support_isSet = !json[QString("schema_support")].isNull() && m_schema_support_isValid;

    m_service_id_isValid = ::OpenAPI::fromJsonValue(m_service_id, json[QString("service_id")]);
    m_service_id_isSet = !json[QString("service_id")].isNull() && m_service_id_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_settings_required_for_authorization_isValid = ::OpenAPI::fromJsonValue(m_settings_required_for_authorization, json[QString("settings_required_for_authorization")]);
    m_settings_required_for_authorization_isSet = !json[QString("settings_required_for_authorization")].isNull() && m_settings_required_for_authorization_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscriptions_isValid = ::OpenAPI::fromJsonValue(m_subscriptions, json[QString("subscriptions")]);
    m_subscriptions_isSet = !json[QString("subscriptions")].isNull() && m_subscriptions_isValid;

    m_tag_line_isValid = ::OpenAPI::fromJsonValue(m_tag_line, json[QString("tag_line")]);
    m_tag_line_isSet = !json[QString("tag_line")].isNull() && m_tag_line_isValid;

    m_unified_api_isValid = ::OpenAPI::fromJsonValue(m_unified_api, json[QString("unified_api")]);
    m_unified_api_isSet = !json[QString("unified_api")].isNull() && m_unified_api_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_validation_support_isValid = ::OpenAPI::fromJsonValue(m_validation_support, json[QString("validation_support")]);
    m_validation_support_isSet = !json[QString("validation_support")].isNull() && m_validation_support_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAIConnection::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConnection::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_type.isSet()) {
        obj.insert(QString("auth_type"), ::OpenAPI::toJsonValue(m_auth_type));
    }
    if (m_authorize_url_isSet) {
        obj.insert(QString("authorize_url"), ::OpenAPI::toJsonValue(m_authorize_url));
    }
    if (m_configurable_resources.size() > 0) {
        obj.insert(QString("configurable_resources"), ::OpenAPI::toJsonValue(m_configurable_resources));
    }
    if (m_configuration.size() > 0) {
        obj.insert(QString("configuration"), ::OpenAPI::toJsonValue(m_configuration));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_custom_mappings.size() > 0) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_form_fields.size() > 0) {
        obj.insert(QString("form_fields"), ::OpenAPI::toJsonValue(m_form_fields));
    }
    if (m_has_guide_isSet) {
        obj.insert(QString("has_guide"), ::OpenAPI::toJsonValue(m_has_guide));
    }
    if (m_icon_isSet) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_integration_state.isSet()) {
        obj.insert(QString("integration_state"), ::OpenAPI::toJsonValue(m_integration_state));
    }
    if (m_logo_isSet) {
        obj.insert(QString("logo"), ::OpenAPI::toJsonValue(m_logo));
    }
    if (m_metadata.size() > 0) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_oauth_grant_type.isSet()) {
        obj.insert(QString("oauth_grant_type"), ::OpenAPI::toJsonValue(m_oauth_grant_type));
    }
    if (m_resource_schema_support.size() > 0) {
        obj.insert(QString("resource_schema_support"), ::OpenAPI::toJsonValue(m_resource_schema_support));
    }
    if (m_resource_settings_support.size() > 0) {
        obj.insert(QString("resource_settings_support"), ::OpenAPI::toJsonValue(m_resource_settings_support));
    }
    if (m_revoke_url_isSet) {
        obj.insert(QString("revoke_url"), ::OpenAPI::toJsonValue(m_revoke_url));
    }
    if (m_schema_support_isSet) {
        obj.insert(QString("schema_support"), ::OpenAPI::toJsonValue(m_schema_support));
    }
    if (m_service_id_isSet) {
        obj.insert(QString("service_id"), ::OpenAPI::toJsonValue(m_service_id));
    }
    if (m_settings.size() > 0) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_settings_required_for_authorization.size() > 0) {
        obj.insert(QString("settings_required_for_authorization"), ::OpenAPI::toJsonValue(m_settings_required_for_authorization));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscriptions.size() > 0) {
        obj.insert(QString("subscriptions"), ::OpenAPI::toJsonValue(m_subscriptions));
    }
    if (m_tag_line_isSet) {
        obj.insert(QString("tag_line"), ::OpenAPI::toJsonValue(m_tag_line));
    }
    if (m_unified_api_isSet) {
        obj.insert(QString("unified_api"), ::OpenAPI::toJsonValue(m_unified_api));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_validation_support_isSet) {
        obj.insert(QString("validation_support"), ::OpenAPI::toJsonValue(m_validation_support));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

OAIAuthType OAIConnection::getAuthType() const {
    return m_auth_type;
}
void OAIConnection::setAuthType(const OAIAuthType &auth_type) {
    m_auth_type = auth_type;
    m_auth_type_isSet = true;
}

bool OAIConnection::is_auth_type_Set() const{
    return m_auth_type_isSet;
}

bool OAIConnection::is_auth_type_Valid() const{
    return m_auth_type_isValid;
}

QString OAIConnection::getAuthorizeUrl() const {
    return m_authorize_url;
}
void OAIConnection::setAuthorizeUrl(const QString &authorize_url) {
    m_authorize_url = authorize_url;
    m_authorize_url_isSet = true;
}

bool OAIConnection::is_authorize_url_Set() const{
    return m_authorize_url_isSet;
}

bool OAIConnection::is_authorize_url_Valid() const{
    return m_authorize_url_isValid;
}

QList<QString> OAIConnection::getConfigurableResources() const {
    return m_configurable_resources;
}
void OAIConnection::setConfigurableResources(const QList<QString> &configurable_resources) {
    m_configurable_resources = configurable_resources;
    m_configurable_resources_isSet = true;
}

bool OAIConnection::is_configurable_resources_Set() const{
    return m_configurable_resources_isSet;
}

bool OAIConnection::is_configurable_resources_Valid() const{
    return m_configurable_resources_isValid;
}

QList<OAIConnection_configuration_inner> OAIConnection::getConfiguration() const {
    return m_configuration;
}
void OAIConnection::setConfiguration(const QList<OAIConnection_configuration_inner> &configuration) {
    m_configuration = configuration;
    m_configuration_isSet = true;
}

bool OAIConnection::is_configuration_Set() const{
    return m_configuration_isSet;
}

bool OAIConnection::is_configuration_Valid() const{
    return m_configuration_isValid;
}

double OAIConnection::getCreatedAt() const {
    return m_created_at;
}
void OAIConnection::setCreatedAt(const double &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIConnection::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIConnection::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QList<OAICustomMapping> OAIConnection::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIConnection::setCustomMappings(const QList<OAICustomMapping> &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIConnection::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIConnection::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

bool OAIConnection::isEnabled() const {
    return m_enabled;
}
void OAIConnection::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIConnection::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIConnection::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QList<OAIFormField> OAIConnection::getFormFields() const {
    return m_form_fields;
}
void OAIConnection::setFormFields(const QList<OAIFormField> &form_fields) {
    m_form_fields = form_fields;
    m_form_fields_isSet = true;
}

bool OAIConnection::is_form_fields_Set() const{
    return m_form_fields_isSet;
}

bool OAIConnection::is_form_fields_Valid() const{
    return m_form_fields_isValid;
}

bool OAIConnection::isHasGuide() const {
    return m_has_guide;
}
void OAIConnection::setHasGuide(const bool &has_guide) {
    m_has_guide = has_guide;
    m_has_guide_isSet = true;
}

bool OAIConnection::is_has_guide_Set() const{
    return m_has_guide_isSet;
}

bool OAIConnection::is_has_guide_Valid() const{
    return m_has_guide_isValid;
}

QString OAIConnection::getIcon() const {
    return m_icon;
}
void OAIConnection::setIcon(const QString &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAIConnection::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAIConnection::is_icon_Valid() const{
    return m_icon_isValid;
}

QString OAIConnection::getId() const {
    return m_id;
}
void OAIConnection::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIConnection::is_id_Set() const{
    return m_id_isSet;
}

bool OAIConnection::is_id_Valid() const{
    return m_id_isValid;
}

OAIIntegrationState OAIConnection::getIntegrationState() const {
    return m_integration_state;
}
void OAIConnection::setIntegrationState(const OAIIntegrationState &integration_state) {
    m_integration_state = integration_state;
    m_integration_state_isSet = true;
}

bool OAIConnection::is_integration_state_Set() const{
    return m_integration_state_isSet;
}

bool OAIConnection::is_integration_state_Valid() const{
    return m_integration_state_isValid;
}

QString OAIConnection::getLogo() const {
    return m_logo;
}
void OAIConnection::setLogo(const QString &logo) {
    m_logo = logo;
    m_logo_isSet = true;
}

bool OAIConnection::is_logo_Set() const{
    return m_logo_isSet;
}

bool OAIConnection::is_logo_Valid() const{
    return m_logo_isValid;
}

QMap<QString, QJsonValue> OAIConnection::getMetadata() const {
    return m_metadata;
}
void OAIConnection::setMetadata(const QMap<QString, QJsonValue> &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIConnection::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIConnection::is_metadata_Valid() const{
    return m_metadata_isValid;
}

QString OAIConnection::getName() const {
    return m_name;
}
void OAIConnection::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIConnection::is_name_Set() const{
    return m_name_isSet;
}

bool OAIConnection::is_name_Valid() const{
    return m_name_isValid;
}

OAIOAuthGrantType OAIConnection::getOauthGrantType() const {
    return m_oauth_grant_type;
}
void OAIConnection::setOauthGrantType(const OAIOAuthGrantType &oauth_grant_type) {
    m_oauth_grant_type = oauth_grant_type;
    m_oauth_grant_type_isSet = true;
}

bool OAIConnection::is_oauth_grant_type_Set() const{
    return m_oauth_grant_type_isSet;
}

bool OAIConnection::is_oauth_grant_type_Valid() const{
    return m_oauth_grant_type_isValid;
}

QList<QString> OAIConnection::getResourceSchemaSupport() const {
    return m_resource_schema_support;
}
void OAIConnection::setResourceSchemaSupport(const QList<QString> &resource_schema_support) {
    m_resource_schema_support = resource_schema_support;
    m_resource_schema_support_isSet = true;
}

bool OAIConnection::is_resource_schema_support_Set() const{
    return m_resource_schema_support_isSet;
}

bool OAIConnection::is_resource_schema_support_Valid() const{
    return m_resource_schema_support_isValid;
}

QList<QString> OAIConnection::getResourceSettingsSupport() const {
    return m_resource_settings_support;
}
void OAIConnection::setResourceSettingsSupport(const QList<QString> &resource_settings_support) {
    m_resource_settings_support = resource_settings_support;
    m_resource_settings_support_isSet = true;
}

bool OAIConnection::is_resource_settings_support_Set() const{
    return m_resource_settings_support_isSet;
}

bool OAIConnection::is_resource_settings_support_Valid() const{
    return m_resource_settings_support_isValid;
}

QString OAIConnection::getRevokeUrl() const {
    return m_revoke_url;
}
void OAIConnection::setRevokeUrl(const QString &revoke_url) {
    m_revoke_url = revoke_url;
    m_revoke_url_isSet = true;
}

bool OAIConnection::is_revoke_url_Set() const{
    return m_revoke_url_isSet;
}

bool OAIConnection::is_revoke_url_Valid() const{
    return m_revoke_url_isValid;
}

bool OAIConnection::isSchemaSupport() const {
    return m_schema_support;
}
void OAIConnection::setSchemaSupport(const bool &schema_support) {
    m_schema_support = schema_support;
    m_schema_support_isSet = true;
}

bool OAIConnection::is_schema_support_Set() const{
    return m_schema_support_isSet;
}

bool OAIConnection::is_schema_support_Valid() const{
    return m_schema_support_isValid;
}

QString OAIConnection::getServiceId() const {
    return m_service_id;
}
void OAIConnection::setServiceId(const QString &service_id) {
    m_service_id = service_id;
    m_service_id_isSet = true;
}

bool OAIConnection::is_service_id_Set() const{
    return m_service_id_isSet;
}

bool OAIConnection::is_service_id_Valid() const{
    return m_service_id_isValid;
}

QMap<QString, QJsonValue> OAIConnection::getSettings() const {
    return m_settings;
}
void OAIConnection::setSettings(const QMap<QString, QJsonValue> &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIConnection::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIConnection::is_settings_Valid() const{
    return m_settings_isValid;
}

QList<QString> OAIConnection::getSettingsRequiredForAuthorization() const {
    return m_settings_required_for_authorization;
}
void OAIConnection::setSettingsRequiredForAuthorization(const QList<QString> &settings_required_for_authorization) {
    m_settings_required_for_authorization = settings_required_for_authorization;
    m_settings_required_for_authorization_isSet = true;
}

bool OAIConnection::is_settings_required_for_authorization_Set() const{
    return m_settings_required_for_authorization_isSet;
}

bool OAIConnection::is_settings_required_for_authorization_Valid() const{
    return m_settings_required_for_authorization_isValid;
}

OAIConnectionState OAIConnection::getState() const {
    return m_state;
}
void OAIConnection::setState(const OAIConnectionState &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIConnection::is_state_Set() const{
    return m_state_isSet;
}

bool OAIConnection::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIConnection::getStatus() const {
    return m_status;
}
void OAIConnection::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIConnection::is_status_Set() const{
    return m_status_isSet;
}

bool OAIConnection::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIWebhookSubscription> OAIConnection::getSubscriptions() const {
    return m_subscriptions;
}
void OAIConnection::setSubscriptions(const QList<OAIWebhookSubscription> &subscriptions) {
    m_subscriptions = subscriptions;
    m_subscriptions_isSet = true;
}

bool OAIConnection::is_subscriptions_Set() const{
    return m_subscriptions_isSet;
}

bool OAIConnection::is_subscriptions_Valid() const{
    return m_subscriptions_isValid;
}

QString OAIConnection::getTagLine() const {
    return m_tag_line;
}
void OAIConnection::setTagLine(const QString &tag_line) {
    m_tag_line = tag_line;
    m_tag_line_isSet = true;
}

bool OAIConnection::is_tag_line_Set() const{
    return m_tag_line_isSet;
}

bool OAIConnection::is_tag_line_Valid() const{
    return m_tag_line_isValid;
}

QString OAIConnection::getUnifiedApi() const {
    return m_unified_api;
}
void OAIConnection::setUnifiedApi(const QString &unified_api) {
    m_unified_api = unified_api;
    m_unified_api_isSet = true;
}

bool OAIConnection::is_unified_api_Set() const{
    return m_unified_api_isSet;
}

bool OAIConnection::is_unified_api_Valid() const{
    return m_unified_api_isValid;
}

double OAIConnection::getUpdatedAt() const {
    return m_updated_at;
}
void OAIConnection::setUpdatedAt(const double &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIConnection::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIConnection::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIConnection::isValidationSupport() const {
    return m_validation_support;
}
void OAIConnection::setValidationSupport(const bool &validation_support) {
    m_validation_support = validation_support;
    m_validation_support_isSet = true;
}

bool OAIConnection::is_validation_support_Set() const{
    return m_validation_support_isSet;
}

bool OAIConnection::is_validation_support_Valid() const{
    return m_validation_support_isValid;
}

QString OAIConnection::getWebsite() const {
    return m_website;
}
void OAIConnection::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAIConnection::is_website_Set() const{
    return m_website_isSet;
}

bool OAIConnection::is_website_Valid() const{
    return m_website_isValid;
}

bool OAIConnection::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_authorize_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_configurable_resources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_configuration.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_mappings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_guide_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_integration_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oauth_grant_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_schema_support.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_resource_settings_support.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_revoke_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schema_support_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_required_for_authorization.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscriptions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_line_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unified_api_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validation_support_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConnection::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
