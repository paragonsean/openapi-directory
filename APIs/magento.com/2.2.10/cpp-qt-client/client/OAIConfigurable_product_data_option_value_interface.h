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
 * OAIConfigurable_product_data_option_value_interface.h
 *
 * Interface OptionValueInterface
 */

#ifndef OAIConfigurable_product_data_option_value_interface_H
#define OAIConfigurable_product_data_option_value_interface_H

#include <QJsonObject>

#include "OAIObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIConfigurable_product_data_option_value_interface : public OAIObject {
public:
    OAIConfigurable_product_data_option_value_interface();
    OAIConfigurable_product_data_option_value_interface(QString json);
    ~OAIConfigurable_product_data_option_value_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    qint32 getValueIndex() const;
    void setValueIndex(const qint32 &value_index);
    bool is_value_index_Set() const;
    bool is_value_index_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    qint32 m_value_index;
    bool m_value_index_isSet;
    bool m_value_index_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigurable_product_data_option_value_interface)

#endif // OAIConfigurable_product_data_option_value_interface_H
