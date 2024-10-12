/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISales_rule_data_rule_interface.h
 *
 * Interface RuleInterface
 */

#ifndef OAISales_rule_data_rule_interface_H
#define OAISales_rule_data_rule_interface_H

#include <QJsonObject>

#include "OAISales_rule_data_condition_interface.h"
#include "OAISales_rule_data_rule_extension_interface.h"
#include "OAISales_rule_data_rule_label_interface.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISales_rule_data_condition_interface;
class OAISales_rule_data_rule_extension_interface;
class OAISales_rule_data_rule_label_interface;

class OAISales_rule_data_rule_interface : public OAIObject {
public:
    OAISales_rule_data_rule_interface();
    OAISales_rule_data_rule_interface(QString json);
    ~OAISales_rule_data_rule_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISales_rule_data_condition_interface getActionCondition() const;
    void setActionCondition(const OAISales_rule_data_condition_interface &action_condition);
    bool is_action_condition_Set() const;
    bool is_action_condition_Valid() const;

    bool isApplyToShipping() const;
    void setApplyToShipping(const bool &apply_to_shipping);
    bool is_apply_to_shipping_Set() const;
    bool is_apply_to_shipping_Valid() const;

    OAISales_rule_data_condition_interface getCondition() const;
    void setCondition(const OAISales_rule_data_condition_interface &condition);
    bool is_condition_Set() const;
    bool is_condition_Valid() const;

    QString getCouponType() const;
    void setCouponType(const QString &coupon_type);
    bool is_coupon_type_Set() const;
    bool is_coupon_type_Valid() const;

    QList<qint32> getCustomerGroupIds() const;
    void setCustomerGroupIds(const QList<qint32> &customer_group_ids);
    bool is_customer_group_ids_Set() const;
    bool is_customer_group_ids_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    double getDiscountAmount() const;
    void setDiscountAmount(const double &discount_amount);
    bool is_discount_amount_Set() const;
    bool is_discount_amount_Valid() const;

    double getDiscountQty() const;
    void setDiscountQty(const double &discount_qty);
    bool is_discount_qty_Set() const;
    bool is_discount_qty_Valid() const;

    qint32 getDiscountStep() const;
    void setDiscountStep(const qint32 &discount_step);
    bool is_discount_step_Set() const;
    bool is_discount_step_Valid() const;

    OAISales_rule_data_rule_extension_interface getExtensionAttributes() const;
    void setExtensionAttributes(const OAISales_rule_data_rule_extension_interface &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getFromDate() const;
    void setFromDate(const QString &from_date);
    bool is_from_date_Set() const;
    bool is_from_date_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsAdvanced() const;
    void setIsAdvanced(const bool &is_advanced);
    bool is_is_advanced_Set() const;
    bool is_is_advanced_Valid() const;

    bool isIsRss() const;
    void setIsRss(const bool &is_rss);
    bool is_is_rss_Set() const;
    bool is_is_rss_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<qint32> getProductIds() const;
    void setProductIds(const QList<qint32> &product_ids);
    bool is_product_ids_Set() const;
    bool is_product_ids_Valid() const;

    qint32 getRuleId() const;
    void setRuleId(const qint32 &rule_id);
    bool is_rule_id_Set() const;
    bool is_rule_id_Valid() const;

    QString getSimpleAction() const;
    void setSimpleAction(const QString &simple_action);
    bool is_simple_action_Set() const;
    bool is_simple_action_Valid() const;

    QString getSimpleFreeShipping() const;
    void setSimpleFreeShipping(const QString &simple_free_shipping);
    bool is_simple_free_shipping_Set() const;
    bool is_simple_free_shipping_Valid() const;

    qint32 getSortOrder() const;
    void setSortOrder(const qint32 &sort_order);
    bool is_sort_order_Set() const;
    bool is_sort_order_Valid() const;

    bool isStopRulesProcessing() const;
    void setStopRulesProcessing(const bool &stop_rules_processing);
    bool is_stop_rules_processing_Set() const;
    bool is_stop_rules_processing_Valid() const;

    QList<OAISales_rule_data_rule_label_interface> getStoreLabels() const;
    void setStoreLabels(const QList<OAISales_rule_data_rule_label_interface> &store_labels);
    bool is_store_labels_Set() const;
    bool is_store_labels_Valid() const;

    qint32 getTimesUsed() const;
    void setTimesUsed(const qint32 &times_used);
    bool is_times_used_Set() const;
    bool is_times_used_Valid() const;

    QString getToDate() const;
    void setToDate(const QString &to_date);
    bool is_to_date_Set() const;
    bool is_to_date_Valid() const;

    bool isUseAutoGeneration() const;
    void setUseAutoGeneration(const bool &use_auto_generation);
    bool is_use_auto_generation_Set() const;
    bool is_use_auto_generation_Valid() const;

    qint32 getUsesPerCoupon() const;
    void setUsesPerCoupon(const qint32 &uses_per_coupon);
    bool is_uses_per_coupon_Set() const;
    bool is_uses_per_coupon_Valid() const;

    qint32 getUsesPerCustomer() const;
    void setUsesPerCustomer(const qint32 &uses_per_customer);
    bool is_uses_per_customer_Set() const;
    bool is_uses_per_customer_Valid() const;

    QList<qint32> getWebsiteIds() const;
    void setWebsiteIds(const QList<qint32> &website_ids);
    bool is_website_ids_Set() const;
    bool is_website_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISales_rule_data_condition_interface m_action_condition;
    bool m_action_condition_isSet;
    bool m_action_condition_isValid;

    bool m_apply_to_shipping;
    bool m_apply_to_shipping_isSet;
    bool m_apply_to_shipping_isValid;

    OAISales_rule_data_condition_interface m_condition;
    bool m_condition_isSet;
    bool m_condition_isValid;

    QString m_coupon_type;
    bool m_coupon_type_isSet;
    bool m_coupon_type_isValid;

    QList<qint32> m_customer_group_ids;
    bool m_customer_group_ids_isSet;
    bool m_customer_group_ids_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    double m_discount_amount;
    bool m_discount_amount_isSet;
    bool m_discount_amount_isValid;

    double m_discount_qty;
    bool m_discount_qty_isSet;
    bool m_discount_qty_isValid;

    qint32 m_discount_step;
    bool m_discount_step_isSet;
    bool m_discount_step_isValid;

    OAISales_rule_data_rule_extension_interface m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_from_date;
    bool m_from_date_isSet;
    bool m_from_date_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_advanced;
    bool m_is_advanced_isSet;
    bool m_is_advanced_isValid;

    bool m_is_rss;
    bool m_is_rss_isSet;
    bool m_is_rss_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<qint32> m_product_ids;
    bool m_product_ids_isSet;
    bool m_product_ids_isValid;

    qint32 m_rule_id;
    bool m_rule_id_isSet;
    bool m_rule_id_isValid;

    QString m_simple_action;
    bool m_simple_action_isSet;
    bool m_simple_action_isValid;

    QString m_simple_free_shipping;
    bool m_simple_free_shipping_isSet;
    bool m_simple_free_shipping_isValid;

    qint32 m_sort_order;
    bool m_sort_order_isSet;
    bool m_sort_order_isValid;

    bool m_stop_rules_processing;
    bool m_stop_rules_processing_isSet;
    bool m_stop_rules_processing_isValid;

    QList<OAISales_rule_data_rule_label_interface> m_store_labels;
    bool m_store_labels_isSet;
    bool m_store_labels_isValid;

    qint32 m_times_used;
    bool m_times_used_isSet;
    bool m_times_used_isValid;

    QString m_to_date;
    bool m_to_date_isSet;
    bool m_to_date_isValid;

    bool m_use_auto_generation;
    bool m_use_auto_generation_isSet;
    bool m_use_auto_generation_isValid;

    qint32 m_uses_per_coupon;
    bool m_uses_per_coupon_isSet;
    bool m_uses_per_coupon_isValid;

    qint32 m_uses_per_customer;
    bool m_uses_per_customer_isSet;
    bool m_uses_per_customer_isValid;

    QList<qint32> m_website_ids;
    bool m_website_ids_isSet;
    bool m_website_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_rule_data_rule_interface)

#endif // OAISales_rule_data_rule_interface_H
