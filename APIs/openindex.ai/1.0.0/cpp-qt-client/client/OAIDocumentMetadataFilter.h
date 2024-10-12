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
 * OAIDocumentMetadataFilter.h
 *
 * 
 */

#ifndef OAIDocumentMetadataFilter_H
#define OAIDocumentMetadataFilter_H

#include <QJsonObject>

#include "OAISource.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDocumentMetadataFilter : public OAIObject {
public:
    OAIDocumentMetadataFilter();
    OAIDocumentMetadataFilter(QString json);
    ~OAIDocumentMetadataFilter() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAuthor() const;
    void setAuthor(const QString &author);
    bool is_author_Set() const;
    bool is_author_Valid() const;

    QString getCollectionId() const;
    void setCollectionId(const QString &collection_id);
    bool is_collection_id_Set() const;
    bool is_collection_id_Valid() const;

    QString getDocumentId() const;
    void setDocumentId(const QString &document_id);
    bool is_document_id_Set() const;
    bool is_document_id_Valid() const;

    QString getEndDate() const;
    void setEndDate(const QString &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    QList<QString> getKeywords() const;
    void setKeywords(const QList<QString> &keywords);
    bool is_keywords_Set() const;
    bool is_keywords_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    OAISource getSource() const;
    void setSource(const OAISource &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getSourceId() const;
    void setSourceId(const QString &source_id);
    bool is_source_id_Set() const;
    bool is_source_id_Valid() const;

    QString getStartDate() const;
    void setStartDate(const QString &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    QString getTimePeriod() const;
    void setTimePeriod(const QString &time_period);
    bool is_time_period_Set() const;
    bool is_time_period_Valid() const;

    QString getUserId() const;
    void setUserId(const QString &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_author;
    bool m_author_isSet;
    bool m_author_isValid;

    QString m_collection_id;
    bool m_collection_id_isSet;
    bool m_collection_id_isValid;

    QString m_document_id;
    bool m_document_id_isSet;
    bool m_document_id_isValid;

    QString m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    QList<QString> m_keywords;
    bool m_keywords_isSet;
    bool m_keywords_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    OAISource m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_source_id;
    bool m_source_id_isSet;
    bool m_source_id_isValid;

    QString m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    QString m_time_period;
    bool m_time_period_isSet;
    bool m_time_period_isValid;

    QString m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDocumentMetadataFilter)

#endif // OAIDocumentMetadataFilter_H
