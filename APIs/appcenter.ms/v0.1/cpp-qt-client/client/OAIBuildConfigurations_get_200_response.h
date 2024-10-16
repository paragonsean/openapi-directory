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
 * OAIBuildConfigurations_get_200_response.h
 *
 * The build configuration in Azure pipeline YAML format
 */

#ifndef OAIBuildConfigurations_get_200_response_H
#define OAIBuildConfigurations_get_200_response_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBuildConfigurations_get_200_response : public OAIObject {
public:
    OAIBuildConfigurations_get_200_response();
    OAIBuildConfigurations_get_200_response(QString json);
    ~OAIBuildConfigurations_get_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getYaml() const;
    void setYaml(const QString &yaml);
    bool is_yaml_Set() const;
    bool is_yaml_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_yaml;
    bool m_yaml_isSet;
    bool m_yaml_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBuildConfigurations_get_200_response)

#endif // OAIBuildConfigurations_get_200_response_H
