/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIoTRole.h
 *
 * Compute role.
 */

#ifndef OAIIoTRole_H
#define OAIIoTRole_H

#include <QJsonObject>

#include "OAIIoTRoleProperties.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIoTRoleProperties;

class OAIIoTRole : public OAIObject {
public:
    OAIIoTRole();
    OAIIoTRole(QString json);
    ~OAIIoTRole() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    OAIIoTRoleProperties getProperties() const;
    void setProperties(const OAIIoTRoleProperties &properties);
    bool is_properties_Set() const;
    bool is_properties_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    OAIIoTRoleProperties m_properties;
    bool m_properties_isSet;
    bool m_properties_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIoTRole)

#endif // OAIIoTRole_H
