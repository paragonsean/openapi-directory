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
 * OAISales_data_invoice_creation_arguments_interface.h
 *
 * Interface for creation arguments for Invoice.
 */

#ifndef OAISales_data_invoice_creation_arguments_interface_H
#define OAISales_data_invoice_creation_arguments_interface_H

#include <QJsonObject>

#include "OAIObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISales_data_invoice_creation_arguments_interface : public OAIObject {
public:
    OAISales_data_invoice_creation_arguments_interface();
    OAISales_data_invoice_creation_arguments_interface(QString json);
    ~OAISales_data_invoice_creation_arguments_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_data_invoice_creation_arguments_interface)

#endif // OAISales_data_invoice_creation_arguments_interface_H
