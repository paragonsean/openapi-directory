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

#include "OAIAmexVPC_allOf_credentials.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAmexVPC_allOf_credentials::OAIAmexVPC_allOf_credentials(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAmexVPC_allOf_credentials::OAIAmexVPC_allOf_credentials() {
    this->initializeModel();
}

OAIAmexVPC_allOf_credentials::~OAIAmexVPC_allOf_credentials() {}

void OAIAmexVPC_allOf_credentials::initializeModel() {

    m_access_code_isSet = false;
    m_access_code_isValid = false;

    m_merchant_id_isSet = false;
    m_merchant_id_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_user_isSet = false;
    m_user_isValid = false;
}

void OAIAmexVPC_allOf_credentials::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAmexVPC_allOf_credentials::fromJsonObject(QJsonObject json) {

    m_access_code_isValid = ::OpenAPI::fromJsonValue(m_access_code, json[QString("accessCode")]);
    m_access_code_isSet = !json[QString("accessCode")].isNull() && m_access_code_isValid;

    m_merchant_id_isValid = ::OpenAPI::fromJsonValue(m_merchant_id, json[QString("merchantId")]);
    m_merchant_id_isSet = !json[QString("merchantId")].isNull() && m_merchant_id_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_user_isValid = ::OpenAPI::fromJsonValue(m_user, json[QString("user")]);
    m_user_isSet = !json[QString("user")].isNull() && m_user_isValid;
}

QString OAIAmexVPC_allOf_credentials::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAmexVPC_allOf_credentials::asJsonObject() const {
    QJsonObject obj;
    if (m_access_code_isSet) {
        obj.insert(QString("accessCode"), ::OpenAPI::toJsonValue(m_access_code));
    }
    if (m_merchant_id_isSet) {
        obj.insert(QString("merchantId"), ::OpenAPI::toJsonValue(m_merchant_id));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_user_isSet) {
        obj.insert(QString("user"), ::OpenAPI::toJsonValue(m_user));
    }
    return obj;
}

QString OAIAmexVPC_allOf_credentials::getAccessCode() const {
    return m_access_code;
}
void OAIAmexVPC_allOf_credentials::setAccessCode(const QString &access_code) {
    m_access_code = access_code;
    m_access_code_isSet = true;
}

bool OAIAmexVPC_allOf_credentials::is_access_code_Set() const{
    return m_access_code_isSet;
}

bool OAIAmexVPC_allOf_credentials::is_access_code_Valid() const{
    return m_access_code_isValid;
}

QString OAIAmexVPC_allOf_credentials::getMerchantId() const {
    return m_merchant_id;
}
void OAIAmexVPC_allOf_credentials::setMerchantId(const QString &merchant_id) {
    m_merchant_id = merchant_id;
    m_merchant_id_isSet = true;
}

bool OAIAmexVPC_allOf_credentials::is_merchant_id_Set() const{
    return m_merchant_id_isSet;
}

bool OAIAmexVPC_allOf_credentials::is_merchant_id_Valid() const{
    return m_merchant_id_isValid;
}

QString OAIAmexVPC_allOf_credentials::getPassword() const {
    return m_password;
}
void OAIAmexVPC_allOf_credentials::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIAmexVPC_allOf_credentials::is_password_Set() const{
    return m_password_isSet;
}

bool OAIAmexVPC_allOf_credentials::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIAmexVPC_allOf_credentials::getUser() const {
    return m_user;
}
void OAIAmexVPC_allOf_credentials::setUser(const QString &user) {
    m_user = user;
    m_user_isSet = true;
}

bool OAIAmexVPC_allOf_credentials::is_user_Set() const{
    return m_user_isSet;
}

bool OAIAmexVPC_allOf_credentials::is_user_Valid() const{
    return m_user_isValid;
}

bool OAIAmexVPC_allOf_credentials::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAmexVPC_allOf_credentials::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_access_code_isValid && m_merchant_id_isValid && m_password_isValid && m_user_isValid && true;
}

} // namespace OpenAPI
