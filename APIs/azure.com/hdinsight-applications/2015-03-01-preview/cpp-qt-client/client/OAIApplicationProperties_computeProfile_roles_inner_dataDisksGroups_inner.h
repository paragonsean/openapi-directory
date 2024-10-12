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
 * OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner.h
 *
 * The data disks groups for the role.
 */

#ifndef OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner_H
#define OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner : public OAIObject {
public:
    OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner();
    OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner(QString json);
    ~OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getDiskSizeGb() const;
    void setDiskSizeGb(const qint32 &disk_size_gb);
    bool is_disk_size_gb_Set() const;
    bool is_disk_size_gb_Valid() const;

    qint32 getDisksPerNode() const;
    void setDisksPerNode(const qint32 &disks_per_node);
    bool is_disks_per_node_Set() const;
    bool is_disks_per_node_Valid() const;

    QString getStorageAccountType() const;
    void setStorageAccountType(const QString &storage_account_type);
    bool is_storage_account_type_Set() const;
    bool is_storage_account_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_disk_size_gb;
    bool m_disk_size_gb_isSet;
    bool m_disk_size_gb_isValid;

    qint32 m_disks_per_node;
    bool m_disks_per_node_isSet;
    bool m_disks_per_node_isValid;

    QString m_storage_account_type;
    bool m_storage_account_type_isSet;
    bool m_storage_account_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner)

#endif // OAIApplicationProperties_computeProfile_roles_inner_dataDisksGroups_inner_H
