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

#include "OAIInvoice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoice::OAIInvoice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoice::OAIInvoice() {
    this->initializeModel();
}

OAIInvoice::~OAIInvoice() {}

void OAIInvoice::initializeModel() {

    m_abandoned_time_isSet = false;
    m_abandoned_time_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_amount_due_isSet = false;
    m_amount_due_isValid = false;

    m_autopay_retry_number_isSet = false;
    m_autopay_retry_number_isValid = false;

    m_autopay_scheduled_time_isSet = false;
    m_autopay_scheduled_time_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_collection_period_isSet = false;
    m_collection_period_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_delinquent_collection_period_isSet = false;
    m_delinquent_collection_period_isValid = false;

    m_delivery_address_isSet = false;
    m_delivery_address_isValid = false;

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_discounts_isSet = false;
    m_discounts_isValid = false;

    m_due_time_isSet = false;
    m_due_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_number_isSet = false;
    m_invoice_number_isValid = false;

    m_issued_time_isSet = false;
    m_issued_time_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_paid_time_isSet = false;
    m_paid_time_isValid = false;

    m_payment_form_url_isSet = false;
    m_payment_form_url_isValid = false;

    m_po_number_isSet = false;
    m_po_number_isValid = false;

    m_shipping_isSet = false;
    m_shipping_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscription_id_isSet = false;
    m_subscription_id_isValid = false;

    m_subtotal_amount_isSet = false;
    m_subtotal_amount_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_voided_time_isSet = false;
    m_voided_time_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_due_reminder_number_isSet = false;
    m_due_reminder_number_isValid = false;

    m_due_reminder_time_isSet = false;
    m_due_reminder_time_isValid = false;

    m_retry_instruction_isSet = false;
    m_retry_instruction_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_transactions_isSet = false;
    m_transactions_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIInvoice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoice::fromJsonObject(QJsonObject json) {

    m_abandoned_time_isValid = ::OpenAPI::fromJsonValue(m_abandoned_time, json[QString("abandonedTime")]);
    m_abandoned_time_isSet = !json[QString("abandonedTime")].isNull() && m_abandoned_time_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_amount_due_isValid = ::OpenAPI::fromJsonValue(m_amount_due, json[QString("amountDue")]);
    m_amount_due_isSet = !json[QString("amountDue")].isNull() && m_amount_due_isValid;

    m_autopay_retry_number_isValid = ::OpenAPI::fromJsonValue(m_autopay_retry_number, json[QString("autopayRetryNumber")]);
    m_autopay_retry_number_isSet = !json[QString("autopayRetryNumber")].isNull() && m_autopay_retry_number_isValid;

    m_autopay_scheduled_time_isValid = ::OpenAPI::fromJsonValue(m_autopay_scheduled_time, json[QString("autopayScheduledTime")]);
    m_autopay_scheduled_time_isSet = !json[QString("autopayScheduledTime")].isNull() && m_autopay_scheduled_time_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_collection_period_isValid = ::OpenAPI::fromJsonValue(m_collection_period, json[QString("collectionPeriod")]);
    m_collection_period_isSet = !json[QString("collectionPeriod")].isNull() && m_collection_period_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_delinquent_collection_period_isValid = ::OpenAPI::fromJsonValue(m_delinquent_collection_period, json[QString("delinquentCollectionPeriod")]);
    m_delinquent_collection_period_isSet = !json[QString("delinquentCollectionPeriod")].isNull() && m_delinquent_collection_period_isValid;

    m_delivery_address_isValid = ::OpenAPI::fromJsonValue(m_delivery_address, json[QString("deliveryAddress")]);
    m_delivery_address_isSet = !json[QString("deliveryAddress")].isNull() && m_delivery_address_isValid;

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("discountAmount")]);
    m_discount_amount_isSet = !json[QString("discountAmount")].isNull() && m_discount_amount_isValid;

    m_discounts_isValid = ::OpenAPI::fromJsonValue(m_discounts, json[QString("discounts")]);
    m_discounts_isSet = !json[QString("discounts")].isNull() && m_discounts_isValid;

    m_due_time_isValid = ::OpenAPI::fromJsonValue(m_due_time, json[QString("dueTime")]);
    m_due_time_isSet = !json[QString("dueTime")].isNull() && m_due_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_number_isValid = ::OpenAPI::fromJsonValue(m_invoice_number, json[QString("invoiceNumber")]);
    m_invoice_number_isSet = !json[QString("invoiceNumber")].isNull() && m_invoice_number_isValid;

    m_issued_time_isValid = ::OpenAPI::fromJsonValue(m_issued_time, json[QString("issuedTime")]);
    m_issued_time_isSet = !json[QString("issuedTime")].isNull() && m_issued_time_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_paid_time_isValid = ::OpenAPI::fromJsonValue(m_paid_time, json[QString("paidTime")]);
    m_paid_time_isSet = !json[QString("paidTime")].isNull() && m_paid_time_isValid;

    m_payment_form_url_isValid = ::OpenAPI::fromJsonValue(m_payment_form_url, json[QString("paymentFormUrl")]);
    m_payment_form_url_isSet = !json[QString("paymentFormUrl")].isNull() && m_payment_form_url_isValid;

    m_po_number_isValid = ::OpenAPI::fromJsonValue(m_po_number, json[QString("poNumber")]);
    m_po_number_isSet = !json[QString("poNumber")].isNull() && m_po_number_isValid;

    m_shipping_isValid = ::OpenAPI::fromJsonValue(m_shipping, json[QString("shipping")]);
    m_shipping_isSet = !json[QString("shipping")].isNull() && m_shipping_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscription_id_isValid = ::OpenAPI::fromJsonValue(m_subscription_id, json[QString("subscriptionId")]);
    m_subscription_id_isSet = !json[QString("subscriptionId")].isNull() && m_subscription_id_isValid;

    m_subtotal_amount_isValid = ::OpenAPI::fromJsonValue(m_subtotal_amount, json[QString("subtotalAmount")]);
    m_subtotal_amount_isSet = !json[QString("subtotalAmount")].isNull() && m_subtotal_amount_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_voided_time_isValid = ::OpenAPI::fromJsonValue(m_voided_time, json[QString("voidedTime")]);
    m_voided_time_isSet = !json[QString("voidedTime")].isNull() && m_voided_time_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_due_reminder_number_isValid = ::OpenAPI::fromJsonValue(m_due_reminder_number, json[QString("dueReminderNumber")]);
    m_due_reminder_number_isSet = !json[QString("dueReminderNumber")].isNull() && m_due_reminder_number_isValid;

    m_due_reminder_time_isValid = ::OpenAPI::fromJsonValue(m_due_reminder_time, json[QString("dueReminderTime")]);
    m_due_reminder_time_isSet = !json[QString("dueReminderTime")].isNull() && m_due_reminder_time_isValid;

    m_retry_instruction_isValid = ::OpenAPI::fromJsonValue(m_retry_instruction, json[QString("retryInstruction")]);
    m_retry_instruction_isSet = !json[QString("retryInstruction")].isNull() && m_retry_instruction_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_transactions_isValid = ::OpenAPI::fromJsonValue(m_transactions, json[QString("transactions")]);
    m_transactions_isSet = !json[QString("transactions")].isNull() && m_transactions_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIInvoice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoice::asJsonObject() const {
    QJsonObject obj;
    if (m_abandoned_time_isSet) {
        obj.insert(QString("abandonedTime"), ::OpenAPI::toJsonValue(m_abandoned_time));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_amount_due_isSet) {
        obj.insert(QString("amountDue"), ::OpenAPI::toJsonValue(m_amount_due));
    }
    if (m_autopay_retry_number_isSet) {
        obj.insert(QString("autopayRetryNumber"), ::OpenAPI::toJsonValue(m_autopay_retry_number));
    }
    if (m_autopay_scheduled_time_isSet) {
        obj.insert(QString("autopayScheduledTime"), ::OpenAPI::toJsonValue(m_autopay_scheduled_time));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_collection_period_isSet) {
        obj.insert(QString("collectionPeriod"), ::OpenAPI::toJsonValue(m_collection_period));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_delinquent_collection_period_isSet) {
        obj.insert(QString("delinquentCollectionPeriod"), ::OpenAPI::toJsonValue(m_delinquent_collection_period));
    }
    if (m_delivery_address.isSet()) {
        obj.insert(QString("deliveryAddress"), ::OpenAPI::toJsonValue(m_delivery_address));
    }
    if (m_discount_amount_isSet) {
        obj.insert(QString("discountAmount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_discounts.size() > 0) {
        obj.insert(QString("discounts"), ::OpenAPI::toJsonValue(m_discounts));
    }
    if (m_due_time_isSet) {
        obj.insert(QString("dueTime"), ::OpenAPI::toJsonValue(m_due_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_number_isSet) {
        obj.insert(QString("invoiceNumber"), ::OpenAPI::toJsonValue(m_invoice_number));
    }
    if (m_issued_time_isSet) {
        obj.insert(QString("issuedTime"), ::OpenAPI::toJsonValue(m_issued_time));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_paid_time_isSet) {
        obj.insert(QString("paidTime"), ::OpenAPI::toJsonValue(m_paid_time));
    }
    if (m_payment_form_url_isSet) {
        obj.insert(QString("paymentFormUrl"), ::OpenAPI::toJsonValue(m_payment_form_url));
    }
    if (m_po_number_isSet) {
        obj.insert(QString("poNumber"), ::OpenAPI::toJsonValue(m_po_number));
    }
    if (m_shipping.isSet()) {
        obj.insert(QString("shipping"), ::OpenAPI::toJsonValue(m_shipping));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscription_id_isSet) {
        obj.insert(QString("subscriptionId"), ::OpenAPI::toJsonValue(m_subscription_id));
    }
    if (m_subtotal_amount_isSet) {
        obj.insert(QString("subtotalAmount"), ::OpenAPI::toJsonValue(m_subtotal_amount));
    }
    if (m_tax.isSet()) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_voided_time_isSet) {
        obj.insert(QString("voidedTime"), ::OpenAPI::toJsonValue(m_voided_time));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_due_reminder_number_isSet) {
        obj.insert(QString("dueReminderNumber"), ::OpenAPI::toJsonValue(m_due_reminder_number));
    }
    if (m_due_reminder_time_isSet) {
        obj.insert(QString("dueReminderTime"), ::OpenAPI::toJsonValue(m_due_reminder_time));
    }
    if (m_retry_instruction.isSet()) {
        obj.insert(QString("retryInstruction"), ::OpenAPI::toJsonValue(m_retry_instruction));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_transactions.size() > 0) {
        obj.insert(QString("transactions"), ::OpenAPI::toJsonValue(m_transactions));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QDateTime OAIInvoice::getAbandonedTime() const {
    return m_abandoned_time;
}
void OAIInvoice::setAbandonedTime(const QDateTime &abandoned_time) {
    m_abandoned_time = abandoned_time;
    m_abandoned_time_isSet = true;
}

bool OAIInvoice::is_abandoned_time_Set() const{
    return m_abandoned_time_isSet;
}

bool OAIInvoice::is_abandoned_time_Valid() const{
    return m_abandoned_time_isValid;
}

double OAIInvoice::getAmount() const {
    return m_amount;
}
void OAIInvoice::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIInvoice::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIInvoice::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAIInvoice::getAmountDue() const {
    return m_amount_due;
}
void OAIInvoice::setAmountDue(const double &amount_due) {
    m_amount_due = amount_due;
    m_amount_due_isSet = true;
}

bool OAIInvoice::is_amount_due_Set() const{
    return m_amount_due_isSet;
}

bool OAIInvoice::is_amount_due_Valid() const{
    return m_amount_due_isValid;
}

qint32 OAIInvoice::getAutopayRetryNumber() const {
    return m_autopay_retry_number;
}
void OAIInvoice::setAutopayRetryNumber(const qint32 &autopay_retry_number) {
    m_autopay_retry_number = autopay_retry_number;
    m_autopay_retry_number_isSet = true;
}

bool OAIInvoice::is_autopay_retry_number_Set() const{
    return m_autopay_retry_number_isSet;
}

bool OAIInvoice::is_autopay_retry_number_Valid() const{
    return m_autopay_retry_number_isValid;
}

QDateTime OAIInvoice::getAutopayScheduledTime() const {
    return m_autopay_scheduled_time;
}
void OAIInvoice::setAutopayScheduledTime(const QDateTime &autopay_scheduled_time) {
    m_autopay_scheduled_time = autopay_scheduled_time;
    m_autopay_scheduled_time_isSet = true;
}

bool OAIInvoice::is_autopay_scheduled_time_Set() const{
    return m_autopay_scheduled_time_isSet;
}

bool OAIInvoice::is_autopay_scheduled_time_Valid() const{
    return m_autopay_scheduled_time_isValid;
}

OAIContactObject OAIInvoice::getBillingAddress() const {
    return m_billing_address;
}
void OAIInvoice::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIInvoice::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIInvoice::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

qint32 OAIInvoice::getCollectionPeriod() const {
    return m_collection_period;
}
void OAIInvoice::setCollectionPeriod(const qint32 &collection_period) {
    m_collection_period = collection_period;
    m_collection_period_isSet = true;
}

bool OAIInvoice::is_collection_period_Set() const{
    return m_collection_period_isSet;
}

bool OAIInvoice::is_collection_period_Valid() const{
    return m_collection_period_isValid;
}

QDateTime OAIInvoice::getCreatedTime() const {
    return m_created_time;
}
void OAIInvoice::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIInvoice::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIInvoice::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIInvoice::getCurrency() const {
    return m_currency;
}
void OAIInvoice::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIInvoice::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIInvoice::is_currency_Valid() const{
    return m_currency_isValid;
}

qint32 OAIInvoice::getDelinquentCollectionPeriod() const {
    return m_delinquent_collection_period;
}
void OAIInvoice::setDelinquentCollectionPeriod(const qint32 &delinquent_collection_period) {
    m_delinquent_collection_period = delinquent_collection_period;
    m_delinquent_collection_period_isSet = true;
}

bool OAIInvoice::is_delinquent_collection_period_Set() const{
    return m_delinquent_collection_period_isSet;
}

bool OAIInvoice::is_delinquent_collection_period_Valid() const{
    return m_delinquent_collection_period_isValid;
}

OAIContactObject OAIInvoice::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAIInvoice::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAIInvoice::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAIInvoice::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

double OAIInvoice::getDiscountAmount() const {
    return m_discount_amount;
}
void OAIInvoice::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAIInvoice::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAIInvoice::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

QList<OAIInvoiceDiscount> OAIInvoice::getDiscounts() const {
    return m_discounts;
}
void OAIInvoice::setDiscounts(const QList<OAIInvoiceDiscount> &discounts) {
    m_discounts = discounts;
    m_discounts_isSet = true;
}

bool OAIInvoice::is_discounts_Set() const{
    return m_discounts_isSet;
}

bool OAIInvoice::is_discounts_Valid() const{
    return m_discounts_isValid;
}

QDateTime OAIInvoice::getDueTime() const {
    return m_due_time;
}
void OAIInvoice::setDueTime(const QDateTime &due_time) {
    m_due_time = due_time;
    m_due_time_isSet = true;
}

bool OAIInvoice::is_due_time_Set() const{
    return m_due_time_isSet;
}

bool OAIInvoice::is_due_time_Valid() const{
    return m_due_time_isValid;
}

QString OAIInvoice::getId() const {
    return m_id;
}
void OAIInvoice::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoice::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoice::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIInvoice::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAIInvoice::setInvoiceNumber(const qint32 &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAIInvoice::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAIInvoice::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

QDateTime OAIInvoice::getIssuedTime() const {
    return m_issued_time;
}
void OAIInvoice::setIssuedTime(const QDateTime &issued_time) {
    m_issued_time = issued_time;
    m_issued_time_isSet = true;
}

bool OAIInvoice::is_issued_time_Set() const{
    return m_issued_time_isSet;
}

bool OAIInvoice::is_issued_time_Valid() const{
    return m_issued_time_isValid;
}

QList<OAIInvoiceItem> OAIInvoice::getItems() const {
    return m_items;
}
void OAIInvoice::setItems(const QList<OAIInvoiceItem> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIInvoice::is_items_Set() const{
    return m_items_isSet;
}

bool OAIInvoice::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIInvoice::getNotes() const {
    return m_notes;
}
void OAIInvoice::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIInvoice::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIInvoice::is_notes_Valid() const{
    return m_notes_isValid;
}

QDateTime OAIInvoice::getPaidTime() const {
    return m_paid_time;
}
void OAIInvoice::setPaidTime(const QDateTime &paid_time) {
    m_paid_time = paid_time;
    m_paid_time_isSet = true;
}

bool OAIInvoice::is_paid_time_Set() const{
    return m_paid_time_isSet;
}

bool OAIInvoice::is_paid_time_Valid() const{
    return m_paid_time_isValid;
}

QString OAIInvoice::getPaymentFormUrl() const {
    return m_payment_form_url;
}
void OAIInvoice::setPaymentFormUrl(const QString &payment_form_url) {
    m_payment_form_url = payment_form_url;
    m_payment_form_url_isSet = true;
}

bool OAIInvoice::is_payment_form_url_Set() const{
    return m_payment_form_url_isSet;
}

bool OAIInvoice::is_payment_form_url_Valid() const{
    return m_payment_form_url_isValid;
}

QString OAIInvoice::getPoNumber() const {
    return m_po_number;
}
void OAIInvoice::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAIInvoice::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAIInvoice::is_po_number_Valid() const{
    return m_po_number_isValid;
}

OAIInvoiceShipping OAIInvoice::getShipping() const {
    return m_shipping;
}
void OAIInvoice::setShipping(const OAIInvoiceShipping &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAIInvoice::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAIInvoice::is_shipping_Valid() const{
    return m_shipping_isValid;
}

QString OAIInvoice::getStatus() const {
    return m_status;
}
void OAIInvoice::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIInvoice::is_status_Set() const{
    return m_status_isSet;
}

bool OAIInvoice::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIInvoice::getSubscriptionId() const {
    return m_subscription_id;
}
void OAIInvoice::setSubscriptionId(const QString &subscription_id) {
    m_subscription_id = subscription_id;
    m_subscription_id_isSet = true;
}

bool OAIInvoice::is_subscription_id_Set() const{
    return m_subscription_id_isSet;
}

bool OAIInvoice::is_subscription_id_Valid() const{
    return m_subscription_id_isValid;
}

double OAIInvoice::getSubtotalAmount() const {
    return m_subtotal_amount;
}
void OAIInvoice::setSubtotalAmount(const double &subtotal_amount) {
    m_subtotal_amount = subtotal_amount;
    m_subtotal_amount_isSet = true;
}

bool OAIInvoice::is_subtotal_amount_Set() const{
    return m_subtotal_amount_isSet;
}

bool OAIInvoice::is_subtotal_amount_Valid() const{
    return m_subtotal_amount_isValid;
}

OAIInvoiceTax OAIInvoice::getTax() const {
    return m_tax;
}
void OAIInvoice::setTax(const OAIInvoiceTax &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIInvoice::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIInvoice::is_tax_Valid() const{
    return m_tax_isValid;
}

QDateTime OAIInvoice::getUpdatedTime() const {
    return m_updated_time;
}
void OAIInvoice::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIInvoice::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIInvoice::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QDateTime OAIInvoice::getVoidedTime() const {
    return m_voided_time;
}
void OAIInvoice::setVoidedTime(const QDateTime &voided_time) {
    m_voided_time = voided_time;
    m_voided_time_isSet = true;
}

bool OAIInvoice::is_voided_time_Set() const{
    return m_voided_time_isSet;
}

bool OAIInvoice::is_voided_time_Valid() const{
    return m_voided_time_isValid;
}

QString OAIInvoice::getWebsiteId() const {
    return m_website_id;
}
void OAIInvoice::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAIInvoice::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAIInvoice::is_website_id_Valid() const{
    return m_website_id_isValid;
}

QList<OAIInvoice_allOf__embedded> OAIInvoice::getEmbedded() const {
    return m__embedded;
}
void OAIInvoice::setEmbedded(const QList<OAIInvoice_allOf__embedded> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAIInvoice::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAIInvoice::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAIInvoice_allOf__links> OAIInvoice::getLinks() const {
    return m__links;
}
void OAIInvoice::setLinks(const QList<OAIInvoice_allOf__links> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIInvoice::is__links_Set() const{
    return m__links_isSet;
}

bool OAIInvoice::is__links_Valid() const{
    return m__links_isValid;
}

QString OAIInvoice::getCustomerId() const {
    return m_customer_id;
}
void OAIInvoice::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIInvoice::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIInvoice::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

qint32 OAIInvoice::getDueReminderNumber() const {
    return m_due_reminder_number;
}
void OAIInvoice::setDueReminderNumber(const qint32 &due_reminder_number) {
    m_due_reminder_number = due_reminder_number;
    m_due_reminder_number_isSet = true;
}

bool OAIInvoice::is_due_reminder_number_Set() const{
    return m_due_reminder_number_isSet;
}

bool OAIInvoice::is_due_reminder_number_Valid() const{
    return m_due_reminder_number_isValid;
}

QDateTime OAIInvoice::getDueReminderTime() const {
    return m_due_reminder_time;
}
void OAIInvoice::setDueReminderTime(const QDateTime &due_reminder_time) {
    m_due_reminder_time = due_reminder_time;
    m_due_reminder_time_isSet = true;
}

bool OAIInvoice::is_due_reminder_time_Set() const{
    return m_due_reminder_time_isSet;
}

bool OAIInvoice::is_due_reminder_time_Valid() const{
    return m_due_reminder_time_isValid;
}

OAIInvoice_allOf_retryInstruction OAIInvoice::getRetryInstruction() const {
    return m_retry_instruction;
}
void OAIInvoice::setRetryInstruction(const OAIInvoice_allOf_retryInstruction &retry_instruction) {
    m_retry_instruction = retry_instruction;
    m_retry_instruction_isSet = true;
}

bool OAIInvoice::is_retry_instruction_Set() const{
    return m_retry_instruction_isSet;
}

bool OAIInvoice::is_retry_instruction_Valid() const{
    return m_retry_instruction_isValid;
}

qint32 OAIInvoice::getRevision() const {
    return m_revision;
}
void OAIInvoice::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAIInvoice::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAIInvoice::is_revision_Valid() const{
    return m_revision_isValid;
}

QList<OAITransaction> OAIInvoice::getTransactions() const {
    return m_transactions;
}
void OAIInvoice::setTransactions(const QList<OAITransaction> &transactions) {
    m_transactions = transactions;
    m_transactions_isSet = true;
}

bool OAIInvoice::is_transactions_Set() const{
    return m_transactions_isSet;
}

bool OAIInvoice::is_transactions_Valid() const{
    return m_transactions_isValid;
}

QString OAIInvoice::getType() const {
    return m_type;
}
void OAIInvoice::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIInvoice::is_type_Set() const{
    return m_type_isSet;
}

bool OAIInvoice::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIInvoice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_abandoned_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_due_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_autopay_retry_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_autopay_scheduled_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_collection_period_isSet) {
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

        if (m_delinquent_collection_period_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issued_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_paid_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_form_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subtotal_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_voided_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_id_isSet) {
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

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_reminder_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_reminder_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_instruction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInvoice::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_currency_isValid && m_website_id_isValid && m_customer_id_isValid && true;
}

} // namespace OpenAPI
