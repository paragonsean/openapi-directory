/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2017-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRedisResourceProperties.h
 *
 * Parameters describing a Redis instance.
 */

#ifndef OAIRedisResourceProperties_H
#define OAIRedisResourceProperties_H

#include <QJsonObject>

#include "OAIRedisAccessKeys.h"
#include "OAIRedisLinkedServerList.h"
#include "OAISku.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRedisAccessKeys;
class OAIRedisLinkedServerList;
class OAISku;

class OAIRedisResourceProperties : public OAIObject {
public:
    OAIRedisResourceProperties();
    OAIRedisResourceProperties(QString json);
    ~OAIRedisResourceProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIRedisAccessKeys getAccessKeys() const;
    void setAccessKeys(const OAIRedisAccessKeys &access_keys);
    bool is_access_keys_Set() const;
    bool is_access_keys_Valid() const;

    QString getHostName() const;
    void setHostName(const QString &host_name);
    bool is_host_name_Set() const;
    bool is_host_name_Valid() const;

    OAIRedisLinkedServerList getLinkedServers() const;
    void setLinkedServers(const OAIRedisLinkedServerList &linked_servers);
    bool is_linked_servers_Set() const;
    bool is_linked_servers_Valid() const;

    qint32 getPort() const;
    void setPort(const qint32 &port);
    bool is_port_Set() const;
    bool is_port_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    QString getRedisVersion() const;
    void setRedisVersion(const QString &redis_version);
    bool is_redis_version_Set() const;
    bool is_redis_version_Valid() const;

    OAISku getSku() const;
    void setSku(const OAISku &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    qint32 getSslPort() const;
    void setSslPort(const qint32 &ssl_port);
    bool is_ssl_port_Set() const;
    bool is_ssl_port_Valid() const;

    bool isEnableNonSslPort() const;
    void setEnableNonSslPort(const bool &enable_non_ssl_port);
    bool is_enable_non_ssl_port_Set() const;
    bool is_enable_non_ssl_port_Valid() const;

    QMap<QString, QString> getRedisConfiguration() const;
    void setRedisConfiguration(const QMap<QString, QString> &redis_configuration);
    bool is_redis_configuration_Set() const;
    bool is_redis_configuration_Valid() const;

    qint32 getShardCount() const;
    void setShardCount(const qint32 &shard_count);
    bool is_shard_count_Set() const;
    bool is_shard_count_Valid() const;

    QString getStaticIp() const;
    void setStaticIp(const QString &static_ip);
    bool is_static_ip_Set() const;
    bool is_static_ip_Valid() const;

    QString getSubnetId() const;
    void setSubnetId(const QString &subnet_id);
    bool is_subnet_id_Set() const;
    bool is_subnet_id_Valid() const;

    QMap<QString, QString> getTenantSettings() const;
    void setTenantSettings(const QMap<QString, QString> &tenant_settings);
    bool is_tenant_settings_Set() const;
    bool is_tenant_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIRedisAccessKeys m_access_keys;
    bool m_access_keys_isSet;
    bool m_access_keys_isValid;

    QString m_host_name;
    bool m_host_name_isSet;
    bool m_host_name_isValid;

    OAIRedisLinkedServerList m_linked_servers;
    bool m_linked_servers_isSet;
    bool m_linked_servers_isValid;

    qint32 m_port;
    bool m_port_isSet;
    bool m_port_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;

    QString m_redis_version;
    bool m_redis_version_isSet;
    bool m_redis_version_isValid;

    OAISku m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    qint32 m_ssl_port;
    bool m_ssl_port_isSet;
    bool m_ssl_port_isValid;

    bool m_enable_non_ssl_port;
    bool m_enable_non_ssl_port_isSet;
    bool m_enable_non_ssl_port_isValid;

    QMap<QString, QString> m_redis_configuration;
    bool m_redis_configuration_isSet;
    bool m_redis_configuration_isValid;

    qint32 m_shard_count;
    bool m_shard_count_isSet;
    bool m_shard_count_isValid;

    QString m_static_ip;
    bool m_static_ip_isSet;
    bool m_static_ip_isValid;

    QString m_subnet_id;
    bool m_subnet_id_isSet;
    bool m_subnet_id_isValid;

    QMap<QString, QString> m_tenant_settings;
    bool m_tenant_settings_isSet;
    bool m_tenant_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRedisResourceProperties)

#endif // OAIRedisResourceProperties_H
