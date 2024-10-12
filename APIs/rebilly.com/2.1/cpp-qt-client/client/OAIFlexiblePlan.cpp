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

#include "OAIFlexiblePlan.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFlexiblePlan::OAIFlexiblePlan(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFlexiblePlan::OAIFlexiblePlan() {
    this->initializeModel();
}

OAIFlexiblePlan::~OAIFlexiblePlan() {}

void OAIFlexiblePlan::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_currency_sign_isSet = false;
    m_currency_sign_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_is_trial_only_isSet = false;
    m_is_trial_only_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pricing_isSet = false;
    m_pricing_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_product_options_isSet = false;
    m_product_options_isValid = false;

    m_recurring_interval_isSet = false;
    m_recurring_interval_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_setup_isSet = false;
    m_setup_isValid = false;

    m_trial_isSet = false;
    m_trial_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIFlexiblePlan::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFlexiblePlan::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_currency_sign_isValid = ::OpenAPI::fromJsonValue(m_currency_sign, json[QString("currencySign")]);
    m_currency_sign_isSet = !json[QString("currencySign")].isNull() && m_currency_sign_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_is_trial_only_isValid = ::OpenAPI::fromJsonValue(m_is_trial_only, json[QString("isTrialOnly")]);
    m_is_trial_only_isSet = !json[QString("isTrialOnly")].isNull() && m_is_trial_only_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pricing_isValid = ::OpenAPI::fromJsonValue(m_pricing, json[QString("pricing")]);
    m_pricing_isSet = !json[QString("pricing")].isNull() && m_pricing_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("productId")]);
    m_product_id_isSet = !json[QString("productId")].isNull() && m_product_id_isValid;

    m_product_options_isValid = ::OpenAPI::fromJsonValue(m_product_options, json[QString("productOptions")]);
    m_product_options_isSet = !json[QString("productOptions")].isNull() && m_product_options_isValid;

    m_recurring_interval_isValid = ::OpenAPI::fromJsonValue(m_recurring_interval, json[QString("recurringInterval")]);
    m_recurring_interval_isSet = !json[QString("recurringInterval")].isNull() && m_recurring_interval_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_setup_isValid = ::OpenAPI::fromJsonValue(m_setup, json[QString("setup")]);
    m_setup_isSet = !json[QString("setup")].isNull() && m_setup_isValid;

    m_trial_isValid = ::OpenAPI::fromJsonValue(m_trial, json[QString("trial")]);
    m_trial_isSet = !json[QString("trial")].isNull() && m_trial_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAIFlexiblePlan::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFlexiblePlan::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_currency_sign_isSet) {
        obj.insert(QString("currencySign"), ::OpenAPI::toJsonValue(m_currency_sign));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_is_trial_only_isSet) {
        obj.insert(QString("isTrialOnly"), ::OpenAPI::toJsonValue(m_is_trial_only));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pricing.isSet()) {
        obj.insert(QString("pricing"), ::OpenAPI::toJsonValue(m_pricing));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("productId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_product_options.size() > 0) {
        obj.insert(QString("productOptions"), ::OpenAPI::toJsonValue(m_product_options));
    }
    if (m_recurring_interval.isSet()) {
        obj.insert(QString("recurringInterval"), ::OpenAPI::toJsonValue(m_recurring_interval));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_setup.isSet()) {
        obj.insert(QString("setup"), ::OpenAPI::toJsonValue(m_setup));
    }
    if (m_trial.isSet()) {
        obj.insert(QString("trial"), ::OpenAPI::toJsonValue(m_trial));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QString OAIFlexiblePlan::getId() const {
    return m_id;
}
void OAIFlexiblePlan::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFlexiblePlan::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFlexiblePlan::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIFlexiblePlan::getCreatedTime() const {
    return m_created_time;
}
void OAIFlexiblePlan::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIFlexiblePlan::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIFlexiblePlan::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIFlexiblePlan::getCurrency() const {
    return m_currency;
}
void OAIFlexiblePlan::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIFlexiblePlan::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIFlexiblePlan::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIFlexiblePlan::getCurrencySign() const {
    return m_currency_sign;
}
void OAIFlexiblePlan::setCurrencySign(const QString &currency_sign) {
    m_currency_sign = currency_sign;
    m_currency_sign_isSet = true;
}

bool OAIFlexiblePlan::is_currency_sign_Set() const{
    return m_currency_sign_isSet;
}

bool OAIFlexiblePlan::is_currency_sign_Valid() const{
    return m_currency_sign_isValid;
}

OAIObject OAIFlexiblePlan::getCustomFields() const {
    return m_custom_fields;
}
void OAIFlexiblePlan::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIFlexiblePlan::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIFlexiblePlan::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

bool OAIFlexiblePlan::isIsTrialOnly() const {
    return m_is_trial_only;
}
void OAIFlexiblePlan::setIsTrialOnly(const bool &is_trial_only) {
    m_is_trial_only = is_trial_only;
    m_is_trial_only_isSet = true;
}

bool OAIFlexiblePlan::is_is_trial_only_Set() const{
    return m_is_trial_only_isSet;
}

bool OAIFlexiblePlan::is_is_trial_only_Valid() const{
    return m_is_trial_only_isValid;
}

QString OAIFlexiblePlan::getName() const {
    return m_name;
}
void OAIFlexiblePlan::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFlexiblePlan::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFlexiblePlan::is_name_Valid() const{
    return m_name_isValid;
}

OAIPlanPriceFormula OAIFlexiblePlan::getPricing() const {
    return m_pricing;
}
void OAIFlexiblePlan::setPricing(const OAIPlanPriceFormula &pricing) {
    m_pricing = pricing;
    m_pricing_isSet = true;
}

bool OAIFlexiblePlan::is_pricing_Set() const{
    return m_pricing_isSet;
}

bool OAIFlexiblePlan::is_pricing_Valid() const{
    return m_pricing_isValid;
}

QString OAIFlexiblePlan::getProductId() const {
    return m_product_id;
}
void OAIFlexiblePlan::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIFlexiblePlan::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIFlexiblePlan::is_product_id_Valid() const{
    return m_product_id_isValid;
}

QMap<QString, QString> OAIFlexiblePlan::getProductOptions() const {
    return m_product_options;
}
void OAIFlexiblePlan::setProductOptions(const QMap<QString, QString> &product_options) {
    m_product_options = product_options;
    m_product_options_isSet = true;
}

bool OAIFlexiblePlan::is_product_options_Set() const{
    return m_product_options_isSet;
}

bool OAIFlexiblePlan::is_product_options_Valid() const{
    return m_product_options_isValid;
}

OAICommonPlan_recurringInterval OAIFlexiblePlan::getRecurringInterval() const {
    return m_recurring_interval;
}
void OAIFlexiblePlan::setRecurringInterval(const OAICommonPlan_recurringInterval &recurring_interval) {
    m_recurring_interval = recurring_interval;
    m_recurring_interval_isSet = true;
}

bool OAIFlexiblePlan::is_recurring_interval_Set() const{
    return m_recurring_interval_isSet;
}

bool OAIFlexiblePlan::is_recurring_interval_Valid() const{
    return m_recurring_interval_isValid;
}

qint32 OAIFlexiblePlan::getRevision() const {
    return m_revision;
}
void OAIFlexiblePlan::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAIFlexiblePlan::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAIFlexiblePlan::is_revision_Valid() const{
    return m_revision_isValid;
}

OAICommonPlan_setup OAIFlexiblePlan::getSetup() const {
    return m_setup;
}
void OAIFlexiblePlan::setSetup(const OAICommonPlan_setup &setup) {
    m_setup = setup;
    m_setup_isSet = true;
}

bool OAIFlexiblePlan::is_setup_Set() const{
    return m_setup_isSet;
}

bool OAIFlexiblePlan::is_setup_Valid() const{
    return m_setup_isValid;
}

OAICommonPlan_trial OAIFlexiblePlan::getTrial() const {
    return m_trial;
}
void OAIFlexiblePlan::setTrial(const OAICommonPlan_trial &trial) {
    m_trial = trial;
    m_trial_isSet = true;
}

bool OAIFlexiblePlan::is_trial_Set() const{
    return m_trial_isSet;
}

bool OAIFlexiblePlan::is_trial_Valid() const{
    return m_trial_isValid;
}

QDateTime OAIFlexiblePlan::getUpdatedTime() const {
    return m_updated_time;
}
void OAIFlexiblePlan::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIFlexiblePlan::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIFlexiblePlan::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIFlexiblePlan::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_sign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_trial_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pricing.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurring_interval.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_setup.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_trial.isSet()) {
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

bool OAIFlexiblePlan::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_currency_isValid && m_name_isValid && m_pricing_isValid && m_product_id_isValid && true;
}

} // namespace OpenAPI
