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

#include "OAISearch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISearch::OAISearch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISearch::OAISearch() {
    this->initializeModel();
}

OAISearch::~OAISearch() {}

void OAISearch::initializeModel() {

    m_customers_isSet = false;
    m_customers_isValid = false;

    m_invoices_isSet = false;
    m_invoices_isValid = false;

    m_orders_isSet = false;
    m_orders_isValid = false;

    m_searched_isSet = false;
    m_searched_isValid = false;

    m_transactions_isSet = false;
    m_transactions_isValid = false;
}

void OAISearch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISearch::fromJsonObject(QJsonObject json) {

    m_customers_isValid = ::OpenAPI::fromJsonValue(m_customers, json[QString("customers")]);
    m_customers_isSet = !json[QString("customers")].isNull() && m_customers_isValid;

    m_invoices_isValid = ::OpenAPI::fromJsonValue(m_invoices, json[QString("invoices")]);
    m_invoices_isSet = !json[QString("invoices")].isNull() && m_invoices_isValid;

    m_orders_isValid = ::OpenAPI::fromJsonValue(m_orders, json[QString("orders")]);
    m_orders_isSet = !json[QString("orders")].isNull() && m_orders_isValid;

    m_searched_isValid = ::OpenAPI::fromJsonValue(m_searched, json[QString("searched")]);
    m_searched_isSet = !json[QString("searched")].isNull() && m_searched_isValid;

    m_transactions_isValid = ::OpenAPI::fromJsonValue(m_transactions, json[QString("transactions")]);
    m_transactions_isSet = !json[QString("transactions")].isNull() && m_transactions_isValid;
}

QString OAISearch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISearch::asJsonObject() const {
    QJsonObject obj;
    if (m_customers.size() > 0) {
        obj.insert(QString("customers"), ::OpenAPI::toJsonValue(m_customers));
    }
    if (m_invoices.size() > 0) {
        obj.insert(QString("invoices"), ::OpenAPI::toJsonValue(m_invoices));
    }
    if (m_orders.size() > 0) {
        obj.insert(QString("orders"), ::OpenAPI::toJsonValue(m_orders));
    }
    if (m_searched.size() > 0) {
        obj.insert(QString("searched"), ::OpenAPI::toJsonValue(m_searched));
    }
    if (m_transactions.size() > 0) {
        obj.insert(QString("transactions"), ::OpenAPI::toJsonValue(m_transactions));
    }
    return obj;
}

QList<OAICustomer> OAISearch::getCustomers() const {
    return m_customers;
}
void OAISearch::setCustomers(const QList<OAICustomer> &customers) {
    m_customers = customers;
    m_customers_isSet = true;
}

bool OAISearch::is_customers_Set() const{
    return m_customers_isSet;
}

bool OAISearch::is_customers_Valid() const{
    return m_customers_isValid;
}

QList<OAIInvoice> OAISearch::getInvoices() const {
    return m_invoices;
}
void OAISearch::setInvoices(const QList<OAIInvoice> &invoices) {
    m_invoices = invoices;
    m_invoices_isSet = true;
}

bool OAISearch::is_invoices_Set() const{
    return m_invoices_isSet;
}

bool OAISearch::is_invoices_Valid() const{
    return m_invoices_isValid;
}

QList<OAISubscription> OAISearch::getOrders() const {
    return m_orders;
}
void OAISearch::setOrders(const QList<OAISubscription> &orders) {
    m_orders = orders;
    m_orders_isSet = true;
}

bool OAISearch::is_orders_Set() const{
    return m_orders_isSet;
}

bool OAISearch::is_orders_Valid() const{
    return m_orders_isValid;
}

QList<QString> OAISearch::getSearched() const {
    return m_searched;
}
void OAISearch::setSearched(const QList<QString> &searched) {
    m_searched = searched;
    m_searched_isSet = true;
}

bool OAISearch::is_searched_Set() const{
    return m_searched_isSet;
}

bool OAISearch::is_searched_Valid() const{
    return m_searched_isValid;
}

QList<OAITransaction> OAISearch::getTransactions() const {
    return m_transactions;
}
void OAISearch::setTransactions(const QList<OAITransaction> &transactions) {
    m_transactions = transactions;
    m_transactions_isSet = true;
}

bool OAISearch::is_transactions_Set() const{
    return m_transactions_isSet;
}

bool OAISearch::is_transactions_Valid() const{
    return m_transactions_isValid;
}

bool OAISearch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_customers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_orders.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_searched.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_transactions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISearch::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
