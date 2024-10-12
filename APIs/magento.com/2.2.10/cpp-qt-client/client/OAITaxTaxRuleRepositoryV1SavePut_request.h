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
 * OAITaxTaxRuleRepositoryV1SavePut_request.h
 *
 * 
 */

#ifndef OAITaxTaxRuleRepositoryV1SavePut_request_H
#define OAITaxTaxRuleRepositoryV1SavePut_request_H

#include <QJsonObject>

#include "OAITax_data_tax_rule_interface.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITax_data_tax_rule_interface;

class OAITaxTaxRuleRepositoryV1SavePut_request : public OAIObject {
public:
    OAITaxTaxRuleRepositoryV1SavePut_request();
    OAITaxTaxRuleRepositoryV1SavePut_request(QString json);
    ~OAITaxTaxRuleRepositoryV1SavePut_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAITax_data_tax_rule_interface getRule() const;
    void setRule(const OAITax_data_tax_rule_interface &rule);
    bool is_rule_Set() const;
    bool is_rule_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAITax_data_tax_rule_interface m_rule;
    bool m_rule_isSet;
    bool m_rule_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITaxTaxRuleRepositoryV1SavePut_request)

#endif // OAITaxTaxRuleRepositoryV1SavePut_request_H
