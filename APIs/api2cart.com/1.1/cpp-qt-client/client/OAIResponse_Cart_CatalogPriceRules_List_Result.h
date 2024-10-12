/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResponse_Cart_CatalogPriceRules_List_Result.h
 *
 * 
 */

#ifndef OAIResponse_Cart_CatalogPriceRules_List_Result_H
#define OAIResponse_Cart_CatalogPriceRules_List_Result_H

#include <QJsonObject>

#include "OAICatalogPriceRule.h"
#include "OAIObject.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICatalogPriceRule;

class OAIResponse_Cart_CatalogPriceRules_List_Result : public OAIObject {
public:
    OAIResponse_Cart_CatalogPriceRules_List_Result();
    OAIResponse_Cart_CatalogPriceRules_List_Result(QString json);
    ~OAIResponse_Cart_CatalogPriceRules_List_Result() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QList<OAICatalogPriceRule> getCatalogPriceRules() const;
    void setCatalogPriceRules(const QList<OAICatalogPriceRule> &catalog_price_rules);
    bool is_catalog_price_rules_Set() const;
    bool is_catalog_price_rules_Valid() const;

    qint32 getCatalogPriceRulesCount() const;
    void setCatalogPriceRulesCount(const qint32 &catalog_price_rules_count);
    bool is_catalog_price_rules_count_Set() const;
    bool is_catalog_price_rules_count_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QList<OAICatalogPriceRule> m_catalog_price_rules;
    bool m_catalog_price_rules_isSet;
    bool m_catalog_price_rules_isValid;

    qint32 m_catalog_price_rules_count;
    bool m_catalog_price_rules_count_isSet;
    bool m_catalog_price_rules_count_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResponse_Cart_CatalogPriceRules_List_Result)

#endif // OAIResponse_Cart_CatalogPriceRules_List_Result_H
