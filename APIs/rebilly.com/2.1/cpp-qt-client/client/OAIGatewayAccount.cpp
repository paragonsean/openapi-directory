/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGatewayAccount.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGatewayAccount::OAIGatewayAccount(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGatewayAccount::OAIGatewayAccount() {
    this->initializeModel();
}

OAIGatewayAccount::~OAIGatewayAccount() {}

void OAIGatewayAccount::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_accepted_currencies_isSet = false;
    m_accepted_currencies_isValid = false;

    m_acquirer_name_isSet = false;
    m_acquirer_name_isValid = false;

    m_additional_filters_isSet = false;
    m_additional_filters_isValid = false;

    m_approval_window_ttl_isSet = false;
    m_approval_window_ttl_isValid = false;

    m_city_field_isSet = false;
    m_city_field_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_dcc_force_currency_isSet = false;
    m_dcc_force_currency_isValid = false;

    m_dcc_markup_isSet = false;
    m_dcc_markup_isValid = false;

    m_descriptor_isSet = false;
    m_descriptor_isValid = false;

    m_digital_wallets_isSet = false;
    m_digital_wallets_isValid = false;

    m_dynamic_descriptor_isSet = false;
    m_dynamic_descriptor_isValid = false;

    m_excluded_dcc_quote_currencies_isSet = false;
    m_excluded_dcc_quote_currencies_isValid = false;

    m_gateway_name_isSet = false;
    m_gateway_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_down_isSet = false;
    m_is_down_isValid = false;

    m_merchant_category_code_isSet = false;
    m_merchant_category_code_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_monthly_limit_isSet = false;
    m_monthly_limit_isValid = false;

    m_organization_id_isSet = false;
    m_organization_id_isValid = false;

    m_payment_card_schemes_isSet = false;
    m_payment_card_schemes_isValid = false;

    m_reconciliation_window_enabled_isSet = false;
    m_reconciliation_window_enabled_isValid = false;

    m_reconciliation_window_ttl_isSet = false;
    m_reconciliation_window_ttl_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_sticky_isSet = false;
    m_sticky_isValid = false;

    m_three_d_secure_isSet = false;
    m_three_d_secure_isValid = false;

    m_timeout_isSet = false;
    m_timeout_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIGatewayAccount::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGatewayAccount::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_accepted_currencies_isValid = ::OpenAPI::fromJsonValue(m_accepted_currencies, json[QString("acceptedCurrencies")]);
    m_accepted_currencies_isSet = !json[QString("acceptedCurrencies")].isNull() && m_accepted_currencies_isValid;

    m_acquirer_name_isValid = ::OpenAPI::fromJsonValue(m_acquirer_name, json[QString("acquirerName")]);
    m_acquirer_name_isSet = !json[QString("acquirerName")].isNull() && m_acquirer_name_isValid;

    m_additional_filters_isValid = ::OpenAPI::fromJsonValue(m_additional_filters, json[QString("additionalFilters")]);
    m_additional_filters_isSet = !json[QString("additionalFilters")].isNull() && m_additional_filters_isValid;

    m_approval_window_ttl_isValid = ::OpenAPI::fromJsonValue(m_approval_window_ttl, json[QString("approvalWindowTtl")]);
    m_approval_window_ttl_isSet = !json[QString("approvalWindowTtl")].isNull() && m_approval_window_ttl_isValid;

    m_city_field_isValid = ::OpenAPI::fromJsonValue(m_city_field, json[QString("cityField")]);
    m_city_field_isSet = !json[QString("cityField")].isNull() && m_city_field_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_dcc_force_currency_isValid = ::OpenAPI::fromJsonValue(m_dcc_force_currency, json[QString("dccForceCurrency")]);
    m_dcc_force_currency_isSet = !json[QString("dccForceCurrency")].isNull() && m_dcc_force_currency_isValid;

    m_dcc_markup_isValid = ::OpenAPI::fromJsonValue(m_dcc_markup, json[QString("dccMarkup")]);
    m_dcc_markup_isSet = !json[QString("dccMarkup")].isNull() && m_dcc_markup_isValid;

    m_descriptor_isValid = ::OpenAPI::fromJsonValue(m_descriptor, json[QString("descriptor")]);
    m_descriptor_isSet = !json[QString("descriptor")].isNull() && m_descriptor_isValid;

    m_digital_wallets_isValid = ::OpenAPI::fromJsonValue(m_digital_wallets, json[QString("digitalWallets")]);
    m_digital_wallets_isSet = !json[QString("digitalWallets")].isNull() && m_digital_wallets_isValid;

    m_dynamic_descriptor_isValid = ::OpenAPI::fromJsonValue(m_dynamic_descriptor, json[QString("dynamicDescriptor")]);
    m_dynamic_descriptor_isSet = !json[QString("dynamicDescriptor")].isNull() && m_dynamic_descriptor_isValid;

    m_excluded_dcc_quote_currencies_isValid = ::OpenAPI::fromJsonValue(m_excluded_dcc_quote_currencies, json[QString("excludedDccQuoteCurrencies")]);
    m_excluded_dcc_quote_currencies_isSet = !json[QString("excludedDccQuoteCurrencies")].isNull() && m_excluded_dcc_quote_currencies_isValid;

    m_gateway_name_isValid = ::OpenAPI::fromJsonValue(m_gateway_name, json[QString("gatewayName")]);
    m_gateway_name_isSet = !json[QString("gatewayName")].isNull() && m_gateway_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_down_isValid = ::OpenAPI::fromJsonValue(m_is_down, json[QString("isDown")]);
    m_is_down_isSet = !json[QString("isDown")].isNull() && m_is_down_isValid;

    m_merchant_category_code_isValid = ::OpenAPI::fromJsonValue(m_merchant_category_code, json[QString("merchantCategoryCode")]);
    m_merchant_category_code_isSet = !json[QString("merchantCategoryCode")].isNull() && m_merchant_category_code_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_monthly_limit_isValid = ::OpenAPI::fromJsonValue(m_monthly_limit, json[QString("monthlyLimit")]);
    m_monthly_limit_isSet = !json[QString("monthlyLimit")].isNull() && m_monthly_limit_isValid;

    m_organization_id_isValid = ::OpenAPI::fromJsonValue(m_organization_id, json[QString("organizationId")]);
    m_organization_id_isSet = !json[QString("organizationId")].isNull() && m_organization_id_isValid;

    m_payment_card_schemes_isValid = ::OpenAPI::fromJsonValue(m_payment_card_schemes, json[QString("paymentCardSchemes")]);
    m_payment_card_schemes_isSet = !json[QString("paymentCardSchemes")].isNull() && m_payment_card_schemes_isValid;

    m_reconciliation_window_enabled_isValid = ::OpenAPI::fromJsonValue(m_reconciliation_window_enabled, json[QString("reconciliationWindowEnabled")]);
    m_reconciliation_window_enabled_isSet = !json[QString("reconciliationWindowEnabled")].isNull() && m_reconciliation_window_enabled_isValid;

    m_reconciliation_window_ttl_isValid = ::OpenAPI::fromJsonValue(m_reconciliation_window_ttl, json[QString("reconciliationWindowTtl")]);
    m_reconciliation_window_ttl_isSet = !json[QString("reconciliationWindowTtl")].isNull() && m_reconciliation_window_ttl_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_sticky_isValid = ::OpenAPI::fromJsonValue(m_sticky, json[QString("sticky")]);
    m_sticky_isSet = !json[QString("sticky")].isNull() && m_sticky_isValid;

    m_three_d_secure_isValid = ::OpenAPI::fromJsonValue(m_three_d_secure, json[QString("threeDSecure")]);
    m_three_d_secure_isSet = !json[QString("threeDSecure")].isNull() && m_three_d_secure_isValid;

    m_timeout_isValid = ::OpenAPI::fromJsonValue(m_timeout, json[QString("timeout")]);
    m_timeout_isSet = !json[QString("timeout")].isNull() && m_timeout_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAIGatewayAccount::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGatewayAccount::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_accepted_currencies.size() > 0) {
        obj.insert(QString("acceptedCurrencies"), ::OpenAPI::toJsonValue(m_accepted_currencies));
    }
    if (m_acquirer_name.isSet()) {
        obj.insert(QString("acquirerName"), ::OpenAPI::toJsonValue(m_acquirer_name));
    }
    if (m_additional_filters_isSet) {
        obj.insert(QString("additionalFilters"), ::OpenAPI::toJsonValue(m_additional_filters));
    }
    if (m_approval_window_ttl_isSet) {
        obj.insert(QString("approvalWindowTtl"), ::OpenAPI::toJsonValue(m_approval_window_ttl));
    }
    if (m_city_field_isSet) {
        obj.insert(QString("cityField"), ::OpenAPI::toJsonValue(m_city_field));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_dcc_force_currency_isSet) {
        obj.insert(QString("dccForceCurrency"), ::OpenAPI::toJsonValue(m_dcc_force_currency));
    }
    if (m_dcc_markup_isSet) {
        obj.insert(QString("dccMarkup"), ::OpenAPI::toJsonValue(m_dcc_markup));
    }
    if (m_descriptor_isSet) {
        obj.insert(QString("descriptor"), ::OpenAPI::toJsonValue(m_descriptor));
    }
    if (m_digital_wallets.isSet()) {
        obj.insert(QString("digitalWallets"), ::OpenAPI::toJsonValue(m_digital_wallets));
    }
    if (m_dynamic_descriptor_isSet) {
        obj.insert(QString("dynamicDescriptor"), ::OpenAPI::toJsonValue(m_dynamic_descriptor));
    }
    if (m_excluded_dcc_quote_currencies.size() > 0) {
        obj.insert(QString("excludedDccQuoteCurrencies"), ::OpenAPI::toJsonValue(m_excluded_dcc_quote_currencies));
    }
    if (m_gateway_name.isSet()) {
        obj.insert(QString("gatewayName"), ::OpenAPI::toJsonValue(m_gateway_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_down_isSet) {
        obj.insert(QString("isDown"), ::OpenAPI::toJsonValue(m_is_down));
    }
    if (m_merchant_category_code_isSet) {
        obj.insert(QString("merchantCategoryCode"), ::OpenAPI::toJsonValue(m_merchant_category_code));
    }
    if (m_method.isSet()) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_monthly_limit_isSet) {
        obj.insert(QString("monthlyLimit"), ::OpenAPI::toJsonValue(m_monthly_limit));
    }
    if (m_organization_id_isSet) {
        obj.insert(QString("organizationId"), ::OpenAPI::toJsonValue(m_organization_id));
    }
    if (m_payment_card_schemes.size() > 0) {
        obj.insert(QString("paymentCardSchemes"), ::OpenAPI::toJsonValue(m_payment_card_schemes));
    }
    if (m_reconciliation_window_enabled_isSet) {
        obj.insert(QString("reconciliationWindowEnabled"), ::OpenAPI::toJsonValue(m_reconciliation_window_enabled));
    }
    if (m_reconciliation_window_ttl_isSet) {
        obj.insert(QString("reconciliationWindowTtl"), ::OpenAPI::toJsonValue(m_reconciliation_window_ttl));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_sticky_isSet) {
        obj.insert(QString("sticky"), ::OpenAPI::toJsonValue(m_sticky));
    }
    if (m_three_d_secure_isSet) {
        obj.insert(QString("threeDSecure"), ::OpenAPI::toJsonValue(m_three_d_secure));
    }
    if (m_timeout_isSet) {
        obj.insert(QString("timeout"), ::OpenAPI::toJsonValue(m_timeout));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QList<OAIGatewayAccount__links_inner> OAIGatewayAccount::getLinks() const {
    return m__links;
}
void OAIGatewayAccount::setLinks(const QList<OAIGatewayAccount__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIGatewayAccount::is__links_Set() const{
    return m__links_isSet;
}

bool OAIGatewayAccount::is__links_Valid() const{
    return m__links_isValid;
}

QList<QString> OAIGatewayAccount::getAcceptedCurrencies() const {
    return m_accepted_currencies;
}
void OAIGatewayAccount::setAcceptedCurrencies(const QList<QString> &accepted_currencies) {
    m_accepted_currencies = accepted_currencies;
    m_accepted_currencies_isSet = true;
}

bool OAIGatewayAccount::is_accepted_currencies_Set() const{
    return m_accepted_currencies_isSet;
}

bool OAIGatewayAccount::is_accepted_currencies_Valid() const{
    return m_accepted_currencies_isValid;
}

OAIAcquirerName OAIGatewayAccount::getAcquirerName() const {
    return m_acquirer_name;
}
void OAIGatewayAccount::setAcquirerName(const OAIAcquirerName &acquirer_name) {
    m_acquirer_name = acquirer_name;
    m_acquirer_name_isSet = true;
}

bool OAIGatewayAccount::is_acquirer_name_Set() const{
    return m_acquirer_name_isSet;
}

bool OAIGatewayAccount::is_acquirer_name_Valid() const{
    return m_acquirer_name_isValid;
}

QString OAIGatewayAccount::getAdditionalFilters() const {
    return m_additional_filters;
}
void OAIGatewayAccount::setAdditionalFilters(const QString &additional_filters) {
    m_additional_filters = additional_filters;
    m_additional_filters_isSet = true;
}

bool OAIGatewayAccount::is_additional_filters_Set() const{
    return m_additional_filters_isSet;
}

bool OAIGatewayAccount::is_additional_filters_Valid() const{
    return m_additional_filters_isValid;
}

qint32 OAIGatewayAccount::getApprovalWindowTtl() const {
    return m_approval_window_ttl;
}
void OAIGatewayAccount::setApprovalWindowTtl(const qint32 &approval_window_ttl) {
    m_approval_window_ttl = approval_window_ttl;
    m_approval_window_ttl_isSet = true;
}

bool OAIGatewayAccount::is_approval_window_ttl_Set() const{
    return m_approval_window_ttl_isSet;
}

bool OAIGatewayAccount::is_approval_window_ttl_Valid() const{
    return m_approval_window_ttl_isValid;
}

QString OAIGatewayAccount::getCityField() const {
    return m_city_field;
}
void OAIGatewayAccount::setCityField(const QString &city_field) {
    m_city_field = city_field;
    m_city_field_isSet = true;
}

bool OAIGatewayAccount::is_city_field_Set() const{
    return m_city_field_isSet;
}

bool OAIGatewayAccount::is_city_field_Valid() const{
    return m_city_field_isValid;
}

QDateTime OAIGatewayAccount::getCreatedTime() const {
    return m_created_time;
}
void OAIGatewayAccount::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIGatewayAccount::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIGatewayAccount::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIGatewayAccount::getDccForceCurrency() const {
    return m_dcc_force_currency;
}
void OAIGatewayAccount::setDccForceCurrency(const QString &dcc_force_currency) {
    m_dcc_force_currency = dcc_force_currency;
    m_dcc_force_currency_isSet = true;
}

bool OAIGatewayAccount::is_dcc_force_currency_Set() const{
    return m_dcc_force_currency_isSet;
}

bool OAIGatewayAccount::is_dcc_force_currency_Valid() const{
    return m_dcc_force_currency_isValid;
}

qint32 OAIGatewayAccount::getDccMarkup() const {
    return m_dcc_markup;
}
void OAIGatewayAccount::setDccMarkup(const qint32 &dcc_markup) {
    m_dcc_markup = dcc_markup;
    m_dcc_markup_isSet = true;
}

bool OAIGatewayAccount::is_dcc_markup_Set() const{
    return m_dcc_markup_isSet;
}

bool OAIGatewayAccount::is_dcc_markup_Valid() const{
    return m_dcc_markup_isValid;
}

QString OAIGatewayAccount::getDescriptor() const {
    return m_descriptor;
}
void OAIGatewayAccount::setDescriptor(const QString &descriptor) {
    m_descriptor = descriptor;
    m_descriptor_isSet = true;
}

bool OAIGatewayAccount::is_descriptor_Set() const{
    return m_descriptor_isSet;
}

bool OAIGatewayAccount::is_descriptor_Valid() const{
    return m_descriptor_isValid;
}

OAIDigitalWallets OAIGatewayAccount::getDigitalWallets() const {
    return m_digital_wallets;
}
void OAIGatewayAccount::setDigitalWallets(const OAIDigitalWallets &digital_wallets) {
    m_digital_wallets = digital_wallets;
    m_digital_wallets_isSet = true;
}

bool OAIGatewayAccount::is_digital_wallets_Set() const{
    return m_digital_wallets_isSet;
}

bool OAIGatewayAccount::is_digital_wallets_Valid() const{
    return m_digital_wallets_isValid;
}

bool OAIGatewayAccount::isDynamicDescriptor() const {
    return m_dynamic_descriptor;
}
void OAIGatewayAccount::setDynamicDescriptor(const bool &dynamic_descriptor) {
    m_dynamic_descriptor = dynamic_descriptor;
    m_dynamic_descriptor_isSet = true;
}

bool OAIGatewayAccount::is_dynamic_descriptor_Set() const{
    return m_dynamic_descriptor_isSet;
}

bool OAIGatewayAccount::is_dynamic_descriptor_Valid() const{
    return m_dynamic_descriptor_isValid;
}

QList<QString> OAIGatewayAccount::getExcludedDccQuoteCurrencies() const {
    return m_excluded_dcc_quote_currencies;
}
void OAIGatewayAccount::setExcludedDccQuoteCurrencies(const QList<QString> &excluded_dcc_quote_currencies) {
    m_excluded_dcc_quote_currencies = excluded_dcc_quote_currencies;
    m_excluded_dcc_quote_currencies_isSet = true;
}

bool OAIGatewayAccount::is_excluded_dcc_quote_currencies_Set() const{
    return m_excluded_dcc_quote_currencies_isSet;
}

bool OAIGatewayAccount::is_excluded_dcc_quote_currencies_Valid() const{
    return m_excluded_dcc_quote_currencies_isValid;
}

OAIGatewayName OAIGatewayAccount::getGatewayName() const {
    return m_gateway_name;
}
void OAIGatewayAccount::setGatewayName(const OAIGatewayName &gateway_name) {
    m_gateway_name = gateway_name;
    m_gateway_name_isSet = true;
}

bool OAIGatewayAccount::is_gateway_name_Set() const{
    return m_gateway_name_isSet;
}

bool OAIGatewayAccount::is_gateway_name_Valid() const{
    return m_gateway_name_isValid;
}

QString OAIGatewayAccount::getId() const {
    return m_id;
}
void OAIGatewayAccount::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGatewayAccount::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGatewayAccount::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIGatewayAccount::isIsDown() const {
    return m_is_down;
}
void OAIGatewayAccount::setIsDown(const bool &is_down) {
    m_is_down = is_down;
    m_is_down_isSet = true;
}

bool OAIGatewayAccount::is_is_down_Set() const{
    return m_is_down_isSet;
}

bool OAIGatewayAccount::is_is_down_Valid() const{
    return m_is_down_isValid;
}

QString OAIGatewayAccount::getMerchantCategoryCode() const {
    return m_merchant_category_code;
}
void OAIGatewayAccount::setMerchantCategoryCode(const QString &merchant_category_code) {
    m_merchant_category_code = merchant_category_code;
    m_merchant_category_code_isSet = true;
}

bool OAIGatewayAccount::is_merchant_category_code_Set() const{
    return m_merchant_category_code_isSet;
}

bool OAIGatewayAccount::is_merchant_category_code_Valid() const{
    return m_merchant_category_code_isValid;
}

OAIPaymentMethod OAIGatewayAccount::getMethod() const {
    return m_method;
}
void OAIGatewayAccount::setMethod(const OAIPaymentMethod &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIGatewayAccount::is_method_Set() const{
    return m_method_isSet;
}

bool OAIGatewayAccount::is_method_Valid() const{
    return m_method_isValid;
}

double OAIGatewayAccount::getMonthlyLimit() const {
    return m_monthly_limit;
}
void OAIGatewayAccount::setMonthlyLimit(const double &monthly_limit) {
    m_monthly_limit = monthly_limit;
    m_monthly_limit_isSet = true;
}

bool OAIGatewayAccount::is_monthly_limit_Set() const{
    return m_monthly_limit_isSet;
}

bool OAIGatewayAccount::is_monthly_limit_Valid() const{
    return m_monthly_limit_isValid;
}

QString OAIGatewayAccount::getOrganizationId() const {
    return m_organization_id;
}
void OAIGatewayAccount::setOrganizationId(const QString &organization_id) {
    m_organization_id = organization_id;
    m_organization_id_isSet = true;
}

bool OAIGatewayAccount::is_organization_id_Set() const{
    return m_organization_id_isSet;
}

bool OAIGatewayAccount::is_organization_id_Valid() const{
    return m_organization_id_isValid;
}

QList<OAIPaymentCardBrand> OAIGatewayAccount::getPaymentCardSchemes() const {
    return m_payment_card_schemes;
}
void OAIGatewayAccount::setPaymentCardSchemes(const QList<OAIPaymentCardBrand> &payment_card_schemes) {
    m_payment_card_schemes = payment_card_schemes;
    m_payment_card_schemes_isSet = true;
}

bool OAIGatewayAccount::is_payment_card_schemes_Set() const{
    return m_payment_card_schemes_isSet;
}

bool OAIGatewayAccount::is_payment_card_schemes_Valid() const{
    return m_payment_card_schemes_isValid;
}

bool OAIGatewayAccount::isReconciliationWindowEnabled() const {
    return m_reconciliation_window_enabled;
}
void OAIGatewayAccount::setReconciliationWindowEnabled(const bool &reconciliation_window_enabled) {
    m_reconciliation_window_enabled = reconciliation_window_enabled;
    m_reconciliation_window_enabled_isSet = true;
}

bool OAIGatewayAccount::is_reconciliation_window_enabled_Set() const{
    return m_reconciliation_window_enabled_isSet;
}

bool OAIGatewayAccount::is_reconciliation_window_enabled_Valid() const{
    return m_reconciliation_window_enabled_isValid;
}

qint32 OAIGatewayAccount::getReconciliationWindowTtl() const {
    return m_reconciliation_window_ttl;
}
void OAIGatewayAccount::setReconciliationWindowTtl(const qint32 &reconciliation_window_ttl) {
    m_reconciliation_window_ttl = reconciliation_window_ttl;
    m_reconciliation_window_ttl_isSet = true;
}

bool OAIGatewayAccount::is_reconciliation_window_ttl_Set() const{
    return m_reconciliation_window_ttl_isSet;
}

bool OAIGatewayAccount::is_reconciliation_window_ttl_Valid() const{
    return m_reconciliation_window_ttl_isValid;
}

QString OAIGatewayAccount::getStatus() const {
    return m_status;
}
void OAIGatewayAccount::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIGatewayAccount::is_status_Set() const{
    return m_status_isSet;
}

bool OAIGatewayAccount::is_status_Valid() const{
    return m_status_isValid;
}

bool OAIGatewayAccount::isSticky() const {
    return m_sticky;
}
void OAIGatewayAccount::setSticky(const bool &sticky) {
    m_sticky = sticky;
    m_sticky_isSet = true;
}

bool OAIGatewayAccount::is_sticky_Set() const{
    return m_sticky_isSet;
}

bool OAIGatewayAccount::is_sticky_Valid() const{
    return m_sticky_isValid;
}

bool OAIGatewayAccount::isThreeDSecure() const {
    return m_three_d_secure;
}
void OAIGatewayAccount::setThreeDSecure(const bool &three_d_secure) {
    m_three_d_secure = three_d_secure;
    m_three_d_secure_isSet = true;
}

bool OAIGatewayAccount::is_three_d_secure_Set() const{
    return m_three_d_secure_isSet;
}

bool OAIGatewayAccount::is_three_d_secure_Valid() const{
    return m_three_d_secure_isValid;
}

qint32 OAIGatewayAccount::getTimeout() const {
    return m_timeout;
}
void OAIGatewayAccount::setTimeout(const qint32 &timeout) {
    m_timeout = timeout;
    m_timeout_isSet = true;
}

bool OAIGatewayAccount::is_timeout_Set() const{
    return m_timeout_isSet;
}

bool OAIGatewayAccount::is_timeout_Valid() const{
    return m_timeout_isValid;
}

QString OAIGatewayAccount::getToken() const {
    return m_token;
}
void OAIGatewayAccount::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIGatewayAccount::is_token_Set() const{
    return m_token_isSet;
}

bool OAIGatewayAccount::is_token_Valid() const{
    return m_token_isValid;
}

QDateTime OAIGatewayAccount::getUpdatedTime() const {
    return m_updated_time;
}
void OAIGatewayAccount::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIGatewayAccount::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIGatewayAccount::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIGatewayAccount::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_accepted_currencies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_acquirer_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_filters_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_approval_window_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dcc_force_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dcc_markup_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_descriptor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_digital_wallets.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dynamic_descriptor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_excluded_dcc_quote_currencies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_down_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_category_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_method.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_monthly_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_organization_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_card_schemes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_reconciliation_window_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reconciliation_window_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sticky_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_three_d_secure_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGatewayAccount::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_accepted_currencies_isValid && m_gateway_name_isValid && m_method_isValid && true;
}

} // namespace OpenAPI
