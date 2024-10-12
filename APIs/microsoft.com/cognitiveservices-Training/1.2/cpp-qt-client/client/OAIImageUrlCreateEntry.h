/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageUrlCreateEntry.h
 *
 * 
 */

#ifndef OAIImageUrlCreateEntry_H
#define OAIImageUrlCreateEntry_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageUrlCreateEntry : public OAIObject {
public:
    OAIImageUrlCreateEntry();
    OAIImageUrlCreateEntry(QString json);
    ~OAIImageUrlCreateEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getTagIds() const;
    void setTagIds(const QList<QString> &tag_ids);
    bool is_tag_ids_Set() const;
    bool is_tag_ids_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_tag_ids;
    bool m_tag_ids_isSet;
    bool m_tag_ids_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageUrlCreateEntry)

#endif // OAIImageUrlCreateEntry_H
