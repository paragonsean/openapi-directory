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

#include "OAICustomerJWT.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerJWT::OAICustomerJWT(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerJWT::OAICustomerJWT() {
    this->initializeModel();
}

OAICustomerJWT::~OAICustomerJWT() {}

void OAICustomerJWT::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_acl_isSet = false;
    m_acl_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_custom_claims_isSet = false;
    m_custom_claims_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_expired_time_isSet = false;
    m_expired_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invalidate_isSet = false;
    m_invalidate_isValid = false;

    m_one_time_password_isSet = false;
    m_one_time_password_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAICustomerJWT::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerJWT::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_acl_isValid = ::OpenAPI::fromJsonValue(m_acl, json[QString("acl")]);
    m_acl_isSet = !json[QString("acl")].isNull() && m_acl_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_custom_claims_isValid = ::OpenAPI::fromJsonValue(m_custom_claims, json[QString("customClaims")]);
    m_custom_claims_isSet = !json[QString("customClaims")].isNull() && m_custom_claims_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_expired_time_isValid = ::OpenAPI::fromJsonValue(m_expired_time, json[QString("expiredTime")]);
    m_expired_time_isSet = !json[QString("expiredTime")].isNull() && m_expired_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invalidate_isValid = ::OpenAPI::fromJsonValue(m_invalidate, json[QString("invalidate")]);
    m_invalidate_isSet = !json[QString("invalidate")].isNull() && m_invalidate_isValid;

    m_one_time_password_isValid = ::OpenAPI::fromJsonValue(m_one_time_password, json[QString("oneTimePassword")]);
    m_one_time_password_isSet = !json[QString("oneTimePassword")].isNull() && m_one_time_password_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAICustomerJWT::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerJWT::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_acl.size() > 0) {
        obj.insert(QString("acl"), ::OpenAPI::toJsonValue(m_acl));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_custom_claims.size() > 0) {
        obj.insert(QString("customClaims"), ::OpenAPI::toJsonValue(m_custom_claims));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_expired_time_isSet) {
        obj.insert(QString("expiredTime"), ::OpenAPI::toJsonValue(m_expired_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invalidate_isSet) {
        obj.insert(QString("invalidate"), ::OpenAPI::toJsonValue(m_invalidate));
    }
    if (m_one_time_password_isSet) {
        obj.insert(QString("oneTimePassword"), ::OpenAPI::toJsonValue(m_one_time_password));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QList<OAICustomerLink> OAICustomerJWT::getLinks() const {
    return m__links;
}
void OAICustomerJWT::setLinks(const QList<OAICustomerLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAICustomerJWT::is__links_Set() const{
    return m__links_isSet;
}

bool OAICustomerJWT::is__links_Valid() const{
    return m__links_isValid;
}

QList<OAIAcl_inner> OAICustomerJWT::getAcl() const {
    return m_acl;
}
void OAICustomerJWT::setAcl(const QList<OAIAcl_inner> &acl) {
    m_acl = acl;
    m_acl_isSet = true;
}

bool OAICustomerJWT::is_acl_Set() const{
    return m_acl_isSet;
}

bool OAICustomerJWT::is_acl_Valid() const{
    return m_acl_isValid;
}

QDateTime OAICustomerJWT::getCreatedTime() const {
    return m_created_time;
}
void OAICustomerJWT::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAICustomerJWT::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAICustomerJWT::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QMap<QString, QJsonValue> OAICustomerJWT::getCustomClaims() const {
    return m_custom_claims;
}
void OAICustomerJWT::setCustomClaims(const QMap<QString, QJsonValue> &custom_claims) {
    m_custom_claims = custom_claims;
    m_custom_claims_isSet = true;
}

bool OAICustomerJWT::is_custom_claims_Set() const{
    return m_custom_claims_isSet;
}

bool OAICustomerJWT::is_custom_claims_Valid() const{
    return m_custom_claims_isValid;
}

QString OAICustomerJWT::getCustomerId() const {
    return m_customer_id;
}
void OAICustomerJWT::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAICustomerJWT::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAICustomerJWT::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QDateTime OAICustomerJWT::getExpiredTime() const {
    return m_expired_time;
}
void OAICustomerJWT::setExpiredTime(const QDateTime &expired_time) {
    m_expired_time = expired_time;
    m_expired_time_isSet = true;
}

bool OAICustomerJWT::is_expired_time_Set() const{
    return m_expired_time_isSet;
}

bool OAICustomerJWT::is_expired_time_Valid() const{
    return m_expired_time_isValid;
}

QString OAICustomerJWT::getId() const {
    return m_id;
}
void OAICustomerJWT::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomerJWT::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomerJWT::is_id_Valid() const{
    return m_id_isValid;
}

bool OAICustomerJWT::isInvalidate() const {
    return m_invalidate;
}
void OAICustomerJWT::setInvalidate(const bool &invalidate) {
    m_invalidate = invalidate;
    m_invalidate_isSet = true;
}

bool OAICustomerJWT::is_invalidate_Set() const{
    return m_invalidate_isSet;
}

bool OAICustomerJWT::is_invalidate_Valid() const{
    return m_invalidate_isValid;
}

QString OAICustomerJWT::getOneTimePassword() const {
    return m_one_time_password;
}
void OAICustomerJWT::setOneTimePassword(const QString &one_time_password) {
    m_one_time_password = one_time_password;
    m_one_time_password_isSet = true;
}

bool OAICustomerJWT::is_one_time_password_Set() const{
    return m_one_time_password_isSet;
}

bool OAICustomerJWT::is_one_time_password_Valid() const{
    return m_one_time_password_isValid;
}

QString OAICustomerJWT::getToken() const {
    return m_token;
}
void OAICustomerJWT::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAICustomerJWT::is_token_Set() const{
    return m_token_isSet;
}

bool OAICustomerJWT::is_token_Valid() const{
    return m_token_isValid;
}

QString OAICustomerJWT::getType() const {
    return m_type;
}
void OAICustomerJWT::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICustomerJWT::is_type_Set() const{
    return m_type_isSet;
}

bool OAICustomerJWT::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAICustomerJWT::getUpdatedTime() const {
    return m_updated_time;
}
void OAICustomerJWT::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAICustomerJWT::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAICustomerJWT::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAICustomerJWT::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_acl.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_claims.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
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

        if (m_invalidate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_one_time_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
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

bool OAICustomerJWT::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
