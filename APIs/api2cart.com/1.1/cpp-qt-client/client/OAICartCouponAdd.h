/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICartCouponAdd.h
 *
 * 
 */

#ifndef OAICartCouponAdd_H
#define OAICartCouponAdd_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICartCouponAdd : public OAIObject {
public:
    OAICartCouponAdd();
    OAICartCouponAdd(QString json);
    ~OAICartCouponAdd() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getActionAmount() const;
    void setActionAmount(const double &action_amount);
    bool is_action_amount_Set() const;
    bool is_action_amount_Valid() const;

    QString getActionApplyTo() const;
    void setActionApplyTo(const QString &action_apply_to);
    bool is_action_apply_to_Set() const;
    bool is_action_apply_to_Valid() const;

    QString getActionConditionEntity() const;
    void setActionConditionEntity(const QString &action_condition_entity);
    bool is_action_condition_entity_Set() const;
    bool is_action_condition_entity_Valid() const;

    QString getActionConditionKey() const;
    void setActionConditionKey(const QString &action_condition_key);
    bool is_action_condition_key_Set() const;
    bool is_action_condition_key_Valid() const;

    QString getActionConditionOperator() const;
    void setActionConditionOperator(const QString &action_condition_operator);
    bool is_action_condition_operator_Set() const;
    bool is_action_condition_operator_Valid() const;

    QString getActionConditionValue() const;
    void setActionConditionValue(const QString &action_condition_value);
    bool is_action_condition_value_Set() const;
    bool is_action_condition_value_Valid() const;

    QString getActionScope() const;
    void setActionScope(const QString &action_scope);
    bool is_action_scope_Set() const;
    bool is_action_scope_Valid() const;

    QString getActionType() const;
    void setActionType(const QString &action_type);
    bool is_action_type_Set() const;
    bool is_action_type_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QList<QString> getCodes() const;
    void setCodes(const QList<QString> &codes);
    bool is_codes_Set() const;
    bool is_codes_Valid() const;

    QString getDateEnd() const;
    void setDateEnd(const QString &date_end);
    bool is_date_end_Set() const;
    bool is_date_end_Valid() const;

    QString getDateStart() const;
    void setDateStart(const QString &date_start);
    bool is_date_start_Set() const;
    bool is_date_start_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    qint32 getUsageLimit() const;
    void setUsageLimit(const qint32 &usage_limit);
    bool is_usage_limit_Set() const;
    bool is_usage_limit_Valid() const;

    qint32 getUsageLimitPerCustomer() const;
    void setUsageLimitPerCustomer(const qint32 &usage_limit_per_customer);
    bool is_usage_limit_per_customer_Set() const;
    bool is_usage_limit_per_customer_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_action_amount;
    bool m_action_amount_isSet;
    bool m_action_amount_isValid;

    QString m_action_apply_to;
    bool m_action_apply_to_isSet;
    bool m_action_apply_to_isValid;

    QString m_action_condition_entity;
    bool m_action_condition_entity_isSet;
    bool m_action_condition_entity_isValid;

    QString m_action_condition_key;
    bool m_action_condition_key_isSet;
    bool m_action_condition_key_isValid;

    QString m_action_condition_operator;
    bool m_action_condition_operator_isSet;
    bool m_action_condition_operator_isValid;

    QString m_action_condition_value;
    bool m_action_condition_value_isSet;
    bool m_action_condition_value_isValid;

    QString m_action_scope;
    bool m_action_scope_isSet;
    bool m_action_scope_isValid;

    QString m_action_type;
    bool m_action_type_isSet;
    bool m_action_type_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QList<QString> m_codes;
    bool m_codes_isSet;
    bool m_codes_isValid;

    QString m_date_end;
    bool m_date_end_isSet;
    bool m_date_end_isValid;

    QString m_date_start;
    bool m_date_start_isSet;
    bool m_date_start_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    qint32 m_usage_limit;
    bool m_usage_limit_isSet;
    bool m_usage_limit_isValid;

    qint32 m_usage_limit_per_customer;
    bool m_usage_limit_per_customer_isSet;
    bool m_usage_limit_per_customer_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartCouponAdd)

#endif // OAICartCouponAdd_H
