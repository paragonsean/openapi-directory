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
 * OAIBuildAgentQueueResponse.h
 *
 * Queue configured in build definition
 */

#ifndef OAIBuildAgentQueueResponse_H
#define OAIBuildAgentQueueResponse_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBuildAgentQueueResponse : public OAIObject {
public:
    OAIBuildAgentQueueResponse();
    OAIBuildAgentQueueResponse(QString json);
    ~OAIBuildAgentQueueResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBuildDefinition() const;
    void setBuildDefinition(const QString &build_definition);
    bool is_build_definition_Set() const;
    bool is_build_definition_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_build_definition;
    bool m_build_definition_isSet;
    bool m_build_definition_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuildAgentQueueResponse)

#endif // OAIBuildAgentQueueResponse_H
