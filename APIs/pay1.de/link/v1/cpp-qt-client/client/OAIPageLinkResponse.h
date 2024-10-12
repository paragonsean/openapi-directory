/**
 * PAYONE Link API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * Contact: info@payone.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPageLinkResponse.h
 *
 * 
 */

#ifndef OAIPageLinkResponse_H
#define OAIPageLinkResponse_H

#include <QJsonObject>

#include "OAILinkResponse.h"
#include "OAIPageable.h"
#include "OAISort.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILinkResponse;
class OAIPageable;
class OAISort;

class OAIPageLinkResponse : public OAIObject {
public:
    OAIPageLinkResponse();
    OAIPageLinkResponse(QString json);
    ~OAIPageLinkResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILinkResponse> getContent() const;
    void setContent(const QList<OAILinkResponse> &content);
    bool is_content_Set() const;
    bool is_content_Valid() const;

    bool isEmpty() const;
    void setEmpty(const bool &empty);
    bool is_empty_Set() const;
    bool is_empty_Valid() const;

    bool isFirst() const;
    void setFirst(const bool &first);
    bool is_first_Set() const;
    bool is_first_Valid() const;

    bool isLast() const;
    void setLast(const bool &last);
    bool is_last_Set() const;
    bool is_last_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getNumberOfElements() const;
    void setNumberOfElements(const qint32 &number_of_elements);
    bool is_number_of_elements_Set() const;
    bool is_number_of_elements_Valid() const;

    OAIPageable getPageable() const;
    void setPageable(const OAIPageable &pageable);
    bool is_pageable_Set() const;
    bool is_pageable_Valid() const;

    qint32 getSize() const;
    void setSize(const qint32 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    OAISort getSort() const;
    void setSort(const OAISort &sort);
    bool is_sort_Set() const;
    bool is_sort_Valid() const;

    qint64 getTotalElements() const;
    void setTotalElements(const qint64 &total_elements);
    bool is_total_elements_Set() const;
    bool is_total_elements_Valid() const;

    qint32 getTotalPages() const;
    void setTotalPages(const qint32 &total_pages);
    bool is_total_pages_Set() const;
    bool is_total_pages_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILinkResponse> m_content;
    bool m_content_isSet;
    bool m_content_isValid;

    bool m_empty;
    bool m_empty_isSet;
    bool m_empty_isValid;

    bool m_first;
    bool m_first_isSet;
    bool m_first_isValid;

    bool m_last;
    bool m_last_isSet;
    bool m_last_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_number_of_elements;
    bool m_number_of_elements_isSet;
    bool m_number_of_elements_isValid;

    OAIPageable m_pageable;
    bool m_pageable_isSet;
    bool m_pageable_isValid;

    qint32 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    OAISort m_sort;
    bool m_sort_isSet;
    bool m_sort_isValid;

    qint64 m_total_elements;
    bool m_total_elements_isSet;
    bool m_total_elements_isValid;

    qint32 m_total_pages;
    bool m_total_pages_isSet;
    bool m_total_pages_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPageLinkResponse)

#endif // OAIPageLinkResponse_H
