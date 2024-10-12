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

#include "OAIAuthenticationOptions.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthenticationOptions::OAIAuthenticationOptions(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthenticationOptions::OAIAuthenticationOptions() {
    this->initializeModel();
}

OAIAuthenticationOptions::~OAIAuthenticationOptions() {}

void OAIAuthenticationOptions::initializeModel() {

    m_auth_token_ttl_isSet = false;
    m_auth_token_ttl_isValid = false;

    m_credential_ttl_isSet = false;
    m_credential_ttl_isValid = false;

    m_otp_required_isSet = false;
    m_otp_required_isValid = false;

    m_password_pattern_isSet = false;
    m_password_pattern_isValid = false;

    m_reset_token_ttl_isSet = false;
    m_reset_token_ttl_isValid = false;
}

void OAIAuthenticationOptions::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthenticationOptions::fromJsonObject(QJsonObject json) {

    m_auth_token_ttl_isValid = ::OpenAPI::fromJsonValue(m_auth_token_ttl, json[QString("authTokenTtl")]);
    m_auth_token_ttl_isSet = !json[QString("authTokenTtl")].isNull() && m_auth_token_ttl_isValid;

    m_credential_ttl_isValid = ::OpenAPI::fromJsonValue(m_credential_ttl, json[QString("credentialTtl")]);
    m_credential_ttl_isSet = !json[QString("credentialTtl")].isNull() && m_credential_ttl_isValid;

    m_otp_required_isValid = ::OpenAPI::fromJsonValue(m_otp_required, json[QString("otpRequired")]);
    m_otp_required_isSet = !json[QString("otpRequired")].isNull() && m_otp_required_isValid;

    m_password_pattern_isValid = ::OpenAPI::fromJsonValue(m_password_pattern, json[QString("passwordPattern")]);
    m_password_pattern_isSet = !json[QString("passwordPattern")].isNull() && m_password_pattern_isValid;

    m_reset_token_ttl_isValid = ::OpenAPI::fromJsonValue(m_reset_token_ttl, json[QString("resetTokenTtl")]);
    m_reset_token_ttl_isSet = !json[QString("resetTokenTtl")].isNull() && m_reset_token_ttl_isValid;
}

QString OAIAuthenticationOptions::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthenticationOptions::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_token_ttl_isSet) {
        obj.insert(QString("authTokenTtl"), ::OpenAPI::toJsonValue(m_auth_token_ttl));
    }
    if (m_credential_ttl_isSet) {
        obj.insert(QString("credentialTtl"), ::OpenAPI::toJsonValue(m_credential_ttl));
    }
    if (m_otp_required_isSet) {
        obj.insert(QString("otpRequired"), ::OpenAPI::toJsonValue(m_otp_required));
    }
    if (m_password_pattern_isSet) {
        obj.insert(QString("passwordPattern"), ::OpenAPI::toJsonValue(m_password_pattern));
    }
    if (m_reset_token_ttl_isSet) {
        obj.insert(QString("resetTokenTtl"), ::OpenAPI::toJsonValue(m_reset_token_ttl));
    }
    return obj;
}

qint32 OAIAuthenticationOptions::getAuthTokenTtl() const {
    return m_auth_token_ttl;
}
void OAIAuthenticationOptions::setAuthTokenTtl(const qint32 &auth_token_ttl) {
    m_auth_token_ttl = auth_token_ttl;
    m_auth_token_ttl_isSet = true;
}

bool OAIAuthenticationOptions::is_auth_token_ttl_Set() const{
    return m_auth_token_ttl_isSet;
}

bool OAIAuthenticationOptions::is_auth_token_ttl_Valid() const{
    return m_auth_token_ttl_isValid;
}

qint32 OAIAuthenticationOptions::getCredentialTtl() const {
    return m_credential_ttl;
}
void OAIAuthenticationOptions::setCredentialTtl(const qint32 &credential_ttl) {
    m_credential_ttl = credential_ttl;
    m_credential_ttl_isSet = true;
}

bool OAIAuthenticationOptions::is_credential_ttl_Set() const{
    return m_credential_ttl_isSet;
}

bool OAIAuthenticationOptions::is_credential_ttl_Valid() const{
    return m_credential_ttl_isValid;
}

bool OAIAuthenticationOptions::isOtpRequired() const {
    return m_otp_required;
}
void OAIAuthenticationOptions::setOtpRequired(const bool &otp_required) {
    m_otp_required = otp_required;
    m_otp_required_isSet = true;
}

bool OAIAuthenticationOptions::is_otp_required_Set() const{
    return m_otp_required_isSet;
}

bool OAIAuthenticationOptions::is_otp_required_Valid() const{
    return m_otp_required_isValid;
}

QString OAIAuthenticationOptions::getPasswordPattern() const {
    return m_password_pattern;
}
void OAIAuthenticationOptions::setPasswordPattern(const QString &password_pattern) {
    m_password_pattern = password_pattern;
    m_password_pattern_isSet = true;
}

bool OAIAuthenticationOptions::is_password_pattern_Set() const{
    return m_password_pattern_isSet;
}

bool OAIAuthenticationOptions::is_password_pattern_Valid() const{
    return m_password_pattern_isValid;
}

qint32 OAIAuthenticationOptions::getResetTokenTtl() const {
    return m_reset_token_ttl;
}
void OAIAuthenticationOptions::setResetTokenTtl(const qint32 &reset_token_ttl) {
    m_reset_token_ttl = reset_token_ttl;
    m_reset_token_ttl_isSet = true;
}

bool OAIAuthenticationOptions::is_reset_token_ttl_Set() const{
    return m_reset_token_ttl_isSet;
}

bool OAIAuthenticationOptions::is_reset_token_ttl_Valid() const{
    return m_reset_token_ttl_isValid;
}

bool OAIAuthenticationOptions::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_token_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_credential_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_otp_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_pattern_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reset_token_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthenticationOptions::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
