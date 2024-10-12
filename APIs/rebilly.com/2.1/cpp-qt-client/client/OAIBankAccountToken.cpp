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

#include "OAIBankAccountToken.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBankAccountToken::OAIBankAccountToken(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBankAccountToken::OAIBankAccountToken() {
    this->initializeModel();
}

OAIBankAccountToken::~OAIBankAccountToken() {}

void OAIBankAccountToken::initializeModel() {

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_payment_instrument_isSet = false;
    m_payment_instrument_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_expiration_time_isSet = false;
    m_expiration_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_used_isSet = false;
    m_is_used_isValid = false;

    m_lead_source_isSet = false;
    m_lead_source_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_usage_time_isSet = false;
    m_usage_time_isValid = false;
}

void OAIBankAccountToken::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBankAccountToken::fromJsonObject(QJsonObject json) {

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_payment_instrument_isValid = ::OpenAPI::fromJsonValue(m_payment_instrument, json[QString("paymentInstrument")]);
    m_payment_instrument_isSet = !json[QString("paymentInstrument")].isNull() && m_payment_instrument_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_expiration_time_isValid = ::OpenAPI::fromJsonValue(m_expiration_time, json[QString("expirationTime")]);
    m_expiration_time_isSet = !json[QString("expirationTime")].isNull() && m_expiration_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_used_isValid = ::OpenAPI::fromJsonValue(m_is_used, json[QString("isUsed")]);
    m_is_used_isSet = !json[QString("isUsed")].isNull() && m_is_used_isValid;

    m_lead_source_isValid = ::OpenAPI::fromJsonValue(m_lead_source, json[QString("leadSource")]);
    m_lead_source_isSet = !json[QString("leadSource")].isNull() && m_lead_source_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_usage_time_isValid = ::OpenAPI::fromJsonValue(m_usage_time, json[QString("usageTime")]);
    m_usage_time_isSet = !json[QString("usageTime")].isNull() && m_usage_time_isValid;
}

QString OAIBankAccountToken::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBankAccountToken::asJsonObject() const {
    QJsonObject obj;
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_method_isSet) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_payment_instrument.isSet()) {
        obj.insert(QString("paymentInstrument"), ::OpenAPI::toJsonValue(m_payment_instrument));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_expiration_time_isSet) {
        obj.insert(QString("expirationTime"), ::OpenAPI::toJsonValue(m_expiration_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_used_isSet) {
        obj.insert(QString("isUsed"), ::OpenAPI::toJsonValue(m_is_used));
    }
    if (m_lead_source.isSet()) {
        obj.insert(QString("leadSource"), ::OpenAPI::toJsonValue(m_lead_source));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_usage_time_isSet) {
        obj.insert(QString("usageTime"), ::OpenAPI::toJsonValue(m_usage_time));
    }
    return obj;
}

OAIContactObject OAIBankAccountToken::getBillingAddress() const {
    return m_billing_address;
}
void OAIBankAccountToken::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIBankAccountToken::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIBankAccountToken::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIBankAccountToken::getMethod() const {
    return m_method;
}
void OAIBankAccountToken::setMethod(const QString &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIBankAccountToken::is_method_Set() const{
    return m_method_isSet;
}

bool OAIBankAccountToken::is_method_Valid() const{
    return m_method_isValid;
}

OAIBankAccountInstrument OAIBankAccountToken::getPaymentInstrument() const {
    return m_payment_instrument;
}
void OAIBankAccountToken::setPaymentInstrument(const OAIBankAccountInstrument &payment_instrument) {
    m_payment_instrument = payment_instrument;
    m_payment_instrument_isSet = true;
}

bool OAIBankAccountToken::is_payment_instrument_Set() const{
    return m_payment_instrument_isSet;
}

bool OAIBankAccountToken::is_payment_instrument_Valid() const{
    return m_payment_instrument_isValid;
}

QList<OAISelfLink> OAIBankAccountToken::getLinks() const {
    return m__links;
}
void OAIBankAccountToken::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIBankAccountToken::is__links_Set() const{
    return m__links_isSet;
}

bool OAIBankAccountToken::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAIBankAccountToken::getCreatedTime() const {
    return m_created_time;
}
void OAIBankAccountToken::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIBankAccountToken::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIBankAccountToken::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QDateTime OAIBankAccountToken::getExpirationTime() const {
    return m_expiration_time;
}
void OAIBankAccountToken::setExpirationTime(const QDateTime &expiration_time) {
    m_expiration_time = expiration_time;
    m_expiration_time_isSet = true;
}

bool OAIBankAccountToken::is_expiration_time_Set() const{
    return m_expiration_time_isSet;
}

bool OAIBankAccountToken::is_expiration_time_Valid() const{
    return m_expiration_time_isValid;
}

QString OAIBankAccountToken::getId() const {
    return m_id;
}
void OAIBankAccountToken::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBankAccountToken::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBankAccountToken::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIBankAccountToken::isIsUsed() const {
    return m_is_used;
}
void OAIBankAccountToken::setIsUsed(const bool &is_used) {
    m_is_used = is_used;
    m_is_used_isSet = true;
}

bool OAIBankAccountToken::is_is_used_Set() const{
    return m_is_used_isSet;
}

bool OAIBankAccountToken::is_is_used_Valid() const{
    return m_is_used_isValid;
}

OAILeadSource OAIBankAccountToken::getLeadSource() const {
    return m_lead_source;
}
void OAIBankAccountToken::setLeadSource(const OAILeadSource &lead_source) {
    m_lead_source = lead_source;
    m_lead_source_isSet = true;
}

bool OAIBankAccountToken::is_lead_source_Set() const{
    return m_lead_source_isSet;
}

bool OAIBankAccountToken::is_lead_source_Valid() const{
    return m_lead_source_isValid;
}

OAIRiskMetadata OAIBankAccountToken::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAIBankAccountToken::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAIBankAccountToken::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAIBankAccountToken::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

QDateTime OAIBankAccountToken::getUpdatedTime() const {
    return m_updated_time;
}
void OAIBankAccountToken::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIBankAccountToken::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIBankAccountToken::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QDateTime OAIBankAccountToken::getUsageTime() const {
    return m_usage_time;
}
void OAIBankAccountToken::setUsageTime(const QDateTime &usage_time) {
    m_usage_time = usage_time;
    m_usage_time_isSet = true;
}

bool OAIBankAccountToken::is_usage_time_Set() const{
    return m_usage_time_isSet;
}

bool OAIBankAccountToken::is_usage_time_Valid() const{
    return m_usage_time_isValid;
}

bool OAIBankAccountToken::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instrument.isSet()) {
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

        if (m_expiration_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_used_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lead_source.isSet()) {
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

        if (m_usage_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBankAccountToken::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_billing_address_isValid && m_method_isValid && m_payment_instrument_isValid && true;
}

} // namespace OpenAPI
