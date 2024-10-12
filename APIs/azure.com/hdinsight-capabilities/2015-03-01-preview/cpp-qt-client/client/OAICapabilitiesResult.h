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
 * OAICapabilitiesResult.h
 *
 * The Get Capabilities operation response.
 */

#ifndef OAICapabilitiesResult_H
#define OAICapabilitiesResult_H

#include <QJsonObject>

#include "OAIQuotaCapability.h"
#include "OAIRegionsCapability.h"
#include "OAIVersionsCapability.h"
#include "OAIVmSizeCompatibilityFilter.h"
#include "OAIVmSizesCapability.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQuotaCapability;
class OAIRegionsCapability;
class OAIVersionsCapability;
class OAIVmSizeCompatibilityFilter;
class OAIVmSizesCapability;

class OAICapabilitiesResult : public OAIObject {
public:
    OAICapabilitiesResult();
    OAICapabilitiesResult(QString json);
    ~OAICapabilitiesResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getFeatures() const;
    void setFeatures(const QList<QString> &features);
    bool is_features_Set() const;
    bool is_features_Valid() const;

    OAIQuotaCapability getQuota() const;
    void setQuota(const OAIQuotaCapability &quota);
    bool is_quota_Set() const;
    bool is_quota_Valid() const;

    QMap<QString, OAIRegionsCapability> getRegions() const;
    void setRegions(const QMap<QString, OAIRegionsCapability> &regions);
    bool is_regions_Set() const;
    bool is_regions_Valid() const;

    QMap<QString, OAIVersionsCapability> getVersions() const;
    void setVersions(const QMap<QString, OAIVersionsCapability> &versions);
    bool is_versions_Set() const;
    bool is_versions_Valid() const;

    QList<OAIVmSizeCompatibilityFilter> getVmSizeFilters() const;
    void setVmSizeFilters(const QList<OAIVmSizeCompatibilityFilter> &vm_size_filters);
    bool is_vm_size_filters_Set() const;
    bool is_vm_size_filters_Valid() const;

    QMap<QString, OAIVmSizesCapability> getVmSizes() const;
    void setVmSizes(const QMap<QString, OAIVmSizesCapability> &vm_sizes);
    bool is_vm_sizes_Set() const;
    bool is_vm_sizes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_features;
    bool m_features_isSet;
    bool m_features_isValid;

    OAIQuotaCapability m_quota;
    bool m_quota_isSet;
    bool m_quota_isValid;

    QMap<QString, OAIRegionsCapability> m_regions;
    bool m_regions_isSet;
    bool m_regions_isValid;

    QMap<QString, OAIVersionsCapability> m_versions;
    bool m_versions_isSet;
    bool m_versions_isValid;

    QList<OAIVmSizeCompatibilityFilter> m_vm_size_filters;
    bool m_vm_size_filters_isSet;
    bool m_vm_size_filters_isValid;

    QMap<QString, OAIVmSizesCapability> m_vm_sizes;
    bool m_vm_sizes_isSet;
    bool m_vm_sizes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICapabilitiesResult)

#endif // OAICapabilitiesResult_H
