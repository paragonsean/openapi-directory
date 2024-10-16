/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISerpCollectResponse_tasks_inner.h
 *
 * 
 */

#ifndef OAISerpCollectResponse_tasks_inner_H
#define OAISerpCollectResponse_tasks_inner_H

#include <QJsonObject>

#include "OAISerpCollectResponse_tasks_inner_task_id.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISerpCollectResponse_tasks_inner_task_id;

class OAISerpCollectResponse_tasks_inner : public OAIObject {
public:
    OAISerpCollectResponse_tasks_inner();
    OAISerpCollectResponse_tasks_inner(QString json);
    ~OAISerpCollectResponse_tasks_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAISerpCollectResponse_tasks_inner_task_id getTaskId() const;
    void setTaskId(const OAISerpCollectResponse_tasks_inner_task_id &task_id);
    bool is_task_id_Set() const;
    bool is_task_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAISerpCollectResponse_tasks_inner_task_id m_task_id;
    bool m_task_id_isSet;
    bool m_task_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISerpCollectResponse_tasks_inner)

#endif // OAISerpCollectResponse_tasks_inner_H
