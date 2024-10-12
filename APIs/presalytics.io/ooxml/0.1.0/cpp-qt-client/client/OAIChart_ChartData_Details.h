/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIChart_ChartData_Details.h
 *
 * 
 */

#ifndef OAIChart_ChartData_Details_H
#define OAIChart_ChartData_Details_H

#include <QJsonObject>

#include "OAIChart_Charts_Details.h"
#include "OAIChart_ColumnCollections_Details.h"
#include "OAIChart_DataPoints_Details.h"
#include "OAIChart_RowCollections_Details.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIChart_Charts_Details;
class OAIChart_ColumnCollections_Details;
class OAIChart_DataPoints_Details;
class OAIChart_RowCollections_Details;

class OAIChart_ChartData_Details : public OAIObject {
public:
    OAIChart_ChartData_Details();
    OAIChart_ChartData_Details(QString json);
    ~OAIChart_ChartData_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIChart_Charts_Details getChart() const;
    void setChart(const OAIChart_Charts_Details &chart);
    bool is_chart_Set() const;
    bool is_chart_Valid() const;

    QString getChartId() const;
    void setChartId(const QString &chart_id);
    bool is_chart_id_Set() const;
    bool is_chart_id_Valid() const;

    OAIChart_ColumnCollections_Details getColumnCollection() const;
    void setColumnCollection(const OAIChart_ColumnCollections_Details &column_collection);
    bool is_column_collection_Set() const;
    bool is_column_collection_Valid() const;

    QList<OAIChart_DataPoints_Details> getDataPoints() const;
    void setDataPoints(const QList<OAIChart_DataPoints_Details> &data_points);
    bool is_data_points_Set() const;
    bool is_data_points_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateModified() const;
    void setDateModified(const QDateTime &date_modified);
    bool is_date_modified_Set() const;
    bool is_date_modified_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIChart_RowCollections_Details getRowCollection() const;
    void setRowCollection(const OAIChart_RowCollections_Details &row_collection);
    bool is_row_collection_Set() const;
    bool is_row_collection_Valid() const;

    QString getUserCreated() const;
    void setUserCreated(const QString &user_created);
    bool is_user_created_Set() const;
    bool is_user_created_Valid() const;

    QString getUserModified() const;
    void setUserModified(const QString &user_modified);
    bool is_user_modified_Set() const;
    bool is_user_modified_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIChart_Charts_Details m_chart;
    bool m_chart_isSet;
    bool m_chart_isValid;

    QString m_chart_id;
    bool m_chart_id_isSet;
    bool m_chart_id_isValid;

    OAIChart_ColumnCollections_Details m_column_collection;
    bool m_column_collection_isSet;
    bool m_column_collection_isValid;

    QList<OAIChart_DataPoints_Details> m_data_points;
    bool m_data_points_isSet;
    bool m_data_points_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIChart_RowCollections_Details m_row_collection;
    bool m_row_collection_isSet;
    bool m_row_collection_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIChart_ChartData_Details)

#endif // OAIChart_ChartData_Details_H
