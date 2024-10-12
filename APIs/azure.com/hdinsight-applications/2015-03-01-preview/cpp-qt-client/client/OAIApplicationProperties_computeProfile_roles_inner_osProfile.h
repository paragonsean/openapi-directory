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
 * OAIApplicationProperties_computeProfile_roles_inner_osProfile.h
 *
 * The Linux operation systems profile.
 */

#ifndef OAIApplicationProperties_computeProfile_roles_inner_osProfile_H
#define OAIApplicationProperties_computeProfile_roles_inner_osProfile_H

#include <QJsonObject>

#include "OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile;

class OAIApplicationProperties_computeProfile_roles_inner_osProfile : public OAIObject {
public:
    OAIApplicationProperties_computeProfile_roles_inner_osProfile();
    OAIApplicationProperties_computeProfile_roles_inner_osProfile(QString json);
    ~OAIApplicationProperties_computeProfile_roles_inner_osProfile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile getLinuxOperatingSystemProfile() const;
    void setLinuxOperatingSystemProfile(const OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile &linux_operating_system_profile);
    bool is_linux_operating_system_profile_Set() const;
    bool is_linux_operating_system_profile_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile m_linux_operating_system_profile;
    bool m_linux_operating_system_profile_isSet;
    bool m_linux_operating_system_profile_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_computeProfile_roles_inner_osProfile)

#endif // OAIApplicationProperties_computeProfile_roles_inner_osProfile_H
