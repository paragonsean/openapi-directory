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
 * OAICatalog_data_product_render_extension_interface.h
 *
 * ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRenderInterface
 */

#ifndef OAICatalog_data_product_render_extension_interface_H
#define OAICatalog_data_product_render_extension_interface_H

#include <QJsonObject>

#include "OAICatalog_data_product_render_button_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICatalog_data_product_render_button_interface;

class OAICatalog_data_product_render_extension_interface : public OAIObject {
public:
    OAICatalog_data_product_render_extension_interface();
    OAICatalog_data_product_render_extension_interface(QString json);
    ~OAICatalog_data_product_render_extension_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getReviewHtml() const;
    void setReviewHtml(const QString &review_html);
    bool is_review_html_Set() const;
    bool is_review_html_Valid() const;

    OAICatalog_data_product_render_button_interface getWishlistButton() const;
    void setWishlistButton(const OAICatalog_data_product_render_button_interface &wishlist_button);
    bool is_wishlist_button_Set() const;
    bool is_wishlist_button_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_review_html;
    bool m_review_html_isSet;
    bool m_review_html_isValid;

    OAICatalog_data_product_render_button_interface m_wishlist_button;
    bool m_wishlist_button_isSet;
    bool m_wishlist_button_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_product_render_extension_interface)

#endif // OAICatalog_data_product_render_extension_interface_H
