/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConfiguration_services_facebook_types_group.h
 *
 * 
 */

#ifndef OAIConfiguration_services_facebook_types_group_H
#define OAIConfiguration_services_facebook_types_group_H

#include <QJsonObject>

#include "OAIConfiguration_services_appdotnet_types_profile_icons.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfiguration_services_appdotnet_types_profile_icons;

class OAIConfiguration_services_facebook_types_group : public OAIObject {
public:
    OAIConfiguration_services_facebook_types_group();
    OAIConfiguration_services_facebook_types_group(QString json);
    ~OAIConfiguration_services_facebook_types_group() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getCharacterLimit() const;
    void setCharacterLimit(const double &character_limit);
    bool is_character_limit_Set() const;
    bool is_character_limit_Valid() const;

    OAIConfiguration_services_appdotnet_types_profile_icons getIcons() const;
    void setIcons(const OAIConfiguration_services_appdotnet_types_profile_icons &icons);
    bool is_icons_Set() const;
    bool is_icons_Valid() const;

    bool isLinkAttachments() const;
    void setLinkAttachments(const bool &link_attachments);
    bool is_link_attachments_Set() const;
    bool is_link_attachments_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    double getScheduleLimit() const;
    void setScheduleLimit(const double &schedule_limit);
    bool is_schedule_limit_Set() const;
    bool is_schedule_limit_Valid() const;

    QList<QString> getSupportedInteractions() const;
    void setSupportedInteractions(const QList<QString> &supported_interactions);
    bool is_supported_interactions_Set() const;
    bool is_supported_interactions_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_character_limit;
    bool m_character_limit_isSet;
    bool m_character_limit_isValid;

    OAIConfiguration_services_appdotnet_types_profile_icons m_icons;
    bool m_icons_isSet;
    bool m_icons_isValid;

    bool m_link_attachments;
    bool m_link_attachments_isSet;
    bool m_link_attachments_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    double m_schedule_limit;
    bool m_schedule_limit_isSet;
    bool m_schedule_limit_isValid;

    QList<QString> m_supported_interactions;
    bool m_supported_interactions_isSet;
    bool m_supported_interactions_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfiguration_services_facebook_types_group)

#endif // OAIConfiguration_services_facebook_types_group_H
