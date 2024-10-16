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
 * OAILegacyApp.h
 *
 * 
 */

#ifndef OAILegacyApp_H
#define OAILegacyApp_H

#include <QJsonObject>

#include "OAILegacyApp_collaborators_value.h"
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILegacyApp_collaborators_value;

class OAILegacyApp : public OAIObject {
public:
    OAILegacyApp();
    OAILegacyApp(QString json);
    ~OAILegacyApp() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, OAILegacyApp_collaborators_value> getCollaborators() const;
    void setCollaborators(const QMap<QString, OAILegacyApp_collaborators_value> &collaborators);
    bool is_collaborators_Set() const;
    bool is_collaborators_Valid() const;

    QList<QString> getDeployments() const;
    void setDeployments(const QList<QString> &deployments);
    bool is_deployments_Set() const;
    bool is_deployments_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, OAILegacyApp_collaborators_value> m_collaborators;
    bool m_collaborators_isSet;
    bool m_collaborators_isValid;

    QList<QString> m_deployments;
    bool m_deployments_isSet;
    bool m_deployments_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILegacyApp)

#endif // OAILegacyApp_H
