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

#include "OAIDispute.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDispute::OAIDispute(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDispute::OAIDispute() {
    this->initializeModel();
}

OAIDispute::~OAIDispute() {}

void OAIDispute::initializeModel() {

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_acquirer_reference_number_isSet = false;
    m_acquirer_reference_number_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_case_id_isSet = false;
    m_case_id_isValid = false;

    m_category_isSet = false;
    m_category_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_deadline_time_isSet = false;
    m_deadline_time_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_posted_time_isSet = false;
    m_posted_time_isValid = false;

    m_raw_response_isSet = false;
    m_raw_response_isValid = false;

    m_reason_code_isSet = false;
    m_reason_code_isValid = false;

    m_resolved_time_isSet = false;
    m_resolved_time_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIDispute::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDispute::fromJsonObject(QJsonObject json) {

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_acquirer_reference_number_isValid = ::OpenAPI::fromJsonValue(m_acquirer_reference_number, json[QString("acquirerReferenceNumber")]);
    m_acquirer_reference_number_isSet = !json[QString("acquirerReferenceNumber")].isNull() && m_acquirer_reference_number_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_case_id_isValid = ::OpenAPI::fromJsonValue(m_case_id, json[QString("caseId")]);
    m_case_id_isSet = !json[QString("caseId")].isNull() && m_case_id_isValid;

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_deadline_time_isValid = ::OpenAPI::fromJsonValue(m_deadline_time, json[QString("deadlineTime")]);
    m_deadline_time_isSet = !json[QString("deadlineTime")].isNull() && m_deadline_time_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_posted_time_isValid = ::OpenAPI::fromJsonValue(m_posted_time, json[QString("postedTime")]);
    m_posted_time_isSet = !json[QString("postedTime")].isNull() && m_posted_time_isValid;

    m_raw_response_isValid = ::OpenAPI::fromJsonValue(m_raw_response, json[QString("rawResponse")]);
    m_raw_response_isSet = !json[QString("rawResponse")].isNull() && m_raw_response_isValid;

    m_reason_code_isValid = ::OpenAPI::fromJsonValue(m_reason_code, json[QString("reasonCode")]);
    m_reason_code_isSet = !json[QString("reasonCode")].isNull() && m_reason_code_isValid;

    m_resolved_time_isValid = ::OpenAPI::fromJsonValue(m_resolved_time, json[QString("resolvedTime")]);
    m_resolved_time_isSet = !json[QString("resolvedTime")].isNull() && m_resolved_time_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("transactionId")]);
    m_transaction_id_isSet = !json[QString("transactionId")].isNull() && m_transaction_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;
}

QString OAIDispute::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDispute::asJsonObject() const {
    QJsonObject obj;
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_acquirer_reference_number_isSet) {
        obj.insert(QString("acquirerReferenceNumber"), ::OpenAPI::toJsonValue(m_acquirer_reference_number));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_case_id_isSet) {
        obj.insert(QString("caseId"), ::OpenAPI::toJsonValue(m_case_id));
    }
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_deadline_time_isSet) {
        obj.insert(QString("deadlineTime"), ::OpenAPI::toJsonValue(m_deadline_time));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_posted_time_isSet) {
        obj.insert(QString("postedTime"), ::OpenAPI::toJsonValue(m_posted_time));
    }
    if (m_raw_response_isSet) {
        obj.insert(QString("rawResponse"), ::OpenAPI::toJsonValue(m_raw_response));
    }
    if (m_reason_code_isSet) {
        obj.insert(QString("reasonCode"), ::OpenAPI::toJsonValue(m_reason_code));
    }
    if (m_resolved_time_isSet) {
        obj.insert(QString("resolvedTime"), ::OpenAPI::toJsonValue(m_resolved_time));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_transaction_id_isSet) {
        obj.insert(QString("transactionId"), ::OpenAPI::toJsonValue(m_transaction_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QList<OAIDispute__embedded_inner> OAIDispute::getEmbedded() const {
    return m__embedded;
}
void OAIDispute::setEmbedded(const QList<OAIDispute__embedded_inner> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAIDispute::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAIDispute::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAIDispute__links_inner> OAIDispute::getLinks() const {
    return m__links;
}
void OAIDispute::setLinks(const QList<OAIDispute__links_inner> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIDispute::is__links_Set() const{
    return m__links_isSet;
}

bool OAIDispute::is__links_Valid() const{
    return m__links_isValid;
}

QString OAIDispute::getAcquirerReferenceNumber() const {
    return m_acquirer_reference_number;
}
void OAIDispute::setAcquirerReferenceNumber(const QString &acquirer_reference_number) {
    m_acquirer_reference_number = acquirer_reference_number;
    m_acquirer_reference_number_isSet = true;
}

bool OAIDispute::is_acquirer_reference_number_Set() const{
    return m_acquirer_reference_number_isSet;
}

bool OAIDispute::is_acquirer_reference_number_Valid() const{
    return m_acquirer_reference_number_isValid;
}

double OAIDispute::getAmount() const {
    return m_amount;
}
void OAIDispute::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIDispute::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIDispute::is_amount_Valid() const{
    return m_amount_isValid;
}

QString OAIDispute::getCaseId() const {
    return m_case_id;
}
void OAIDispute::setCaseId(const QString &case_id) {
    m_case_id = case_id;
    m_case_id_isSet = true;
}

bool OAIDispute::is_case_id_Set() const{
    return m_case_id_isSet;
}

bool OAIDispute::is_case_id_Valid() const{
    return m_case_id_isValid;
}

QString OAIDispute::getCategory() const {
    return m_category;
}
void OAIDispute::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAIDispute::is_category_Set() const{
    return m_category_isSet;
}

bool OAIDispute::is_category_Valid() const{
    return m_category_isValid;
}

QDateTime OAIDispute::getCreatedTime() const {
    return m_created_time;
}
void OAIDispute::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIDispute::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIDispute::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAIDispute::getCurrency() const {
    return m_currency;
}
void OAIDispute::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIDispute::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIDispute::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIDispute::getCustomerId() const {
    return m_customer_id;
}
void OAIDispute::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIDispute::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIDispute::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QDateTime OAIDispute::getDeadlineTime() const {
    return m_deadline_time;
}
void OAIDispute::setDeadlineTime(const QDateTime &deadline_time) {
    m_deadline_time = deadline_time;
    m_deadline_time_isSet = true;
}

bool OAIDispute::is_deadline_time_Set() const{
    return m_deadline_time_isSet;
}

bool OAIDispute::is_deadline_time_Valid() const{
    return m_deadline_time_isValid;
}

QString OAIDispute::getId() const {
    return m_id;
}
void OAIDispute::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDispute::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDispute::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIDispute::getPostedTime() const {
    return m_posted_time;
}
void OAIDispute::setPostedTime(const QDateTime &posted_time) {
    m_posted_time = posted_time;
    m_posted_time_isSet = true;
}

bool OAIDispute::is_posted_time_Set() const{
    return m_posted_time_isSet;
}

bool OAIDispute::is_posted_time_Valid() const{
    return m_posted_time_isValid;
}

QString OAIDispute::getRawResponse() const {
    return m_raw_response;
}
void OAIDispute::setRawResponse(const QString &raw_response) {
    m_raw_response = raw_response;
    m_raw_response_isSet = true;
}

bool OAIDispute::is_raw_response_Set() const{
    return m_raw_response_isSet;
}

bool OAIDispute::is_raw_response_Valid() const{
    return m_raw_response_isValid;
}

QString OAIDispute::getReasonCode() const {
    return m_reason_code;
}
void OAIDispute::setReasonCode(const QString &reason_code) {
    m_reason_code = reason_code;
    m_reason_code_isSet = true;
}

bool OAIDispute::is_reason_code_Set() const{
    return m_reason_code_isSet;
}

bool OAIDispute::is_reason_code_Valid() const{
    return m_reason_code_isValid;
}

QDateTime OAIDispute::getResolvedTime() const {
    return m_resolved_time;
}
void OAIDispute::setResolvedTime(const QDateTime &resolved_time) {
    m_resolved_time = resolved_time;
    m_resolved_time_isSet = true;
}

bool OAIDispute::is_resolved_time_Set() const{
    return m_resolved_time_isSet;
}

bool OAIDispute::is_resolved_time_Valid() const{
    return m_resolved_time_isValid;
}

QString OAIDispute::getStatus() const {
    return m_status;
}
void OAIDispute::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIDispute::is_status_Set() const{
    return m_status_isSet;
}

bool OAIDispute::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIDispute::getTransactionId() const {
    return m_transaction_id;
}
void OAIDispute::setTransactionId(const QString &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIDispute::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIDispute::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

QString OAIDispute::getType() const {
    return m_type;
}
void OAIDispute::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDispute::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDispute::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIDispute::getUpdatedTime() const {
    return m_updated_time;
}
void OAIDispute::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIDispute::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIDispute::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIDispute::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__embedded.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_acquirer_reference_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_case_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_category_isSet) {
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

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deadline_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_posted_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_raw_response_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resolved_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_id_isSet) {
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

bool OAIDispute::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_currency_isValid && m_posted_time_isValid && m_reason_code_isValid && m_status_isValid && m_transaction_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
