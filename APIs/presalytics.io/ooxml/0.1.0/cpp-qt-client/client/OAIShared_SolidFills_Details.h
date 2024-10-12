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
 * OAIShared_SolidFills_Details.h
 *
 * 
 */

#ifndef OAIShared_SolidFills_Details_H
#define OAIShared_SolidFills_Details_H

#include <QJsonObject>

#include "OAIShared_ColorTransformations_Details.h"
#include "OAIShared_FillMap_Details.h"
#include "OAIShared_GradientStops_Details.h"
#include "OAIShared_Lines_Details.h"
#include "OAIShared_Text_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIShared_ColorTransformations_Details;
class OAIShared_FillMap_Details;
class OAIShared_GradientStops_Details;
class OAIShared_Lines_Details;
class OAIShared_Text_Details;

class OAIShared_SolidFills_Details : public OAIObject {
public:
    OAIShared_SolidFills_Details();
    OAIShared_SolidFills_Details(QString json);
    ~OAIShared_SolidFills_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIShared_ColorTransformations_Details getColorTransformations() const;
    void setColorTransformations(const OAIShared_ColorTransformations_Details &color_transformations);
    bool is_color_transformations_Set() const;
    bool is_color_transformations_Valid() const;

    qint32 getColorTypeId() const;
    void setColorTypeId(const qint32 &color_type_id);
    bool is_color_type_id_Set() const;
    bool is_color_type_id_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateModified() const;
    void setDateModified(const QDateTime &date_modified);
    bool is_date_modified_Set() const;
    bool is_date_modified_Valid() const;

    QString getFillMapId() const;
    void setFillMapId(const QString &fill_map_id);
    bool is_fill_map_id_Set() const;
    bool is_fill_map_id_Valid() const;

    QString getHexValue() const;
    void setHexValue(const QString &hex_value);
    bool is_hex_value_Set() const;
    bool is_hex_value_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsUserColor() const;
    void setIsUserColor(const bool &is_user_color);
    bool is_is_user_color_Set() const;
    bool is_is_user_color_Valid() const;

    OAIShared_FillMap_Details getParentFillMap() const;
    void setParentFillMap(const OAIShared_FillMap_Details &parent_fill_map);
    bool is_parent_fill_map_Set() const;
    bool is_parent_fill_map_Valid() const;

    OAIShared_GradientStops_Details getParentGradientStop() const;
    void setParentGradientStop(const OAIShared_GradientStops_Details &parent_gradient_stop);
    bool is_parent_gradient_stop_Set() const;
    bool is_parent_gradient_stop_Valid() const;

    QString getParentGradientStopId() const;
    void setParentGradientStopId(const QString &parent_gradient_stop_id);
    bool is_parent_gradient_stop_id_Set() const;
    bool is_parent_gradient_stop_id_Valid() const;

    OAIShared_Lines_Details getParentLine() const;
    void setParentLine(const OAIShared_Lines_Details &parent_line);
    bool is_parent_line_Set() const;
    bool is_parent_line_Valid() const;

    QString getParentLineId() const;
    void setParentLineId(const QString &parent_line_id);
    bool is_parent_line_id_Set() const;
    bool is_parent_line_id_Valid() const;

    OAIShared_Text_Details getParentText() const;
    void setParentText(const OAIShared_Text_Details &parent_text);
    bool is_parent_text_Set() const;
    bool is_parent_text_Valid() const;

    QString getParentTextId() const;
    void setParentTextId(const QString &parent_text_id);
    bool is_parent_text_id_Set() const;
    bool is_parent_text_id_Valid() const;

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

    OAIShared_ColorTransformations_Details m_color_transformations;
    bool m_color_transformations_isSet;
    bool m_color_transformations_isValid;

    qint32 m_color_type_id;
    bool m_color_type_id_isSet;
    bool m_color_type_id_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    QString m_fill_map_id;
    bool m_fill_map_id_isSet;
    bool m_fill_map_id_isValid;

    QString m_hex_value;
    bool m_hex_value_isSet;
    bool m_hex_value_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_user_color;
    bool m_is_user_color_isSet;
    bool m_is_user_color_isValid;

    OAIShared_FillMap_Details m_parent_fill_map;
    bool m_parent_fill_map_isSet;
    bool m_parent_fill_map_isValid;

    OAIShared_GradientStops_Details m_parent_gradient_stop;
    bool m_parent_gradient_stop_isSet;
    bool m_parent_gradient_stop_isValid;

    QString m_parent_gradient_stop_id;
    bool m_parent_gradient_stop_id_isSet;
    bool m_parent_gradient_stop_id_isValid;

    OAIShared_Lines_Details m_parent_line;
    bool m_parent_line_isSet;
    bool m_parent_line_isValid;

    QString m_parent_line_id;
    bool m_parent_line_id_isSet;
    bool m_parent_line_id_isValid;

    OAIShared_Text_Details m_parent_text;
    bool m_parent_text_isSet;
    bool m_parent_text_isValid;

    QString m_parent_text_id;
    bool m_parent_text_id_isSet;
    bool m_parent_text_id_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIShared_SolidFills_Details)

#endif // OAIShared_SolidFills_Details_H
