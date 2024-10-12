/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQueryFilters.h
 *
 * 
 */

#ifndef OAIQueryFilters_H
#define OAIQueryFilters_H

#include <QJsonObject>

#include "OAISourceRef.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISourceRef;

class OAIQueryFilters : public OAIObject {
public:
    OAIQueryFilters();
    OAIQueryFilters(QString json);
    ~OAIQueryFilters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<qint64> getSeriesTagIds() const;
    void setSeriesTagIds(const QList<qint64> &series_tag_ids);
    bool is_series_tag_ids_Set() const;
    bool is_series_tag_ids_Valid() const;

    QList<qint64> getSeriesTypeIds() const;
    void setSeriesTypeIds(const QList<qint64> &series_type_ids);
    bool is_series_type_ids_Set() const;
    bool is_series_type_ids_Valid() const;

    QList<OAISourceRef> getSourceRefs() const;
    void setSourceRefs(const QList<OAISourceRef> &source_refs);
    bool is_source_refs_Set() const;
    bool is_source_refs_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<qint64> m_series_tag_ids;
    bool m_series_tag_ids_isSet;
    bool m_series_tag_ids_isValid;

    QList<qint64> m_series_type_ids;
    bool m_series_type_ids_isSet;
    bool m_series_type_ids_isValid;

    QList<OAISourceRef> m_source_refs;
    bool m_source_refs_isSet;
    bool m_source_refs_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQueryFilters)

#endif // OAIQueryFilters_H
