/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILandlordPhotoModel.h
 *
 * Stores a photo related to a property structure.
 */

#ifndef OAILandlordPhotoModel_H
#define OAILandlordPhotoModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILandlordPhotoModel : public OAIObject {
public:
    OAILandlordPhotoModel();
    OAILandlordPhotoModel(QString json);
    ~OAILandlordPhotoModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getFileName() const;
    void setFileName(const QString &file_name);
    bool is_file_name_Set() const;
    bool is_file_name_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    QString getPhotoType() const;
    void setPhotoType(const QString &photo_type);
    bool is_photo_type_Set() const;
    bool is_photo_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_file_name;
    bool m_file_name_isSet;
    bool m_file_name_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    QString m_photo_type;
    bool m_photo_type_isSet;
    bool m_photo_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILandlordPhotoModel)

#endif // OAILandlordPhotoModel_H
