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

#include "OAIPaymentInstrument_2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentInstrument_2::OAIPaymentInstrument_2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentInstrument_2::OAIPaymentInstrument_2() {
    this->initializeModel();
}

OAIPaymentInstrument_2::~OAIPaymentInstrument_2() {}

void OAIPaymentInstrument_2::initializeModel() {

    m_bank_country_isSet = false;
    m_bank_country_isValid = false;

    m_bank_name_isSet = false;
    m_bank_name_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_bin_isSet = false;
    m_bin_isValid = false;

    m_brand_isSet = false;
    m_brand_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_cvv_isSet = false;
    m_cvv_isValid = false;

    m_exp_month_isSet = false;
    m_exp_month_isValid = false;

    m_exp_year_isSet = false;
    m_exp_year_isValid = false;

    m_fingerprint_isSet = false;
    m_fingerprint_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last4_isSet = false;
    m_last4_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_pan_isSet = false;
    m_pan_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_expiration_reminder_number_isSet = false;
    m_expiration_reminder_number_isValid = false;

    m_expiration_reminder_time_isSet = false;
    m_expiration_reminder_time_isValid = false;

    m_sticky_gateway_account_id_isSet = false;
    m_sticky_gateway_account_id_isValid = false;

    m_account_number_type_isSet = false;
    m_account_number_type_isValid = false;

    m_account_type_isSet = false;
    m_account_type_isValid = false;

    m_bic_isSet = false;
    m_bic_isValid = false;

    m_routing_number_isSet = false;
    m_routing_number_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;
}

void OAIPaymentInstrument_2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentInstrument_2::fromJsonObject(QJsonObject json) {

    m_bank_country_isValid = ::OpenAPI::fromJsonValue(m_bank_country, json[QString("bankCountry")]);
    m_bank_country_isSet = !json[QString("bankCountry")].isNull() && m_bank_country_isValid;

    m_bank_name_isValid = ::OpenAPI::fromJsonValue(m_bank_name, json[QString("bankName")]);
    m_bank_name_isSet = !json[QString("bankName")].isNull() && m_bank_name_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_bin_isValid = ::OpenAPI::fromJsonValue(m_bin, json[QString("bin")]);
    m_bin_isSet = !json[QString("bin")].isNull() && m_bin_isValid;

    m_brand_isValid = ::OpenAPI::fromJsonValue(m_brand, json[QString("brand")]);
    m_brand_isSet = !json[QString("brand")].isNull() && m_brand_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_cvv_isValid = ::OpenAPI::fromJsonValue(m_cvv, json[QString("cvv")]);
    m_cvv_isSet = !json[QString("cvv")].isNull() && m_cvv_isValid;

    m_exp_month_isValid = ::OpenAPI::fromJsonValue(m_exp_month, json[QString("expMonth")]);
    m_exp_month_isSet = !json[QString("expMonth")].isNull() && m_exp_month_isValid;

    m_exp_year_isValid = ::OpenAPI::fromJsonValue(m_exp_year, json[QString("expYear")]);
    m_exp_year_isSet = !json[QString("expYear")].isNull() && m_exp_year_isValid;

    m_fingerprint_isValid = ::OpenAPI::fromJsonValue(m_fingerprint, json[QString("fingerprint")]);
    m_fingerprint_isSet = !json[QString("fingerprint")].isNull() && m_fingerprint_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last4_isValid = ::OpenAPI::fromJsonValue(m_last4, json[QString("last4")]);
    m_last4_isSet = !json[QString("last4")].isNull() && m_last4_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_pan_isValid = ::OpenAPI::fromJsonValue(m_pan, json[QString("pan")]);
    m_pan_isSet = !json[QString("pan")].isNull() && m_pan_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_expiration_reminder_number_isValid = ::OpenAPI::fromJsonValue(m_expiration_reminder_number, json[QString("expirationReminderNumber")]);
    m_expiration_reminder_number_isSet = !json[QString("expirationReminderNumber")].isNull() && m_expiration_reminder_number_isValid;

    m_expiration_reminder_time_isValid = ::OpenAPI::fromJsonValue(m_expiration_reminder_time, json[QString("expirationReminderTime")]);
    m_expiration_reminder_time_isSet = !json[QString("expirationReminderTime")].isNull() && m_expiration_reminder_time_isValid;

    m_sticky_gateway_account_id_isValid = ::OpenAPI::fromJsonValue(m_sticky_gateway_account_id, json[QString("stickyGatewayAccountId")]);
    m_sticky_gateway_account_id_isSet = !json[QString("stickyGatewayAccountId")].isNull() && m_sticky_gateway_account_id_isValid;

    m_account_number_type_isValid = ::OpenAPI::fromJsonValue(m_account_number_type, json[QString("accountNumberType")]);
    m_account_number_type_isSet = !json[QString("accountNumberType")].isNull() && m_account_number_type_isValid;

    m_account_type_isValid = ::OpenAPI::fromJsonValue(m_account_type, json[QString("accountType")]);
    m_account_type_isSet = !json[QString("accountType")].isNull() && m_account_type_isValid;

    m_bic_isValid = ::OpenAPI::fromJsonValue(m_bic, json[QString("bic")]);
    m_bic_isSet = !json[QString("bic")].isNull() && m_bic_isValid;

    m_routing_number_isValid = ::OpenAPI::fromJsonValue(m_routing_number, json[QString("routingNumber")]);
    m_routing_number_isSet = !json[QString("routingNumber")].isNull() && m_routing_number_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;
}

QString OAIPaymentInstrument_2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentInstrument_2::asJsonObject() const {
    QJsonObject obj;
    if (m_bank_country_isSet) {
        obj.insert(QString("bankCountry"), ::OpenAPI::toJsonValue(m_bank_country));
    }
    if (m_bank_name_isSet) {
        obj.insert(QString("bankName"), ::OpenAPI::toJsonValue(m_bank_name));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_bin_isSet) {
        obj.insert(QString("bin"), ::OpenAPI::toJsonValue(m_bin));
    }
    if (m_brand.isSet()) {
        obj.insert(QString("brand"), ::OpenAPI::toJsonValue(m_brand));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_cvv_isSet) {
        obj.insert(QString("cvv"), ::OpenAPI::toJsonValue(m_cvv));
    }
    if (m_exp_month_isSet) {
        obj.insert(QString("expMonth"), ::OpenAPI::toJsonValue(m_exp_month));
    }
    if (m_exp_year_isSet) {
        obj.insert(QString("expYear"), ::OpenAPI::toJsonValue(m_exp_year));
    }
    if (m_fingerprint_isSet) {
        obj.insert(QString("fingerprint"), ::OpenAPI::toJsonValue(m_fingerprint));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last4_isSet) {
        obj.insert(QString("last4"), ::OpenAPI::toJsonValue(m_last4));
    }
    if (m_method.isSet()) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_pan_isSet) {
        obj.insert(QString("pan"), ::OpenAPI::toJsonValue(m_pan));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_expiration_reminder_number_isSet) {
        obj.insert(QString("expirationReminderNumber"), ::OpenAPI::toJsonValue(m_expiration_reminder_number));
    }
    if (m_expiration_reminder_time_isSet) {
        obj.insert(QString("expirationReminderTime"), ::OpenAPI::toJsonValue(m_expiration_reminder_time));
    }
    if (m_sticky_gateway_account_id_isSet) {
        obj.insert(QString("stickyGatewayAccountId"), ::OpenAPI::toJsonValue(m_sticky_gateway_account_id));
    }
    if (m_account_number_type_isSet) {
        obj.insert(QString("accountNumberType"), ::OpenAPI::toJsonValue(m_account_number_type));
    }
    if (m_account_type_isSet) {
        obj.insert(QString("accountType"), ::OpenAPI::toJsonValue(m_account_type));
    }
    if (m_bic_isSet) {
        obj.insert(QString("bic"), ::OpenAPI::toJsonValue(m_bic));
    }
    if (m_routing_number_isSet) {
        obj.insert(QString("routingNumber"), ::OpenAPI::toJsonValue(m_routing_number));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    return obj;
}

QString OAIPaymentInstrument_2::getBankCountry() const {
    return m_bank_country;
}
void OAIPaymentInstrument_2::setBankCountry(const QString &bank_country) {
    m_bank_country = bank_country;
    m_bank_country_isSet = true;
}

bool OAIPaymentInstrument_2::is_bank_country_Set() const{
    return m_bank_country_isSet;
}

bool OAIPaymentInstrument_2::is_bank_country_Valid() const{
    return m_bank_country_isValid;
}

QString OAIPaymentInstrument_2::getBankName() const {
    return m_bank_name;
}
void OAIPaymentInstrument_2::setBankName(const QString &bank_name) {
    m_bank_name = bank_name;
    m_bank_name_isSet = true;
}

bool OAIPaymentInstrument_2::is_bank_name_Set() const{
    return m_bank_name_isSet;
}

bool OAIPaymentInstrument_2::is_bank_name_Valid() const{
    return m_bank_name_isValid;
}

OAIContactObject OAIPaymentInstrument_2::getBillingAddress() const {
    return m_billing_address;
}
void OAIPaymentInstrument_2::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIPaymentInstrument_2::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIPaymentInstrument_2::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIPaymentInstrument_2::getBin() const {
    return m_bin;
}
void OAIPaymentInstrument_2::setBin(const QString &bin) {
    m_bin = bin;
    m_bin_isSet = true;
}

bool OAIPaymentInstrument_2::is_bin_Set() const{
    return m_bin_isSet;
}

bool OAIPaymentInstrument_2::is_bin_Valid() const{
    return m_bin_isValid;
}

OAIPaymentCardBrand OAIPaymentInstrument_2::getBrand() const {
    return m_brand;
}
void OAIPaymentInstrument_2::setBrand(const OAIPaymentCardBrand &brand) {
    m_brand = brand;
    m_brand_isSet = true;
}

bool OAIPaymentInstrument_2::is_brand_Set() const{
    return m_brand_isSet;
}

bool OAIPaymentInstrument_2::is_brand_Valid() const{
    return m_brand_isValid;
}

QDateTime OAIPaymentInstrument_2::getCreatedTime() const {
    return m_created_time;
}
void OAIPaymentInstrument_2::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIPaymentInstrument_2::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIPaymentInstrument_2::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIObject OAIPaymentInstrument_2::getCustomFields() const {
    return m_custom_fields;
}
void OAIPaymentInstrument_2::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIPaymentInstrument_2::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIPaymentInstrument_2::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIPaymentInstrument_2::getCustomerId() const {
    return m_customer_id;
}
void OAIPaymentInstrument_2::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIPaymentInstrument_2::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIPaymentInstrument_2::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAIPaymentInstrument_2::getCvv() const {
    return m_cvv;
}
void OAIPaymentInstrument_2::setCvv(const QString &cvv) {
    m_cvv = cvv;
    m_cvv_isSet = true;
}

bool OAIPaymentInstrument_2::is_cvv_Set() const{
    return m_cvv_isSet;
}

bool OAIPaymentInstrument_2::is_cvv_Valid() const{
    return m_cvv_isValid;
}

qint32 OAIPaymentInstrument_2::getExpMonth() const {
    return m_exp_month;
}
void OAIPaymentInstrument_2::setExpMonth(const qint32 &exp_month) {
    m_exp_month = exp_month;
    m_exp_month_isSet = true;
}

bool OAIPaymentInstrument_2::is_exp_month_Set() const{
    return m_exp_month_isSet;
}

bool OAIPaymentInstrument_2::is_exp_month_Valid() const{
    return m_exp_month_isValid;
}

qint32 OAIPaymentInstrument_2::getExpYear() const {
    return m_exp_year;
}
void OAIPaymentInstrument_2::setExpYear(const qint32 &exp_year) {
    m_exp_year = exp_year;
    m_exp_year_isSet = true;
}

bool OAIPaymentInstrument_2::is_exp_year_Set() const{
    return m_exp_year_isSet;
}

bool OAIPaymentInstrument_2::is_exp_year_Valid() const{
    return m_exp_year_isValid;
}

QString OAIPaymentInstrument_2::getFingerprint() const {
    return m_fingerprint;
}
void OAIPaymentInstrument_2::setFingerprint(const QString &fingerprint) {
    m_fingerprint = fingerprint;
    m_fingerprint_isSet = true;
}

bool OAIPaymentInstrument_2::is_fingerprint_Set() const{
    return m_fingerprint_isSet;
}

bool OAIPaymentInstrument_2::is_fingerprint_Valid() const{
    return m_fingerprint_isValid;
}

QString OAIPaymentInstrument_2::getId() const {
    return m_id;
}
void OAIPaymentInstrument_2::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPaymentInstrument_2::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPaymentInstrument_2::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPaymentInstrument_2::getLast4() const {
    return m_last4;
}
void OAIPaymentInstrument_2::setLast4(const QString &last4) {
    m_last4 = last4;
    m_last4_isSet = true;
}

bool OAIPaymentInstrument_2::is_last4_Set() const{
    return m_last4_isSet;
}

bool OAIPaymentInstrument_2::is_last4_Valid() const{
    return m_last4_isValid;
}

OAIAlternativePaymentMethods OAIPaymentInstrument_2::getMethod() const {
    return m_method;
}
void OAIPaymentInstrument_2::setMethod(const OAIAlternativePaymentMethods &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIPaymentInstrument_2::is_method_Set() const{
    return m_method_isSet;
}

bool OAIPaymentInstrument_2::is_method_Valid() const{
    return m_method_isValid;
}

QString OAIPaymentInstrument_2::getPan() const {
    return m_pan;
}
void OAIPaymentInstrument_2::setPan(const QString &pan) {
    m_pan = pan;
    m_pan_isSet = true;
}

bool OAIPaymentInstrument_2::is_pan_Set() const{
    return m_pan_isSet;
}

bool OAIPaymentInstrument_2::is_pan_Valid() const{
    return m_pan_isValid;
}

OAIRiskMetadata OAIPaymentInstrument_2::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAIPaymentInstrument_2::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAIPaymentInstrument_2::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAIPaymentInstrument_2::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

QString OAIPaymentInstrument_2::getStatus() const {
    return m_status;
}
void OAIPaymentInstrument_2::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPaymentInstrument_2::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPaymentInstrument_2::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIPaymentInstrument_2::getUpdatedTime() const {
    return m_updated_time;
}
void OAIPaymentInstrument_2::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIPaymentInstrument_2::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIPaymentInstrument_2::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QList<OAIAlternativePaymentInstrument_2__embedded_inner> OAIPaymentInstrument_2::getEmbedded() const {
    return m__embedded;
}
void OAIPaymentInstrument_2::setEmbedded(const QList<OAIAlternativePaymentInstrument_2__embedded_inner> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAIPaymentInstrument_2::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAIPaymentInstrument_2::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAIAlternativePaymentInstrument_2__links_inner> OAIPaymentInstrument_2::getLinks() const {
    return m__links;
}
void OAIPaymentInstrument_2::setLinks(const QList<OAIAlternativePaymentInstrument_2__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIPaymentInstrument_2::is__links_Set() const{
    return m__links_isSet;
}

bool OAIPaymentInstrument_2::is__links_Valid() const{
    return m__links_isValid;
}

qint32 OAIPaymentInstrument_2::getExpirationReminderNumber() const {
    return m_expiration_reminder_number;
}
void OAIPaymentInstrument_2::setExpirationReminderNumber(const qint32 &expiration_reminder_number) {
    m_expiration_reminder_number = expiration_reminder_number;
    m_expiration_reminder_number_isSet = true;
}

bool OAIPaymentInstrument_2::is_expiration_reminder_number_Set() const{
    return m_expiration_reminder_number_isSet;
}

bool OAIPaymentInstrument_2::is_expiration_reminder_number_Valid() const{
    return m_expiration_reminder_number_isValid;
}

QDateTime OAIPaymentInstrument_2::getExpirationReminderTime() const {
    return m_expiration_reminder_time;
}
void OAIPaymentInstrument_2::setExpirationReminderTime(const QDateTime &expiration_reminder_time) {
    m_expiration_reminder_time = expiration_reminder_time;
    m_expiration_reminder_time_isSet = true;
}

bool OAIPaymentInstrument_2::is_expiration_reminder_time_Set() const{
    return m_expiration_reminder_time_isSet;
}

bool OAIPaymentInstrument_2::is_expiration_reminder_time_Valid() const{
    return m_expiration_reminder_time_isValid;
}

QString OAIPaymentInstrument_2::getStickyGatewayAccountId() const {
    return m_sticky_gateway_account_id;
}
void OAIPaymentInstrument_2::setStickyGatewayAccountId(const QString &sticky_gateway_account_id) {
    m_sticky_gateway_account_id = sticky_gateway_account_id;
    m_sticky_gateway_account_id_isSet = true;
}

bool OAIPaymentInstrument_2::is_sticky_gateway_account_id_Set() const{
    return m_sticky_gateway_account_id_isSet;
}

bool OAIPaymentInstrument_2::is_sticky_gateway_account_id_Valid() const{
    return m_sticky_gateway_account_id_isValid;
}

QString OAIPaymentInstrument_2::getAccountNumberType() const {
    return m_account_number_type;
}
void OAIPaymentInstrument_2::setAccountNumberType(const QString &account_number_type) {
    m_account_number_type = account_number_type;
    m_account_number_type_isSet = true;
}

bool OAIPaymentInstrument_2::is_account_number_type_Set() const{
    return m_account_number_type_isSet;
}

bool OAIPaymentInstrument_2::is_account_number_type_Valid() const{
    return m_account_number_type_isValid;
}

QString OAIPaymentInstrument_2::getAccountType() const {
    return m_account_type;
}
void OAIPaymentInstrument_2::setAccountType(const QString &account_type) {
    m_account_type = account_type;
    m_account_type_isSet = true;
}

bool OAIPaymentInstrument_2::is_account_type_Set() const{
    return m_account_type_isSet;
}

bool OAIPaymentInstrument_2::is_account_type_Valid() const{
    return m_account_type_isValid;
}

QString OAIPaymentInstrument_2::getBic() const {
    return m_bic;
}
void OAIPaymentInstrument_2::setBic(const QString &bic) {
    m_bic = bic;
    m_bic_isSet = true;
}

bool OAIPaymentInstrument_2::is_bic_Set() const{
    return m_bic_isSet;
}

bool OAIPaymentInstrument_2::is_bic_Valid() const{
    return m_bic_isValid;
}

QString OAIPaymentInstrument_2::getRoutingNumber() const {
    return m_routing_number;
}
void OAIPaymentInstrument_2::setRoutingNumber(const QString &routing_number) {
    m_routing_number = routing_number;
    m_routing_number_isSet = true;
}

bool OAIPaymentInstrument_2::is_routing_number_Set() const{
    return m_routing_number_isSet;
}

bool OAIPaymentInstrument_2::is_routing_number_Valid() const{
    return m_routing_number_isValid;
}

QString OAIPaymentInstrument_2::getUsername() const {
    return m_username;
}
void OAIPaymentInstrument_2::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIPaymentInstrument_2::is_username_Set() const{
    return m_username_isSet;
}

bool OAIPaymentInstrument_2::is_username_Valid() const{
    return m_username_isValid;
}

QString OAIPaymentInstrument_2::getNumber() const {
    return m_number;
}
void OAIPaymentInstrument_2::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIPaymentInstrument_2::is_number_Set() const{
    return m_number_isSet;
}

bool OAIPaymentInstrument_2::is_number_Valid() const{
    return m_number_isValid;
}

bool OAIPaymentInstrument_2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bank_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_bin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_brand.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvv_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_month_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fingerprint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_method.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pan_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__embedded.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_reminder_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expiration_reminder_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sticky_gateway_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_account_number_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_account_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_routing_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentInstrument_2::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_billing_address_isValid && m_customer_id_isValid && m_method_isValid && true;
}

} // namespace OpenAPI
