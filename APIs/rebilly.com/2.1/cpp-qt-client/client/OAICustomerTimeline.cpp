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

#include "OAICustomerTimeline.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerTimeline::OAICustomerTimeline(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerTimeline::OAICustomerTimeline() {
    this->initializeModel();
}

OAICustomerTimeline::~OAICustomerTimeline() {}

void OAICustomerTimeline::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_custom_data_isSet = false;
    m_custom_data_isValid = false;

    m_custom_event_type_isSet = false;
    m_custom_event_type_isValid = false;

    m_extra_data_isSet = false;
    m_extra_data_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;

    m_occurred_time_isSet = false;
    m_occurred_time_isValid = false;

    m_triggered_by_isSet = false;
    m_triggered_by_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICustomerTimeline::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerTimeline::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_custom_data_isValid = ::OpenAPI::fromJsonValue(m_custom_data, json[QString("customData")]);
    m_custom_data_isSet = !json[QString("customData")].isNull() && m_custom_data_isValid;

    m_custom_event_type_isValid = ::OpenAPI::fromJsonValue(m_custom_event_type, json[QString("customEventType")]);
    m_custom_event_type_isSet = !json[QString("customEventType")].isNull() && m_custom_event_type_isValid;

    m_extra_data_isValid = ::OpenAPI::fromJsonValue(m_extra_data, json[QString("extraData")]);
    m_extra_data_isSet = !json[QString("extraData")].isNull() && m_extra_data_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_occurred_time_isValid = ::OpenAPI::fromJsonValue(m_occurred_time, json[QString("occurredTime")]);
    m_occurred_time_isSet = !json[QString("occurredTime")].isNull() && m_occurred_time_isValid;

    m_triggered_by_isValid = ::OpenAPI::fromJsonValue(m_triggered_by, json[QString("triggeredBy")]);
    m_triggered_by_isSet = !json[QString("triggeredBy")].isNull() && m_triggered_by_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAICustomerTimeline::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerTimeline::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_custom_data_isSet) {
        obj.insert(QString("customData"), ::OpenAPI::toJsonValue(m_custom_data));
    }
    if (m_custom_event_type_isSet) {
        obj.insert(QString("customEventType"), ::OpenAPI::toJsonValue(m_custom_event_type));
    }
    if (m_extra_data.isSet()) {
        obj.insert(QString("extraData"), ::OpenAPI::toJsonValue(m_extra_data));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_occurred_time_isSet) {
        obj.insert(QString("occurredTime"), ::OpenAPI::toJsonValue(m_occurred_time));
    }
    if (m_triggered_by_isSet) {
        obj.insert(QString("triggeredBy"), ::OpenAPI::toJsonValue(m_triggered_by));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QList<OAISelfLink> OAICustomerTimeline::getLinks() const {
    return m__links;
}
void OAICustomerTimeline::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAICustomerTimeline::is__links_Set() const{
    return m__links_isSet;
}

bool OAICustomerTimeline::is__links_Valid() const{
    return m__links_isValid;
}

OAIObject OAICustomerTimeline::getCustomData() const {
    return m_custom_data;
}
void OAICustomerTimeline::setCustomData(const OAIObject &custom_data) {
    m_custom_data = custom_data;
    m_custom_data_isSet = true;
}

bool OAICustomerTimeline::is_custom_data_Set() const{
    return m_custom_data_isSet;
}

bool OAICustomerTimeline::is_custom_data_Valid() const{
    return m_custom_data_isValid;
}

QString OAICustomerTimeline::getCustomEventType() const {
    return m_custom_event_type;
}
void OAICustomerTimeline::setCustomEventType(const QString &custom_event_type) {
    m_custom_event_type = custom_event_type;
    m_custom_event_type_isSet = true;
}

bool OAICustomerTimeline::is_custom_event_type_Set() const{
    return m_custom_event_type_isSet;
}

bool OAICustomerTimeline::is_custom_event_type_Valid() const{
    return m_custom_event_type_isValid;
}

OAITimelineExtraData OAICustomerTimeline::getExtraData() const {
    return m_extra_data;
}
void OAICustomerTimeline::setExtraData(const OAITimelineExtraData &extra_data) {
    m_extra_data = extra_data;
    m_extra_data_isSet = true;
}

bool OAICustomerTimeline::is_extra_data_Set() const{
    return m_extra_data_isSet;
}

bool OAICustomerTimeline::is_extra_data_Valid() const{
    return m_extra_data_isValid;
}

QString OAICustomerTimeline::getId() const {
    return m_id;
}
void OAICustomerTimeline::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomerTimeline::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomerTimeline::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICustomerTimeline::getMessage() const {
    return m_message;
}
void OAICustomerTimeline::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAICustomerTimeline::is_message_Set() const{
    return m_message_isSet;
}

bool OAICustomerTimeline::is_message_Valid() const{
    return m_message_isValid;
}

QDateTime OAICustomerTimeline::getOccurredTime() const {
    return m_occurred_time;
}
void OAICustomerTimeline::setOccurredTime(const QDateTime &occurred_time) {
    m_occurred_time = occurred_time;
    m_occurred_time_isSet = true;
}

bool OAICustomerTimeline::is_occurred_time_Set() const{
    return m_occurred_time_isSet;
}

bool OAICustomerTimeline::is_occurred_time_Valid() const{
    return m_occurred_time_isValid;
}

QString OAICustomerTimeline::getTriggeredBy() const {
    return m_triggered_by;
}
void OAICustomerTimeline::setTriggeredBy(const QString &triggered_by) {
    m_triggered_by = triggered_by;
    m_triggered_by_isSet = true;
}

bool OAICustomerTimeline::is_triggered_by_Set() const{
    return m_triggered_by_isSet;
}

bool OAICustomerTimeline::is_triggered_by_Valid() const{
    return m_triggered_by_isValid;
}

QString OAICustomerTimeline::getType() const {
    return m_type;
}
void OAICustomerTimeline::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICustomerTimeline::is_type_Set() const{
    return m_type_isSet;
}

bool OAICustomerTimeline::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICustomerTimeline::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_event_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extra_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_occurred_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_triggered_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerTimeline::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
