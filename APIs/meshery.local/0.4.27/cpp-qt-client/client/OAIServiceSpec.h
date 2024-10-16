/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIServiceSpec.h
 *
 * 
 */

#ifndef OAIServiceSpec_H
#define OAIServiceSpec_H

#include <QJsonObject>

#include "OAIServicePort.h"
#include "OAISessionAffinityConfig.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIServicePort;
class OAISessionAffinityConfig;

class OAIServiceSpec : public OAIObject {
public:
    OAIServiceSpec();
    OAIServiceSpec(QString json);
    ~OAIServiceSpec() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClusterIp() const;
    void setClusterIp(const QString &cluster_ip);
    bool is_cluster_ip_Set() const;
    bool is_cluster_ip_Valid() const;

    QList<QString> getExternalIps() const;
    void setExternalIps(const QList<QString> &external_ips);
    bool is_external_ips_Set() const;
    bool is_external_ips_Valid() const;

    QString getExternalName() const;
    void setExternalName(const QString &external_name);
    bool is_external_name_Set() const;
    bool is_external_name_Valid() const;

    QString getExternalTrafficPolicy() const;
    void setExternalTrafficPolicy(const QString &external_traffic_policy);
    bool is_external_traffic_policy_Set() const;
    bool is_external_traffic_policy_Valid() const;

    qint32 getHealthCheckNodePort() const;
    void setHealthCheckNodePort(const qint32 &health_check_node_port);
    bool is_health_check_node_port_Set() const;
    bool is_health_check_node_port_Valid() const;

    QString getIpFamily() const;
    void setIpFamily(const QString &ip_family);
    bool is_ip_family_Set() const;
    bool is_ip_family_Valid() const;

    QString getLoadBalancerIp() const;
    void setLoadBalancerIp(const QString &load_balancer_ip);
    bool is_load_balancer_ip_Set() const;
    bool is_load_balancer_ip_Valid() const;

    QList<QString> getLoadBalancerSourceRanges() const;
    void setLoadBalancerSourceRanges(const QList<QString> &load_balancer_source_ranges);
    bool is_load_balancer_source_ranges_Set() const;
    bool is_load_balancer_source_ranges_Valid() const;

    QList<OAIServicePort> getPorts() const;
    void setPorts(const QList<OAIServicePort> &ports);
    bool is_ports_Set() const;
    bool is_ports_Valid() const;

    bool isPublishNotReadyAddresses() const;
    void setPublishNotReadyAddresses(const bool &publish_not_ready_addresses);
    bool is_publish_not_ready_addresses_Set() const;
    bool is_publish_not_ready_addresses_Valid() const;

    QMap<QString, QString> getSelector() const;
    void setSelector(const QMap<QString, QString> &selector);
    bool is_selector_Set() const;
    bool is_selector_Valid() const;

    QString getSessionAffinity() const;
    void setSessionAffinity(const QString &session_affinity);
    bool is_session_affinity_Set() const;
    bool is_session_affinity_Valid() const;

    OAISessionAffinityConfig getSessionAffinityConfig() const;
    void setSessionAffinityConfig(const OAISessionAffinityConfig &session_affinity_config);
    bool is_session_affinity_config_Set() const;
    bool is_session_affinity_config_Valid() const;

    QList<QString> getTopologyKeys() const;
    void setTopologyKeys(const QList<QString> &topology_keys);
    bool is_topology_keys_Set() const;
    bool is_topology_keys_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_cluster_ip;
    bool m_cluster_ip_isSet;
    bool m_cluster_ip_isValid;

    QList<QString> m_external_ips;
    bool m_external_ips_isSet;
    bool m_external_ips_isValid;

    QString m_external_name;
    bool m_external_name_isSet;
    bool m_external_name_isValid;

    QString m_external_traffic_policy;
    bool m_external_traffic_policy_isSet;
    bool m_external_traffic_policy_isValid;

    qint32 m_health_check_node_port;
    bool m_health_check_node_port_isSet;
    bool m_health_check_node_port_isValid;

    QString m_ip_family;
    bool m_ip_family_isSet;
    bool m_ip_family_isValid;

    QString m_load_balancer_ip;
    bool m_load_balancer_ip_isSet;
    bool m_load_balancer_ip_isValid;

    QList<QString> m_load_balancer_source_ranges;
    bool m_load_balancer_source_ranges_isSet;
    bool m_load_balancer_source_ranges_isValid;

    QList<OAIServicePort> m_ports;
    bool m_ports_isSet;
    bool m_ports_isValid;

    bool m_publish_not_ready_addresses;
    bool m_publish_not_ready_addresses_isSet;
    bool m_publish_not_ready_addresses_isValid;

    QMap<QString, QString> m_selector;
    bool m_selector_isSet;
    bool m_selector_isValid;

    QString m_session_affinity;
    bool m_session_affinity_isSet;
    bool m_session_affinity_isValid;

    OAISessionAffinityConfig m_session_affinity_config;
    bool m_session_affinity_config_isSet;
    bool m_session_affinity_config_isValid;

    QList<QString> m_topology_keys;
    bool m_topology_keys_isSet;
    bool m_topology_keys_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIServiceSpec)

#endif // OAIServiceSpec_H
