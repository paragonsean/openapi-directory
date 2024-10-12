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

#include "OAIPostPaymentCard_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPostPaymentCard_request::OAIPostPaymentCard_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPostPaymentCard_request::OAIPostPaymentCard_request() {
    this->initializeModel();
}

OAIPostPaymentCard_request::~OAIPostPaymentCard_request() {}

void OAIPostPaymentCard_request::initializeModel() {

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_cvv_isSet = false;
    m_cvv_isValid = false;

    m_exp_month_isSet = false;
    m_exp_month_isValid = false;

    m_exp_year_isSet = false;
    m_exp_year_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_pan_isSet = false;
    m_pan_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;
}

void OAIPostPaymentCard_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPostPaymentCard_request::fromJsonObject(QJsonObject json) {

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_cvv_isValid = ::OpenAPI::fromJsonValue(m_cvv, json[QString("cvv")]);
    m_cvv_isSet = !json[QString("cvv")].isNull() && m_cvv_isValid;

    m_exp_month_isValid = ::OpenAPI::fromJsonValue(m_exp_month, json[QString("expMonth")]);
    m_exp_month_isSet = !json[QString("expMonth")].isNull() && m_exp_month_isValid;

    m_exp_year_isValid = ::OpenAPI::fromJsonValue(m_exp_year, json[QString("expYear")]);
    m_exp_year_isSet = !json[QString("expYear")].isNull() && m_exp_year_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_pan_isValid = ::OpenAPI::fromJsonValue(m_pan, json[QString("pan")]);
    m_pan_isSet = !json[QString("pan")].isNull() && m_pan_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;
}

QString OAIPostPaymentCard_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPostPaymentCard_request::asJsonObject() const {
    QJsonObject obj;
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_cvv_isSet) {
        obj.insert(QString("cvv"), ::OpenAPI::toJsonValue(m_cvv));
    }
    if (m_exp_month_isSet) {
        obj.insert(QString("expMonth"), ::OpenAPI::toJsonValue(m_exp_month));
    }
    if (m_exp_year_isSet) {
        obj.insert(QString("expYear"), ::OpenAPI::toJsonValue(m_exp_year));
    }
    if (m_method_isSet) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_pan_isSet) {
        obj.insert(QString("pan"), ::OpenAPI::toJsonValue(m_pan));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    return obj;
}

OAIObject OAIPostPaymentCard_request::getCustomFields() const {
    return m_custom_fields;
}
void OAIPostPaymentCard_request::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIPostPaymentCard_request::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIPostPaymentCard_request::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIPostPaymentCard_request::getCustomerId() const {
    return m_customer_id;
}
void OAIPostPaymentCard_request::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIPostPaymentCard_request::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIPostPaymentCard_request::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAIPostPaymentCard_request::getToken() const {
    return m_token;
}
void OAIPostPaymentCard_request::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIPostPaymentCard_request::is_token_Set() const{
    return m_token_isSet;
}

bool OAIPostPaymentCard_request::is_token_Valid() const{
    return m_token_isValid;
}

OAIContactObject OAIPostPaymentCard_request::getBillingAddress() const {
    return m_billing_address;
}
void OAIPostPaymentCard_request::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIPostPaymentCard_request::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIPostPaymentCard_request::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIPostPaymentCard_request::getCvv() const {
    return m_cvv;
}
void OAIPostPaymentCard_request::setCvv(const QString &cvv) {
    m_cvv = cvv;
    m_cvv_isSet = true;
}

bool OAIPostPaymentCard_request::is_cvv_Set() const{
    return m_cvv_isSet;
}

bool OAIPostPaymentCard_request::is_cvv_Valid() const{
    return m_cvv_isValid;
}

qint32 OAIPostPaymentCard_request::getExpMonth() const {
    return m_exp_month;
}
void OAIPostPaymentCard_request::setExpMonth(const qint32 &exp_month) {
    m_exp_month = exp_month;
    m_exp_month_isSet = true;
}

bool OAIPostPaymentCard_request::is_exp_month_Set() const{
    return m_exp_month_isSet;
}

bool OAIPostPaymentCard_request::is_exp_month_Valid() const{
    return m_exp_month_isValid;
}

qint32 OAIPostPaymentCard_request::getExpYear() const {
    return m_exp_year;
}
void OAIPostPaymentCard_request::setExpYear(const qint32 &exp_year) {
    m_exp_year = exp_year;
    m_exp_year_isSet = true;
}

bool OAIPostPaymentCard_request::is_exp_year_Set() const{
    return m_exp_year_isSet;
}

bool OAIPostPaymentCard_request::is_exp_year_Valid() const{
    return m_exp_year_isValid;
}

QString OAIPostPaymentCard_request::getMethod() const {
    return m_method;
}
void OAIPostPaymentCard_request::setMethod(const QString &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAIPostPaymentCard_request::is_method_Set() const{
    return m_method_isSet;
}

bool OAIPostPaymentCard_request::is_method_Valid() const{
    return m_method_isValid;
}

QString OAIPostPaymentCard_request::getPan() const {
    return m_pan;
}
void OAIPostPaymentCard_request::setPan(const QString &pan) {
    m_pan = pan;
    m_pan_isSet = true;
}

bool OAIPostPaymentCard_request::is_pan_Set() const{
    return m_pan_isSet;
}

bool OAIPostPaymentCard_request::is_pan_Valid() const{
    return m_pan_isValid;
}

OAIRiskMetadata OAIPostPaymentCard_request::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAIPostPaymentCard_request::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAIPostPaymentCard_request::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAIPostPaymentCard_request::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

bool OAIPostPaymentCard_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cvv_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_month_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pan_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPostPaymentCard_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_customer_id_isValid && m_token_isValid && m_billing_address_isValid && m_exp_month_isValid && m_exp_year_isValid && m_method_isValid && m_pan_isValid && true;
}

} // namespace OpenAPI
