/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITVShowActor.h
 *
 * 
 */

#ifndef OAITVShowActor_H
#define OAITVShowActor_H

#include <QJsonObject>

#include "OAIExternalIDs.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExternalIDs;

class OAITVShowActor : public OAIObject {
public:
    OAITVShowActor();
    OAITVShowActor(QString json);
    ~OAITVShowActor() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIExternalIDs> getExternals() const;
    void setExternals(const QList<OAIExternalIDs> &externals);
    bool is_externals_Set() const;
    bool is_externals_Valid() const;

    QString getImage() const;
    void setImage(const QString &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getRole() const;
    void setRole(const QString &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    QString getShowName() const;
    void setShowName(const QString &show_name);
    bool is_show_name_Set() const;
    bool is_show_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIExternalIDs> m_externals;
    bool m_externals_isSet;
    bool m_externals_isValid;

    QString m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_role;
    bool m_role_isSet;
    bool m_role_isValid;

    QString m_show_name;
    bool m_show_name_isSet;
    bool m_show_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITVShowActor)

#endif // OAITVShowActor_H
