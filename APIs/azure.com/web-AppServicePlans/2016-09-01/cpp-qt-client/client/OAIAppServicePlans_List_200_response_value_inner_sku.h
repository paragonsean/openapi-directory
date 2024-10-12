/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_List_200_response_value_inner_sku.h
 *
 * Description of a SKU for a scalable resource.
 */

#ifndef OAIAppServicePlans_List_200_response_value_inner_sku_H
#define OAIAppServicePlans_List_200_response_value_inner_sku_H

#include <QJsonObject>

#include "OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner.h"
#include "OAIAppServicePlans_List_200_response_value_inner_sku_skuCapacity.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner;
class OAIAppServicePlans_List_200_response_value_inner_sku_skuCapacity;

class OAIAppServicePlans_List_200_response_value_inner_sku : public OAIObject {
public:
    OAIAppServicePlans_List_200_response_value_inner_sku();
    OAIAppServicePlans_List_200_response_value_inner_sku(QString json);
    ~OAIAppServicePlans_List_200_response_value_inner_sku() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner> getCapabilities() const;
    void setCapabilities(const QList<OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner> &capabilities);
    bool is_capabilities_Set() const;
    bool is_capabilities_Valid() const;

    qint32 getCapacity() const;
    void setCapacity(const qint32 &capacity);
    bool is_capacity_Set() const;
    bool is_capacity_Valid() const;

    QString getFamily() const;
    void setFamily(const QString &family);
    bool is_family_Set() const;
    bool is_family_Valid() const;

    QList<QString> getLocations() const;
    void setLocations(const QList<QString> &locations);
    bool is_locations_Set() const;
    bool is_locations_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSize() const;
    void setSize(const QString &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    OAIAppServicePlans_List_200_response_value_inner_sku_skuCapacity getSkuCapacity() const;
    void setSkuCapacity(const OAIAppServicePlans_List_200_response_value_inner_sku_skuCapacity &sku_capacity);
    bool is_sku_capacity_Set() const;
    bool is_sku_capacity_Valid() const;

    QString getTier() const;
    void setTier(const QString &tier);
    bool is_tier_Set() const;
    bool is_tier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAppServicePlans_List_200_response_value_inner_sku_capabilities_inner> m_capabilities;
    bool m_capabilities_isSet;
    bool m_capabilities_isValid;

    qint32 m_capacity;
    bool m_capacity_isSet;
    bool m_capacity_isValid;

    QString m_family;
    bool m_family_isSet;
    bool m_family_isValid;

    QList<QString> m_locations;
    bool m_locations_isSet;
    bool m_locations_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    OAIAppServicePlans_List_200_response_value_inner_sku_skuCapacity m_sku_capacity;
    bool m_sku_capacity_isSet;
    bool m_sku_capacity_isValid;

    QString m_tier;
    bool m_tier_isSet;
    bool m_tier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_List_200_response_value_inner_sku)

#endif // OAIAppServicePlans_List_200_response_value_inner_sku_H
