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

#include "OAICommonPlan_recurringInterval.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommonPlan_recurringInterval::OAICommonPlan_recurringInterval(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommonPlan_recurringInterval::OAICommonPlan_recurringInterval() {
    this->initializeModel();
}

OAICommonPlan_recurringInterval::~OAICommonPlan_recurringInterval() {}

void OAICommonPlan_recurringInterval::initializeModel() {

    m_length_isSet = false;
    m_length_isValid = false;

    m_unit_isSet = false;
    m_unit_isValid = false;

    m_billing_timing_isSet = false;
    m_billing_timing_isValid = false;

    m_limit_isSet = false;
    m_limit_isValid = false;
}

void OAICommonPlan_recurringInterval::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommonPlan_recurringInterval::fromJsonObject(QJsonObject json) {

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;

    m_billing_timing_isValid = ::OpenAPI::fromJsonValue(m_billing_timing, json[QString("billingTiming")]);
    m_billing_timing_isSet = !json[QString("billingTiming")].isNull() && m_billing_timing_isValid;

    m_limit_isValid = ::OpenAPI::fromJsonValue(m_limit, json[QString("limit")]);
    m_limit_isSet = !json[QString("limit")].isNull() && m_limit_isValid;
}

QString OAICommonPlan_recurringInterval::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommonPlan_recurringInterval::asJsonObject() const {
    QJsonObject obj;
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    if (m_billing_timing.isSet()) {
        obj.insert(QString("billingTiming"), ::OpenAPI::toJsonValue(m_billing_timing));
    }
    if (m_limit_isSet) {
        obj.insert(QString("limit"), ::OpenAPI::toJsonValue(m_limit));
    }
    return obj;
}

qint32 OAICommonPlan_recurringInterval::getLength() const {
    return m_length;
}
void OAICommonPlan_recurringInterval::setLength(const qint32 &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAICommonPlan_recurringInterval::is_length_Set() const{
    return m_length_isSet;
}

bool OAICommonPlan_recurringInterval::is_length_Valid() const{
    return m_length_isValid;
}

QString OAICommonPlan_recurringInterval::getUnit() const {
    return m_unit;
}
void OAICommonPlan_recurringInterval::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAICommonPlan_recurringInterval::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAICommonPlan_recurringInterval::is_unit_Valid() const{
    return m_unit_isValid;
}

OAIPlanBillingTiming OAICommonPlan_recurringInterval::getBillingTiming() const {
    return m_billing_timing;
}
void OAICommonPlan_recurringInterval::setBillingTiming(const OAIPlanBillingTiming &billing_timing) {
    m_billing_timing = billing_timing;
    m_billing_timing_isSet = true;
}

bool OAICommonPlan_recurringInterval::is_billing_timing_Set() const{
    return m_billing_timing_isSet;
}

bool OAICommonPlan_recurringInterval::is_billing_timing_Valid() const{
    return m_billing_timing_isValid;
}

qint32 OAICommonPlan_recurringInterval::getLimit() const {
    return m_limit;
}
void OAICommonPlan_recurringInterval::setLimit(const qint32 &limit) {
    m_limit = limit;
    m_limit_isSet = true;
}

bool OAICommonPlan_recurringInterval::is_limit_Set() const{
    return m_limit_isSet;
}

bool OAICommonPlan_recurringInterval::is_limit_Valid() const{
    return m_limit_isValid;
}

bool OAICommonPlan_recurringInterval::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_timing.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_limit_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommonPlan_recurringInterval::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_length_isValid && m_unit_isValid && true;
}

} // namespace OpenAPI
