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
 * OAIBuilds_listToolsetProjects_200_response_uwp.h
 *
 * 
 */

#ifndef OAIBuilds_listToolsetProjects_200_response_uwp_H
#define OAIBuilds_listToolsetProjects_200_response_uwp_H

#include <QJsonObject>

#include "OAIBuilds_listToolsetProjects_200_response_uwp_uwpSolutions_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBuilds_listToolsetProjects_200_response_uwp_uwpSolutions_inner;

class OAIBuilds_listToolsetProjects_200_response_uwp : public OAIObject {
public:
    OAIBuilds_listToolsetProjects_200_response_uwp();
    OAIBuilds_listToolsetProjects_200_response_uwp(QString json);
    ~OAIBuilds_listToolsetProjects_200_response_uwp() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBuilds_listToolsetProjects_200_response_uwp_uwpSolutions_inner> getUwpSolutions() const;
    void setUwpSolutions(const QList<OAIBuilds_listToolsetProjects_200_response_uwp_uwpSolutions_inner> &uwp_solutions);
    bool is_uwp_solutions_Set() const;
    bool is_uwp_solutions_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBuilds_listToolsetProjects_200_response_uwp_uwpSolutions_inner> m_uwp_solutions;
    bool m_uwp_solutions_isSet;
    bool m_uwp_solutions_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuilds_listToolsetProjects_200_response_uwp)

#endif // OAIBuilds_listToolsetProjects_200_response_uwp_H
