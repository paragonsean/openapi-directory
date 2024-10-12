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
 * OAIVault_data_payment_token_interface.h
 *
 * Gateway vault payment token interface.
 */

#ifndef OAIVault_data_payment_token_interface_H
#define OAIVault_data_payment_token_interface_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVault_data_payment_token_interface : public OAIObject {
public:
    OAIVault_data_payment_token_interface();
    OAIVault_data_payment_token_interface(QString json);
    ~OAIVault_data_payment_token_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    qint32 getCustomerId() const;
    void setCustomerId(const qint32 &customer_id);
    bool is_customer_id_Set() const;
    bool is_customer_id_Valid() const;

    qint32 getEntityId() const;
    void setEntityId(const qint32 &entity_id);
    bool is_entity_id_Set() const;
    bool is_entity_id_Valid() const;

    QString getExpiresAt() const;
    void setExpiresAt(const QString &expires_at);
    bool is_expires_at_Set() const;
    bool is_expires_at_Valid() const;

    QString getGatewayToken() const;
    void setGatewayToken(const QString &gateway_token);
    bool is_gateway_token_Set() const;
    bool is_gateway_token_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsVisible() const;
    void setIsVisible(const bool &is_visible);
    bool is_is_visible_Set() const;
    bool is_is_visible_Valid() const;

    QString getPaymentMethodCode() const;
    void setPaymentMethodCode(const QString &payment_method_code);
    bool is_payment_method_code_Set() const;
    bool is_payment_method_code_Valid() const;

    QString getPublicHash() const;
    void setPublicHash(const QString &public_hash);
    bool is_public_hash_Set() const;
    bool is_public_hash_Valid() const;

    QString getTokenDetails() const;
    void setTokenDetails(const QString &token_details);
    bool is_token_details_Set() const;
    bool is_token_details_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    qint32 m_customer_id;
    bool m_customer_id_isSet;
    bool m_customer_id_isValid;

    qint32 m_entity_id;
    bool m_entity_id_isSet;
    bool m_entity_id_isValid;

    QString m_expires_at;
    bool m_expires_at_isSet;
    bool m_expires_at_isValid;

    QString m_gateway_token;
    bool m_gateway_token_isSet;
    bool m_gateway_token_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_visible;
    bool m_is_visible_isSet;
    bool m_is_visible_isValid;

    QString m_payment_method_code;
    bool m_payment_method_code_isSet;
    bool m_payment_method_code_isValid;

    QString m_public_hash;
    bool m_public_hash_isSet;
    bool m_public_hash_isValid;

    QString m_token_details;
    bool m_token_details_isSet;
    bool m_token_details_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVault_data_payment_token_interface)

#endif // OAIVault_data_payment_token_interface_H
