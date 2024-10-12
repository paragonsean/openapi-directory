/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICustomer.h
 *
 * Customer information
 */

#ifndef OAICustomer_H
#define OAICustomer_H

#include <QJsonObject>

#include "OAICustomerAttributes.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICustomerAttributes;

class OAICustomer : public OAIObject {
public:
    OAICustomer();
    OAICustomer(QString json);
    ~OAICustomer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    Q_DECL_DEPRECATED QString getActivationCode() const;
    Q_DECL_DEPRECATED void setActivationCode(const QString &activation_code);
    Q_DECL_DEPRECATED bool is_activation_code_Set() const;
    Q_DECL_DEPRECATED bool is_activation_code_Valid() const;

    qint32 getCntGuestUser() const;
    void setCntGuestUser(const qint32 &cnt_guest_user);
    bool is_cnt_guest_user_Set() const;
    bool is_cnt_guest_user_Valid() const;

    qint32 getCntInternalUser() const;
    void setCntInternalUser(const qint32 &cnt_internal_user);
    bool is_cnt_internal_user_Set() const;
    bool is_cnt_internal_user_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAICustomerAttributes getCustomerAttributes() const;
    void setCustomerAttributes(const OAICustomerAttributes &customer_attributes);
    bool is_customer_attributes_Set() const;
    bool is_customer_attributes_Valid() const;

    QString getCustomerContractType() const;
    void setCustomerContractType(const QString &customer_contract_type);
    bool is_customer_contract_type_Set() const;
    bool is_customer_contract_type_Valid() const;

    QString getCustomerUuid() const;
    void setCustomerUuid(const QString &customer_uuid);
    bool is_customer_uuid_Set() const;
    bool is_customer_uuid_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsLocked() const;
    void setIsLocked(const bool &is_locked);
    bool is_is_locked_Set() const;
    bool is_is_locked_Valid() const;

    QDateTime getLastLoginAt() const;
    void setLastLoginAt(const QDateTime &last_login_at);
    bool is_last_login_at_Set() const;
    bool is_last_login_at_Valid() const;

    Q_DECL_DEPRECATED bool isLockStatus() const;
    Q_DECL_DEPRECATED void setLockStatus(const bool &lock_status);
    Q_DECL_DEPRECATED bool is_lock_status_Set() const;
    Q_DECL_DEPRECATED bool is_lock_status_Valid() const;

    QString getProviderCustomerId() const;
    void setProviderCustomerId(const QString &provider_customer_id);
    bool is_provider_customer_id_Set() const;
    bool is_provider_customer_id_Valid() const;

    qint64 getQuotaMax() const;
    void setQuotaMax(const qint64 &quota_max);
    bool is_quota_max_Set() const;
    bool is_quota_max_Valid() const;

    qint64 getQuotaUsed() const;
    void setQuotaUsed(const qint64 &quota_used);
    bool is_quota_used_Set() const;
    bool is_quota_used_Valid() const;

    qint32 getTrialDaysLeft() const;
    void setTrialDaysLeft(const qint32 &trial_days_left);
    bool is_trial_days_left_Set() const;
    bool is_trial_days_left_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    qint32 getUserMax() const;
    void setUserMax(const qint32 &user_max);
    bool is_user_max_Set() const;
    bool is_user_max_Valid() const;

    qint32 getUserUsed() const;
    void setUserUsed(const qint32 &user_used);
    bool is_user_used_Set() const;
    bool is_user_used_Valid() const;

    qint64 getWebhooksMax() const;
    void setWebhooksMax(const qint64 &webhooks_max);
    bool is_webhooks_max_Set() const;
    bool is_webhooks_max_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_activation_code;
    bool m_activation_code_isSet;
    bool m_activation_code_isValid;

    qint32 m_cnt_guest_user;
    bool m_cnt_guest_user_isSet;
    bool m_cnt_guest_user_isValid;

    qint32 m_cnt_internal_user;
    bool m_cnt_internal_user_isSet;
    bool m_cnt_internal_user_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAICustomerAttributes m_customer_attributes;
    bool m_customer_attributes_isSet;
    bool m_customer_attributes_isValid;

    QString m_customer_contract_type;
    bool m_customer_contract_type_isSet;
    bool m_customer_contract_type_isValid;

    QString m_customer_uuid;
    bool m_customer_uuid_isSet;
    bool m_customer_uuid_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_locked;
    bool m_is_locked_isSet;
    bool m_is_locked_isValid;

    QDateTime m_last_login_at;
    bool m_last_login_at_isSet;
    bool m_last_login_at_isValid;

    bool m_lock_status;
    bool m_lock_status_isSet;
    bool m_lock_status_isValid;

    QString m_provider_customer_id;
    bool m_provider_customer_id_isSet;
    bool m_provider_customer_id_isValid;

    qint64 m_quota_max;
    bool m_quota_max_isSet;
    bool m_quota_max_isValid;

    qint64 m_quota_used;
    bool m_quota_used_isSet;
    bool m_quota_used_isValid;

    qint32 m_trial_days_left;
    bool m_trial_days_left_isSet;
    bool m_trial_days_left_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    qint32 m_user_max;
    bool m_user_max_isSet;
    bool m_user_max_isValid;

    qint32 m_user_used;
    bool m_user_used_isSet;
    bool m_user_used_isValid;

    qint64 m_webhooks_max;
    bool m_webhooks_max_isSet;
    bool m_webhooks_max_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomer)

#endif // OAICustomer_H
