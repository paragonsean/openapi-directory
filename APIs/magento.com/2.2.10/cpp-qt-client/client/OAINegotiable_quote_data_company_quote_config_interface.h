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
 * OAINegotiable_quote_data_company_quote_config_interface.h
 *
 * Interface CompanyQuoteConfigInterface
 */

#ifndef OAINegotiable_quote_data_company_quote_config_interface_H
#define OAINegotiable_quote_data_company_quote_config_interface_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINegotiable_quote_data_company_quote_config_interface : public OAIObject {
public:
    OAINegotiable_quote_data_company_quote_config_interface();
    OAINegotiable_quote_data_company_quote_config_interface(QString json);
    ~OAINegotiable_quote_data_company_quote_config_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCompanyId() const;
    void setCompanyId(const QString &company_id);
    bool is_company_id_Set() const;
    bool is_company_id_Valid() const;

    OAIObject getExtensionAttributes() const;
    void setExtensionAttributes(const OAIObject &extension_attributes);
    bool is_extension_attributes_Set() const;
    bool is_extension_attributes_Valid() const;

    bool isIsQuoteEnabled() const;
    void setIsQuoteEnabled(const bool &is_quote_enabled);
    bool is_is_quote_enabled_Set() const;
    bool is_is_quote_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_company_id;
    bool m_company_id_isSet;
    bool m_company_id_isValid;

    OAIObject m_extension_attributes;
    bool m_extension_attributes_isSet;
    bool m_extension_attributes_isValid;

    bool m_is_quote_enabled;
    bool m_is_quote_enabled_isSet;
    bool m_is_quote_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINegotiable_quote_data_company_quote_config_interface)

#endif // OAINegotiable_quote_data_company_quote_config_interface_H
