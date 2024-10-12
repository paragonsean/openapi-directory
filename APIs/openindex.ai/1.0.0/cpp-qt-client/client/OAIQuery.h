/**
 * OpenIndex Retrieval Plugin API
 * A retrieval API for querying and filtering documents based on natural language queries and metadata
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQuery.h
 *
 * 
 */

#ifndef OAIQuery_H
#define OAIQuery_H

#include <QJsonObject>

#include "OAIDocumentMetadataFilter.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDocumentMetadataFilter;

class OAIQuery : public OAIObject {
public:
    OAIQuery();
    OAIQuery(QString json);
    ~OAIQuery() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIDocumentMetadataFilter getFilter() const;
    void setFilter(const OAIDocumentMetadataFilter &filter);
    bool is_filter_Set() const;
    bool is_filter_Valid() const;

    QString getQuery() const;
    void setQuery(const QString &query);
    bool is_query_Set() const;
    bool is_query_Valid() const;

    qint32 getTopK() const;
    void setTopK(const qint32 &top_k);
    bool is_top_k_Set() const;
    bool is_top_k_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIDocumentMetadataFilter m_filter;
    bool m_filter_isSet;
    bool m_filter_isValid;

    QString m_query;
    bool m_query_isSet;
    bool m_query_isValid;

    qint32 m_top_k;
    bool m_top_k_isSet;
    bool m_top_k_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuery)

#endif // OAIQuery_H
