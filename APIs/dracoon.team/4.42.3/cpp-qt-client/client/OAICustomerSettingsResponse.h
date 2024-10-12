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
 * OAICustomerSettingsResponse.h
 *
 * Customer settings
 */

#ifndef OAICustomerSettingsResponse_H
#define OAICustomerSettingsResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICustomerSettingsResponse : public OAIObject {
public:
    OAICustomerSettingsResponse();
    OAICustomerSettingsResponse(QString json);
    ~OAICustomerSettingsResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getHomeRoomParentId() const;
    void setHomeRoomParentId(const qint64 &home_room_parent_id);
    bool is_home_room_parent_id_Set() const;
    bool is_home_room_parent_id_Valid() const;

    QString getHomeRoomParentName() const;
    void setHomeRoomParentName(const QString &home_room_parent_name);
    bool is_home_room_parent_name_Set() const;
    bool is_home_room_parent_name_Valid() const;

    qint64 getHomeRoomQuota() const;
    void setHomeRoomQuota(const qint64 &home_room_quota);
    bool is_home_room_quota_Set() const;
    bool is_home_room_quota_Valid() const;

    bool isHomeRoomsActive() const;
    void setHomeRoomsActive(const bool &home_rooms_active);
    bool is_home_rooms_active_Set() const;
    bool is_home_rooms_active_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_home_room_parent_id;
    bool m_home_room_parent_id_isSet;
    bool m_home_room_parent_id_isValid;

    QString m_home_room_parent_name;
    bool m_home_room_parent_name_isSet;
    bool m_home_room_parent_name_isValid;

    qint64 m_home_room_quota;
    bool m_home_room_quota_isSet;
    bool m_home_room_quota_isValid;

    bool m_home_rooms_active;
    bool m_home_rooms_active_isSet;
    bool m_home_rooms_active_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICustomerSettingsResponse)

#endif // OAICustomerSettingsResponse_H
