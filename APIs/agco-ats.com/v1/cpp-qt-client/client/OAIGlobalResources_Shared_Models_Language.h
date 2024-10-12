/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGlobalResources_Shared_Models_Language.h
 *
 * A language used for string translations.
 */

#ifndef OAIGlobalResources_Shared_Models_Language_H
#define OAIGlobalResources_Shared_Models_Language_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGlobalResources_Shared_Models_Language : public OAIObject {
public:
    OAIGlobalResources_Shared_Models_Language();
    OAIGlobalResources_Shared_Models_Language(QString json);
    ~OAIGlobalResources_Shared_Models_Language() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isIsDeleted() const;
    void setIsDeleted(const bool &is_deleted);
    bool is_is_deleted_Set() const;
    bool is_is_deleted_Valid() const;

    qint32 getLocaleId() const;
    void setLocaleId(const qint32 &locale_id);
    bool is_locale_id_Set() const;
    bool is_locale_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_is_deleted;
    bool m_is_deleted_isSet;
    bool m_is_deleted_isValid;

    qint32 m_locale_id;
    bool m_locale_id_isSet;
    bool m_locale_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGlobalResources_Shared_Models_Language)

#endif // OAIGlobalResources_Shared_Models_Language_H
