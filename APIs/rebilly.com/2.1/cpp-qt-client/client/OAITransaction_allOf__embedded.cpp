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

#include "OAITransaction_allOf__embedded.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransaction_allOf__embedded::OAITransaction_allOf__embedded(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransaction_allOf__embedded::OAITransaction_allOf__embedded() {
    this->initializeModel();
}

OAITransaction_allOf__embedded::~OAITransaction_allOf__embedded() {}

void OAITransaction_allOf__embedded::initializeModel() {

    m_parent_transaction_isSet = false;
    m_parent_transaction_isValid = false;

    m_retried_transaction_isSet = false;
    m_retried_transaction_isValid = false;

    m_gateway_account_isSet = false;
    m_gateway_account_isValid = false;

    m_customer_isSet = false;
    m_customer_isValid = false;

    m_lead_source_isSet = false;
    m_lead_source_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;

    m_payment_card_isSet = false;
    m_payment_card_isValid = false;

    m_bank_account_isSet = false;
    m_bank_account_isValid = false;

    m_invoices_isSet = false;
    m_invoices_isValid = false;
}

void OAITransaction_allOf__embedded::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransaction_allOf__embedded::fromJsonObject(QJsonObject json) {

    m_parent_transaction_isValid = ::OpenAPI::fromJsonValue(m_parent_transaction, json[QString("parentTransaction")]);
    m_parent_transaction_isSet = !json[QString("parentTransaction")].isNull() && m_parent_transaction_isValid;

    m_retried_transaction_isValid = ::OpenAPI::fromJsonValue(m_retried_transaction, json[QString("retriedTransaction")]);
    m_retried_transaction_isSet = !json[QString("retriedTransaction")].isNull() && m_retried_transaction_isValid;

    m_gateway_account_isValid = ::OpenAPI::fromJsonValue(m_gateway_account, json[QString("gatewayAccount")]);
    m_gateway_account_isSet = !json[QString("gatewayAccount")].isNull() && m_gateway_account_isValid;

    m_customer_isValid = ::OpenAPI::fromJsonValue(m_customer, json[QString("customer")]);
    m_customer_isSet = !json[QString("customer")].isNull() && m_customer_isValid;

    m_lead_source_isValid = ::OpenAPI::fromJsonValue(m_lead_source, json[QString("leadSource")]);
    m_lead_source_isSet = !json[QString("leadSource")].isNull() && m_lead_source_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;

    m_payment_card_isValid = ::OpenAPI::fromJsonValue(m_payment_card, json[QString("paymentCard")]);
    m_payment_card_isSet = !json[QString("paymentCard")].isNull() && m_payment_card_isValid;

    m_bank_account_isValid = ::OpenAPI::fromJsonValue(m_bank_account, json[QString("bankAccount")]);
    m_bank_account_isSet = !json[QString("bankAccount")].isNull() && m_bank_account_isValid;

    m_invoices_isValid = ::OpenAPI::fromJsonValue(m_invoices, json[QString("invoices")]);
    m_invoices_isSet = !json[QString("invoices")].isNull() && m_invoices_isValid;
}

QString OAITransaction_allOf__embedded::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransaction_allOf__embedded::asJsonObject() const {
    QJsonObject obj;
    if (m_parent_transaction.isSet()) {
        obj.insert(QString("parentTransaction"), ::OpenAPI::toJsonValue(m_parent_transaction));
    }
    if (m_retried_transaction.isSet()) {
        obj.insert(QString("retriedTransaction"), ::OpenAPI::toJsonValue(m_retried_transaction));
    }
    if (m_gateway_account.isSet()) {
        obj.insert(QString("gatewayAccount"), ::OpenAPI::toJsonValue(m_gateway_account));
    }
    if (m_customer.isSet()) {
        obj.insert(QString("customer"), ::OpenAPI::toJsonValue(m_customer));
    }
    if (m_lead_source.isSet()) {
        obj.insert(QString("leadSource"), ::OpenAPI::toJsonValue(m_lead_source));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    if (m_payment_card.isSet()) {
        obj.insert(QString("paymentCard"), ::OpenAPI::toJsonValue(m_payment_card));
    }
    if (m_bank_account.isSet()) {
        obj.insert(QString("bankAccount"), ::OpenAPI::toJsonValue(m_bank_account));
    }
    if (m_invoices.size() > 0) {
        obj.insert(QString("invoices"), ::OpenAPI::toJsonValue(m_invoices));
    }
    return obj;
}

OAITransaction OAITransaction_allOf__embedded::getParentTransaction() const {
    return m_parent_transaction;
}
void OAITransaction_allOf__embedded::setParentTransaction(const OAITransaction &parent_transaction) {
    m_parent_transaction = parent_transaction;
    m_parent_transaction_isSet = true;
}

bool OAITransaction_allOf__embedded::is_parent_transaction_Set() const{
    return m_parent_transaction_isSet;
}

bool OAITransaction_allOf__embedded::is_parent_transaction_Valid() const{
    return m_parent_transaction_isValid;
}

OAITransaction OAITransaction_allOf__embedded::getRetriedTransaction() const {
    return m_retried_transaction;
}
void OAITransaction_allOf__embedded::setRetriedTransaction(const OAITransaction &retried_transaction) {
    m_retried_transaction = retried_transaction;
    m_retried_transaction_isSet = true;
}

bool OAITransaction_allOf__embedded::is_retried_transaction_Set() const{
    return m_retried_transaction_isSet;
}

bool OAITransaction_allOf__embedded::is_retried_transaction_Valid() const{
    return m_retried_transaction_isValid;
}

OAIGatewayAccount OAITransaction_allOf__embedded::getGatewayAccount() const {
    return m_gateway_account;
}
void OAITransaction_allOf__embedded::setGatewayAccount(const OAIGatewayAccount &gateway_account) {
    m_gateway_account = gateway_account;
    m_gateway_account_isSet = true;
}

bool OAITransaction_allOf__embedded::is_gateway_account_Set() const{
    return m_gateway_account_isSet;
}

bool OAITransaction_allOf__embedded::is_gateway_account_Valid() const{
    return m_gateway_account_isValid;
}

OAICustomer OAITransaction_allOf__embedded::getCustomer() const {
    return m_customer;
}
void OAITransaction_allOf__embedded::setCustomer(const OAICustomer &customer) {
    m_customer = customer;
    m_customer_isSet = true;
}

bool OAITransaction_allOf__embedded::is_customer_Set() const{
    return m_customer_isSet;
}

bool OAITransaction_allOf__embedded::is_customer_Valid() const{
    return m_customer_isValid;
}

OAILeadSource OAITransaction_allOf__embedded::getLeadSource() const {
    return m_lead_source;
}
void OAITransaction_allOf__embedded::setLeadSource(const OAILeadSource &lead_source) {
    m_lead_source = lead_source;
    m_lead_source_isSet = true;
}

bool OAITransaction_allOf__embedded::is_lead_source_Set() const{
    return m_lead_source_isSet;
}

bool OAITransaction_allOf__embedded::is_lead_source_Valid() const{
    return m_lead_source_isValid;
}

OAIObject OAITransaction_allOf__embedded::getWebsite() const {
    return m_website;
}
void OAITransaction_allOf__embedded::setWebsite(const OAIObject &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAITransaction_allOf__embedded::is_website_Set() const{
    return m_website_isSet;
}

bool OAITransaction_allOf__embedded::is_website_Valid() const{
    return m_website_isValid;
}

OAIPaymentCard OAITransaction_allOf__embedded::getPaymentCard() const {
    return m_payment_card;
}
void OAITransaction_allOf__embedded::setPaymentCard(const OAIPaymentCard &payment_card) {
    m_payment_card = payment_card;
    m_payment_card_isSet = true;
}

bool OAITransaction_allOf__embedded::is_payment_card_Set() const{
    return m_payment_card_isSet;
}

bool OAITransaction_allOf__embedded::is_payment_card_Valid() const{
    return m_payment_card_isValid;
}

OAIBankAccount OAITransaction_allOf__embedded::getBankAccount() const {
    return m_bank_account;
}
void OAITransaction_allOf__embedded::setBankAccount(const OAIBankAccount &bank_account) {
    m_bank_account = bank_account;
    m_bank_account_isSet = true;
}

bool OAITransaction_allOf__embedded::is_bank_account_Set() const{
    return m_bank_account_isSet;
}

bool OAITransaction_allOf__embedded::is_bank_account_Valid() const{
    return m_bank_account_isValid;
}

QList<OAIInvoice> OAITransaction_allOf__embedded::getInvoices() const {
    return m_invoices;
}
void OAITransaction_allOf__embedded::setInvoices(const QList<OAIInvoice> &invoices) {
    m_invoices = invoices;
    m_invoices_isSet = true;
}

bool OAITransaction_allOf__embedded::is_invoices_Set() const{
    return m_invoices_isSet;
}

bool OAITransaction_allOf__embedded::is_invoices_Valid() const{
    return m_invoices_isValid;
}

bool OAITransaction_allOf__embedded::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_parent_transaction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_retried_transaction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_lead_source.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_card.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoices.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransaction_allOf__embedded::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
