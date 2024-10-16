/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateSystem_Models_UpdateGroupClientRelationship.h
 *
 * 
 */

#ifndef OAIUpdateSystem_Models_UpdateGroupClientRelationship_H
#define OAIUpdateSystem_Models_UpdateGroupClientRelationship_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateSystem_Models_UpdateGroupClientRelationship : public OAIObject {
public:
    OAIUpdateSystem_Models_UpdateGroupClientRelationship();
    OAIUpdateSystem_Models_UpdateGroupClientRelationship(QString json);
    ~OAIUpdateSystem_Models_UpdateGroupClientRelationship() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isActive() const;
    void setActive(const bool &active);
    bool is_active_Set() const;
    bool is_active_Valid() const;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QDateTime getLastCheckin() const;
    void setLastCheckin(const QDateTime &last_checkin);
    bool is_last_checkin_Set() const;
    bool is_last_checkin_Valid() const;

    QString getRelationshipId() const;
    void setRelationshipId(const QString &relationship_id);
    bool is_relationship_id_Set() const;
    bool is_relationship_id_Valid() const;

    QString getUpdateGroupId() const;
    void setUpdateGroupId(const QString &update_group_id);
    bool is_update_group_id_Set() const;
    bool is_update_group_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_active;
    bool m_active_isSet;
    bool m_active_isValid;

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QDateTime m_last_checkin;
    bool m_last_checkin_isSet;
    bool m_last_checkin_isValid;

    QString m_relationship_id;
    bool m_relationship_id_isSet;
    bool m_relationship_id_isValid;

    QString m_update_group_id;
    bool m_update_group_id_isSet;
    bool m_update_group_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateSystem_Models_UpdateGroupClientRelationship)

#endif // OAIUpdateSystem_Models_UpdateGroupClientRelationship_H
