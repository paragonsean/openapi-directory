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
 * OAICatalog_data_product_render_formatted_price_info_interface.h
 *
 * Formatted Price interface. Aggregate formatted html with price representations. E.g.: &lt;span class&#x3D;\&quot;price\&quot;&gt;$9.00&lt;/span&gt; Consider currency, rounding and html
 */

#ifndef OAICatalog_data_product_render_formatted_price_info_interface_H
#define OAICatalog_data_product_render_formatted_price_info_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICatalog_data_product_render_formatted_price_info_interface : public OAIObject {
public:
    OAICatalog_data_product_render_formatted_price_info_interface();
    OAICatalog_data_product_render_formatted_price_info_interface(QString json);
    ~OAICatalog_data_product_render_formatted_price_info_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getFinalPrice() const;
    void setFinalPrice(const QString &final_price);
    bool is_final_price_Set() const;
    bool is_final_price_Valid() const;

    QString getMaxPrice() const;
    void setMaxPrice(const QString &max_price);
    bool is_max_price_Set() const;
    bool is_max_price_Valid() const;

    QString getMaxRegularPrice() const;
    void setMaxRegularPrice(const QString &max_regular_price);
    bool is_max_regular_price_Set() const;
    bool is_max_regular_price_Valid() const;

    QString getMinimalPrice() const;
    void setMinimalPrice(const QString &minimal_price);
    bool is_minimal_price_Set() const;
    bool is_minimal_price_Valid() const;

    QString getMinimalRegularPrice() const;
    void setMinimalRegularPrice(const QString &minimal_regular_price);
    bool is_minimal_regular_price_Set() const;
    bool is_minimal_regular_price_Valid() const;

    QString getRegularPrice() const;
    void setRegularPrice(const QString &regular_price);
    bool is_regular_price_Set() const;
    bool is_regular_price_Valid() const;

    QString getSpecialPrice() const;
    void setSpecialPrice(const QString &special_price);
    bool is_special_price_Set() const;
    bool is_special_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_final_price;
    bool m_final_price_isSet;
    bool m_final_price_isValid;

    QString m_max_price;
    bool m_max_price_isSet;
    bool m_max_price_isValid;

    QString m_max_regular_price;
    bool m_max_regular_price_isSet;
    bool m_max_regular_price_isValid;

    QString m_minimal_price;
    bool m_minimal_price_isSet;
    bool m_minimal_price_isValid;

    QString m_minimal_regular_price;
    bool m_minimal_regular_price_isSet;
    bool m_minimal_regular_price_isValid;

    QString m_regular_price;
    bool m_regular_price_isSet;
    bool m_regular_price_isValid;

    QString m_special_price;
    bool m_special_price_isSet;
    bool m_special_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_product_render_formatted_price_info_interface)

#endif // OAICatalog_data_product_render_formatted_price_info_interface_H
