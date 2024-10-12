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

#include "OAIBrowserData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBrowserData::OAIBrowserData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBrowserData::OAIBrowserData() {
    this->initializeModel();
}

OAIBrowserData::~OAIBrowserData() {}

void OAIBrowserData::initializeModel() {

    m_color_depth_isSet = false;
    m_color_depth_isValid = false;

    m_is_java_enabled_isSet = false;
    m_is_java_enabled_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_screen_height_isSet = false;
    m_screen_height_isValid = false;

    m_screen_width_isSet = false;
    m_screen_width_isValid = false;

    m_time_zone_offset_isSet = false;
    m_time_zone_offset_isValid = false;
}

void OAIBrowserData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBrowserData::fromJsonObject(QJsonObject json) {

    m_color_depth_isValid = ::OpenAPI::fromJsonValue(m_color_depth, json[QString("colorDepth")]);
    m_color_depth_isSet = !json[QString("colorDepth")].isNull() && m_color_depth_isValid;

    m_is_java_enabled_isValid = ::OpenAPI::fromJsonValue(m_is_java_enabled, json[QString("isJavaEnabled")]);
    m_is_java_enabled_isSet = !json[QString("isJavaEnabled")].isNull() && m_is_java_enabled_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_screen_height_isValid = ::OpenAPI::fromJsonValue(m_screen_height, json[QString("screenHeight")]);
    m_screen_height_isSet = !json[QString("screenHeight")].isNull() && m_screen_height_isValid;

    m_screen_width_isValid = ::OpenAPI::fromJsonValue(m_screen_width, json[QString("screenWidth")]);
    m_screen_width_isSet = !json[QString("screenWidth")].isNull() && m_screen_width_isValid;

    m_time_zone_offset_isValid = ::OpenAPI::fromJsonValue(m_time_zone_offset, json[QString("timeZoneOffset")]);
    m_time_zone_offset_isSet = !json[QString("timeZoneOffset")].isNull() && m_time_zone_offset_isValid;
}

QString OAIBrowserData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBrowserData::asJsonObject() const {
    QJsonObject obj;
    if (m_color_depth_isSet) {
        obj.insert(QString("colorDepth"), ::OpenAPI::toJsonValue(m_color_depth));
    }
    if (m_is_java_enabled_isSet) {
        obj.insert(QString("isJavaEnabled"), ::OpenAPI::toJsonValue(m_is_java_enabled));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_screen_height_isSet) {
        obj.insert(QString("screenHeight"), ::OpenAPI::toJsonValue(m_screen_height));
    }
    if (m_screen_width_isSet) {
        obj.insert(QString("screenWidth"), ::OpenAPI::toJsonValue(m_screen_width));
    }
    if (m_time_zone_offset_isSet) {
        obj.insert(QString("timeZoneOffset"), ::OpenAPI::toJsonValue(m_time_zone_offset));
    }
    return obj;
}

qint32 OAIBrowserData::getColorDepth() const {
    return m_color_depth;
}
void OAIBrowserData::setColorDepth(const qint32 &color_depth) {
    m_color_depth = color_depth;
    m_color_depth_isSet = true;
}

bool OAIBrowserData::is_color_depth_Set() const{
    return m_color_depth_isSet;
}

bool OAIBrowserData::is_color_depth_Valid() const{
    return m_color_depth_isValid;
}

bool OAIBrowserData::isIsJavaEnabled() const {
    return m_is_java_enabled;
}
void OAIBrowserData::setIsJavaEnabled(const bool &is_java_enabled) {
    m_is_java_enabled = is_java_enabled;
    m_is_java_enabled_isSet = true;
}

bool OAIBrowserData::is_is_java_enabled_Set() const{
    return m_is_java_enabled_isSet;
}

bool OAIBrowserData::is_is_java_enabled_Valid() const{
    return m_is_java_enabled_isValid;
}

QString OAIBrowserData::getLanguage() const {
    return m_language;
}
void OAIBrowserData::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIBrowserData::is_language_Set() const{
    return m_language_isSet;
}

bool OAIBrowserData::is_language_Valid() const{
    return m_language_isValid;
}

qint32 OAIBrowserData::getScreenHeight() const {
    return m_screen_height;
}
void OAIBrowserData::setScreenHeight(const qint32 &screen_height) {
    m_screen_height = screen_height;
    m_screen_height_isSet = true;
}

bool OAIBrowserData::is_screen_height_Set() const{
    return m_screen_height_isSet;
}

bool OAIBrowserData::is_screen_height_Valid() const{
    return m_screen_height_isValid;
}

qint32 OAIBrowserData::getScreenWidth() const {
    return m_screen_width;
}
void OAIBrowserData::setScreenWidth(const qint32 &screen_width) {
    m_screen_width = screen_width;
    m_screen_width_isSet = true;
}

bool OAIBrowserData::is_screen_width_Set() const{
    return m_screen_width_isSet;
}

bool OAIBrowserData::is_screen_width_Valid() const{
    return m_screen_width_isValid;
}

qint32 OAIBrowserData::getTimeZoneOffset() const {
    return m_time_zone_offset;
}
void OAIBrowserData::setTimeZoneOffset(const qint32 &time_zone_offset) {
    m_time_zone_offset = time_zone_offset;
    m_time_zone_offset_isSet = true;
}

bool OAIBrowserData::is_time_zone_offset_Set() const{
    return m_time_zone_offset_isSet;
}

bool OAIBrowserData::is_time_zone_offset_Valid() const{
    return m_time_zone_offset_isValid;
}

bool OAIBrowserData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_depth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_java_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_screen_width_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_offset_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBrowserData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_color_depth_isValid && m_is_java_enabled_isValid && m_language_isValid && m_screen_height_isValid && m_screen_width_isValid && m_time_zone_offset_isValid && true;
}

} // namespace OpenAPI
