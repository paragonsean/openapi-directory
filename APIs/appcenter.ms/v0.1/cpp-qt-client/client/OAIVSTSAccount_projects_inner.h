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
 * OAIVSTSAccount_projects_inner.h
 *
 * VSTS project
 */

#ifndef OAIVSTSAccount_projects_inner_H
#define OAIVSTSAccount_projects_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIVSTSAccount_projects_inner : public OAIObject {
public:
    OAIVSTSAccount_projects_inner();
    OAIVSTSAccount_projects_inner(QString json);
    ~OAIVSTSAccount_projects_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    QString getVisibility() const;
    void setVisibility(const QString &visibility);
    bool is_visibility_Set() const;
    bool is_visibility_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    QString m_visibility;
    bool m_visibility_isSet;
    bool m_visibility_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIVSTSAccount_projects_inner)

#endif // OAIVSTSAccount_projects_inner_H
