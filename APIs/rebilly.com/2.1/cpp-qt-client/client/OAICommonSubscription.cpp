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

#include "OAICommonSubscription.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommonSubscription::OAICommonSubscription(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommonSubscription::OAICommonSubscription() {
    this->initializeModel();
}

OAICommonSubscription::~OAICommonSubscription() {}

void OAICommonSubscription::initializeModel() {

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
}

void OAICommonSubscription::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommonSubscription::fromJsonObject(QJsonObject json) {

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
}

QString OAICommonSubscription::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommonSubscription::asJsonObject() const {
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
    return obj;
}

QDateTime OAICommonSubscription::getActivationTime() const {
    return m_activation_time;
}
void OAICommonSubscription::setActivationTime(const QDateTime &activation_time) {
    m_activation_time = activation_time;
    m_activation_time_isSet = true;
}

bool OAICommonSubscription::is_activation_time_Set() const{
    return m_activation_time_isSet;
}

bool OAICommonSubscription::is_activation_time_Valid() const{
    return m_activation_time_isValid;
}

OAIContactObject OAICommonSubscription::getBillingAddress() const {
    return m_billing_address;
}
void OAICommonSubscription::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICommonSubscription::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICommonSubscription::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAICommonSubscription::getBillingStatus() const {
    return m_billing_status;
}
void OAICommonSubscription::setBillingStatus(const QString &billing_status) {
    m_billing_status = billing_status;
    m_billing_status_isSet = true;
}

bool OAICommonSubscription::is_billing_status_Set() const{
    return m_billing_status_isSet;
}

bool OAICommonSubscription::is_billing_status_Valid() const{
    return m_billing_status_isValid;
}

QList<QString> OAICommonSubscription::getCouponIds() const {
    return m_coupon_ids;
}
void OAICommonSubscription::setCouponIds(const QList<QString> &coupon_ids) {
    m_coupon_ids = coupon_ids;
    m_coupon_ids_isSet = true;
}

bool OAICommonSubscription::is_coupon_ids_Set() const{
    return m_coupon_ids_isSet;
}

bool OAICommonSubscription::is_coupon_ids_Valid() const{
    return m_coupon_ids_isValid;
}

OAIContactObject OAICommonSubscription::getDeliveryAddress() const {
    return m_delivery_address;
}
void OAICommonSubscription::setDeliveryAddress(const OAIContactObject &delivery_address) {
    m_delivery_address = delivery_address;
    m_delivery_address_isSet = true;
}

bool OAICommonSubscription::is_delivery_address_Set() const{
    return m_delivery_address_isSet;
}

bool OAICommonSubscription::is_delivery_address_Valid() const{
    return m_delivery_address_isValid;
}

QString OAICommonSubscription::getId() const {
    return m_id;
}
void OAICommonSubscription::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICommonSubscription::is_id_Set() const{
    return m_id_isSet;
}

bool OAICommonSubscription::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICommonSubscription::getInitialInvoiceId() const {
    return m_initial_invoice_id;
}
void OAICommonSubscription::setInitialInvoiceId(const QString &initial_invoice_id) {
    m_initial_invoice_id = initial_invoice_id;
    m_initial_invoice_id_isSet = true;
}

bool OAICommonSubscription::is_initial_invoice_id_Set() const{
    return m_initial_invoice_id_isSet;
}

bool OAICommonSubscription::is_initial_invoice_id_Valid() const{
    return m_initial_invoice_id_isValid;
}

QList<OAICommonSubscription_items_inner> OAICommonSubscription::getItems() const {
    return m_items;
}
void OAICommonSubscription::setItems(const QList<OAICommonSubscription_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAICommonSubscription::is_items_Set() const{
    return m_items_isSet;
}

bool OAICommonSubscription::is_items_Valid() const{
    return m_items_isValid;
}

QString OAICommonSubscription::getOrderType() const {
    return m_order_type;
}
void OAICommonSubscription::setOrderType(const QString &order_type) {
    m_order_type = order_type;
    m_order_type_isSet = true;
}

bool OAICommonSubscription::is_order_type_Set() const{
    return m_order_type_isSet;
}

bool OAICommonSubscription::is_order_type_Valid() const{
    return m_order_type_isValid;
}

QString OAICommonSubscription::getPoNumber() const {
    return m_po_number;
}
void OAICommonSubscription::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAICommonSubscription::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAICommonSubscription::is_po_number_Valid() const{
    return m_po_number_isValid;
}

QString OAICommonSubscription::getRecentInvoiceId() const {
    return m_recent_invoice_id;
}
void OAICommonSubscription::setRecentInvoiceId(const QString &recent_invoice_id) {
    m_recent_invoice_id = recent_invoice_id;
    m_recent_invoice_id_isSet = true;
}

bool OAICommonSubscription::is_recent_invoice_id_Set() const{
    return m_recent_invoice_id_isSet;
}

bool OAICommonSubscription::is_recent_invoice_id_Valid() const{
    return m_recent_invoice_id_isValid;
}

QDateTime OAICommonSubscription::getVoidTime() const {
    return m_void_time;
}
void OAICommonSubscription::setVoidTime(const QDateTime &void_time) {
    m_void_time = void_time;
    m_void_time_isSet = true;
}

bool OAICommonSubscription::is_void_time_Set() const{
    return m_void_time_isSet;
}

bool OAICommonSubscription::is_void_time_Valid() const{
    return m_void_time_isValid;
}

QString OAICommonSubscription::getWebsiteId() const {
    return m_website_id;
}
void OAICommonSubscription::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICommonSubscription::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICommonSubscription::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICommonSubscription::isSet() const {
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
    } while (false);
    return isObjectUpdated;
}

bool OAICommonSubscription::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
