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

#include "OAIThreeDSecureResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIThreeDSecureResult::OAIThreeDSecureResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIThreeDSecureResult::OAIThreeDSecureResult() {
    this->initializeModel();
}

OAIThreeDSecureResult::~OAIThreeDSecureResult() {}

void OAIThreeDSecureResult::initializeModel() {

    m_authenticated_isSet = false;
    m_authenticated_isValid = false;

    m_enrolled_isSet = false;
    m_enrolled_isValid = false;

    m_flow_isSet = false;
    m_flow_isValid = false;

    m_is_downgraded_isSet = false;
    m_is_downgraded_isValid = false;

    m_liability_isSet = false;
    m_liability_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIThreeDSecureResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIThreeDSecureResult::fromJsonObject(QJsonObject json) {

    m_authenticated_isValid = ::OpenAPI::fromJsonValue(m_authenticated, json[QString("authenticated")]);
    m_authenticated_isSet = !json[QString("authenticated")].isNull() && m_authenticated_isValid;

    m_enrolled_isValid = ::OpenAPI::fromJsonValue(m_enrolled, json[QString("enrolled")]);
    m_enrolled_isSet = !json[QString("enrolled")].isNull() && m_enrolled_isValid;

    m_flow_isValid = ::OpenAPI::fromJsonValue(m_flow, json[QString("flow")]);
    m_flow_isSet = !json[QString("flow")].isNull() && m_flow_isValid;

    m_is_downgraded_isValid = ::OpenAPI::fromJsonValue(m_is_downgraded, json[QString("isDowngraded")]);
    m_is_downgraded_isSet = !json[QString("isDowngraded")].isNull() && m_is_downgraded_isValid;

    m_liability_isValid = ::OpenAPI::fromJsonValue(m_liability, json[QString("liability")]);
    m_liability_isSet = !json[QString("liability")].isNull() && m_liability_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIThreeDSecureResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIThreeDSecureResult::asJsonObject() const {
    QJsonObject obj;
    if (m_authenticated_isSet) {
        obj.insert(QString("authenticated"), ::OpenAPI::toJsonValue(m_authenticated));
    }
    if (m_enrolled_isSet) {
        obj.insert(QString("enrolled"), ::OpenAPI::toJsonValue(m_enrolled));
    }
    if (m_flow_isSet) {
        obj.insert(QString("flow"), ::OpenAPI::toJsonValue(m_flow));
    }
    if (m_is_downgraded_isSet) {
        obj.insert(QString("isDowngraded"), ::OpenAPI::toJsonValue(m_is_downgraded));
    }
    if (m_liability_isSet) {
        obj.insert(QString("liability"), ::OpenAPI::toJsonValue(m_liability));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIThreeDSecureResult::getAuthenticated() const {
    return m_authenticated;
}
void OAIThreeDSecureResult::setAuthenticated(const QString &authenticated) {
    m_authenticated = authenticated;
    m_authenticated_isSet = true;
}

bool OAIThreeDSecureResult::is_authenticated_Set() const{
    return m_authenticated_isSet;
}

bool OAIThreeDSecureResult::is_authenticated_Valid() const{
    return m_authenticated_isValid;
}

QString OAIThreeDSecureResult::getEnrolled() const {
    return m_enrolled;
}
void OAIThreeDSecureResult::setEnrolled(const QString &enrolled) {
    m_enrolled = enrolled;
    m_enrolled_isSet = true;
}

bool OAIThreeDSecureResult::is_enrolled_Set() const{
    return m_enrolled_isSet;
}

bool OAIThreeDSecureResult::is_enrolled_Valid() const{
    return m_enrolled_isValid;
}

QString OAIThreeDSecureResult::getFlow() const {
    return m_flow;
}
void OAIThreeDSecureResult::setFlow(const QString &flow) {
    m_flow = flow;
    m_flow_isSet = true;
}

bool OAIThreeDSecureResult::is_flow_Set() const{
    return m_flow_isSet;
}

bool OAIThreeDSecureResult::is_flow_Valid() const{
    return m_flow_isValid;
}

bool OAIThreeDSecureResult::isIsDowngraded() const {
    return m_is_downgraded;
}
void OAIThreeDSecureResult::setIsDowngraded(const bool &is_downgraded) {
    m_is_downgraded = is_downgraded;
    m_is_downgraded_isSet = true;
}

bool OAIThreeDSecureResult::is_is_downgraded_Set() const{
    return m_is_downgraded_isSet;
}

bool OAIThreeDSecureResult::is_is_downgraded_Valid() const{
    return m_is_downgraded_isValid;
}

QString OAIThreeDSecureResult::getLiability() const {
    return m_liability;
}
void OAIThreeDSecureResult::setLiability(const QString &liability) {
    m_liability = liability;
    m_liability_isSet = true;
}

bool OAIThreeDSecureResult::is_liability_Set() const{
    return m_liability_isSet;
}

bool OAIThreeDSecureResult::is_liability_Valid() const{
    return m_liability_isValid;
}

QString OAIThreeDSecureResult::getVersion() const {
    return m_version;
}
void OAIThreeDSecureResult::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIThreeDSecureResult::is_version_Set() const{
    return m_version_isSet;
}

bool OAIThreeDSecureResult::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIThreeDSecureResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_authenticated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enrolled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flow_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_downgraded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_liability_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIThreeDSecureResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_authenticated_isValid && m_enrolled_isValid && m_is_downgraded_isValid && m_liability_isValid && true;
}

} // namespace OpenAPI
