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
 * OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile.h
 *
 * The list of SSH public keys.
 */

#ifndef OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_H
#define OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_H

#include <QJsonObject>

#include "OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner;

class OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile : public OAIObject {
public:
    OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile();
    OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile(QString json);
    ~OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner> getPublicKeys() const;
    void setPublicKeys(const QList<OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner> &public_keys);
    bool is_public_keys_Set() const;
    bool is_public_keys_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner> m_public_keys;
    bool m_public_keys_isSet;
    bool m_public_keys_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile)

#endif // OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_H
