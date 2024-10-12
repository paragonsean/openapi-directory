/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIControllerPowerStateChangeRequestProperties.h
 *
 * The properties of the controller power state change request.
 */

#ifndef OAIControllerPowerStateChangeRequestProperties_H
#define OAIControllerPowerStateChangeRequestProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIControllerPowerStateChangeRequestProperties : public OAIObject {
public:
    OAIControllerPowerStateChangeRequestProperties();
    OAIControllerPowerStateChangeRequestProperties(QString json);
    ~OAIControllerPowerStateChangeRequestProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAction() const;
    void setAction(const QString &action);
    bool is_action_Set() const;
    bool is_action_Valid() const;

    QString getActiveController() const;
    void setActiveController(const QString &active_controller);
    bool is_active_controller_Set() const;
    bool is_active_controller_Valid() const;

    QString getController0State() const;
    void setController0State(const QString &controller0_state);
    bool is_controller0_state_Set() const;
    bool is_controller0_state_Valid() const;

    QString getController1State() const;
    void setController1State(const QString &controller1_state);
    bool is_controller1_state_Set() const;
    bool is_controller1_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action;
    bool m_action_isSet;
    bool m_action_isValid;

    QString m_active_controller;
    bool m_active_controller_isSet;
    bool m_active_controller_isValid;

    QString m_controller0_state;
    bool m_controller0_state_isSet;
    bool m_controller0_state_isValid;

    QString m_controller1_state;
    bool m_controller1_state_isSet;
    bool m_controller1_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIControllerPowerStateChangeRequestProperties)

#endif // OAIControllerPowerStateChangeRequestProperties_H
