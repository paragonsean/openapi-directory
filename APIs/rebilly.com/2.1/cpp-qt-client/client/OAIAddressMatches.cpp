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

#include "OAIAddressMatches.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddressMatches::OAIAddressMatches(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddressMatches::OAIAddressMatches() {
    this->initializeModel();
}

OAIAddressMatches::~OAIAddressMatches() {}

void OAIAddressMatches::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_date_isSet = false;
    m_date_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_line1_isSet = false;
    m_line1_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_unique_words_isSet = false;
    m_unique_words_isValid = false;

    m_unique_words_result_isSet = false;
    m_unique_words_result_isValid = false;

    m_word_count_isSet = false;
    m_word_count_isValid = false;

    m_word_count_result_isSet = false;
    m_word_count_result_isValid = false;
}

void OAIAddressMatches::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddressMatches::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_date_isValid = ::OpenAPI::fromJsonValue(m_date, json[QString("date")]);
    m_date_isSet = !json[QString("date")].isNull() && m_date_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_line1_isValid = ::OpenAPI::fromJsonValue(m_line1, json[QString("line1")]);
    m_line1_isSet = !json[QString("line1")].isNull() && m_line1_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_unique_words_isValid = ::OpenAPI::fromJsonValue(m_unique_words, json[QString("uniqueWords")]);
    m_unique_words_isSet = !json[QString("uniqueWords")].isNull() && m_unique_words_isValid;

    m_unique_words_result_isValid = ::OpenAPI::fromJsonValue(m_unique_words_result, json[QString("uniqueWordsResult")]);
    m_unique_words_result_isSet = !json[QString("uniqueWordsResult")].isNull() && m_unique_words_result_isValid;

    m_word_count_isValid = ::OpenAPI::fromJsonValue(m_word_count, json[QString("wordCount")]);
    m_word_count_isSet = !json[QString("wordCount")].isNull() && m_word_count_isValid;

    m_word_count_result_isValid = ::OpenAPI::fromJsonValue(m_word_count_result, json[QString("wordCountResult")]);
    m_word_count_result_isSet = !json[QString("wordCountResult")].isNull() && m_word_count_result_isValid;
}

QString OAIAddressMatches::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddressMatches::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_date_isSet) {
        obj.insert(QString("date"), ::OpenAPI::toJsonValue(m_date));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_line1_isSet) {
        obj.insert(QString("line1"), ::OpenAPI::toJsonValue(m_line1));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_unique_words_isSet) {
        obj.insert(QString("uniqueWords"), ::OpenAPI::toJsonValue(m_unique_words));
    }
    if (m_unique_words_result_isSet) {
        obj.insert(QString("uniqueWordsResult"), ::OpenAPI::toJsonValue(m_unique_words_result));
    }
    if (m_word_count_isSet) {
        obj.insert(QString("wordCount"), ::OpenAPI::toJsonValue(m_word_count));
    }
    if (m_word_count_result_isSet) {
        obj.insert(QString("wordCountResult"), ::OpenAPI::toJsonValue(m_word_count_result));
    }
    return obj;
}

QString OAIAddressMatches::getCity() const {
    return m_city;
}
void OAIAddressMatches::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIAddressMatches::is_city_Set() const{
    return m_city_isSet;
}

bool OAIAddressMatches::is_city_Valid() const{
    return m_city_isValid;
}

QDate OAIAddressMatches::getDate() const {
    return m_date;
}
void OAIAddressMatches::setDate(const QDate &date) {
    m_date = date;
    m_date_isSet = true;
}

bool OAIAddressMatches::is_date_Set() const{
    return m_date_isSet;
}

bool OAIAddressMatches::is_date_Valid() const{
    return m_date_isValid;
}

QString OAIAddressMatches::getFirstName() const {
    return m_first_name;
}
void OAIAddressMatches::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIAddressMatches::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIAddressMatches::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIAddressMatches::getLastName() const {
    return m_last_name;
}
void OAIAddressMatches::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIAddressMatches::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIAddressMatches::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIAddressMatches::getLine1() const {
    return m_line1;
}
void OAIAddressMatches::setLine1(const QString &line1) {
    m_line1 = line1;
    m_line1_isSet = true;
}

bool OAIAddressMatches::is_line1_Set() const{
    return m_line1_isSet;
}

bool OAIAddressMatches::is_line1_Valid() const{
    return m_line1_isValid;
}

QString OAIAddressMatches::getPhone() const {
    return m_phone;
}
void OAIAddressMatches::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAIAddressMatches::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAIAddressMatches::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAIAddressMatches::getPostalCode() const {
    return m_postal_code;
}
void OAIAddressMatches::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIAddressMatches::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIAddressMatches::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAIAddressMatches::getRegion() const {
    return m_region;
}
void OAIAddressMatches::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIAddressMatches::is_region_Set() const{
    return m_region_isSet;
}

bool OAIAddressMatches::is_region_Valid() const{
    return m_region_isValid;
}

qint32 OAIAddressMatches::getUniqueWords() const {
    return m_unique_words;
}
void OAIAddressMatches::setUniqueWords(const qint32 &unique_words) {
    m_unique_words = unique_words;
    m_unique_words_isSet = true;
}

bool OAIAddressMatches::is_unique_words_Set() const{
    return m_unique_words_isSet;
}

bool OAIAddressMatches::is_unique_words_Valid() const{
    return m_unique_words_isValid;
}

bool OAIAddressMatches::isUniqueWordsResult() const {
    return m_unique_words_result;
}
void OAIAddressMatches::setUniqueWordsResult(const bool &unique_words_result) {
    m_unique_words_result = unique_words_result;
    m_unique_words_result_isSet = true;
}

bool OAIAddressMatches::is_unique_words_result_Set() const{
    return m_unique_words_result_isSet;
}

bool OAIAddressMatches::is_unique_words_result_Valid() const{
    return m_unique_words_result_isValid;
}

qint32 OAIAddressMatches::getWordCount() const {
    return m_word_count;
}
void OAIAddressMatches::setWordCount(const qint32 &word_count) {
    m_word_count = word_count;
    m_word_count_isSet = true;
}

bool OAIAddressMatches::is_word_count_Set() const{
    return m_word_count_isSet;
}

bool OAIAddressMatches::is_word_count_Valid() const{
    return m_word_count_isValid;
}

bool OAIAddressMatches::isWordCountResult() const {
    return m_word_count_result;
}
void OAIAddressMatches::setWordCountResult(const bool &word_count_result) {
    m_word_count_result = word_count_result;
    m_word_count_result_isSet = true;
}

bool OAIAddressMatches::is_word_count_result_Set() const{
    return m_word_count_result_isSet;
}

bool OAIAddressMatches::is_word_count_result_Valid() const{
    return m_word_count_result_isValid;
}

bool OAIAddressMatches::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unique_words_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unique_words_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_word_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_word_count_result_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddressMatches::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
