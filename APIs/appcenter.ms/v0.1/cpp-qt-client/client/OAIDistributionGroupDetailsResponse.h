/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDistributionGroupDetailsResponse.h
 *
 * 
 */

#ifndef OAIDistributionGroupDetailsResponse_H
#define OAIDistributionGroupDetailsResponse_H

#include <QJsonObject>

#include "OAIDistributionGroups_listUsers_200_response_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDistributionGroups_listUsers_200_response_inner;

class OAIDistributionGroupDetailsResponse : public OAIObject {
public:
    OAIDistributionGroupDetailsResponse();
    OAIDistributionGroupDetailsResponse(QString json);
    ~OAIDistributionGroupDetailsResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsPublic() const;
    void setIsPublic(const bool &is_public);
    bool is_is_public_Set() const;
    bool is_is_public_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOrigin() const;
    void setOrigin(const QString &origin);
    bool is_origin_Set() const;
    bool is_origin_Valid() const;

    QString getGroupType() const;
    void setGroupType(const QString &group_type);
    bool is_group_type_Set() const;
    bool is_group_type_Valid() const;

    bool isIsShared() const;
    void setIsShared(const bool &is_shared);
    bool is_is_shared_Set() const;
    bool is_is_shared_Valid() const;

    double getNotifiedUserCount() const;
    void setNotifiedUserCount(const double &notified_user_count);
    bool is_notified_user_count_Set() const;
    bool is_notified_user_count_Valid() const;

    double getTotalAppsCount() const;
    void setTotalAppsCount(const double &total_apps_count);
    bool is_total_apps_count_Set() const;
    bool is_total_apps_count_Valid() const;

    double getTotalUserCount() const;
    void setTotalUserCount(const double &total_user_count);
    bool is_total_user_count_Set() const;
    bool is_total_user_count_Valid() const;

    QList<OAIDistributionGroups_listUsers_200_response_inner> getUsers() const;
    void setUsers(const QList<OAIDistributionGroups_listUsers_200_response_inner> &users);
    bool is_users_Set() const;
    bool is_users_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_public;
    bool m_is_public_isSet;
    bool m_is_public_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_origin;
    bool m_origin_isSet;
    bool m_origin_isValid;

    QString m_group_type;
    bool m_group_type_isSet;
    bool m_group_type_isValid;

    bool m_is_shared;
    bool m_is_shared_isSet;
    bool m_is_shared_isValid;

    double m_notified_user_count;
    bool m_notified_user_count_isSet;
    bool m_notified_user_count_isValid;

    double m_total_apps_count;
    bool m_total_apps_count_isSet;
    bool m_total_apps_count_isValid;

    double m_total_user_count;
    bool m_total_user_count_isSet;
    bool m_total_user_count_isValid;

    QList<OAIDistributionGroups_listUsers_200_response_inner> m_users;
    bool m_users_isSet;
    bool m_users_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDistributionGroupDetailsResponse)

#endif // OAIDistributionGroupDetailsResponse_H
