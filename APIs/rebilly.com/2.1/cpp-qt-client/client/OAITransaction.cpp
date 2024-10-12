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

#include "OAITransaction.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransaction::OAITransaction(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransaction::OAITransaction() {
    this->initializeModel();
}

OAITransaction::~OAITransaction() {}

void OAITransaction::initializeModel() {

    m_r_3ds_isSet = false;
    m_r_3ds_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_billing_descriptor_isSet = false;
    m_billing_descriptor_isValid = false;

    m_child_transactions_isSet = false;
    m_child_transactions_isValid = false;

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_gateway_name_isSet = false;
    m_gateway_name_isValid = false;

    m_has3ds_isSet = false;
    m_has3ds_isValid = false;

    m_has_amount_adjustment_isSet = false;
    m_has_amount_adjustment_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_ids_isSet = false;
    m_invoice_ids_isValid = false;

    m_is_rebill_isSet = false;
    m_is_rebill_isValid = false;

    m_is_retry_isSet = false;
    m_is_retry_isValid = false;

    m_parent_transaction_id_isSet = false;
    m_parent_transaction_id_isValid = false;

    m_payment_instrument_isSet = false;
    m_payment_instrument_isValid = false;

    m_plan_ids_isSet = false;
    m_plan_ids_isValid = false;

    m_processed_time_isSet = false;
    m_processed_time_isValid = false;

    m_purchase_amount_isSet = false;
    m_purchase_amount_isValid = false;

    m_purchase_currency_isSet = false;
    m_purchase_currency_isValid = false;

    m_rebill_number_isSet = false;
    m_rebill_number_isValid = false;

    m_redirect_url_isSet = false;
    m_redirect_url_isValid = false;

    m_request_amount_isSet = false;
    m_request_amount_isValid = false;

    m_request_currency_isSet = false;
    m_request_currency_isValid = false;

    m_request_id_isSet = false;
    m_request_id_isValid = false;

    m_result_isSet = false;
    m_result_isValid = false;

    m_retry_number_isSet = false;
    m_retry_number_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subscription_ids_isSet = false;
    m_subscription_ids_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_website_id_isSet = false;
    m_website_id_isValid = false;

    m__embedded_isSet = false;
    m__embedded_isValid = false;

    m__links_isSet = false;
    m__links_isValid = false;

    m_acquirer_name_isSet = false;
    m_acquirer_name_isValid = false;

    m_arn_isSet = false;
    m_arn_isValid = false;

    m_bin_isSet = false;
    m_bin_isValid = false;

    m_bump_offer_isSet = false;
    m_bump_offer_isValid = false;

    m_dcc_isSet = false;
    m_dcc_isValid = false;

    m_discrepancy_time_isSet = false;
    m_discrepancy_time_isValid = false;

    m_dispute_status_isSet = false;
    m_dispute_status_isValid = false;

    m_dispute_time_isSet = false;
    m_dispute_time_isValid = false;

    m_gateway_isSet = false;
    m_gateway_isValid = false;

    m_gateway_account_id_isSet = false;
    m_gateway_account_id_isValid = false;

    m_gateway_transaction_id_isSet = false;
    m_gateway_transaction_id_isValid = false;

    m_had_discrepancy_isSet = false;
    m_had_discrepancy_isValid = false;

    m_has_bump_offer_isSet = false;
    m_has_bump_offer_isValid = false;

    m_has_dcc_isSet = false;
    m_has_dcc_isValid = false;

    m_is_disputed_isSet = false;
    m_is_disputed_isValid = false;

    m_is_merchant_initiated_isSet = false;
    m_is_merchant_initiated_isValid = false;

    m_is_processed_outside_isSet = false;
    m_is_processed_outside_isValid = false;

    m_is_reconciled_isSet = false;
    m_is_reconciled_isValid = false;

    m_method_isSet = false;
    m_method_isValid = false;

    m_notification_url_isSet = false;
    m_notification_url_isValid = false;

    m_order_id_isSet = false;
    m_order_id_isValid = false;

    m_reference_data_isSet = false;
    m_reference_data_isValid = false;

    m_report_amount_isSet = false;
    m_report_amount_isValid = false;

    m_report_currency_isSet = false;
    m_report_currency_isValid = false;

    m_retried_transaction_id_isSet = false;
    m_retried_transaction_id_isValid = false;

    m_retries_result_isSet = false;
    m_retries_result_isValid = false;

    m_retry_instruction_isSet = false;
    m_retry_instruction_isValid = false;

    m_revision_isSet = false;
    m_revision_isValid = false;

    m_risk_metadata_isSet = false;
    m_risk_metadata_isValid = false;

    m_risk_score_isSet = false;
    m_risk_score_isValid = false;

    m_scheduled_time_isSet = false;
    m_scheduled_time_isValid = false;

    m_settlement_time_isSet = false;
    m_settlement_time_isValid = false;

    m_velocity_isSet = false;
    m_velocity_isValid = false;
}

void OAITransaction::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransaction::fromJsonObject(QJsonObject json) {

    m_r_3ds_isValid = ::OpenAPI::fromJsonValue(m_r_3ds, json[QString("3ds")]);
    m_r_3ds_isSet = !json[QString("3ds")].isNull() && m_r_3ds_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billingAddress")]);
    m_billing_address_isSet = !json[QString("billingAddress")].isNull() && m_billing_address_isValid;

    m_billing_descriptor_isValid = ::OpenAPI::fromJsonValue(m_billing_descriptor, json[QString("billingDescriptor")]);
    m_billing_descriptor_isSet = !json[QString("billingDescriptor")].isNull() && m_billing_descriptor_isValid;

    m_child_transactions_isValid = ::OpenAPI::fromJsonValue(m_child_transactions, json[QString("childTransactions")]);
    m_child_transactions_isSet = !json[QString("childTransactions")].isNull() && m_child_transactions_isValid;

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_gateway_name_isValid = ::OpenAPI::fromJsonValue(m_gateway_name, json[QString("gatewayName")]);
    m_gateway_name_isSet = !json[QString("gatewayName")].isNull() && m_gateway_name_isValid;

    m_has3ds_isValid = ::OpenAPI::fromJsonValue(m_has3ds, json[QString("has3ds")]);
    m_has3ds_isSet = !json[QString("has3ds")].isNull() && m_has3ds_isValid;

    m_has_amount_adjustment_isValid = ::OpenAPI::fromJsonValue(m_has_amount_adjustment, json[QString("hasAmountAdjustment")]);
    m_has_amount_adjustment_isSet = !json[QString("hasAmountAdjustment")].isNull() && m_has_amount_adjustment_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_ids_isValid = ::OpenAPI::fromJsonValue(m_invoice_ids, json[QString("invoiceIds")]);
    m_invoice_ids_isSet = !json[QString("invoiceIds")].isNull() && m_invoice_ids_isValid;

    m_is_rebill_isValid = ::OpenAPI::fromJsonValue(m_is_rebill, json[QString("isRebill")]);
    m_is_rebill_isSet = !json[QString("isRebill")].isNull() && m_is_rebill_isValid;

    m_is_retry_isValid = ::OpenAPI::fromJsonValue(m_is_retry, json[QString("isRetry")]);
    m_is_retry_isSet = !json[QString("isRetry")].isNull() && m_is_retry_isValid;

    m_parent_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_parent_transaction_id, json[QString("parentTransactionId")]);
    m_parent_transaction_id_isSet = !json[QString("parentTransactionId")].isNull() && m_parent_transaction_id_isValid;

    m_payment_instrument_isValid = ::OpenAPI::fromJsonValue(m_payment_instrument, json[QString("paymentInstrument")]);
    m_payment_instrument_isSet = !json[QString("paymentInstrument")].isNull() && m_payment_instrument_isValid;

    m_plan_ids_isValid = ::OpenAPI::fromJsonValue(m_plan_ids, json[QString("planIds")]);
    m_plan_ids_isSet = !json[QString("planIds")].isNull() && m_plan_ids_isValid;

    m_processed_time_isValid = ::OpenAPI::fromJsonValue(m_processed_time, json[QString("processedTime")]);
    m_processed_time_isSet = !json[QString("processedTime")].isNull() && m_processed_time_isValid;

    m_purchase_amount_isValid = ::OpenAPI::fromJsonValue(m_purchase_amount, json[QString("purchaseAmount")]);
    m_purchase_amount_isSet = !json[QString("purchaseAmount")].isNull() && m_purchase_amount_isValid;

    m_purchase_currency_isValid = ::OpenAPI::fromJsonValue(m_purchase_currency, json[QString("purchaseCurrency")]);
    m_purchase_currency_isSet = !json[QString("purchaseCurrency")].isNull() && m_purchase_currency_isValid;

    m_rebill_number_isValid = ::OpenAPI::fromJsonValue(m_rebill_number, json[QString("rebillNumber")]);
    m_rebill_number_isSet = !json[QString("rebillNumber")].isNull() && m_rebill_number_isValid;

    m_redirect_url_isValid = ::OpenAPI::fromJsonValue(m_redirect_url, json[QString("redirectUrl")]);
    m_redirect_url_isSet = !json[QString("redirectUrl")].isNull() && m_redirect_url_isValid;

    m_request_amount_isValid = ::OpenAPI::fromJsonValue(m_request_amount, json[QString("requestAmount")]);
    m_request_amount_isSet = !json[QString("requestAmount")].isNull() && m_request_amount_isValid;

    m_request_currency_isValid = ::OpenAPI::fromJsonValue(m_request_currency, json[QString("requestCurrency")]);
    m_request_currency_isSet = !json[QString("requestCurrency")].isNull() && m_request_currency_isValid;

    m_request_id_isValid = ::OpenAPI::fromJsonValue(m_request_id, json[QString("requestId")]);
    m_request_id_isSet = !json[QString("requestId")].isNull() && m_request_id_isValid;

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;

    m_retry_number_isValid = ::OpenAPI::fromJsonValue(m_retry_number, json[QString("retryNumber")]);
    m_retry_number_isSet = !json[QString("retryNumber")].isNull() && m_retry_number_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subscription_ids_isValid = ::OpenAPI::fromJsonValue(m_subscription_ids, json[QString("subscriptionIds")]);
    m_subscription_ids_isSet = !json[QString("subscriptionIds")].isNull() && m_subscription_ids_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updatedTime")]);
    m_updated_time_isSet = !json[QString("updatedTime")].isNull() && m_updated_time_isValid;

    m_website_id_isValid = ::OpenAPI::fromJsonValue(m_website_id, json[QString("websiteId")]);
    m_website_id_isSet = !json[QString("websiteId")].isNull() && m_website_id_isValid;

    m__embedded_isValid = ::OpenAPI::fromJsonValue(m__embedded, json[QString("_embedded")]);
    m__embedded_isSet = !json[QString("_embedded")].isNull() && m__embedded_isValid;

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_acquirer_name_isValid = ::OpenAPI::fromJsonValue(m_acquirer_name, json[QString("acquirerName")]);
    m_acquirer_name_isSet = !json[QString("acquirerName")].isNull() && m_acquirer_name_isValid;

    m_arn_isValid = ::OpenAPI::fromJsonValue(m_arn, json[QString("arn")]);
    m_arn_isSet = !json[QString("arn")].isNull() && m_arn_isValid;

    m_bin_isValid = ::OpenAPI::fromJsonValue(m_bin, json[QString("bin")]);
    m_bin_isSet = !json[QString("bin")].isNull() && m_bin_isValid;

    m_bump_offer_isValid = ::OpenAPI::fromJsonValue(m_bump_offer, json[QString("bumpOffer")]);
    m_bump_offer_isSet = !json[QString("bumpOffer")].isNull() && m_bump_offer_isValid;

    m_dcc_isValid = ::OpenAPI::fromJsonValue(m_dcc, json[QString("dcc")]);
    m_dcc_isSet = !json[QString("dcc")].isNull() && m_dcc_isValid;

    m_discrepancy_time_isValid = ::OpenAPI::fromJsonValue(m_discrepancy_time, json[QString("discrepancyTime")]);
    m_discrepancy_time_isSet = !json[QString("discrepancyTime")].isNull() && m_discrepancy_time_isValid;

    m_dispute_status_isValid = ::OpenAPI::fromJsonValue(m_dispute_status, json[QString("disputeStatus")]);
    m_dispute_status_isSet = !json[QString("disputeStatus")].isNull() && m_dispute_status_isValid;

    m_dispute_time_isValid = ::OpenAPI::fromJsonValue(m_dispute_time, json[QString("disputeTime")]);
    m_dispute_time_isSet = !json[QString("disputeTime")].isNull() && m_dispute_time_isValid;

    m_gateway_isValid = ::OpenAPI::fromJsonValue(m_gateway, json[QString("gateway")]);
    m_gateway_isSet = !json[QString("gateway")].isNull() && m_gateway_isValid;

    m_gateway_account_id_isValid = ::OpenAPI::fromJsonValue(m_gateway_account_id, json[QString("gatewayAccountId")]);
    m_gateway_account_id_isSet = !json[QString("gatewayAccountId")].isNull() && m_gateway_account_id_isValid;

    m_gateway_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_gateway_transaction_id, json[QString("gatewayTransactionId")]);
    m_gateway_transaction_id_isSet = !json[QString("gatewayTransactionId")].isNull() && m_gateway_transaction_id_isValid;

    m_had_discrepancy_isValid = ::OpenAPI::fromJsonValue(m_had_discrepancy, json[QString("hadDiscrepancy")]);
    m_had_discrepancy_isSet = !json[QString("hadDiscrepancy")].isNull() && m_had_discrepancy_isValid;

    m_has_bump_offer_isValid = ::OpenAPI::fromJsonValue(m_has_bump_offer, json[QString("hasBumpOffer")]);
    m_has_bump_offer_isSet = !json[QString("hasBumpOffer")].isNull() && m_has_bump_offer_isValid;

    m_has_dcc_isValid = ::OpenAPI::fromJsonValue(m_has_dcc, json[QString("hasDcc")]);
    m_has_dcc_isSet = !json[QString("hasDcc")].isNull() && m_has_dcc_isValid;

    m_is_disputed_isValid = ::OpenAPI::fromJsonValue(m_is_disputed, json[QString("isDisputed")]);
    m_is_disputed_isSet = !json[QString("isDisputed")].isNull() && m_is_disputed_isValid;

    m_is_merchant_initiated_isValid = ::OpenAPI::fromJsonValue(m_is_merchant_initiated, json[QString("isMerchantInitiated")]);
    m_is_merchant_initiated_isSet = !json[QString("isMerchantInitiated")].isNull() && m_is_merchant_initiated_isValid;

    m_is_processed_outside_isValid = ::OpenAPI::fromJsonValue(m_is_processed_outside, json[QString("isProcessedOutside")]);
    m_is_processed_outside_isSet = !json[QString("isProcessedOutside")].isNull() && m_is_processed_outside_isValid;

    m_is_reconciled_isValid = ::OpenAPI::fromJsonValue(m_is_reconciled, json[QString("isReconciled")]);
    m_is_reconciled_isSet = !json[QString("isReconciled")].isNull() && m_is_reconciled_isValid;

    m_method_isValid = ::OpenAPI::fromJsonValue(m_method, json[QString("method")]);
    m_method_isSet = !json[QString("method")].isNull() && m_method_isValid;

    m_notification_url_isValid = ::OpenAPI::fromJsonValue(m_notification_url, json[QString("notificationUrl")]);
    m_notification_url_isSet = !json[QString("notificationUrl")].isNull() && m_notification_url_isValid;

    m_order_id_isValid = ::OpenAPI::fromJsonValue(m_order_id, json[QString("orderId")]);
    m_order_id_isSet = !json[QString("orderId")].isNull() && m_order_id_isValid;

    m_reference_data_isValid = ::OpenAPI::fromJsonValue(m_reference_data, json[QString("referenceData")]);
    m_reference_data_isSet = !json[QString("referenceData")].isNull() && m_reference_data_isValid;

    m_report_amount_isValid = ::OpenAPI::fromJsonValue(m_report_amount, json[QString("reportAmount")]);
    m_report_amount_isSet = !json[QString("reportAmount")].isNull() && m_report_amount_isValid;

    m_report_currency_isValid = ::OpenAPI::fromJsonValue(m_report_currency, json[QString("reportCurrency")]);
    m_report_currency_isSet = !json[QString("reportCurrency")].isNull() && m_report_currency_isValid;

    m_retried_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_retried_transaction_id, json[QString("retriedTransactionId")]);
    m_retried_transaction_id_isSet = !json[QString("retriedTransactionId")].isNull() && m_retried_transaction_id_isValid;

    m_retries_result_isValid = ::OpenAPI::fromJsonValue(m_retries_result, json[QString("retriesResult")]);
    m_retries_result_isSet = !json[QString("retriesResult")].isNull() && m_retries_result_isValid;

    m_retry_instruction_isValid = ::OpenAPI::fromJsonValue(m_retry_instruction, json[QString("retryInstruction")]);
    m_retry_instruction_isSet = !json[QString("retryInstruction")].isNull() && m_retry_instruction_isValid;

    m_revision_isValid = ::OpenAPI::fromJsonValue(m_revision, json[QString("revision")]);
    m_revision_isSet = !json[QString("revision")].isNull() && m_revision_isValid;

    m_risk_metadata_isValid = ::OpenAPI::fromJsonValue(m_risk_metadata, json[QString("riskMetadata")]);
    m_risk_metadata_isSet = !json[QString("riskMetadata")].isNull() && m_risk_metadata_isValid;

    m_risk_score_isValid = ::OpenAPI::fromJsonValue(m_risk_score, json[QString("riskScore")]);
    m_risk_score_isSet = !json[QString("riskScore")].isNull() && m_risk_score_isValid;

    m_scheduled_time_isValid = ::OpenAPI::fromJsonValue(m_scheduled_time, json[QString("scheduledTime")]);
    m_scheduled_time_isSet = !json[QString("scheduledTime")].isNull() && m_scheduled_time_isValid;

    m_settlement_time_isValid = ::OpenAPI::fromJsonValue(m_settlement_time, json[QString("settlementTime")]);
    m_settlement_time_isSet = !json[QString("settlementTime")].isNull() && m_settlement_time_isValid;

    m_velocity_isValid = ::OpenAPI::fromJsonValue(m_velocity, json[QString("velocity")]);
    m_velocity_isSet = !json[QString("velocity")].isNull() && m_velocity_isValid;
}

QString OAITransaction::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransaction::asJsonObject() const {
    QJsonObject obj;
    if (m_r_3ds.isSet()) {
        obj.insert(QString("3ds"), ::OpenAPI::toJsonValue(m_r_3ds));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billingAddress"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_billing_descriptor_isSet) {
        obj.insert(QString("billingDescriptor"), ::OpenAPI::toJsonValue(m_billing_descriptor));
    }
    if (m_child_transactions.size() > 0) {
        obj.insert(QString("childTransactions"), ::OpenAPI::toJsonValue(m_child_transactions));
    }
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
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
    if (m_gateway_name.isSet()) {
        obj.insert(QString("gatewayName"), ::OpenAPI::toJsonValue(m_gateway_name));
    }
    if (m_has3ds_isSet) {
        obj.insert(QString("has3ds"), ::OpenAPI::toJsonValue(m_has3ds));
    }
    if (m_has_amount_adjustment_isSet) {
        obj.insert(QString("hasAmountAdjustment"), ::OpenAPI::toJsonValue(m_has_amount_adjustment));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_ids.size() > 0) {
        obj.insert(QString("invoiceIds"), ::OpenAPI::toJsonValue(m_invoice_ids));
    }
    if (m_is_rebill_isSet) {
        obj.insert(QString("isRebill"), ::OpenAPI::toJsonValue(m_is_rebill));
    }
    if (m_is_retry_isSet) {
        obj.insert(QString("isRetry"), ::OpenAPI::toJsonValue(m_is_retry));
    }
    if (m_parent_transaction_id_isSet) {
        obj.insert(QString("parentTransactionId"), ::OpenAPI::toJsonValue(m_parent_transaction_id));
    }
    if (m_payment_instrument.isSet()) {
        obj.insert(QString("paymentInstrument"), ::OpenAPI::toJsonValue(m_payment_instrument));
    }
    if (m_plan_ids.size() > 0) {
        obj.insert(QString("planIds"), ::OpenAPI::toJsonValue(m_plan_ids));
    }
    if (m_processed_time_isSet) {
        obj.insert(QString("processedTime"), ::OpenAPI::toJsonValue(m_processed_time));
    }
    if (m_purchase_amount_isSet) {
        obj.insert(QString("purchaseAmount"), ::OpenAPI::toJsonValue(m_purchase_amount));
    }
    if (m_purchase_currency_isSet) {
        obj.insert(QString("purchaseCurrency"), ::OpenAPI::toJsonValue(m_purchase_currency));
    }
    if (m_rebill_number_isSet) {
        obj.insert(QString("rebillNumber"), ::OpenAPI::toJsonValue(m_rebill_number));
    }
    if (m_redirect_url_isSet) {
        obj.insert(QString("redirectUrl"), ::OpenAPI::toJsonValue(m_redirect_url));
    }
    if (m_request_amount_isSet) {
        obj.insert(QString("requestAmount"), ::OpenAPI::toJsonValue(m_request_amount));
    }
    if (m_request_currency_isSet) {
        obj.insert(QString("requestCurrency"), ::OpenAPI::toJsonValue(m_request_currency));
    }
    if (m_request_id_isSet) {
        obj.insert(QString("requestId"), ::OpenAPI::toJsonValue(m_request_id));
    }
    if (m_result_isSet) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    if (m_retry_number_isSet) {
        obj.insert(QString("retryNumber"), ::OpenAPI::toJsonValue(m_retry_number));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subscription_ids.size() > 0) {
        obj.insert(QString("subscriptionIds"), ::OpenAPI::toJsonValue(m_subscription_ids));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updatedTime"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_website_id_isSet) {
        obj.insert(QString("websiteId"), ::OpenAPI::toJsonValue(m_website_id));
    }
    if (m__embedded.size() > 0) {
        obj.insert(QString("_embedded"), ::OpenAPI::toJsonValue(m__embedded));
    }
    if (m__links.size() > 0) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_acquirer_name.isSet()) {
        obj.insert(QString("acquirerName"), ::OpenAPI::toJsonValue(m_acquirer_name));
    }
    if (m_arn_isSet) {
        obj.insert(QString("arn"), ::OpenAPI::toJsonValue(m_arn));
    }
    if (m_bin_isSet) {
        obj.insert(QString("bin"), ::OpenAPI::toJsonValue(m_bin));
    }
    if (m_bump_offer.isSet()) {
        obj.insert(QString("bumpOffer"), ::OpenAPI::toJsonValue(m_bump_offer));
    }
    if (m_dcc.isSet()) {
        obj.insert(QString("dcc"), ::OpenAPI::toJsonValue(m_dcc));
    }
    if (m_discrepancy_time_isSet) {
        obj.insert(QString("discrepancyTime"), ::OpenAPI::toJsonValue(m_discrepancy_time));
    }
    if (m_dispute_status_isSet) {
        obj.insert(QString("disputeStatus"), ::OpenAPI::toJsonValue(m_dispute_status));
    }
    if (m_dispute_time_isSet) {
        obj.insert(QString("disputeTime"), ::OpenAPI::toJsonValue(m_dispute_time));
    }
    if (m_gateway.isSet()) {
        obj.insert(QString("gateway"), ::OpenAPI::toJsonValue(m_gateway));
    }
    if (m_gateway_account_id_isSet) {
        obj.insert(QString("gatewayAccountId"), ::OpenAPI::toJsonValue(m_gateway_account_id));
    }
    if (m_gateway_transaction_id_isSet) {
        obj.insert(QString("gatewayTransactionId"), ::OpenAPI::toJsonValue(m_gateway_transaction_id));
    }
    if (m_had_discrepancy_isSet) {
        obj.insert(QString("hadDiscrepancy"), ::OpenAPI::toJsonValue(m_had_discrepancy));
    }
    if (m_has_bump_offer_isSet) {
        obj.insert(QString("hasBumpOffer"), ::OpenAPI::toJsonValue(m_has_bump_offer));
    }
    if (m_has_dcc_isSet) {
        obj.insert(QString("hasDcc"), ::OpenAPI::toJsonValue(m_has_dcc));
    }
    if (m_is_disputed_isSet) {
        obj.insert(QString("isDisputed"), ::OpenAPI::toJsonValue(m_is_disputed));
    }
    if (m_is_merchant_initiated_isSet) {
        obj.insert(QString("isMerchantInitiated"), ::OpenAPI::toJsonValue(m_is_merchant_initiated));
    }
    if (m_is_processed_outside_isSet) {
        obj.insert(QString("isProcessedOutside"), ::OpenAPI::toJsonValue(m_is_processed_outside));
    }
    if (m_is_reconciled_isSet) {
        obj.insert(QString("isReconciled"), ::OpenAPI::toJsonValue(m_is_reconciled));
    }
    if (m_method.isSet()) {
        obj.insert(QString("method"), ::OpenAPI::toJsonValue(m_method));
    }
    if (m_notification_url_isSet) {
        obj.insert(QString("notificationUrl"), ::OpenAPI::toJsonValue(m_notification_url));
    }
    if (m_order_id_isSet) {
        obj.insert(QString("orderId"), ::OpenAPI::toJsonValue(m_order_id));
    }
    if (m_reference_data.size() > 0) {
        obj.insert(QString("referenceData"), ::OpenAPI::toJsonValue(m_reference_data));
    }
    if (m_report_amount_isSet) {
        obj.insert(QString("reportAmount"), ::OpenAPI::toJsonValue(m_report_amount));
    }
    if (m_report_currency_isSet) {
        obj.insert(QString("reportCurrency"), ::OpenAPI::toJsonValue(m_report_currency));
    }
    if (m_retried_transaction_id_isSet) {
        obj.insert(QString("retriedTransactionId"), ::OpenAPI::toJsonValue(m_retried_transaction_id));
    }
    if (m_retries_result_isSet) {
        obj.insert(QString("retriesResult"), ::OpenAPI::toJsonValue(m_retries_result));
    }
    if (m_retry_instruction.isSet()) {
        obj.insert(QString("retryInstruction"), ::OpenAPI::toJsonValue(m_retry_instruction));
    }
    if (m_revision_isSet) {
        obj.insert(QString("revision"), ::OpenAPI::toJsonValue(m_revision));
    }
    if (m_risk_metadata.isSet()) {
        obj.insert(QString("riskMetadata"), ::OpenAPI::toJsonValue(m_risk_metadata));
    }
    if (m_risk_score_isSet) {
        obj.insert(QString("riskScore"), ::OpenAPI::toJsonValue(m_risk_score));
    }
    if (m_scheduled_time_isSet) {
        obj.insert(QString("scheduledTime"), ::OpenAPI::toJsonValue(m_scheduled_time));
    }
    if (m_settlement_time_isSet) {
        obj.insert(QString("settlementTime"), ::OpenAPI::toJsonValue(m_settlement_time));
    }
    if (m_velocity_isSet) {
        obj.insert(QString("velocity"), ::OpenAPI::toJsonValue(m_velocity));
    }
    return obj;
}

OAIThreeDSecureResult OAITransaction::getR3ds() const {
    return m_r_3ds;
}
void OAITransaction::setR3ds(const OAIThreeDSecureResult &r_3ds) {
    m_r_3ds = r_3ds;
    m_r_3ds_isSet = true;
}

bool OAITransaction::is_r_3ds_Set() const{
    return m_r_3ds_isSet;
}

bool OAITransaction::is_r_3ds_Valid() const{
    return m_r_3ds_isValid;
}

double OAITransaction::getAmount() const {
    return m_amount;
}
void OAITransaction::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAITransaction::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAITransaction::is_amount_Valid() const{
    return m_amount_isValid;
}

OAIContactObject OAITransaction::getBillingAddress() const {
    return m_billing_address;
}
void OAITransaction::setBillingAddress(const OAIContactObject &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAITransaction::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAITransaction::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAITransaction::getBillingDescriptor() const {
    return m_billing_descriptor;
}
void OAITransaction::setBillingDescriptor(const QString &billing_descriptor) {
    m_billing_descriptor = billing_descriptor;
    m_billing_descriptor_isSet = true;
}

bool OAITransaction::is_billing_descriptor_Set() const{
    return m_billing_descriptor_isSet;
}

bool OAITransaction::is_billing_descriptor_Valid() const{
    return m_billing_descriptor_isValid;
}

QList<QString> OAITransaction::getChildTransactions() const {
    return m_child_transactions;
}
void OAITransaction::setChildTransactions(const QList<QString> &child_transactions) {
    m_child_transactions = child_transactions;
    m_child_transactions_isSet = true;
}

bool OAITransaction::is_child_transactions_Set() const{
    return m_child_transactions_isSet;
}

bool OAITransaction::is_child_transactions_Valid() const{
    return m_child_transactions_isValid;
}

QDateTime OAITransaction::getCreatedTime() const {
    return m_created_time;
}
void OAITransaction::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAITransaction::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAITransaction::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QString OAITransaction::getCurrency() const {
    return m_currency;
}
void OAITransaction::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAITransaction::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAITransaction::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAITransaction::getCustomFields() const {
    return m_custom_fields;
}
void OAITransaction::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAITransaction::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAITransaction::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAITransaction::getCustomerId() const {
    return m_customer_id;
}
void OAITransaction::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAITransaction::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAITransaction::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAITransaction::getDescription() const {
    return m_description;
}
void OAITransaction::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAITransaction::is_description_Set() const{
    return m_description_isSet;
}

bool OAITransaction::is_description_Valid() const{
    return m_description_isValid;
}

OAIGatewayName OAITransaction::getGatewayName() const {
    return m_gateway_name;
}
void OAITransaction::setGatewayName(const OAIGatewayName &gateway_name) {
    m_gateway_name = gateway_name;
    m_gateway_name_isSet = true;
}

bool OAITransaction::is_gateway_name_Set() const{
    return m_gateway_name_isSet;
}

bool OAITransaction::is_gateway_name_Valid() const{
    return m_gateway_name_isValid;
}

bool OAITransaction::isHas3ds() const {
    return m_has3ds;
}
void OAITransaction::setHas3ds(const bool &has3ds) {
    m_has3ds = has3ds;
    m_has3ds_isSet = true;
}

bool OAITransaction::is_has3ds_Set() const{
    return m_has3ds_isSet;
}

bool OAITransaction::is_has3ds_Valid() const{
    return m_has3ds_isValid;
}

bool OAITransaction::isHasAmountAdjustment() const {
    return m_has_amount_adjustment;
}
void OAITransaction::setHasAmountAdjustment(const bool &has_amount_adjustment) {
    m_has_amount_adjustment = has_amount_adjustment;
    m_has_amount_adjustment_isSet = true;
}

bool OAITransaction::is_has_amount_adjustment_Set() const{
    return m_has_amount_adjustment_isSet;
}

bool OAITransaction::is_has_amount_adjustment_Valid() const{
    return m_has_amount_adjustment_isValid;
}

QString OAITransaction::getId() const {
    return m_id;
}
void OAITransaction::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITransaction::is_id_Set() const{
    return m_id_isSet;
}

bool OAITransaction::is_id_Valid() const{
    return m_id_isValid;
}

QList<QString> OAITransaction::getInvoiceIds() const {
    return m_invoice_ids;
}
void OAITransaction::setInvoiceIds(const QList<QString> &invoice_ids) {
    m_invoice_ids = invoice_ids;
    m_invoice_ids_isSet = true;
}

bool OAITransaction::is_invoice_ids_Set() const{
    return m_invoice_ids_isSet;
}

bool OAITransaction::is_invoice_ids_Valid() const{
    return m_invoice_ids_isValid;
}

bool OAITransaction::isIsRebill() const {
    return m_is_rebill;
}
void OAITransaction::setIsRebill(const bool &is_rebill) {
    m_is_rebill = is_rebill;
    m_is_rebill_isSet = true;
}

bool OAITransaction::is_is_rebill_Set() const{
    return m_is_rebill_isSet;
}

bool OAITransaction::is_is_rebill_Valid() const{
    return m_is_rebill_isValid;
}

bool OAITransaction::isIsRetry() const {
    return m_is_retry;
}
void OAITransaction::setIsRetry(const bool &is_retry) {
    m_is_retry = is_retry;
    m_is_retry_isSet = true;
}

bool OAITransaction::is_is_retry_Set() const{
    return m_is_retry_isSet;
}

bool OAITransaction::is_is_retry_Valid() const{
    return m_is_retry_isValid;
}

QString OAITransaction::getParentTransactionId() const {
    return m_parent_transaction_id;
}
void OAITransaction::setParentTransactionId(const QString &parent_transaction_id) {
    m_parent_transaction_id = parent_transaction_id;
    m_parent_transaction_id_isSet = true;
}

bool OAITransaction::is_parent_transaction_id_Set() const{
    return m_parent_transaction_id_isSet;
}

bool OAITransaction::is_parent_transaction_id_Valid() const{
    return m_parent_transaction_id_isValid;
}

OAIPaymentInstrument OAITransaction::getPaymentInstrument() const {
    return m_payment_instrument;
}
void OAITransaction::setPaymentInstrument(const OAIPaymentInstrument &payment_instrument) {
    m_payment_instrument = payment_instrument;
    m_payment_instrument_isSet = true;
}

bool OAITransaction::is_payment_instrument_Set() const{
    return m_payment_instrument_isSet;
}

bool OAITransaction::is_payment_instrument_Valid() const{
    return m_payment_instrument_isValid;
}

QList<QString> OAITransaction::getPlanIds() const {
    return m_plan_ids;
}
void OAITransaction::setPlanIds(const QList<QString> &plan_ids) {
    m_plan_ids = plan_ids;
    m_plan_ids_isSet = true;
}

bool OAITransaction::is_plan_ids_Set() const{
    return m_plan_ids_isSet;
}

bool OAITransaction::is_plan_ids_Valid() const{
    return m_plan_ids_isValid;
}

QDateTime OAITransaction::getProcessedTime() const {
    return m_processed_time;
}
void OAITransaction::setProcessedTime(const QDateTime &processed_time) {
    m_processed_time = processed_time;
    m_processed_time_isSet = true;
}

bool OAITransaction::is_processed_time_Set() const{
    return m_processed_time_isSet;
}

bool OAITransaction::is_processed_time_Valid() const{
    return m_processed_time_isValid;
}

double OAITransaction::getPurchaseAmount() const {
    return m_purchase_amount;
}
void OAITransaction::setPurchaseAmount(const double &purchase_amount) {
    m_purchase_amount = purchase_amount;
    m_purchase_amount_isSet = true;
}

bool OAITransaction::is_purchase_amount_Set() const{
    return m_purchase_amount_isSet;
}

bool OAITransaction::is_purchase_amount_Valid() const{
    return m_purchase_amount_isValid;
}

QString OAITransaction::getPurchaseCurrency() const {
    return m_purchase_currency;
}
void OAITransaction::setPurchaseCurrency(const QString &purchase_currency) {
    m_purchase_currency = purchase_currency;
    m_purchase_currency_isSet = true;
}

bool OAITransaction::is_purchase_currency_Set() const{
    return m_purchase_currency_isSet;
}

bool OAITransaction::is_purchase_currency_Valid() const{
    return m_purchase_currency_isValid;
}

qint32 OAITransaction::getRebillNumber() const {
    return m_rebill_number;
}
void OAITransaction::setRebillNumber(const qint32 &rebill_number) {
    m_rebill_number = rebill_number;
    m_rebill_number_isSet = true;
}

bool OAITransaction::is_rebill_number_Set() const{
    return m_rebill_number_isSet;
}

bool OAITransaction::is_rebill_number_Valid() const{
    return m_rebill_number_isValid;
}

QString OAITransaction::getRedirectUrl() const {
    return m_redirect_url;
}
void OAITransaction::setRedirectUrl(const QString &redirect_url) {
    m_redirect_url = redirect_url;
    m_redirect_url_isSet = true;
}

bool OAITransaction::is_redirect_url_Set() const{
    return m_redirect_url_isSet;
}

bool OAITransaction::is_redirect_url_Valid() const{
    return m_redirect_url_isValid;
}

double OAITransaction::getRequestAmount() const {
    return m_request_amount;
}
void OAITransaction::setRequestAmount(const double &request_amount) {
    m_request_amount = request_amount;
    m_request_amount_isSet = true;
}

bool OAITransaction::is_request_amount_Set() const{
    return m_request_amount_isSet;
}

bool OAITransaction::is_request_amount_Valid() const{
    return m_request_amount_isValid;
}

QString OAITransaction::getRequestCurrency() const {
    return m_request_currency;
}
void OAITransaction::setRequestCurrency(const QString &request_currency) {
    m_request_currency = request_currency;
    m_request_currency_isSet = true;
}

bool OAITransaction::is_request_currency_Set() const{
    return m_request_currency_isSet;
}

bool OAITransaction::is_request_currency_Valid() const{
    return m_request_currency_isValid;
}

QString OAITransaction::getRequestId() const {
    return m_request_id;
}
void OAITransaction::setRequestId(const QString &request_id) {
    m_request_id = request_id;
    m_request_id_isSet = true;
}

bool OAITransaction::is_request_id_Set() const{
    return m_request_id_isSet;
}

bool OAITransaction::is_request_id_Valid() const{
    return m_request_id_isValid;
}

QString OAITransaction::getResult() const {
    return m_result;
}
void OAITransaction::setResult(const QString &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAITransaction::is_result_Set() const{
    return m_result_isSet;
}

bool OAITransaction::is_result_Valid() const{
    return m_result_isValid;
}

qint32 OAITransaction::getRetryNumber() const {
    return m_retry_number;
}
void OAITransaction::setRetryNumber(const qint32 &retry_number) {
    m_retry_number = retry_number;
    m_retry_number_isSet = true;
}

bool OAITransaction::is_retry_number_Set() const{
    return m_retry_number_isSet;
}

bool OAITransaction::is_retry_number_Valid() const{
    return m_retry_number_isValid;
}

QString OAITransaction::getStatus() const {
    return m_status;
}
void OAITransaction::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAITransaction::is_status_Set() const{
    return m_status_isSet;
}

bool OAITransaction::is_status_Valid() const{
    return m_status_isValid;
}

QList<QString> OAITransaction::getSubscriptionIds() const {
    return m_subscription_ids;
}
void OAITransaction::setSubscriptionIds(const QList<QString> &subscription_ids) {
    m_subscription_ids = subscription_ids;
    m_subscription_ids_isSet = true;
}

bool OAITransaction::is_subscription_ids_Set() const{
    return m_subscription_ids_isSet;
}

bool OAITransaction::is_subscription_ids_Valid() const{
    return m_subscription_ids_isValid;
}

QString OAITransaction::getType() const {
    return m_type;
}
void OAITransaction::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITransaction::is_type_Set() const{
    return m_type_isSet;
}

bool OAITransaction::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAITransaction::getUpdatedTime() const {
    return m_updated_time;
}
void OAITransaction::setUpdatedTime(const QDateTime &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAITransaction::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAITransaction::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

QString OAITransaction::getWebsiteId() const {
    return m_website_id;
}
void OAITransaction::setWebsiteId(const QString &website_id) {
    m_website_id = website_id;
    m_website_id_isSet = true;
}

bool OAITransaction::is_website_id_Set() const{
    return m_website_id_isSet;
}

bool OAITransaction::is_website_id_Valid() const{
    return m_website_id_isValid;
}

QList<OAITransaction_allOf__embedded> OAITransaction::getEmbedded() const {
    return m__embedded;
}
void OAITransaction::setEmbedded(const QList<OAITransaction_allOf__embedded> &_embedded) {
    m__embedded = _embedded;
    m__embedded_isSet = true;
}

bool OAITransaction::is__embedded_Set() const{
    return m__embedded_isSet;
}

bool OAITransaction::is__embedded_Valid() const{
    return m__embedded_isValid;
}

QList<OAITransaction_allOf__links> OAITransaction::getLinks() const {
    return m__links;
}
void OAITransaction::setLinks(const QList<OAITransaction_allOf__links> &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAITransaction::is__links_Set() const{
    return m__links_isSet;
}

bool OAITransaction::is__links_Valid() const{
    return m__links_isValid;
}

OAIAcquirerName OAITransaction::getAcquirerName() const {
    return m_acquirer_name;
}
void OAITransaction::setAcquirerName(const OAIAcquirerName &acquirer_name) {
    m_acquirer_name = acquirer_name;
    m_acquirer_name_isSet = true;
}

bool OAITransaction::is_acquirer_name_Set() const{
    return m_acquirer_name_isSet;
}

bool OAITransaction::is_acquirer_name_Valid() const{
    return m_acquirer_name_isValid;
}

QString OAITransaction::getArn() const {
    return m_arn;
}
void OAITransaction::setArn(const QString &arn) {
    m_arn = arn;
    m_arn_isSet = true;
}

bool OAITransaction::is_arn_Set() const{
    return m_arn_isSet;
}

bool OAITransaction::is_arn_Valid() const{
    return m_arn_isValid;
}

QString OAITransaction::getBin() const {
    return m_bin;
}
void OAITransaction::setBin(const QString &bin) {
    m_bin = bin;
    m_bin_isSet = true;
}

bool OAITransaction::is_bin_Set() const{
    return m_bin_isSet;
}

bool OAITransaction::is_bin_Valid() const{
    return m_bin_isValid;
}

OAITransaction_allOf_bumpOffer OAITransaction::getBumpOffer() const {
    return m_bump_offer;
}
void OAITransaction::setBumpOffer(const OAITransaction_allOf_bumpOffer &bump_offer) {
    m_bump_offer = bump_offer;
    m_bump_offer_isSet = true;
}

bool OAITransaction::is_bump_offer_Set() const{
    return m_bump_offer_isSet;
}

bool OAITransaction::is_bump_offer_Valid() const{
    return m_bump_offer_isValid;
}

OAITransaction_allOf_dcc OAITransaction::getDcc() const {
    return m_dcc;
}
void OAITransaction::setDcc(const OAITransaction_allOf_dcc &dcc) {
    m_dcc = dcc;
    m_dcc_isSet = true;
}

bool OAITransaction::is_dcc_Set() const{
    return m_dcc_isSet;
}

bool OAITransaction::is_dcc_Valid() const{
    return m_dcc_isValid;
}

QDateTime OAITransaction::getDiscrepancyTime() const {
    return m_discrepancy_time;
}
void OAITransaction::setDiscrepancyTime(const QDateTime &discrepancy_time) {
    m_discrepancy_time = discrepancy_time;
    m_discrepancy_time_isSet = true;
}

bool OAITransaction::is_discrepancy_time_Set() const{
    return m_discrepancy_time_isSet;
}

bool OAITransaction::is_discrepancy_time_Valid() const{
    return m_discrepancy_time_isValid;
}

QString OAITransaction::getDisputeStatus() const {
    return m_dispute_status;
}
void OAITransaction::setDisputeStatus(const QString &dispute_status) {
    m_dispute_status = dispute_status;
    m_dispute_status_isSet = true;
}

bool OAITransaction::is_dispute_status_Set() const{
    return m_dispute_status_isSet;
}

bool OAITransaction::is_dispute_status_Valid() const{
    return m_dispute_status_isValid;
}

QDateTime OAITransaction::getDisputeTime() const {
    return m_dispute_time;
}
void OAITransaction::setDisputeTime(const QDateTime &dispute_time) {
    m_dispute_time = dispute_time;
    m_dispute_time_isSet = true;
}

bool OAITransaction::is_dispute_time_Set() const{
    return m_dispute_time_isSet;
}

bool OAITransaction::is_dispute_time_Valid() const{
    return m_dispute_time_isValid;
}

OAITransaction_allOf_gateway OAITransaction::getGateway() const {
    return m_gateway;
}
void OAITransaction::setGateway(const OAITransaction_allOf_gateway &gateway) {
    m_gateway = gateway;
    m_gateway_isSet = true;
}

bool OAITransaction::is_gateway_Set() const{
    return m_gateway_isSet;
}

bool OAITransaction::is_gateway_Valid() const{
    return m_gateway_isValid;
}

QString OAITransaction::getGatewayAccountId() const {
    return m_gateway_account_id;
}
void OAITransaction::setGatewayAccountId(const QString &gateway_account_id) {
    m_gateway_account_id = gateway_account_id;
    m_gateway_account_id_isSet = true;
}

bool OAITransaction::is_gateway_account_id_Set() const{
    return m_gateway_account_id_isSet;
}

bool OAITransaction::is_gateway_account_id_Valid() const{
    return m_gateway_account_id_isValid;
}

QString OAITransaction::getGatewayTransactionId() const {
    return m_gateway_transaction_id;
}
void OAITransaction::setGatewayTransactionId(const QString &gateway_transaction_id) {
    m_gateway_transaction_id = gateway_transaction_id;
    m_gateway_transaction_id_isSet = true;
}

bool OAITransaction::is_gateway_transaction_id_Set() const{
    return m_gateway_transaction_id_isSet;
}

bool OAITransaction::is_gateway_transaction_id_Valid() const{
    return m_gateway_transaction_id_isValid;
}

bool OAITransaction::isHadDiscrepancy() const {
    return m_had_discrepancy;
}
void OAITransaction::setHadDiscrepancy(const bool &had_discrepancy) {
    m_had_discrepancy = had_discrepancy;
    m_had_discrepancy_isSet = true;
}

bool OAITransaction::is_had_discrepancy_Set() const{
    return m_had_discrepancy_isSet;
}

bool OAITransaction::is_had_discrepancy_Valid() const{
    return m_had_discrepancy_isValid;
}

bool OAITransaction::isHasBumpOffer() const {
    return m_has_bump_offer;
}
void OAITransaction::setHasBumpOffer(const bool &has_bump_offer) {
    m_has_bump_offer = has_bump_offer;
    m_has_bump_offer_isSet = true;
}

bool OAITransaction::is_has_bump_offer_Set() const{
    return m_has_bump_offer_isSet;
}

bool OAITransaction::is_has_bump_offer_Valid() const{
    return m_has_bump_offer_isValid;
}

bool OAITransaction::isHasDcc() const {
    return m_has_dcc;
}
void OAITransaction::setHasDcc(const bool &has_dcc) {
    m_has_dcc = has_dcc;
    m_has_dcc_isSet = true;
}

bool OAITransaction::is_has_dcc_Set() const{
    return m_has_dcc_isSet;
}

bool OAITransaction::is_has_dcc_Valid() const{
    return m_has_dcc_isValid;
}

bool OAITransaction::isIsDisputed() const {
    return m_is_disputed;
}
void OAITransaction::setIsDisputed(const bool &is_disputed) {
    m_is_disputed = is_disputed;
    m_is_disputed_isSet = true;
}

bool OAITransaction::is_is_disputed_Set() const{
    return m_is_disputed_isSet;
}

bool OAITransaction::is_is_disputed_Valid() const{
    return m_is_disputed_isValid;
}

bool OAITransaction::isIsMerchantInitiated() const {
    return m_is_merchant_initiated;
}
void OAITransaction::setIsMerchantInitiated(const bool &is_merchant_initiated) {
    m_is_merchant_initiated = is_merchant_initiated;
    m_is_merchant_initiated_isSet = true;
}

bool OAITransaction::is_is_merchant_initiated_Set() const{
    return m_is_merchant_initiated_isSet;
}

bool OAITransaction::is_is_merchant_initiated_Valid() const{
    return m_is_merchant_initiated_isValid;
}

bool OAITransaction::isIsProcessedOutside() const {
    return m_is_processed_outside;
}
void OAITransaction::setIsProcessedOutside(const bool &is_processed_outside) {
    m_is_processed_outside = is_processed_outside;
    m_is_processed_outside_isSet = true;
}

bool OAITransaction::is_is_processed_outside_Set() const{
    return m_is_processed_outside_isSet;
}

bool OAITransaction::is_is_processed_outside_Valid() const{
    return m_is_processed_outside_isValid;
}

bool OAITransaction::isIsReconciled() const {
    return m_is_reconciled;
}
void OAITransaction::setIsReconciled(const bool &is_reconciled) {
    m_is_reconciled = is_reconciled;
    m_is_reconciled_isSet = true;
}

bool OAITransaction::is_is_reconciled_Set() const{
    return m_is_reconciled_isSet;
}

bool OAITransaction::is_is_reconciled_Valid() const{
    return m_is_reconciled_isValid;
}

OAIPaymentMethod OAITransaction::getMethod() const {
    return m_method;
}
void OAITransaction::setMethod(const OAIPaymentMethod &method) {
    m_method = method;
    m_method_isSet = true;
}

bool OAITransaction::is_method_Set() const{
    return m_method_isSet;
}

bool OAITransaction::is_method_Valid() const{
    return m_method_isValid;
}

QString OAITransaction::getNotificationUrl() const {
    return m_notification_url;
}
void OAITransaction::setNotificationUrl(const QString &notification_url) {
    m_notification_url = notification_url;
    m_notification_url_isSet = true;
}

bool OAITransaction::is_notification_url_Set() const{
    return m_notification_url_isSet;
}

bool OAITransaction::is_notification_url_Valid() const{
    return m_notification_url_isValid;
}

QString OAITransaction::getOrderId() const {
    return m_order_id;
}
void OAITransaction::setOrderId(const QString &order_id) {
    m_order_id = order_id;
    m_order_id_isSet = true;
}

bool OAITransaction::is_order_id_Set() const{
    return m_order_id_isSet;
}

bool OAITransaction::is_order_id_Valid() const{
    return m_order_id_isValid;
}

QMap<QString, QString> OAITransaction::getReferenceData() const {
    return m_reference_data;
}
void OAITransaction::setReferenceData(const QMap<QString, QString> &reference_data) {
    m_reference_data = reference_data;
    m_reference_data_isSet = true;
}

bool OAITransaction::is_reference_data_Set() const{
    return m_reference_data_isSet;
}

bool OAITransaction::is_reference_data_Valid() const{
    return m_reference_data_isValid;
}

double OAITransaction::getReportAmount() const {
    return m_report_amount;
}
void OAITransaction::setReportAmount(const double &report_amount) {
    m_report_amount = report_amount;
    m_report_amount_isSet = true;
}

bool OAITransaction::is_report_amount_Set() const{
    return m_report_amount_isSet;
}

bool OAITransaction::is_report_amount_Valid() const{
    return m_report_amount_isValid;
}

QString OAITransaction::getReportCurrency() const {
    return m_report_currency;
}
void OAITransaction::setReportCurrency(const QString &report_currency) {
    m_report_currency = report_currency;
    m_report_currency_isSet = true;
}

bool OAITransaction::is_report_currency_Set() const{
    return m_report_currency_isSet;
}

bool OAITransaction::is_report_currency_Valid() const{
    return m_report_currency_isValid;
}

QString OAITransaction::getRetriedTransactionId() const {
    return m_retried_transaction_id;
}
void OAITransaction::setRetriedTransactionId(const QString &retried_transaction_id) {
    m_retried_transaction_id = retried_transaction_id;
    m_retried_transaction_id_isSet = true;
}

bool OAITransaction::is_retried_transaction_id_Set() const{
    return m_retried_transaction_id_isSet;
}

bool OAITransaction::is_retried_transaction_id_Valid() const{
    return m_retried_transaction_id_isValid;
}

QString OAITransaction::getRetriesResult() const {
    return m_retries_result;
}
void OAITransaction::setRetriesResult(const QString &retries_result) {
    m_retries_result = retries_result;
    m_retries_result_isSet = true;
}

bool OAITransaction::is_retries_result_Set() const{
    return m_retries_result_isSet;
}

bool OAITransaction::is_retries_result_Valid() const{
    return m_retries_result_isValid;
}

OAIPaymentRetry OAITransaction::getRetryInstruction() const {
    return m_retry_instruction;
}
void OAITransaction::setRetryInstruction(const OAIPaymentRetry &retry_instruction) {
    m_retry_instruction = retry_instruction;
    m_retry_instruction_isSet = true;
}

bool OAITransaction::is_retry_instruction_Set() const{
    return m_retry_instruction_isSet;
}

bool OAITransaction::is_retry_instruction_Valid() const{
    return m_retry_instruction_isValid;
}

qint32 OAITransaction::getRevision() const {
    return m_revision;
}
void OAITransaction::setRevision(const qint32 &revision) {
    m_revision = revision;
    m_revision_isSet = true;
}

bool OAITransaction::is_revision_Set() const{
    return m_revision_isSet;
}

bool OAITransaction::is_revision_Valid() const{
    return m_revision_isValid;
}

OAIRiskMetadata OAITransaction::getRiskMetadata() const {
    return m_risk_metadata;
}
void OAITransaction::setRiskMetadata(const OAIRiskMetadata &risk_metadata) {
    m_risk_metadata = risk_metadata;
    m_risk_metadata_isSet = true;
}

bool OAITransaction::is_risk_metadata_Set() const{
    return m_risk_metadata_isSet;
}

bool OAITransaction::is_risk_metadata_Valid() const{
    return m_risk_metadata_isValid;
}

qint32 OAITransaction::getRiskScore() const {
    return m_risk_score;
}
void OAITransaction::setRiskScore(const qint32 &risk_score) {
    m_risk_score = risk_score;
    m_risk_score_isSet = true;
}

bool OAITransaction::is_risk_score_Set() const{
    return m_risk_score_isSet;
}

bool OAITransaction::is_risk_score_Valid() const{
    return m_risk_score_isValid;
}

QDateTime OAITransaction::getScheduledTime() const {
    return m_scheduled_time;
}
void OAITransaction::setScheduledTime(const QDateTime &scheduled_time) {
    m_scheduled_time = scheduled_time;
    m_scheduled_time_isSet = true;
}

bool OAITransaction::is_scheduled_time_Set() const{
    return m_scheduled_time_isSet;
}

bool OAITransaction::is_scheduled_time_Valid() const{
    return m_scheduled_time_isValid;
}

QDateTime OAITransaction::getSettlementTime() const {
    return m_settlement_time;
}
void OAITransaction::setSettlementTime(const QDateTime &settlement_time) {
    m_settlement_time = settlement_time;
    m_settlement_time_isSet = true;
}

bool OAITransaction::is_settlement_time_Set() const{
    return m_settlement_time_isSet;
}

bool OAITransaction::is_settlement_time_Valid() const{
    return m_settlement_time_isValid;
}

qint32 OAITransaction::getVelocity() const {
    return m_velocity;
}
void OAITransaction::setVelocity(const qint32 &velocity) {
    m_velocity = velocity;
    m_velocity_isSet = true;
}

bool OAITransaction::is_velocity_Set() const{
    return m_velocity_isSet;
}

bool OAITransaction::is_velocity_Valid() const{
    return m_velocity_isValid;
}

bool OAITransaction::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_3ds.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_descriptor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_child_transactions.size() > 0) {
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

        if (m_gateway_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_has3ds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_amount_adjustment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_rebill_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_retry_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instrument.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_plan_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_processed_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rebill_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_redirect_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_ids.size() > 0) {
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

        if (m_website_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__embedded.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m__links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_acquirer_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_arn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bump_offer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dcc.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_discrepancy_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dispute_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dispute_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_had_discrepancy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_bump_offer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_dcc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_disputed_isSet) {
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

        if (m_is_reconciled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_method.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retried_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retries_result_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_instruction.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_risk_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settlement_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_velocity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransaction::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
