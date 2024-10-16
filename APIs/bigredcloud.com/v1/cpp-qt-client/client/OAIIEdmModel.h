/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIEdmModel.h
 *
 * 
 */

#ifndef OAIIEdmModel_H
#define OAIIEdmModel_H

#include <QJsonObject>

#include "OAIIEdmSchemaElement.h"
#include "OAIIEdmVocabularyAnnotation.h"
#include "OAIObject.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIEdmSchemaElement;
class OAIIEdmVocabularyAnnotation;

class OAIIEdmModel : public OAIObject {
public:
    OAIIEdmModel();
    OAIIEdmModel(QString json);
    ~OAIIEdmModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getDirectValueAnnotationsManager() const;
    void setDirectValueAnnotationsManager(const OAIObject &direct_value_annotations_manager);
    bool is_direct_value_annotations_manager_Set() const;
    bool is_direct_value_annotations_manager_Valid() const;

    QList<OAIIEdmModel> getReferencedModels() const;
    void setReferencedModels(const QList<OAIIEdmModel> &referenced_models);
    bool is_referenced_models_Set() const;
    bool is_referenced_models_Valid() const;

    QList<OAIIEdmSchemaElement> getSchemaElements() const;
    void setSchemaElements(const QList<OAIIEdmSchemaElement> &schema_elements);
    bool is_schema_elements_Set() const;
    bool is_schema_elements_Valid() const;

    QList<OAIIEdmVocabularyAnnotation> getVocabularyAnnotations() const;
    void setVocabularyAnnotations(const QList<OAIIEdmVocabularyAnnotation> &vocabulary_annotations);
    bool is_vocabulary_annotations_Set() const;
    bool is_vocabulary_annotations_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_direct_value_annotations_manager;
    bool m_direct_value_annotations_manager_isSet;
    bool m_direct_value_annotations_manager_isValid;

    QList<OAIIEdmModel> m_referenced_models;
    bool m_referenced_models_isSet;
    bool m_referenced_models_isValid;

    QList<OAIIEdmSchemaElement> m_schema_elements;
    bool m_schema_elements_isSet;
    bool m_schema_elements_isValid;

    QList<OAIIEdmVocabularyAnnotation> m_vocabulary_annotations;
    bool m_vocabulary_annotations_isSet;
    bool m_vocabulary_annotations_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIEdmModel)

#endif // OAIIEdmModel_H
