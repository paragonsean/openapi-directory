/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGraphQLExtension.h
 *
 * GraphQLExtension describes the graphql server extension point in the backend
 */

#ifndef OAIGraphQLExtension_H
#define OAIGraphQLExtension_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGraphQLExtension : public OAIObject {
public:
    OAIGraphQLExtension();
    OAIGraphQLExtension(QString json);
    ~OAIGraphQLExtension() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getComponent() const;
    void setComponent(const QString &component);
    bool is_component_Set() const;
    bool is_component_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_component;
    bool m_component_isSet;
    bool m_component_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGraphQLExtension)

#endif // OAIGraphQLExtension_H
