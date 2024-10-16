/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIKeywordJobRank.h
 *
 * 
 */

#ifndef OAIKeywordJobRank_H
#define OAIKeywordJobRank_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIKeywordJobRank : public OAIObject {
public:
    OAIKeywordJobRank();
    OAIKeywordJobRank(QString json);
    ~OAIKeywordJobRank() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDomain() const;
    void setDomain(const QString &domain);
    bool is_domain_Set() const;
    bool is_domain_Valid() const;

    QString getKeyword() const;
    void setKeyword(const QString &keyword);
    bool is_keyword_Set() const;
    bool is_keyword_Valid() const;

    QString getLocalizationCode() const;
    void setLocalizationCode(const QString &localization_code);
    bool is_localization_code_Set() const;
    bool is_localization_code_Valid() const;

    QString getLocalizationZip() const;
    void setLocalizationZip(const QString &localization_zip);
    bool is_localization_zip_Set() const;
    bool is_localization_zip_Valid() const;

    QString getSearchEngine() const;
    void setSearchEngine(const QString &search_engine);
    bool is_search_engine_Set() const;
    bool is_search_engine_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_domain;
    bool m_domain_isSet;
    bool m_domain_isValid;

    QString m_keyword;
    bool m_keyword_isSet;
    bool m_keyword_isValid;

    QString m_localization_code;
    bool m_localization_code_isSet;
    bool m_localization_code_isValid;

    QString m_localization_zip;
    bool m_localization_zip_isSet;
    bool m_localization_zip_isValid;

    QString m_search_engine;
    bool m_search_engine_isSet;
    bool m_search_engine_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIKeywordJobRank)

#endif // OAIKeywordJobRank_H
