/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISkuInfos.h
 *
 * Collection of SKU information.
 */

#ifndef OAISkuInfos_H
#define OAISkuInfos_H

#include <QJsonObject>

#include "OAIGlobalCsmSkuDescription.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGlobalCsmSkuDescription;

class OAISkuInfos : public OAIObject {
public:
    OAISkuInfos();
    OAISkuInfos(QString json);
    ~OAISkuInfos() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getResourceType() const;
    void setResourceType(const QString &resource_type);
    bool is_resource_type_Set() const;
    bool is_resource_type_Valid() const;

    QList<OAIGlobalCsmSkuDescription> getSkus() const;
    void setSkus(const QList<OAIGlobalCsmSkuDescription> &skus);
    bool is_skus_Set() const;
    bool is_skus_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_resource_type;
    bool m_resource_type_isSet;
    bool m_resource_type_isValid;

    QList<OAIGlobalCsmSkuDescription> m_skus;
    bool m_skus_isSet;
    bool m_skus_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISkuInfos)

#endif // OAISkuInfos_H
