/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2015-03-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQuotaCapability.h
 *
 * The regional quota capability.
 */

#ifndef OAIQuotaCapability_H
#define OAIQuotaCapability_H

#include <QJsonObject>

#include "OAIRegionalQuotaCapability.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRegionalQuotaCapability;

class OAIQuotaCapability : public OAIObject {
public:
    OAIQuotaCapability();
    OAIQuotaCapability(QString json);
    ~OAIQuotaCapability() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIRegionalQuotaCapability> getRegionalQuotas() const;
    void setRegionalQuotas(const QList<OAIRegionalQuotaCapability> &regional_quotas);
    bool is_regional_quotas_Set() const;
    bool is_regional_quotas_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIRegionalQuotaCapability> m_regional_quotas;
    bool m_regional_quotas_isSet;
    bool m_regional_quotas_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuotaCapability)

#endif // OAIQuotaCapability_H
