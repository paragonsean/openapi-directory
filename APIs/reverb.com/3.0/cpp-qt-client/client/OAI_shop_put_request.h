/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_shop_put_request.h
 *
 * 
 */

#ifndef OAI_shop_put_request_H
#define OAI_shop_put_request_H

#include <QJsonObject>

#include "OAI_shop_put_request_address.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAI_shop_put_request_address;

class OAI_shop_put_request : public OAIObject {
public:
    OAI_shop_put_request();
    OAI_shop_put_request(QString json);
    ~OAI_shop_put_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAI_shop_put_request_address getAddress() const;
    void setAddress(const OAI_shop_put_request_address &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getLegalCountryCode() const;
    void setLegalCountryCode(const QString &legal_country_code);
    bool is_legal_country_code_Set() const;
    bool is_legal_country_code_Valid() const;

    bool isLegalCountryCodeConfirmed() const;
    void setLegalCountryCodeConfirmed(const bool &legal_country_code_confirmed);
    bool is_legal_country_code_confirmed_Set() const;
    bool is_legal_country_code_confirmed_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPaymentPolicy() const;
    void setPaymentPolicy(const QString &payment_policy);
    bool is_payment_policy_Set() const;
    bool is_payment_policy_Valid() const;

    QString getReturnPolicy() const;
    void setReturnPolicy(const QString &return_policy);
    bool is_return_policy_Set() const;
    bool is_return_policy_Valid() const;

    QString getShippingPolicy() const;
    void setShippingPolicy(const QString &shipping_policy);
    bool is_shipping_policy_Set() const;
    bool is_shipping_policy_Valid() const;

    QString getShopType() const;
    void setShopType(const QString &shop_type);
    bool is_shop_type_Set() const;
    bool is_shop_type_Valid() const;

    QString getWebsite() const;
    void setWebsite(const QString &website);
    bool is_website_Set() const;
    bool is_website_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAI_shop_put_request_address m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_legal_country_code;
    bool m_legal_country_code_isSet;
    bool m_legal_country_code_isValid;

    bool m_legal_country_code_confirmed;
    bool m_legal_country_code_confirmed_isSet;
    bool m_legal_country_code_confirmed_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_payment_policy;
    bool m_payment_policy_isSet;
    bool m_payment_policy_isValid;

    QString m_return_policy;
    bool m_return_policy_isSet;
    bool m_return_policy_isValid;

    QString m_shipping_policy;
    bool m_shipping_policy_isSet;
    bool m_shipping_policy_isValid;

    QString m_shop_type;
    bool m_shop_type_isSet;
    bool m_shop_type_isValid;

    QString m_website;
    bool m_website_isSet;
    bool m_website_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_shop_put_request)

#endif // OAI_shop_put_request_H
