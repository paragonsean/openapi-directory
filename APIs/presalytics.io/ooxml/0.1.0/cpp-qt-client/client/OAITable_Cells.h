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
 * OAITable_Cells.h
 *
 * 
 */

#ifndef OAITable_Cells_H
#define OAITable_Cells_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITable_Cells : public OAIObject {
public:
    OAITable_Cells();
    OAITable_Cells(QString json);
    ~OAITable_Cells() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getColumnId() const;
    void setColumnId(const QString &column_id);
    bool is_column_id_Set() const;
    bool is_column_id_Valid() const;

    qint32 getColumnSpan() const;
    void setColumnSpan(const qint32 &column_span);
    bool is_column_span_Set() const;
    bool is_column_span_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsMergedHorozontal() const;
    void setIsMergedHorozontal(const bool &is_merged_horozontal);
    bool is_is_merged_horozontal_Set() const;
    bool is_is_merged_horozontal_Valid() const;

    bool isIsMergedVertical() const;
    void setIsMergedVertical(const bool &is_merged_vertical);
    bool is_is_merged_vertical_Set() const;
    bool is_is_merged_vertical_Valid() const;

    QString getRowId() const;
    void setRowId(const QString &row_id);
    bool is_row_id_Set() const;
    bool is_row_id_Valid() const;

    qint32 getRowSpan() const;
    void setRowSpan(const qint32 &row_span);
    bool is_row_span_Set() const;
    bool is_row_span_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_column_id;
    bool m_column_id_isSet;
    bool m_column_id_isValid;

    qint32 m_column_span;
    bool m_column_span_isSet;
    bool m_column_span_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_merged_horozontal;
    bool m_is_merged_horozontal_isSet;
    bool m_is_merged_horozontal_isValid;

    bool m_is_merged_vertical;
    bool m_is_merged_vertical_isSet;
    bool m_is_merged_vertical_isValid;

    QString m_row_id;
    bool m_row_id_isSet;
    bool m_row_id_isValid;

    qint32 m_row_span;
    bool m_row_span_isSet;
    bool m_row_span_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITable_Cells)

#endif // OAITable_Cells_H
