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
 * OAITable_Borders_Details.h
 *
 * 
 */

#ifndef OAITable_Borders_Details_H
#define OAITable_Borders_Details_H

#include <QJsonObject>

#include "OAIShared_Lines_Details.h"
#include "OAITable_Cells_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIShared_Lines_Details;
class OAITable_Cells_Details;

class OAITable_Borders_Details : public OAIObject {
public:
    OAITable_Borders_Details();
    OAITable_Borders_Details(QString json);
    ~OAITable_Borders_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIShared_Lines_Details getBLtoTr() const;
    void setBLtoTr(const OAIShared_Lines_Details &b_lto_tr);
    bool is_b_lto_tr_Set() const;
    bool is_b_lto_tr_Valid() const;

    OAIShared_Lines_Details getBottom() const;
    void setBottom(const OAIShared_Lines_Details &bottom);
    bool is_bottom_Set() const;
    bool is_bottom_Valid() const;

    OAITable_Cells_Details getCell() const;
    void setCell(const OAITable_Cells_Details &cell);
    bool is_cell_Set() const;
    bool is_cell_Valid() const;

    QString getCellId() const;
    void setCellId(const QString &cell_id);
    bool is_cell_id_Set() const;
    bool is_cell_id_Valid() const;

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

    OAIShared_Lines_Details getLeft() const;
    void setLeft(const OAIShared_Lines_Details &left);
    bool is_left_Set() const;
    bool is_left_Valid() const;

    OAIShared_Lines_Details getRight() const;
    void setRight(const OAIShared_Lines_Details &right);
    bool is_right_Set() const;
    bool is_right_Valid() const;

    OAIShared_Lines_Details getTLtoBr() const;
    void setTLtoBr(const OAIShared_Lines_Details &t_lto_br);
    bool is_t_lto_br_Set() const;
    bool is_t_lto_br_Valid() const;

    OAIShared_Lines_Details getTop() const;
    void setTop(const OAIShared_Lines_Details &top);
    bool is_top_Set() const;
    bool is_top_Valid() const;

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

    OAIShared_Lines_Details m_b_lto_tr;
    bool m_b_lto_tr_isSet;
    bool m_b_lto_tr_isValid;

    OAIShared_Lines_Details m_bottom;
    bool m_bottom_isSet;
    bool m_bottom_isValid;

    OAITable_Cells_Details m_cell;
    bool m_cell_isSet;
    bool m_cell_isValid;

    QString m_cell_id;
    bool m_cell_id_isSet;
    bool m_cell_id_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIShared_Lines_Details m_left;
    bool m_left_isSet;
    bool m_left_isValid;

    OAIShared_Lines_Details m_right;
    bool m_right_isSet;
    bool m_right_isValid;

    OAIShared_Lines_Details m_t_lto_br;
    bool m_t_lto_br_isSet;
    bool m_t_lto_br_isValid;

    OAIShared_Lines_Details m_top;
    bool m_top_isSet;
    bool m_top_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITable_Borders_Details)

#endif // OAITable_Borders_Details_H
