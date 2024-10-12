/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageRegionCreateSummary.h
 *
 * 
 */

#ifndef OAIImageRegionCreateSummary_H
#define OAIImageRegionCreateSummary_H

#include <QJsonObject>

#include "OAIImageRegionCreateEntry.h"
#include "OAIImageRegionCreateResult.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImageRegionCreateResult;
class OAIImageRegionCreateEntry;

class OAIImageRegionCreateSummary : public OAIObject {
public:
    OAIImageRegionCreateSummary();
    OAIImageRegionCreateSummary(QString json);
    ~OAIImageRegionCreateSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIImageRegionCreateResult> getCreated() const;
    void setCreated(const QList<OAIImageRegionCreateResult> &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    QList<OAIImageRegionCreateEntry> getDuplicated() const;
    void setDuplicated(const QList<OAIImageRegionCreateEntry> &duplicated);
    bool is_duplicated_Set() const;
    bool is_duplicated_Valid() const;

    QList<OAIImageRegionCreateEntry> getExceeded() const;
    void setExceeded(const QList<OAIImageRegionCreateEntry> &exceeded);
    bool is_exceeded_Set() const;
    bool is_exceeded_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIImageRegionCreateResult> m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    QList<OAIImageRegionCreateEntry> m_duplicated;
    bool m_duplicated_isSet;
    bool m_duplicated_isValid;

    QList<OAIImageRegionCreateEntry> m_exceeded;
    bool m_exceeded_isSet;
    bool m_exceeded_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageRegionCreateSummary)

#endif // OAIImageRegionCreateSummary_H
