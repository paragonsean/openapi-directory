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

#include "OAICommonSubscriptionOrder.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommonSubscriptionOrder::OAICommonSubscriptionOrder(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommonSubscriptionOrder::OAICommonSubscriptionOrder() {
    this->initializeModel();
}

OAICommonSubscriptionOrder::~OAICommonSubscriptionOrder() {}

void OAICommonSubscriptionOrder::initializeModel() {

    m_activation_time_isSet = false;
    m_activation_time_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_billing_status_isSet = false;
    m_billing_status_isValid = false;

    m_coupon_ids_isSet = false;
    m_coupon_ids_isValid = false;

    m_delivery_address_isSet = false;
    m_delivery_address_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_initial_invoice_id_isSet = false;
    m_initial_invoice_id_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_order_type_isSet = false;
    m_order_type_isValid = false;

    m_po_number_isSet = false;
    m_po_number_isValid = false;

    m_recent_invoice_id_isSet = false;
    m_recent_invoice_id_isValid = false;

    m_void_time_isSet = false;
    m_void_time_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;

    m_autopay_isSet = false;
    m_autopay_isValid = false;

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_in_trial_isSet = false;
    m_in_trial_isValid = false;

    m_invoice_time_shift_isSet = false;
    m_invoice_time_shift_isValid = false;

    m_is_trial_only_isSet = false;
    m_is_trial_only_isValid = false;

    m_line_item_subtotal_isSet = false;
    m_line_item_subtotal_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_rebill_number_isSet = false;
    m_rebill_number_isValid = false;

    m_recurring_interval_isSet = false;
    m_recurring_interval_isValid = false;

    m_renewal_time_isSet = false;
    m_renewal_time_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_trial_isSet = false;
    m_trial_isValid = false;
}

void OAICommonSubscriptionOrder::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommonSubscriptionOrder::fromJsonObject(QJsonObject json) {

    m_activation_time_isValid = ::OpenAPI::fromJsonValue(m_activation_time, json[QString("activationTime")]);
    m_activation_time_isSet = !json[QString("activationTime")].isNull() && m_activation_time_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_billing_status_isValid = ::OpenAPI::fromJsonValue(m_billing_status, json[QString("billingStatus")]);
    m_billing_status_isSet = !json[QString("billingStatus")].isNull() && m_billing_status_isValid;

    m_coupon_ids_isValid = ::OpenAPI::fromJsonValue(m_coupon_ids, json[QString("couponIds")]);
    m_coupon_ids_isSet = !json[QString("couponIds")].isNull() && m_coupon_ids_isValid;

    m_delivery_address_isValid = ::OpenAPI::fromJsonValue(m_delivery_address, json[QString("deliveryAddress")]);
    m_delivery_address_isSet = !json[QString("deliveryAddress")].isNull() && m_delivery_address_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_initial_invoice_id_isValid = ::OpenAPI::fromJsonValue(m_initial_invoice_id, json[QString("initialInvoiceId")]);
    m_initial_invoice_id_isSet = !json[QString("initialInvoiceId")].isNull() && m_initial_invoice_id_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_order_type_isValid = ::OpenAPI::fromJsonValue(m_order_type, json[QString("orderType")]);
    m_order_type_isSet = !json[QString("orderType")].isNull() && m_order_type_isValid;

    m_po_number_isValid = ::OpenAPI::fromJsonValue(m_po_number, json[QString("poNumber")]);
    m_po_number_isSet = !json[QString("poNumber")].isNull() && m_po_number_isValid;

    m_recent_invoice_id_isValid = ::OpenAPI::fromJsonValue(m_recent_invoice_id, json[QString("recentInvoiceId")]);
    m_recent_invoice_id_isSet = !json[QString("recentInvoiceId")].isNull() && m_recent_invoice_id_isValid;

    m_void_time_isValid = ::OpenAPI::fromJsonValue(m_void_time, json[QString("voidTime")]);
    m_void_time_isSet = !json[QString("voidTime")].isNull() && m_void_time_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;

    m_autopay_isValid = ::OpenAPI::fromJsonValue(m_autopay, json[QString("autopay")]);
    m_autopay_isSet = !json[QString("autopay")].isNull() && m_autopay_isValid;

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_in_trial_isValid = ::OpenAPI::fromJsonValue(m_in_trial, json[QString("inTrial")]);
    m_in_trial_isSet = !json[QString("inTrial")].isNull() && m_in_trial_isValid;

    m_invoice_time_shift_isValid = ::OpenAPI::fromJsonValue(m_invoice_time_shift, json[QString("invoiceTimeShift")]);
    m_invoice_time_shift_isSet = !json[QString("invoiceTimeShift")].isNull() && m_invoice_time_shift_isValid;

    m_is_trial_only_isValid = ::OpenAPI::fromJsonValue(m_is_trial_only, json[QString("isTrialOnly")]);
    m_is_trial_only_isSet = !json[QString("isTrialOnly")].isNull() && m_is_trial_only_isValid;

    m_line_item_subtotal_isValid = ::OpenAPI::fromJsonValue(m_line_item_subtotal, json[QString("lineItemSubtotal")]);
    m_line_item_subtotal_isSet = !json[QString("lineItemSubtotal")].isNull() && m_line_item_subtotal_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("lineItems")]);
    m_line_items_isSet = !json[QString("lineItems")].isNull() && m_line_items_isValid;

    m_rebill_number_isValid = ::OpenAPI::fromJsonValue(m_rebill_number, json[QString("rebillNumber")]);
    m_rebill_number_isSet = !json[QString("rebillNumber")].isNull() && m_rebill_number_isValid;

    m_recurring_interval_isValid = ::OpenAPI::fromJsonValue(m_recurring_interval, json[QString("recurringInterval")]);
    m_recurring_interval_isSet = !json[QString("recurringInterval")].isNull() && m_recurring_interval_isValid;

    m_renewal_time_isValid = ::OpenAPI::fromJsonValue(m_renewal_time, json[QString("renewalTime")]);
    m_renewal_time_isSet = !json[QString("renewalTime")].isNull() && m_renewal_time_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_trial_isValid = ::OpenAPI::fromJsonValue(m_trial, json[QString("trial")]);
    m_trial_isSet = !json[QString("trial")].isNull() && m_trial_isValid;
}

QString OAICommonSubscriptionOrder::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommonSubscriptionOrder::asJsonObject() const {
    QJsonObject obj;
    if (m_activation_time_isSet) {
        obj.insert(QString("activationTime"), ::OpenAPI::toJsonValue(m_activation_time));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_billing_status_isSet) {
        obj.insert(QString("billingStatus"), ::OpenAPI::toJsonValue(m_billing_status));
    }
    if (m_coupon_ids.size() > 0) {
        obj.insert(QString("couponIds"), ::OpenAPI::toJsonValue(m_coupon_ids));
    }
    if (m_delivery_address.isSet()) {
        obj.insert(QString("deliveryAddress"), ::OpenAPI::toJsonValue(m_delivery_address));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_initial_invoice_id_isSet) {
        obj.insert(QString("initialInvoiceId"), ::OpenAPI::toJsonValue(m_initial_invoice_id));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_order_type_isSet) {
        obj.insert(QString("orderType"), ::OpenAPI::toJsonValue(m_order_type));
    }
    if (m_po_number_isSet) {
        obj.insert(QString("poNumber"), ::OpenAPI::toJsonValue(m_po_number));
    }
    if (m_recent_invoice_id_isSet) {
        obj.insert(QString("recentInvoiceId"), ::OpenAPI::toJsonValue(m_recent_invoice_id));
    }
    if (m_void_time_isSet) {
        obj.insert(QString("voidTime"), ::OpenAPI::toJsonValue(m_void_time));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    if (m_autopay_isSet) {
        obj.insert(QString("autopay"), ::OpenAPI::toJsonValue(m_autopay));
    }
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_in_trial_isSet) {
        obj.insert(QString("inTrial"), ::OpenAPI::toJsonValue(m_in_trial));
    }
    if (m_invoice_time_shift.isSet()) {
        obj.insert(QString("invoiceTimeShift"), ::OpenAPI::toJsonValue(m_invoice_time_shift));
    }
    if (m_is_trial_only_isSet) {
        obj.insert(QString("isTrialOnly"), ::OpenAPI::toJsonValue(m_is_trial_only));
    }
    if (m_line_item_subtotal.isSet()) {
        obj.insert(QString("lineItemSubtotal"), ::OpenAPI::toJsonValue(m_line_item_subtotal));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("lineItems"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_rebill_number_isSet) {
        obj.insert(QString("rebillNumber"), ::OpenAPI::toJsonValue(m_rebill_number));
    }
    if (m_recurring_interval.isSet()) {
        obj.insert(QString("recurringInterval"), ::OpenAPI::toJsonValue(m_recurring_interval));
    }
    if (m_renewal_time_isSet) {
        obj.insert(QString("renewalTime"), ::OpenAPI::toJsonValue(m_renewal_time));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_trial.isSet()) {
        obj.insert(QString("trial"), ::OpenAPI::toJsonValue(m_trial));
    }
    return obj;
}

QDateTime OAICommonSubscriptionOrder::getActivationTime() const {
    return m_activation_time;
}
void OAICommonSubscriptionOrder::setActivationTime(const QDateTime &activation_time) {
    m_activation_time = activation_time;
    m_activation_time_isSet = true;
}

bool OAICommonSubscriptionOrder::is_activation_time_Set() const{
    return m_activation_time_isSet;
}

bool OAICommonSubscriptionOrder::is_activation_time_Valid() const{
    return m_activation_time_isValid;
}

OAIContactObject OAICommonSubscriptionOrder::getBillingAddress() const {
    return m_billing_address;
}
void OAICommonSubscriptionOrder::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICommonSubscriptionOrder::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICommonSubscriptionOrder::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAICommonSubscriptionOrder::getBillingStatus() const {
    return m_billing_status;
}
void OAICommonSubscriptionOrder::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAICommonSubscriptionOrder::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAICommonSubscriptionOrder::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

QList<QString> OAICommonSubscriptionOrder::getCouponIds() const {
    return m_coupon_ids;
}
void OAICommonSubscriptionOrder::setCouponIds(const QList<QString> &coupon_ids) {
    m_coupon_ids = coupon_ids;
    m_coupon_ids_isSet = true;
}

bool OAICommonSubscriptionOrder::is_coupon_ids_Set() const{
    return m_coupon_ids_isSet;
}

bool OAICommonSubscriptionOrder::is_coupon_ids_Valid() const{
    return m_coupon_ids_isValid;
}

OAIContactObject OAICommonSubscriptionOrder::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAICommonSubscriptionOrder::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAICommonSubscriptionOrder::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAICommonSubscriptionOrder::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

QString OAICommonSubscriptionOrder::getId() const {
    return m_id;
}
void OAICommonSubscriptionOrder::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICommonSubscriptionOrder::is_id_Set() const{
    return m_id_isSet;
}

bool OAICommonSubscriptionOrder::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICommonSubscriptionOrder::getInitialInvoiceId() const {
    return m_initial_invoice_id;
}
void OAICommonSubscriptionOrder::setInitialInvoiceId(const QString &initial_invoice_id) {
    m_initial_invoice_id = initial_invoice_id;
    m_initial_invoice_id_isSet = true;
}

bool OAICommonSubscriptionOrder::is_initial_invoice_id_Set() const{
    return m_initial_invoice_id_isSet;
}

bool OAICommonSubscriptionOrder::is_initial_invoice_id_Valid() const{
    return m_initial_invoice_id_isValid;
}

QList<OAICommonSubscription_items_inner> OAICommonSubscriptionOrder::getItems() const {
    return m_items;
}
void OAICommonSubscriptionOrder::setItems(const QList<OAICommonSubscription_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAICommonSubscriptionOrder::is_items_Set() const{
    return m_items_isSet;
}

bool OAICommonSubscriptionOrder::is_items_Valid() const{
    return m_items_isValid;
}

QString OAICommonSubscriptionOrder::getOrderType() const {
    return m_order_type;
}
void OAICommonSubscriptionOrder::setOrderType(const QString &order_type) {
    m_order_type = order_type;
    m_order_type_isSet = true;
}

bool OAICommonSubscriptionOrder::is_order_type_Set() const{
    return m_order_type_isSet;
}

bool OAICommonSubscriptionOrder::is_order_type_Valid() const{
    return m_order_type_isValid;
}

QString OAICommonSubscriptionOrder::getPoNumber() const {
    return m_po_number;
}
void OAICommonSubscriptionOrder::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAICommonSubscriptionOrder::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAICommonSubscriptionOrder::is_po_number_Valid() const{
    return m_po_number_isValid;
}

QString OAICommonSubscriptionOrder::getRecentInvoiceId() const {
    return m_recent_invoice_id;
}
void OAICommonSubscriptionOrder::setRecentInvoiceId(const QString &recent_invoice_id) {
    m_recent_invoice_id = recent_invoice_id;
    m_recent_invoice_id_isSet = true;
}

bool OAICommonSubscriptionOrder::is_recent_invoice_id_Set() const{
    return m_recent_invoice_id_isSet;
}

bool OAICommonSubscriptionOrder::is_recent_invoice_id_Valid() const{
    return m_recent_invoice_id_isValid;
}

QDateTime OAICommonSubscriptionOrder::getVoidTime() const {
    return m_void_time;
}
void OAICommonSubscriptionOrder::setVoidTime(const QDateTime &void_time) {
    m_void_time = void_time;
    m_void_time_isSet = true;
}

bool OAICommonSubscriptionOrder::is_void_time_Set() const{
    return m_void_time_isSet;
}

bool OAICommonSubscriptionOrder::is_void_time_Valid() const{
    return m_void_time_isValid;
}

QString OAICommonSubscriptionOrder::getWebsiteId() const {
    return m_website_id;
}
void OAICommonSubscriptionOrder::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICommonSubscriptionOrder::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICommonSubscriptionOrder::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICommonSubscriptionOrder::isAutopay() const {
    return m_autopay;
}
void OAICommonSubscriptionOrder::setAutopay(const bool &autopay) {
    m_autopay = autopay;
    m_autopay_isSet = true;
}

bool OAICommonSubscriptionOrder::is_autopay_Set() const{
    return m_autopay_isSet;
}

bool OAICommonSubscriptionOrder::is_autopay_Valid() const{
    return m_autopay_isValid;
}

QDateTime OAICommonSubscriptionOrder::getEndTime() const {
    return m_end_time;
}
void OAICommonSubscriptionOrder::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAICommonSubscriptionOrder::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAICommonSubscriptionOrder::is_end_time_Valid() const{
    return m_end_time_isValid;
}

bool OAICommonSubscriptionOrder::isInTrial() const {
    return m_in_trial;
}
void OAICommonSubscriptionOrder::setInTrial(const bool &in_trial) {
    m_in_trial = in_trial;
    m_in_trial_isSet = true;
}

bool OAICommonSubscriptionOrder::is_in_trial_Set() const{
    return m_in_trial_isSet;
}

bool OAICommonSubscriptionOrder::is_in_trial_Valid() const{
    return m_in_trial_isValid;
}

OAIInvoiceTimeShift OAICommonSubscriptionOrder::getInvoiceTimeShift() const {
    return m_invoice_time_shift;
}
void OAICommonSubscriptionOrder::setInvoiceTimeShift(const OAIInvoiceTimeShift &invoice_time_shift) {
    m_invoice_time_shift = invoice_time_shift;
    m_invoice_time_shift_isSet = true;
}

bool OAICommonSubscriptionOrder::is_invoice_time_shift_Set() const{
    return m_invoice_time_shift_isSet;
}

bool OAICommonSubscriptionOrder::is_invoice_time_shift_Valid() const{
    return m_invoice_time_shift_isValid;
}

bool OAICommonSubscriptionOrder::isIsTrialOnly() const {
    return m_is_trial_only;
}
void OAICommonSubscriptionOrder::setIsTrialOnly(const bool &is_trial_only) {
    m_is_trial_only = is_trial_only;
    m_is_trial_only_isSet = true;
}

bool OAICommonSubscriptionOrder::is_is_trial_only_Set() const{
    return m_is_trial_only_isSet;
}

bool OAICommonSubscriptionOrder::is_is_trial_only_Valid() const{
    return m_is_trial_only_isValid;
}

OAICommonSubscriptionOrder_allOf_lineItemSubtotal OAICommonSubscriptionOrder::getLineItemSubtotal() const {
    return m_line_item_subtotal;
}
void OAICommonSubscriptionOrder::setLineItemSubtotal(const OAICommonSubscriptionOrder_allOf_lineItemSubtotal &line_item_subtotal) {
    m_line_item_subtotal = line_item_subtotal;
    m_line_item_subtotal_isSet = true;
}

bool OAICommonSubscriptionOrder::is_line_item_subtotal_Set() const{
    return m_line_item_subtotal_isSet;
}

bool OAICommonSubscriptionOrder::is_line_item_subtotal_Valid() const{
    return m_line_item_subtotal_isValid;
}

QList<OAIUpcomingInvoiceItem> OAICommonSubscriptionOrder::getLineItems() const {
    return m_line_items;
}
void OAICommonSubscriptionOrder::setLineItems(const QList<OAIUpcomingInvoiceItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAICommonSubscriptionOrder::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAICommonSubscriptionOrder::is_line_items_Valid() const{
    return m_line_items_isValid;
}

qint32 OAICommonSubscriptionOrder::getRebillNumber() const {
    return m_rebill_number;
}
void OAICommonSubscriptionOrder::setRebillNumber(const qint32 &rebill_number) {
    m_rebill_number = rebill_number;
    m_rebill_number_isSet = true;
}

bool OAICommonSubscriptionOrder::is_rebill_number_Set() const{
    return m_rebill_number_isSet;
}

bool OAICommonSubscriptionOrder::is_rebill_number_Valid() const{
    return m_rebill_number_isValid;
}

OAICommonSubscriptionOrder_allOf_recurringInterval OAICommonSubscriptionOrder::getRecurringInterval() const {
    return m_recurring_interval;
}
void OAICommonSubscriptionOrder::setRecurringInterval(const OAICommonSubscriptionOrder_allOf_recurringInterval &recurring_interval) {
    m_recurring_interval = recurring_interval;
    m_recurring_interval_isSet = true;
}

bool OAICommonSubscriptionOrder::is_recurring_interval_Set() const{
    return m_recurring_interval_isSet;
}

bool OAICommonSubscriptionOrder::is_recurring_interval_Valid() const{
    return m_recurring_interval_isValid;
}

QDateTime OAICommonSubscriptionOrder::getRenewalTime() const {
    return m_renewal_time;
}
void OAICommonSubscriptionOrder::setRenewalTime(const QDateTime &renewal_time) {
    m_renewal_time = renewal_time;
    m_renewal_time_isSet = true;
}

bool OAICommonSubscriptionOrder::is_renewal_time_Set() const{
    return m_renewal_time_isSet;
}

bool OAICommonSubscriptionOrder::is_renewal_time_Valid() const{
    return m_renewal_time_isValid;
}

QDateTime OAICommonSubscriptionOrder::getStartTime() const {
    return m_start_time;
}
void OAICommonSubscriptionOrder::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAICommonSubscriptionOrder::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAICommonSubscriptionOrder::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAICommonSubscriptionOrder::getStatus() const {
    return m_status;
}
void OAICommonSubscriptionOrder::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICommonSubscriptionOrder::is_status_Set() const{
    return m_status_isSet;
}

bool OAICommonSubscriptionOrder::is_status_Valid() const{
    return m_status_isValid;
}

OAICommonSubscriptionOrder_allOf_trial OAICommonSubscriptionOrder::getTrial() const {
    return m_trial;
}
void OAICommonSubscriptionOrder::setTrial(const OAICommonSubscriptionOrder_allOf_trial &trial) {
    m_trial = trial;
    m_trial_isSet = true;
}

bool OAICommonSubscriptionOrder::is_trial_Set() const{
    return m_trial_isSet;
}

bool OAICommonSubscriptionOrder::is_trial_Valid() const{
    return m_trial_isValid;
}

bool OAICommonSubscriptionOrder::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activation_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coupon_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_initial_invoice_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recent_invoice_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_void_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_autopay_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_in_trial_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_time_shift.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_trial_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_item_subtotal.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rebill_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_interval.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_renewal_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommonSubscriptionOrder::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
