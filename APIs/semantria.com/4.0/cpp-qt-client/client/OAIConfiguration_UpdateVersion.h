/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConfiguration_UpdateVersion.h
 *
 * 
 */

#ifndef OAIConfiguration_UpdateVersion_H
#define OAIConfiguration_UpdateVersion_H

#include <QJsonObject>

#include "OAIConfigurationCollectionSection.h"
#include "OAIConfigurationDocumentSection.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIConfigurationCollectionSection;
class OAIConfigurationDocumentSection;

class OAIConfiguration_UpdateVersion : public OAIObject {
public:
    OAIConfiguration_UpdateVersion();
    OAIConfiguration_UpdateVersion(QString json);
    ~OAIConfiguration_UpdateVersion() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAutoResponse() const;
    void setAutoResponse(const bool &auto_response);
    bool is_auto_response_Set() const;
    bool is_auto_response_Valid() const;

    QString getCallback() const;
    void setCallback(const QString &callback);
    bool is_callback_Set() const;
    bool is_callback_Valid() const;

    double getCategoriesThreshold() const;
    void setCategoriesThreshold(const double &categories_threshold);
    bool is_categories_threshold_Set() const;
    bool is_categories_threshold_Valid() const;

    qint32 getCharsThreshold() const;
    void setCharsThreshold(const qint32 &chars_threshold);
    bool is_chars_threshold_Set() const;
    bool is_chars_threshold_Valid() const;

    OAIConfigurationCollectionSection getCollection() const;
    void setCollection(const OAIConfigurationCollectionSection &collection);
    bool is_collection_Set() const;
    bool is_collection_Valid() const;

    QString getConfigId() const;
    void setConfigId(const QString &config_id);
    bool is_config_id_Set() const;
    bool is_config_id_Valid() const;

    OAIConfigurationDocumentSection getDocument() const;
    void setDocument(const OAIConfigurationDocumentSection &document);
    bool is_document_Set() const;
    bool is_document_Valid() const;

    qint32 getEntitiesThreshold() const;
    void setEntitiesThreshold(const qint32 &entities_threshold);
    bool is_entities_threshold_Set() const;
    bool is_entities_threshold_Valid() const;

    bool isIsPrimary() const;
    void setIsPrimary(const bool &is_primary);
    bool is_is_primary_Set() const;
    bool is_is_primary_Valid() const;

    QString getLanguage() const;
    void setLanguage(const QString &language);
    bool is_language_Set() const;
    bool is_language_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    bool isOneSentence() const;
    void setOneSentence(const bool &one_sentence);
    bool is_one_sentence_Set() const;
    bool is_one_sentence_Valid() const;

    bool isProcessHtml() const;
    void setProcessHtml(const bool &process_html);
    bool is_process_html_Set() const;
    bool is_process_html_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_auto_response;
    bool m_auto_response_isSet;
    bool m_auto_response_isValid;

    QString m_callback;
    bool m_callback_isSet;
    bool m_callback_isValid;

    double m_categories_threshold;
    bool m_categories_threshold_isSet;
    bool m_categories_threshold_isValid;

    qint32 m_chars_threshold;
    bool m_chars_threshold_isSet;
    bool m_chars_threshold_isValid;

    OAIConfigurationCollectionSection m_collection;
    bool m_collection_isSet;
    bool m_collection_isValid;

    QString m_config_id;
    bool m_config_id_isSet;
    bool m_config_id_isValid;

    OAIConfigurationDocumentSection m_document;
    bool m_document_isSet;
    bool m_document_isValid;

    qint32 m_entities_threshold;
    bool m_entities_threshold_isSet;
    bool m_entities_threshold_isValid;

    bool m_is_primary;
    bool m_is_primary_isSet;
    bool m_is_primary_isValid;

    QString m_language;
    bool m_language_isSet;
    bool m_language_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    bool m_one_sentence;
    bool m_one_sentence_isSet;
    bool m_one_sentence_isValid;

    bool m_process_html;
    bool m_process_html_isSet;
    bool m_process_html_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfiguration_UpdateVersion)

#endif // OAIConfiguration_UpdateVersion_H
