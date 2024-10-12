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
 * OAISlide_SmartArts_Details.h
 *
 * 
 */

#ifndef OAISlide_SmartArts_Details_H
#define OAISlide_SmartArts_Details_H

#include <QJsonObject>

#include "OAISlide_Graphics_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISlide_Graphics_Details;

class OAISlide_SmartArts_Details : public OAIObject {
public:
    OAISlide_SmartArts_Details();
    OAISlide_SmartArts_Details(QString json);
    ~OAISlide_SmartArts_Details() override;

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

    QString getGraphicsId() const;
    void setGraphicsId(const QString &graphics_id);
    bool is_graphics_id_Set() const;
    bool is_graphics_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPackageUri() const;
    void setPackageUri(const QString &package_uri);
    bool is_package_uri_Set() const;
    bool is_package_uri_Valid() const;

    OAISlide_Graphics_Details getParentGraphic() const;
    void setParentGraphic(const OAISlide_Graphics_Details &parent_graphic);
    bool is_parent_graphic_Set() const;
    bool is_parent_graphic_Valid() const;

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

    QString m_graphics_id;
    bool m_graphics_id_isSet;
    bool m_graphics_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_package_uri;
    bool m_package_uri_isSet;
    bool m_package_uri_isValid;

    OAISlide_Graphics_Details m_parent_graphic;
    bool m_parent_graphic_isSet;
    bool m_parent_graphic_isValid;

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

Q_DECLARE_METATYPE(OpenAPI::OAISlide_SmartArts_Details)

#endif // OAISlide_SmartArts_Details_H
