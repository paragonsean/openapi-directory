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
 * OAIBuilds_listToolsetProjects_200_response_testcloud.h
 *
 * 
 */

#ifndef OAIBuilds_listToolsetProjects_200_response_testcloud_H
#define OAIBuilds_listToolsetProjects_200_response_testcloud_H

#include <QJsonObject>

#include "OAIBuilds_listToolsetProjects_200_response_testcloud_projects_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBuilds_listToolsetProjects_200_response_testcloud_projects_inner;

class OAIBuilds_listToolsetProjects_200_response_testcloud : public OAIObject {
public:
    OAIBuilds_listToolsetProjects_200_response_testcloud();
    OAIBuilds_listToolsetProjects_200_response_testcloud(QString json);
    ~OAIBuilds_listToolsetProjects_200_response_testcloud() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBuilds_listToolsetProjects_200_response_testcloud_projects_inner> getProjects() const;
    void setProjects(const QList<OAIBuilds_listToolsetProjects_200_response_testcloud_projects_inner> &projects);
    bool is_projects_Set() const;
    bool is_projects_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBuilds_listToolsetProjects_200_response_testcloud_projects_inner> m_projects;
    bool m_projects_isSet;
    bool m_projects_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuilds_listToolsetProjects_200_response_testcloud)

#endif // OAIBuilds_listToolsetProjects_200_response_testcloud_H
