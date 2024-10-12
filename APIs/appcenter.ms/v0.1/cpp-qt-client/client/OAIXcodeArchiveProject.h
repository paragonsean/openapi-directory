/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIXcodeArchiveProject.h
 *
 * 
 */

#ifndef OAIXcodeArchiveProject_H
#define OAIXcodeArchiveProject_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIXcodeArchiveProject : public OAIObject {
public:
    OAIXcodeArchiveProject();
    OAIXcodeArchiveProject(QString json);
    ~OAIXcodeArchiveProject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArchiveTargetId() const;
    void setArchiveTargetId(const QString &archive_target_id);
    bool is_archive_target_id_Set() const;
    bool is_archive_target_id_Valid() const;

    QString getProjectName() const;
    void setProjectName(const QString &project_name);
    bool is_project_name_Set() const;
    bool is_project_name_Valid() const;

    QString getProjectPath() const;
    void setProjectPath(const QString &project_path);
    bool is_project_path_Set() const;
    bool is_project_path_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_archive_target_id;
    bool m_archive_target_id_isSet;
    bool m_archive_target_id_isValid;

    QString m_project_name;
    bool m_project_name_isSet;
    bool m_project_name_isValid;

    QString m_project_path;
    bool m_project_path_isSet;
    bool m_project_path_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIXcodeArchiveProject)

#endif // OAIXcodeArchiveProject_H
