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

#include "OAISubscriptionCancellation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionCancellation::OAISubscriptionCancellation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionCancellation::OAISubscriptionCancellation() {
    this->initializeModel();
}

OAISubscriptionCancellation::~OAISubscriptionCancellation() {}

void OAISubscriptionCancellation::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_applied_invoice_id_isSet = false;
    m_applied_invoice_id_isValid = false;

    m_canceled_by_isSet = false;
    m_canceled_by_isValid = false;

    m_canceled_time_isSet = false;
    m_canceled_time_isValid = false;

    m_churn_time_isSet = false;
    m_churn_time_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_line_item_subtotal_isSet = false;
    m_line_item_subtotal_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_prorated_isSet = false;
    m_prorated_isValid = false;

    m_prorated_invoice_id_isSet = false;
    m_prorated_invoice_id_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscription_id_isSet = false;
    m_subscription_id_isValid = false;
}

void OAISubscriptionCancellation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionCancellation::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_applied_invoice_id_isValid = ::OpenAPI::fromJsonValue(m_applied_invoice_id, json[QString("appliedInvoiceId")]);
    m_applied_invoice_id_isSet = !json[QString("appliedInvoiceId")].isNull() && m_applied_invoice_id_isValid;

    m_canceled_by_isValid = ::OpenAPI::fromJsonValue(m_canceled_by, json[QString("canceledBy")]);
    m_canceled_by_isSet = !json[QString("canceledBy")].isNull() && m_canceled_by_isValid;

    m_canceled_time_isValid = ::OpenAPI::fromJsonValue(m_canceled_time, json[QString("canceledTime")]);
    m_canceled_time_isSet = !json[QString("canceledTime")].isNull() && m_canceled_time_isValid;

    m_churn_time_isValid = ::OpenAPI::fromJsonValue(m_churn_time, json[QString("churnTime")]);
    m_churn_time_isSet = !json[QString("churnTime")].isNull() && m_churn_time_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_line_item_subtotal_isValid = ::OpenAPI::fromJsonValue(m_line_item_subtotal, json[QString("lineItemSubtotal")]);
    m_line_item_subtotal_isSet = !json[QString("lineItemSubtotal")].isNull() && m_line_item_subtotal_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("lineItems")]);
    m_line_items_isSet = !json[QString("lineItems")].isNull() && m_line_items_isValid;

    m_prorated_isValid = ::OpenAPI::fromJsonValue(m_prorated, json[QString("prorated")]);
    m_prorated_isSet = !json[QString("prorated")].isNull() && m_prorated_isValid;

    m_prorated_invoice_id_isValid = ::OpenAPI::fromJsonValue(m_prorated_invoice_id, json[QString("proratedInvoiceId")]);
    m_prorated_invoice_id_isSet = !json[QString("proratedInvoiceId")].isNull() && m_prorated_invoice_id_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscription_id_isValid = ::OpenAPI::fromJsonValue(m_subscription_id, json[QString("subscriptionId")]);
    m_subscription_id_isSet = !json[QString("subscriptionId")].isNull() && m_subscription_id_isValid;
}

QString OAISubscriptionCancellation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionCancellation::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_applied_invoice_id_isSet) {
        obj.insert(QString("appliedInvoiceId"), ::OpenAPI::toJsonValue(m_applied_invoice_id));
    }
    if (m_canceled_by_isSet) {
        obj.insert(QString("canceledBy"), ::OpenAPI::toJsonValue(m_canceled_by));
    }
    if (m_canceled_time_isSet) {
        obj.insert(QString("canceledTime"), ::OpenAPI::toJsonValue(m_canceled_time));
    }
    if (m_churn_time_isSet) {
        obj.insert(QString("churnTime"), ::OpenAPI::toJsonValue(m_churn_time));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_line_item_subtotal_isSet) {
        obj.insert(QString("lineItemSubtotal"), ::OpenAPI::toJsonValue(m_line_item_subtotal));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("lineItems"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_prorated_isSet) {
        obj.insert(QString("prorated"), ::OpenAPI::toJsonValue(m_prorated));
    }
    if (m_prorated_invoice_id_isSet) {
        obj.insert(QString("proratedInvoiceId"), ::OpenAPI::toJsonValue(m_prorated_invoice_id));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscription_id_isSet) {
        obj.insert(QString("subscriptionId"), ::OpenAPI::toJsonValue(m_subscription_id));
    }
    return obj;
}

QList<OAISelfLink> OAISubscriptionCancellation::getLinks() const {
    return m__links;
}
void OAISubscriptionCancellation::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAISubscriptionCancellation::is__links_Set() const{
    return m__links_isSet;
}

bool OAISubscriptionCancellation::is__links_Valid() const{
    return m__links_isValid;
}

QString OAISubscriptionCancellation::getAppliedInvoiceId() const {
    return m_applied_invoice_id;
}
void OAISubscriptionCancellation::setAppliedInvoiceId(const QString &applied_invoice_id) {
    m_applied_invoice_id = applied_invoice_id;
    m_applied_invoice_id_isSet = true;
}

bool OAISubscriptionCancellation::is_applied_invoice_id_Set() const{
    return m_applied_invoice_id_isSet;
}

bool OAISubscriptionCancellation::is_applied_invoice_id_Valid() const{
    return m_applied_invoice_id_isValid;
}

QString OAISubscriptionCancellation::getCanceledBy() const {
    return m_canceled_by;
}
void OAISubscriptionCancellation::setCanceledBy(const QString &canceled_by) {
    m_canceled_by = canceled_by;
    m_canceled_by_isSet = true;
}

bool OAISubscriptionCancellation::is_canceled_by_Set() const{
    return m_canceled_by_isSet;
}

bool OAISubscriptionCancellation::is_canceled_by_Valid() const{
    return m_canceled_by_isValid;
}

QDateTime OAISubscriptionCancellation::getCanceledTime() const {
    return m_canceled_time;
}
void OAISubscriptionCancellation::setCanceledTime(const QDateTime &canceled_time) {
    m_canceled_time = canceled_time;
    m_canceled_time_isSet = true;
}

bool OAISubscriptionCancellation::is_canceled_time_Set() const{
    return m_canceled_time_isSet;
}

bool OAISubscriptionCancellation::is_canceled_time_Valid() const{
    return m_canceled_time_isValid;
}

QDateTime OAISubscriptionCancellation::getChurnTime() const {
    return m_churn_time;
}
void OAISubscriptionCancellation::setChurnTime(const QDateTime &churn_time) {
    m_churn_time = churn_time;
    m_churn_time_isSet = true;
}

bool OAISubscriptionCancellation::is_churn_time_Set() const{
    return m_churn_time_isSet;
}

bool OAISubscriptionCancellation::is_churn_time_Valid() const{
    return m_churn_time_isValid;
}

QDateTime OAISubscriptionCancellation::getCreatedTime() const {
    return m_created_time;
}
void OAISubscriptionCancellation::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAISubscriptionCancellation::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAISubscriptionCancellation::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAISubscriptionCancellation::getDescription() const {
    return m_description;
}
void OAISubscriptionCancellation::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISubscriptionCancellation::is_description_Set() const{
    return m_description_isSet;
}

bool OAISubscriptionCancellation::is_description_Valid() const{
    return m_description_isValid;
}

QString OAISubscriptionCancellation::getId() const {
    return m_id;
}
void OAISubscriptionCancellation::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISubscriptionCancellation::is_id_Set() const{
    return m_id_isSet;
}

bool OAISubscriptionCancellation::is_id_Valid() const{
    return m_id_isValid;
}

double OAISubscriptionCancellation::getLineItemSubtotal() const {
    return m_line_item_subtotal;
}
void OAISubscriptionCancellation::setLineItemSubtotal(const double &line_item_subtotal) {
    m_line_item_subtotal = line_item_subtotal;
    m_line_item_subtotal_isSet = true;
}

bool OAISubscriptionCancellation::is_line_item_subtotal_Set() const{
    return m_line_item_subtotal_isSet;
}

bool OAISubscriptionCancellation::is_line_item_subtotal_Valid() const{
    return m_line_item_subtotal_isValid;
}

QList<OAIUpcomingInvoiceItem> OAISubscriptionCancellation::getLineItems() const {
    return m_line_items;
}
void OAISubscriptionCancellation::setLineItems(const QList<OAIUpcomingInvoiceItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAISubscriptionCancellation::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAISubscriptionCancellation::is_line_items_Valid() const{
    return m_line_items_isValid;
}

bool OAISubscriptionCancellation::isProrated() const {
    return m_prorated;
}
void OAISubscriptionCancellation::setProrated(const bool &prorated) {
    m_prorated = prorated;
    m_prorated_isSet = true;
}

bool OAISubscriptionCancellation::is_prorated_Set() const{
    return m_prorated_isSet;
}

bool OAISubscriptionCancellation::is_prorated_Valid() const{
    return m_prorated_isValid;
}

QString OAISubscriptionCancellation::getProratedInvoiceId() const {
    return m_prorated_invoice_id;
}
void OAISubscriptionCancellation::setProratedInvoiceId(const QString &prorated_invoice_id) {
    m_prorated_invoice_id = prorated_invoice_id;
    m_prorated_invoice_id_isSet = true;
}

bool OAISubscriptionCancellation::is_prorated_invoice_id_Set() const{
    return m_prorated_invoice_id_isSet;
}

bool OAISubscriptionCancellation::is_prorated_invoice_id_Valid() const{
    return m_prorated_invoice_id_isValid;
}

QString OAISubscriptionCancellation::getReason() const {
    return m_reason;
}
void OAISubscriptionCancellation::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAISubscriptionCancellation::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAISubscriptionCancellation::is_reason_Valid() const{
    return m_reason_isValid;
}

QString OAISubscriptionCancellation::getStatus() const {
    return m_status;
}
void OAISubscriptionCancellation::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAISubscriptionCancellation::is_status_Set() const{
    return m_status_isSet;
}

bool OAISubscriptionCancellation::is_status_Valid() const{
    return m_status_isValid;
}

QString OAISubscriptionCancellation::getSubscriptionId() const {
    return m_subscription_id;
}
void OAISubscriptionCancellation::setSubscriptionId(const QString &subscription_id) {
    m_subscription_id = subscription_id;
    m_subscription_id_isSet = true;
}

bool OAISubscriptionCancellation::is_subscription_id_Set() const{
    return m_subscription_id_isSet;
}

bool OAISubscriptionCancellation::is_subscription_id_Valid() const{
    return m_subscription_id_isValid;
}

bool OAISubscriptionCancellation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_applied_invoice_id_isSet) {
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

        if (m_churn_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_item_subtotal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_prorated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prorated_invoice_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionCancellation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_churn_time_isValid && m_subscription_id_isValid && true;
}

} // namespace OpenAPI
