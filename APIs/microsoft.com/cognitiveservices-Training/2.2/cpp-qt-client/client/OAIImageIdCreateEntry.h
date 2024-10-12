/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageIdCreateEntry.h
 *
 * 
 */

#ifndef OAIImageIdCreateEntry_H
#define OAIImageIdCreateEntry_H

#include <QJsonObject>

#include "OAIRegion.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRegion;

class OAIImageIdCreateEntry : public OAIObject {
public:
    OAIImageIdCreateEntry();
    OAIImageIdCreateEntry(QString json);
    ~OAIImageIdCreateEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIRegion> getRegions() const;
    void setRegions(const QList<OAIRegion> &regions);
    bool is_regions_Set() const;
    bool is_regions_Valid() const;

    QList<QString> getTagIds() const;
    void setTagIds(const QList<QString> &tag_ids);
    bool is_tag_ids_Set() const;
    bool is_tag_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIRegion> m_regions;
    bool m_regions_isSet;
    bool m_regions_isValid;

    QList<QString> m_tag_ids;
    bool m_tag_ids_isSet;
    bool m_tag_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageIdCreateEntry)

#endif // OAIImageIdCreateEntry_H
