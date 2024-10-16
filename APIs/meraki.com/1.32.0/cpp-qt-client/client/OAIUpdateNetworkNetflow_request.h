/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateNetworkNetflow_request.h
 *
 * 
 */

#ifndef OAIUpdateNetworkNetflow_request_H
#define OAIUpdateNetworkNetflow_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkNetflow_request : public OAIObject {
public:
    OAIUpdateNetworkNetflow_request();
    OAIUpdateNetworkNetflow_request(QString json);
    ~OAIUpdateNetworkNetflow_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCollectorIp() const;
    void setCollectorIp(const QString &collector_ip);
    bool is_collector_ip_Set() const;
    bool is_collector_ip_Valid() const;

    qint32 getCollectorPort() const;
    void setCollectorPort(const qint32 &collector_port);
    bool is_collector_port_Set() const;
    bool is_collector_port_Valid() const;

    qint32 getEtaDstPort() const;
    void setEtaDstPort(const qint32 &eta_dst_port);
    bool is_eta_dst_port_Set() const;
    bool is_eta_dst_port_Valid() const;

    bool isEtaEnabled() const;
    void setEtaEnabled(const bool &eta_enabled);
    bool is_eta_enabled_Set() const;
    bool is_eta_enabled_Valid() const;

    bool isReportingEnabled() const;
    void setReportingEnabled(const bool &reporting_enabled);
    bool is_reporting_enabled_Set() const;
    bool is_reporting_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_collector_ip;
    bool m_collector_ip_isSet;
    bool m_collector_ip_isValid;

    qint32 m_collector_port;
    bool m_collector_port_isSet;
    bool m_collector_port_isValid;

    qint32 m_eta_dst_port;
    bool m_eta_dst_port_isSet;
    bool m_eta_dst_port_isValid;

    bool m_eta_enabled;
    bool m_eta_enabled_isSet;
    bool m_eta_enabled_isValid;

    bool m_reporting_enabled;
    bool m_reporting_enabled_isSet;
    bool m_reporting_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkNetflow_request)

#endif // OAIUpdateNetworkNetflow_request_H
