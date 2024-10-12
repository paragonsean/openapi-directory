/**
 * AuthorizationManagementClient
 * Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.
 *
 * The version of the OpenAPI document: 2018-01-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResourceType.h
 *
 * Resource Type
 */

#ifndef OAIResourceType_H
#define OAIResourceType_H

#include <QJsonObject>

#include "OAIProviderOperation.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIProviderOperation;

class OAIResourceType : public OAIObject {
public:
    OAIResourceType();
    OAIResourceType(QString json);
    ~OAIResourceType() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIProviderOperation> getOperations() const;
    void setOperations(const QList<OAIProviderOperation> &operations);
    bool is_operations_Set() const;
    bool is_operations_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIProviderOperation> m_operations;
    bool m_operations_isSet;
    bool m_operations_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceType)

#endif // OAIResourceType_H
