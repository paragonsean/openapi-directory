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
 * OAIDocument.h
 *
 * 
 */

#ifndef OAIDocument_H
#define OAIDocument_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDocument : public OAIObject {
public:
    OAIDocument();
    OAIDocument(QString json);
    ~OAIDocument() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseElementBlobUrl() const;
    void setBaseElementBlobUrl(const QString &base_element_blob_url);
    bool is_base_element_blob_url_Set() const;
    bool is_base_element_blob_url_Valid() const;

    QString getBlobLocation() const;
    void setBlobLocation(const QString &blob_location);
    bool is_blob_location_Set() const;
    bool is_blob_location_Valid() const;

    QString getChangedBaseElementBlobUrl() const;
    void setChangedBaseElementBlobUrl(const QString &changed_base_element_blob_url);
    bool is_changed_base_element_blob_url_Set() const;
    bool is_changed_base_element_blob_url_Valid() const;

    qint32 getDocumentTypeId() const;
    void setDocumentTypeId(const qint32 &document_type_id);
    bool is_document_type_id_Set() const;
    bool is_document_type_id_Valid() const;

    QString getFilename() const;
    void setFilename(const QString &filename);
    bool is_filename_Set() const;
    bool is_filename_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getOwnerGuid() const;
    void setOwnerGuid(const QString &owner_guid);
    bool is_owner_guid_Set() const;
    bool is_owner_guid_Valid() const;

    QString getPackageUri() const;
    void setPackageUri(const QString &package_uri);
    bool is_package_uri_Set() const;
    bool is_package_uri_Valid() const;

    QString getStoryId() const;
    void setStoryId(const QString &story_id);
    bool is_story_id_Set() const;
    bool is_story_id_Valid() const;

    QString getTableStylesXmlBlobUrl() const;
    void setTableStylesXmlBlobUrl(const QString &table_styles_xml_blob_url);
    bool is_table_styles_xml_blob_url_Set() const;
    bool is_table_styles_xml_blob_url_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_base_element_blob_url;
    bool m_base_element_blob_url_isSet;
    bool m_base_element_blob_url_isValid;

    QString m_blob_location;
    bool m_blob_location_isSet;
    bool m_blob_location_isValid;

    QString m_changed_base_element_blob_url;
    bool m_changed_base_element_blob_url_isSet;
    bool m_changed_base_element_blob_url_isValid;

    qint32 m_document_type_id;
    bool m_document_type_id_isSet;
    bool m_document_type_id_isValid;

    QString m_filename;
    bool m_filename_isSet;
    bool m_filename_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_owner_guid;
    bool m_owner_guid_isSet;
    bool m_owner_guid_isValid;

    QString m_package_uri;
    bool m_package_uri_isSet;
    bool m_package_uri_isValid;

    QString m_story_id;
    bool m_story_id_isSet;
    bool m_story_id_isValid;

    QString m_table_styles_xml_blob_url;
    bool m_table_styles_xml_blob_url_isSet;
    bool m_table_styles_xml_blob_url_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDocument)

#endif // OAIDocument_H
