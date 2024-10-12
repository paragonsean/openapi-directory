/**
 * ComputeManagementConvenienceClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDependency.h
 *
 * Deployment dependency information.
 */

#ifndef OAIDependency_H
#define OAIDependency_H

#include <QJsonObject>

#include "OAIBasicDependency.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBasicDependency;

class OAIDependency : public OAIObject {
public:
    OAIDependency();
    OAIDependency(QString json);
    ~OAIDependency() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBasicDependency> getDependsOn() const;
    void setDependsOn(const QList<OAIBasicDependency> &depends_on);
    bool is_depends_on_Set() const;
    bool is_depends_on_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getResourceName() const;
    void setResourceName(const QString &resource_name);
    bool is_resource_name_Set() const;
    bool is_resource_name_Valid() const;

    QString getResourceType() const;
    void setResourceType(const QString &resource_type);
    bool is_resource_type_Set() const;
    bool is_resource_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBasicDependency> m_depends_on;
    bool m_depends_on_isSet;
    bool m_depends_on_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_resource_name;
    bool m_resource_name_isSet;
    bool m_resource_name_isValid;

    QString m_resource_type;
    bool m_resource_type_isSet;
    bool m_resource_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDependency)

#endif // OAIDependency_H
