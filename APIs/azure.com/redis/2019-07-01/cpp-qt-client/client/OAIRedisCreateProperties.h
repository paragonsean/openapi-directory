/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRedisCreateProperties.h
 *
 * Properties supplied to Create Redis operation.
 */

#ifndef OAIRedisCreateProperties_H
#define OAIRedisCreateProperties_H

#include <QJsonObject>

#include "OAISku.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISku;

class OAIRedisCreateProperties : public OAIObject {
public:
    OAIRedisCreateProperties();
    OAIRedisCreateProperties(QString json);
    ~OAIRedisCreateProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISku getSku() const;
    void setSku(const OAISku &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    QString getStaticIp() const;
    void setStaticIp(const QString &static_ip);
    bool is_static_ip_Set() const;
    bool is_static_ip_Valid() const;

    QString getSubnetId() const;
    void setSubnetId(const QString &subnet_id);
    bool is_subnet_id_Set() const;
    bool is_subnet_id_Valid() const;

    bool isEnableNonSslPort() const;
    void setEnableNonSslPort(const bool &enable_non_ssl_port);
    bool is_enable_non_ssl_port_Set() const;
    bool is_enable_non_ssl_port_Valid() const;

    QString getMinimumTlsVersion() const;
    void setMinimumTlsVersion(const QString &minimum_tls_version);
    bool is_minimum_tls_version_Set() const;
    bool is_minimum_tls_version_Valid() const;

    QMap<QString, QString> getRedisConfiguration() const;
    void setRedisConfiguration(const QMap<QString, QString> &redis_configuration);
    bool is_redis_configuration_Set() const;
    bool is_redis_configuration_Valid() const;

    qint32 getReplicasPerMaster() const;
    void setReplicasPerMaster(const qint32 &replicas_per_master);
    bool is_replicas_per_master_Set() const;
    bool is_replicas_per_master_Valid() const;

    qint32 getShardCount() const;
    void setShardCount(const qint32 &shard_count);
    bool is_shard_count_Set() const;
    bool is_shard_count_Valid() const;

    QMap<QString, QString> getTenantSettings() const;
    void setTenantSettings(const QMap<QString, QString> &tenant_settings);
    bool is_tenant_settings_Set() const;
    bool is_tenant_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISku m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    QString m_static_ip;
    bool m_static_ip_isSet;
    bool m_static_ip_isValid;

    QString m_subnet_id;
    bool m_subnet_id_isSet;
    bool m_subnet_id_isValid;

    bool m_enable_non_ssl_port;
    bool m_enable_non_ssl_port_isSet;
    bool m_enable_non_ssl_port_isValid;

    QString m_minimum_tls_version;
    bool m_minimum_tls_version_isSet;
    bool m_minimum_tls_version_isValid;

    QMap<QString, QString> m_redis_configuration;
    bool m_redis_configuration_isSet;
    bool m_redis_configuration_isValid;

    qint32 m_replicas_per_master;
    bool m_replicas_per_master_isSet;
    bool m_replicas_per_master_isValid;

    qint32 m_shard_count;
    bool m_shard_count_isSet;
    bool m_shard_count_isValid;

    QMap<QString, QString> m_tenant_settings;
    bool m_tenant_settings_isSet;
    bool m_tenant_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRedisCreateProperties)

#endif // OAIRedisCreateProperties_H
