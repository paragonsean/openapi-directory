/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICategory.h
 *
 * 
 */

#ifndef OAICategory_H
#define OAICategory_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICategory : public OAIObject {
public:
    OAICategory();
    OAICategory(QString json);
    ~OAICategory() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint64 getParentId() const;
    void setParentId(const qint64 &parent_id);
    bool is_parent_id_Set() const;
    bool is_parent_id_Valid() const;

    QString getPath() const;
    void setPath(const QString &path);
    bool is_path_Set() const;
    bool is_path_Valid() const;

    QString getSourceId() const;
    void setSourceId(const QString &source_id);
    bool is_source_id_Set() const;
    bool is_source_id_Valid() const;

    qint64 getTaxonomyId() const;
    void setTaxonomyId(const qint64 &taxonomy_id);
    bool is_taxonomy_id_Set() const;
    bool is_taxonomy_id_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint64 m_parent_id;
    bool m_parent_id_isSet;
    bool m_parent_id_isValid;

    QString m_path;
    bool m_path_isSet;
    bool m_path_isValid;

    QString m_source_id;
    bool m_source_id_isSet;
    bool m_source_id_isValid;

    qint64 m_taxonomy_id;
    bool m_taxonomy_id_isSet;
    bool m_taxonomy_id_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICategory)

#endif // OAICategory_H
