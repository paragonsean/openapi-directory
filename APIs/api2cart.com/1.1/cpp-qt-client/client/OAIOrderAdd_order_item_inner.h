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
 * OAIOrderAdd_order_item_inner.h
 *
 * 
 */

#ifndef OAIOrderAdd_order_item_inner_H
#define OAIOrderAdd_order_item_inner_H

#include <QJsonObject>

#include "OAIOrderAdd_order_item_inner_order_item_option_inner.h"
#include "OAIOrderAdd_order_item_inner_order_item_property_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrderAdd_order_item_inner_order_item_option_inner;
class OAIOrderAdd_order_item_inner_order_item_property_inner;

class OAIOrderAdd_order_item_inner : public OAIObject {
public:
    OAIOrderAdd_order_item_inner();
    OAIOrderAdd_order_item_inner(QString json);
    ~OAIOrderAdd_order_item_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isOrderItemAllowRefundItemsSeparately() const;
    void setOrderItemAllowRefundItemsSeparately(const bool &order_item_allow_refund_items_separately);
    bool is_order_item_allow_refund_items_separately_Set() const;
    bool is_order_item_allow_refund_items_separately_Valid() const;

    bool isOrderItemAllowShipItemsSeparately() const;
    void setOrderItemAllowShipItemsSeparately(const bool &order_item_allow_ship_items_separately);
    bool is_order_item_allow_ship_items_separately_Set() const;
    bool is_order_item_allow_ship_items_separately_Valid() const;

    QString getOrderItemId() const;
    void setOrderItemId(const QString &order_item_id);
    bool is_order_item_id_Set() const;
    bool is_order_item_id_Valid() const;

    QString getOrderItemModel() const;
    void setOrderItemModel(const QString &order_item_model);
    bool is_order_item_model_Set() const;
    bool is_order_item_model_Valid() const;

    QString getOrderItemName() const;
    void setOrderItemName(const QString &order_item_name);
    bool is_order_item_name_Set() const;
    bool is_order_item_name_Valid() const;

    QList<OAIOrderAdd_order_item_inner_order_item_option_inner> getOrderItemOption() const;
    void setOrderItemOption(const QList<OAIOrderAdd_order_item_inner_order_item_option_inner> &order_item_option);
    bool is_order_item_option_Set() const;
    bool is_order_item_option_Valid() const;

    qint32 getOrderItemParent() const;
    void setOrderItemParent(const qint32 &order_item_parent);
    bool is_order_item_parent_Set() const;
    bool is_order_item_parent_Valid() const;

    QString getOrderItemParentOptionName() const;
    void setOrderItemParentOptionName(const QString &order_item_parent_option_name);
    bool is_order_item_parent_option_name_Set() const;
    bool is_order_item_parent_option_name_Valid() const;

    double getOrderItemPrice() const;
    void setOrderItemPrice(const double &order_item_price);
    bool is_order_item_price_Set() const;
    bool is_order_item_price_Valid() const;

    bool isOrderItemPriceIncludesTax() const;
    void setOrderItemPriceIncludesTax(const bool &order_item_price_includes_tax);
    bool is_order_item_price_includes_tax_Set() const;
    bool is_order_item_price_includes_tax_Valid() const;

    QList<OAIOrderAdd_order_item_inner_order_item_property_inner> getOrderItemProperty() const;
    void setOrderItemProperty(const QList<OAIOrderAdd_order_item_inner_order_item_property_inner> &order_item_property);
    bool is_order_item_property_Set() const;
    bool is_order_item_property_Valid() const;

    qint32 getOrderItemQuantity() const;
    void setOrderItemQuantity(const qint32 &order_item_quantity);
    bool is_order_item_quantity_Set() const;
    bool is_order_item_quantity_Valid() const;

    double getOrderItemTax() const;
    void setOrderItemTax(const double &order_item_tax);
    bool is_order_item_tax_Set() const;
    bool is_order_item_tax_Valid() const;

    QString getOrderItemVariantId() const;
    void setOrderItemVariantId(const QString &order_item_variant_id);
    bool is_order_item_variant_id_Set() const;
    bool is_order_item_variant_id_Valid() const;

    double getOrderItemWeight() const;
    void setOrderItemWeight(const double &order_item_weight);
    bool is_order_item_weight_Set() const;
    bool is_order_item_weight_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_order_item_allow_refund_items_separately;
    bool m_order_item_allow_refund_items_separately_isSet;
    bool m_order_item_allow_refund_items_separately_isValid;

    bool m_order_item_allow_ship_items_separately;
    bool m_order_item_allow_ship_items_separately_isSet;
    bool m_order_item_allow_ship_items_separately_isValid;

    QString m_order_item_id;
    bool m_order_item_id_isSet;
    bool m_order_item_id_isValid;

    QString m_order_item_model;
    bool m_order_item_model_isSet;
    bool m_order_item_model_isValid;

    QString m_order_item_name;
    bool m_order_item_name_isSet;
    bool m_order_item_name_isValid;

    QList<OAIOrderAdd_order_item_inner_order_item_option_inner> m_order_item_option;
    bool m_order_item_option_isSet;
    bool m_order_item_option_isValid;

    qint32 m_order_item_parent;
    bool m_order_item_parent_isSet;
    bool m_order_item_parent_isValid;

    QString m_order_item_parent_option_name;
    bool m_order_item_parent_option_name_isSet;
    bool m_order_item_parent_option_name_isValid;

    double m_order_item_price;
    bool m_order_item_price_isSet;
    bool m_order_item_price_isValid;

    bool m_order_item_price_includes_tax;
    bool m_order_item_price_includes_tax_isSet;
    bool m_order_item_price_includes_tax_isValid;

    QList<OAIOrderAdd_order_item_inner_order_item_property_inner> m_order_item_property;
    bool m_order_item_property_isSet;
    bool m_order_item_property_isValid;

    qint32 m_order_item_quantity;
    bool m_order_item_quantity_isSet;
    bool m_order_item_quantity_isValid;

    double m_order_item_tax;
    bool m_order_item_tax_isSet;
    bool m_order_item_tax_isValid;

    QString m_order_item_variant_id;
    bool m_order_item_variant_id_isSet;
    bool m_order_item_variant_id_isValid;

    double m_order_item_weight;
    bool m_order_item_weight_isSet;
    bool m_order_item_weight_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrderAdd_order_item_inner)

#endif // OAIOrderAdd_order_item_inner_H
