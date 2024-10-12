/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImage.h
 *
 * 
 */

#ifndef OAIImage_H
#define OAIImage_H

#include <QJsonObject>

#include "OAIA2CDateTime.h"
#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIA2CDateTime;

class OAIImage : public OAIObject {
public:
    OAIImage();
    OAIImage(QString json);
    ~OAIImage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIObject getAdditionalFields() const;
    void setAdditionalFields(const OAIObject &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getAlt() const;
    void setAlt(const QString &alt);
    bool is_alt_Set() const;
    bool is_alt_Valid() const;

    bool isAvail() const;
    void setAvail(const bool &avail);
    bool is_avail_Set() const;
    bool is_avail_Valid() const;

    OAIA2CDateTime getCreateAt() const;
    void setCreateAt(const OAIA2CDateTime &create_at);
    bool is_create_at_Set() const;
    bool is_create_at_Valid() const;

    OAIObject getCustomFields() const;
    void setCustomFields(const OAIObject &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getFileName() const;
    void setFileName(const QString &file_name);
    bool is_file_name_Set() const;
    bool is_file_name_Valid() const;

    QString getHttpPath() const;
    void setHttpPath(const QString &http_path);
    bool is_http_path_Set() const;
    bool is_http_path_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getMimeType() const;
    void setMimeType(const QString &mime_type);
    bool is_mime_type_Set() const;
    bool is_mime_type_Valid() const;

    OAIA2CDateTime getModifiedAt() const;
    void setModifiedAt(const OAIA2CDateTime &modified_at);
    bool is_modified_at_Set() const;
    bool is_modified_at_Valid() const;

    qint32 getSize() const;
    void setSize(const qint32 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    qint32 getSortOrder() const;
    void setSortOrder(const qint32 &sort_order);
    bool is_sort_order_Set() const;
    bool is_sort_order_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIObject m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_alt;
    bool m_alt_isSet;
    bool m_alt_isValid;

    bool m_avail;
    bool m_avail_isSet;
    bool m_avail_isValid;

    OAIA2CDateTime m_create_at;
    bool m_create_at_isSet;
    bool m_create_at_isValid;

    OAIObject m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_file_name;
    bool m_file_name_isSet;
    bool m_file_name_isValid;

    QString m_http_path;
    bool m_http_path_isSet;
    bool m_http_path_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_mime_type;
    bool m_mime_type_isSet;
    bool m_mime_type_isValid;

    OAIA2CDateTime m_modified_at;
    bool m_modified_at_isSet;
    bool m_modified_at_isValid;

    qint32 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    qint32 m_sort_order;
    bool m_sort_order_isSet;
    bool m_sort_order_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImage)

#endif // OAIImage_H
