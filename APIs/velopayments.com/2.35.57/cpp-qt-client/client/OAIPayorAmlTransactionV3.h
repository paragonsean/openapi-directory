/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPayorAmlTransactionV3.h
 *
 * 
 */

#ifndef OAIPayorAmlTransactionV3_H
#define OAIPayorAmlTransactionV3_H

#include <QJsonObject>

#include <QDate>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPayorAmlTransactionV3 : public OAIObject {
public:
    OAIPayorAmlTransactionV3();
    OAIPayorAmlTransactionV3(QString json);
    ~OAIPayorAmlTransactionV3() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCredit() const;
    void setCredit(const qint64 &credit);
    bool is_credit_Set() const;
    bool is_credit_Valid() const;

    QString getCreditCurrency() const;
    void setCreditCurrency(const QString &credit_currency);
    bool is_credit_currency_Set() const;
    bool is_credit_currency_Valid() const;

    QString getDateFundingRequested() const;
    void setDateFundingRequested(const QString &date_funding_requested);
    bool is_date_funding_requested_Set() const;
    bool is_date_funding_requested_Valid() const;

    qint64 getDebit() const;
    void setDebit(const qint64 &debit);
    bool is_debit_Set() const;
    bool is_debit_Valid() const;

    QString getDebitCurrency() const;
    void setDebitCurrency(const QString &debit_currency);
    bool is_debit_currency_Set() const;
    bool is_debit_currency_Valid() const;

    QString getFundingType() const;
    void setFundingType(const QString &funding_type);
    bool is_funding_type_Set() const;
    bool is_funding_type_Valid() const;

    double getFxApplied() const;
    void setFxApplied(const double &fx_applied);
    bool is_fx_applied_Set() const;
    bool is_fx_applied_Valid() const;

    QString getPayeeType() const;
    void setPayeeType(const QString &payee_type);
    bool is_payee_type_Set() const;
    bool is_payee_type_Valid() const;

    qint64 getPaymentAmount() const;
    void setPaymentAmount(const qint64 &payment_amount);
    bool is_payment_amount_Set() const;
    bool is_payment_amount_Valid() const;

    QString getPaymentCurrency() const;
    void setPaymentCurrency(const QString &payment_currency);
    bool is_payment_currency_Set() const;
    bool is_payment_currency_Valid() const;

    QString getPaymentMemo() const;
    void setPaymentMemo(const QString &payment_memo);
    bool is_payment_memo_Set() const;
    bool is_payment_memo_Valid() const;

    QString getPaymentRails() const;
    void setPaymentRails(const QString &payment_rails);
    bool is_payment_rails_Set() const;
    bool is_payment_rails_Valid() const;

    QString getPaymentStatus() const;
    void setPaymentStatus(const QString &payment_status);
    bool is_payment_status_Set() const;
    bool is_payment_status_Valid() const;

    QString getPayorPaymentId() const;
    void setPayorPaymentId(const QString &payor_payment_id);
    bool is_payor_payment_id_Set() const;
    bool is_payor_payment_id_Valid() const;

    QString getRejectReason() const;
    void setRejectReason(const QString &reject_reason);
    bool is_reject_reason_Set() const;
    bool is_reject_reason_Valid() const;

    QString getRemoteId() const;
    void setRemoteId(const QString &remote_id);
    bool is_remote_id_Set() const;
    bool is_remote_id_Valid() const;

    QString getReportTransactionType() const;
    void setReportTransactionType(const QString &report_transaction_type);
    bool is_report_transaction_type_Set() const;
    bool is_report_transaction_type_Valid() const;

    QString getReturnCode() const;
    void setReturnCode(const QString &return_code);
    bool is_return_code_Set() const;
    bool is_return_code_Valid() const;

    QString getReturnDescription() const;
    void setReturnDescription(const QString &return_description);
    bool is_return_description_Set() const;
    bool is_return_description_Valid() const;

    QString getReturnFee() const;
    void setReturnFee(const QString &return_fee);
    bool is_return_fee_Set() const;
    bool is_return_fee_Valid() const;

    QString getReturnFeeCurrency() const;
    void setReturnFeeCurrency(const QString &return_fee_currency);
    bool is_return_fee_currency_Set() const;
    bool is_return_fee_currency_Valid() const;

    QString getReturnFeeDescription() const;
    void setReturnFeeDescription(const QString &return_fee_description);
    bool is_return_fee_description_Set() const;
    bool is_return_fee_description_Valid() const;

    QString getSourceAccount() const;
    void setSourceAccount(const QString &source_account);
    bool is_source_account_Set() const;
    bool is_source_account_Valid() const;

    QDate getTransactionDate() const;
    void setTransactionDate(const QDate &transaction_date);
    bool is_transaction_date_Set() const;
    bool is_transaction_date_Valid() const;

    QString getTransactionTime() const;
    void setTransactionTime(const QString &transaction_time);
    bool is_transaction_time_Set() const;
    bool is_transaction_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_credit;
    bool m_credit_isSet;
    bool m_credit_isValid;

    QString m_credit_currency;
    bool m_credit_currency_isSet;
    bool m_credit_currency_isValid;

    QString m_date_funding_requested;
    bool m_date_funding_requested_isSet;
    bool m_date_funding_requested_isValid;

    qint64 m_debit;
    bool m_debit_isSet;
    bool m_debit_isValid;

    QString m_debit_currency;
    bool m_debit_currency_isSet;
    bool m_debit_currency_isValid;

    QString m_funding_type;
    bool m_funding_type_isSet;
    bool m_funding_type_isValid;

    double m_fx_applied;
    bool m_fx_applied_isSet;
    bool m_fx_applied_isValid;

    QString m_payee_type;
    bool m_payee_type_isSet;
    bool m_payee_type_isValid;

    qint64 m_payment_amount;
    bool m_payment_amount_isSet;
    bool m_payment_amount_isValid;

    QString m_payment_currency;
    bool m_payment_currency_isSet;
    bool m_payment_currency_isValid;

    QString m_payment_memo;
    bool m_payment_memo_isSet;
    bool m_payment_memo_isValid;

    QString m_payment_rails;
    bool m_payment_rails_isSet;
    bool m_payment_rails_isValid;

    QString m_payment_status;
    bool m_payment_status_isSet;
    bool m_payment_status_isValid;

    QString m_payor_payment_id;
    bool m_payor_payment_id_isSet;
    bool m_payor_payment_id_isValid;

    QString m_reject_reason;
    bool m_reject_reason_isSet;
    bool m_reject_reason_isValid;

    QString m_remote_id;
    bool m_remote_id_isSet;
    bool m_remote_id_isValid;

    QString m_report_transaction_type;
    bool m_report_transaction_type_isSet;
    bool m_report_transaction_type_isValid;

    QString m_return_code;
    bool m_return_code_isSet;
    bool m_return_code_isValid;

    QString m_return_description;
    bool m_return_description_isSet;
    bool m_return_description_isValid;

    QString m_return_fee;
    bool m_return_fee_isSet;
    bool m_return_fee_isValid;

    QString m_return_fee_currency;
    bool m_return_fee_currency_isSet;
    bool m_return_fee_currency_isValid;

    QString m_return_fee_description;
    bool m_return_fee_description_isSet;
    bool m_return_fee_description_isValid;

    QString m_source_account;
    bool m_source_account_isSet;
    bool m_source_account_isValid;

    QDate m_transaction_date;
    bool m_transaction_date_isSet;
    bool m_transaction_date_isValid;

    QString m_transaction_time;
    bool m_transaction_time_isSet;
    bool m_transaction_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPayorAmlTransactionV3)

#endif // OAIPayorAmlTransactionV3_H
