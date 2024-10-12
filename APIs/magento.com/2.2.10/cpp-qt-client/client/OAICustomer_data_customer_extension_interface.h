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
 * OAICustomer_data_customer_extension_interface.h
 *
 * ExtensionInterface class for @see \\Magento\\Customer\\Api\\Data\\CustomerInterface
 */

#ifndef OAICustomer_data_customer_extension_interface_H
#define OAICustomer_data_customer_extension_interface_H

#include <QJsonObject>

#include "OAICompany_data_company_customer_interface.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICompany_data_company_customer_interface;

class OAICustomer_data_customer_extension_interface : public OAIObject {
public:
    OAICustomer_data_customer_extension_interface();
    OAICustomer_data_customer_extension_interface(QString json);
    ~OAICustomer_data_customer_extension_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAmazonId() const;
    void setAmazonId(const QString &amazon_id);
    bool is_amazon_id_Set() const;
    bool is_amazon_id_Valid() const;

    OAICompany_data_company_customer_interface getCompanyAttributes() const;
    void setCompanyAttributes(const OAICompany_data_company_customer_interface &company_attributes);
    bool is_company_attributes_Set() const;
    bool is_company_attributes_Valid() const;

    bool isIsSubscribed() const;
    void setIsSubscribed(const bool &is_subscribed);
    bool is_is_subscribed_Set() const;
    bool is_is_subscribed_Valid() const;

    QString getVertexCustomerCode() const;
    void setVertexCustomerCode(const QString &vertex_customer_code);
    bool is_vertex_customer_code_Set() const;
    bool is_vertex_customer_code_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_amazon_id;
    bool m_amazon_id_isSet;
    bool m_amazon_id_isValid;

    OAICompany_data_company_customer_interface m_company_attributes;
    bool m_company_attributes_isSet;
    bool m_company_attributes_isValid;

    bool m_is_subscribed;
    bool m_is_subscribed_isSet;
    bool m_is_subscribed_isValid;

    QString m_vertex_customer_code;
    bool m_vertex_customer_code_isSet;
    bool m_vertex_customer_code_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomer_data_customer_extension_interface)

#endif // OAICustomer_data_customer_extension_interface_H
