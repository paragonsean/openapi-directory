/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIValidateProperties.h
 *
 * App properties used for validation.
 */

#ifndef OAIValidateProperties_H
#define OAIValidateProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIValidateProperties : public OAIObject {
public:
    OAIValidateProperties();
    OAIValidateProperties(QString json);
    ~OAIValidateProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCapacity() const;
    void setCapacity(const qint32 &capacity);
    bool is_capacity_Set() const;
    bool is_capacity_Valid() const;

    QString getContainerImagePlatform() const;
    void setContainerImagePlatform(const QString &container_image_platform);
    bool is_container_image_platform_Set() const;
    bool is_container_image_platform_Valid() const;

    QString getContainerImageRepository() const;
    void setContainerImageRepository(const QString &container_image_repository);
    bool is_container_image_repository_Set() const;
    bool is_container_image_repository_Valid() const;

    QString getContainerImageTag() const;
    void setContainerImageTag(const QString &container_image_tag);
    bool is_container_image_tag_Set() const;
    bool is_container_image_tag_Valid() const;

    QString getContainerRegistryBaseUrl() const;
    void setContainerRegistryBaseUrl(const QString &container_registry_base_url);
    bool is_container_registry_base_url_Set() const;
    bool is_container_registry_base_url_Valid() const;

    QString getContainerRegistryPassword() const;
    void setContainerRegistryPassword(const QString &container_registry_password);
    bool is_container_registry_password_Set() const;
    bool is_container_registry_password_Valid() const;

    QString getContainerRegistryUsername() const;
    void setContainerRegistryUsername(const QString &container_registry_username);
    bool is_container_registry_username_Set() const;
    bool is_container_registry_username_Valid() const;

    QString getHostingEnvironment() const;
    void setHostingEnvironment(const QString &hosting_environment);
    bool is_hosting_environment_Set() const;
    bool is_hosting_environment_Valid() const;

    bool isIsSpot() const;
    void setIsSpot(const bool &is_spot);
    bool is_is_spot_Set() const;
    bool is_is_spot_Valid() const;

    bool isIsXenon() const;
    void setIsXenon(const bool &is_xenon);
    bool is_is_xenon_Set() const;
    bool is_is_xenon_Valid() const;

    bool isNeedLinuxWorkers() const;
    void setNeedLinuxWorkers(const bool &need_linux_workers);
    bool is_need_linux_workers_Set() const;
    bool is_need_linux_workers_Valid() const;

    QString getServerFarmId() const;
    void setServerFarmId(const QString &server_farm_id);
    bool is_server_farm_id_Set() const;
    bool is_server_farm_id_Valid() const;

    QString getSkuName() const;
    void setSkuName(const QString &sku_name);
    bool is_sku_name_Set() const;
    bool is_sku_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_capacity;
    bool m_capacity_isSet;
    bool m_capacity_isValid;

    QString m_container_image_platform;
    bool m_container_image_platform_isSet;
    bool m_container_image_platform_isValid;

    QString m_container_image_repository;
    bool m_container_image_repository_isSet;
    bool m_container_image_repository_isValid;

    QString m_container_image_tag;
    bool m_container_image_tag_isSet;
    bool m_container_image_tag_isValid;

    QString m_container_registry_base_url;
    bool m_container_registry_base_url_isSet;
    bool m_container_registry_base_url_isValid;

    QString m_container_registry_password;
    bool m_container_registry_password_isSet;
    bool m_container_registry_password_isValid;

    QString m_container_registry_username;
    bool m_container_registry_username_isSet;
    bool m_container_registry_username_isValid;

    QString m_hosting_environment;
    bool m_hosting_environment_isSet;
    bool m_hosting_environment_isValid;

    bool m_is_spot;
    bool m_is_spot_isSet;
    bool m_is_spot_isValid;

    bool m_is_xenon;
    bool m_is_xenon_isSet;
    bool m_is_xenon_isValid;

    bool m_need_linux_workers;
    bool m_need_linux_workers_isSet;
    bool m_need_linux_workers_isValid;

    QString m_server_farm_id;
    bool m_server_farm_id_isSet;
    bool m_server_farm_id_isValid;

    QString m_sku_name;
    bool m_sku_name_isSet;
    bool m_sku_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIValidateProperties)

#endif // OAIValidateProperties_H
