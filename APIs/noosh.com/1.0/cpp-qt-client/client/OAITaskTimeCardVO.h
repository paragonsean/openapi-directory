/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITaskTimeCardVO.h
 *
 * Java type: com.noosh.nooshapi.vo.TaskTimeCardVO
 */

#ifndef OAITaskTimeCardVO_H
#define OAITaskTimeCardVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITaskTimeCardVO : public OAIObject {
public:
    OAITaskTimeCardVO();
    OAITaskTimeCardVO(QString json);
    ~OAITaskTimeCardVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getTaskId() const;
    void setTaskId(const qint64 &task_id);
    bool is_task_id_Set() const;
    bool is_task_id_Valid() const;

    QString getTaskName() const;
    void setTaskName(const QString &task_name);
    bool is_task_name_Set() const;
    bool is_task_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_task_id;
    bool m_task_id_isSet;
    bool m_task_id_isValid;

    QString m_task_name;
    bool m_task_name_isSet;
    bool m_task_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITaskTimeCardVO)

#endif // OAITaskTimeCardVO_H
