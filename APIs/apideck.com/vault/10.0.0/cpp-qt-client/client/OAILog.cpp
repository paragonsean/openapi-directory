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

#include "OAILog.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILog::OAILog(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILog::OAILog() {
    this->initializeModel();
}

OAILog::~OAILog() {}

void OAILog::initializeModel() {

    m_api_style_isSet = false;
    m_api_style_isValid = false;

    m_base_url_isSet = false;
    m_base_url_isValid = false;

    m_child_request_isSet = false;
    m_child_request_isValid = false;

    m_consumer_id_isSet = false;
    m_consumer_id_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_error_message_isSet = false;
    m_error_message_isValid = false;

    m_execution_isSet = false;
    m_execution_isValid = false;

    m_has_children_isSet = false;
    m_has_children_isValid = false;

    m_http_method_isSet = false;
    m_http_method_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_latency_isSet = false;
    m_latency_isValid = false;

    m_operation_isSet = false;
    m_operation_isValid = false;

    m_parent_id_isSet = false;
    m_parent_id_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_sandbox_isSet = false;
    m_sandbox_isValid = false;

    m_service_isSet = false;
    m_service_isValid = false;

    m_source_ip_isSet = false;
    m_source_ip_isValid = false;

    m_status_code_isSet = false;
    m_status_code_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_unified_api_isSet = false;
    m_unified_api_isValid = false;
}

void OAILog::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILog::fromJsonObject(QJsonObject json) {

    m_api_style_isValid = ::OpenAPI::fromJsonValue(m_api_style, json[QString("api_style")]);
    m_api_style_isSet = !json[QString("api_style")].isNull() && m_api_style_isValid;

    m_base_url_isValid = ::OpenAPI::fromJsonValue(m_base_url, json[QString("base_url")]);
    m_base_url_isSet = !json[QString("base_url")].isNull() && m_base_url_isValid;

    m_child_request_isValid = ::OpenAPI::fromJsonValue(m_child_request, json[QString("child_request")]);
    m_child_request_isSet = !json[QString("child_request")].isNull() && m_child_request_isValid;

    m_consumer_id_isValid = ::OpenAPI::fromJsonValue(m_consumer_id, json[QString("consumer_id")]);
    m_consumer_id_isSet = !json[QString("consumer_id")].isNull() && m_consumer_id_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_error_message_isValid = ::OpenAPI::fromJsonValue(m_error_message, json[QString("error_message")]);
    m_error_message_isSet = !json[QString("error_message")].isNull() && m_error_message_isValid;

    m_execution_isValid = ::OpenAPI::fromJsonValue(m_execution, json[QString("execution")]);
    m_execution_isSet = !json[QString("execution")].isNull() && m_execution_isValid;

    m_has_children_isValid = ::OpenAPI::fromJsonValue(m_has_children, json[QString("has_children")]);
    m_has_children_isSet = !json[QString("has_children")].isNull() && m_has_children_isValid;

    m_http_method_isValid = ::OpenAPI::fromJsonValue(m_http_method, json[QString("http_method")]);
    m_http_method_isSet = !json[QString("http_method")].isNull() && m_http_method_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_latency_isValid = ::OpenAPI::fromJsonValue(m_latency, json[QString("latency")]);
    m_latency_isSet = !json[QString("latency")].isNull() && m_latency_isValid;

    m_operation_isValid = ::OpenAPI::fromJsonValue(m_operation, json[QString("operation")]);
    m_operation_isSet = !json[QString("operation")].isNull() && m_operation_isValid;

    m_parent_id_isValid = ::OpenAPI::fromJsonValue(m_parent_id, json[QString("parent_id")]);
    m_parent_id_isSet = !json[QString("parent_id")].isNull() && m_parent_id_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_sandbox_isValid = ::OpenAPI::fromJsonValue(m_sandbox, json[QString("sandbox")]);
    m_sandbox_isSet = !json[QString("sandbox")].isNull() && m_sandbox_isValid;

    m_service_isValid = ::OpenAPI::fromJsonValue(m_service, json[QString("service")]);
    m_service_isSet = !json[QString("service")].isNull() && m_service_isValid;

    m_source_ip_isValid = ::OpenAPI::fromJsonValue(m_source_ip, json[QString("source_ip")]);
    m_source_ip_isSet = !json[QString("source_ip")].isNull() && m_source_ip_isValid;

    m_status_code_isValid = ::OpenAPI::fromJsonValue(m_status_code, json[QString("status_code")]);
    m_status_code_isSet = !json[QString("status_code")].isNull() && m_status_code_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_unified_api_isValid = ::OpenAPI::fromJsonValue(m_unified_api, json[QString("unified_api")]);
    m_unified_api_isSet = !json[QString("unified_api")].isNull() && m_unified_api_isValid;
}

QString OAILog::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILog::asJsonObject() const {
    QJsonObject obj;
    if (m_api_style_isSet) {
        obj.insert(QString("api_style"), ::OpenAPI::toJsonValue(m_api_style));
    }
    if (m_base_url_isSet) {
        obj.insert(QString("base_url"), ::OpenAPI::toJsonValue(m_base_url));
    }
    if (m_child_request_isSet) {
        obj.insert(QString("child_request"), ::OpenAPI::toJsonValue(m_child_request));
    }
    if (m_consumer_id_isSet) {
        obj.insert(QString("consumer_id"), ::OpenAPI::toJsonValue(m_consumer_id));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_error_message_isSet) {
        obj.insert(QString("error_message"), ::OpenAPI::toJsonValue(m_error_message));
    }
    if (m_execution_isSet) {
        obj.insert(QString("execution"), ::OpenAPI::toJsonValue(m_execution));
    }
    if (m_has_children_isSet) {
        obj.insert(QString("has_children"), ::OpenAPI::toJsonValue(m_has_children));
    }
    if (m_http_method_isSet) {
        obj.insert(QString("http_method"), ::OpenAPI::toJsonValue(m_http_method));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_latency_isSet) {
        obj.insert(QString("latency"), ::OpenAPI::toJsonValue(m_latency));
    }
    if (m_operation.isSet()) {
        obj.insert(QString("operation"), ::OpenAPI::toJsonValue(m_operation));
    }
    if (m_parent_id_isSet) {
        obj.insert(QString("parent_id"), ::OpenAPI::toJsonValue(m_parent_id));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_sandbox_isSet) {
        obj.insert(QString("sandbox"), ::OpenAPI::toJsonValue(m_sandbox));
    }
    if (m_service.isSet()) {
        obj.insert(QString("service"), ::OpenAPI::toJsonValue(m_service));
    }
    if (m_source_ip_isSet) {
        obj.insert(QString("source_ip"), ::OpenAPI::toJsonValue(m_source_ip));
    }
    if (m_status_code_isSet) {
        obj.insert(QString("status_code"), ::OpenAPI::toJsonValue(m_status_code));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_unified_api_isSet) {
        obj.insert(QString("unified_api"), ::OpenAPI::toJsonValue(m_unified_api));
    }
    return obj;
}

QString OAILog::getApiStyle() const {
    return m_api_style;
}
void OAILog::setApiStyle(const QString &api_style) {
    m_api_style = api_style;
    m_api_style_isSet = true;
}

bool OAILog::is_api_style_Set() const{
    return m_api_style_isSet;
}

bool OAILog::is_api_style_Valid() const{
    return m_api_style_isValid;
}

QString OAILog::getBaseUrl() const {
    return m_base_url;
}
void OAILog::setBaseUrl(const QString &base_url) {
    m_base_url = base_url;
    m_base_url_isSet = true;
}

bool OAILog::is_base_url_Set() const{
    return m_base_url_isSet;
}

bool OAILog::is_base_url_Valid() const{
    return m_base_url_isValid;
}

bool OAILog::isChildRequest() const {
    return m_child_request;
}
void OAILog::setChildRequest(const bool &child_request) {
    m_child_request = child_request;
    m_child_request_isSet = true;
}

bool OAILog::is_child_request_Set() const{
    return m_child_request_isSet;
}

bool OAILog::is_child_request_Valid() const{
    return m_child_request_isValid;
}

QString OAILog::getConsumerId() const {
    return m_consumer_id;
}
void OAILog::setConsumerId(const QString &consumer_id) {
    m_consumer_id = consumer_id;
    m_consumer_id_isSet = true;
}

bool OAILog::is_consumer_id_Set() const{
    return m_consumer_id_isSet;
}

bool OAILog::is_consumer_id_Valid() const{
    return m_consumer_id_isValid;
}

double OAILog::getDuration() const {
    return m_duration;
}
void OAILog::setDuration(const double &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAILog::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAILog::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAILog::getErrorMessage() const {
    return m_error_message;
}
void OAILog::setErrorMessage(const QString &error_message) {
    m_error_message = error_message;
    m_error_message_isSet = true;
}

bool OAILog::is_error_message_Set() const{
    return m_error_message_isSet;
}

bool OAILog::is_error_message_Valid() const{
    return m_error_message_isValid;
}

qint32 OAILog::getExecution() const {
    return m_execution;
}
void OAILog::setExecution(const qint32 &execution) {
    m_execution = execution;
    m_execution_isSet = true;
}

bool OAILog::is_execution_Set() const{
    return m_execution_isSet;
}

bool OAILog::is_execution_Valid() const{
    return m_execution_isValid;
}

bool OAILog::isHasChildren() const {
    return m_has_children;
}
void OAILog::setHasChildren(const bool &has_children) {
    m_has_children = has_children;
    m_has_children_isSet = true;
}

bool OAILog::is_has_children_Set() const{
    return m_has_children_isSet;
}

bool OAILog::is_has_children_Valid() const{
    return m_has_children_isValid;
}

QString OAILog::getHttpMethod() const {
    return m_http_method;
}
void OAILog::setHttpMethod(const QString &http_method) {
    m_http_method = http_method;
    m_http_method_isSet = true;
}

bool OAILog::is_http_method_Set() const{
    return m_http_method_isSet;
}

bool OAILog::is_http_method_Valid() const{
    return m_http_method_isValid;
}

QString OAILog::getId() const {
    return m_id;
}
void OAILog::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAILog::is_id_Set() const{
    return m_id_isSet;
}

bool OAILog::is_id_Valid() const{
    return m_id_isValid;
}

double OAILog::getLatency() const {
    return m_latency;
}
void OAILog::setLatency(const double &latency) {
    m_latency = latency;
    m_latency_isSet = true;
}

bool OAILog::is_latency_Set() const{
    return m_latency_isSet;
}

bool OAILog::is_latency_Valid() const{
    return m_latency_isValid;
}

OAILog_operation OAILog::getOperation() const {
    return m_operation;
}
void OAILog::setOperation(const OAILog_operation &operation) {
    m_operation = operation;
    m_operation_isSet = true;
}

bool OAILog::is_operation_Set() const{
    return m_operation_isSet;
}

bool OAILog::is_operation_Valid() const{
    return m_operation_isValid;
}

QString OAILog::getParentId() const {
    return m_parent_id;
}
void OAILog::setParentId(const QString &parent_id) {
    m_parent_id = parent_id;
    m_parent_id_isSet = true;
}

bool OAILog::is_parent_id_Set() const{
    return m_parent_id_isSet;
}

bool OAILog::is_parent_id_Valid() const{
    return m_parent_id_isValid;
}

QString OAILog::getPath() const {
    return m_path;
}
void OAILog::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAILog::is_path_Set() const{
    return m_path_isSet;
}

bool OAILog::is_path_Valid() const{
    return m_path_isValid;
}

bool OAILog::isSandbox() const {
    return m_sandbox;
}
void OAILog::setSandbox(const bool &sandbox) {
    m_sandbox = sandbox;
    m_sandbox_isSet = true;
}

bool OAILog::is_sandbox_Set() const{
    return m_sandbox_isSet;
}

bool OAILog::is_sandbox_Valid() const{
    return m_sandbox_isValid;
}

OAILog_service OAILog::getService() const {
    return m_service;
}
void OAILog::setService(const OAILog_service &service) {
    m_service = service;
    m_service_isSet = true;
}

bool OAILog::is_service_Set() const{
    return m_service_isSet;
}

bool OAILog::is_service_Valid() const{
    return m_service_isValid;
}

QString OAILog::getSourceIp() const {
    return m_source_ip;
}
void OAILog::setSourceIp(const QString &source_ip) {
    m_source_ip = source_ip;
    m_source_ip_isSet = true;
}

bool OAILog::is_source_ip_Set() const{
    return m_source_ip_isSet;
}

bool OAILog::is_source_ip_Valid() const{
    return m_source_ip_isValid;
}

qint32 OAILog::getStatusCode() const {
    return m_status_code;
}
void OAILog::setStatusCode(const qint32 &status_code) {
    m_status_code = status_code;
    m_status_code_isSet = true;
}

bool OAILog::is_status_code_Set() const{
    return m_status_code_isSet;
}

bool OAILog::is_status_code_Valid() const{
    return m_status_code_isValid;
}

bool OAILog::isSuccess() const {
    return m_success;
}
void OAILog::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAILog::is_success_Set() const{
    return m_success_isSet;
}

bool OAILog::is_success_Valid() const{
    return m_success_isValid;
}

QString OAILog::getTimestamp() const {
    return m_timestamp;
}
void OAILog::setTimestamp(const QString &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAILog::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAILog::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

QString OAILog::getUnifiedApi() const {
    return m_unified_api;
}
void OAILog::setUnifiedApi(const QString &unified_api) {
    m_unified_api = unified_api;
    m_unified_api_isSet = true;
}

bool OAILog::is_unified_api_Set() const{
    return m_unified_api_isSet;
}

bool OAILog::is_unified_api_Valid() const{
    return m_unified_api_isValid;
}

bool OAILog::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_api_style_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_base_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_child_request_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_consumer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_children_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_http_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operation.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sandbox_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unified_api_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILog::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_api_style_isValid && m_base_url_isValid && m_child_request_isValid && m_consumer_id_isValid && m_duration_isValid && m_execution_isValid && m_has_children_isValid && m_http_method_isValid && m_id_isValid && m_latency_isValid && m_operation_isValid && m_parent_id_isValid && m_path_isValid && m_sandbox_isValid && m_service_isValid && m_status_code_isValid && m_success_isValid && m_timestamp_isValid && m_unified_api_isValid && true;
}

} // namespace OpenAPI
