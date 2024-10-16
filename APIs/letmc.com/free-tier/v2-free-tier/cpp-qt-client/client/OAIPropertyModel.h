/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPropertyModel.h
 *
 * Stores the &#39;Sales&#39; type fields for property ownable as a stepping stone to a full on BO when we finally get the go ahead to write sales!!
 */

#ifndef OAIPropertyModel_H
#define OAIPropertyModel_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPropertyModel : public OAIObject {
public:
    OAIPropertyModel();
    OAIPropertyModel(QString json);
    ~OAIPropertyModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArea() const;
    void setArea(const QString &area);
    bool is_area_Set() const;
    bool is_area_Valid() const;

    QString getBranch() const;
    void setBranch(const QString &branch);
    bool is_branch_Set() const;
    bool is_branch_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getETag() const;
    void setETag(const QString &e_tag);
    bool is_e_tag_Set() const;
    bool is_e_tag_Valid() const;

    QString getFullAddress() const;
    void setFullAddress(const QString &full_address);
    bool is_full_address_Set() const;
    bool is_full_address_Valid() const;

    QString getGlobalReference() const;
    void setGlobalReference(const QString &global_reference);
    bool is_global_reference_Set() const;
    bool is_global_reference_Valid() const;

    QString getMainPhoto() const;
    void setMainPhoto(const QString &main_photo);
    bool is_main_photo_Set() const;
    bool is_main_photo_Valid() const;

    QString getManagedByStaff() const;
    void setManagedByStaff(const QString &managed_by_staff);
    bool is_managed_by_staff_Set() const;
    bool is_managed_by_staff_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    QString getPropertySource() const;
    void setPropertySource(const QString &property_source);
    bool is_property_source_Set() const;
    bool is_property_source_Valid() const;

    QString getPropertyType() const;
    void setPropertyType(const QString &property_type);
    bool is_property_type_Set() const;
    bool is_property_type_Valid() const;

    QString getRoomName() const;
    void setRoomName(const QString &room_name);
    bool is_room_name_Set() const;
    bool is_room_name_Valid() const;

    QString getVideoUrl() const;
    void setVideoUrl(const QString &video_url);
    bool is_video_url_Set() const;
    bool is_video_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_area;
    bool m_area_isSet;
    bool m_area_isValid;

    QString m_branch;
    bool m_branch_isSet;
    bool m_branch_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_e_tag;
    bool m_e_tag_isSet;
    bool m_e_tag_isValid;

    QString m_full_address;
    bool m_full_address_isSet;
    bool m_full_address_isValid;

    QString m_global_reference;
    bool m_global_reference_isSet;
    bool m_global_reference_isValid;

    QString m_main_photo;
    bool m_main_photo_isSet;
    bool m_main_photo_isValid;

    QString m_managed_by_staff;
    bool m_managed_by_staff_isSet;
    bool m_managed_by_staff_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;

    QString m_property_source;
    bool m_property_source_isSet;
    bool m_property_source_isValid;

    QString m_property_type;
    bool m_property_type_isSet;
    bool m_property_type_isValid;

    QString m_room_name;
    bool m_room_name_isSet;
    bool m_room_name_isValid;

    QString m_video_url;
    bool m_video_url_isSet;
    bool m_video_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPropertyModel)

#endif // OAIPropertyModel_H
