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
 * OAISystemVersionNameGroups_inner.h
 *
 * A response represents information about symbol name group
 */

#ifndef OAISystemVersionNameGroups_inner_H
#define OAISystemVersionNameGroups_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISystemVersionNameGroups_inner : public OAIObject {
public:
    OAISystemVersionNameGroups_inner();
    OAISystemVersionNameGroups_inner(QString json);
    ~OAISystemVersionNameGroups_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<QString> getVersions() const;
    void setVersions(const QList<QString> &versions);
    bool is_versions_Set() const;
    bool is_versions_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<QString> m_versions;
    bool m_versions_isSet;
    bool m_versions_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISystemVersionNameGroups_inner)

#endif // OAISystemVersionNameGroups_inner_H
