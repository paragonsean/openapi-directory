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
 * OAIProjectBaseVO.h
 *
 * Java type: com.noosh.nooshapi.vo.ProjectBaseVO
 */

#ifndef OAIProjectBaseVO_H
#define OAIProjectBaseVO_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProjectBaseVO : public OAIObject {
public:
    OAIProjectBaseVO();
    OAIProjectBaseVO(QString json);
    ~OAIProjectBaseVO() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getProjectId() const;
    void setProjectId(const qint64 &project_id);
    bool is_project_id_Set() const;
    bool is_project_id_Valid() const;

    QString getProjectName() const;
    void setProjectName(const QString &project_name);
    bool is_project_name_Set() const;
    bool is_project_name_Valid() const;

    QString getProjectNumber() const;
    void setProjectNumber(const QString &project_number);
    bool is_project_number_Set() const;
    bool is_project_number_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_project_id;
    bool m_project_id_isSet;
    bool m_project_id_isValid;

    QString m_project_name;
    bool m_project_name_isSet;
    bool m_project_name_isValid;

    QString m_project_number;
    bool m_project_number_isSet;
    bool m_project_number_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectBaseVO)

#endif // OAIProjectBaseVO_H
