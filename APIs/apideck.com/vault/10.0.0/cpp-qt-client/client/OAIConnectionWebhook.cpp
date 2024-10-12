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

#include "OAIConnectionWebhook.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConnectionWebhook::OAIConnectionWebhook(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConnectionWebhook::OAIConnectionWebhook() {
    this->initializeModel();
}

OAIConnectionWebhook::~OAIConnectionWebhook() {}

void OAIConnectionWebhook::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_delivery_url_isSet = false;
    m_delivery_url_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_disabled_reason_isSet = false;
    m_disabled_reason_isValid = false;

    m_events_isSet = false;
    m_events_isValid = false;

    m_execute_base_url_isSet = false;
    m_execute_base_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_unified_api_isSet = false;
    m_unified_api_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIConnectionWebhook::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConnectionWebhook::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_delivery_url_isValid = ::OpenAPI::fromJsonValue(m_delivery_url, json[QString("delivery_url")]);
    m_delivery_url_isSet = !json[QString("delivery_url")].isNull() && m_delivery_url_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_disabled_reason_isValid = ::OpenAPI::fromJsonValue(m_disabled_reason, json[QString("disabled_reason")]);
    m_disabled_reason_isSet = !json[QString("disabled_reason")].isNull() && m_disabled_reason_isValid;

    m_events_isValid = ::OpenAPI::fromJsonValue(m_events, json[QString("events")]);
    m_events_isSet = !json[QString("events")].isNull() && m_events_isValid;

    m_execute_base_url_isValid = ::OpenAPI::fromJsonValue(m_execute_base_url, json[QString("execute_base_url")]);
    m_execute_base_url_isSet = !json[QString("execute_base_url")].isNull() && m_execute_base_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_unified_api_isValid = ::OpenAPI::fromJsonValue(m_unified_api, json[QString("unified_api")]);
    m_unified_api_isSet = !json[QString("unified_api")].isNull() && m_unified_api_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIConnectionWebhook::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConnectionWebhook::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_delivery_url_isSet) {
        obj.insert(QString("delivery_url"), ::OpenAPI::toJsonValue(m_delivery_url));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_disabled_reason_isSet) {
        obj.insert(QString("disabled_reason"), ::OpenAPI::toJsonValue(m_disabled_reason));
    }
    if (m_events.size() > 0) {
        obj.insert(QString("events"), ::OpenAPI::toJsonValue(m_events));
    }
    if (m_execute_base_url_isSet) {
        obj.insert(QString("execute_base_url"), ::OpenAPI::toJsonValue(m_execute_base_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_unified_api.isSet()) {
        obj.insert(QString("unified_api"), ::OpenAPI::toJsonValue(m_unified_api));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QDateTime OAIConnectionWebhook::getCreatedAt() const {
    return m_created_at;
}
void OAIConnectionWebhook::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIConnectionWebhook::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIConnectionWebhook::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIConnectionWebhook::getDeliveryUrl() const {
    return m_delivery_url;
}
void OAIConnectionWebhook::setDeliveryUrl(const QString &delivery_url) {
    m_delivery_url = delivery_url;
    m_delivery_url_isSet = true;
}

bool OAIConnectionWebhook::is_delivery_url_Set() const{
    return m_delivery_url_isSet;
}

bool OAIConnectionWebhook::is_delivery_url_Valid() const{
    return m_delivery_url_isValid;
}

QString OAIConnectionWebhook::getDescription() const {
    return m_description;
}
void OAIConnectionWebhook::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIConnectionWebhook::is_description_Set() const{
    return m_description_isSet;
}

bool OAIConnectionWebhook::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIConnectionWebhook::getDisabledReason() const {
    return m_disabled_reason;
}
void OAIConnectionWebhook::setDisabledReason(const QString &disabled_reason) {
    m_disabled_reason = disabled_reason;
    m_disabled_reason_isSet = true;
}

bool OAIConnectionWebhook::is_disabled_reason_Set() const{
    return m_disabled_reason_isSet;
}

bool OAIConnectionWebhook::is_disabled_reason_Valid() const{
    return m_disabled_reason_isValid;
}

QList<QString> OAIConnectionWebhook::getEvents() const {
    return m_events;
}
void OAIConnectionWebhook::setEvents(const QList<QString> &events) {
    m_events = events;
    m_events_isSet = true;
}

bool OAIConnectionWebhook::is_events_Set() const{
    return m_events_isSet;
}

bool OAIConnectionWebhook::is_events_Valid() const{
    return m_events_isValid;
}

QString OAIConnectionWebhook::getExecuteBaseUrl() const {
    return m_execute_base_url;
}
void OAIConnectionWebhook::setExecuteBaseUrl(const QString &execute_base_url) {
    m_execute_base_url = execute_base_url;
    m_execute_base_url_isSet = true;
}

bool OAIConnectionWebhook::is_execute_base_url_Set() const{
    return m_execute_base_url_isSet;
}

bool OAIConnectionWebhook::is_execute_base_url_Valid() const{
    return m_execute_base_url_isValid;
}

QString OAIConnectionWebhook::getId() const {
    return m_id;
}
void OAIConnectionWebhook::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIConnectionWebhook::is_id_Set() const{
    return m_id_isSet;
}

bool OAIConnectionWebhook::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIConnectionWebhook::getStatus() const {
    return m_status;
}
void OAIConnectionWebhook::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIConnectionWebhook::is_status_Set() const{
    return m_status_isSet;
}

bool OAIConnectionWebhook::is_status_Valid() const{
    return m_status_isValid;
}

OAIUnifiedApiId OAIConnectionWebhook::getUnifiedApi() const {
    return m_unified_api;
}
void OAIConnectionWebhook::setUnifiedApi(const OAIUnifiedApiId &unified_api) {
    m_unified_api = unified_api;
    m_unified_api_isSet = true;
}

bool OAIConnectionWebhook::is_unified_api_Set() const{
    return m_unified_api_isSet;
}

bool OAIConnectionWebhook::is_unified_api_Valid() const{
    return m_unified_api_isValid;
}

QDateTime OAIConnectionWebhook::getUpdatedAt() const {
    return m_updated_at;
}
void OAIConnectionWebhook::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIConnectionWebhook::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIConnectionWebhook::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIConnectionWebhook::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_disabled_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_events.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_execute_base_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unified_api.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConnectionWebhook::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_delivery_url_isValid && m_events_isValid && m_execute_base_url_isValid && m_status_isValid && m_unified_api_isValid && true;
}

} // namespace OpenAPI
