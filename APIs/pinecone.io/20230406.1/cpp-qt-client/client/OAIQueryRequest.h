/**
 * Pinecone API
 * Pinecone is a vector database. This is an unofficial, community-managed OpenAPI spec that (should) accurately model the Pinecone API. This project was developed independent of and is unaffiliated with Pinecone Systems. Users should switch to the official API spec, if and when Pinecone releases it.
 *
 * The version of the OpenAPI document: 20230406.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQueryRequest.h
 *
 * 
 */

#ifndef OAIQueryRequest_H
#define OAIQueryRequest_H

#include <QJsonObject>

#include "OAISparseVectorData.h"
#include <QJsonValue>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISparseVectorData;

class OAIQueryRequest : public OAIObject {
public:
    OAIQueryRequest();
    OAIQueryRequest(QString json);
    ~OAIQueryRequest() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QMap<QString, QJsonValue> getFilter() const;
    void setFilter(const QMap<QString, QJsonValue> &filter);
    bool is_filter_Set() const;
    bool is_filter_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIncludeMetadata() const;
    void setIncludeMetadata(const bool &include_metadata);
    bool is_include_metadata_Set() const;
    bool is_include_metadata_Valid() const;

    bool isIncludeValues() const;
    void setIncludeValues(const bool &include_values);
    bool is_include_values_Set() const;
    bool is_include_values_Valid() const;

    QString getRNamespace() const;
    void setRNamespace(const QString &r_namespace);
    bool is_r_namespace_Set() const;
    bool is_r_namespace_Valid() const;

    OAISparseVectorData getSparseVector() const;
    void setSparseVector(const OAISparseVectorData &sparse_vector);
    bool is_sparse_vector_Set() const;
    bool is_sparse_vector_Valid() const;

    qint64 getTopK() const;
    void setTopK(const qint64 &top_k);
    bool is_top_k_Set() const;
    bool is_top_k_Valid() const;

    QList<float> getVector() const;
    void setVector(const QList<float> &vector);
    bool is_vector_Set() const;
    bool is_vector_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QMap<QString, QJsonValue> m_filter;
    bool m_filter_isSet;
    bool m_filter_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_include_metadata;
    bool m_include_metadata_isSet;
    bool m_include_metadata_isValid;

    bool m_include_values;
    bool m_include_values_isSet;
    bool m_include_values_isValid;

    QString m_r_namespace;
    bool m_r_namespace_isSet;
    bool m_r_namespace_isValid;

    OAISparseVectorData m_sparse_vector;
    bool m_sparse_vector_isSet;
    bool m_sparse_vector_isValid;

    qint64 m_top_k;
    bool m_top_k_isSet;
    bool m_top_k_isValid;

    QList<float> m_vector;
    bool m_vector_isSet;
    bool m_vector_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQueryRequest)

#endif // OAIQueryRequest_H
