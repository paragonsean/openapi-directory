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
 * OAISlide_Connector_Details.h
 *
 * 
 */

#ifndef OAISlide_Connector_Details_H
#define OAISlide_Connector_Details_H

#include <QJsonObject>

#include "OAIShared_Effects_Details.h"
#include "OAIShared_FillMap_Details.h"
#include "OAIShared_Lines_Details.h"
#include "OAISlide_GroupElements_Details.h"
#include "OAISlide_Shapes_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIShared_Effects_Details;
class OAISlide_Shapes_Details;
class OAIShared_FillMap_Details;
class OAISlide_GroupElements_Details;
class OAIShared_Lines_Details;

class OAISlide_Connector_Details : public OAIObject {
public:
    OAISlide_Connector_Details();
    OAISlide_Connector_Details(QString json);
    ~OAISlide_Connector_Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseElementBlobUrl() const;
    void setBaseElementBlobUrl(const QString &base_element_blob_url);
    bool is_base_element_blob_url_Set() const;
    bool is_base_element_blob_url_Valid() const;

    QString getChangedBaseElementBlobUrl() const;
    void setChangedBaseElementBlobUrl(const QString &changed_base_element_blob_url);
    bool is_changed_base_element_blob_url_Set() const;
    bool is_changed_base_element_blob_url_Valid() const;

    QDateTime getDateCreated() const;
    void setDateCreated(const QDateTime &date_created);
    bool is_date_created_Set() const;
    bool is_date_created_Valid() const;

    QDateTime getDateModified() const;
    void setDateModified(const QDateTime &date_modified);
    bool is_date_modified_Set() const;
    bool is_date_modified_Valid() const;

    OAIShared_Effects_Details getEffect() const;
    void setEffect(const OAIShared_Effects_Details &effect);
    bool is_effect_Set() const;
    bool is_effect_Valid() const;

    qint32 getEndConnectionIdx() const;
    void setEndConnectionIdx(const qint32 &end_connection_idx);
    bool is_end_connection_idx_Set() const;
    bool is_end_connection_idx_Valid() const;

    OAISlide_Shapes_Details getEndConnectionShape() const;
    void setEndConnectionShape(const OAISlide_Shapes_Details &end_connection_shape);
    bool is_end_connection_shape_Set() const;
    bool is_end_connection_shape_Valid() const;

    QString getEndConnectionShapeId() const;
    void setEndConnectionShapeId(const QString &end_connection_shape_id);
    bool is_end_connection_shape_id_Set() const;
    bool is_end_connection_shape_id_Valid() const;

    OAIShared_FillMap_Details getFillMap() const;
    void setFillMap(const OAIShared_FillMap_Details &fill_map);
    bool is_fill_map_Set() const;
    bool is_fill_map_Valid() const;

    bool isFlipHorizontal() const;
    void setFlipHorizontal(const bool &flip_horizontal);
    bool is_flip_horizontal_Set() const;
    bool is_flip_horizontal_Valid() const;

    bool isFlipVertical() const;
    void setFlipVertical(const bool &flip_vertical);
    bool is_flip_vertical_Set() const;
    bool is_flip_vertical_Valid() const;

    QString getFreeFormPathXml() const;
    void setFreeFormPathXml(const QString &free_form_path_xml);
    bool is_free_form_path_xml_Set() const;
    bool is_free_form_path_xml_Valid() const;

    OAISlide_GroupElements_Details getGroupElement() const;
    void setGroupElement(const OAISlide_GroupElements_Details &group_element);
    bool is_group_element_Set() const;
    bool is_group_element_Valid() const;

    QString getGroupElementsId() const;
    void setGroupElementsId(const QString &group_elements_id);
    bool is_group_elements_id_Set() const;
    bool is_group_elements_id_Valid() const;

    bool isHidden() const;
    void setHidden(const bool &hidden);
    bool is_hidden_Set() const;
    bool is_hidden_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsThemeEffect() const;
    void setIsThemeEffect(const bool &is_theme_effect);
    bool is_is_theme_effect_Set() const;
    bool is_is_theme_effect_Valid() const;

    bool isIsThemeFill() const;
    void setIsThemeFill(const bool &is_theme_fill);
    bool is_is_theme_fill_Set() const;
    bool is_is_theme_fill_Valid() const;

    bool isIsThemeLine() const;
    void setIsThemeLine(const bool &is_theme_line);
    bool is_is_theme_line_Set() const;
    bool is_is_theme_line_Valid() const;

    OAIShared_Lines_Details getLine() const;
    void setLine(const OAIShared_Lines_Details &line);
    bool is_line_Set() const;
    bool is_line_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getOoxmlId() const;
    void setOoxmlId(const qint32 &ooxml_id);
    bool is_ooxml_id_Set() const;
    bool is_ooxml_id_Valid() const;

    QString getPackageUri() const;
    void setPackageUri(const QString &package_uri);
    bool is_package_uri_Set() const;
    bool is_package_uri_Valid() const;

    QString getPresetTypeId() const;
    void setPresetTypeId(const QString &preset_type_id);
    bool is_preset_type_id_Set() const;
    bool is_preset_type_id_Valid() const;

    qint32 getRotation() const;
    void setRotation(const qint32 &rotation);
    bool is_rotation_Set() const;
    bool is_rotation_Valid() const;

    qint32 getStartConnectionIdx() const;
    void setStartConnectionIdx(const qint32 &start_connection_idx);
    bool is_start_connection_idx_Set() const;
    bool is_start_connection_idx_Valid() const;

    OAISlide_Shapes_Details getStartConnectionShape() const;
    void setStartConnectionShape(const OAISlide_Shapes_Details &start_connection_shape);
    bool is_start_connection_shape_Set() const;
    bool is_start_connection_shape_Valid() const;

    QString getStartConnectionShapeId() const;
    void setStartConnectionShapeId(const QString &start_connection_shape_id);
    bool is_start_connection_shape_id_Set() const;
    bool is_start_connection_shape_id_Valid() const;

    QString getSvgBlobUrl() const;
    void setSvgBlobUrl(const QString &svg_blob_url);
    bool is_svg_blob_url_Set() const;
    bool is_svg_blob_url_Valid() const;

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

    QString m_base_element_blob_url;
    bool m_base_element_blob_url_isSet;
    bool m_base_element_blob_url_isValid;

    QString m_changed_base_element_blob_url;
    bool m_changed_base_element_blob_url_isSet;
    bool m_changed_base_element_blob_url_isValid;

    QDateTime m_date_created;
    bool m_date_created_isSet;
    bool m_date_created_isValid;

    QDateTime m_date_modified;
    bool m_date_modified_isSet;
    bool m_date_modified_isValid;

    OAIShared_Effects_Details m_effect;
    bool m_effect_isSet;
    bool m_effect_isValid;

    qint32 m_end_connection_idx;
    bool m_end_connection_idx_isSet;
    bool m_end_connection_idx_isValid;

    OAISlide_Shapes_Details m_end_connection_shape;
    bool m_end_connection_shape_isSet;
    bool m_end_connection_shape_isValid;

    QString m_end_connection_shape_id;
    bool m_end_connection_shape_id_isSet;
    bool m_end_connection_shape_id_isValid;

    OAIShared_FillMap_Details m_fill_map;
    bool m_fill_map_isSet;
    bool m_fill_map_isValid;

    bool m_flip_horizontal;
    bool m_flip_horizontal_isSet;
    bool m_flip_horizontal_isValid;

    bool m_flip_vertical;
    bool m_flip_vertical_isSet;
    bool m_flip_vertical_isValid;

    QString m_free_form_path_xml;
    bool m_free_form_path_xml_isSet;
    bool m_free_form_path_xml_isValid;

    OAISlide_GroupElements_Details m_group_element;
    bool m_group_element_isSet;
    bool m_group_element_isValid;

    QString m_group_elements_id;
    bool m_group_elements_id_isSet;
    bool m_group_elements_id_isValid;

    bool m_hidden;
    bool m_hidden_isSet;
    bool m_hidden_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_theme_effect;
    bool m_is_theme_effect_isSet;
    bool m_is_theme_effect_isValid;

    bool m_is_theme_fill;
    bool m_is_theme_fill_isSet;
    bool m_is_theme_fill_isValid;

    bool m_is_theme_line;
    bool m_is_theme_line_isSet;
    bool m_is_theme_line_isValid;

    OAIShared_Lines_Details m_line;
    bool m_line_isSet;
    bool m_line_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_ooxml_id;
    bool m_ooxml_id_isSet;
    bool m_ooxml_id_isValid;

    QString m_package_uri;
    bool m_package_uri_isSet;
    bool m_package_uri_isValid;

    QString m_preset_type_id;
    bool m_preset_type_id_isSet;
    bool m_preset_type_id_isValid;

    qint32 m_rotation;
    bool m_rotation_isSet;
    bool m_rotation_isValid;

    qint32 m_start_connection_idx;
    bool m_start_connection_idx_isSet;
    bool m_start_connection_idx_isValid;

    OAISlide_Shapes_Details m_start_connection_shape;
    bool m_start_connection_shape_isSet;
    bool m_start_connection_shape_isValid;

    QString m_start_connection_shape_id;
    bool m_start_connection_shape_id_isSet;
    bool m_start_connection_shape_id_isValid;

    QString m_svg_blob_url;
    bool m_svg_blob_url_isSet;
    bool m_svg_blob_url_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISlide_Connector_Details)

#endif // OAISlide_Connector_Details_H
