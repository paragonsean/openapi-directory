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
 * OAIQuote_data_cart_item_interface.h
 *
 * Interface CartItemInterface
 */

#ifndef OAIQuote_data_cart_item_interface_H
#define OAIQuote_data_cart_item_interface_H

#include <QJsonObject>

#include "OAIQuote_data_cart_item_extension_interface.h"
#include "OAIQuote_data_product_option_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQuote_data_cart_item_extension_interface;
class OAIQuote_data_product_option_interface;

class OAIQuote_data_cart_item_interface : public OAIObject {
public:
    OAIQuote_data_cart_item_interface();
    OAIQuote_data_cart_item_interface(QString json);
    ~OAIQuote_data_cart_item_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIQuote_data_cart_item_extension_interface getExtensionAttributes() const;
    void setExtensionAttributes(const OAIQuote_data_cart_item_extension_interface &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getItemId() const;
    void setItemId(const qint32 &item_id);
    bool is_item_id_Set() const;
    bool is_item_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getPrice() const;
    void setPrice(const double &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    OAIQuote_data_product_option_interface getProductOption() const;
    void setProductOption(const OAIQuote_data_product_option_interface &product_option);
    bool is_product_option_Set() const;
    bool is_product_option_Valid() const;

    QString getProductType() const;
    void setProductType(const QString &product_type);
    bool is_product_type_Set() const;
    bool is_product_type_Valid() const;

    double getQty() const;
    void setQty(const double &qty);
    bool is_qty_Set() const;
    bool is_qty_Valid() const;

    QString getQuoteId() const;
    void setQuoteId(const QString &quote_id);
    bool is_quote_id_Set() const;
    bool is_quote_id_Valid() const;

    QString getSku() const;
    void setSku(const QString &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIQuote_data_cart_item_extension_interface m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_item_id;
    bool m_item_id_isSet;
    bool m_item_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    OAIQuote_data_product_option_interface m_product_option;
    bool m_product_option_isSet;
    bool m_product_option_isValid;

    QString m_product_type;
    bool m_product_type_isSet;
    bool m_product_type_isValid;

    double m_qty;
    bool m_qty_isSet;
    bool m_qty_isValid;

    QString m_quote_id;
    bool m_quote_id_isSet;
    bool m_quote_id_isValid;

    QString m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuote_data_cart_item_interface)

#endif // OAIQuote_data_cart_item_interface_H
