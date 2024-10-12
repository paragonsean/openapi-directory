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

/*
 * OAITransaction.h
 *
 * 
 */

#ifndef OAITransaction_H
#define OAITransaction_H

#include <QJsonObject>

#include "OAIAcquirerName.h"
#include "OAIContactObject.h"
#include "OAIGatewayName.h"
#include "OAIObject.h"
#include "OAIPaymentInstrument.h"
#include "OAIPaymentMethod.h"
#include "OAIPaymentRetry.h"
#include "OAIRiskMetadata.h"
#include "OAIThreeDSecureResult.h"
#include "OAITransaction_allOf__embedded.h"
#include "OAITransaction_allOf__links.h"
#include "OAITransaction_allOf_bumpOffer.h"
#include "OAITransaction_allOf_dcc.h"
#include "OAITransaction_allOf_gateway.h"
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIThreeDSecureResult;
class OAIContactObject;
class OAIPaymentInstrument;
class OAITransaction_allOf__embedded;
class OAITransaction_allOf__links;
class OAITransaction_allOf_bumpOffer;
class OAITransaction_allOf_dcc;
class OAITransaction_allOf_gateway;
class OAIPaymentRetry;
class OAIRiskMetadata;

class OAITransaction : public OAIObject {
public:
    OAITransaction();
    OAITransaction(QString json);
    ~OAITransaction() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIThreeDSecureResult getR3ds() const;
    void setR3ds(const OAIThreeDSecureResult &r_3ds);
    bool is_r_3ds_Set() const;
    bool is_r_3ds_Valid() const;

    double getAmount() const;
    void setAmount(const double &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    OAIContactObject getBillingAddress() const;
    void setBillingAddress(const OAIContactObject &billing_address);
    bool is_billing_address_Set() const;
    bool is_billing_address_Valid() const;

    QString getBillingDescriptor() const;
    void setBillingDescriptor(const QString &billing_descriptor);
    bool is_billing_descriptor_Set() const;
    bool is_billing_descriptor_Valid() const;

    QList<QString> getChildTransactions() const;
    void setChildTransactions(const QList<QString> &child_transactions);
    bool is_child_transactions_Set() const;
    bool is_child_transactions_Valid() const;

    QDateTime getCreatedTime() const;
    void setCreatedTime(const QDateTime &created_time);
    bool is_created_time_Set() const;
    bool is_created_time_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getCustomerId() const;
    void setCustomerId(const QString &customer_id);
    bool is_customer_id_Set() const;
    bool is_customer_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIGatewayName getGatewayName() const;
    void setGatewayName(const OAIGatewayName &gateway_name);
    bool is_gateway_name_Set() const;
    bool is_gateway_name_Valid() const;

    bool isHas3ds() const;
    void setHas3ds(const bool &has3ds);
    bool is_has3ds_Set() const;
    bool is_has3ds_Valid() const;

    bool isHasAmountAdjustment() const;
    void setHasAmountAdjustment(const bool &has_amount_adjustment);
    bool is_has_amount_adjustment_Set() const;
    bool is_has_amount_adjustment_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<QString> getInvoiceIds() const;
    void setInvoiceIds(const QList<QString> &invoice_ids);
    bool is_invoice_ids_Set() const;
    bool is_invoice_ids_Valid() const;

    bool isIsRebill() const;
    void setIsRebill(const bool &is_rebill);
    bool is_is_rebill_Set() const;
    bool is_is_rebill_Valid() const;

    bool isIsRetry() const;
    void setIsRetry(const bool &is_retry);
    bool is_is_retry_Set() const;
    bool is_is_retry_Valid() const;

    QString getParentTransactionId() const;
    void setParentTransactionId(const QString &parent_transaction_id);
    bool is_parent_transaction_id_Set() const;
    bool is_parent_transaction_id_Valid() const;

    OAIPaymentInstrument getPaymentInstrument() const;
    void setPaymentInstrument(const OAIPaymentInstrument &payment_instrument);
    bool is_payment_instrument_Set() const;
    bool is_payment_instrument_Valid() const;

    QList<QString> getPlanIds() const;
    void setPlanIds(const QList<QString> &plan_ids);
    bool is_plan_ids_Set() const;
    bool is_plan_ids_Valid() const;

    QDateTime getProcessedTime() const;
    void setProcessedTime(const QDateTime &processed_time);
    bool is_processed_time_Set() const;
    bool is_processed_time_Valid() const;

    double getPurchaseAmount() const;
    void setPurchaseAmount(const double &purchase_amount);
    bool is_purchase_amount_Set() const;
    bool is_purchase_amount_Valid() const;

    QString getPurchaseCurrency() const;
    void setPurchaseCurrency(const QString &purchase_currency);
    bool is_purchase_currency_Set() const;
    bool is_purchase_currency_Valid() const;

    qint32 getRebillNumber() const;
    void setRebillNumber(const qint32 &rebill_number);
    bool is_rebill_number_Set() const;
    bool is_rebill_number_Valid() const;

    QString getRedirectUrl() const;
    void setRedirectUrl(const QString &redirect_url);
    bool is_redirect_url_Set() const;
    bool is_redirect_url_Valid() const;

    double getRequestAmount() const;
    void setRequestAmount(const double &request_amount);
    bool is_request_amount_Set() const;
    bool is_request_amount_Valid() const;

    QString getRequestCurrency() const;
    void setRequestCurrency(const QString &request_currency);
    bool is_request_currency_Set() const;
    bool is_request_currency_Valid() const;

    QString getRequestId() const;
    void setRequestId(const QString &request_id);
    bool is_request_id_Set() const;
    bool is_request_id_Valid() const;

    QString getResult() const;
    void setResult(const QString &result);
    bool is_result_Set() const;
    bool is_result_Valid() const;

    qint32 getRetryNumber() const;
    void setRetryNumber(const qint32 &retry_number);
    bool is_retry_number_Set() const;
    bool is_retry_number_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<QString> getSubscriptionIds() const;
    void setSubscriptionIds(const QList<QString> &subscription_ids);
    bool is_subscription_ids_Set() const;
    bool is_subscription_ids_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QDateTime getUpdatedTime() const;
    void setUpdatedTime(const QDateTime &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    QString getWebsiteId() const;
    void setWebsiteId(const QString &website_id);
    bool is_website_id_Set() const;
    bool is_website_id_Valid() const;

    QList<OAITransaction_allOf__embedded> getEmbedded() const;
    void setEmbedded(const QList<OAITransaction_allOf__embedded> &_embedded);
    bool is__embedded_Set() const;
    bool is__embedded_Valid() const;

    QList<OAITransaction_allOf__links> getLinks() const;
    void setLinks(const QList<OAITransaction_allOf__links> &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    OAIAcquirerName getAcquirerName() const;
    void setAcquirerName(const OAIAcquirerName &acquirer_name);
    bool is_acquirer_name_Set() const;
    bool is_acquirer_name_Valid() const;

    QString getArn() const;
    void setArn(const QString &arn);
    bool is_arn_Set() const;
    bool is_arn_Valid() const;

    QString getBin() const;
    void setBin(const QString &bin);
    bool is_bin_Set() const;
    bool is_bin_Valid() const;

    OAITransaction_allOf_bumpOffer getBumpOffer() const;
    void setBumpOffer(const OAITransaction_allOf_bumpOffer &bump_offer);
    bool is_bump_offer_Set() const;
    bool is_bump_offer_Valid() const;

    OAITransaction_allOf_dcc getDcc() const;
    void setDcc(const OAITransaction_allOf_dcc &dcc);
    bool is_dcc_Set() const;
    bool is_dcc_Valid() const;

    QDateTime getDiscrepancyTime() const;
    void setDiscrepancyTime(const QDateTime &discrepancy_time);
    bool is_discrepancy_time_Set() const;
    bool is_discrepancy_time_Valid() const;

    QString getDisputeStatus() const;
    void setDisputeStatus(const QString &dispute_status);
    bool is_dispute_status_Set() const;
    bool is_dispute_status_Valid() const;

    QDateTime getDisputeTime() const;
    void setDisputeTime(const QDateTime &dispute_time);
    bool is_dispute_time_Set() const;
    bool is_dispute_time_Valid() const;

    OAITransaction_allOf_gateway getGateway() const;
    void setGateway(const OAITransaction_allOf_gateway &gateway);
    bool is_gateway_Set() const;
    bool is_gateway_Valid() const;

    QString getGatewayAccountId() const;
    void setGatewayAccountId(const QString &gateway_account_id);
    bool is_gateway_account_id_Set() const;
    bool is_gateway_account_id_Valid() const;

    QString getGatewayTransactionId() const;
    void setGatewayTransactionId(const QString &gateway_transaction_id);
    bool is_gateway_transaction_id_Set() const;
    bool is_gateway_transaction_id_Valid() const;

    bool isHadDiscrepancy() const;
    void setHadDiscrepancy(const bool &had_discrepancy);
    bool is_had_discrepancy_Set() const;
    bool is_had_discrepancy_Valid() const;

    bool isHasBumpOffer() const;
    void setHasBumpOffer(const bool &has_bump_offer);
    bool is_has_bump_offer_Set() const;
    bool is_has_bump_offer_Valid() const;

    bool isHasDcc() const;
    void setHasDcc(const bool &has_dcc);
    bool is_has_dcc_Set() const;
    bool is_has_dcc_Valid() const;

    bool isIsDisputed() const;
    void setIsDisputed(const bool &is_disputed);
    bool is_is_disputed_Set() const;
    bool is_is_disputed_Valid() const;

    bool isIsMerchantInitiated() const;
    void setIsMerchantInitiated(const bool &is_merchant_initiated);
    bool is_is_merchant_initiated_Set() const;
    bool is_is_merchant_initiated_Valid() const;

    bool isIsProcessedOutside() const;
    void setIsProcessedOutside(const bool &is_processed_outside);
    bool is_is_processed_outside_Set() const;
    bool is_is_processed_outside_Valid() const;

    bool isIsReconciled() const;
    void setIsReconciled(const bool &is_reconciled);
    bool is_is_reconciled_Set() const;
    bool is_is_reconciled_Valid() const;

    Q_DECL_DEPRECATED OAIPaymentMethod getMethod() const;
    Q_DECL_DEPRECATED void setMethod(const OAIPaymentMethod &method);
    Q_DECL_DEPRECATED bool is_method_Set() const;
    Q_DECL_DEPRECATED bool is_method_Valid() const;

    QString getNotificationUrl() const;
    void setNotificationUrl(const QString &notification_url);
    bool is_notification_url_Set() const;
    bool is_notification_url_Valid() const;

    Q_DECL_DEPRECATED QString getOrderId() const;
    Q_DECL_DEPRECATED void setOrderId(const QString &order_id);
    Q_DECL_DEPRECATED bool is_order_id_Set() const;
    Q_DECL_DEPRECATED bool is_order_id_Valid() const;

    QMap<QString, QString> getReferenceData() const;
    void setReferenceData(const QMap<QString, QString> &reference_data);
    bool is_reference_data_Set() const;
    bool is_reference_data_Valid() const;

    double getReportAmount() const;
    void setReportAmount(const double &report_amount);
    bool is_report_amount_Set() const;
    bool is_report_amount_Valid() const;

    QString getReportCurrency() const;
    void setReportCurrency(const QString &report_currency);
    bool is_report_currency_Set() const;
    bool is_report_currency_Valid() const;

    QString getRetriedTransactionId() const;
    void setRetriedTransactionId(const QString &retried_transaction_id);
    bool is_retried_transaction_id_Set() const;
    bool is_retried_transaction_id_Valid() const;

    QString getRetriesResult() const;
    void setRetriesResult(const QString &retries_result);
    bool is_retries_result_Set() const;
    bool is_retries_result_Valid() const;

    OAIPaymentRetry getRetryInstruction() const;
    void setRetryInstruction(const OAIPaymentRetry &retry_instruction);
    bool is_retry_instruction_Set() const;
    bool is_retry_instruction_Valid() const;

    qint32 getRevision() const;
    void setRevision(const qint32 &revision);
    bool is_revision_Set() const;
    bool is_revision_Valid() const;

    OAIRiskMetadata getRiskMetadata() const;
    void setRiskMetadata(const OAIRiskMetadata &risk_metadata);
    bool is_risk_metadata_Set() const;
    bool is_risk_metadata_Valid() const;

    qint32 getRiskScore() const;
    void setRiskScore(const qint32 &risk_score);
    bool is_risk_score_Set() const;
    bool is_risk_score_Valid() const;

    QDateTime getScheduledTime() const;
    void setScheduledTime(const QDateTime &scheduled_time);
    bool is_scheduled_time_Set() const;
    bool is_scheduled_time_Valid() const;

    QDateTime getSettlementTime() const;
    void setSettlementTime(const QDateTime &settlement_time);
    bool is_settlement_time_Set() const;
    bool is_settlement_time_Valid() const;

    qint32 getVelocity() const;
    void setVelocity(const qint32 &velocity);
    bool is_velocity_Set() const;
    bool is_velocity_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIThreeDSecureResult m_r_3ds;
    bool m_r_3ds_isSet;
    bool m_r_3ds_isValid;

    double m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    OAIContactObject m_billing_address;
    bool m_billing_address_isSet;
    bool m_billing_address_isValid;

    QString m_billing_descriptor;
    bool m_billing_descriptor_isSet;
    bool m_billing_descriptor_isValid;

    QList<QString> m_child_transactions;
    bool m_child_transactions_isSet;
    bool m_child_transactions_isValid;

    QDateTime m_created_time;
    bool m_created_time_isSet;
    bool m_created_time_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_customer_id;
    bool m_customer_id_isSet;
    bool m_customer_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIGatewayName m_gateway_name;
    bool m_gateway_name_isSet;
    bool m_gateway_name_isValid;

    bool m_has3ds;
    bool m_has3ds_isSet;
    bool m_has3ds_isValid;

    bool m_has_amount_adjustment;
    bool m_has_amount_adjustment_isSet;
    bool m_has_amount_adjustment_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<QString> m_invoice_ids;
    bool m_invoice_ids_isSet;
    bool m_invoice_ids_isValid;

    bool m_is_rebill;
    bool m_is_rebill_isSet;
    bool m_is_rebill_isValid;

    bool m_is_retry;
    bool m_is_retry_isSet;
    bool m_is_retry_isValid;

    QString m_parent_transaction_id;
    bool m_parent_transaction_id_isSet;
    bool m_parent_transaction_id_isValid;

    OAIPaymentInstrument m_payment_instrument;
    bool m_payment_instrument_isSet;
    bool m_payment_instrument_isValid;

    QList<QString> m_plan_ids;
    bool m_plan_ids_isSet;
    bool m_plan_ids_isValid;

    QDateTime m_processed_time;
    bool m_processed_time_isSet;
    bool m_processed_time_isValid;

    double m_purchase_amount;
    bool m_purchase_amount_isSet;
    bool m_purchase_amount_isValid;

    QString m_purchase_currency;
    bool m_purchase_currency_isSet;
    bool m_purchase_currency_isValid;

    qint32 m_rebill_number;
    bool m_rebill_number_isSet;
    bool m_rebill_number_isValid;

    QString m_redirect_url;
    bool m_redirect_url_isSet;
    bool m_redirect_url_isValid;

    double m_request_amount;
    bool m_request_amount_isSet;
    bool m_request_amount_isValid;

    QString m_request_currency;
    bool m_request_currency_isSet;
    bool m_request_currency_isValid;

    QString m_request_id;
    bool m_request_id_isSet;
    bool m_request_id_isValid;

    QString m_result;
    bool m_result_isSet;
    bool m_result_isValid;

    qint32 m_retry_number;
    bool m_retry_number_isSet;
    bool m_retry_number_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<QString> m_subscription_ids;
    bool m_subscription_ids_isSet;
    bool m_subscription_ids_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QDateTime m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    QString m_website_id;
    bool m_website_id_isSet;
    bool m_website_id_isValid;

    QList<OAITransaction_allOf__embedded> m__embedded;
    bool m__embedded_isSet;
    bool m__embedded_isValid;

    QList<OAITransaction_allOf__links> m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    OAIAcquirerName m_acquirer_name;
    bool m_acquirer_name_isSet;
    bool m_acquirer_name_isValid;

    QString m_arn;
    bool m_arn_isSet;
    bool m_arn_isValid;

    QString m_bin;
    bool m_bin_isSet;
    bool m_bin_isValid;

    OAITransaction_allOf_bumpOffer m_bump_offer;
    bool m_bump_offer_isSet;
    bool m_bump_offer_isValid;

    OAITransaction_allOf_dcc m_dcc;
    bool m_dcc_isSet;
    bool m_dcc_isValid;

    QDateTime m_discrepancy_time;
    bool m_discrepancy_time_isSet;
    bool m_discrepancy_time_isValid;

    QString m_dispute_status;
    bool m_dispute_status_isSet;
    bool m_dispute_status_isValid;

    QDateTime m_dispute_time;
    bool m_dispute_time_isSet;
    bool m_dispute_time_isValid;

    OAITransaction_allOf_gateway m_gateway;
    bool m_gateway_isSet;
    bool m_gateway_isValid;

    QString m_gateway_account_id;
    bool m_gateway_account_id_isSet;
    bool m_gateway_account_id_isValid;

    QString m_gateway_transaction_id;
    bool m_gateway_transaction_id_isSet;
    bool m_gateway_transaction_id_isValid;

    bool m_had_discrepancy;
    bool m_had_discrepancy_isSet;
    bool m_had_discrepancy_isValid;

    bool m_has_bump_offer;
    bool m_has_bump_offer_isSet;
    bool m_has_bump_offer_isValid;

    bool m_has_dcc;
    bool m_has_dcc_isSet;
    bool m_has_dcc_isValid;

    bool m_is_disputed;
    bool m_is_disputed_isSet;
    bool m_is_disputed_isValid;

    bool m_is_merchant_initiated;
    bool m_is_merchant_initiated_isSet;
    bool m_is_merchant_initiated_isValid;

    bool m_is_processed_outside;
    bool m_is_processed_outside_isSet;
    bool m_is_processed_outside_isValid;

    bool m_is_reconciled;
    bool m_is_reconciled_isSet;
    bool m_is_reconciled_isValid;

    OAIPaymentMethod m_method;
    bool m_method_isSet;
    bool m_method_isValid;

    QString m_notification_url;
    bool m_notification_url_isSet;
    bool m_notification_url_isValid;

    QString m_order_id;
    bool m_order_id_isSet;
    bool m_order_id_isValid;

    QMap<QString, QString> m_reference_data;
    bool m_reference_data_isSet;
    bool m_reference_data_isValid;

    double m_report_amount;
    bool m_report_amount_isSet;
    bool m_report_amount_isValid;

    QString m_report_currency;
    bool m_report_currency_isSet;
    bool m_report_currency_isValid;

    QString m_retried_transaction_id;
    bool m_retried_transaction_id_isSet;
    bool m_retried_transaction_id_isValid;

    QString m_retries_result;
    bool m_retries_result_isSet;
    bool m_retries_result_isValid;

    OAIPaymentRetry m_retry_instruction;
    bool m_retry_instruction_isSet;
    bool m_retry_instruction_isValid;

    qint32 m_revision;
    bool m_revision_isSet;
    bool m_revision_isValid;

    OAIRiskMetadata m_risk_metadata;
    bool m_risk_metadata_isSet;
    bool m_risk_metadata_isValid;

    qint32 m_risk_score;
    bool m_risk_score_isSet;
    bool m_risk_score_isValid;

    QDateTime m_scheduled_time;
    bool m_scheduled_time_isSet;
    bool m_scheduled_time_isValid;

    QDateTime m_settlement_time;
    bool m_settlement_time_isSet;
    bool m_settlement_time_isValid;

    qint32 m_velocity;
    bool m_velocity_isSet;
    bool m_velocity_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITransaction)

#endif // OAITransaction_H
