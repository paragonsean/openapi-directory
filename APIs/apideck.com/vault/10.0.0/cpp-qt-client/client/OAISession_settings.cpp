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

#include "OAISession_settings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISession_settings::OAISession_settings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISession_settings::OAISession_settings() {
    this->initializeModel();
}

OAISession_settings::~OAISession_settings() {}

void OAISession_settings::initializeModel() {

    m_allow_actions_isSet = false;
    m_allow_actions_isValid = false;

    m_auto_redirect_isSet = false;
    m_auto_redirect_isValid = false;

    m_hide_guides_isSet = false;
    m_hide_guides_isValid = false;

    m_hide_resource_settings_isSet = false;
    m_hide_resource_settings_isValid = false;

    m_isolation_mode_isSet = false;
    m_isolation_mode_isValid = false;

    m_sandbox_mode_isSet = false;
    m_sandbox_mode_isValid = false;

    m_session_length_isSet = false;
    m_session_length_isValid = false;

    m_show_logs_isSet = false;
    m_show_logs_isValid = false;

    m_show_sidebar_isSet = false;
    m_show_sidebar_isValid = false;

    m_show_suggestions_isSet = false;
    m_show_suggestions_isValid = false;

    m_unified_apis_isSet = false;
    m_unified_apis_isValid = false;
}

void OAISession_settings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISession_settings::fromJsonObject(QJsonObject json) {

    m_allow_actions_isValid = ::OpenAPI::fromJsonValue(m_allow_actions, json[QString("allow_actions")]);
    m_allow_actions_isSet = !json[QString("allow_actions")].isNull() && m_allow_actions_isValid;

    m_auto_redirect_isValid = ::OpenAPI::fromJsonValue(m_auto_redirect, json[QString("auto_redirect")]);
    m_auto_redirect_isSet = !json[QString("auto_redirect")].isNull() && m_auto_redirect_isValid;

    m_hide_guides_isValid = ::OpenAPI::fromJsonValue(m_hide_guides, json[QString("hide_guides")]);
    m_hide_guides_isSet = !json[QString("hide_guides")].isNull() && m_hide_guides_isValid;

    m_hide_resource_settings_isValid = ::OpenAPI::fromJsonValue(m_hide_resource_settings, json[QString("hide_resource_settings")]);
    m_hide_resource_settings_isSet = !json[QString("hide_resource_settings")].isNull() && m_hide_resource_settings_isValid;

    m_isolation_mode_isValid = ::OpenAPI::fromJsonValue(m_isolation_mode, json[QString("isolation_mode")]);
    m_isolation_mode_isSet = !json[QString("isolation_mode")].isNull() && m_isolation_mode_isValid;

    m_sandbox_mode_isValid = ::OpenAPI::fromJsonValue(m_sandbox_mode, json[QString("sandbox_mode")]);
    m_sandbox_mode_isSet = !json[QString("sandbox_mode")].isNull() && m_sandbox_mode_isValid;

    m_session_length_isValid = ::OpenAPI::fromJsonValue(m_session_length, json[QString("session_length")]);
    m_session_length_isSet = !json[QString("session_length")].isNull() && m_session_length_isValid;

    m_show_logs_isValid = ::OpenAPI::fromJsonValue(m_show_logs, json[QString("show_logs")]);
    m_show_logs_isSet = !json[QString("show_logs")].isNull() && m_show_logs_isValid;

    m_show_sidebar_isValid = ::OpenAPI::fromJsonValue(m_show_sidebar, json[QString("show_sidebar")]);
    m_show_sidebar_isSet = !json[QString("show_sidebar")].isNull() && m_show_sidebar_isValid;

    m_show_suggestions_isValid = ::OpenAPI::fromJsonValue(m_show_suggestions, json[QString("show_suggestions")]);
    m_show_suggestions_isSet = !json[QString("show_suggestions")].isNull() && m_show_suggestions_isValid;

    m_unified_apis_isValid = ::OpenAPI::fromJsonValue(m_unified_apis, json[QString("unified_apis")]);
    m_unified_apis_isSet = !json[QString("unified_apis")].isNull() && m_unified_apis_isValid;
}

QString OAISession_settings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISession_settings::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_actions.size() > 0) {
        obj.insert(QString("allow_actions"), ::OpenAPI::toJsonValue(m_allow_actions));
    }
    if (m_auto_redirect_isSet) {
        obj.insert(QString("auto_redirect"), ::OpenAPI::toJsonValue(m_auto_redirect));
    }
    if (m_hide_guides_isSet) {
        obj.insert(QString("hide_guides"), ::OpenAPI::toJsonValue(m_hide_guides));
    }
    if (m_hide_resource_settings_isSet) {
        obj.insert(QString("hide_resource_settings"), ::OpenAPI::toJsonValue(m_hide_resource_settings));
    }
    if (m_isolation_mode_isSet) {
        obj.insert(QString("isolation_mode"), ::OpenAPI::toJsonValue(m_isolation_mode));
    }
    if (m_sandbox_mode_isSet) {
        obj.insert(QString("sandbox_mode"), ::OpenAPI::toJsonValue(m_sandbox_mode));
    }
    if (m_session_length_isSet) {
        obj.insert(QString("session_length"), ::OpenAPI::toJsonValue(m_session_length));
    }
    if (m_show_logs_isSet) {
        obj.insert(QString("show_logs"), ::OpenAPI::toJsonValue(m_show_logs));
    }
    if (m_show_sidebar_isSet) {
        obj.insert(QString("show_sidebar"), ::OpenAPI::toJsonValue(m_show_sidebar));
    }
    if (m_show_suggestions_isSet) {
        obj.insert(QString("show_suggestions"), ::OpenAPI::toJsonValue(m_show_suggestions));
    }
    if (m_unified_apis.size() > 0) {
        obj.insert(QString("unified_apis"), ::OpenAPI::toJsonValue(m_unified_apis));
    }
    return obj;
}

QList<QString> OAISession_settings::getAllowActions() const {
    return m_allow_actions;
}
void OAISession_settings::setAllowActions(const QList<QString> &allow_actions) {
    m_allow_actions = allow_actions;
    m_allow_actions_isSet = true;
}

bool OAISession_settings::is_allow_actions_Set() const{
    return m_allow_actions_isSet;
}

bool OAISession_settings::is_allow_actions_Valid() const{
    return m_allow_actions_isValid;
}

bool OAISession_settings::isAutoRedirect() const {
    return m_auto_redirect;
}
void OAISession_settings::setAutoRedirect(const bool &auto_redirect) {
    m_auto_redirect = auto_redirect;
    m_auto_redirect_isSet = true;
}

bool OAISession_settings::is_auto_redirect_Set() const{
    return m_auto_redirect_isSet;
}

bool OAISession_settings::is_auto_redirect_Valid() const{
    return m_auto_redirect_isValid;
}

bool OAISession_settings::isHideGuides() const {
    return m_hide_guides;
}
void OAISession_settings::setHideGuides(const bool &hide_guides) {
    m_hide_guides = hide_guides;
    m_hide_guides_isSet = true;
}

bool OAISession_settings::is_hide_guides_Set() const{
    return m_hide_guides_isSet;
}

bool OAISession_settings::is_hide_guides_Valid() const{
    return m_hide_guides_isValid;
}

bool OAISession_settings::isHideResourceSettings() const {
    return m_hide_resource_settings;
}
void OAISession_settings::setHideResourceSettings(const bool &hide_resource_settings) {
    m_hide_resource_settings = hide_resource_settings;
    m_hide_resource_settings_isSet = true;
}

bool OAISession_settings::is_hide_resource_settings_Set() const{
    return m_hide_resource_settings_isSet;
}

bool OAISession_settings::is_hide_resource_settings_Valid() const{
    return m_hide_resource_settings_isValid;
}

bool OAISession_settings::isIsolationMode() const {
    return m_isolation_mode;
}
void OAISession_settings::setIsolationMode(const bool &isolation_mode) {
    m_isolation_mode = isolation_mode;
    m_isolation_mode_isSet = true;
}

bool OAISession_settings::is_isolation_mode_Set() const{
    return m_isolation_mode_isSet;
}

bool OAISession_settings::is_isolation_mode_Valid() const{
    return m_isolation_mode_isValid;
}

bool OAISession_settings::isSandboxMode() const {
    return m_sandbox_mode;
}
void OAISession_settings::setSandboxMode(const bool &sandbox_mode) {
    m_sandbox_mode = sandbox_mode;
    m_sandbox_mode_isSet = true;
}

bool OAISession_settings::is_sandbox_mode_Set() const{
    return m_sandbox_mode_isSet;
}

bool OAISession_settings::is_sandbox_mode_Valid() const{
    return m_sandbox_mode_isValid;
}

QString OAISession_settings::getSessionLength() const {
    return m_session_length;
}
void OAISession_settings::setSessionLength(const QString &session_length) {
    m_session_length = session_length;
    m_session_length_isSet = true;
}

bool OAISession_settings::is_session_length_Set() const{
    return m_session_length_isSet;
}

bool OAISession_settings::is_session_length_Valid() const{
    return m_session_length_isValid;
}

bool OAISession_settings::isShowLogs() const {
    return m_show_logs;
}
void OAISession_settings::setShowLogs(const bool &show_logs) {
    m_show_logs = show_logs;
    m_show_logs_isSet = true;
}

bool OAISession_settings::is_show_logs_Set() const{
    return m_show_logs_isSet;
}

bool OAISession_settings::is_show_logs_Valid() const{
    return m_show_logs_isValid;
}

bool OAISession_settings::isShowSidebar() const {
    return m_show_sidebar;
}
void OAISession_settings::setShowSidebar(const bool &show_sidebar) {
    m_show_sidebar = show_sidebar;
    m_show_sidebar_isSet = true;
}

bool OAISession_settings::is_show_sidebar_Set() const{
    return m_show_sidebar_isSet;
}

bool OAISession_settings::is_show_sidebar_Valid() const{
    return m_show_sidebar_isValid;
}

bool OAISession_settings::isShowSuggestions() const {
    return m_show_suggestions;
}
void OAISession_settings::setShowSuggestions(const bool &show_suggestions) {
    m_show_suggestions = show_suggestions;
    m_show_suggestions_isSet = true;
}

bool OAISession_settings::is_show_suggestions_Set() const{
    return m_show_suggestions_isSet;
}

bool OAISession_settings::is_show_suggestions_Valid() const{
    return m_show_suggestions_isValid;
}

QList<OAIUnifiedApiId> OAISession_settings::getUnifiedApis() const {
    return m_unified_apis;
}
void OAISession_settings::setUnifiedApis(const QList<OAIUnifiedApiId> &unified_apis) {
    m_unified_apis = unified_apis;
    m_unified_apis_isSet = true;
}

bool OAISession_settings::is_unified_apis_Set() const{
    return m_unified_apis_isSet;
}

bool OAISession_settings::is_unified_apis_Valid() const{
    return m_unified_apis_isValid;
}

bool OAISession_settings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_actions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_redirect_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hide_guides_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hide_resource_settings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_isolation_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sandbox_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_session_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_logs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_sidebar_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_suggestions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unified_apis.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISession_settings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
