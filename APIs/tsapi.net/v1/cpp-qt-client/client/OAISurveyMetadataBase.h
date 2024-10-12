/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISurveyMetadataBase.h
 *
 * 
 */

#ifndef OAISurveyMetadataBase_H
#define OAISurveyMetadataBase_H

#include <QJsonObject>

#include "OAILanguage.h"
#include "OAIVariable.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILanguage;
class OAIVariable;

class OAISurveyMetadataBase : public OAIObject {
public:
    OAISurveyMetadataBase();
    OAISurveyMetadataBase(QString json);
    ~OAISurveyMetadataBase() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getInterviewCount() const;
    void setInterviewCount(const qint32 &interview_count);
    bool is_interview_count_Set() const;
    bool is_interview_count_Valid() const;

    QList<OAILanguage> getLanguages() const;
    void setLanguages(const QList<OAILanguage> &languages);
    bool is_languages_Set() const;
    bool is_languages_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QList<OAIVariable> getVariables() const;
    void setVariables(const QList<OAIVariable> &variables);
    bool is_variables_Set() const;
    bool is_variables_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_interview_count;
    bool m_interview_count_isSet;
    bool m_interview_count_isValid;

    QList<OAILanguage> m_languages;
    bool m_languages_isSet;
    bool m_languages_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QList<OAIVariable> m_variables;
    bool m_variables_isSet;
    bool m_variables_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISurveyMetadataBase)

#endif // OAISurveyMetadataBase_H
