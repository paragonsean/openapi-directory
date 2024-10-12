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

#include "OAICoupon.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICoupon::OAICoupon(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICoupon::OAICoupon() {
    this->initializeModel();
}

OAICoupon::~OAICoupon() {}

void OAICoupon::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_isSet = false;
    m_discount_isValid = false;

    m_expired_time_isSet = false;
    m_expired_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_issued_time_isSet = false;
    m_issued_time_isValid = false;

    m_redemptions_count_isSet = false;
    m_redemptions_count_isValid = false;

    m_restrictions_isSet = false;
    m_restrictions_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAICoupon::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICoupon::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_discount_isValid = ::OpenAPI::fromJsonValue(m_discount, json[QString("discount")]);
    m_discount_isSet = !json[QString("discount")].isNull() && m_discount_isValid;

    m_expired_time_isValid = ::OpenAPI::fromJsonValue(m_expired_time, json[QString("expiredTime")]);
    m_expired_time_isSet = !json[QString("expiredTime")].isNull() && m_expired_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_issued_time_isValid = ::OpenAPI::fromJsonValue(m_issued_time, json[QString("issuedTime")]);
    m_issued_time_isSet = !json[QString("issuedTime")].isNull() && m_issued_time_isValid;

    m_redemptions_count_isValid = ::OpenAPI::fromJsonValue(m_redemptions_count, json[QString("redemptionsCount")]);
    m_redemptions_count_isSet = !json[QString("redemptionsCount")].isNull() && m_redemptions_count_isValid;

    m_restrictions_isValid = ::OpenAPI::fromJsonValue(m_restrictions, json[QString("restrictions")]);
    m_restrictions_isSet = !json[QString("restrictions")].isNull() && m_restrictions_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAICoupon::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICoupon::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount.isSet()) {
        obj.insert(QString("discount"), ::OpenAPI::toJsonValue(m_discount));
    }
    if (m_expired_time_isSet) {
        obj.insert(QString("expiredTime"), ::OpenAPI::toJsonValue(m_expired_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_issued_time_isSet) {
        obj.insert(QString("issuedTime"), ::OpenAPI::toJsonValue(m_issued_time));
    }
    if (m_redemptions_count_isSet) {
        obj.insert(QString("redemptionsCount"), ::OpenAPI::toJsonValue(m_redemptions_count));
    }
    if (m_restrictions.size() > 0) {
        obj.insert(QString("restrictions"), ::OpenAPI::toJsonValue(m_restrictions));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QList<OAISelfLink> OAICoupon::getLinks() const {
    return m__links;
}
void OAICoupon::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAICoupon::is__links_Set() const{
    return m__links_isSet;
}

bool OAICoupon::is__links_Valid() const{
    return m__links_isValid;
}

QDateTime OAICoupon::getCreatedTime() const {
    return m_created_time;
}
void OAICoupon::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAICoupon::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAICoupon::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAICoupon::getDescription() const {
    return m_description;
}
void OAICoupon::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICoupon::is_description_Set() const{
    return m_description_isSet;
}

bool OAICoupon::is_description_Valid() const{
    return m_description_isValid;
}

OAIDiscount OAICoupon::getDiscount() const {
    return m_discount;
}
void OAICoupon::setDiscount(const OAIDiscount &discount) {
    m_discount = discount;
    m_discount_isSet = true;
}

bool OAICoupon::is_discount_Set() const{
    return m_discount_isSet;
}

bool OAICoupon::is_discount_Valid() const{
    return m_discount_isValid;
}

QDateTime OAICoupon::getExpiredTime() const {
    return m_expired_time;
}
void OAICoupon::setExpiredTime(const QDateTime &expired_time) {
    m_expired_time = expired_time;
    m_expired_time_isSet = true;
}

bool OAICoupon::is_expired_time_Set() const{
    return m_expired_time_isSet;
}

bool OAICoupon::is_expired_time_Valid() const{
    return m_expired_time_isValid;
}

QString OAICoupon::getId() const {
    return m_id;
}
void OAICoupon::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICoupon::is_id_Set() const{
    return m_id_isSet;
}

bool OAICoupon::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAICoupon::getIssuedTime() const {
    return m_issued_time;
}
void OAICoupon::setIssuedTime(const QDateTime &issued_time) {
    m_issued_time = issued_time;
    m_issued_time_isSet = true;
}

bool OAICoupon::is_issued_time_Set() const{
    return m_issued_time_isSet;
}

bool OAICoupon::is_issued_time_Valid() const{
    return m_issued_time_isValid;
}

qint32 OAICoupon::getRedemptionsCount() const {
    return m_redemptions_count;
}
void OAICoupon::setRedemptionsCount(const qint32 &redemptions_count) {
    m_redemptions_count = redemptions_count;
    m_redemptions_count_isSet = true;
}

bool OAICoupon::is_redemptions_count_Set() const{
    return m_redemptions_count_isSet;
}

bool OAICoupon::is_redemptions_count_Valid() const{
    return m_redemptions_count_isValid;
}

QList<OAICouponRestriction> OAICoupon::getRestrictions() const {
    return m_restrictions;
}
void OAICoupon::setRestrictions(const QList<OAICouponRestriction> &restrictions) {
    m_restrictions = restrictions;
    m_restrictions_isSet = true;
}

bool OAICoupon::is_restrictions_Set() const{
    return m_restrictions_isSet;
}

bool OAICoupon::is_restrictions_Valid() const{
    return m_restrictions_isValid;
}

QString OAICoupon::getStatus() const {
    return m_status;
}
void OAICoupon::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICoupon::is_status_Set() const{
    return m_status_isSet;
}

bool OAICoupon::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAICoupon::getUpdatedTime() const {
    return m_updated_time;
}
void OAICoupon::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAICoupon::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAICoupon::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAICoupon::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
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

        if (m_discount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_expired_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_issued_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_redemptions_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_restrictions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICoupon::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_discount_isValid && m_issued_time_isValid && true;
}

} // namespace OpenAPI
