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
 * OAIProductVariantUpdate.h
 *
 * 
 */

#ifndef OAIProductVariantUpdate_H
#define OAIProductVariantUpdate_H

#include <QJsonObject>

#include "OAIProductVariantUpdate_options_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProductVariantUpdate_options_inner;

class OAIProductVariantUpdate : public OAIObject {
public:
    OAIProductVariantUpdate();
    OAIProductVariantUpdate(QString json);
    ~OAIProductVariantUpdate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAvailableForSale() const;
    void setAvailableForSale(const bool &available_for_sale);
    bool is_available_for_sale_Set() const;
    bool is_available_for_sale_Valid() const;

    QString getBackorderStatus() const;
    void setBackorderStatus(const QString &backorder_status);
    bool is_backorder_status_Set() const;
    bool is_backorder_status_Valid() const;

    QString getBarcode() const;
    void setBarcode(const QString &barcode);
    bool is_barcode_Set() const;
    bool is_barcode_Valid() const;

    bool isClearCache() const;
    void setClearCache(const bool &clear_cache);
    bool is_clear_cache_Set() const;
    bool is_clear_cache_Valid() const;

    double getCostPrice() const;
    void setCostPrice(const double &cost_price);
    bool is_cost_price_Set() const;
    bool is_cost_price_Valid() const;

    QString getCountryOfOrigin() const;
    void setCountryOfOrigin(const QString &country_of_origin);
    bool is_country_of_origin_Set() const;
    bool is_country_of_origin_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getGtin() const;
    void setGtin(const QString &gtin);
    bool is_gtin_Set() const;
    bool is_gtin_Valid() const;

    QString getHarmonizedSystemCode() const;
    void setHarmonizedSystemCode(const QString &harmonized_system_code);
    bool is_harmonized_system_code_Set() const;
    bool is_harmonized_system_code_Valid() const;

    double getHeight() const;
    void setHeight(const double &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isInStock() const;
    void setInStock(const bool &in_stock);
    bool is_in_stock_Set() const;
    bool is_in_stock_Valid() const;

    double getIncreaseQuantity() const;
    void setIncreaseQuantity(const double &increase_quantity);
    bool is_increase_quantity_Set() const;
    bool is_increase_quantity_Valid() const;

    QString getLangId() const;
    void setLangId(const QString &lang_id);
    bool is_lang_id_Set() const;
    bool is_lang_id_Valid() const;

    double getLength() const;
    void setLength(const double &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    bool isManageStock() const;
    void setManageStock(const bool &manage_stock);
    bool is_manage_stock_Set() const;
    bool is_manage_stock_Valid() const;

    QString getMetaDescription() const;
    void setMetaDescription(const QString &meta_description);
    bool is_meta_description_Set() const;
    bool is_meta_description_Valid() const;

    QString getMetaKeywords() const;
    void setMetaKeywords(const QString &meta_keywords);
    bool is_meta_keywords_Set() const;
    bool is_meta_keywords_Valid() const;

    QString getMetaTitle() const;
    void setMetaTitle(const QString &meta_title);
    bool is_meta_title_Set() const;
    bool is_meta_title_Valid() const;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getOldPrice() const;
    void setOldPrice(const double &old_price);
    bool is_old_price_Set() const;
    bool is_old_price_Valid() const;

    QList<OAIProductVariantUpdate_options_inner> getOptions() const;
    void setOptions(const QList<OAIProductVariantUpdate_options_inner> &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    double getPrice() const;
    void setPrice(const double &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getProductId() const;
    void setProductId(const QString &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    double getQuantity() const;
    void setQuantity(const double &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    double getReduceQuantity() const;
    void setReduceQuantity(const double &reduce_quantity);
    bool is_reduce_quantity_Set() const;
    bool is_reduce_quantity_Valid() const;

    bool isReindex() const;
    void setReindex(const bool &reindex);
    bool is_reindex_Set() const;
    bool is_reindex_Valid() const;

    double getReserveQuantity() const;
    void setReserveQuantity(const double &reserve_quantity);
    bool is_reserve_quantity_Set() const;
    bool is_reserve_quantity_Valid() const;

    double getRetailPrice() const;
    void setRetailPrice(const double &retail_price);
    bool is_retail_price_Set() const;
    bool is_retail_price_Valid() const;

    QString getShortDescription() const;
    void setShortDescription(const QString &short_description);
    bool is_short_description_Set() const;
    bool is_short_description_Valid() const;

    QString getSku() const;
    void setSku(const QString &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    double getSpecialPrice() const;
    void setSpecialPrice(const double &special_price);
    bool is_special_price_Set() const;
    bool is_special_price_Valid() const;

    QString getSpriceCreate() const;
    void setSpriceCreate(const QString &sprice_create);
    bool is_sprice_create_Set() const;
    bool is_sprice_create_Valid() const;

    QString getSpriceExpire() const;
    void setSpriceExpire(const QString &sprice_expire);
    bool is_sprice_expire_Set() const;
    bool is_sprice_expire_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    bool isTaxable() const;
    void setTaxable(const bool &taxable);
    bool is_taxable_Set() const;
    bool is_taxable_Valid() const;

    QString getVisible() const;
    void setVisible(const QString &visible);
    bool is_visible_Set() const;
    bool is_visible_Valid() const;

    QString getWarehouseId() const;
    void setWarehouseId(const QString &warehouse_id);
    bool is_warehouse_id_Set() const;
    bool is_warehouse_id_Valid() const;

    double getWeight() const;
    void setWeight(const double &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    double getWidth() const;
    void setWidth(const double &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_available_for_sale;
    bool m_available_for_sale_isSet;
    bool m_available_for_sale_isValid;

    QString m_backorder_status;
    bool m_backorder_status_isSet;
    bool m_backorder_status_isValid;

    QString m_barcode;
    bool m_barcode_isSet;
    bool m_barcode_isValid;

    bool m_clear_cache;
    bool m_clear_cache_isSet;
    bool m_clear_cache_isValid;

    double m_cost_price;
    bool m_cost_price_isSet;
    bool m_cost_price_isValid;

    QString m_country_of_origin;
    bool m_country_of_origin_isSet;
    bool m_country_of_origin_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_gtin;
    bool m_gtin_isSet;
    bool m_gtin_isValid;

    QString m_harmonized_system_code;
    bool m_harmonized_system_code_isSet;
    bool m_harmonized_system_code_isValid;

    double m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_in_stock;
    bool m_in_stock_isSet;
    bool m_in_stock_isValid;

    double m_increase_quantity;
    bool m_increase_quantity_isSet;
    bool m_increase_quantity_isValid;

    QString m_lang_id;
    bool m_lang_id_isSet;
    bool m_lang_id_isValid;

    double m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    bool m_manage_stock;
    bool m_manage_stock_isSet;
    bool m_manage_stock_isValid;

    QString m_meta_description;
    bool m_meta_description_isSet;
    bool m_meta_description_isValid;

    QString m_meta_keywords;
    bool m_meta_keywords_isSet;
    bool m_meta_keywords_isValid;

    QString m_meta_title;
    bool m_meta_title_isSet;
    bool m_meta_title_isValid;

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_old_price;
    bool m_old_price_isSet;
    bool m_old_price_isValid;

    QList<OAIProductVariantUpdate_options_inner> m_options;
    bool m_options_isSet;
    bool m_options_isValid;

    double m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;

    double m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    double m_reduce_quantity;
    bool m_reduce_quantity_isSet;
    bool m_reduce_quantity_isValid;

    bool m_reindex;
    bool m_reindex_isSet;
    bool m_reindex_isValid;

    double m_reserve_quantity;
    bool m_reserve_quantity_isSet;
    bool m_reserve_quantity_isValid;

    double m_retail_price;
    bool m_retail_price_isSet;
    bool m_retail_price_isValid;

    QString m_short_description;
    bool m_short_description_isSet;
    bool m_short_description_isValid;

    QString m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    double m_special_price;
    bool m_special_price_isSet;
    bool m_special_price_isValid;

    QString m_sprice_create;
    bool m_sprice_create_isSet;
    bool m_sprice_create_isValid;

    QString m_sprice_expire;
    bool m_sprice_expire_isSet;
    bool m_sprice_expire_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    bool m_taxable;
    bool m_taxable_isSet;
    bool m_taxable_isValid;

    QString m_visible;
    bool m_visible_isSet;
    bool m_visible_isValid;

    QString m_warehouse_id;
    bool m_warehouse_id_isSet;
    bool m_warehouse_id_isValid;

    double m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;

    double m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductVariantUpdate)

#endif // OAIProductVariantUpdate_H
