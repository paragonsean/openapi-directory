/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOrchestratorVersionProfileProperties.h
 *
 * The properties of an orchestrator version profile.
 */

#ifndef OAIOrchestratorVersionProfileProperties_H
#define OAIOrchestratorVersionProfileProperties_H

#include <QJsonObject>

#include "OAIOrchestratorVersionProfile.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrchestratorVersionProfile;

class OAIOrchestratorVersionProfileProperties : public OAIObject {
public:
    OAIOrchestratorVersionProfileProperties();
    OAIOrchestratorVersionProfileProperties(QString json);
    ~OAIOrchestratorVersionProfileProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIOrchestratorVersionProfile> getOrchestrators() const;
    void setOrchestrators(const QList<OAIOrchestratorVersionProfile> &orchestrators);
    bool is_orchestrators_Set() const;
    bool is_orchestrators_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIOrchestratorVersionProfile> m_orchestrators;
    bool m_orchestrators_isSet;
    bool m_orchestrators_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrchestratorVersionProfileProperties)

#endif // OAIOrchestratorVersionProfileProperties_H
