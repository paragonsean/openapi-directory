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

#include "OAICustomer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomer::OAICustomer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomer::OAICustomer() {
    this->initializeModel();
}

OAICustomer::~OAICustomer() {}

void OAICustomer::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_average_value_isSet = false;
    m_average_value_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_default_payment_instrument_isSet = false;
    m_default_payment_instrument_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_count_isSet = false;
    m_invoice_count_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_last_payment_time_isSet = false;
    m_last_payment_time_isValid = false;

    m_lifetime_revenue_isSet = false;
    m_lifetime_revenue_isValid = false;

    m_payment_count_isSet = false;
    m_payment_count_isValid = false;

    m_payment_token_isSet = false;
    m_payment_token_isValid = false;

    m_primary_address_isSet = false;
    m_primary_address_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;
}

void OAICustomer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomer::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_average_value_isValid = ::OpenAPI::fromJsonValue(m_average_value, json[QString("averageValue")]);
    m_average_value_isSet = !json[QString("averageValue")].isNull() && m_average_value_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_default_payment_instrument_isValid = ::OpenAPI::fromJsonValue(m_default_payment_instrument, json[QString("defaultPaymentInstrument")]);
    m_default_payment_instrument_isSet = !json[QString("defaultPaymentInstrument")].isNull() && m_default_payment_instrument_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_count_isValid = ::OpenAPI::fromJsonValue(m_invoice_count, json[QString("invoiceCount")]);
    m_invoice_count_isSet = !json[QString("invoiceCount")].isNull() && m_invoice_count_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_last_payment_time_isValid = ::OpenAPI::fromJsonValue(m_last_payment_time, json[QString("lastPaymentTime")]);
    m_last_payment_time_isSet = !json[QString("lastPaymentTime")].isNull() && m_last_payment_time_isValid;

    m_lifetime_revenue_isValid = ::OpenAPI::fromJsonValue(m_lifetime_revenue, json[QString("lifetimeRevenue")]);
    m_lifetime_revenue_isSet = !json[QString("lifetimeRevenue")].isNull() && m_lifetime_revenue_isValid;

    m_payment_count_isValid = ::OpenAPI::fromJsonValue(m_payment_count, json[QString("paymentCount")]);
    m_payment_count_isSet = !json[QString("paymentCount")].isNull() && m_payment_count_isValid;

    m_payment_token_isValid = ::OpenAPI::fromJsonValue(m_payment_token, json[QString("paymentToken")]);
    m_payment_token_isSet = !json[QString("paymentToken")].isNull() && m_payment_token_isValid;

    m_primary_address_isValid = ::OpenAPI::fromJsonValue(m_primary_address, json[QString("primaryAddress")]);
    m_primary_address_isSet = !json[QString("primaryAddress")].isNull() && m_primary_address_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;
}

QString OAICustomer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomer::asJsonObject() const {
    QJsonObject obj;
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_average_value.isSet()) {
        obj.insert(QString("averageValue"), ::OpenAPI::toJsonValue(m_average_value));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_default_payment_instrument.isSet()) {
        obj.insert(QString("defaultPaymentInstrument"), ::OpenAPI::toJsonValue(m_default_payment_instrument));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_count_isSet) {
        obj.insert(QString("invoiceCount"), ::OpenAPI::toJsonValue(m_invoice_count));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_last_payment_time_isSet) {
        obj.insert(QString("lastPaymentTime"), ::OpenAPI::toJsonValue(m_last_payment_time));
    }
    if (m_lifetime_revenue.isSet()) {
        obj.insert(QString("lifetimeRevenue"), ::OpenAPI::toJsonValue(m_lifetime_revenue));
    }
    if (m_payment_count_isSet) {
        obj.insert(QString("paymentCount"), ::OpenAPI::toJsonValue(m_payment_count));
    }
    if (m_payment_token_isSet) {
        obj.insert(QString("paymentToken"), ::OpenAPI::toJsonValue(m_payment_token));
    }
    if (m_primary_address.isSet()) {
        obj.insert(QString("primaryAddress"), ::OpenAPI::toJsonValue(m_primary_address));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    return obj;
}

QList<OAICustomer__embedded_inner> OAICustomer::getEmbedded() const {
    return m__embedded;
}
void OAICustomer::setEmbedded(const QList<OAICustomer__embedded_inner> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAICustomer::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAICustomer::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAICustomer__links_inner> OAICustomer::getLinks() const {
    return m__links;
}
void OAICustomer::setLinks(const QList<OAICustomer__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAICustomer::is__links_Set() const{
    return m__links_isSet;
}

bool OAICustomer::is__links_Valid() const{
    return m__links_isValid;
}

OAICustomerAverageValue OAICustomer::getAverageValue() const {
    return m_average_value;
}
void OAICustomer::setAverageValue(const OAICustomerAverageValue &average_value) {
    m_average_value = average_value;
    m_average_value_isSet = true;
}

bool OAICustomer::is_average_value_Set() const{
    return m_average_value_isSet;
}

bool OAICustomer::is_average_value_Valid() const{
    return m_average_value_isValid;
}

QDateTime OAICustomer::getCreatedTime() const {
    return m_created_time;
}
void OAICustomer::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAICustomer::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAICustomer::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIObject OAICustomer::getCustomFields() const {
    return m_custom_fields;
}
void OAICustomer::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAICustomer::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAICustomer::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIPaymentInstrument OAICustomer::getDefaultPaymentInstrument() const {
    return m_default_payment_instrument;
}
void OAICustomer::setDefaultPaymentInstrument(const OAIPaymentInstrument &default_payment_instrument) {
    m_default_payment_instrument = default_payment_instrument;
    m_default_payment_instrument_isSet = true;
}

bool OAICustomer::is_default_payment_instrument_Set() const{
    return m_default_payment_instrument_isSet;
}

bool OAICustomer::is_default_payment_instrument_Valid() const{
    return m_default_payment_instrument_isValid;
}

QString OAICustomer::getEmail() const {
    return m_email;
}
void OAICustomer::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAICustomer::is_email_Set() const{
    return m_email_isSet;
}

bool OAICustomer::is_email_Valid() const{
    return m_email_isValid;
}

QString OAICustomer::getFirstName() const {
    return m_first_name;
}
void OAICustomer::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAICustomer::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAICustomer::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAICustomer::getId() const {
    return m_id;
}
void OAICustomer::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomer::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomer::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAICustomer::getInvoiceCount() const {
    return m_invoice_count;
}
void OAICustomer::setInvoiceCount(const qint32 &invoice_count) {
    m_invoice_count = invoice_count;
    m_invoice_count_isSet = true;
}

bool OAICustomer::is_invoice_count_Set() const{
    return m_invoice_count_isSet;
}

bool OAICustomer::is_invoice_count_Valid() const{
    return m_invoice_count_isValid;
}

QString OAICustomer::getLastName() const {
    return m_last_name;
}
void OAICustomer::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAICustomer::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAICustomer::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QDateTime OAICustomer::getLastPaymentTime() const {
    return m_last_payment_time;
}
void OAICustomer::setLastPaymentTime(const QDateTime &last_payment_time) {
    m_last_payment_time = last_payment_time;
    m_last_payment_time_isSet = true;
}

bool OAICustomer::is_last_payment_time_Set() const{
    return m_last_payment_time_isSet;
}

bool OAICustomer::is_last_payment_time_Valid() const{
    return m_last_payment_time_isValid;
}

OAICustomerLifetimeRevenue OAICustomer::getLifetimeRevenue() const {
    return m_lifetime_revenue;
}
void OAICustomer::setLifetimeRevenue(const OAICustomerLifetimeRevenue &lifetime_revenue) {
    m_lifetime_revenue = lifetime_revenue;
    m_lifetime_revenue_isSet = true;
}

bool OAICustomer::is_lifetime_revenue_Set() const{
    return m_lifetime_revenue_isSet;
}

bool OAICustomer::is_lifetime_revenue_Valid() const{
    return m_lifetime_revenue_isValid;
}

qint32 OAICustomer::getPaymentCount() const {
    return m_payment_count;
}
void OAICustomer::setPaymentCount(const qint32 &payment_count) {
    m_payment_count = payment_count;
    m_payment_count_isSet = true;
}

bool OAICustomer::is_payment_count_Set() const{
    return m_payment_count_isSet;
}

bool OAICustomer::is_payment_count_Valid() const{
    return m_payment_count_isValid;
}

QString OAICustomer::getPaymentToken() const {
    return m_payment_token;
}
void OAICustomer::setPaymentToken(const QString &payment_token) {
    m_payment_token = payment_token;
    m_payment_token_isSet = true;
}

bool OAICustomer::is_payment_token_Set() const{
    return m_payment_token_isSet;
}

bool OAICustomer::is_payment_token_Valid() const{
    return m_payment_token_isValid;
}

OAIContactObject OAICustomer::getPrimaryAddress() const {
    return m_primary_address;
}
void OAICustomer::setPrimaryAddress(const OAIContactObject &primary_address) {
    m_primary_address = primary_address;
    m_primary_address_isSet = true;
}

bool OAICustomer::is_primary_address_Set() const{
    return m_primary_address_isSet;
}

bool OAICustomer::is_primary_address_Valid() const{
    return m_primary_address_isValid;
}

qint32 OAICustomer::getRevision() const {
    return m_revision;
}
void OAICustomer::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAICustomer::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAICustomer::is_revision_Valid() const{
    return m_revision_isValid;
}

QList<OAITag> OAICustomer::getTags() const {
    return m_tags;
}
void OAICustomer::setTags(const QList<OAITag> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICustomer::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICustomer::is_tags_Valid() const{
    return m_tags_isValid;
}

QDateTime OAICustomer::getUpdatedTime() const {
    return m_updated_time;
}
void OAICustomer::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAICustomer::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAICustomer::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAICustomer::getWebsiteId() const {
    return m_website_id;
}
void OAICustomer::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAICustomer::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAICustomer::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAICustomer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__embedded.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_average_value.isSet()) {
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

        if (m_default_payment_instrument.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_payment_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lifetime_revenue.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
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

bool OAICustomer::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
