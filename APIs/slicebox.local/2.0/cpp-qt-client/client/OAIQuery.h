/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIQuery.h
 *
 * 
 */

#ifndef OAIQuery_H
#define OAIQuery_H

#include <QJsonObject>

#include "OAIQueryFilters.h"
#include "OAIQueryOrder.h"
#include "OAIQueryProperty.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQueryFilters;
class OAIQueryOrder;
class OAIQueryProperty;

class OAIQuery : public OAIObject {
public:
    OAIQuery();
    OAIQuery(QString json);
    ~OAIQuery() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getCount() const;
    void setCount(const qint64 &count);
    bool is_count_Set() const;
    bool is_count_Valid() const;

    OAIQueryFilters getFilters() const;
    void setFilters(const OAIQueryFilters &filters);
    bool is_filters_Set() const;
    bool is_filters_Valid() const;

    OAIQueryOrder getOrder() const;
    void setOrder(const OAIQueryOrder &order);
    bool is_order_Set() const;
    bool is_order_Valid() const;

    QList<OAIQueryProperty> getQueryProperties() const;
    void setQueryProperties(const QList<OAIQueryProperty> &query_properties);
    bool is_query_properties_Set() const;
    bool is_query_properties_Valid() const;

    qint64 getStartIndex() const;
    void setStartIndex(const qint64 &start_index);
    bool is_start_index_Set() const;
    bool is_start_index_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_count;
    bool m_count_isSet;
    bool m_count_isValid;

    OAIQueryFilters m_filters;
    bool m_filters_isSet;
    bool m_filters_isValid;

    OAIQueryOrder m_order;
    bool m_order_isSet;
    bool m_order_isValid;

    QList<OAIQueryProperty> m_query_properties;
    bool m_query_properties_isSet;
    bool m_query_properties_isValid;

    qint64 m_start_index;
    bool m_start_index_isSet;
    bool m_start_index_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIQuery)

#endif // OAIQuery_H
