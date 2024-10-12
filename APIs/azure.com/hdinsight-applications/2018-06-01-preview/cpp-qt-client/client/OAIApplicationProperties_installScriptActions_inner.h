/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIApplicationProperties_installScriptActions_inner.h
 *
 * Describes a script action on a running cluster.
 */

#ifndef OAIApplicationProperties_installScriptActions_inner_H
#define OAIApplicationProperties_installScriptActions_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIApplicationProperties_installScriptActions_inner : public OAIObject {
public:
    OAIApplicationProperties_installScriptActions_inner();
    OAIApplicationProperties_installScriptActions_inner(QString json);
    ~OAIApplicationProperties_installScriptActions_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getApplicationName() const;
    void setApplicationName(const QString &application_name);
    bool is_application_name_Set() const;
    bool is_application_name_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getParameters() const;
    void setParameters(const QString &parameters);
    bool is_parameters_Set() const;
    bool is_parameters_Valid() const;

    QList<QString> getRoles() const;
    void setRoles(const QList<QString> &roles);
    bool is_roles_Set() const;
    bool is_roles_Valid() const;

    QString getUri() const;
    void setUri(const QString &uri);
    bool is_uri_Set() const;
    bool is_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_application_name;
    bool m_application_name_isSet;
    bool m_application_name_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_parameters;
    bool m_parameters_isSet;
    bool m_parameters_isValid;

    QList<QString> m_roles;
    bool m_roles_isSet;
    bool m_roles_isValid;

    QString m_uri;
    bool m_uri_isSet;
    bool m_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIApplicationProperties_installScriptActions_inner)

#endif // OAIApplicationProperties_installScriptActions_inner_H
