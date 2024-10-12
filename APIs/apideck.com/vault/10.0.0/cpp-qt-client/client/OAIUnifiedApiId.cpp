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

#include "OAIUnifiedApiId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUnifiedApiId::OAIUnifiedApiId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUnifiedApiId::OAIUnifiedApiId() {
    this->initializeModel();
}

OAIUnifiedApiId::~OAIUnifiedApiId() {}

void OAIUnifiedApiId::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIUnifiedApiId::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIUnifiedApiId::fromJson(QString jsonString) {
    
    if ( jsonString.compare("accounting", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::ACCOUNTING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ats", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::ATS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("calendar", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::CALENDAR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("crm", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::CRM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("csp", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::CSP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("customer-support", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::CUSTOMER_SUPPORT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ecommerce", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::ECOMMERCE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("email", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::EMAIL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("email-marketing", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::EMAIL_MARKETING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("expense-management", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::EXPENSE_MANAGEMENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("file-storage", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::FILE_STORAGE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("form", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::FORM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hris", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::HRIS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lead", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::LEAD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("payroll", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::PAYROLL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("pos", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::POS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("procurement", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::PROCUREMENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("project-management", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::PROJECT_MANAGEMENT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("script", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::SCRIPT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sms", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::SMS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("spreadsheet", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::SPREADSHEET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("team-messaging", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::TEAM_MESSAGING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("issue-tracking", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::ISSUE_TRACKING;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("time-registration", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::TIME_REGISTRATION;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transactional-email", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::TRANSACTIONAL_EMAIL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("vault", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::VAULT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("data-warehouse", Qt::CaseInsensitive) == 0) {
        m_value = eOAIUnifiedApiId::DATA_WAREHOUSE;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIUnifiedApiId::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIUnifiedApiId::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIUnifiedApiId::ACCOUNTING:
            val = "accounting";
            break;
        case eOAIUnifiedApiId::ATS:
            val = "ats";
            break;
        case eOAIUnifiedApiId::CALENDAR:
            val = "calendar";
            break;
        case eOAIUnifiedApiId::CRM:
            val = "crm";
            break;
        case eOAIUnifiedApiId::CSP:
            val = "csp";
            break;
        case eOAIUnifiedApiId::CUSTOMER_SUPPORT:
            val = "customer-support";
            break;
        case eOAIUnifiedApiId::ECOMMERCE:
            val = "ecommerce";
            break;
        case eOAIUnifiedApiId::EMAIL:
            val = "email";
            break;
        case eOAIUnifiedApiId::EMAIL_MARKETING:
            val = "email-marketing";
            break;
        case eOAIUnifiedApiId::EXPENSE_MANAGEMENT:
            val = "expense-management";
            break;
        case eOAIUnifiedApiId::FILE_STORAGE:
            val = "file-storage";
            break;
        case eOAIUnifiedApiId::FORM:
            val = "form";
            break;
        case eOAIUnifiedApiId::HRIS:
            val = "hris";
            break;
        case eOAIUnifiedApiId::LEAD:
            val = "lead";
            break;
        case eOAIUnifiedApiId::PAYROLL:
            val = "payroll";
            break;
        case eOAIUnifiedApiId::POS:
            val = "pos";
            break;
        case eOAIUnifiedApiId::PROCUREMENT:
            val = "procurement";
            break;
        case eOAIUnifiedApiId::PROJECT_MANAGEMENT:
            val = "project-management";
            break;
        case eOAIUnifiedApiId::SCRIPT:
            val = "script";
            break;
        case eOAIUnifiedApiId::SMS:
            val = "sms";
            break;
        case eOAIUnifiedApiId::SPREADSHEET:
            val = "spreadsheet";
            break;
        case eOAIUnifiedApiId::TEAM_MESSAGING:
            val = "team-messaging";
            break;
        case eOAIUnifiedApiId::ISSUE_TRACKING:
            val = "issue-tracking";
            break;
        case eOAIUnifiedApiId::TIME_REGISTRATION:
            val = "time-registration";
            break;
        case eOAIUnifiedApiId::TRANSACTIONAL_EMAIL:
            val = "transactional-email";
            break;
        case eOAIUnifiedApiId::VAULT:
            val = "vault";
            break;
        case eOAIUnifiedApiId::DATA_WAREHOUSE:
            val = "data-warehouse";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIUnifiedApiId::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIUnifiedApiId::eOAIUnifiedApiId OAIUnifiedApiId::getValue() const {
    return m_value;
}

void OAIUnifiedApiId::setValue(const OAIUnifiedApiId::eOAIUnifiedApiId& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIUnifiedApiId::isSet() const {
    
    return m_value_isSet;
}

bool OAIUnifiedApiId::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
