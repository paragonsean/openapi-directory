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
 * OAICheckout_data_totals_information_interface.h
 *
 * Interface TotalsInformationInterface
 */

#ifndef OAICheckout_data_totals_information_interface_H
#define OAICheckout_data_totals_information_interface_H

#include <QJsonObject>

#include "OAIFramework_attribute_interface.h"
#include "OAIObject.h"
#include "OAIQuote_data_address_interface.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQuote_data_address_interface;
class OAIFramework_attribute_interface;

class OAICheckout_data_totals_information_interface : public OAIObject {
public:
    OAICheckout_data_totals_information_interface();
    OAICheckout_data_totals_information_interface(QString json);
    ~OAICheckout_data_totals_information_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIQuote_data_address_interface getAddress() const;
    void setAddress(const OAIQuote_data_address_interface &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QList<OAIFramework_attribute_interface> getCustomAttributes() const;
    void setCustomAttributes(const QList<OAIFramework_attribute_interface> &custom_attributes);
    bool is_custom_attributes_Set() const;
    bool is_custom_attributes_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    QString getShippingCarrierCode() const;
    void setShippingCarrierCode(const QString &shipping_carrier_code);
    bool is_shipping_carrier_code_Set() const;
    bool is_shipping_carrier_code_Valid() const;

    QString getShippingMethodCode() const;
    void setShippingMethodCode(const QString &shipping_method_code);
    bool is_shipping_method_code_Set() const;
    bool is_shipping_method_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIQuote_data_address_interface m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QList<OAIFramework_attribute_interface> m_custom_attributes;
    bool m_custom_attributes_isSet;
    bool m_custom_attributes_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    QString m_shipping_carrier_code;
    bool m_shipping_carrier_code_isSet;
    bool m_shipping_carrier_code_isValid;

    QString m_shipping_method_code;
    bool m_shipping_method_code_isSet;
    bool m_shipping_method_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICheckout_data_totals_information_interface)

#endif // OAICheckout_data_totals_information_interface_H
