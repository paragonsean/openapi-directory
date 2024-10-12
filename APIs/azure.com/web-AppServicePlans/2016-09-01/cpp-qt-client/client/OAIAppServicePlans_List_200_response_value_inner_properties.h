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
 * OAIAppServicePlans_List_200_response_value_inner_properties.h
 *
 * AppServicePlan resource specific properties
 */

#ifndef OAIAppServicePlans_List_200_response_value_inner_properties_H
#define OAIAppServicePlans_List_200_response_value_inner_properties_H

#include <QJsonObject>

#include "OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile;

class OAIAppServicePlans_List_200_response_value_inner_properties : public OAIObject {
public:
    OAIAppServicePlans_List_200_response_value_inner_properties();
    OAIAppServicePlans_List_200_response_value_inner_properties(QString json);
    ~OAIAppServicePlans_List_200_response_value_inner_properties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAdminSiteName() const;
    void setAdminSiteName(const QString &admin_site_name);
    bool is_admin_site_name_Set() const;
    bool is_admin_site_name_Valid() const;

    QString getGeoRegion() const;
    void setGeoRegion(const QString &geo_region);
    bool is_geo_region_Set() const;
    bool is_geo_region_Valid() const;

    OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile getHostingEnvironmentProfile() const;
    void setHostingEnvironmentProfile(const OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile &hosting_environment_profile);
    bool is_hosting_environment_profile_Set() const;
    bool is_hosting_environment_profile_Valid() const;

    bool isIsSpot() const;
    void setIsSpot(const bool &is_spot);
    bool is_is_spot_Set() const;
    bool is_is_spot_Valid() const;

    qint32 getMaximumNumberOfWorkers() const;
    void setMaximumNumberOfWorkers(const qint32 &maximum_number_of_workers);
    bool is_maximum_number_of_workers_Set() const;
    bool is_maximum_number_of_workers_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumberOfSites() const;
    void setNumberOfSites(const qint32 &number_of_sites);
    bool is_number_of_sites_Set() const;
    bool is_number_of_sites_Valid() const;

    bool isPerSiteScaling() const;
    void setPerSiteScaling(const bool &per_site_scaling);
    bool is_per_site_scaling_Set() const;
    bool is_per_site_scaling_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    bool isReserved() const;
    void setReserved(const bool &reserved);
    bool is_reserved_Set() const;
    bool is_reserved_Valid() const;

    QString getResourceGroup() const;
    void setResourceGroup(const QString &resource_group);
    bool is_resource_group_Set() const;
    bool is_resource_group_Valid() const;

    QDateTime getSpotExpirationTime() const;
    void setSpotExpirationTime(const QDateTime &spot_expiration_time);
    bool is_spot_expiration_time_Set() const;
    bool is_spot_expiration_time_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    QString getSubscription() const;
    void setSubscription(const QString &subscription);
    bool is_subscription_Set() const;
    bool is_subscription_Valid() const;

    qint32 getTargetWorkerCount() const;
    void setTargetWorkerCount(const qint32 &target_worker_count);
    bool is_target_worker_count_Set() const;
    bool is_target_worker_count_Valid() const;

    qint32 getTargetWorkerSizeId() const;
    void setTargetWorkerSizeId(const qint32 &target_worker_size_id);
    bool is_target_worker_size_id_Set() const;
    bool is_target_worker_size_id_Valid() const;

    QString getWorkerTierName() const;
    void setWorkerTierName(const QString &worker_tier_name);
    bool is_worker_tier_name_Set() const;
    bool is_worker_tier_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_admin_site_name;
    bool m_admin_site_name_isSet;
    bool m_admin_site_name_isValid;

    QString m_geo_region;
    bool m_geo_region_isSet;
    bool m_geo_region_isValid;

    OAIAppServicePlans_List_200_response_value_inner_properties_hostingEnvironmentProfile m_hosting_environment_profile;
    bool m_hosting_environment_profile_isSet;
    bool m_hosting_environment_profile_isValid;

    bool m_is_spot;
    bool m_is_spot_isSet;
    bool m_is_spot_isValid;

    qint32 m_maximum_number_of_workers;
    bool m_maximum_number_of_workers_isSet;
    bool m_maximum_number_of_workers_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number_of_sites;
    bool m_number_of_sites_isSet;
    bool m_number_of_sites_isValid;

    bool m_per_site_scaling;
    bool m_per_site_scaling_isSet;
    bool m_per_site_scaling_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;

    bool m_reserved;
    bool m_reserved_isSet;
    bool m_reserved_isValid;

    QString m_resource_group;
    bool m_resource_group_isSet;
    bool m_resource_group_isValid;

    QDateTime m_spot_expiration_time;
    bool m_spot_expiration_time_isSet;
    bool m_spot_expiration_time_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    QString m_subscription;
    bool m_subscription_isSet;
    bool m_subscription_isValid;

    qint32 m_target_worker_count;
    bool m_target_worker_count_isSet;
    bool m_target_worker_count_isValid;

    qint32 m_target_worker_size_id;
    bool m_target_worker_size_id_isSet;
    bool m_target_worker_size_id_isValid;

    QString m_worker_tier_name;
    bool m_worker_tier_name_isSet;
    bool m_worker_tier_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_List_200_response_value_inner_properties)

#endif // OAIAppServicePlans_List_200_response_value_inner_properties_H
