/**
 * SqlManagementClient
 * The Azure SQL Database management API provides a RESTful set of web APIs that interact with Azure SQL Database services to manage your databases. The API enables users to create, retrieve, update, and delete databases, servers, and other entities.
 *
 * The version of the OpenAPI document: 2015-05-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFailoverGroupProperties.h
 *
 * Properties of a failover group.
 */

#ifndef OAIFailoverGroupProperties_H
#define OAIFailoverGroupProperties_H

#include <QJsonObject>

#include "OAIFailoverGroupReadOnlyEndpoint.h"
#include "OAIFailoverGroupReadWriteEndpoint.h"
#include "OAIPartnerInfo.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPartnerInfo;
class OAIFailoverGroupReadOnlyEndpoint;
class OAIFailoverGroupReadWriteEndpoint;

class OAIFailoverGroupProperties : public OAIObject {
public:
    OAIFailoverGroupProperties();
    OAIFailoverGroupProperties(QString json);
    ~OAIFailoverGroupProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getDatabases() const;
    void setDatabases(const QList<QString> &databases);
    bool is_databases_Set() const;
    bool is_databases_Valid() const;

    QList<OAIPartnerInfo> getPartnerServers() const;
    void setPartnerServers(const QList<OAIPartnerInfo> &partner_servers);
    bool is_partner_servers_Set() const;
    bool is_partner_servers_Valid() const;

    OAIFailoverGroupReadOnlyEndpoint getReadOnlyEndpoint() const;
    void setReadOnlyEndpoint(const OAIFailoverGroupReadOnlyEndpoint &read_only_endpoint);
    bool is_read_only_endpoint_Set() const;
    bool is_read_only_endpoint_Valid() const;

    OAIFailoverGroupReadWriteEndpoint getReadWriteEndpoint() const;
    void setReadWriteEndpoint(const OAIFailoverGroupReadWriteEndpoint &read_write_endpoint);
    bool is_read_write_endpoint_Set() const;
    bool is_read_write_endpoint_Valid() const;

    QString getReplicationRole() const;
    void setReplicationRole(const QString &replication_role);
    bool is_replication_role_Set() const;
    bool is_replication_role_Valid() const;

    QString getReplicationState() const;
    void setReplicationState(const QString &replication_state);
    bool is_replication_state_Set() const;
    bool is_replication_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_databases;
    bool m_databases_isSet;
    bool m_databases_isValid;

    QList<OAIPartnerInfo> m_partner_servers;
    bool m_partner_servers_isSet;
    bool m_partner_servers_isValid;

    OAIFailoverGroupReadOnlyEndpoint m_read_only_endpoint;
    bool m_read_only_endpoint_isSet;
    bool m_read_only_endpoint_isValid;

    OAIFailoverGroupReadWriteEndpoint m_read_write_endpoint;
    bool m_read_write_endpoint_isSet;
    bool m_read_write_endpoint_isValid;

    QString m_replication_role;
    bool m_replication_role_isSet;
    bool m_replication_role_isValid;

    QString m_replication_state;
    bool m_replication_state_isSet;
    bool m_replication_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFailoverGroupProperties)

#endif // OAIFailoverGroupProperties_H
