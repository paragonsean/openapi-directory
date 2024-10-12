/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFailoverServer.h
 *
 * Failover server information
 */

#ifndef OAIFailoverServer_H
#define OAIFailoverServer_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFailoverServer : public OAIObject {
public:
    OAIFailoverServer();
    OAIFailoverServer(QString json);
    ~OAIFailoverServer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isFailoverEnabled() const;
    void setFailoverEnabled(const bool &failover_enabled);
    bool is_failover_enabled_Set() const;
    bool is_failover_enabled_Valid() const;

    QString getFailoverIpAddress() const;
    void setFailoverIpAddress(const QString &failover_ip_address);
    bool is_failover_ip_address_Set() const;
    bool is_failover_ip_address_Valid() const;

    qint32 getFailoverPort() const;
    void setFailoverPort(const qint32 &failover_port);
    bool is_failover_port_Set() const;
    bool is_failover_port_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_failover_enabled;
    bool m_failover_enabled_isSet;
    bool m_failover_enabled_isValid;

    QString m_failover_ip_address;
    bool m_failover_ip_address_isSet;
    bool m_failover_ip_address_isValid;

    qint32 m_failover_port;
    bool m_failover_port_isSet;
    bool m_failover_port_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFailoverServer)

#endif // OAIFailoverServer_H
