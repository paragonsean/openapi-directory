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

#include "OAICommonInvoice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommonInvoice::OAICommonInvoice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommonInvoice::OAICommonInvoice() {
    this->initializeModel();
}

OAICommonInvoice::~OAICommonInvoice() {}

void OAICommonInvoice::initializeModel() {

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
}

void OAICommonInvoice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommonInvoice::fromJsonObject(QJsonObject json) {

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
}

QString OAICommonInvoice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommonInvoice::asJsonObject() const {
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
    return obj;
}

QDateTime OAICommonInvoice::getAbandonedTime() const {
    return m_abandoned_time;
}
void OAICommonInvoice::setAbandonedTime(const QDateTime &abandoned_time) {
    m_abandoned_time = abandoned_time;
    m_abandoned_time_isSet = true;
}

bool OAICommonInvoice::is_abandoned_time_Set() const{
    return m_abandoned_time_isSet;
}

bool OAICommonInvoice::is_abandoned_time_Valid() const{
    return m_abandoned_time_isValid;
}

double OAICommonInvoice::getAmount() const {
    return m_amount;
}
void OAICommonInvoice::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAICommonInvoice::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAICommonInvoice::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAICommonInvoice::getAmountDue() const {
    return m_amount_due;
}
void OAICommonInvoice::setAmountDue(const double &amount_due) {
    m_amount_due = amount_due;
    m_amount_due_isSet = true;
}

bool OAICommonInvoice::is_amount_due_Set() const{
    return m_amount_due_isSet;
}

bool OAICommonInvoice::is_amount_due_Valid() const{
    return m_amount_due_isValid;
}

qint32 OAICommonInvoice::getAutopayRetryNumber() const {
    return m_autopay_retry_number;
}
void OAICommonInvoice::setAutopayRetryNumber(const qint32 &autopay_retry_number) {
    m_autopay_retry_number = autopay_retry_number;
    m_autopay_retry_number_isSet = true;
}

bool OAICommonInvoice::is_autopay_retry_number_Set() const{
    return m_autopay_retry_number_isSet;
}

bool OAICommonInvoice::is_autopay_retry_number_Valid() const{
    return m_autopay_retry_number_isValid;
}

QDateTime OAICommonInvoice::getAutopayScheduledTime() const {
    return m_autopay_scheduled_time;
}
void OAICommonInvoice::setAutopayScheduledTime(const QDateTime &autopay_scheduled_time) {
    m_autopay_scheduled_time = autopay_scheduled_time;
    m_autopay_scheduled_time_isSet = true;
}

bool OAICommonInvoice::is_autopay_scheduled_time_Set() const{
    return m_autopay_scheduled_time_isSet;
}

bool OAICommonInvoice::is_autopay_scheduled_time_Valid() const{
    return m_autopay_scheduled_time_isValid;
}

OAIContactObject OAICommonInvoice::getBillingAddress() const {
    return m_billing_address;
}
void OAICommonInvoice::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICommonInvoice::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICommonInvoice::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

qint32 OAICommonInvoice::getCollectionPeriod() const {
    return m_collection_period;
}
void OAICommonInvoice::setCollectionPeriod(const qint32 &collection_period) {
    m_collection_period = collection_period;
    m_collection_period_isSet = true;
}

bool OAICommonInvoice::is_collection_period_Set() const{
    return m_collection_period_isSet;
}

bool OAICommonInvoice::is_collection_period_Valid() const{
    return m_collection_period_isValid;
}

QDateTime OAICommonInvoice::getCreatedTime() const {
    return m_created_time;
}
void OAICommonInvoice::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAICommonInvoice::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAICommonInvoice::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAICommonInvoice::getCurrency() const {
    return m_currency;
}
void OAICommonInvoice::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAICommonInvoice::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAICommonInvoice::is_currency_Valid() const{
    return m_currency_isValid;
}

qint32 OAICommonInvoice::getDelinquentCollectionPeriod() const {
    return m_delinquent_collection_period;
}
void OAICommonInvoice::setDelinquentCollectionPeriod(const qint32 &delinquent_collection_period) {
    m_delinquent_collection_period = delinquent_collection_period;
    m_delinquent_collection_period_isSet = true;
}

bool OAICommonInvoice::is_delinquent_collection_period_Set() const{
    return m_delinquent_collection_period_isSet;
}

bool OAICommonInvoice::is_delinquent_collection_period_Valid() const{
    return m_delinquent_collection_period_isValid;
}

OAIContactObject OAICommonInvoice::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAICommonInvoice::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAICommonInvoice::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAICommonInvoice::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

double OAICommonInvoice::getDiscountAmount() const {
    return m_discount_amount;
}
void OAICommonInvoice::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAICommonInvoice::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAICommonInvoice::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

QList<OAIInvoiceDiscount> OAICommonInvoice::getDiscounts() const {
    return m_discounts;
}
void OAICommonInvoice::setDiscounts(const QList<OAIInvoiceDiscount> &discounts) {
    m_discounts = discounts;
    m_discounts_isSet = true;
}

bool OAICommonInvoice::is_discounts_Set() const{
    return m_discounts_isSet;
}

bool OAICommonInvoice::is_discounts_Valid() const{
    return m_discounts_isValid;
}

QDateTime OAICommonInvoice::getDueTime() const {
    return m_due_time;
}
void OAICommonInvoice::setDueTime(const QDateTime &due_time) {
    m_due_time = due_time;
    m_due_time_isSet = true;
}

bool OAICommonInvoice::is_due_time_Set() const{
    return m_due_time_isSet;
}

bool OAICommonInvoice::is_due_time_Valid() const{
    return m_due_time_isValid;
}

QString OAICommonInvoice::getId() const {
    return m_id;
}
void OAICommonInvoice::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICommonInvoice::is_id_Set() const{
    return m_id_isSet;
}

bool OAICommonInvoice::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAICommonInvoice::getInvoiceNumber() const {
    return m_invoice_number;
}
void OAICommonInvoice::setInvoiceNumber(const qint32 &invoice_number) {
    m_invoice_number = invoice_number;
    m_invoice_number_isSet = true;
}

bool OAICommonInvoice::is_invoice_number_Set() const{
    return m_invoice_number_isSet;
}

bool OAICommonInvoice::is_invoice_number_Valid() const{
    return m_invoice_number_isValid;
}

QDateTime OAICommonInvoice::getIssuedTime() const {
    return m_issued_time;
}
void OAICommonInvoice::setIssuedTime(const QDateTime &issued_time) {
    m_issued_time = issued_time;
    m_issued_time_isSet = true;
}

bool OAICommonInvoice::is_issued_time_Set() const{
    return m_issued_time_isSet;
}

bool OAICommonInvoice::is_issued_time_Valid() const{
    return m_issued_time_isValid;
}

QList<OAIInvoiceItem> OAICommonInvoice::getItems() const {
    return m_items;
}
void OAICommonInvoice::setItems(const QList<OAIInvoiceItem> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAICommonInvoice::is_items_Set() const{
    return m_items_isSet;
}

bool OAICommonInvoice::is_items_Valid() const{
    return m_items_isValid;
}

QString OAICommonInvoice::getNotes() const {
    return m_notes;
}
void OAICommonInvoice::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAICommonInvoice::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAICommonInvoice::is_notes_Valid() const{
    return m_notes_isValid;
}

QDateTime OAICommonInvoice::getPaidTime() const {
    return m_paid_time;
}
void OAICommonInvoice::setPaidTime(const QDateTime &paid_time) {
    m_paid_time = paid_time;
    m_paid_time_isSet = true;
}

bool OAICommonInvoice::is_paid_time_Set() const{
    return m_paid_time_isSet;
}

bool OAICommonInvoice::is_paid_time_Valid() const{
    return m_paid_time_isValid;
}

QString OAICommonInvoice::getPaymentFormUrl() const {
    return m_payment_form_url;
}
void OAICommonInvoice::setPaymentFormUrl(const QString &payment_form_url) {
    m_payment_form_url = payment_form_url;
    m_payment_form_url_isSet = true;
}

bool OAICommonInvoice::is_payment_form_url_Set() const{
    return m_payment_form_url_isSet;
}

bool OAICommonInvoice::is_payment_form_url_Valid() const{
    return m_payment_form_url_isValid;
}

QString OAICommonInvoice::getPoNumber() const {
    return m_po_number;
}
void OAICommonInvoice::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAICommonInvoice::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAICommonInvoice::is_po_number_Valid() const{
    return m_po_number_isValid;
}

OAIInvoiceShipping OAICommonInvoice::getShipping() const {
    return m_shipping;
}
void OAICommonInvoice::setShipping(const OAIInvoiceShipping &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAICommonInvoice::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAICommonInvoice::is_shipping_Valid() const{
    return m_shipping_isValid;
}

QString OAICommonInvoice::getStatus() const {
    return m_status;
}
void OAICommonInvoice::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICommonInvoice::is_status_Set() const{
    return m_status_isSet;
}

bool OAICommonInvoice::is_status_Valid() const{
    return m_status_isValid;
}

QString OAICommonInvoice::getSubscriptionId() const {
    return m_subscription_id;
}
void OAICommonInvoice::setSubscriptionId(const QString &subscription_id) {
    m_subscription_id = subscription_id;
    m_subscription_id_isSet = true;
}

bool OAICommonInvoice::is_subscription_id_Set() const{
    return m_subscription_id_isSet;
}

bool OAICommonInvoice::is_subscription_id_Valid() const{
    return m_subscription_id_isValid;
}

double OAICommonInvoice::getSubtotalAmount() const {
    return m_subtotal_amount;
}
void OAICommonInvoice::setSubtotalAmount(const double &subtotal_amount) {
    m_subtotal_amount = subtotal_amount;
    m_subtotal_amount_isSet = true;
}

bool OAICommonInvoice::is_subtotal_amount_Set() const{
    return m_subtotal_amount_isSet;
}

bool OAICommonInvoice::is_subtotal_amount_Valid() const{
    return m_subtotal_amount_isValid;
}

OAIInvoiceTax OAICommonInvoice::getTax() const {
    return m_tax;
}
void OAICommonInvoice::setTax(const OAIInvoiceTax &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAICommonInvoice::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAICommonInvoice::is_tax_Valid() const{
    return m_tax_isValid;
}

QDateTime OAICommonInvoice::getUpdatedTime() const {
    return m_updated_time;
}
void OAICommonInvoice::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAICommonInvoice::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAICommonInvoice::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QDateTime OAICommonInvoice::getVoidedTime() const {
    return m_voided_time;
}
void OAICommonInvoice::setVoidedTime(const QDateTime &voided_time) {
    m_voided_time = voided_time;
    m_voided_time_isSet = true;
}

bool OAICommonInvoice::is_voided_time_Set() const{
    return m_voided_time_isSet;
}

bool OAICommonInvoice::is_voided_time_Valid() const{
    return m_voided_time_isValid;
}

QString OAICommonInvoice::getWebsiteId() const {
    return m_website_id;
}
void OAICommonInvoice::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICommonInvoice::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICommonInvoice::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICommonInvoice::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAICommonInvoice::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_currency_isValid && m_website_id_isValid && true;
}

} // namespace OpenAPI
