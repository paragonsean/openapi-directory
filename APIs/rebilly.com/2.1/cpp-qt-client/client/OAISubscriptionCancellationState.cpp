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

#include "OAISubscriptionCancellationState.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISubscriptionCancellationState::OAISubscriptionCancellationState(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISubscriptionCancellationState::OAISubscriptionCancellationState() {
    this->initializeModel();
}

OAISubscriptionCancellationState::~OAISubscriptionCancellationState() {}

void OAISubscriptionCancellationState::initializeModel() {

    m_cancel_category_isSet = false;
    m_cancel_category_isValid = false;

    m_cancel_description_isSet = false;
    m_cancel_description_isValid = false;

    m_canceled_by_isSet = false;
    m_canceled_by_isValid = false;

    m_canceled_time_isSet = false;
    m_canceled_time_isValid = false;
}

void OAISubscriptionCancellationState::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISubscriptionCancellationState::fromJsonObject(QJsonObject json) {

    m_cancel_category_isValid = ::OpenAPI::fromJsonValue(m_cancel_category, json[QString("cancelCategory")]);
    m_cancel_category_isSet = !json[QString("cancelCategory")].isNull() && m_cancel_category_isValid;

    m_cancel_description_isValid = ::OpenAPI::fromJsonValue(m_cancel_description, json[QString("cancelDescription")]);
    m_cancel_description_isSet = !json[QString("cancelDescription")].isNull() && m_cancel_description_isValid;

    m_canceled_by_isValid = ::OpenAPI::fromJsonValue(m_canceled_by, json[QString("canceledBy")]);
    m_canceled_by_isSet = !json[QString("canceledBy")].isNull() && m_canceled_by_isValid;

    m_canceled_time_isValid = ::OpenAPI::fromJsonValue(m_canceled_time, json[QString("canceledTime")]);
    m_canceled_time_isSet = !json[QString("canceledTime")].isNull() && m_canceled_time_isValid;
}

QString OAISubscriptionCancellationState::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISubscriptionCancellationState::asJsonObject() const {
    QJsonObject obj;
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
    return obj;
}

QString OAISubscriptionCancellationState::getCancelCategory() const {
    return m_cancel_category;
}
void OAISubscriptionCancellationState::setCancelCategory(const QString &cancel_category) {
    m_cancel_category = cancel_category;
    m_cancel_category_isSet = true;
}

bool OAISubscriptionCancellationState::is_cancel_category_Set() const{
    return m_cancel_category_isSet;
}

bool OAISubscriptionCancellationState::is_cancel_category_Valid() const{
    return m_cancel_category_isValid;
}

QString OAISubscriptionCancellationState::getCancelDescription() const {
    return m_cancel_description;
}
void OAISubscriptionCancellationState::setCancelDescription(const QString &cancel_description) {
    m_cancel_description = cancel_description;
    m_cancel_description_isSet = true;
}

bool OAISubscriptionCancellationState::is_cancel_description_Set() const{
    return m_cancel_description_isSet;
}

bool OAISubscriptionCancellationState::is_cancel_description_Valid() const{
    return m_cancel_description_isValid;
}

QString OAISubscriptionCancellationState::getCanceledBy() const {
    return m_canceled_by;
}
void OAISubscriptionCancellationState::setCanceledBy(const QString &canceled_by) {
    m_canceled_by = canceled_by;
    m_canceled_by_isSet = true;
}

bool OAISubscriptionCancellationState::is_canceled_by_Set() const{
    return m_canceled_by_isSet;
}

bool OAISubscriptionCancellationState::is_canceled_by_Valid() const{
    return m_canceled_by_isValid;
}

QDateTime OAISubscriptionCancellationState::getCanceledTime() const {
    return m_canceled_time;
}
void OAISubscriptionCancellationState::setCanceledTime(const QDateTime &canceled_time) {
    m_canceled_time = canceled_time;
    m_canceled_time_isSet = true;
}

bool OAISubscriptionCancellationState::is_canceled_time_Set() const{
    return m_canceled_time_isSet;
}

bool OAISubscriptionCancellationState::is_canceled_time_Valid() const{
    return m_canceled_time_isValid;
}

bool OAISubscriptionCancellationState::isSet() const {
    bool isObjectUpdated = false;
    do {
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
    } while (false);
    return isObjectUpdated;
}

bool OAISubscriptionCancellationState::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
