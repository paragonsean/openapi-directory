/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIClientPlanSelectorParams.h
 *
 * Parameters to select a plan from a client file
 */

#ifndef OAIClientPlanSelectorParams_H
#define OAIClientPlanSelectorParams_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIClientPlanSelectorParams : public OAIObject {
public:
    OAIClientPlanSelectorParams();
    OAIClientPlanSelectorParams(QString json);
    ~OAIClientPlanSelectorParams() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getPlanId() const;
    void setPlanId(const QString &plan_id);
    bool is_plan_id_Set() const;
    bool is_plan_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_plan_id;
    bool m_plan_id_isSet;
    bool m_plan_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIClientPlanSelectorParams)

#endif // OAIClientPlanSelectorParams_H
