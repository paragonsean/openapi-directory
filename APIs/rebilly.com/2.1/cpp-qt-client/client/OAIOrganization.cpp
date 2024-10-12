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

#include "OAIOrganization.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrganization::OAIOrganization(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrganization::OAIOrganization() {
    this->initializeModel();
}

OAIOrganization::~OAIOrganization() {}

void OAIOrganization::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_address2_isSet = false;
    m_address2_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_time_zone_isSet = false;
    m_invoice_time_zone_isValid = false;

    m_is_primary_isSet = false;
    m_is_primary_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_questionnaire_isSet = false;
    m_questionnaire_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_tax_descriptor_isSet = false;
    m_tax_descriptor_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIOrganization::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrganization::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_address2_isValid = ::OpenAPI::fromJsonValue(m_address2, json[QString("address2")]);
    m_address2_isSet = !json[QString("address2")].isNull() && m_address2_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_time_zone_isValid = ::OpenAPI::fromJsonValue(m_invoice_time_zone, json[QString("invoiceTimeZone")]);
    m_invoice_time_zone_isSet = !json[QString("invoiceTimeZone")].isNull() && m_invoice_time_zone_isValid;

    m_is_primary_isValid = ::OpenAPI::fromJsonValue(m_is_primary, json[QString("isPrimary")]);
    m_is_primary_isSet = !json[QString("isPrimary")].isNull() && m_is_primary_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phoneNumbers")]);
    m_phone_numbers_isSet = !json[QString("phoneNumbers")].isNull() && m_phone_numbers_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_questionnaire_isValid = ::OpenAPI::fromJsonValue(m_questionnaire, json[QString("questionnaire")]);
    m_questionnaire_isSet = !json[QString("questionnaire")].isNull() && m_questionnaire_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_tax_descriptor_isValid = ::OpenAPI::fromJsonValue(m_tax_descriptor, json[QString("taxDescriptor")]);
    m_tax_descriptor_isSet = !json[QString("taxDescriptor")].isNull() && m_tax_descriptor_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAIOrganization::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrganization::asJsonObject() const {
    QJsonObject obj;
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
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
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_time_zone_isSet) {
        obj.insert(QString("invoiceTimeZone"), ::OpenAPI::toJsonValue(m_invoice_time_zone));
    }
    if (m_is_primary_isSet) {
        obj.insert(QString("isPrimary"), ::OpenAPI::toJsonValue(m_is_primary));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phoneNumbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_questionnaire.isSet()) {
        obj.insert(QString("questionnaire"), ::OpenAPI::toJsonValue(m_questionnaire));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_tax_descriptor_isSet) {
        obj.insert(QString("taxDescriptor"), ::OpenAPI::toJsonValue(m_tax_descriptor));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QList<OAISelfLink> OAIOrganization::getLinks() const {
    return m__links;
}
void OAIOrganization::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIOrganization::is__links_Set() const{
    return m__links_isSet;
}

bool OAIOrganization::is__links_Valid() const{
    return m__links_isValid;
}

QString OAIOrganization::getAddress() const {
    return m_address;
}
void OAIOrganization::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIOrganization::is_address_Set() const{
    return m_address_isSet;
}

bool OAIOrganization::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIOrganization::getAddress2() const {
    return m_address2;
}
void OAIOrganization::setAddress2(const QString &address2) {
    m_address2 = address2;
    m_address2_isSet = true;
}

bool OAIOrganization::is_address2_Set() const{
    return m_address2_isSet;
}

bool OAIOrganization::is_address2_Valid() const{
    return m_address2_isValid;
}

QString OAIOrganization::getCity() const {
    return m_city;
}
void OAIOrganization::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIOrganization::is_city_Set() const{
    return m_city_isSet;
}

bool OAIOrganization::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIOrganization::getCountry() const {
    return m_country;
}
void OAIOrganization::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIOrganization::is_country_Set() const{
    return m_country_isSet;
}

bool OAIOrganization::is_country_Valid() const{
    return m_country_isValid;
}

QDateTime OAIOrganization::getCreatedTime() const {
    return m_created_time;
}
void OAIOrganization::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIOrganization::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIOrganization::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QList<OAIContactEmails_inner> OAIOrganization::getEmails() const {
    return m_emails;
}
void OAIOrganization::setEmails(const QList<OAIContactEmails_inner> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAIOrganization::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAIOrganization::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAIOrganization::getId() const {
    return m_id;
}
void OAIOrganization::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrganization::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrganization::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrganization::getInvoiceTimeZone() const {
    return m_invoice_time_zone;
}
void OAIOrganization::setInvoiceTimeZone(const QString &invoice_time_zone) {
    m_invoice_time_zone = invoice_time_zone;
    m_invoice_time_zone_isSet = true;
}

bool OAIOrganization::is_invoice_time_zone_Set() const{
    return m_invoice_time_zone_isSet;
}

bool OAIOrganization::is_invoice_time_zone_Valid() const{
    return m_invoice_time_zone_isValid;
}

bool OAIOrganization::isIsPrimary() const {
    return m_is_primary;
}
void OAIOrganization::setIsPrimary(const bool &is_primary) {
    m_is_primary = is_primary;
    m_is_primary_isSet = true;
}

bool OAIOrganization::is_is_primary_Set() const{
    return m_is_primary_isSet;
}

bool OAIOrganization::is_is_primary_Valid() const{
    return m_is_primary_isValid;
}

QString OAIOrganization::getName() const {
    return m_name;
}
void OAIOrganization::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrganization::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrganization::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIContactPhoneNumbers_inner> OAIOrganization::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIOrganization::setPhoneNumbers(const QList<OAIContactPhoneNumbers_inner> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIOrganization::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIOrganization::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

QString OAIOrganization::getPostalCode() const {
    return m_postal_code;
}
void OAIOrganization::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIOrganization::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIOrganization::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

OAIOrganizationQuestionnaire OAIOrganization::getQuestionnaire() const {
    return m_questionnaire;
}
void OAIOrganization::setQuestionnaire(const OAIOrganizationQuestionnaire &questionnaire) {
    m_questionnaire = questionnaire;
    m_questionnaire_isSet = true;
}

bool OAIOrganization::is_questionnaire_Set() const{
    return m_questionnaire_isSet;
}

bool OAIOrganization::is_questionnaire_Valid() const{
    return m_questionnaire_isValid;
}

QString OAIOrganization::getRegion() const {
    return m_region;
}
void OAIOrganization::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIOrganization::is_region_Set() const{
    return m_region_isSet;
}

bool OAIOrganization::is_region_Valid() const{
    return m_region_isValid;
}

QString OAIOrganization::getTaxDescriptor() const {
    return m_tax_descriptor;
}
void OAIOrganization::setTaxDescriptor(const QString &tax_descriptor) {
    m_tax_descriptor = tax_descriptor;
    m_tax_descriptor_isSet = true;
}

bool OAIOrganization::is_tax_descriptor_Set() const{
    return m_tax_descriptor_isSet;
}

bool OAIOrganization::is_tax_descriptor_Valid() const{
    return m_tax_descriptor_isValid;
}

QDateTime OAIOrganization::getUpdatedTime() const {
    return m_updated_time;
}
void OAIOrganization::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIOrganization::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIOrganization::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIOrganization::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

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

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_primary_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

        if (m_questionnaire.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_descriptor_isSet) {
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

bool OAIOrganization::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_country_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
