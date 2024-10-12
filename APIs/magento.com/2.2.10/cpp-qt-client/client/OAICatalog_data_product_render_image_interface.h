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
 * OAICatalog_data_product_render_image_interface.h
 *
 * Product Render image interface. Represents physical characteristics of image, that can be used in product listing or product view
 */

#ifndef OAICatalog_data_product_render_image_interface_H
#define OAICatalog_data_product_render_image_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICatalog_data_product_render_image_interface : public OAIObject {
public:
    OAICatalog_data_product_render_image_interface();
    OAICatalog_data_product_render_image_interface(QString json);
    ~OAICatalog_data_product_render_image_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    double getHeight() const;
    void setHeight(const double &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    double getResizedHeight() const;
    void setResizedHeight(const double &resized_height);
    bool is_resized_height_Set() const;
    bool is_resized_height_Valid() const;

    double getResizedWidth() const;
    void setResizedWidth(const double &resized_width);
    bool is_resized_width_Set() const;
    bool is_resized_width_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    double getWidth() const;
    void setWidth(const double &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    double m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    double m_resized_height;
    bool m_resized_height_isSet;
    bool m_resized_height_isValid;

    double m_resized_width;
    bool m_resized_width_isSet;
    bool m_resized_width_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    double m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_product_render_image_interface)

#endif // OAICatalog_data_product_render_image_interface_H
