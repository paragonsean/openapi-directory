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
 * OAIShared_TextContainer.h
 *
 * 
 */

#ifndef OAIShared_TextContainer_H
#define OAIShared_TextContainer_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIShared_TextContainer : public OAIObject {
public:
    OAIShared_TextContainer();
    OAIShared_TextContainer(QString json);
    ~OAIShared_TextContainer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAxisId() const;
    void setAxisId(const QString &axis_id);
    bool is_axis_id_Set() const;
    bool is_axis_id_Valid() const;

    QString getChartId() const;
    void setChartId(const QString &chart_id);
    bool is_chart_id_Set() const;
    bool is_chart_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getOuterXml() const;
    void setOuterXml(const QString &outer_xml);
    bool is_outer_xml_Set() const;
    bool is_outer_xml_Valid() const;

    QString getShapeId() const;
    void setShapeId(const QString &shape_id);
    bool is_shape_id_Set() const;
    bool is_shape_id_Valid() const;

    QString getTableCellId() const;
    void setTableCellId(const QString &table_cell_id);
    bool is_table_cell_id_Set() const;
    bool is_table_cell_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_axis_id;
    bool m_axis_id_isSet;
    bool m_axis_id_isValid;

    QString m_chart_id;
    bool m_chart_id_isSet;
    bool m_chart_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_outer_xml;
    bool m_outer_xml_isSet;
    bool m_outer_xml_isValid;

    QString m_shape_id;
    bool m_shape_id_isSet;
    bool m_shape_id_isValid;

    QString m_table_cell_id;
    bool m_table_cell_id_isSet;
    bool m_table_cell_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShared_TextContainer)

#endif // OAIShared_TextContainer_H
