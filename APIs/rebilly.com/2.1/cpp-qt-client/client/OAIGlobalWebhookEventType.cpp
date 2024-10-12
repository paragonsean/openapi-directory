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

#include "OAIGlobalWebhookEventType.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGlobalWebhookEventType::OAIGlobalWebhookEventType(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGlobalWebhookEventType::OAIGlobalWebhookEventType() {
    this->initializeModel();
}

OAIGlobalWebhookEventType::~OAIGlobalWebhookEventType() {}

void OAIGlobalWebhookEventType::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIGlobalWebhookEventType::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIGlobalWebhookEventType::fromJson(QString jsonString) {
    
    if ( jsonString.compare("aml-list-possibly-matched", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::AML_LIST_POSSIBLY_MATCHED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("customer-created", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::CUSTOMER_CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("customer-merged", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::CUSTOMER_MERGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("customer-one-time-password-requested", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::CUSTOMER_ONE_TIME_PASSWORD_REQUESTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("customer-updated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::CUSTOMER_UPDATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("dispute-created", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::DISPUTE_CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("experian-check-performed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::EXPERIAN_CHECK_PERFORMED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gateway-account-downtime-ended", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_DOWNTIME_ENDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gateway-account-downtime-started", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_DOWNTIME_STARTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gateway-account-limit-reached", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_LIMIT_REACHED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gateway-account-requested", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_REQUESTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-abandoned", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_ABANDONED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-created", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-issued", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_ISSUED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-modified", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_MODIFIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-paid", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_PAID;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-past-due", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_PAST_DUE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-past-due-reminder", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_PAST_DUE_REMINDER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-reissued", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_REISSUED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("invoice-voided", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::INVOICE_VOIDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kyc-document-accepted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::KYC_DOCUMENT_ACCEPTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kyc-document-created", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::KYC_DOCUMENT_CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kyc-document-modified", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::KYC_DOCUMENT_MODIFIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kyc-document-rejected", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::KYC_DOCUMENT_REJECTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kyc-document-reviewed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::KYC_DOCUMENT_REVIEWED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lead-source-changed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::LEAD_SOURCE_CHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nsf-response-received", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::NSF_RESPONSE_RECEIVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("offsite-payment-completed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::OFFSITE_PAYMENT_COMPLETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("order-completed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::ORDER_COMPLETED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("payment-card-created", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::PAYMENT_CARD_CREATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("payment-card-expiration-reminder", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::PAYMENT_CARD_EXPIRATION_REMINDER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("payment-card-expired", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::PAYMENT_CARD_EXPIRED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("payment-instrument-modified", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::PAYMENT_INSTRUMENT_MODIFIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("renewal-invoice-issued", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::RENEWAL_INVOICE_ISSUED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("renewal-invoice-payment-canceled", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::RENEWAL_INVOICE_PAYMENT_CANCELED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("renewal-invoice-payment-declined", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::RENEWAL_INVOICE_PAYMENT_DECLINED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("risk-score-changed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::RISK_SCORE_CHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-activated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_ACTIVATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-canceled", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_CANCELED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-modified", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_MODIFIED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-reactivated", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_REACTIVATED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-renewal-reminder", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_RENEWAL_REMINDER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-renewed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_RENEWED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-trial-converted", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_CONVERTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-trial-end-reminder", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_END_REMINDER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-trial-ended", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_ENDED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("subscription-trial-end-changed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_END_CHANGED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-amount-discrepancy-found", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_AMOUNT_DISCREPANCY_FOUND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-declined", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_DECLINED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-discrepancy-found", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_DISCREPANCY_FOUND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-process-requested", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_PROCESS_REQUESTED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-processed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_PROCESSED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-reconciled", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_RECONCILED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("transaction-timeout-resolved", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::TRANSACTION_TIMEOUT_RESOLVED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("waiting-gateway-transaction-completed", Qt::CaseInsensitive) == 0) {
        m_value = eOAIGlobalWebhookEventType::WAITING_GATEWAY_TRANSACTION_COMPLETED;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIGlobalWebhookEventType::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIGlobalWebhookEventType::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIGlobalWebhookEventType::AML_LIST_POSSIBLY_MATCHED:
            val = "aml-list-possibly-matched";
            break;
        case eOAIGlobalWebhookEventType::CUSTOMER_CREATED:
            val = "customer-created";
            break;
        case eOAIGlobalWebhookEventType::CUSTOMER_MERGED:
            val = "customer-merged";
            break;
        case eOAIGlobalWebhookEventType::CUSTOMER_ONE_TIME_PASSWORD_REQUESTED:
            val = "customer-one-time-password-requested";
            break;
        case eOAIGlobalWebhookEventType::CUSTOMER_UPDATED:
            val = "customer-updated";
            break;
        case eOAIGlobalWebhookEventType::DISPUTE_CREATED:
            val = "dispute-created";
            break;
        case eOAIGlobalWebhookEventType::EXPERIAN_CHECK_PERFORMED:
            val = "experian-check-performed";
            break;
        case eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_DOWNTIME_ENDED:
            val = "gateway-account-downtime-ended";
            break;
        case eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_DOWNTIME_STARTED:
            val = "gateway-account-downtime-started";
            break;
        case eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_LIMIT_REACHED:
            val = "gateway-account-limit-reached";
            break;
        case eOAIGlobalWebhookEventType::GATEWAY_ACCOUNT_REQUESTED:
            val = "gateway-account-requested";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_ABANDONED:
            val = "invoice-abandoned";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_CREATED:
            val = "invoice-created";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_ISSUED:
            val = "invoice-issued";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_MODIFIED:
            val = "invoice-modified";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_PAID:
            val = "invoice-paid";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_PAST_DUE:
            val = "invoice-past-due";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_PAST_DUE_REMINDER:
            val = "invoice-past-due-reminder";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_REISSUED:
            val = "invoice-reissued";
            break;
        case eOAIGlobalWebhookEventType::INVOICE_VOIDED:
            val = "invoice-voided";
            break;
        case eOAIGlobalWebhookEventType::KYC_DOCUMENT_ACCEPTED:
            val = "kyc-document-accepted";
            break;
        case eOAIGlobalWebhookEventType::KYC_DOCUMENT_CREATED:
            val = "kyc-document-created";
            break;
        case eOAIGlobalWebhookEventType::KYC_DOCUMENT_MODIFIED:
            val = "kyc-document-modified";
            break;
        case eOAIGlobalWebhookEventType::KYC_DOCUMENT_REJECTED:
            val = "kyc-document-rejected";
            break;
        case eOAIGlobalWebhookEventType::KYC_DOCUMENT_REVIEWED:
            val = "kyc-document-reviewed";
            break;
        case eOAIGlobalWebhookEventType::LEAD_SOURCE_CHANGED:
            val = "lead-source-changed";
            break;
        case eOAIGlobalWebhookEventType::NSF_RESPONSE_RECEIVED:
            val = "nsf-response-received";
            break;
        case eOAIGlobalWebhookEventType::OFFSITE_PAYMENT_COMPLETED:
            val = "offsite-payment-completed";
            break;
        case eOAIGlobalWebhookEventType::ORDER_COMPLETED:
            val = "order-completed";
            break;
        case eOAIGlobalWebhookEventType::PAYMENT_CARD_CREATED:
            val = "payment-card-created";
            break;
        case eOAIGlobalWebhookEventType::PAYMENT_CARD_EXPIRATION_REMINDER:
            val = "payment-card-expiration-reminder";
            break;
        case eOAIGlobalWebhookEventType::PAYMENT_CARD_EXPIRED:
            val = "payment-card-expired";
            break;
        case eOAIGlobalWebhookEventType::PAYMENT_INSTRUMENT_MODIFIED:
            val = "payment-instrument-modified";
            break;
        case eOAIGlobalWebhookEventType::RENEWAL_INVOICE_ISSUED:
            val = "renewal-invoice-issued";
            break;
        case eOAIGlobalWebhookEventType::RENEWAL_INVOICE_PAYMENT_CANCELED:
            val = "renewal-invoice-payment-canceled";
            break;
        case eOAIGlobalWebhookEventType::RENEWAL_INVOICE_PAYMENT_DECLINED:
            val = "renewal-invoice-payment-declined";
            break;
        case eOAIGlobalWebhookEventType::RISK_SCORE_CHANGED:
            val = "risk-score-changed";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_ACTIVATED:
            val = "subscription-activated";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_CANCELED:
            val = "subscription-canceled";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_MODIFIED:
            val = "subscription-modified";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_REACTIVATED:
            val = "subscription-reactivated";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_RENEWAL_REMINDER:
            val = "subscription-renewal-reminder";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_RENEWED:
            val = "subscription-renewed";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_CONVERTED:
            val = "subscription-trial-converted";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_END_REMINDER:
            val = "subscription-trial-end-reminder";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_ENDED:
            val = "subscription-trial-ended";
            break;
        case eOAIGlobalWebhookEventType::SUBSCRIPTION_TRIAL_END_CHANGED:
            val = "subscription-trial-end-changed";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_AMOUNT_DISCREPANCY_FOUND:
            val = "transaction-amount-discrepancy-found";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_DECLINED:
            val = "transaction-declined";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_DISCREPANCY_FOUND:
            val = "transaction-discrepancy-found";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_PROCESS_REQUESTED:
            val = "transaction-process-requested";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_PROCESSED:
            val = "transaction-processed";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_RECONCILED:
            val = "transaction-reconciled";
            break;
        case eOAIGlobalWebhookEventType::TRANSACTION_TIMEOUT_RESOLVED:
            val = "transaction-timeout-resolved";
            break;
        case eOAIGlobalWebhookEventType::WAITING_GATEWAY_TRANSACTION_COMPLETED:
            val = "waiting-gateway-transaction-completed";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIGlobalWebhookEventType::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIGlobalWebhookEventType::eOAIGlobalWebhookEventType OAIGlobalWebhookEventType::getValue() const {
    return m_value;
}

void OAIGlobalWebhookEventType::setValue(const OAIGlobalWebhookEventType::eOAIGlobalWebhookEventType& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIGlobalWebhookEventType::isSet() const {
    
    return m_value_isSet;
}

bool OAIGlobalWebhookEventType::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
