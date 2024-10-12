/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBaseServiceGroup.h
 *
 * 
 */

#ifndef OAIBaseServiceGroup_H
#define OAIBaseServiceGroup_H

#include <QJsonObject>

#include "OAIEntityType.h"
#include "OAIGroup.h"
#include "OAIReference.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIReference;

class OAIBaseServiceGroup : public OAIObject {
public:
    OAIBaseServiceGroup();
    OAIBaseServiceGroup(QString json);
    ~OAIBaseServiceGroup() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEntityId() const;
    void setEntityId(const QString &entity_id);
    bool is_entity_id_Set() const;
    bool is_entity_id_Valid() const;

    OAIEntityType getEntityType() const;
    void setEntityType(const OAIEntityType &entity_type);
    bool is_entity_type_Set() const;
    bool is_entity_type_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIReference> getMembers() const;
    void setMembers(const QList<OAIReference> &members);
    bool is_members_Set() const;
    bool is_members_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_entity_id;
    bool m_entity_id_isSet;
    bool m_entity_id_isValid;

    OAIEntityType m_entity_type;
    bool m_entity_type_isSet;
    bool m_entity_type_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIReference> m_members;
    bool m_members_isSet;
    bool m_members_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBaseServiceGroup)

#endif // OAIBaseServiceGroup_H
