/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2017-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOrchestratorVersionProfile.h
 *
 * The profile of an orchestrator and its available versions.
 */

#ifndef OAIOrchestratorVersionProfile_H
#define OAIOrchestratorVersionProfile_H

#include <QJsonObject>

#include "OAIOrchestratorProfile.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrchestratorProfile;

class OAIOrchestratorVersionProfile : public OAIObject {
public:
    OAIOrchestratorVersionProfile();
    OAIOrchestratorVersionProfile(QString json);
    ~OAIOrchestratorVersionProfile() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isRDefault() const;
    void setRDefault(const bool &r_default);
    bool is_r_default_Set() const;
    bool is_r_default_Valid() const;

    QString getOrchestratorType() const;
    void setOrchestratorType(const QString &orchestrator_type);
    bool is_orchestrator_type_Set() const;
    bool is_orchestrator_type_Valid() const;

    QString getOrchestratorVersion() const;
    void setOrchestratorVersion(const QString &orchestrator_version);
    bool is_orchestrator_version_Set() const;
    bool is_orchestrator_version_Valid() const;

    QList<OAIOrchestratorProfile> getUpgrades() const;
    void setUpgrades(const QList<OAIOrchestratorProfile> &upgrades);
    bool is_upgrades_Set() const;
    bool is_upgrades_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_r_default;
    bool m_r_default_isSet;
    bool m_r_default_isValid;

    QString m_orchestrator_type;
    bool m_orchestrator_type_isSet;
    bool m_orchestrator_type_isValid;

    QString m_orchestrator_version;
    bool m_orchestrator_version_isSet;
    bool m_orchestrator_version_isValid;

    QList<OAIOrchestratorProfile> m_upgrades;
    bool m_upgrades_isSet;
    bool m_upgrades_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrchestratorVersionProfile)

#endif // OAIOrchestratorVersionProfile_H
