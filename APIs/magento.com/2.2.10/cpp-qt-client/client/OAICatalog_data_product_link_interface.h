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
 * OAICatalog_data_product_link_interface.h
 *
 * 
 */

#ifndef OAICatalog_data_product_link_interface_H
#define OAICatalog_data_product_link_interface_H

#include <QJsonObject>

#include "OAICatalog_data_product_link_extension_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICatalog_data_product_link_extension_interface;

class OAICatalog_data_product_link_interface : public OAIObject {
public:
    OAICatalog_data_product_link_interface();
    OAICatalog_data_product_link_interface(QString json);
    ~OAICatalog_data_product_link_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICatalog_data_product_link_extension_interface getExtensionAttributes() const;
    void setExtensionAttributes(const OAICatalog_data_product_link_extension_interface &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getLinkType() const;
    void setLinkType(const QString &link_type);
    bool is_link_type_Set() const;
    bool is_link_type_Valid() const;

    QString getLinkedProductSku() const;
    void setLinkedProductSku(const QString &linked_product_sku);
    bool is_linked_product_sku_Set() const;
    bool is_linked_product_sku_Valid() const;

    QString getLinkedProductType() const;
    void setLinkedProductType(const QString &linked_product_type);
    bool is_linked_product_type_Set() const;
    bool is_linked_product_type_Valid() const;

    qint32 getPosition() const;
    void setPosition(const qint32 &position);
    bool is_position_Set() const;
    bool is_position_Valid() const;

    QString getSku() const;
    void setSku(const QString &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICatalog_data_product_link_extension_interface m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_link_type;
    bool m_link_type_isSet;
    bool m_link_type_isValid;

    QString m_linked_product_sku;
    bool m_linked_product_sku_isSet;
    bool m_linked_product_sku_isValid;

    QString m_linked_product_type;
    bool m_linked_product_type_isSet;
    bool m_linked_product_type_isValid;

    qint32 m_position;
    bool m_position_isSet;
    bool m_position_isValid;

    QString m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_product_link_interface)

#endif // OAICatalog_data_product_link_interface_H
