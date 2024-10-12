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
 * OAISales_data_order_payment_extension_interface.h
 *
 * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\OrderPaymentInterface
 */

#ifndef OAISales_data_order_payment_extension_interface_H
#define OAISales_data_order_payment_extension_interface_H

#include <QJsonObject>

#include "OAIVault_data_payment_token_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIVault_data_payment_token_interface;

class OAISales_data_order_payment_extension_interface : public OAIObject {
public:
    OAISales_data_order_payment_extension_interface();
    OAISales_data_order_payment_extension_interface(QString json);
    ~OAISales_data_order_payment_extension_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIVault_data_payment_token_interface getVaultPaymentToken() const;
    void setVaultPaymentToken(const OAIVault_data_payment_token_interface &vault_payment_token);
    bool is_vault_payment_token_Set() const;
    bool is_vault_payment_token_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIVault_data_payment_token_interface m_vault_payment_token;
    bool m_vault_payment_token_isSet;
    bool m_vault_payment_token_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISales_data_order_payment_extension_interface)

#endif // OAISales_data_order_payment_extension_interface_H
