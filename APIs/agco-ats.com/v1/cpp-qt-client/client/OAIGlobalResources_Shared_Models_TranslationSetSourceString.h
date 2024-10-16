/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGlobalResources_Shared_Models_TranslationSetSourceString.h
 *
 * Information needed to translate a string in a translation set
 */

#ifndef OAIGlobalResources_Shared_Models_TranslationSetSourceString_H
#define OAIGlobalResources_Shared_Models_TranslationSetSourceString_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGlobalResources_Shared_Models_TranslationSetSourceString : public OAIObject {
public:
    OAIGlobalResources_Shared_Models_TranslationSetSourceString();
    OAIGlobalResources_Shared_Models_TranslationSetSourceString(QString json);
    ~OAIGlobalResources_Shared_Models_TranslationSetSourceString() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDescriptionForTranslator() const;
    void setDescriptionForTranslator(const QString &description_for_translator);
    bool is_description_for_translator_Set() const;
    bool is_description_for_translator_Valid() const;

    qint32 getLanguageId() const;
    void setLanguageId(const qint32 &language_id);
    bool is_language_id_Set() const;
    bool is_language_id_Valid() const;

    QString getStringId() const;
    void setStringId(const QString &string_id);
    bool is_string_id_Set() const;
    bool is_string_id_Valid() const;

    QString getStringValue() const;
    void setStringValue(const QString &string_value);
    bool is_string_value_Set() const;
    bool is_string_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_description_for_translator;
    bool m_description_for_translator_isSet;
    bool m_description_for_translator_isValid;

    qint32 m_language_id;
    bool m_language_id_isSet;
    bool m_language_id_isValid;

    QString m_string_id;
    bool m_string_id_isSet;
    bool m_string_id_isValid;

    QString m_string_value;
    bool m_string_value_isSet;
    bool m_string_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGlobalResources_Shared_Models_TranslationSetSourceString)

#endif // OAIGlobalResources_Shared_Models_TranslationSetSourceString_H
