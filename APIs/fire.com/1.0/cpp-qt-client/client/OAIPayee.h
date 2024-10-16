/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPayee.h
 *
 * 
 */

#ifndef OAIPayee_H
#define OAIPayee_H

#include <QJsonObject>

#include "OAICurrency.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrency;

class OAIPayee : public OAIObject {
public:
    OAIPayee();
    OAIPayee(QString json);
    ~OAIPayee() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountHolderName() const;
    void setAccountHolderName(const QString &account_holder_name);
    bool is_account_holder_name_Set() const;
    bool is_account_holder_name_Valid() const;

    QString getAccountName() const;
    void setAccountName(const QString &account_name);
    bool is_account_name_Set() const;
    bool is_account_name_Valid() const;

    QString getAccountNumber() const;
    void setAccountNumber(const QString &account_number);
    bool is_account_number_Set() const;
    bool is_account_number_Valid() const;

    QString getBic() const;
    void setBic(const QString &bic);
    bool is_bic_Set() const;
    bool is_bic_Valid() const;

    QString getCreatedBy() const;
    void setCreatedBy(const QString &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    OAICurrency getCurrency() const;
    void setCurrency(const OAICurrency &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QString getIban() const;
    void setIban(const QString &iban);
    bool is_iban_Set() const;
    bool is_iban_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getNsc() const;
    void setNsc(const QString &nsc);
    bool is_nsc_Set() const;
    bool is_nsc_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_holder_name;
    bool m_account_holder_name_isSet;
    bool m_account_holder_name_isValid;

    QString m_account_name;
    bool m_account_name_isSet;
    bool m_account_name_isValid;

    QString m_account_number;
    bool m_account_number_isSet;
    bool m_account_number_isValid;

    QString m_bic;
    bool m_bic_isSet;
    bool m_bic_isValid;

    QString m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    OAICurrency m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QString m_iban;
    bool m_iban_isSet;
    bool m_iban_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_nsc;
    bool m_nsc_isSet;
    bool m_nsc_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPayee)

#endif // OAIPayee_H
