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

#include "OAIProduct.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProduct::OAIProduct(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProduct::OAIProduct() {
    this->initializeModel();
}

OAIProduct::~OAIProduct() {}

void OAIProduct::initializeModel() {

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_requires_shipping_isSet = false;
    m_requires_shipping_isValid = false;

    m_unit_label_isSet = false;
    m_unit_label_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_accounting_code_isSet = false;
    m_accounting_code_isValid = false;

    m_tax_category_id_isSet = false;
    m_tax_category_id_isValid = false;
}

void OAIProduct::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProduct::fromJsonObject(QJsonObject json) {

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_requires_shipping_isValid = ::OpenAPI::fromJsonValue(m_requires_shipping, json[QString("requiresShipping")]);
    m_requires_shipping_isSet = !json[QString("requiresShipping")].isNull() && m_requires_shipping_isValid;

    m_unit_label_isValid = ::OpenAPI::fromJsonValue(m_unit_label, json[QString("unitLabel")]);
    m_unit_label_isSet = !json[QString("unitLabel")].isNull() && m_unit_label_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_accounting_code_isValid = ::OpenAPI::fromJsonValue(m_accounting_code, json[QString("accountingCode")]);
    m_accounting_code_isSet = !json[QString("accountingCode")].isNull() && m_accounting_code_isValid;

    m_tax_category_id_isValid = ::OpenAPI::fromJsonValue(m_tax_category_id, json[QString("taxCategoryId")]);
    m_tax_category_id_isSet = !json[QString("taxCategoryId")].isNull() && m_tax_category_id_isValid;
}

QString OAIProduct::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProduct::asJsonObject() const {
    QJsonObject obj;
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_requires_shipping_isSet) {
        obj.insert(QString("requiresShipping"), ::OpenAPI::toJsonValue(m_requires_shipping));
    }
    if (m_unit_label_isSet) {
        obj.insert(QString("unitLabel"), ::OpenAPI::toJsonValue(m_unit_label));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_accounting_code_isSet) {
        obj.insert(QString("accountingCode"), ::OpenAPI::toJsonValue(m_accounting_code));
    }
    if (m_tax_category_id_isSet) {
        obj.insert(QString("taxCategoryId"), ::OpenAPI::toJsonValue(m_tax_category_id));
    }
    return obj;
}

QDateTime OAIProduct::getCreatedTime() const {
    return m_created_time;
}
void OAIProduct::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIProduct::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIProduct::is_created_time_Valid() const{
    return m_created_time_isValid;
}

OAIObject OAIProduct::getCustomFields() const {
    return m_custom_fields;
}
void OAIProduct::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIProduct::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIProduct::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIProduct::getDescription() const {
    return m_description;
}
void OAIProduct::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIProduct::is_description_Set() const{
    return m_description_isSet;
}

bool OAIProduct::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIProduct::getId() const {
    return m_id;
}
void OAIProduct::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIProduct::is_id_Set() const{
    return m_id_isSet;
}

bool OAIProduct::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIProduct::getName() const {
    return m_name;
}
void OAIProduct::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIProduct::is_name_Set() const{
    return m_name_isSet;
}

bool OAIProduct::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAIProduct::getOptions() const {
    return m_options;
}
void OAIProduct::setOptions(const QList<QString> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIProduct::is_options_Set() const{
    return m_options_isSet;
}

bool OAIProduct::is_options_Valid() const{
    return m_options_isValid;
}

bool OAIProduct::isRequiresShipping() const {
    return m_requires_shipping;
}
void OAIProduct::setRequiresShipping(const bool &requires_shipping) {
    m_requires_shipping = requires_shipping;
    m_requires_shipping_isSet = true;
}

bool OAIProduct::is_requires_shipping_Set() const{
    return m_requires_shipping_isSet;
}

bool OAIProduct::is_requires_shipping_Valid() const{
    return m_requires_shipping_isValid;
}

QString OAIProduct::getUnitLabel() const {
    return m_unit_label;
}
void OAIProduct::setUnitLabel(const QString &unit_label) {
    m_unit_label = unit_label;
    m_unit_label_isSet = true;
}

bool OAIProduct::is_unit_label_Set() const{
    return m_unit_label_isSet;
}

bool OAIProduct::is_unit_label_Valid() const{
    return m_unit_label_isValid;
}

QDateTime OAIProduct::getUpdatedTime() const {
    return m_updated_time;
}
void OAIProduct::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIProduct::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIProduct::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QList<OAISelfLink> OAIProduct::getLinks() const {
    return m__links;
}
void OAIProduct::setLinks(const QList<OAISelfLink> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIProduct::is__links_Set() const{
    return m__links_isSet;
}

bool OAIProduct::is__links_Valid() const{
    return m__links_isValid;
}

QString OAIProduct::getAccountingCode() const {
    return m_accounting_code;
}
void OAIProduct::setAccountingCode(const QString &accounting_code) {
    m_accounting_code = accounting_code;
    m_accounting_code_isSet = true;
}

bool OAIProduct::is_accounting_code_Set() const{
    return m_accounting_code_isSet;
}

bool OAIProduct::is_accounting_code_Valid() const{
    return m_accounting_code_isValid;
}

QString OAIProduct::getTaxCategoryId() const {
    return m_tax_category_id;
}
void OAIProduct::setTaxCategoryId(const QString &tax_category_id) {
    m_tax_category_id = tax_category_id;
    m_tax_category_id_isSet = true;
}

bool OAIProduct::is_tax_category_id_Set() const{
    return m_tax_category_id_isSet;
}

bool OAIProduct::is_tax_category_id_Valid() const{
    return m_tax_category_id_isValid;
}

bool OAIProduct::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_requires_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_accounting_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProduct::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
