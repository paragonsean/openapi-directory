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
 * OAITestCloudProjectFrameworkProperties.h
 *
 * 
 */

#ifndef OAITestCloudProjectFrameworkProperties_H
#define OAITestCloudProjectFrameworkProperties_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITestCloudProjectFrameworkProperties : public OAIObject {
public:
    OAITestCloudProjectFrameworkProperties();
    OAITestCloudProjectFrameworkProperties(QString json);
    ~OAITestCloudProjectFrameworkProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getConfigurations() const;
    void setConfigurations(const QList<QString> &configurations);
    bool is_configurations_Set() const;
    bool is_configurations_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_configurations;
    bool m_configurations_isSet;
    bool m_configurations_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITestCloudProjectFrameworkProperties)

#endif // OAITestCloudProjectFrameworkProperties_H
