/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIScopeRepresentation.h
 *
 * 
 */

#ifndef OAIScopeRepresentation_H
#define OAIScopeRepresentation_H

#include <QJsonObject>

#include "OAIPolicyRepresentation.h"
#include "OAIResourceRepresentation.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPolicyRepresentation;
class OAIResourceRepresentation;

class OAIScopeRepresentation : public OAIObject {
public:
    OAIScopeRepresentation();
    OAIScopeRepresentation(QString json);
    ~OAIScopeRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getIconUri() const;
    void setIconUri(const QString &icon_uri);
    bool is_icon_uri_Set() const;
    bool is_icon_uri_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIPolicyRepresentation> getPolicies() const;
    void setPolicies(const QList<OAIPolicyRepresentation> &policies);
    bool is_policies_Set() const;
    bool is_policies_Valid() const;

    QList<OAIResourceRepresentation> getResources() const;
    void setResources(const QList<OAIResourceRepresentation> &resources);
    bool is_resources_Set() const;
    bool is_resources_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_icon_uri;
    bool m_icon_uri_isSet;
    bool m_icon_uri_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIPolicyRepresentation> m_policies;
    bool m_policies_isSet;
    bool m_policies_isValid;

    QList<OAIResourceRepresentation> m_resources;
    bool m_resources_isSet;
    bool m_resources_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIScopeRepresentation)

#endif // OAIScopeRepresentation_H
