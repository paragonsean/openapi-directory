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

#include "OAIOneTimeOrder.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOneTimeOrder::OAIOneTimeOrder(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOneTimeOrder::OAIOneTimeOrder() {
    this->initializeModel();
}

OAIOneTimeOrder::~OAIOneTimeOrder() {}

void OAIOneTimeOrder::initializeModel() {

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

    m_status_isSet = false;
    m_status_isValid = false;

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
}

void OAIOneTimeOrder::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOneTimeOrder::fromJsonObject(QJsonObject json) {

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

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

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
}

QString OAIOneTimeOrder::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOneTimeOrder::asJsonObject() const {
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
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
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
    return obj;
}

QDateTime OAIOneTimeOrder::getActivationTime() const {
    return m_activation_time;
}
void OAIOneTimeOrder::setActivationTime(const QDateTime &activation_time) {
    m_activation_time = activation_time;
    m_activation_time_isSet = true;
}

bool OAIOneTimeOrder::is_activation_time_Set() const{
    return m_activation_time_isSet;
}

bool OAIOneTimeOrder::is_activation_time_Valid() const{
    return m_activation_time_isValid;
}

OAIContactObject OAIOneTimeOrder::getBillingAddress() const {
    return m_billing_address;
}
void OAIOneTimeOrder::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIOneTimeOrder::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIOneTimeOrder::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIOneTimeOrder::getBillingStatus() const {
    return m_billing_status;
}
void OAIOneTimeOrder::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAIOneTimeOrder::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAIOneTimeOrder::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

QList<QString> OAIOneTimeOrder::getCouponIds() const {
    return m_coupon_ids;
}
void OAIOneTimeOrder::setCouponIds(const QList<QString> &coupon_ids) {
    m_coupon_ids = coupon_ids;
    m_coupon_ids_isSet = true;
}

bool OAIOneTimeOrder::is_coupon_ids_Set() const{
    return m_coupon_ids_isSet;
}

bool OAIOneTimeOrder::is_coupon_ids_Valid() const{
    return m_coupon_ids_isValid;
}

OAIContactObject OAIOneTimeOrder::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAIOneTimeOrder::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAIOneTimeOrder::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAIOneTimeOrder::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

QString OAIOneTimeOrder::getId() const {
    return m_id;
}
void OAIOneTimeOrder::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOneTimeOrder::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOneTimeOrder::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOneTimeOrder::getInitialInvoiceId() const {
    return m_initial_invoice_id;
}
void OAIOneTimeOrder::setInitialInvoiceId(const QString &initial_invoice_id) {
    m_initial_invoice_id = initial_invoice_id;
    m_initial_invoice_id_isSet = true;
}

bool OAIOneTimeOrder::is_initial_invoice_id_Set() const{
    return m_initial_invoice_id_isSet;
}

bool OAIOneTimeOrder::is_initial_invoice_id_Valid() const{
    return m_initial_invoice_id_isValid;
}

QList<OAICommonSubscription_items_inner> OAIOneTimeOrder::getItems() const {
    return m_items;
}
void OAIOneTimeOrder::setItems(const QList<OAICommonSubscription_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIOneTimeOrder::is_items_Set() const{
    return m_items_isSet;
}

bool OAIOneTimeOrder::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIOneTimeOrder::getOrderType() const {
    return m_order_type;
}
void OAIOneTimeOrder::setOrderType(const QString &order_type) {
    m_order_type = order_type;
    m_order_type_isSet = true;
}

bool OAIOneTimeOrder::is_order_type_Set() const{
    return m_order_type_isSet;
}

bool OAIOneTimeOrder::is_order_type_Valid() const{
    return m_order_type_isValid;
}

QString OAIOneTimeOrder::getPoNumber() const {
    return m_po_number;
}
void OAIOneTimeOrder::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAIOneTimeOrder::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAIOneTimeOrder::is_po_number_Valid() const{
    return m_po_number_isValid;
}

QString OAIOneTimeOrder::getRecentInvoiceId() const {
    return m_recent_invoice_id;
}
void OAIOneTimeOrder::setRecentInvoiceId(const QString &recent_invoice_id) {
    m_recent_invoice_id = recent_invoice_id;
    m_recent_invoice_id_isSet = true;
}

bool OAIOneTimeOrder::is_recent_invoice_id_Set() const{
    return m_recent_invoice_id_isSet;
}

bool OAIOneTimeOrder::is_recent_invoice_id_Valid() const{
    return m_recent_invoice_id_isValid;
}

QDateTime OAIOneTimeOrder::getVoidTime() const {
    return m_void_time;
}
void OAIOneTimeOrder::setVoidTime(const QDateTime &void_time) {
    m_void_time = void_time;
    m_void_time_isSet = true;
}

bool OAIOneTimeOrder::is_void_time_Set() const{
    return m_void_time_isSet;
}

bool OAIOneTimeOrder::is_void_time_Valid() const{
    return m_void_time_isValid;
}

QString OAIOneTimeOrder::getWebsiteId() const {
    return m_website_id;
}
void OAIOneTimeOrder::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAIOneTimeOrder::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAIOneTimeOrder::is_website_id_Valid() const{
    return m_website_id_isValid;
}

QString OAIOneTimeOrder::getStatus() const {
    return m_status;
}
void OAIOneTimeOrder::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOneTimeOrder::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOneTimeOrder::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAISubscriptionMetadata__embedded_inner> OAIOneTimeOrder::getEmbedded() const {
    return m__embedded;
}
void OAIOneTimeOrder::setEmbedded(const QList<OAISubscriptionMetadata__embedded_inner> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAIOneTimeOrder::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAIOneTimeOrder::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAISubscriptionMetadata__links_inner> OAIOneTimeOrder::getLinks() const {
    return m__links;
}
void OAIOneTimeOrder::setLinks(const QList<OAISubscriptionMetadata__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIOneTimeOrder::is__links_Set() const{
    return m__links_isSet;
}

bool OAIOneTimeOrder::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAIOneTimeOrder::getCreatedTime() const {
    return m_created_time;
}
void OAIOneTimeOrder::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIOneTimeOrder::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIOneTimeOrder::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIObject OAIOneTimeOrder::getCustomFields() const {
    return m_custom_fields;
}
void OAIOneTimeOrder::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIOneTimeOrder::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIOneTimeOrder::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

qint32 OAIOneTimeOrder::getRevision() const {
    return m_revision;
}
void OAIOneTimeOrder::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAIOneTimeOrder::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAIOneTimeOrder::is_revision_Valid() const{
    return m_revision_isValid;
}

OAIRiskMetadata OAIOneTimeOrder::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAIOneTimeOrder::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAIOneTimeOrder::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAIOneTimeOrder::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

QDateTime OAIOneTimeOrder::getUpdatedTime() const {
    return m_updated_time;
}
void OAIOneTimeOrder::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIOneTimeOrder::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIOneTimeOrder::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAIOneTimeOrder::getCustomerId() const {
    return m_customer_id;
}
void OAIOneTimeOrder::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIOneTimeOrder::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIOneTimeOrder::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

bool OAIOneTimeOrder::isSet() const {
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

        if (m_status_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIOneTimeOrder::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_items_isValid && m_order_type_isValid && m_website_id_isValid && m_customer_id_isValid && true;
}

} // namespace OpenAPI
