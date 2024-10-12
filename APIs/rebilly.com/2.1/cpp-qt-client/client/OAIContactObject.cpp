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

#include "OAIContactObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContactObject::OAIContactObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContactObject::OAIContactObject() {
    this->initializeModel();
}

OAIContactObject::~OAIContactObject() {}

void OAIContactObject::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_address2_isSet = false;
    m_address2_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_hash_isSet = false;
    m_hash_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_organization_isSet = false;
    m_organization_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;
}

void OAIContactObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContactObject::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_address2_isValid = ::OpenAPI::fromJsonValue(m_address2, json[QString("address2")]);
    m_address2_isSet = !json[QString("address2")].isNull() && m_address2_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_hash_isValid = ::OpenAPI::fromJsonValue(m_hash, json[QString("hash")]);
    m_hash_isSet = !json[QString("hash")].isNull() && m_hash_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_organization_isValid = ::OpenAPI::fromJsonValue(m_organization, json[QString("organization")]);
    m_organization_isSet = !json[QString("organization")].isNull() && m_organization_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phoneNumbers")]);
    m_phone_numbers_isSet = !json[QString("phoneNumbers")].isNull() && m_phone_numbers_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;
}

QString OAIContactObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContactObject::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_address2_isSet) {
        obj.insert(QString("address2"), ::OpenAPI::toJsonValue(m_address2));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_hash_isSet) {
        obj.insert(QString("hash"), ::OpenAPI::toJsonValue(m_hash));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_organization_isSet) {
        obj.insert(QString("organization"), ::OpenAPI::toJsonValue(m_organization));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phoneNumbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    return obj;
}

QString OAIContactObject::getAddress() const {
    return m_address;
}
void OAIContactObject::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIContactObject::is_address_Set() const{
    return m_address_isSet;
}

bool OAIContactObject::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIContactObject::getAddress2() const {
    return m_address2;
}
void OAIContactObject::setAddress2(const QString &address2) {
    m_address2 = address2;
    m_address2_isSet = true;
}

bool OAIContactObject::is_address2_Set() const{
    return m_address2_isSet;
}

bool OAIContactObject::is_address2_Valid() const{
    return m_address2_isValid;
}

QString OAIContactObject::getCity() const {
    return m_city;
}
void OAIContactObject::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIContactObject::is_city_Set() const{
    return m_city_isSet;
}

bool OAIContactObject::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIContactObject::getCountry() const {
    return m_country;
}
void OAIContactObject::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIContactObject::is_country_Set() const{
    return m_country_isSet;
}

bool OAIContactObject::is_country_Valid() const{
    return m_country_isValid;
}

QList<OAIContactEmails_inner> OAIContactObject::getEmails() const {
    return m_emails;
}
void OAIContactObject::setEmails(const QList<OAIContactEmails_inner> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAIContactObject::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAIContactObject::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAIContactObject::getFirstName() const {
    return m_first_name;
}
void OAIContactObject::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIContactObject::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIContactObject::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIContactObject::getHash() const {
    return m_hash;
}
void OAIContactObject::setHash(const QString &hash) {
    m_hash = hash;
    m_hash_isSet = true;
}

bool OAIContactObject::is_hash_Set() const{
    return m_hash_isSet;
}

bool OAIContactObject::is_hash_Valid() const{
    return m_hash_isValid;
}

QString OAIContactObject::getLastName() const {
    return m_last_name;
}
void OAIContactObject::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIContactObject::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIContactObject::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIContactObject::getOrganization() const {
    return m_organization;
}
void OAIContactObject::setOrganization(const QString &organization) {
    m_organization = organization;
    m_organization_isSet = true;
}

bool OAIContactObject::is_organization_Set() const{
    return m_organization_isSet;
}

bool OAIContactObject::is_organization_Valid() const{
    return m_organization_isValid;
}

QList<OAIContactPhoneNumbers_inner> OAIContactObject::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIContactObject::setPhoneNumbers(const QList<OAIContactPhoneNumbers_inner> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIContactObject::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIContactObject::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

QString OAIContactObject::getPostalCode() const {
    return m_postal_code;
}
void OAIContactObject::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIContactObject::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIContactObject::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAIContactObject::getRegion() const {
    return m_region;
}
void OAIContactObject::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIContactObject::is_region_Set() const{
    return m_region_isSet;
}

bool OAIContactObject::is_region_Valid() const{
    return m_region_isValid;
}

bool OAIContactObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_organization_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_numbers.size() > 0) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIContactObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
