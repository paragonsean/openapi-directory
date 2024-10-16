/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICrashes_getAppCrashesInfo_200_response_features.h
 *
 * 
 */

#ifndef OAICrashes_getAppCrashesInfo_200_response_features_H
#define OAICrashes_getAppCrashesInfo_200_response_features_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICrashes_getAppCrashesInfo_200_response_features : public OAIObject {
public:
    OAICrashes_getAppCrashesInfo_200_response_features();
    OAICrashes_getAppCrashesInfo_200_response_features(QString json);
    ~OAICrashes_getAppCrashesInfo_200_response_features() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCrashDownloadRaw() const;
    void setCrashDownloadRaw(const bool &crash_download_raw);
    bool is_crash_download_raw_Set() const;
    bool is_crash_download_raw_Valid() const;

    bool isCrashgroupAnalyticsCrashfreeusers() const;
    void setCrashgroupAnalyticsCrashfreeusers(const bool &crashgroup_analytics_crashfreeusers);
    bool is_crashgroup_analytics_crashfreeusers_Set() const;
    bool is_crashgroup_analytics_crashfreeusers_Valid() const;

    bool isCrashgroupAnalyticsImpactedusers() const;
    void setCrashgroupAnalyticsImpactedusers(const bool &crashgroup_analytics_impactedusers);
    bool is_crashgroup_analytics_impactedusers_Set() const;
    bool is_crashgroup_analytics_impactedusers_Valid() const;

    bool isCrashgroupModifyAnnotation() const;
    void setCrashgroupModifyAnnotation(const bool &crashgroup_modify_annotation);
    bool is_crashgroup_modify_annotation_Set() const;
    bool is_crashgroup_modify_annotation_Valid() const;

    bool isCrashgroupModifyStatus() const;
    void setCrashgroupModifyStatus(const bool &crashgroup_modify_status);
    bool is_crashgroup_modify_status_Set() const;
    bool is_crashgroup_modify_status_Valid() const;

    bool isSearch() const;
    void setSearch(const bool &search);
    bool is_search_Set() const;
    bool is_search_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_crash_download_raw;
    bool m_crash_download_raw_isSet;
    bool m_crash_download_raw_isValid;

    bool m_crashgroup_analytics_crashfreeusers;
    bool m_crashgroup_analytics_crashfreeusers_isSet;
    bool m_crashgroup_analytics_crashfreeusers_isValid;

    bool m_crashgroup_analytics_impactedusers;
    bool m_crashgroup_analytics_impactedusers_isSet;
    bool m_crashgroup_analytics_impactedusers_isValid;

    bool m_crashgroup_modify_annotation;
    bool m_crashgroup_modify_annotation_isSet;
    bool m_crashgroup_modify_annotation_isValid;

    bool m_crashgroup_modify_status;
    bool m_crashgroup_modify_status_isSet;
    bool m_crashgroup_modify_status_isValid;

    bool m_search;
    bool m_search_isSet;
    bool m_search_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICrashes_getAppCrashesInfo_200_response_features)

#endif // OAICrashes_getAppCrashesInfo_200_response_features_H
