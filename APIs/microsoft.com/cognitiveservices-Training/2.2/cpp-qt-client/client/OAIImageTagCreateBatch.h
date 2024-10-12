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
 * OAIImageTagCreateBatch.h
 *
 * Batch of image tags.
 */

#ifndef OAIImageTagCreateBatch_H
#define OAIImageTagCreateBatch_H

#include <QJsonObject>

#include "OAIImageTagCreateEntry.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImageTagCreateEntry;

class OAIImageTagCreateBatch : public OAIObject {
public:
    OAIImageTagCreateBatch();
    OAIImageTagCreateBatch(QString json);
    ~OAIImageTagCreateBatch() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIImageTagCreateEntry> getTags() const;
    void setTags(const QList<OAIImageTagCreateEntry> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIImageTagCreateEntry> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageTagCreateBatch)

#endif // OAIImageTagCreateBatch_H
