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
 * OAIClusterMonitoringRequest.h
 *
 * The Operations Management Suite (OMS) parameters.
 */

#ifndef OAIClusterMonitoringRequest_H
#define OAIClusterMonitoringRequest_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIClusterMonitoringRequest : public OAIObject {
public:
    OAIClusterMonitoringRequest();
    OAIClusterMonitoringRequest(QString json);
    ~OAIClusterMonitoringRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPrimaryKey() const;
    void setPrimaryKey(const QString &primary_key);
    bool is_primary_key_Set() const;
    bool is_primary_key_Valid() const;

    QString getWorkspaceId() const;
    void setWorkspaceId(const QString &workspace_id);
    bool is_workspace_id_Set() const;
    bool is_workspace_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_primary_key;
    bool m_primary_key_isSet;
    bool m_primary_key_isValid;

    QString m_workspace_id;
    bool m_workspace_id_isSet;
    bool m_workspace_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIClusterMonitoringRequest)

#endif // OAIClusterMonitoringRequest_H
