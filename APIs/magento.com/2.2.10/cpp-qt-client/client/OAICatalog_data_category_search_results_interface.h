/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICatalog_data_category_search_results_interface.h
 *
 * 
 */

#ifndef OAICatalog_data_category_search_results_interface_H
#define OAICatalog_data_category_search_results_interface_H

#include <QJsonObject>

#include "OAICatalog_data_category_interface.h"
#include "OAIFramework_search_criteria_interface.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICatalog_data_category_interface;
class OAIFramework_search_criteria_interface;

class OAICatalog_data_category_search_results_interface : public OAIObject {
public:
    OAICatalog_data_category_search_results_interface();
    OAICatalog_data_category_search_results_interface(QString json);
    ~OAICatalog_data_category_search_results_interface() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICatalog_data_category_interface> getItems() const;
    void setItems(const QList<OAICatalog_data_category_interface> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    OAIFramework_search_criteria_interface getSearchCriteria() const;
    void setSearchCriteria(const OAIFramework_search_criteria_interface &search_criteria);
    bool is_search_criteria_Set() const;
    bool is_search_criteria_Valid() const;

    qint32 getTotalCount() const;
    void setTotalCount(const qint32 &total_count);
    bool is_total_count_Set() const;
    bool is_total_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICatalog_data_category_interface> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    OAIFramework_search_criteria_interface m_search_criteria;
    bool m_search_criteria_isSet;
    bool m_search_criteria_isValid;

    qint32 m_total_count;
    bool m_total_count_isSet;
    bool m_total_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICatalog_data_category_search_results_interface)

#endif // OAICatalog_data_category_search_results_interface_H
