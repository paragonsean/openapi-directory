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
 * OAIGift_wrapping_data_wrapping_interface.h
 *
 * Interface WrappingInterface
 */

#ifndef OAIGift_wrapping_data_wrapping_interface_H
#define OAIGift_wrapping_data_wrapping_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGift_wrapping_data_wrapping_interface : public OAIObject {
public:
    OAIGift_wrapping_data_wrapping_interface();
    OAIGift_wrapping_data_wrapping_interface(QString json);
    ~OAIGift_wrapping_data_wrapping_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseCurrencyCode() const;
    void setBaseCurrencyCode(const QString &base_currency_code);
    bool is_base_currency_code_Set() const;
    bool is_base_currency_code_Valid() const;

    double getBasePrice() const;
    void setBasePrice(const double &base_price);
    bool is_base_price_Set() const;
    bool is_base_price_Valid() const;

    QString getDesign() const;
    void setDesign(const QString &design);
    bool is_design_Set() const;
    bool is_design_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getImageBase64Content() const;
    void setImageBase64Content(const QString &image_base64_content);
    bool is_image_base64_content_Set() const;
    bool is_image_base64_content_Valid() const;

    QString getImageName() const;
    void setImageName(const QString &image_name);
    bool is_image_name_Set() const;
    bool is_image_name_Valid() const;

    QString getImageUrl() const;
    void setImageUrl(const QString &image_url);
    bool is_image_url_Set() const;
    bool is_image_url_Valid() const;

    qint32 getStatus() const;
    void setStatus(const qint32 &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QList<qint32> getWebsiteIds() const;
    void setWebsiteIds(const QList<qint32> &website_ids);
    bool is_website_ids_Set() const;
    bool is_website_ids_Valid() const;

    qint32 getWrappingId() const;
    void setWrappingId(const qint32 &wrapping_id);
    bool is_wrapping_id_Set() const;
    bool is_wrapping_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_base_currency_code;
    bool m_base_currency_code_isSet;
    bool m_base_currency_code_isValid;

    double m_base_price;
    bool m_base_price_isSet;
    bool m_base_price_isValid;

    QString m_design;
    bool m_design_isSet;
    bool m_design_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_image_base64_content;
    bool m_image_base64_content_isSet;
    bool m_image_base64_content_isValid;

    QString m_image_name;
    bool m_image_name_isSet;
    bool m_image_name_isValid;

    QString m_image_url;
    bool m_image_url_isSet;
    bool m_image_url_isValid;

    qint32 m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QList<qint32> m_website_ids;
    bool m_website_ids_isSet;
    bool m_website_ids_isValid;

    qint32 m_wrapping_id;
    bool m_wrapping_id_isSet;
    bool m_wrapping_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGift_wrapping_data_wrapping_interface)

#endif // OAIGift_wrapping_data_wrapping_interface_H
