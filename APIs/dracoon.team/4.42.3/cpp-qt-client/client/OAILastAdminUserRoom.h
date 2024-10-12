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
 * OAILastAdminUserRoom.h
 *
 * Room information
 */

#ifndef OAILastAdminUserRoom_H
#define OAILastAdminUserRoom_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILastAdminUserRoom : public OAIObject {
public:
    OAILastAdminUserRoom();
    OAILastAdminUserRoom(QString json);
    ~OAILastAdminUserRoom() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isLastAdminInGroup() const;
    void setLastAdminInGroup(const bool &last_admin_in_group);
    bool is_last_admin_in_group_Set() const;
    bool is_last_admin_in_group_Valid() const;

    qint64 getLastAdminInGroupId() const;
    void setLastAdminInGroupId(const qint64 &last_admin_in_group_id);
    bool is_last_admin_in_group_id_Set() const;
    bool is_last_admin_in_group_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint64 getParentId() const;
    void setParentId(const qint64 &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    QString getParentPath() const;
    void setParentPath(const QString &parent_path);
    bool is_parent_path_Set() const;
    bool is_parent_path_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_last_admin_in_group;
    bool m_last_admin_in_group_isSet;
    bool m_last_admin_in_group_isValid;

    qint64 m_last_admin_in_group_id;
    bool m_last_admin_in_group_id_isSet;
    bool m_last_admin_in_group_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint64 m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    QString m_parent_path;
    bool m_parent_path_isSet;
    bool m_parent_path_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILastAdminUserRoom)

#endif // OAILastAdminUserRoom_H
