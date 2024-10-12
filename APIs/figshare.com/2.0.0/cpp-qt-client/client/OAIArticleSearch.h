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
 * OAIArticleSearch.h
 *
 * 
 */

#ifndef OAIArticleSearch_H
#define OAIArticleSearch_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArticleSearch : public OAIObject {
public:
    OAIArticleSearch();
    OAIArticleSearch(QString json);
    ~OAIArticleSearch() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDoi() const;
    void setDoi(const QString &doi);
    bool is_doi_Set() const;
    bool is_doi_Valid() const;

    QString getHandle() const;
    void setHandle(const QString &handle);
    bool is_handle_Set() const;
    bool is_handle_Valid() const;

    qint64 getItemType() const;
    void setItemType(const qint64 &item_type);
    bool is_item_type_Set() const;
    bool is_item_type_Valid() const;

    QString getOrder() const;
    void setOrder(const QString &order);
    bool is_order_Set() const;
    bool is_order_Valid() const;

    qint64 getProjectId() const;
    void setProjectId(const qint64 &project_id);
    bool is_project_id_Set() const;
    bool is_project_id_Valid() const;

    QString getResourceDoi() const;
    void setResourceDoi(const QString &resource_doi);
    bool is_resource_doi_Set() const;
    bool is_resource_doi_Valid() const;

    qint32 getGroup() const;
    void setGroup(const qint32 &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    qint32 getInstitution() const;
    void setInstitution(const qint32 &institution);
    bool is_institution_Set() const;
    bool is_institution_Valid() const;

    qint64 getLimit() const;
    void setLimit(const qint64 &limit);
    bool is_limit_Set() const;
    bool is_limit_Valid() const;

    QString getModifiedSince() const;
    void setModifiedSince(const QString &modified_since);
    bool is_modified_since_Set() const;
    bool is_modified_since_Valid() const;

    qint64 getOffset() const;
    void setOffset(const qint64 &offset);
    bool is_offset_Set() const;
    bool is_offset_Valid() const;

    QString getOrderDirection() const;
    void setOrderDirection(const QString &order_direction);
    bool is_order_direction_Set() const;
    bool is_order_direction_Valid() const;

    qint64 getPage() const;
    void setPage(const qint64 &page);
    bool is_page_Set() const;
    bool is_page_Valid() const;

    qint64 getPageSize() const;
    void setPageSize(const qint64 &page_size);
    bool is_page_size_Set() const;
    bool is_page_size_Valid() const;

    QString getPublishedSince() const;
    void setPublishedSince(const QString &published_since);
    bool is_published_since_Set() const;
    bool is_published_since_Valid() const;

    QString getSearchFor() const;
    void setSearchFor(const QString &search_for);
    bool is_search_for_Set() const;
    bool is_search_for_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_doi;
    bool m_doi_isSet;
    bool m_doi_isValid;

    QString m_handle;
    bool m_handle_isSet;
    bool m_handle_isValid;

    qint64 m_item_type;
    bool m_item_type_isSet;
    bool m_item_type_isValid;

    QString m_order;
    bool m_order_isSet;
    bool m_order_isValid;

    qint64 m_project_id;
    bool m_project_id_isSet;
    bool m_project_id_isValid;

    QString m_resource_doi;
    bool m_resource_doi_isSet;
    bool m_resource_doi_isValid;

    qint32 m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    qint32 m_institution;
    bool m_institution_isSet;
    bool m_institution_isValid;

    qint64 m_limit;
    bool m_limit_isSet;
    bool m_limit_isValid;

    QString m_modified_since;
    bool m_modified_since_isSet;
    bool m_modified_since_isValid;

    qint64 m_offset;
    bool m_offset_isSet;
    bool m_offset_isValid;

    QString m_order_direction;
    bool m_order_direction_isSet;
    bool m_order_direction_isValid;

    qint64 m_page;
    bool m_page_isSet;
    bool m_page_isValid;

    qint64 m_page_size;
    bool m_page_size_isSet;
    bool m_page_size_isValid;

    QString m_published_since;
    bool m_published_since_isSet;
    bool m_published_since_isValid;

    QString m_search_for;
    bool m_search_for_isSet;
    bool m_search_for_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArticleSearch)

#endif // OAIArticleSearch_H
