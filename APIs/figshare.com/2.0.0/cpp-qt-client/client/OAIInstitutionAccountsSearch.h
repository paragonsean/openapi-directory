/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInstitutionAccountsSearch.h
 *
 * 
 */

#ifndef OAIInstitutionAccountsSearch_H
#define OAIInstitutionAccountsSearch_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIInstitutionAccountsSearch : public OAIObject {
public:
    OAIInstitutionAccountsSearch();
    OAIInstitutionAccountsSearch(QString json);
    ~OAIInstitutionAccountsSearch() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEmail() const;
    void setEmail(const QString &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    QString getInstitutionUserId() const;
    void setInstitutionUserId(const QString &institution_user_id);
    bool is_institution_user_id_Set() const;
    bool is_institution_user_id_Valid() const;

    qint64 getIsActive() const;
    void setIsActive(const qint64 &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    qint64 getLimit() const;
    void setLimit(const qint64 &limit);
    bool is_limit_Set() const;
    bool is_limit_Valid() const;

    qint64 getOffset() const;
    void setOffset(const qint64 &offset);
    bool is_offset_Set() const;
    bool is_offset_Valid() const;

    qint64 getPage() const;
    void setPage(const qint64 &page);
    bool is_page_Set() const;
    bool is_page_Valid() const;

    qint64 getPageSize() const;
    void setPageSize(const qint64 &page_size);
    bool is_page_size_Set() const;
    bool is_page_size_Valid() const;

    QString getSearchFor() const;
    void setSearchFor(const QString &search_for);
    bool is_search_for_Set() const;
    bool is_search_for_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_email;
    bool m_email_isSet;
    bool m_email_isValid;

    QString m_institution_user_id;
    bool m_institution_user_id_isSet;
    bool m_institution_user_id_isValid;

    qint64 m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    qint64 m_limit;
    bool m_limit_isSet;
    bool m_limit_isValid;

    qint64 m_offset;
    bool m_offset_isSet;
    bool m_offset_isValid;

    qint64 m_page;
    bool m_page_isSet;
    bool m_page_isValid;

    qint64 m_page_size;
    bool m_page_size_isSet;
    bool m_page_size_isValid;

    QString m_search_for;
    bool m_search_for_isSet;
    bool m_search_for_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInstitutionAccountsSearch)

#endif // OAIInstitutionAccountsSearch_H
