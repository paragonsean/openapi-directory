/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApplicationProperties.h
 *
 * The HDInsight cluster application GET response.
 */

#ifndef OAIApplicationProperties_H
#define OAIApplicationProperties_H

#include <QJsonObject>

#include "OAIApplicationGetEndpoint.h"
#include "OAIApplicationGetHttpsEndpoint.h"
#include "OAIApplicationProperties_computeProfile.h"
#include "OAIApplicationProperties_errors_inner.h"
#include "OAIApplicationProperties_installScriptActions_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIApplicationProperties_computeProfile;
class OAIApplicationProperties_errors_inner;
class OAIApplicationGetHttpsEndpoint;
class OAIApplicationProperties_installScriptActions_inner;
class OAIApplicationGetEndpoint;

class OAIApplicationProperties : public OAIObject {
public:
    OAIApplicationProperties();
    OAIApplicationProperties(QString json);
    ~OAIApplicationProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApplicationState() const;
    void setApplicationState(const QString &application_state);
    bool is_application_state_Set() const;
    bool is_application_state_Valid() const;

    QString getApplicationType() const;
    void setApplicationType(const QString &application_type);
    bool is_application_type_Set() const;
    bool is_application_type_Valid() const;

    OAIApplicationProperties_computeProfile getComputeProfile() const;
    void setComputeProfile(const OAIApplicationProperties_computeProfile &compute_profile);
    bool is_compute_profile_Set() const;
    bool is_compute_profile_Valid() const;

    QString getCreatedDate() const;
    void setCreatedDate(const QString &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    QList<OAIApplicationProperties_errors_inner> getErrors() const;
    void setErrors(const QList<OAIApplicationProperties_errors_inner> &errors);
    bool is_errors_Set() const;
    bool is_errors_Valid() const;

    QList<OAIApplicationGetHttpsEndpoint> getHttpsEndpoints() const;
    void setHttpsEndpoints(const QList<OAIApplicationGetHttpsEndpoint> &https_endpoints);
    bool is_https_endpoints_Set() const;
    bool is_https_endpoints_Valid() const;

    QList<OAIApplicationProperties_installScriptActions_inner> getInstallScriptActions() const;
    void setInstallScriptActions(const QList<OAIApplicationProperties_installScriptActions_inner> &install_script_actions);
    bool is_install_script_actions_Set() const;
    bool is_install_script_actions_Valid() const;

    QString getMarketplaceIdentifier() const;
    void setMarketplaceIdentifier(const QString &marketplace_identifier);
    bool is_marketplace_identifier_Set() const;
    bool is_marketplace_identifier_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    QList<OAIApplicationGetEndpoint> getSshEndpoints() const;
    void setSshEndpoints(const QList<OAIApplicationGetEndpoint> &ssh_endpoints);
    bool is_ssh_endpoints_Set() const;
    bool is_ssh_endpoints_Valid() const;

    QList<OAIApplicationProperties_installScriptActions_inner> getUninstallScriptActions() const;
    void setUninstallScriptActions(const QList<OAIApplicationProperties_installScriptActions_inner> &uninstall_script_actions);
    bool is_uninstall_script_actions_Set() const;
    bool is_uninstall_script_actions_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_application_state;
    bool m_application_state_isSet;
    bool m_application_state_isValid;

    QString m_application_type;
    bool m_application_type_isSet;
    bool m_application_type_isValid;

    OAIApplicationProperties_computeProfile m_compute_profile;
    bool m_compute_profile_isSet;
    bool m_compute_profile_isValid;

    QString m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    QList<OAIApplicationProperties_errors_inner> m_errors;
    bool m_errors_isSet;
    bool m_errors_isValid;

    QList<OAIApplicationGetHttpsEndpoint> m_https_endpoints;
    bool m_https_endpoints_isSet;
    bool m_https_endpoints_isValid;

    QList<OAIApplicationProperties_installScriptActions_inner> m_install_script_actions;
    bool m_install_script_actions_isSet;
    bool m_install_script_actions_isValid;

    QString m_marketplace_identifier;
    bool m_marketplace_identifier_isSet;
    bool m_marketplace_identifier_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;

    QList<OAIApplicationGetEndpoint> m_ssh_endpoints;
    bool m_ssh_endpoints_isSet;
    bool m_ssh_endpoints_isValid;

    QList<OAIApplicationProperties_installScriptActions_inner> m_uninstall_script_actions;
    bool m_uninstall_script_actions_isSet;
    bool m_uninstall_script_actions_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties)

#endif // OAIApplicationProperties_H
