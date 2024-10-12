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

/*
 * OAIConnection.h
 *
 * 
 */

#ifndef OAIConnection_H
#define OAIConnection_H

#include <QJsonObject>

#include "OAIAuthType.h"
#include "OAIConnectionState.h"
#include "OAIConnection_configuration_inner.h"
#include "OAICustomMapping.h"
#include "OAIFormField.h"
#include "OAIIntegrationState.h"
#include "OAIOAuthGrantType.h"
#include "OAIWebhookSubscription.h"
#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConnection_configuration_inner;
class OAICustomMapping;
class OAIFormField;
class OAIWebhookSubscription;

class OAIConnection : public OAIObject {
public:
    OAIConnection();
    OAIConnection(QString json);
    ~OAIConnection() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAuthType getAuthType() const;
    void setAuthType(const OAIAuthType &auth_type);
    bool is_auth_type_Set() const;
    bool is_auth_type_Valid() const;

    QString getAuthorizeUrl() const;
    void setAuthorizeUrl(const QString &authorize_url);
    bool is_authorize_url_Set() const;
    bool is_authorize_url_Valid() const;

    QList<QString> getConfigurableResources() const;
    void setConfigurableResources(const QList<QString> &configurable_resources);
    bool is_configurable_resources_Set() const;
    bool is_configurable_resources_Valid() const;

    QList<OAIConnection_configuration_inner> getConfiguration() const;
    void setConfiguration(const QList<OAIConnection_configuration_inner> &configuration);
    bool is_configuration_Set() const;
    bool is_configuration_Valid() const;

    double getCreatedAt() const;
    void setCreatedAt(const double &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QList<OAICustomMapping> getCustomMappings() const;
    void setCustomMappings(const QList<OAICustomMapping> &custom_mappings);
    bool is_custom_mappings_Set() const;
    bool is_custom_mappings_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QList<OAIFormField> getFormFields() const;
    void setFormFields(const QList<OAIFormField> &form_fields);
    bool is_form_fields_Set() const;
    bool is_form_fields_Valid() const;

    bool isHasGuide() const;
    void setHasGuide(const bool &has_guide);
    bool is_has_guide_Set() const;
    bool is_has_guide_Valid() const;

    QString getIcon() const;
    void setIcon(const QString &icon);
    bool is_icon_Set() const;
    bool is_icon_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIIntegrationState getIntegrationState() const;
    void setIntegrationState(const OAIIntegrationState &integration_state);
    bool is_integration_state_Set() const;
    bool is_integration_state_Valid() const;

    QString getLogo() const;
    void setLogo(const QString &logo);
    bool is_logo_Set() const;
    bool is_logo_Valid() const;

    QMap<QString, QJsonValue> getMetadata() const;
    void setMetadata(const QMap<QString, QJsonValue> &metadata);
    bool is_metadata_Set() const;
    bool is_metadata_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIOAuthGrantType getOauthGrantType() const;
    void setOauthGrantType(const OAIOAuthGrantType &oauth_grant_type);
    bool is_oauth_grant_type_Set() const;
    bool is_oauth_grant_type_Valid() const;

    QList<QString> getResourceSchemaSupport() const;
    void setResourceSchemaSupport(const QList<QString> &resource_schema_support);
    bool is_resource_schema_support_Set() const;
    bool is_resource_schema_support_Valid() const;

    QList<QString> getResourceSettingsSupport() const;
    void setResourceSettingsSupport(const QList<QString> &resource_settings_support);
    bool is_resource_settings_support_Set() const;
    bool is_resource_settings_support_Valid() const;

    QString getRevokeUrl() const;
    void setRevokeUrl(const QString &revoke_url);
    bool is_revoke_url_Set() const;
    bool is_revoke_url_Valid() const;

    bool isSchemaSupport() const;
    void setSchemaSupport(const bool &schema_support);
    bool is_schema_support_Set() const;
    bool is_schema_support_Valid() const;

    QString getServiceId() const;
    void setServiceId(const QString &service_id);
    bool is_service_id_Set() const;
    bool is_service_id_Valid() const;

    QMap<QString, QJsonValue> getSettings() const;
    void setSettings(const QMap<QString, QJsonValue> &settings);
    bool is_settings_Set() const;
    bool is_settings_Valid() const;

    QList<QString> getSettingsRequiredForAuthorization() const;
    void setSettingsRequiredForAuthorization(const QList<QString> &settings_required_for_authorization);
    bool is_settings_required_for_authorization_Set() const;
    bool is_settings_required_for_authorization_Valid() const;

    OAIConnectionState getState() const;
    void setState(const OAIConnectionState &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<OAIWebhookSubscription> getSubscriptions() const;
    void setSubscriptions(const QList<OAIWebhookSubscription> &subscriptions);
    bool is_subscriptions_Set() const;
    bool is_subscriptions_Valid() const;

    QString getTagLine() const;
    void setTagLine(const QString &tag_line);
    bool is_tag_line_Set() const;
    bool is_tag_line_Valid() const;

    QString getUnifiedApi() const;
    void setUnifiedApi(const QString &unified_api);
    bool is_unified_api_Set() const;
    bool is_unified_api_Valid() const;

    double getUpdatedAt() const;
    void setUpdatedAt(const double &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    bool isValidationSupport() const;
    void setValidationSupport(const bool &validation_support);
    bool is_validation_support_Set() const;
    bool is_validation_support_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAuthType m_auth_type;
    bool m_auth_type_isSet;
    bool m_auth_type_isValid;

    QString m_authorize_url;
    bool m_authorize_url_isSet;
    bool m_authorize_url_isValid;

    QList<QString> m_configurable_resources;
    bool m_configurable_resources_isSet;
    bool m_configurable_resources_isValid;

    QList<OAIConnection_configuration_inner> m_configuration;
    bool m_configuration_isSet;
    bool m_configuration_isValid;

    double m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QList<OAICustomMapping> m_custom_mappings;
    bool m_custom_mappings_isSet;
    bool m_custom_mappings_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QList<OAIFormField> m_form_fields;
    bool m_form_fields_isSet;
    bool m_form_fields_isValid;

    bool m_has_guide;
    bool m_has_guide_isSet;
    bool m_has_guide_isValid;

    QString m_icon;
    bool m_icon_isSet;
    bool m_icon_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIIntegrationState m_integration_state;
    bool m_integration_state_isSet;
    bool m_integration_state_isValid;

    QString m_logo;
    bool m_logo_isSet;
    bool m_logo_isValid;

    QMap<QString, QJsonValue> m_metadata;
    bool m_metadata_isSet;
    bool m_metadata_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIOAuthGrantType m_oauth_grant_type;
    bool m_oauth_grant_type_isSet;
    bool m_oauth_grant_type_isValid;

    QList<QString> m_resource_schema_support;
    bool m_resource_schema_support_isSet;
    bool m_resource_schema_support_isValid;

    QList<QString> m_resource_settings_support;
    bool m_resource_settings_support_isSet;
    bool m_resource_settings_support_isValid;

    QString m_revoke_url;
    bool m_revoke_url_isSet;
    bool m_revoke_url_isValid;

    bool m_schema_support;
    bool m_schema_support_isSet;
    bool m_schema_support_isValid;

    QString m_service_id;
    bool m_service_id_isSet;
    bool m_service_id_isValid;

    QMap<QString, QJsonValue> m_settings;
    bool m_settings_isSet;
    bool m_settings_isValid;

    QList<QString> m_settings_required_for_authorization;
    bool m_settings_required_for_authorization_isSet;
    bool m_settings_required_for_authorization_isValid;

    OAIConnectionState m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<OAIWebhookSubscription> m_subscriptions;
    bool m_subscriptions_isSet;
    bool m_subscriptions_isValid;

    QString m_tag_line;
    bool m_tag_line_isSet;
    bool m_tag_line_isValid;

    QString m_unified_api;
    bool m_unified_api_isSet;
    bool m_unified_api_isValid;

    double m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    bool m_validation_support;
    bool m_validation_support_isSet;
    bool m_validation_support_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConnection)

#endif // OAIConnection_H
