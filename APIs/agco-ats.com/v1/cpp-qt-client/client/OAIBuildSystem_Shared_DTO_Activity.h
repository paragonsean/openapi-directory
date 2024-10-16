/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBuildSystem_Shared_DTO_Activity.h
 *
 * A DTO for an IActivity
 */

#ifndef OAIBuildSystem_Shared_DTO_Activity_H
#define OAIBuildSystem_Shared_DTO_Activity_H

#include <QJsonObject>

#include "OAIBuildSystem_Shared_DTO_ActivityStep.h"
#include "OAIBuildSystem_Shared_DTO_Parameter.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBuildSystem_Shared_DTO_Parameter;
class OAIBuildSystem_Shared_DTO_ActivityStep;

class OAIBuildSystem_Shared_DTO_Activity : public OAIObject {
public:
    OAIBuildSystem_Shared_DTO_Activity();
    OAIBuildSystem_Shared_DTO_Activity(QString json);
    ~OAIBuildSystem_Shared_DTO_Activity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getActivityId() const;
    void setActivityId(const qint32 &activity_id);
    bool is_activity_id_Set() const;
    bool is_activity_id_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIBuildSystem_Shared_DTO_Parameter> getParameters() const;
    void setParameters(const QList<OAIBuildSystem_Shared_DTO_Parameter> &parameters);
    bool is_parameters_Set() const;
    bool is_parameters_Valid() const;

    QList<OAIBuildSystem_Shared_DTO_ActivityStep> getSteps() const;
    void setSteps(const QList<OAIBuildSystem_Shared_DTO_ActivityStep> &steps);
    bool is_steps_Set() const;
    bool is_steps_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_activity_id;
    bool m_activity_id_isSet;
    bool m_activity_id_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIBuildSystem_Shared_DTO_Parameter> m_parameters;
    bool m_parameters_isSet;
    bool m_parameters_isValid;

    QList<OAIBuildSystem_Shared_DTO_ActivityStep> m_steps;
    bool m_steps_isSet;
    bool m_steps_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuildSystem_Shared_DTO_Activity)

#endif // OAIBuildSystem_Shared_DTO_Activity_H
