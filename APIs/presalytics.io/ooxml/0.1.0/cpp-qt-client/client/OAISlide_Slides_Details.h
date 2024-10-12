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
 * OAISlide_Slides_Details.h
 *
 * 
 */

#ifndef OAISlide_Slides_Details_H
#define OAISlide_Slides_Details_H

#include <QJsonObject>

#include "OAIDocument_Details.h"
#include "OAISlide_ShapeTrees_Details.h"
#include "OAISlide_SlideMasters_Details.h"
#include "OAITheme_Themes_Details.h"
#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDocument_Details;
class OAISlide_ShapeTrees_Details;
class OAISlide_SlideMasters_Details;
class OAITheme_Themes_Details;

class OAISlide_Slides_Details : public OAIObject {
public:
    OAISlide_Slides_Details();
    OAISlide_Slides_Details(QString json);
    ~OAISlide_Slides_Details() override;

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

    OAIDocument_Details getDocument() const;
    void setDocument(const OAIDocument_Details &document);
    bool is_document_Set() const;
    bool is_document_Valid() const;

    QString getDocumentId() const;
    void setDocumentId(const QString &document_id);
    bool is_document_id_Set() const;
    bool is_document_id_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    qint32 getOoxmlId() const;
    void setOoxmlId(const qint32 &ooxml_id);
    bool is_ooxml_id_Set() const;
    bool is_ooxml_id_Valid() const;

    QString getPackageUri() const;
    void setPackageUri(const QString &package_uri);
    bool is_package_uri_Set() const;
    bool is_package_uri_Valid() const;

    OAISlide_ShapeTrees_Details getShapeTree() const;
    void setShapeTree(const OAISlide_ShapeTrees_Details &shape_tree);
    bool is_shape_tree_Set() const;
    bool is_shape_tree_Valid() const;

    QString getSlideDocumentUrl() const;
    void setSlideDocumentUrl(const QString &slide_document_url);
    bool is_slide_document_url_Set() const;
    bool is_slide_document_url_Valid() const;

    OAISlide_SlideMasters_Details getSlideMaster() const;
    void setSlideMaster(const OAISlide_SlideMasters_Details &slide_master);
    bool is_slide_master_Set() const;
    bool is_slide_master_Valid() const;

    QString getSvgBlobUrl() const;
    void setSvgBlobUrl(const QString &svg_blob_url);
    bool is_svg_blob_url_Set() const;
    bool is_svg_blob_url_Valid() const;

    OAITheme_Themes_Details getTheme() const;
    void setTheme(const OAITheme_Themes_Details &theme);
    bool is_theme_Set() const;
    bool is_theme_Valid() const;

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

    OAIDocument_Details m_document;
    bool m_document_isSet;
    bool m_document_isValid;

    QString m_document_id;
    bool m_document_id_isSet;
    bool m_document_id_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    qint32 m_ooxml_id;
    bool m_ooxml_id_isSet;
    bool m_ooxml_id_isValid;

    QString m_package_uri;
    bool m_package_uri_isSet;
    bool m_package_uri_isValid;

    OAISlide_ShapeTrees_Details m_shape_tree;
    bool m_shape_tree_isSet;
    bool m_shape_tree_isValid;

    QString m_slide_document_url;
    bool m_slide_document_url_isSet;
    bool m_slide_document_url_isValid;

    OAISlide_SlideMasters_Details m_slide_master;
    bool m_slide_master_isSet;
    bool m_slide_master_isValid;

    QString m_svg_blob_url;
    bool m_svg_blob_url_isSet;
    bool m_svg_blob_url_isValid;

    OAITheme_Themes_Details m_theme;
    bool m_theme_isSet;
    bool m_theme_isValid;

    QString m_user_created;
    bool m_user_created_isSet;
    bool m_user_created_isValid;

    QString m_user_modified;
    bool m_user_modified_isSet;
    bool m_user_modified_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISlide_Slides_Details)

#endif // OAISlide_Slides_Details_H
