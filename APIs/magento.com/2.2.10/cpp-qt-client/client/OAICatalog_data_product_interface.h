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
 * OAICatalog_data_product_interface.h
 *
 * 
 */

#ifndef OAICatalog_data_product_interface_H
#define OAICatalog_data_product_interface_H

#include <QJsonObject>

#include "OAICatalog_data_product_attribute_media_gallery_entry_interface.h"
#include "OAICatalog_data_product_custom_option_interface.h"
#include "OAICatalog_data_product_extension_interface.h"
#include "OAICatalog_data_product_link_interface.h"
#include "OAICatalog_data_product_tier_price_interface.h"
#include "OAIFramework_attribute_interface.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFramework_attribute_interface;
class OAICatalog_data_product_extension_interface;
class OAICatalog_data_product_attribute_media_gallery_entry_interface;
class OAICatalog_data_product_custom_option_interface;
class OAICatalog_data_product_link_interface;
class OAICatalog_data_product_tier_price_interface;

class OAICatalog_data_product_interface : public OAIObject {
public:
    OAICatalog_data_product_interface();
    OAICatalog_data_product_interface(QString json);
    ~OAICatalog_data_product_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAttributeSetId() const;
    void setAttributeSetId(const qint32 &attribute_set_id);
    bool is_attribute_set_id_Set() const;
    bool is_attribute_set_id_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QList<OAIFramework_attribute_interface> getCustomAttributes() const;
    void setCustomAttributes(const QList<OAIFramework_attribute_interface> &custom_attributes);
    bool is_custom_attributes_Set() const;
    bool is_custom_attributes_Valid() const;

    OAICatalog_data_product_extension_interface getExtensionAttributes() const;
    void setExtensionAttributes(const OAICatalog_data_product_extension_interface &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAICatalog_data_product_attribute_media_gallery_entry_interface> getMediaGalleryEntries() const;
    void setMediaGalleryEntries(const QList<OAICatalog_data_product_attribute_media_gallery_entry_interface> &media_gallery_entries);
    bool is_media_gallery_entries_Set() const;
    bool is_media_gallery_entries_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAICatalog_data_product_custom_option_interface> getOptions() const;
    void setOptions(const QList<OAICatalog_data_product_custom_option_interface> &options);
    bool is_options_Set() const;
    bool is_options_Valid() const;

    double getPrice() const;
    void setPrice(const double &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QList<OAICatalog_data_product_link_interface> getProductLinks() const;
    void setProductLinks(const QList<OAICatalog_data_product_link_interface> &product_links);
    bool is_product_links_Set() const;
    bool is_product_links_Valid() const;

    QString getSku() const;
    void setSku(const QString &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    qint32 getStatus() const;
    void setStatus(const qint32 &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<OAICatalog_data_product_tier_price_interface> getTierPrices() const;
    void setTierPrices(const QList<OAICatalog_data_product_tier_price_interface> &tier_prices);
    bool is_tier_prices_Set() const;
    bool is_tier_prices_Valid() const;

    QString getTypeId() const;
    void setTypeId(const QString &type_id);
    bool is_type_id_Set() const;
    bool is_type_id_Valid() const;

    QString getUpdatedAt() const;
    void setUpdatedAt(const QString &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    qint32 getVisibility() const;
    void setVisibility(const qint32 &visibility);
    bool is_visibility_Set() const;
    bool is_visibility_Valid() const;

    double getWeight() const;
    void setWeight(const double &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_attribute_set_id;
    bool m_attribute_set_id_isSet;
    bool m_attribute_set_id_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QList<OAIFramework_attribute_interface> m_custom_attributes;
    bool m_custom_attributes_isSet;
    bool m_custom_attributes_isValid;

    OAICatalog_data_product_extension_interface m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAICatalog_data_product_attribute_media_gallery_entry_interface> m_media_gallery_entries;
    bool m_media_gallery_entries_isSet;
    bool m_media_gallery_entries_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAICatalog_data_product_custom_option_interface> m_options;
    bool m_options_isSet;
    bool m_options_isValid;

    double m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QList<OAICatalog_data_product_link_interface> m_product_links;
    bool m_product_links_isSet;
    bool m_product_links_isValid;

    QString m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    qint32 m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<OAICatalog_data_product_tier_price_interface> m_tier_prices;
    bool m_tier_prices_isSet;
    bool m_tier_prices_isValid;

    QString m_type_id;
    bool m_type_id_isSet;
    bool m_type_id_isValid;

    QString m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    qint32 m_visibility;
    bool m_visibility_isSet;
    bool m_visibility_isValid;

    double m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_product_interface)

#endif // OAICatalog_data_product_interface_H
