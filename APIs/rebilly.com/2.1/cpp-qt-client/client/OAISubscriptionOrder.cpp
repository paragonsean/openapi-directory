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

#include "OAISubscriptionOrder.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionOrder::OAISubscriptionOrder(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionOrder::OAISubscriptionOrder() {
    this->initializeModel();
}

OAISubscriptionOrder::~OAISubscriptionOrder() {}

void OAISubscriptionOrder::initializeModel() {

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

    m_cancel_category_isSet = false;
    m_cancel_category_isValid = false;

    m_cancel_description_isSet = false;
    m_cancel_description_isValid = false;

    m_canceled_by_isSet = false;
    m_canceled_by_isValid = false;

    m_canceled_time_isSet = false;
    m_canceled_time_isValid = false;

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_renewal_reminder_number_isSet = false;
    m_renewal_reminder_number_isValid = false;

    m_renewal_reminder_time_isSet = false;
    m_renewal_reminder_time_isValid = false;

    m_trial_reminder_number_isSet = false;
    m_trial_reminder_number_isValid = false;

    m_trial_reminder_time_isSet = false;
    m_trial_reminder_time_isValid = false;
}

void OAISubscriptionOrder::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionOrder::fromJsonObject(QJsonObject json) {

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

    m_cancel_category_isValid = ::OpenAPI::fromJsonValue(m_cancel_category, json[QString("cancelCategory")]);
    m_cancel_category_isSet = !json[QString("cancelCategory")].isNull() && m_cancel_category_isValid;

    m_cancel_description_isValid = ::OpenAPI::fromJsonValue(m_cancel_description, json[QString("cancelDescription")]);
    m_cancel_description_isSet = !json[QString("cancelDescription")].isNull() && m_cancel_description_isValid;

    m_canceled_by_isValid = ::OpenAPI::fromJsonValue(m_canceled_by, json[QString("canceledBy")]);
    m_canceled_by_isSet = !json[QString("canceledBy")].isNull() && m_canceled_by_isValid;

    m_canceled_time_isValid = ::OpenAPI::fromJsonValue(m_canceled_time, json[QString("canceledTime")]);
    m_canceled_time_isSet = !json[QString("canceledTime")].isNull() && m_canceled_time_isValid;

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_renewal_reminder_number_isValid = ::OpenAPI::fromJsonValue(m_renewal_reminder_number, json[QString("renewalReminderNumber")]);
    m_renewal_reminder_number_isSet = !json[QString("renewalReminderNumber")].isNull() && m_renewal_reminder_number_isValid;

    m_renewal_reminder_time_isValid = ::OpenAPI::fromJsonValue(m_renewal_reminder_time, json[QString("renewalReminderTime")]);
    m_renewal_reminder_time_isSet = !json[QString("renewalReminderTime")].isNull() && m_renewal_reminder_time_isValid;

    m_trial_reminder_number_isValid = ::OpenAPI::fromJsonValue(m_trial_reminder_number, json[QString("trialReminderNumber")]);
    m_trial_reminder_number_isSet = !json[QString("trialReminderNumber")].isNull() && m_trial_reminder_number_isValid;

    m_trial_reminder_time_isValid = ::OpenAPI::fromJsonValue(m_trial_reminder_time, json[QString("trialReminderTime")]);
    m_trial_reminder_time_isSet = !json[QString("trialReminderTime")].isNull() && m_trial_reminder_time_isValid;
}

QString OAISubscriptionOrder::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionOrder::asJsonObject() const {
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
    if (m_cancel_category_isSet) {
        obj.insert(QString("cancelCategory"), ::OpenAPI::toJsonValue(m_cancel_category));
    }
    if (m_cancel_description_isSet) {
        obj.insert(QString("cancelDescription"), ::OpenAPI::toJsonValue(m_cancel_description));
    }
    if (m_canceled_by_isSet) {
        obj.insert(QString("canceledBy"), ::OpenAPI::toJsonValue(m_canceled_by));
    }
    if (m_canceled_time_isSet) {
        obj.insert(QString("canceledTime"), ::OpenAPI::toJsonValue(m_canceled_time));
    }
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_renewal_reminder_number_isSet) {
        obj.insert(QString("renewalReminderNumber"), ::OpenAPI::toJsonValue(m_renewal_reminder_number));
    }
    if (m_renewal_reminder_time_isSet) {
        obj.insert(QString("renewalReminderTime"), ::OpenAPI::toJsonValue(m_renewal_reminder_time));
    }
    if (m_trial_reminder_number_isSet) {
        obj.insert(QString("trialReminderNumber"), ::OpenAPI::toJsonValue(m_trial_reminder_number));
    }
    if (m_trial_reminder_time_isSet) {
        obj.insert(QString("trialReminderTime"), ::OpenAPI::toJsonValue(m_trial_reminder_time));
    }
    return obj;
}

QDateTime OAISubscriptionOrder::getActivationTime() const {
    return m_activation_time;
}
void OAISubscriptionOrder::setActivationTime(const QDateTime &activation_time) {
    m_activation_time = activation_time;
    m_activation_time_isSet = true;
}

bool OAISubscriptionOrder::is_activation_time_Set() const{
    return m_activation_time_isSet;
}

bool OAISubscriptionOrder::is_activation_time_Valid() const{
    return m_activation_time_isValid;
}

OAIContactObject OAISubscriptionOrder::getBillingAddress() const {
    return m_billing_address;
}
void OAISubscriptionOrder::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAISubscriptionOrder::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAISubscriptionOrder::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAISubscriptionOrder::getBillingStatus() const {
    return m_billing_status;
}
void OAISubscriptionOrder::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAISubscriptionOrder::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAISubscriptionOrder::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

QList<QString> OAISubscriptionOrder::getCouponIds() const {
    return m_coupon_ids;
}
void OAISubscriptionOrder::setCouponIds(const QList<QString> &coupon_ids) {
    m_coupon_ids = coupon_ids;
    m_coupon_ids_isSet = true;
}

bool OAISubscriptionOrder::is_coupon_ids_Set() const{
    return m_coupon_ids_isSet;
}

bool OAISubscriptionOrder::is_coupon_ids_Valid() const{
    return m_coupon_ids_isValid;
}

OAIContactObject OAISubscriptionOrder::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAISubscriptionOrder::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAISubscriptionOrder::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAISubscriptionOrder::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

QString OAISubscriptionOrder::getId() const {
    return m_id;
}
void OAISubscriptionOrder::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISubscriptionOrder::is_id_Set() const{
    return m_id_isSet;
}

bool OAISubscriptionOrder::is_id_Valid() const{
    return m_id_isValid;
}

QString OAISubscriptionOrder::getInitialInvoiceId() const {
    return m_initial_invoice_id;
}
void OAISubscriptionOrder::setInitialInvoiceId(const QString &initial_invoice_id) {
    m_initial_invoice_id = initial_invoice_id;
    m_initial_invoice_id_isSet = true;
}

bool OAISubscriptionOrder::is_initial_invoice_id_Set() const{
    return m_initial_invoice_id_isSet;
}

bool OAISubscriptionOrder::is_initial_invoice_id_Valid() const{
    return m_initial_invoice_id_isValid;
}

QList<OAICommonSubscription_items_inner> OAISubscriptionOrder::getItems() const {
    return m_items;
}
void OAISubscriptionOrder::setItems(const QList<OAICommonSubscription_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAISubscriptionOrder::is_items_Set() const{
    return m_items_isSet;
}

bool OAISubscriptionOrder::is_items_Valid() const{
    return m_items_isValid;
}

QString OAISubscriptionOrder::getOrderType() const {
    return m_order_type;
}
void OAISubscriptionOrder::setOrderType(const QString &order_type) {
    m_order_type = order_type;
    m_order_type_isSet = true;
}

bool OAISubscriptionOrder::is_order_type_Set() const{
    return m_order_type_isSet;
}

bool OAISubscriptionOrder::is_order_type_Valid() const{
    return m_order_type_isValid;
}

QString OAISubscriptionOrder::getPoNumber() const {
    return m_po_number;
}
void OAISubscriptionOrder::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAISubscriptionOrder::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAISubscriptionOrder::is_po_number_Valid() const{
    return m_po_number_isValid;
}

QString OAISubscriptionOrder::getRecentInvoiceId() const {
    return m_recent_invoice_id;
}
void OAISubscriptionOrder::setRecentInvoiceId(const QString &recent_invoice_id) {
    m_recent_invoice_id = recent_invoice_id;
    m_recent_invoice_id_isSet = true;
}

bool OAISubscriptionOrder::is_recent_invoice_id_Set() const{
    return m_recent_invoice_id_isSet;
}

bool OAISubscriptionOrder::is_recent_invoice_id_Valid() const{
    return m_recent_invoice_id_isValid;
}

QDateTime OAISubscriptionOrder::getVoidTime() const {
    return m_void_time;
}
void OAISubscriptionOrder::setVoidTime(const QDateTime &void_time) {
    m_void_time = void_time;
    m_void_time_isSet = true;
}

bool OAISubscriptionOrder::is_void_time_Set() const{
    return m_void_time_isSet;
}

bool OAISubscriptionOrder::is_void_time_Valid() const{
    return m_void_time_isValid;
}

QString OAISubscriptionOrder::getWebsiteId() const {
    return m_website_id;
}
void OAISubscriptionOrder::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAISubscriptionOrder::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAISubscriptionOrder::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAISubscriptionOrder::isAutopay() const {
    return m_autopay;
}
void OAISubscriptionOrder::setAutopay(const bool &autopay) {
    m_autopay = autopay;
    m_autopay_isSet = true;
}

bool OAISubscriptionOrder::is_autopay_Set() const{
    return m_autopay_isSet;
}

bool OAISubscriptionOrder::is_autopay_Valid() const{
    return m_autopay_isValid;
}

QDateTime OAISubscriptionOrder::getEndTime() const {
    return m_end_time;
}
void OAISubscriptionOrder::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAISubscriptionOrder::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAISubscriptionOrder::is_end_time_Valid() const{
    return m_end_time_isValid;
}

bool OAISubscriptionOrder::isInTrial() const {
    return m_in_trial;
}
void OAISubscriptionOrder::setInTrial(const bool &in_trial) {
    m_in_trial = in_trial;
    m_in_trial_isSet = true;
}

bool OAISubscriptionOrder::is_in_trial_Set() const{
    return m_in_trial_isSet;
}

bool OAISubscriptionOrder::is_in_trial_Valid() const{
    return m_in_trial_isValid;
}

OAIInvoiceTimeShift OAISubscriptionOrder::getInvoiceTimeShift() const {
    return m_invoice_time_shift;
}
void OAISubscriptionOrder::setInvoiceTimeShift(const OAIInvoiceTimeShift &invoice_time_shift) {
    m_invoice_time_shift = invoice_time_shift;
    m_invoice_time_shift_isSet = true;
}

bool OAISubscriptionOrder::is_invoice_time_shift_Set() const{
    return m_invoice_time_shift_isSet;
}

bool OAISubscriptionOrder::is_invoice_time_shift_Valid() const{
    return m_invoice_time_shift_isValid;
}

bool OAISubscriptionOrder::isIsTrialOnly() const {
    return m_is_trial_only;
}
void OAISubscriptionOrder::setIsTrialOnly(const bool &is_trial_only) {
    m_is_trial_only = is_trial_only;
    m_is_trial_only_isSet = true;
}

bool OAISubscriptionOrder::is_is_trial_only_Set() const{
    return m_is_trial_only_isSet;
}

bool OAISubscriptionOrder::is_is_trial_only_Valid() const{
    return m_is_trial_only_isValid;
}

OAICommonSubscriptionOrder_allOf_lineItemSubtotal OAISubscriptionOrder::getLineItemSubtotal() const {
    return m_line_item_subtotal;
}
void OAISubscriptionOrder::setLineItemSubtotal(const OAICommonSubscriptionOrder_allOf_lineItemSubtotal &line_item_subtotal) {
    m_line_item_subtotal = line_item_subtotal;
    m_line_item_subtotal_isSet = true;
}

bool OAISubscriptionOrder::is_line_item_subtotal_Set() const{
    return m_line_item_subtotal_isSet;
}

bool OAISubscriptionOrder::is_line_item_subtotal_Valid() const{
    return m_line_item_subtotal_isValid;
}

QList<OAIUpcomingInvoiceItem> OAISubscriptionOrder::getLineItems() const {
    return m_line_items;
}
void OAISubscriptionOrder::setLineItems(const QList<OAIUpcomingInvoiceItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAISubscriptionOrder::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAISubscriptionOrder::is_line_items_Valid() const{
    return m_line_items_isValid;
}

qint32 OAISubscriptionOrder::getRebillNumber() const {
    return m_rebill_number;
}
void OAISubscriptionOrder::setRebillNumber(const qint32 &rebill_number) {
    m_rebill_number = rebill_number;
    m_rebill_number_isSet = true;
}

bool OAISubscriptionOrder::is_rebill_number_Set() const{
    return m_rebill_number_isSet;
}

bool OAISubscriptionOrder::is_rebill_number_Valid() const{
    return m_rebill_number_isValid;
}

OAICommonSubscriptionOrder_allOf_recurringInterval OAISubscriptionOrder::getRecurringInterval() const {
    return m_recurring_interval;
}
void OAISubscriptionOrder::setRecurringInterval(const OAICommonSubscriptionOrder_allOf_recurringInterval &recurring_interval) {
    m_recurring_interval = recurring_interval;
    m_recurring_interval_isSet = true;
}

bool OAISubscriptionOrder::is_recurring_interval_Set() const{
    return m_recurring_interval_isSet;
}

bool OAISubscriptionOrder::is_recurring_interval_Valid() const{
    return m_recurring_interval_isValid;
}

QDateTime OAISubscriptionOrder::getRenewalTime() const {
    return m_renewal_time;
}
void OAISubscriptionOrder::setRenewalTime(const QDateTime &renewal_time) {
    m_renewal_time = renewal_time;
    m_renewal_time_isSet = true;
}

bool OAISubscriptionOrder::is_renewal_time_Set() const{
    return m_renewal_time_isSet;
}

bool OAISubscriptionOrder::is_renewal_time_Valid() const{
    return m_renewal_time_isValid;
}

QDateTime OAISubscriptionOrder::getStartTime() const {
    return m_start_time;
}
void OAISubscriptionOrder::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAISubscriptionOrder::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAISubscriptionOrder::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAISubscriptionOrder::getStatus() const {
    return m_status;
}
void OAISubscriptionOrder::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISubscriptionOrder::is_status_Set() const{
    return m_status_isSet;
}

bool OAISubscriptionOrder::is_status_Valid() const{
    return m_status_isValid;
}

OAICommonSubscriptionOrder_allOf_trial OAISubscriptionOrder::getTrial() const {
    return m_trial;
}
void OAISubscriptionOrder::setTrial(const OAICommonSubscriptionOrder_allOf_trial &trial) {
    m_trial = trial;
    m_trial_isSet = true;
}

bool OAISubscriptionOrder::is_trial_Set() const{
    return m_trial_isSet;
}

bool OAISubscriptionOrder::is_trial_Valid() const{
    return m_trial_isValid;
}

QString OAISubscriptionOrder::getCancelCategory() const {
    return m_cancel_category;
}
void OAISubscriptionOrder::setCancelCategory(const QString &cancel_category) {
    m_cancel_category = cancel_category;
    m_cancel_category_isSet = true;
}

bool OAISubscriptionOrder::is_cancel_category_Set() const{
    return m_cancel_category_isSet;
}

bool OAISubscriptionOrder::is_cancel_category_Valid() const{
    return m_cancel_category_isValid;
}

QString OAISubscriptionOrder::getCancelDescription() const {
    return m_cancel_description;
}
void OAISubscriptionOrder::setCancelDescription(const QString &cancel_description) {
    m_cancel_description = cancel_description;
    m_cancel_description_isSet = true;
}

bool OAISubscriptionOrder::is_cancel_description_Set() const{
    return m_cancel_description_isSet;
}

bool OAISubscriptionOrder::is_cancel_description_Valid() const{
    return m_cancel_description_isValid;
}

QString OAISubscriptionOrder::getCanceledBy() const {
    return m_canceled_by;
}
void OAISubscriptionOrder::setCanceledBy(const QString &canceled_by) {
    m_canceled_by = canceled_by;
    m_canceled_by_isSet = true;
}

bool OAISubscriptionOrder::is_canceled_by_Set() const{
    return m_canceled_by_isSet;
}

bool OAISubscriptionOrder::is_canceled_by_Valid() const{
    return m_canceled_by_isValid;
}

QDateTime OAISubscriptionOrder::getCanceledTime() const {
    return m_canceled_time;
}
void OAISubscriptionOrder::setCanceledTime(const QDateTime &canceled_time) {
    m_canceled_time = canceled_time;
    m_canceled_time_isSet = true;
}

bool OAISubscriptionOrder::is_canceled_time_Set() const{
    return m_canceled_time_isSet;
}

bool OAISubscriptionOrder::is_canceled_time_Valid() const{
    return m_canceled_time_isValid;
}

QList<OAISubscriptionMetadata__embedded_inner> OAISubscriptionOrder::getEmbedded() const {
    return m__embedded;
}
void OAISubscriptionOrder::setEmbedded(const QList<OAISubscriptionMetadata__embedded_inner> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAISubscriptionOrder::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAISubscriptionOrder::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAISubscriptionMetadata__links_inner> OAISubscriptionOrder::getLinks() const {
    return m__links;
}
void OAISubscriptionOrder::setLinks(const QList<OAISubscriptionMetadata__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAISubscriptionOrder::is__links_Set() const{
    return m__links_isSet;
}

bool OAISubscriptionOrder::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAISubscriptionOrder::getCreatedTime() const {
    return m_created_time;
}
void OAISubscriptionOrder::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAISubscriptionOrder::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAISubscriptionOrder::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIObject OAISubscriptionOrder::getCustomFields() const {
    return m_custom_fields;
}
void OAISubscriptionOrder::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAISubscriptionOrder::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAISubscriptionOrder::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

qint32 OAISubscriptionOrder::getRevision() const {
    return m_revision;
}
void OAISubscriptionOrder::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAISubscriptionOrder::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAISubscriptionOrder::is_revision_Valid() const{
    return m_revision_isValid;
}

OAIRiskMetadata OAISubscriptionOrder::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAISubscriptionOrder::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAISubscriptionOrder::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAISubscriptionOrder::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

QDateTime OAISubscriptionOrder::getUpdatedTime() const {
    return m_updated_time;
}
void OAISubscriptionOrder::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAISubscriptionOrder::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAISubscriptionOrder::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAISubscriptionOrder::getCustomerId() const {
    return m_customer_id;
}
void OAISubscriptionOrder::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAISubscriptionOrder::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAISubscriptionOrder::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

qint32 OAISubscriptionOrder::getRenewalReminderNumber() const {
    return m_renewal_reminder_number;
}
void OAISubscriptionOrder::setRenewalReminderNumber(const qint32 &renewal_reminder_number) {
    m_renewal_reminder_number = renewal_reminder_number;
    m_renewal_reminder_number_isSet = true;
}

bool OAISubscriptionOrder::is_renewal_reminder_number_Set() const{
    return m_renewal_reminder_number_isSet;
}

bool OAISubscriptionOrder::is_renewal_reminder_number_Valid() const{
    return m_renewal_reminder_number_isValid;
}

QDateTime OAISubscriptionOrder::getRenewalReminderTime() const {
    return m_renewal_reminder_time;
}
void OAISubscriptionOrder::setRenewalReminderTime(const QDateTime &renewal_reminder_time) {
    m_renewal_reminder_time = renewal_reminder_time;
    m_renewal_reminder_time_isSet = true;
}

bool OAISubscriptionOrder::is_renewal_reminder_time_Set() const{
    return m_renewal_reminder_time_isSet;
}

bool OAISubscriptionOrder::is_renewal_reminder_time_Valid() const{
    return m_renewal_reminder_time_isValid;
}

qint32 OAISubscriptionOrder::getTrialReminderNumber() const {
    return m_trial_reminder_number;
}
void OAISubscriptionOrder::setTrialReminderNumber(const qint32 &trial_reminder_number) {
    m_trial_reminder_number = trial_reminder_number;
    m_trial_reminder_number_isSet = true;
}

bool OAISubscriptionOrder::is_trial_reminder_number_Set() const{
    return m_trial_reminder_number_isSet;
}

bool OAISubscriptionOrder::is_trial_reminder_number_Valid() const{
    return m_trial_reminder_number_isValid;
}

QDateTime OAISubscriptionOrder::getTrialReminderTime() const {
    return m_trial_reminder_time;
}
void OAISubscriptionOrder::setTrialReminderTime(const QDateTime &trial_reminder_time) {
    m_trial_reminder_time = trial_reminder_time;
    m_trial_reminder_time_isSet = true;
}

bool OAISubscriptionOrder::is_trial_reminder_time_Set() const{
    return m_trial_reminder_time_isSet;
}

bool OAISubscriptionOrder::is_trial_reminder_time_Valid() const{
    return m_trial_reminder_time_isValid;
}

bool OAISubscriptionOrder::isSet() const {
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

        if (m_cancel_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cancel_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_canceled_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_canceled_time_isSet) {
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

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_renewal_reminder_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_renewal_reminder_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial_reminder_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial_reminder_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionOrder::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && m_order_type_isValid && m_website_id_isValid && m_customer_id_isValid && true;
}

} // namespace OpenAPI
