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

#include "OAICommonTransaction.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommonTransaction::OAICommonTransaction(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommonTransaction::OAICommonTransaction() {
    this->initializeModel();
}

OAICommonTransaction::~OAICommonTransaction() {}

void OAICommonTransaction::initializeModel() {

    m_r_3ds_isSet = false;
    m_r_3ds_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_billing_descriptor_isSet = false;
    m_billing_descriptor_isValid = false;

    m_child_transactions_isSet = false;
    m_child_transactions_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_gateway_name_isSet = false;
    m_gateway_name_isValid = false;

    m_has3ds_isSet = false;
    m_has3ds_isValid = false;

    m_has_amount_adjustment_isSet = false;
    m_has_amount_adjustment_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_ids_isSet = false;
    m_invoice_ids_isValid = false;

    m_is_rebill_isSet = false;
    m_is_rebill_isValid = false;

    m_is_retry_isSet = false;
    m_is_retry_isValid = false;

    m_parent_transaction_id_isSet = false;
    m_parent_transaction_id_isValid = false;

    m_payment_instrument_isSet = false;
    m_payment_instrument_isValid = false;

    m_plan_ids_isSet = false;
    m_plan_ids_isValid = false;

    m_processed_time_isSet = false;
    m_processed_time_isValid = false;

    m_purchase_amount_isSet = false;
    m_purchase_amount_isValid = false;

    m_purchase_currency_isSet = false;
    m_purchase_currency_isValid = false;

    m_rebill_number_isSet = false;
    m_rebill_number_isValid = false;

    m_redirect_url_isSet = false;
    m_redirect_url_isValid = false;

    m_request_amount_isSet = false;
    m_request_amount_isValid = false;

    m_request_currency_isSet = false;
    m_request_currency_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_result_isSet = false;
    m_result_isValid = false;

    m_retry_number_isSet = false;
    m_retry_number_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscription_ids_isSet = false;
    m_subscription_ids_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;
}

void OAICommonTransaction::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommonTransaction::fromJsonObject(QJsonObject json) {

    m_r_3ds_isValid = ::OpenAPI::fromJsonValue(m_r_3ds, json[QString("3ds")]);
    m_r_3ds_isSet = !json[QString("3ds")].isNull() && m_r_3ds_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_billing_descriptor_isValid = ::OpenAPI::fromJsonValue(m_billing_descriptor, json[QString("billingDescriptor")]);
    m_billing_descriptor_isSet = !json[QString("billingDescriptor")].isNull() && m_billing_descriptor_isValid;

    m_child_transactions_isValid = ::OpenAPI::fromJsonValue(m_child_transactions, json[QString("childTransactions")]);
    m_child_transactions_isSet = !json[QString("childTransactions")].isNull() && m_child_transactions_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_gateway_name_isValid = ::OpenAPI::fromJsonValue(m_gateway_name, json[QString("gatewayName")]);
    m_gateway_name_isSet = !json[QString("gatewayName")].isNull() && m_gateway_name_isValid;

    m_has3ds_isValid = ::OpenAPI::fromJsonValue(m_has3ds, json[QString("has3ds")]);
    m_has3ds_isSet = !json[QString("has3ds")].isNull() && m_has3ds_isValid;

    m_has_amount_adjustment_isValid = ::OpenAPI::fromJsonValue(m_has_amount_adjustment, json[QString("hasAmountAdjustment")]);
    m_has_amount_adjustment_isSet = !json[QString("hasAmountAdjustment")].isNull() && m_has_amount_adjustment_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_ids_isValid = ::OpenAPI::fromJsonValue(m_invoice_ids, json[QString("invoiceIds")]);
    m_invoice_ids_isSet = !json[QString("invoiceIds")].isNull() && m_invoice_ids_isValid;

    m_is_rebill_isValid = ::OpenAPI::fromJsonValue(m_is_rebill, json[QString("isRebill")]);
    m_is_rebill_isSet = !json[QString("isRebill")].isNull() && m_is_rebill_isValid;

    m_is_retry_isValid = ::OpenAPI::fromJsonValue(m_is_retry, json[QString("isRetry")]);
    m_is_retry_isSet = !json[QString("isRetry")].isNull() && m_is_retry_isValid;

    m_parent_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_parent_transaction_id, json[QString("parentTransactionId")]);
    m_parent_transaction_id_isSet = !json[QString("parentTransactionId")].isNull() && m_parent_transaction_id_isValid;

    m_payment_instrument_isValid = ::OpenAPI::fromJsonValue(m_payment_instrument, json[QString("paymentInstrument")]);
    m_payment_instrument_isSet = !json[QString("paymentInstrument")].isNull() && m_payment_instrument_isValid;

    m_plan_ids_isValid = ::OpenAPI::fromJsonValue(m_plan_ids, json[QString("planIds")]);
    m_plan_ids_isSet = !json[QString("planIds")].isNull() && m_plan_ids_isValid;

    m_processed_time_isValid = ::OpenAPI::fromJsonValue(m_processed_time, json[QString("processedTime")]);
    m_processed_time_isSet = !json[QString("processedTime")].isNull() && m_processed_time_isValid;

    m_purchase_amount_isValid = ::OpenAPI::fromJsonValue(m_purchase_amount, json[QString("purchaseAmount")]);
    m_purchase_amount_isSet = !json[QString("purchaseAmount")].isNull() && m_purchase_amount_isValid;

    m_purchase_currency_isValid = ::OpenAPI::fromJsonValue(m_purchase_currency, json[QString("purchaseCurrency")]);
    m_purchase_currency_isSet = !json[QString("purchaseCurrency")].isNull() && m_purchase_currency_isValid;

    m_rebill_number_isValid = ::OpenAPI::fromJsonValue(m_rebill_number, json[QString("rebillNumber")]);
    m_rebill_number_isSet = !json[QString("rebillNumber")].isNull() && m_rebill_number_isValid;

    m_redirect_url_isValid = ::OpenAPI::fromJsonValue(m_redirect_url, json[QString("redirectUrl")]);
    m_redirect_url_isSet = !json[QString("redirectUrl")].isNull() && m_redirect_url_isValid;

    m_request_amount_isValid = ::OpenAPI::fromJsonValue(m_request_amount, json[QString("requestAmount")]);
    m_request_amount_isSet = !json[QString("requestAmount")].isNull() && m_request_amount_isValid;

    m_request_currency_isValid = ::OpenAPI::fromJsonValue(m_request_currency, json[QString("requestCurrency")]);
    m_request_currency_isSet = !json[QString("requestCurrency")].isNull() && m_request_currency_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;

    m_retry_number_isValid = ::OpenAPI::fromJsonValue(m_retry_number, json[QString("retryNumber")]);
    m_retry_number_isSet = !json[QString("retryNumber")].isNull() && m_retry_number_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscription_ids_isValid = ::OpenAPI::fromJsonValue(m_subscription_ids, json[QString("subscriptionIds")]);
    m_subscription_ids_isSet = !json[QString("subscriptionIds")].isNull() && m_subscription_ids_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;
}

QString OAICommonTransaction::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommonTransaction::asJsonObject() const {
    QJsonObject obj;
    if (m_r_3ds.isSet()) {
        obj.insert(QString("3ds"), ::OpenAPI::toJsonValue(m_r_3ds));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_billing_descriptor_isSet) {
        obj.insert(QString("billingDescriptor"), ::OpenAPI::toJsonValue(m_billing_descriptor));
    }
    if (m_child_transactions.size() > 0) {
        obj.insert(QString("childTransactions"), ::OpenAPI::toJsonValue(m_child_transactions));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_gateway_name.isSet()) {
        obj.insert(QString("gatewayName"), ::OpenAPI::toJsonValue(m_gateway_name));
    }
    if (m_has3ds_isSet) {
        obj.insert(QString("has3ds"), ::OpenAPI::toJsonValue(m_has3ds));
    }
    if (m_has_amount_adjustment_isSet) {
        obj.insert(QString("hasAmountAdjustment"), ::OpenAPI::toJsonValue(m_has_amount_adjustment));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_ids.size() > 0) {
        obj.insert(QString("invoiceIds"), ::OpenAPI::toJsonValue(m_invoice_ids));
    }
    if (m_is_rebill_isSet) {
        obj.insert(QString("isRebill"), ::OpenAPI::toJsonValue(m_is_rebill));
    }
    if (m_is_retry_isSet) {
        obj.insert(QString("isRetry"), ::OpenAPI::toJsonValue(m_is_retry));
    }
    if (m_parent_transaction_id_isSet) {
        obj.insert(QString("parentTransactionId"), ::OpenAPI::toJsonValue(m_parent_transaction_id));
    }
    if (m_payment_instrument.isSet()) {
        obj.insert(QString("paymentInstrument"), ::OpenAPI::toJsonValue(m_payment_instrument));
    }
    if (m_plan_ids.size() > 0) {
        obj.insert(QString("planIds"), ::OpenAPI::toJsonValue(m_plan_ids));
    }
    if (m_processed_time_isSet) {
        obj.insert(QString("processedTime"), ::OpenAPI::toJsonValue(m_processed_time));
    }
    if (m_purchase_amount_isSet) {
        obj.insert(QString("purchaseAmount"), ::OpenAPI::toJsonValue(m_purchase_amount));
    }
    if (m_purchase_currency_isSet) {
        obj.insert(QString("purchaseCurrency"), ::OpenAPI::toJsonValue(m_purchase_currency));
    }
    if (m_rebill_number_isSet) {
        obj.insert(QString("rebillNumber"), ::OpenAPI::toJsonValue(m_rebill_number));
    }
    if (m_redirect_url_isSet) {
        obj.insert(QString("redirectUrl"), ::OpenAPI::toJsonValue(m_redirect_url));
    }
    if (m_request_amount_isSet) {
        obj.insert(QString("requestAmount"), ::OpenAPI::toJsonValue(m_request_amount));
    }
    if (m_request_currency_isSet) {
        obj.insert(QString("requestCurrency"), ::OpenAPI::toJsonValue(m_request_currency));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_result_isSet) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_retry_number_isSet) {
        obj.insert(QString("retryNumber"), ::OpenAPI::toJsonValue(m_retry_number));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscription_ids.size() > 0) {
        obj.insert(QString("subscriptionIds"), ::OpenAPI::toJsonValue(m_subscription_ids));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    return obj;
}

OAIThreeDSecureResult OAICommonTransaction::getR3ds() const {
    return m_r_3ds;
}
void OAICommonTransaction::setR3ds(const OAIThreeDSecureResult &r_3ds) {
    m_r_3ds = r_3ds;
    m_r_3ds_isSet = true;
}

bool OAICommonTransaction::is_r_3ds_Set() const{
    return m_r_3ds_isSet;
}

bool OAICommonTransaction::is_r_3ds_Valid() const{
    return m_r_3ds_isValid;
}

double OAICommonTransaction::getAmount() const {
    return m_amount;
}
void OAICommonTransaction::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAICommonTransaction::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAICommonTransaction::is_amount_Valid() const{
    return m_amount_isValid;
}

OAIContactObject OAICommonTransaction::getBillingAddress() const {
    return m_billing_address;
}
void OAICommonTransaction::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICommonTransaction::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICommonTransaction::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAICommonTransaction::getBillingDescriptor() const {
    return m_billing_descriptor;
}
void OAICommonTransaction::setBillingDescriptor(const QString &billing_descriptor) {
    m_billing_descriptor = billing_descriptor;
    m_billing_descriptor_isSet = true;
}

bool OAICommonTransaction::is_billing_descriptor_Set() const{
    return m_billing_descriptor_isSet;
}

bool OAICommonTransaction::is_billing_descriptor_Valid() const{
    return m_billing_descriptor_isValid;
}

QList<QString> OAICommonTransaction::getChildTransactions() const {
    return m_child_transactions;
}
void OAICommonTransaction::setChildTransactions(const QList<QString> &child_transactions) {
    m_child_transactions = child_transactions;
    m_child_transactions_isSet = true;
}

bool OAICommonTransaction::is_child_transactions_Set() const{
    return m_child_transactions_isSet;
}

bool OAICommonTransaction::is_child_transactions_Valid() const{
    return m_child_transactions_isValid;
}

QDateTime OAICommonTransaction::getCreatedTime() const {
    return m_created_time;
}
void OAICommonTransaction::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAICommonTransaction::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAICommonTransaction::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAICommonTransaction::getCurrency() const {
    return m_currency;
}
void OAICommonTransaction::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAICommonTransaction::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAICommonTransaction::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAICommonTransaction::getCustomFields() const {
    return m_custom_fields;
}
void OAICommonTransaction::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAICommonTransaction::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAICommonTransaction::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAICommonTransaction::getCustomerId() const {
    return m_customer_id;
}
void OAICommonTransaction::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAICommonTransaction::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAICommonTransaction::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAICommonTransaction::getDescription() const {
    return m_description;
}
void OAICommonTransaction::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICommonTransaction::is_description_Set() const{
    return m_description_isSet;
}

bool OAICommonTransaction::is_description_Valid() const{
    return m_description_isValid;
}

OAIGatewayName OAICommonTransaction::getGatewayName() const {
    return m_gateway_name;
}
void OAICommonTransaction::setGatewayName(const OAIGatewayName &gateway_name) {
    m_gateway_name = gateway_name;
    m_gateway_name_isSet = true;
}

bool OAICommonTransaction::is_gateway_name_Set() const{
    return m_gateway_name_isSet;
}

bool OAICommonTransaction::is_gateway_name_Valid() const{
    return m_gateway_name_isValid;
}

bool OAICommonTransaction::isHas3ds() const {
    return m_has3ds;
}
void OAICommonTransaction::setHas3ds(const bool &has3ds) {
    m_has3ds = has3ds;
    m_has3ds_isSet = true;
}

bool OAICommonTransaction::is_has3ds_Set() const{
    return m_has3ds_isSet;
}

bool OAICommonTransaction::is_has3ds_Valid() const{
    return m_has3ds_isValid;
}

bool OAICommonTransaction::isHasAmountAdjustment() const {
    return m_has_amount_adjustment;
}
void OAICommonTransaction::setHasAmountAdjustment(const bool &has_amount_adjustment) {
    m_has_amount_adjustment = has_amount_adjustment;
    m_has_amount_adjustment_isSet = true;
}

bool OAICommonTransaction::is_has_amount_adjustment_Set() const{
    return m_has_amount_adjustment_isSet;
}

bool OAICommonTransaction::is_has_amount_adjustment_Valid() const{
    return m_has_amount_adjustment_isValid;
}

QString OAICommonTransaction::getId() const {
    return m_id;
}
void OAICommonTransaction::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICommonTransaction::is_id_Set() const{
    return m_id_isSet;
}

bool OAICommonTransaction::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAICommonTransaction::getInvoiceIds() const {
    return m_invoice_ids;
}
void OAICommonTransaction::setInvoiceIds(const QList<QString> &invoice_ids) {
    m_invoice_ids = invoice_ids;
    m_invoice_ids_isSet = true;
}

bool OAICommonTransaction::is_invoice_ids_Set() const{
    return m_invoice_ids_isSet;
}

bool OAICommonTransaction::is_invoice_ids_Valid() const{
    return m_invoice_ids_isValid;
}

bool OAICommonTransaction::isIsRebill() const {
    return m_is_rebill;
}
void OAICommonTransaction::setIsRebill(const bool &is_rebill) {
    m_is_rebill = is_rebill;
    m_is_rebill_isSet = true;
}

bool OAICommonTransaction::is_is_rebill_Set() const{
    return m_is_rebill_isSet;
}

bool OAICommonTransaction::is_is_rebill_Valid() const{
    return m_is_rebill_isValid;
}

bool OAICommonTransaction::isIsRetry() const {
    return m_is_retry;
}
void OAICommonTransaction::setIsRetry(const bool &is_retry) {
    m_is_retry = is_retry;
    m_is_retry_isSet = true;
}

bool OAICommonTransaction::is_is_retry_Set() const{
    return m_is_retry_isSet;
}

bool OAICommonTransaction::is_is_retry_Valid() const{
    return m_is_retry_isValid;
}

QString OAICommonTransaction::getParentTransactionId() const {
    return m_parent_transaction_id;
}
void OAICommonTransaction::setParentTransactionId(const QString &parent_transaction_id) {
    m_parent_transaction_id = parent_transaction_id;
    m_parent_transaction_id_isSet = true;
}

bool OAICommonTransaction::is_parent_transaction_id_Set() const{
    return m_parent_transaction_id_isSet;
}

bool OAICommonTransaction::is_parent_transaction_id_Valid() const{
    return m_parent_transaction_id_isValid;
}

OAIInstrumentReference OAICommonTransaction::getPaymentInstrument() const {
    return m_payment_instrument;
}
void OAICommonTransaction::setPaymentInstrument(const OAIInstrumentReference &payment_instrument) {
    m_payment_instrument = payment_instrument;
    m_payment_instrument_isSet = true;
}

bool OAICommonTransaction::is_payment_instrument_Set() const{
    return m_payment_instrument_isSet;
}

bool OAICommonTransaction::is_payment_instrument_Valid() const{
    return m_payment_instrument_isValid;
}

QList<QString> OAICommonTransaction::getPlanIds() const {
    return m_plan_ids;
}
void OAICommonTransaction::setPlanIds(const QList<QString> &plan_ids) {
    m_plan_ids = plan_ids;
    m_plan_ids_isSet = true;
}

bool OAICommonTransaction::is_plan_ids_Set() const{
    return m_plan_ids_isSet;
}

bool OAICommonTransaction::is_plan_ids_Valid() const{
    return m_plan_ids_isValid;
}

QDateTime OAICommonTransaction::getProcessedTime() const {
    return m_processed_time;
}
void OAICommonTransaction::setProcessedTime(const QDateTime &processed_time) {
    m_processed_time = processed_time;
    m_processed_time_isSet = true;
}

bool OAICommonTransaction::is_processed_time_Set() const{
    return m_processed_time_isSet;
}

bool OAICommonTransaction::is_processed_time_Valid() const{
    return m_processed_time_isValid;
}

double OAICommonTransaction::getPurchaseAmount() const {
    return m_purchase_amount;
}
void OAICommonTransaction::setPurchaseAmount(const double &purchase_amount) {
    m_purchase_amount = purchase_amount;
    m_purchase_amount_isSet = true;
}

bool OAICommonTransaction::is_purchase_amount_Set() const{
    return m_purchase_amount_isSet;
}

bool OAICommonTransaction::is_purchase_amount_Valid() const{
    return m_purchase_amount_isValid;
}

QString OAICommonTransaction::getPurchaseCurrency() const {
    return m_purchase_currency;
}
void OAICommonTransaction::setPurchaseCurrency(const QString &purchase_currency) {
    m_purchase_currency = purchase_currency;
    m_purchase_currency_isSet = true;
}

bool OAICommonTransaction::is_purchase_currency_Set() const{
    return m_purchase_currency_isSet;
}

bool OAICommonTransaction::is_purchase_currency_Valid() const{
    return m_purchase_currency_isValid;
}

qint32 OAICommonTransaction::getRebillNumber() const {
    return m_rebill_number;
}
void OAICommonTransaction::setRebillNumber(const qint32 &rebill_number) {
    m_rebill_number = rebill_number;
    m_rebill_number_isSet = true;
}

bool OAICommonTransaction::is_rebill_number_Set() const{
    return m_rebill_number_isSet;
}

bool OAICommonTransaction::is_rebill_number_Valid() const{
    return m_rebill_number_isValid;
}

QString OAICommonTransaction::getRedirectUrl() const {
    return m_redirect_url;
}
void OAICommonTransaction::setRedirectUrl(const QString &redirect_url) {
    m_redirect_url = redirect_url;
    m_redirect_url_isSet = true;
}

bool OAICommonTransaction::is_redirect_url_Set() const{
    return m_redirect_url_isSet;
}

bool OAICommonTransaction::is_redirect_url_Valid() const{
    return m_redirect_url_isValid;
}

double OAICommonTransaction::getRequestAmount() const {
    return m_request_amount;
}
void OAICommonTransaction::setRequestAmount(const double &request_amount) {
    m_request_amount = request_amount;
    m_request_amount_isSet = true;
}

bool OAICommonTransaction::is_request_amount_Set() const{
    return m_request_amount_isSet;
}

bool OAICommonTransaction::is_request_amount_Valid() const{
    return m_request_amount_isValid;
}

QString OAICommonTransaction::getRequestCurrency() const {
    return m_request_currency;
}
void OAICommonTransaction::setRequestCurrency(const QString &request_currency) {
    m_request_currency = request_currency;
    m_request_currency_isSet = true;
}

bool OAICommonTransaction::is_request_currency_Set() const{
    return m_request_currency_isSet;
}

bool OAICommonTransaction::is_request_currency_Valid() const{
    return m_request_currency_isValid;
}

QString OAICommonTransaction::getRequestId() const {
    return m_request_id;
}
void OAICommonTransaction::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAICommonTransaction::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAICommonTransaction::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QString OAICommonTransaction::getResult() const {
    return m_result;
}
void OAICommonTransaction::setResult(const QString &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAICommonTransaction::is_result_Set() const{
    return m_result_isSet;
}

bool OAICommonTransaction::is_result_Valid() const{
    return m_result_isValid;
}

qint32 OAICommonTransaction::getRetryNumber() const {
    return m_retry_number;
}
void OAICommonTransaction::setRetryNumber(const qint32 &retry_number) {
    m_retry_number = retry_number;
    m_retry_number_isSet = true;
}

bool OAICommonTransaction::is_retry_number_Set() const{
    return m_retry_number_isSet;
}

bool OAICommonTransaction::is_retry_number_Valid() const{
    return m_retry_number_isValid;
}

QString OAICommonTransaction::getStatus() const {
    return m_status;
}
void OAICommonTransaction::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICommonTransaction::is_status_Set() const{
    return m_status_isSet;
}

bool OAICommonTransaction::is_status_Valid() const{
    return m_status_isValid;
}

QList<QString> OAICommonTransaction::getSubscriptionIds() const {
    return m_subscription_ids;
}
void OAICommonTransaction::setSubscriptionIds(const QList<QString> &subscription_ids) {
    m_subscription_ids = subscription_ids;
    m_subscription_ids_isSet = true;
}

bool OAICommonTransaction::is_subscription_ids_Set() const{
    return m_subscription_ids_isSet;
}

bool OAICommonTransaction::is_subscription_ids_Valid() const{
    return m_subscription_ids_isValid;
}

QString OAICommonTransaction::getType() const {
    return m_type;
}
void OAICommonTransaction::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICommonTransaction::is_type_Set() const{
    return m_type_isSet;
}

bool OAICommonTransaction::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAICommonTransaction::getUpdatedTime() const {
    return m_updated_time;
}
void OAICommonTransaction::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAICommonTransaction::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAICommonTransaction::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAICommonTransaction::getWebsiteId() const {
    return m_website_id;
}
void OAICommonTransaction::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICommonTransaction::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICommonTransaction::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICommonTransaction::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_3ds.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_descriptor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_child_transactions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
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

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_has3ds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_amount_adjustment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_rebill_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_retry_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instrument.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_plan_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_processed_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rebill_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_redirect_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommonTransaction::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
