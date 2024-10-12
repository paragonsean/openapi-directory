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

#include "OAIConsumerRequestCountsInDateRangeResponse_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsumerRequestCountsInDateRangeResponse_data::OAIConsumerRequestCountsInDateRangeResponse_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsumerRequestCountsInDateRangeResponse_data::OAIConsumerRequestCountsInDateRangeResponse_data() {
    this->initializeModel();
}

OAIConsumerRequestCountsInDateRangeResponse_data::~OAIConsumerRequestCountsInDateRangeResponse_data() {}

void OAIConsumerRequestCountsInDateRangeResponse_data::initializeModel() {

    m_aggregated_request_count_isSet = false;
    m_aggregated_request_count_isValid = false;

    m_application_id_isSet = false;
    m_application_id_isValid = false;

    m_consumer_id_isSet = false;
    m_consumer_id_isValid = false;

    m_end_datetime_isSet = false;
    m_end_datetime_isValid = false;

    m_request_counts_isSet = false;
    m_request_counts_isValid = false;

    m_start_datetime_isSet = false;
    m_start_datetime_isValid = false;
}

void OAIConsumerRequestCountsInDateRangeResponse_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsumerRequestCountsInDateRangeResponse_data::fromJsonObject(QJsonObject json) {

    m_aggregated_request_count_isValid = ::OpenAPI::fromJsonValue(m_aggregated_request_count, json[QString("aggregated_request_count")]);
    m_aggregated_request_count_isSet = !json[QString("aggregated_request_count")].isNull() && m_aggregated_request_count_isValid;

    m_application_id_isValid = ::OpenAPI::fromJsonValue(m_application_id, json[QString("application_id")]);
    m_application_id_isSet = !json[QString("application_id")].isNull() && m_application_id_isValid;

    m_consumer_id_isValid = ::OpenAPI::fromJsonValue(m_consumer_id, json[QString("consumer_id")]);
    m_consumer_id_isSet = !json[QString("consumer_id")].isNull() && m_consumer_id_isValid;

    m_end_datetime_isValid = ::OpenAPI::fromJsonValue(m_end_datetime, json[QString("end_datetime")]);
    m_end_datetime_isSet = !json[QString("end_datetime")].isNull() && m_end_datetime_isValid;

    m_request_counts_isValid = ::OpenAPI::fromJsonValue(m_request_counts, json[QString("request_counts")]);
    m_request_counts_isSet = !json[QString("request_counts")].isNull() && m_request_counts_isValid;

    m_start_datetime_isValid = ::OpenAPI::fromJsonValue(m_start_datetime, json[QString("start_datetime")]);
    m_start_datetime_isSet = !json[QString("start_datetime")].isNull() && m_start_datetime_isValid;
}

QString OAIConsumerRequestCountsInDateRangeResponse_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsumerRequestCountsInDateRangeResponse_data::asJsonObject() const {
    QJsonObject obj;
    if (m_aggregated_request_count_isSet) {
        obj.insert(QString("aggregated_request_count"), ::OpenAPI::toJsonValue(m_aggregated_request_count));
    }
    if (m_application_id_isSet) {
        obj.insert(QString("application_id"), ::OpenAPI::toJsonValue(m_application_id));
    }
    if (m_consumer_id_isSet) {
        obj.insert(QString("consumer_id"), ::OpenAPI::toJsonValue(m_consumer_id));
    }
    if (m_end_datetime_isSet) {
        obj.insert(QString("end_datetime"), ::OpenAPI::toJsonValue(m_end_datetime));
    }
    if (m_request_counts.isSet()) {
        obj.insert(QString("request_counts"), ::OpenAPI::toJsonValue(m_request_counts));
    }
    if (m_start_datetime_isSet) {
        obj.insert(QString("start_datetime"), ::OpenAPI::toJsonValue(m_start_datetime));
    }
    return obj;
}

double OAIConsumerRequestCountsInDateRangeResponse_data::getAggregatedRequestCount() const {
    return m_aggregated_request_count;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setAggregatedRequestCount(const double &aggregated_request_count) {
    m_aggregated_request_count = aggregated_request_count;
    m_aggregated_request_count_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_aggregated_request_count_Set() const{
    return m_aggregated_request_count_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_aggregated_request_count_Valid() const{
    return m_aggregated_request_count_isValid;
}

QString OAIConsumerRequestCountsInDateRangeResponse_data::getApplicationId() const {
    return m_application_id;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setApplicationId(const QString &application_id) {
    m_application_id = application_id;
    m_application_id_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_application_id_Set() const{
    return m_application_id_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_application_id_Valid() const{
    return m_application_id_isValid;
}

QString OAIConsumerRequestCountsInDateRangeResponse_data::getConsumerId() const {
    return m_consumer_id;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setConsumerId(const QString &consumer_id) {
    m_consumer_id = consumer_id;
    m_consumer_id_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_consumer_id_Set() const{
    return m_consumer_id_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_consumer_id_Valid() const{
    return m_consumer_id_isValid;
}

QString OAIConsumerRequestCountsInDateRangeResponse_data::getEndDatetime() const {
    return m_end_datetime;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setEndDatetime(const QString &end_datetime) {
    m_end_datetime = end_datetime;
    m_end_datetime_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_end_datetime_Set() const{
    return m_end_datetime_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_end_datetime_Valid() const{
    return m_end_datetime_isValid;
}

OAIRequestCountAllocation OAIConsumerRequestCountsInDateRangeResponse_data::getRequestCounts() const {
    return m_request_counts;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setRequestCounts(const OAIRequestCountAllocation &request_counts) {
    m_request_counts = request_counts;
    m_request_counts_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_request_counts_Set() const{
    return m_request_counts_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_request_counts_Valid() const{
    return m_request_counts_isValid;
}

QString OAIConsumerRequestCountsInDateRangeResponse_data::getStartDatetime() const {
    return m_start_datetime;
}
void OAIConsumerRequestCountsInDateRangeResponse_data::setStartDatetime(const QString &start_datetime) {
    m_start_datetime = start_datetime;
    m_start_datetime_isSet = true;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_start_datetime_Set() const{
    return m_start_datetime_isSet;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::is_start_datetime_Valid() const{
    return m_start_datetime_isValid;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_aggregated_request_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_application_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_consumer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_counts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConsumerRequestCountsInDateRangeResponse_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
