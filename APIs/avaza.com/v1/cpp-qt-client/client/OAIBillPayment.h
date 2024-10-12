/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBillPayment.h
 *
 * 
 */

#ifndef OAIBillPayment_H
#define OAIBillPayment_H

#include <QJsonObject>

#include "OAIBillPaymentAllocation.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBillPaymentAllocation;

class OAIBillPayment : public OAIObject {
public:
    OAIBillPayment();
    OAIBillPayment(QString json);
    ~OAIBillPayment() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccountIdfk() const;
    void setAccountIdfk(const qint32 &account_idfk);
    bool is_account_idfk_Set() const;
    bool is_account_idfk_Valid() const;

    double getBalance() const;
    void setBalance(const double &balance);
    bool is_balance_Set() const;
    bool is_balance_Valid() const;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateIssued() const;
    void setDateIssued(const QDateTime &date_issued);
    bool is_date_issued_Set() const;
    bool is_date_issued_Valid() const;

    QDateTime getDateUpdated() const;
    void setDateUpdated(const QDateTime &date_updated);
    bool is_date_updated_Set() const;
    bool is_date_updated_Valid() const;

    double getExchangeRate() const;
    void setExchangeRate(const double &exchange_rate);
    bool is_exchange_rate_Set() const;
    bool is_exchange_rate_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    QList<OAIBillPaymentAllocation> getPaymentAllocations() const;
    void setPaymentAllocations(const QList<OAIBillPaymentAllocation> &payment_allocations);
    bool is_payment_allocations_Set() const;
    bool is_payment_allocations_Valid() const;

    QString getPaymentNumber() const;
    void setPaymentNumber(const QString &payment_number);
    bool is_payment_number_Set() const;
    bool is_payment_number_Valid() const;

    QString getPaymentProviderCode() const;
    void setPaymentProviderCode(const QString &payment_provider_code);
    bool is_payment_provider_code_Set() const;
    bool is_payment_provider_code_Valid() const;

    qint32 getSupplierIdfk() const;
    void setSupplierIdfk(const qint32 &supplier_idfk);
    bool is_supplier_idfk_Set() const;
    bool is_supplier_idfk_Valid() const;

    double getTotalAmount() const;
    void setTotalAmount(const double &total_amount);
    bool is_total_amount_Set() const;
    bool is_total_amount_Valid() const;

    qint64 getTransactionId() const;
    void setTransactionId(const qint64 &transaction_id);
    bool is_transaction_id_Set() const;
    bool is_transaction_id_Valid() const;

    QString getTransactionPrefix() const;
    void setTransactionPrefix(const QString &transaction_prefix);
    bool is_transaction_prefix_Set() const;
    bool is_transaction_prefix_Valid() const;

    QString getTransactionReference() const;
    void setTransactionReference(const QString &transaction_reference);
    bool is_transaction_reference_Set() const;
    bool is_transaction_reference_Valid() const;

    QString getTransactionStatusCode() const;
    void setTransactionStatusCode(const QString &transaction_status_code);
    bool is_transaction_status_code_Set() const;
    bool is_transaction_status_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_account_idfk;
    bool m_account_idfk_isSet;
    bool m_account_idfk_isValid;

    double m_balance;
    bool m_balance_isSet;
    bool m_balance_isValid;

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_issued;
    bool m_date_issued_isSet;
    bool m_date_issued_isValid;

    QDateTime m_date_updated;
    bool m_date_updated_isSet;
    bool m_date_updated_isValid;

    double m_exchange_rate;
    bool m_exchange_rate_isSet;
    bool m_exchange_rate_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    QList<OAIBillPaymentAllocation> m_payment_allocations;
    bool m_payment_allocations_isSet;
    bool m_payment_allocations_isValid;

    QString m_payment_number;
    bool m_payment_number_isSet;
    bool m_payment_number_isValid;

    QString m_payment_provider_code;
    bool m_payment_provider_code_isSet;
    bool m_payment_provider_code_isValid;

    qint32 m_supplier_idfk;
    bool m_supplier_idfk_isSet;
    bool m_supplier_idfk_isValid;

    double m_total_amount;
    bool m_total_amount_isSet;
    bool m_total_amount_isValid;

    qint64 m_transaction_id;
    bool m_transaction_id_isSet;
    bool m_transaction_id_isValid;

    QString m_transaction_prefix;
    bool m_transaction_prefix_isSet;
    bool m_transaction_prefix_isValid;

    QString m_transaction_reference;
    bool m_transaction_reference_isSet;
    bool m_transaction_reference_isValid;

    QString m_transaction_status_code;
    bool m_transaction_status_code_isSet;
    bool m_transaction_status_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBillPayment)

#endif // OAIBillPayment_H
