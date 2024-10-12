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

#include "OAIPayoutRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPayoutRequest::OAIPayoutRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPayoutRequest::OAIPayoutRequest() {
    this->initializeModel();
}

OAIPayoutRequest::~OAIPayoutRequest() {}

void OAIPayoutRequest::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_gateway_account_id_isSet = false;
    m_gateway_account_id_isValid = false;

    m_invoice_ids_isSet = false;
    m_invoice_ids_isValid = false;

    m_is_merchant_initiated_isSet = false;
    m_is_merchant_initiated_isValid = false;

    m_is_processed_outside_isSet = false;
    m_is_processed_outside_isValid = false;

    m_notification_url_isSet = false;
    m_notification_url_isValid = false;

    m_payment_instruction_isSet = false;
    m_payment_instruction_isValid = false;

    m_payment_instrument_isSet = false;
    m_payment_instrument_isValid = false;

    m_processed_time_isSet = false;
    m_processed_time_isValid = false;

    m_redirect_url_isSet = false;
    m_redirect_url_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;
}

void OAIPayoutRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPayoutRequest::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_gateway_account_id_isValid = ::OpenAPI::fromJsonValue(m_gateway_account_id, json[QString("gatewayAccountId")]);
    m_gateway_account_id_isSet = !json[QString("gatewayAccountId")].isNull() && m_gateway_account_id_isValid;

    m_invoice_ids_isValid = ::OpenAPI::fromJsonValue(m_invoice_ids, json[QString("invoiceIds")]);
    m_invoice_ids_isSet = !json[QString("invoiceIds")].isNull() && m_invoice_ids_isValid;

    m_is_merchant_initiated_isValid = ::OpenAPI::fromJsonValue(m_is_merchant_initiated, json[QString("isMerchantInitiated")]);
    m_is_merchant_initiated_isSet = !json[QString("isMerchantInitiated")].isNull() && m_is_merchant_initiated_isValid;

    m_is_processed_outside_isValid = ::OpenAPI::fromJsonValue(m_is_processed_outside, json[QString("isProcessedOutside")]);
    m_is_processed_outside_isSet = !json[QString("isProcessedOutside")].isNull() && m_is_processed_outside_isValid;

    m_notification_url_isValid = ::OpenAPI::fromJsonValue(m_notification_url, json[QString("notificationUrl")]);
    m_notification_url_isSet = !json[QString("notificationUrl")].isNull() && m_notification_url_isValid;

    m_payment_instruction_isValid = ::OpenAPI::fromJsonValue(m_payment_instruction, json[QString("paymentInstruction")]);
    m_payment_instruction_isSet = !json[QString("paymentInstruction")].isNull() && m_payment_instruction_isValid;

    m_payment_instrument_isValid = ::OpenAPI::fromJsonValue(m_payment_instrument, json[QString("paymentInstrument")]);
    m_payment_instrument_isSet = !json[QString("paymentInstrument")].isNull() && m_payment_instrument_isValid;

    m_processed_time_isValid = ::OpenAPI::fromJsonValue(m_processed_time, json[QString("processedTime")]);
    m_processed_time_isSet = !json[QString("processedTime")].isNull() && m_processed_time_isValid;

    m_redirect_url_isValid = ::OpenAPI::fromJsonValue(m_redirect_url, json[QString("redirectUrl")]);
    m_redirect_url_isSet = !json[QString("redirectUrl")].isNull() && m_redirect_url_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;
}

QString OAIPayoutRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPayoutRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_gateway_account_id_isSet) {
        obj.insert(QString("gatewayAccountId"), ::OpenAPI::toJsonValue(m_gateway_account_id));
    }
    if (m_invoice_ids.size() > 0) {
        obj.insert(QString("invoiceIds"), ::OpenAPI::toJsonValue(m_invoice_ids));
    }
    if (m_is_merchant_initiated_isSet) {
        obj.insert(QString("isMerchantInitiated"), ::OpenAPI::toJsonValue(m_is_merchant_initiated));
    }
    if (m_is_processed_outside_isSet) {
        obj.insert(QString("isProcessedOutside"), ::OpenAPI::toJsonValue(m_is_processed_outside));
    }
    if (m_notification_url_isSet) {
        obj.insert(QString("notificationUrl"), ::OpenAPI::toJsonValue(m_notification_url));
    }
    if (m_payment_instruction.isSet()) {
        obj.insert(QString("paymentInstruction"), ::OpenAPI::toJsonValue(m_payment_instruction));
    }
    if (m_payment_instrument.isSet()) {
        obj.insert(QString("paymentInstrument"), ::OpenAPI::toJsonValue(m_payment_instrument));
    }
    if (m_processed_time_isSet) {
        obj.insert(QString("processedTime"), ::OpenAPI::toJsonValue(m_processed_time));
    }
    if (m_redirect_url_isSet) {
        obj.insert(QString("redirectUrl"), ::OpenAPI::toJsonValue(m_redirect_url));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    return obj;
}

double OAIPayoutRequest::getAmount() const {
    return m_amount;
}
void OAIPayoutRequest::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIPayoutRequest::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIPayoutRequest::is_amount_Valid() const{
    return m_amount_isValid;
}

OAIContactObject OAIPayoutRequest::getBillingAddress() const {
    return m_billing_address;
}
void OAIPayoutRequest::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIPayoutRequest::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIPayoutRequest::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIPayoutRequest::getCurrency() const {
    return m_currency;
}
void OAIPayoutRequest::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIPayoutRequest::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIPayoutRequest::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAIPayoutRequest::getCustomFields() const {
    return m_custom_fields;
}
void OAIPayoutRequest::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIPayoutRequest::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIPayoutRequest::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIPayoutRequest::getCustomerId() const {
    return m_customer_id;
}
void OAIPayoutRequest::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIPayoutRequest::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIPayoutRequest::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAIPayoutRequest::getDescription() const {
    return m_description;
}
void OAIPayoutRequest::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPayoutRequest::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPayoutRequest::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIPayoutRequest::getGatewayAccountId() const {
    return m_gateway_account_id;
}
void OAIPayoutRequest::setGatewayAccountId(const QString &gateway_account_id) {
    m_gateway_account_id = gateway_account_id;
    m_gateway_account_id_isSet = true;
}

bool OAIPayoutRequest::is_gateway_account_id_Set() const{
    return m_gateway_account_id_isSet;
}

bool OAIPayoutRequest::is_gateway_account_id_Valid() const{
    return m_gateway_account_id_isValid;
}

QList<QString> OAIPayoutRequest::getInvoiceIds() const {
    return m_invoice_ids;
}
void OAIPayoutRequest::setInvoiceIds(const QList<QString> &invoice_ids) {
    m_invoice_ids = invoice_ids;
    m_invoice_ids_isSet = true;
}

bool OAIPayoutRequest::is_invoice_ids_Set() const{
    return m_invoice_ids_isSet;
}

bool OAIPayoutRequest::is_invoice_ids_Valid() const{
    return m_invoice_ids_isValid;
}

bool OAIPayoutRequest::isIsMerchantInitiated() const {
    return m_is_merchant_initiated;
}
void OAIPayoutRequest::setIsMerchantInitiated(const bool &is_merchant_initiated) {
    m_is_merchant_initiated = is_merchant_initiated;
    m_is_merchant_initiated_isSet = true;
}

bool OAIPayoutRequest::is_is_merchant_initiated_Set() const{
    return m_is_merchant_initiated_isSet;
}

bool OAIPayoutRequest::is_is_merchant_initiated_Valid() const{
    return m_is_merchant_initiated_isValid;
}

bool OAIPayoutRequest::isIsProcessedOutside() const {
    return m_is_processed_outside;
}
void OAIPayoutRequest::setIsProcessedOutside(const bool &is_processed_outside) {
    m_is_processed_outside = is_processed_outside;
    m_is_processed_outside_isSet = true;
}

bool OAIPayoutRequest::is_is_processed_outside_Set() const{
    return m_is_processed_outside_isSet;
}

bool OAIPayoutRequest::is_is_processed_outside_Valid() const{
    return m_is_processed_outside_isValid;
}

QString OAIPayoutRequest::getNotificationUrl() const {
    return m_notification_url;
}
void OAIPayoutRequest::setNotificationUrl(const QString &notification_url) {
    m_notification_url = notification_url;
    m_notification_url_isSet = true;
}

bool OAIPayoutRequest::is_notification_url_Set() const{
    return m_notification_url_isSet;
}

bool OAIPayoutRequest::is_notification_url_Valid() const{
    return m_notification_url_isValid;
}

OAIPaymentInstruction OAIPayoutRequest::getPaymentInstruction() const {
    return m_payment_instruction;
}
void OAIPayoutRequest::setPaymentInstruction(const OAIPaymentInstruction &payment_instruction) {
    m_payment_instruction = payment_instruction;
    m_payment_instruction_isSet = true;
}

bool OAIPayoutRequest::is_payment_instruction_Set() const{
    return m_payment_instruction_isSet;
}

bool OAIPayoutRequest::is_payment_instruction_Valid() const{
    return m_payment_instruction_isValid;
}

OAIPaymentInstrument OAIPayoutRequest::getPaymentInstrument() const {
    return m_payment_instrument;
}
void OAIPayoutRequest::setPaymentInstrument(const OAIPaymentInstrument &payment_instrument) {
    m_payment_instrument = payment_instrument;
    m_payment_instrument_isSet = true;
}

bool OAIPayoutRequest::is_payment_instrument_Set() const{
    return m_payment_instrument_isSet;
}

bool OAIPayoutRequest::is_payment_instrument_Valid() const{
    return m_payment_instrument_isValid;
}

QDateTime OAIPayoutRequest::getProcessedTime() const {
    return m_processed_time;
}
void OAIPayoutRequest::setProcessedTime(const QDateTime &processed_time) {
    m_processed_time = processed_time;
    m_processed_time_isSet = true;
}

bool OAIPayoutRequest::is_processed_time_Set() const{
    return m_processed_time_isSet;
}

bool OAIPayoutRequest::is_processed_time_Valid() const{
    return m_processed_time_isValid;
}

QString OAIPayoutRequest::getRedirectUrl() const {
    return m_redirect_url;
}
void OAIPayoutRequest::setRedirectUrl(const QString &redirect_url) {
    m_redirect_url = redirect_url;
    m_redirect_url_isSet = true;
}

bool OAIPayoutRequest::is_redirect_url_Set() const{
    return m_redirect_url_isSet;
}

bool OAIPayoutRequest::is_redirect_url_Valid() const{
    return m_redirect_url_isValid;
}

QString OAIPayoutRequest::getRequestId() const {
    return m_request_id;
}
void OAIPayoutRequest::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAIPayoutRequest::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAIPayoutRequest::is_request_id_Valid() const{
    return m_request_id_isValid;
}

OAIRiskMetadata OAIPayoutRequest::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAIPayoutRequest::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAIPayoutRequest::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAIPayoutRequest::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

QString OAIPayoutRequest::getWebsiteId() const {
    return m_website_id;
}
void OAIPayoutRequest::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAIPayoutRequest::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAIPayoutRequest::is_website_id_Valid() const{
    return m_website_id_isValid;
}

bool OAIPayoutRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_merchant_initiated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_processed_outside_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instruction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instrument.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_processed_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_redirect_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPayoutRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_currency_isValid && m_customer_id_isValid && m_website_id_isValid && true;
}

} // namespace OpenAPI
